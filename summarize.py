#!/usr/bin/env python3
"""Generate the AI TL;DR for archived articles that do not have one yet.

Summaries are produced by a local model reached through the offload server
(https://agent.ephellon.duckdns.org), authenticated with OFFSER_TOKEN, and
written to archive/summaries.json. Running dbd_archive.py afterwards injects
them into the pages.

Only articles missing a summary are sent, so a normal week costs one request.

    python3 summarize.py                  # fill in whatever is missing
    python3 summarize.py --list           # name them, send nothing
    python3 summarize.py --redo 558 560   # regenerate specific articles
    python3 summarize.py --model gemma4:31b-cloud

Without OFFSER_TOKEN it exits 0 having done nothing, so an automated run that
cannot reach the server still succeeds and simply leaves the pages unsummarised.
"""
import argparse
import json
import os
import queue
import re
import sys
import threading
import time
import urllib.error
import urllib.request

BASE = os.environ.get("OFFSER_BASE", "https://agent.ephellon.duckdns.org")
TOK = os.environ.get("OFFSER_TOKEN", "")
MODEL = "gpt-oss:120b-cloud"
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "archive")
OUT = os.path.join(ROOT, "summaries.json")

INSTRUCTIONS = """You are writing a short summary for an archived Dead by Daylight patch note page.

Rules:
- HARD LIMIT: at most TWO paragraphs and at most 120 WORDS in total. Count them. One paragraph is better
  when one will do. Separate paragraphs with a blank line.
- A TL;DR, not an inventory. When a page lists thirty bug fixes, say what areas
  they covered; do not enumerate them.
- Plain prose only. No headings, no bullets, no markdown emphasis, no links.
- Lead with what actually changed: name the killer, survivor, perk, map or system specifically.
- Then say the shape of the rest: mostly bug fixes, a new chapter, a platform hotfix, etc.
- For a Developer Update, say what was proposed or explained and its state (PTB, upcoming, shipped).
- Never invent versions, dates or changes not present in the page.
- Do NOT start with "This patch", "This article", "This page" or "Summary", and do
  NOT open with the version number ("The 3.1.0 update..."). Start with the substance:
  what changed, named.
- Output ONLY the summary text. No preamble, no commentary, no quotes around it.

PAGE TITLE: {title}
SECTION: {section}

PAGE CONTENT:
{body}
"""

_throttle = threading.Semaphore(5)   # the host resets connections under load


def req(path, data=None, method=None, tries=5):
    body = json.dumps(data).encode() if data is not None else None
    last = None
    for attempt in range(tries):
        r = urllib.request.Request(BASE + path, method=method,
            headers={"Authorization": "Bearer " + TOK,
                     "Content-Type": "application/json"},
            data=body)
        try:
            with _throttle:
                with urllib.request.urlopen(r, timeout=180) as resp:
                    return resp.status, json.loads(resp.read().decode())
        except urllib.error.HTTPError as err:
            if err.code == 202:
                raise
            last = err
        except Exception as err:
            last = err
        time.sleep(min(2 ** attempt, 20))
    raise RuntimeError(f"{path}: {last}")

def clean_body(path):
    t = open(path, encoding="utf-8").read()
    t = t.split("\n---\n", 1)[-1]
    t = re.sub(r"<!-- nav -->.*?<!-- /nav -->", "", t, flags=re.S)
    t = re.sub(r"<!-- summary -->.*?<!-- /summary -->", "", t, flags=re.S)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\n{3,}", "\n\n", t).strip()
    return t[:60000]

# Typographic characters the model favours that break plain-text search.
_NORMALISE = {0x2011: "-", 0x2012: "-", 0x2013: "-", 0x202F: " ", 0x00A0: " ",
              0x2009: " ", 0x200B: ""}


def tidy(text):
    text = text.translate(_NORMALISE).strip()
    text = re.sub(r"^(here('s| is)[^\n:]*:|summary:)\s*", "", text, flags=re.I)
    # Only unwrap quotes that enclose the WHOLE summary; a leading quote that
    # belongs to a name ("The First" killer) must survive.
    stripped = text.strip()
    for q in ('"', "'", "`"):
        while stripped.startswith(q) and stripped.endswith(q) and len(stripped) > 1:
            stripped = stripped[1:-1].strip()
    text = stripped
    text = re.sub(r"^#+ .*\n+", "", text)
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    return "\n\n".join(paras[:2]).strip()

def drop(slug):
    """End the thread for this key so its stored reply cannot be replayed."""
    try:
        req("/jobs", {"model": MODEL, "filename": slug, "content": f"/drop {slug}"})
    except Exception as err:
        print(f"  .. drop {slug}: {err}", file=sys.stderr, flush=True)


def _mtime(slug):
    try:
        _, data = req(f"/jobs/{slug}")
    except urllib.error.HTTPError as err:
        if err.code in (202, 404):
            return 0.0
        raise
    except Exception:
        return 0.0
    return float(data.get("mtime") or 0)


def _ask(slug, prompt):
    # Each turn overwrites the same reply in place, so remember what was there
    # and refuse to accept it as this turn's answer.
    before = _mtime(slug)
    req("/jobs", {"model": MODEL, "filename": slug, "content": prompt})
    deadline = time.time() + 900
    while time.time() < deadline:
        time.sleep(5)
        try:
            status, data = req(f"/jobs/{slug}?read=true")
        except urllib.error.HTTPError as e:
            if e.code == 202:
                continue
            raise
        if data.get("ready") and float(data.get("mtime") or 0) > before:
            return tidy(data.get("content") or "")
    raise TimeoutError(slug)


WORD_LIMIT = 120
HARD_LIMIT = 190


def run_one(aid, rec):
    slug = f"dbd-sum-{aid}"
    body = clean_body(os.path.join(ROOT, rec["markdown"]))
    prompt = INSTRUCTIONS.format(title=rec["name"], section=rec["section"], body=body)
    try:
        summary = _ask(slug, prompt)
        if len(summary.split()) > HARD_LIMIT:
            # The model routinely overshoots the cap on long patch notes; one
            # compression turn on the same thread gets it back in range.
            summary = _ask(slug,
                           f"Too long. Rewrite your summary in at most "
                           f"{WORD_LIMIT} words, keeping the specific names and "
                           "the two-paragraph maximum. Output only the summary."
                           ) or summary
        return summary
    finally:
        drop(slug)

def pending(man, done, redo):
    if redo:
        return [(a, man[a]) for a in redo if a in man]
    return [(a, r) for a, r in sorted(man.items(), key=lambda kv: int(kv[0]))
            if not done.get(a)]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true",
                    help="name the articles missing a summary and exit")
    ap.add_argument("--redo", nargs="+", metavar="ID",
                    help="regenerate these article ids even if they have one")
    ap.add_argument("--model", default=MODEL,
                    help="offload model (default: " + MODEL + ")")
    ap.add_argument("--workers", type=int, default=6, help="jobs in flight (default: 6)")
    args = ap.parse_args(argv)
    globals()["MODEL"] = args.model

    man = json.load(open(os.path.join(ROOT, "manifest.json")))["articles"]
    done = json.load(open(OUT)) if os.path.exists(OUT) else {}
    todo = pending(man, done, args.redo)

    if args.list:
        for aid, rec in todo:
            print(f"{aid}\t{rec['name']}")
        print(f"{len(todo)} article(s) without a summary", file=sys.stderr)
        return 0
    if not todo:
        print("Every article already has a summary.")
        return 0
    if not TOK:
        # An automated run without the credential should not fail the build;
        # the missing summaries are reported by the caller instead.
        print(f"OFFSER_TOKEN is not set; leaving {len(todo)} article(s) "
              "without a summary.", file=sys.stderr)
        return 0

    print(f"{len(done)} done, {len(todo)} to go", flush=True)
    lock = threading.Lock()
    work = queue.Queue()
    for item in todo:
        work.put(item)
    failures = []

    def worker():
        while True:
            try:
                aid, rec = work.get_nowait()
            except queue.Empty:
                return
            try:
                summary = run_one(aid, rec)
                if not summary:
                    raise ValueError("empty summary")
                with lock:
                    done[aid] = summary
                    json.dump(done, open(OUT, "w"), indent=1, sort_keys=True)
                    print(f"  [{len(done)}/{len(man)}] {rec['name']}", flush=True)
            except Exception as err:
                print(f"  !! {aid} {rec['name']}: {err}", file=sys.stderr, flush=True)
                with lock:
                    failures.append((aid, rec))
            finally:
                work.task_done()

    threads = [threading.Thread(target=worker, daemon=True)
               for _ in range(max(1, args.workers))]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # The host resets connections under load; a serial sweep mops that up.
    for attempt in range(3):
        if not failures:
            break
        print(f"retry sweep {attempt + 1}: {len(failures)} left", flush=True)
        retry, failures = failures, []
        for aid, rec in retry:
            try:
                summary = run_one(aid, rec)
                if not summary:
                    raise ValueError("empty summary")
                done[aid] = summary
                json.dump(done, open(OUT, "w"), indent=1, sort_keys=True)
                print(f"  [{len(done)}/{len(man)}] {rec['name']}", flush=True)
            except Exception as err:
                print(f"  !! {aid}: {err}", file=sys.stderr, flush=True)
                failures.append((aid, rec))

    print(f"finished: {len(done)}/{len(man)} summarised")
    if failures:
        print("unresolved: " + ", ".join(a for a, _ in failures), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
