#!/usr/bin/env python3
"""
dbd_archive.py -- focused scraper for the Dead by Daylight knowledge base.

Archives BHVR's Dead by Daylight Patch Notes and Developer Updates as Markdown,
downloading every in-body image alongside each article. Stdlib only, so the
result stays runnable long after the source disappears.

Usage:
    python3 dbd_archive.py                    # archive everything
    python3 dbd_archive.py --section live     # one section
    python3 dbd_archive.py --dry-run          # report sizes, write nothing
    python3 dbd_archive.py --force            # ignore the manifest, redo all
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import html
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

API = "https://forums.bhvr.com/api/v2"
USER_AGENT = "dbd-bug-archive/1.0 (+https://github.com/Ephellon/dbd-bug-archive)"

# Knowledge-base categories to archive: slug -> (knowledgeCategoryID, title)
SECTIONS = {
    "live":                    (20, "Live"),
    "player-test-build":       (9,  "Player Test Build (PTB)"),
    "archive-steam":           (4,  "Archive: Steam"),
    "archive-ps4":             (3,  "Archive: PS4"),
    "archive-xbox-one":        (5,  "Archive: Xbox One"),
    "archive-nintendo-switch": (6,  "Archive: Nintendo Switch"),
    "archive-windows-store":   (7,  "Archive: Windows Store"),
    "archive-stadia":          (19, "Archive: Stadia"),
    "developer-updates":       (29, "Developer Updates"),
}

# Every image is stored once, under its content hash, and referenced from each
# article that uses it. The dividers alone repeat across hundreds of pages.
IMAGE_DIR = "images"


# Where each section's Markdown lands, relative to the output root.
def section_dir(slug: str) -> str:
    return slug if slug == "developer-updates" else os.path.join("patch-notes", slug)


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #

class Fetcher:
    def __init__(self, delay: float = 1.0, retries: int = 4, timeout: int = 60):
        self.delay = delay
        self.retries = retries
        self.timeout = timeout
        self._last = 0.0

    def _throttle(self) -> None:
        wait = self.delay - (time.monotonic() - self._last)
        if wait > 0:
            time.sleep(wait)
        self._last = time.monotonic()

    def get(self, url: str) -> bytes:
        last_err: Exception | None = None
        for attempt in range(self.retries):
            self._throttle()
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    return resp.read()
            except urllib.error.HTTPError as err:
                # 4xx other than 429 will not get better by retrying.
                if err.code != 429 and 400 <= err.code < 500:
                    raise
                last_err = err
            except Exception as err:  # noqa: BLE001 - network is network
                last_err = err
            time.sleep(2 ** (attempt + 1))
        raise RuntimeError(f"giving up on {url}: {last_err}")

    def get_json(self, url: str):
        return json.loads(self.get(url).decode("utf-8"))


# --------------------------------------------------------------------------- #
# Tiny DOM
# --------------------------------------------------------------------------- #

VOID = {"br", "hr", "img", "input", "meta", "link", "source", "wbr"}


class Node:
    __slots__ = ("tag", "attrs", "children", "text", "parent")

    def __init__(self, tag: str | None, attrs: dict | None = None, text: str = ""):
        self.tag = tag              # None => text node
        self.attrs = attrs or {}
        self.children: list["Node"] = []
        self.text = text
        self.parent: "Node | None" = None

    def add(self, node: "Node") -> "Node":
        node.parent = self
        self.children.append(node)
        return node


class DOMBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs))
        self.stack[-1].add(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].add(Node(tag, dict(attrs)))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return
        # Stray close tag: ignore.

    def handle_data(self, data):
        self.stack[-1].add(Node(None, text=data))


def parse_html(fragment: str) -> Node:
    builder = DOMBuilder()
    builder.feed(fragment)
    builder.close()
    return builder.root


# --------------------------------------------------------------------------- #
# HTML -> Markdown
# --------------------------------------------------------------------------- #

BLOCK_TAGS = {
    "p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li",
    "blockquote", "pre", "hr", "table", "tr", "section", "article", "figure",
}
INLINE_PASSTHROUGH = {"span", "font", "small", "abbr", "label", "figcaption", "center"}
# Interface chrome that carries no article content.
DROP_TAGS = {"script", "style", "noscript", "svg", "path", "title", "button",
             "input", "select", "textarea", "head", "meta", "link"}


def classes(node: "Node") -> set[str]:
    return set((node.attrs.get("class") or "").split())

_WS = re.compile(r"[ \t\r\f\v\u00a0\u2007\u202f]+")
_MD_ESCAPE = re.compile(r"(?<!\\)([*_`\[\]])")

# Tags whose Markdown output is wrapped in a symmetric emphasis marker.
EMPHASIS = {"strong": "**", "b": "**", "em": "*", "i": "*",
            "del": "~~", "s": "~~", "strike": "~~"}


def unwrap_leaving(url: str) -> str:
    """BHVR wraps outbound links in /home/leaving?target=<encoded>."""
    if "/home/leaving" not in url:
        return url
    query = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
    return query.get("target", [url])[0]


class MarkdownWriter:
    """Renders a Node tree to Markdown, collecting image references as it goes."""

    def __init__(self, on_image):
        self.on_image = on_image          # (src, alt) -> markdown replacement path
        self.unknown_tags: set[str] = set()

    # -- inline ------------------------------------------------------------ #

    def inline(self, node: Node) -> str:
        out: list[str] = []
        marks: list[str | None] = []
        for child in node.children:
            piece = self._inline_node(child)
            mark = EMPHASIS.get(child.tag) if child.tag else None
            if piece and mark and out and marks[-1]:
                # <em>a</em><em>b</em> would emit *a**b*, which reads as a
                # stray bold. Fuse the touching runs instead.
                for candidate in ("**", "*", "~~"):
                    if out[-1].endswith(candidate) and piece.startswith(candidate):
                        out[-1] = out[-1][: -len(candidate)]
                        piece = piece[len(candidate):]
                        break
            out.append(piece)
            marks.append(mark)
        return "".join(out)

    def _inline_node(self, node: Node) -> str:
        if node.tag is None:
            return _MD_ESCAPE.sub(r"\\\1", _WS.sub(" ", node.text.replace("\n", " ")))

        tag = node.tag
        if tag in DROP_TAGS:
            return ""
        if tag in ("strong", "b"):
            return self._emphasise(node, "**")
        if tag in ("em", "i"):
            return self._emphasise(node, "*")
        if tag in ("del", "s", "strike"):
            return self._emphasise(node, "~~")
        if tag == "code":
            return f"`{self.plain(node)}`"
        if tag == "br":
            return "  \n"
        if tag == "img":
            return self._image(node)
        if tag == "a":
            # An anchor wrapping nothing but an image is a lightbox link: drop it.
            elements = [c for c in node.children if c.tag or c.text.strip()]
            if len(elements) == 1 and elements[0].tag == "img":
                return self._image(elements[0])
            inner = self.inline(node).strip()
            href = unwrap_leaving(node.attrs.get("href", "")).strip()
            if not inner:
                return ""
            if not href:
                return inner
            return f"[{inner}]({href})"
        if tag in INLINE_PASSTHROUGH:
            return self.inline(node)
        if tag in BLOCK_TAGS:
            # A block nested where we expected inline content; render it flat.
            return self.inline(node)
        self.unknown_tags.add(tag)
        return self.inline(node)

    def _emphasise(self, node: Node, mark: str) -> str:
        """Wrap in `mark`, keeping any surrounding space outside the markers.

        Markdown ignores `** x **`, so the space an author put inside the tag
        has to move out or the emphasised word collides with its neighbour.
        """
        inner = self.inline(node)
        core = inner.strip()
        if not core:
            return " " if inner else ""
        if not re.search(r"\w", core):
            # <em>. </em> and friends: emphasis on bare punctuation renders as
            # literal asterisks, because the markers are not left-flanking.
            return inner
        lead = " " if inner[:1].isspace() else ""
        trail = " " if inner[-1:].isspace() else ""
        return f"{lead}{mark}{core}{mark}{trail}"

    def _image(self, node: Node) -> str:
        src = node.attrs.get("src", "").strip()
        if not src:
            return ""
        alt = node.attrs.get("alt", "").strip()
        path = self.on_image(src, alt)
        return f"![{alt}]({path})"

    def plain(self, node: Node) -> str:
        if node.tag is None:
            return node.text
        return "".join(self.plain(c) for c in node.children)

    # -- block -------------------------------------------------------------- #

    def render(self, node: Node, indent: str = "") -> list[str]:
        """Returns a list of Markdown blocks."""
        blocks: list[str] = []
        pending: list[Node] = []

        def flush() -> None:
            if not pending:
                return
            holder = Node("#inline")
            holder.children = pending[:]
            text = re.sub(r" {2,}(?=\S)", " ", self.inline(holder)).strip()
            pending.clear()
            if text:
                blocks.append(indent + text)

        for child in node.children:
            if child.tag is None:
                if child.text.strip() or pending:
                    pending.append(child)
                continue
            if child.tag in DROP_TAGS:
                continue
            if child.tag in BLOCK_TAGS:
                flush()
                blocks.extend(self._block(child, indent))
            else:
                pending.append(child)
        flush()
        return blocks

    def _block(self, node: Node, indent: str) -> list[str]:
        tag = node.tag
        if tag in DROP_TAGS:
            return []
        node_classes = classes(node)
        if "spoiler-buttonContainer" in node_classes:
            return []
        if "blockquote" in node_classes:
            inner = "\n\n".join(self.render(node, ""))
            if not inner.strip():
                return []
            return ["\n".join(f"{indent}> {line}".rstrip()
                               for line in inner.split("\n"))]
        if "spoiler" in node_classes:
            inner = "\n\n".join(self.render(node, ""))
            if not inner.strip():
                return []
            body = "\n".join(indent + ln if ln else "" for ln in inner.split("\n"))
            return [f"{indent}<details>\n{indent}<summary>Spoiler</summary>\n\n"
                    f"{body}\n\n{indent}</details>"]
        if tag == "hr":
            return [indent + "---"]
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            # A heading wrapped entirely in <strong> is presentation, so unwrap
            # it. Emphasis on only PART of a heading is content, and must stay:
            # <h3><strong>N</strong>ew Map</h3> is not a wrapped heading.
            target = node
            while True:
                kids = [c for c in target.children if c.tag or c.text.strip()]
                if len(kids) == 1 and kids[0].tag in ("strong", "b", "em", "i"):
                    target = kids[0]
                    continue
                break
            text = self.inline(target).strip()
            return [f"{indent}{'#' * level} {text}"] if text else []
        if tag in ("ul", "ol"):
            return self._list(node, indent)
        if tag == "blockquote":
            inner = self.render(node, "")
            body = "\n\n".join(inner)
            return [
                "\n".join(f"{indent}> {line}".rstrip() for line in body.split("\n"))
            ] if body else []
        if tag == "pre":
            code = self.plain(node).strip("\n")
            return [f"{indent}```\n{code}\n{indent}```"] if code.strip() else []
        if tag == "table":
            return self._table(node, indent)
        if tag in ("p", "div", "section", "article", "figure", "li", "tr"):
            return self.render(node, indent)
        self.unknown_tags.add(tag)
        return self.render(node, indent)

    def _list(self, node: Node, indent: str) -> list[str]:
        ordered = node.tag == "ol"
        lines: list[str] = []
        number = 0
        for item in node.children:
            if item.tag != "li":
                continue
            number += 1
            marker = f"{number}. " if ordered else "- "
            child_indent = indent + " " * len(marker)
            blocks = self.render(item, "")
            if not blocks:
                continue
            first, *rest = blocks
            first_lines = first.split("\n")
            lines.append(indent + marker + first_lines[0])
            lines.extend(child_indent + ln for ln in first_lines[1:])
            for block in rest:
                # Nested lists hug the parent bullet; other blocks get a blank line.
                if not block.lstrip().startswith(("- ", "1. ")):
                    lines.append("")
                for ln in block.split("\n"):
                    lines.append(child_indent + ln if ln else "")
        return ["\n".join(lines)] if lines else []

    def _table(self, node: Node, indent: str) -> list[str]:
        rows: list[list[str]] = []
        header = False
        for tr in _descendants(node, "tr"):
            cells = []
            for cell in tr.children:
                if cell.tag in ("td", "th"):
                    if cell.tag == "th" and not rows:
                        header = True
                    cells.append(self.inline(cell).strip().replace("|", "\\|") or " ")
            if cells:
                rows.append(cells)
        if not rows:
            return []
        width = max(len(r) for r in rows)
        rows = [r + [" "] * (width - len(r)) for r in rows]
        if not header:
            rows.insert(0, [" "] * width)
        out = ["| " + " | ".join(rows[0]) + " |",
               "| " + " | ".join(["---"] * width) + " |"]
        out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
        return [indent + ("\n" + indent).join(out)]


def _descendants(node: Node, tag: str):
    for child in node.children:
        if child.tag == tag:
            yield child
        else:
            yield from _descendants(child, tag)


def to_markdown(body_html: str, on_image) -> tuple[str, set[str]]:
    writer = MarkdownWriter(on_image)
    blocks = writer.render(parse_html(body_html))
    text = "\n\n".join(b for b in blocks if b.strip())
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n", writer.unknown_tags


# --------------------------------------------------------------------------- #
# Archiving
# --------------------------------------------------------------------------- #

def slugify(value: str) -> str:
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-") or "untitled"


def yaml_quote(value) -> str:
    if value is None:
        return '""'
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


class Archiver:
    def __init__(self, root: str, fetcher: Fetcher, dry_run: bool = False,
                 force: bool = False, rerender: bool = False):
        self.root = root
        self.fetcher = fetcher
        self.dry_run = dry_run
        self.force = force
        self.rerender = rerender
        self.manifest_path = os.path.join(root, "manifest.json")
        self.manifest = self._load_manifest()
        self.by_url = self._index_images()
        self.stats = {"articles": 0, "updated": 0, "skipped": 0, "images": 0,
                      "image_bytes": 0, "reused": 0, "deduped": 0}
        self.unknown_tags: set[str] = set()

    def _load_manifest(self) -> dict:
        if self.force or not os.path.exists(self.manifest_path):
            return {"articles": {}}
        try:
            with open(self.manifest_path, encoding="utf-8") as fh:
                data = json.load(fh)
            data.setdefault("articles", {})
            return data
        except (OSError, ValueError):
            return {"articles": {}}

    def _index_images(self) -> dict:
        """Map source URL to stored file, so a known image is never refetched."""
        index = {}
        for record in self.manifest["articles"].values():
            for image in record.get("images", []):
                stored = image.get("file")
                if stored and os.path.exists(os.path.join(self.root, stored)):
                    index[image["source"]] = image
        return index

    def save_manifest(self) -> None:
        if self.dry_run:
            return
        self.manifest["generated"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        os.makedirs(self.root, exist_ok=True)
        with open(self.manifest_path, "w", encoding="utf-8") as fh:
            json.dump(self.manifest, fh, indent=2, sort_keys=True)
            fh.write("\n")

    # -- images ------------------------------------------------------------- #

    @staticmethod
    def _image_name(src: str, digest: str) -> str:
        path = urllib.parse.urlparse(src).path
        ext = os.path.splitext(path)[1].lower()
        if ext not in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp"):
            ext = ".png"
        stem = slugify(os.path.splitext(os.path.basename(path))[0])[:48] or "image"
        return f"{digest[:16]}-{stem}{ext}"

    def store_image(self, src: str) -> dict:
        """Fetch an image unless it is already stored, and return its record."""
        known = self.by_url.get(src)
        if known and not self.force:
            self.stats["reused"] += 1
            return known
        if self.dry_run:
            self.stats["images"] += 1
            return {"source": src, "file": "", "bytes": 0, "sha256": ""}

        data = self.fetcher.get(src)
        digest = hashlib.sha256(data).hexdigest()
        # The same bytes can arrive under different URLs and filenames, so the
        # digest alone decides identity; the name is only for readability.
        existing = glob.glob(os.path.join(self.root, IMAGE_DIR, f"{digest[:16]}-*"))
        if existing:
            name = os.path.basename(existing[0])
        else:
            name = self._image_name(src, digest)
        rel = f"{IMAGE_DIR}/{name}"
        dest = os.path.join(self.root, IMAGE_DIR, name)
        if not os.path.exists(dest):
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as fh:
                fh.write(data)
            self.stats["image_bytes"] += len(data)
        else:
            # Same bytes reached us under a second URL; one copy is enough.
            self.stats["deduped"] += 1
        record = {"source": src, "file": rel, "bytes": len(data), "sha256": digest}
        self.by_url[src] = record
        self.stats["images"] += 1
        return record

    # -- articles ----------------------------------------------------------- #

    def article_paths(self, section_slug: str, article: dict) -> tuple[str, str]:
        base = article["slug"]
        return os.path.join(section_dir(section_slug), f"{base}.md"), base

    def archive_article(self, section_slug: str, stub: dict) -> dict | None:
        article_id = str(stub["articleID"])
        known = self.manifest["articles"].get(article_id)
        md_rel, _ = self.article_paths(section_slug, stub)
        md_abs = os.path.join(self.root, md_rel)
        if (known and not self.force and not self.rerender
                and known.get("dateUpdated") == stub["dateUpdated"]
                and os.path.exists(md_abs)):
            self.stats["skipped"] += 1
            return known

        article = self.fetcher.get_json(f"{API}/articles/{article_id}")
        here = os.path.dirname(md_rel)
        images: list[dict] = []
        seen: dict[str, str] = {}

        def on_image(src: str, _alt: str) -> str:
            if src in seen:
                return seen[src]
            record = self.store_image(src)
            images.append(record)
            rel = os.path.relpath(record["file"], here).replace(os.sep, "/")
            seen[src] = rel
            return rel

        body, unknown = to_markdown(article.get("body") or "", on_image)
        self.unknown_tags |= unknown

        record = {
            "articleID": article["articleID"],
            "name": article["name"],
            "section": section_slug,
            "url": article["url"],
            "slug": article["slug"],
            "author": (article.get("insertUser") or {}).get("name"),
            "lastEditor": (article.get("updateUser") or {}).get("name"),
            "dateInserted": article["dateInserted"],
            "dateUpdated": article["dateUpdated"],
            "markdown": md_rel.replace(os.sep, "/"),
            "images": images,
        }

        if not self.dry_run:
            os.makedirs(os.path.dirname(md_abs), exist_ok=True)
            with open(md_abs, "w", encoding="utf-8") as fh:
                fh.write(self._front_matter(record, section_slug))
                fh.write("\n")
                fh.write(f"# {article['name']}\n\n")
                fh.write(body)

        self.manifest["articles"][article_id] = record
        self.stats["updated"] += 1
        return record

    def _front_matter(self, record: dict, section_slug: str) -> str:
        lines = [
            "---",
            f"title: {yaml_quote(record['name'])}",
            f"section: {yaml_quote(SECTIONS[section_slug][1])}",
            f"article_id: {record['articleID']}",
            f"source: {yaml_quote(record['url'])}",
            f"author: {yaml_quote(record['author'])}",
            f"published: {yaml_quote(record['dateInserted'])}",
            f"updated: {yaml_quote(record['dateUpdated'])}",
            f"archived: {yaml_quote(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))}",
            "---",
        ]
        return "\n".join(lines) + "\n"

    # -- sections ----------------------------------------------------------- #

    def list_articles(self, category_id: int) -> list[dict]:
        found: list[dict] = []
        page = 1
        while True:
            url = (f"{API}/articles?knowledgeCategoryID={category_id}"
                   f"&limit=100&page={page}")
            batch = self.fetcher.get_json(url)
            if not batch:
                break
            found.extend(batch)
            if len(batch) < 100:
                break
            page += 1
        return found

    def archive_section(self, section_slug: str) -> list[dict]:
        category_id, title = SECTIONS[section_slug]
        stubs = self.list_articles(category_id)
        print(f"  {title}: {len(stubs)} article(s)", flush=True)
        records = []
        for stub in stubs:
            self.stats["articles"] += 1
            try:
                record = self.archive_article(section_slug, stub)
            except Exception as err:  # noqa: BLE001 - keep going, report at end
                print(f"    !! {stub['slug']}: {err}", file=sys.stderr)
                continue
            if record:
                records.append(record)
                self.save_manifest()   # checkpoint: a long run can be resumed
                print(f"    - {record['name']} "
                      f"({len(record['images'])} image(s))", flush=True)
        return records


def _sha256_file(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


# --------------------------------------------------------------------------- #
# Summaries
# --------------------------------------------------------------------------- #

SUMMARY_OPEN = "<!-- summary -->"
SUMMARY_CLOSE = "<!-- /summary -->"
_SUMMARY_BLOCK = re.compile(
    re.escape(SUMMARY_OPEN) + r".*?" + re.escape(SUMMARY_CLOSE) + r"\n*", re.DOTALL)
SUMMARIES_FILE = "summaries.json"
SUMMARY_HEADING = "## AI TL;DR"


def write_summaries(root: str, manifest: dict) -> int:
    """Inject the summaries from summaries.json below each article's front matter.

    The file maps article id to a short plain-text summary and is produced
    outside this bot. Articles without an entry are left alone, and an existing
    block is replaced, so re-running after a summary is rewritten updates the
    page. The navigation pass that follows settles the final ordering.
    """
    path = os.path.join(root, SUMMARIES_FILE)
    if not os.path.exists(path):
        return 0
    with open(path, encoding="utf-8") as fh:
        summaries = json.load(fh)

    touched = 0
    for record in manifest["articles"].values():
        summary = (summaries.get(str(record["articleID"])) or "").strip()
        article = os.path.join(root, record["markdown"])
        if not os.path.exists(article):
            continue
        with open(article, encoding="utf-8") as fh:
            text = fh.read()
        front, marker, body = text.partition("\n---\n")
        body = _SUMMARY_BLOCK.sub("", body).lstrip("\n")
        if summary:
            block = (f"{SUMMARY_OPEN}\n{SUMMARY_HEADING}\n\n{summary}\n"
                     f"{SUMMARY_CLOSE}\n\n")
            body = block + body
        updated = front + marker + "\n" + body
        if updated != text:
            with open(article, "w", encoding="utf-8") as fh:
                fh.write(updated)
            touched += 1
    return touched


# --------------------------------------------------------------------------- #
# Navigation
# --------------------------------------------------------------------------- #

NAV_OPEN = "<!-- nav -->"
NAV_CLOSE = "<!-- /nav -->"
_NAV_BLOCK = re.compile(re.escape(NAV_OPEN) + r".*?" + re.escape(NAV_CLOSE) + r"\n*",
                        re.DOTALL)


def _nav_line(record: dict, older: dict | None, newer: dict | None,
              index_rel: str) -> str:
    """One breadcrumb line: older article, the index, newer article."""
    here = os.path.dirname(record["markdown"])

    def link(target: dict) -> str:
        rel = os.path.relpath(target["markdown"], here).replace(os.sep, "/")
        return f"[{target['name']}]({urllib.parse.quote(rel)})"

    parts = [f"&larr; {link(older)}" if older else "&larr; _oldest_"]
    parts.append(f"[{SECTIONS[record['section']][1]}]({index_rel}#"
                 f"{slugify(SECTIONS[record['section']][1])})")
    parts.append(f"{link(newer)} &rarr;" if newer else "_newest_ &rarr;")
    return f"{NAV_OPEN}\n" + " · ".join(parts) + f"\n{NAV_CLOSE}"


def write_navigation(root: str, manifest: dict) -> int:
    """Rewrite the header/footer nav of every archived article.

    Runs after each sync so articles on either side of a newly added one pick
    up the new neighbour. Idempotent: unchanged neighbours mean unchanged
    bytes, so a quiet run leaves the files alone.
    """
    by_section: dict[str, list[dict]] = {}
    for record in manifest["articles"].values():
        by_section.setdefault(record["section"], []).append(record)

    touched = 0
    for records in by_section.values():
        records.sort(key=lambda r: (r["dateInserted"], r["articleID"]))
        for position, record in enumerate(records):
            path = os.path.join(root, record["markdown"])
            if not os.path.exists(path):
                continue
            older = records[position - 1] if position else None
            newer = records[position + 1] if position + 1 < len(records) else None
            index_rel = os.path.relpath(
                "index.md", os.path.dirname(record["markdown"])).replace(os.sep, "/")
            nav = _nav_line(record, older, newer, index_rel)

            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            head, marker, body = text.partition("\n---\n")
            front = head + marker
            body = _NAV_BLOCK.sub("", body)
            # The summary is a standfirst: it stays directly under the front
            # matter, above the navigation line.
            found = _SUMMARY_BLOCK.search(body)
            summary = found.group(0).strip() + "\n\n" if found else ""
            body = _SUMMARY_BLOCK.sub("", body).strip()
            updated = f"{front}\n{summary}{nav}\n\n{body}\n\n{nav}\n"
            if updated != text:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(updated)
                touched += 1
    return touched


# --------------------------------------------------------------------------- #
# Index
# --------------------------------------------------------------------------- #

def write_index(root: str, manifest: dict) -> None:
    by_section: dict[str, list[dict]] = {slug: [] for slug in SECTIONS}
    for record in manifest["articles"].values():
        by_section.setdefault(record["section"], []).append(record)

    lines = [
        "# Dead by Daylight Patch Note Archive",
        "",
        "An unofficial, read-only archive of BHVR's Dead by Daylight patch notes",
        "and developer updates, captured before their removal.",
        "",
        f"{len(manifest['articles'])} articles. "
        "See `manifest.json` for capture timestamps and image hashes.",
        "",
    ]
    for slug, (_cid, title) in SECTIONS.items():
        records = sorted(by_section.get(slug, []),
                         key=lambda r: r["dateInserted"], reverse=True)
        if not records:
            continue
        lines += [f"## {title}", "", f"{len(records)} article(s).", ""]
        for record in records:
            date = record["dateInserted"][:10]
            lines.append(f"- [{record['name']}]({record['markdown']}) — {date}")
        lines.append("")
    with open(os.path.join(root, "index.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="archive", help="output root (default: archive)")
    parser.add_argument("--section", action="append", choices=sorted(SECTIONS),
                        help="limit to one or more sections (repeatable)")
    parser.add_argument("--delay", type=float, default=1.0,
                        help="seconds between requests (default: 1.0)")
    parser.add_argument("--dry-run", action="store_true",
                        help="fetch and convert, but write nothing")
    parser.add_argument("--force", action="store_true",
                        help="re-download everything, ignoring the manifest")
    parser.add_argument("--rerender", action="store_true",
                        help="rewrite every article's Markdown, reusing stored images")
    parser.add_argument("--no-index", action="store_true", help="skip index.md")
    args = parser.parse_args(argv)

    root = os.path.abspath(args.out)
    fetcher = Fetcher(delay=args.delay)
    archiver = Archiver(root, fetcher, dry_run=args.dry_run, force=args.force,
                        rerender=args.rerender)
    sections = args.section or list(SECTIONS)

    print(f"Archiving {len(sections)} section(s) into {root}"
          f"{' (dry run)' if args.dry_run else ''}")
    for slug in sections:
        archiver.archive_section(slug)

    archiver.save_manifest()
    if not args.dry_run:
        summarised = write_summaries(root, archiver.manifest)
        if summarised:
            print(f"Summaries applied to {summarised} article(s)")
        touched = write_navigation(root, archiver.manifest)
        print(f"Navigation refreshed on {touched} article(s)")
        if not args.no_index:
            write_index(root, archiver.manifest)

    stats = archiver.stats
    print(f"\nArticles seen {stats['articles']}, written {stats['updated']}, "
          f"unchanged {stats['skipped']}")
    print(f"Images stored {stats['images']} ({stats['image_bytes'] / 1e6:.1f} MB), "
          f"reused {stats['reused']}, duplicates skipped {stats['deduped']}")
    if archiver.unknown_tags:
        print(f"Unhandled tags (rendered inline): "
              f"{', '.join(sorted(archiver.unknown_tags))}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
