# dbd-bug-archive

An unofficial archive of Dead by Daylight's **patch notes** and **developer
updates**, captured from [forums.bhvr.com](https://forums.bhvr.com/dead-by-daylight/kb/patchnotes)
before their scheduled removal in October 2026.

479 articles, from the 2018 Emblems patch to September 2026, as plain Markdown
with every image. No account, no JavaScript, no forum — just files.

> This repository is a preservation effort. It is not affiliated with, endorsed
> by, or supported by Behaviour Interactive.

---

## Start here

**→ [`archive/index.md`](archive/index.md)** — every article, grouped by
section, newest first.

Three ways to find a patch:

| You want | Do this |
| --- | --- |
| To browse | Open [the index](archive/index.md) and pick a section |
| A specific version | Press <kbd>t</kbd> on GitHub and type it with dashes, e.g. `10-1-2` |
| Anything mentioning a thing | Press <kbd>/</kbd> on GitHub and search, e.g. `Decisive Strike` |

Filenames use dashes where a version uses dots, because they come from the
forum's own slugs: `10.1.2` is `558-10-1-2-bugfix-patch.md`. The file finder
matches on that name, so `10.1.2` finds nothing and `10-1-2` finds the page.
Full-text search is unaffected — `10.1.2` works there, since the version
appears with its dots inside the page.

Reading an article, you never need to go back to the index: every page has
**← previous · section · next →** links at the top *and* bottom, ordered
oldest to newest within its section.

The <img width="38" height="36" alt="image" align="middle" src="https://github.com/user-attachments/assets/734c7c58-0e18-49b8-b08f-cc12314c8d3a" /> (Outline button) at the top right of this module can provide a Table of Contents layout for easier navigation.

---

## What's in a page

Every article follows the same shape:

```
┌─ front matter ──── title, version, author, dates, link to the original
├─ AI TL;DR ─────── a short summary, one or two paragraphs
├─ navigation ───── ← previous · section · next →
├─ the article ──── exactly as BHVR published it, images and all
└─ navigation ───── the same links again
```

**The AI TL;DR is not BHVR's writing.** It is generated from the page below it,
as a finding aid — enough to tell whether this is the patch you are looking
for. Everything under the `# ` title is the original article, unedited. If the
two ever disagree, the article is right.

The `source:` line in the front matter links back to the original forum page
for as long as that page exists.

---

## What is archived

Nine knowledge-base categories:

| Section | Articles | What it covers |
| --- | ---: | --- |
| [Live](archive/patch-notes/live/) | 135 | the current public channel all players are on |
| [Player Test Build](archive/patch-notes/player-test-build/) | 66 | the beta channel for upcoming changes |
| [Archive: Steam](archive/patch-notes/archive-steam/) | 57 | Steam-only changes, mostly bug fixes |
| [Archive: PS4](archive/patch-notes/archive-ps4/) | 56 | PlayStation-only changes, mostly bug fixes |
| [Archive: Xbox One](archive/patch-notes/archive-xbox-one/) | 53 | Xbox-only changes, mostly bug fixes |
| [Archive: Nintendo Switch](archive/patch-notes/archive-nintendo-switch/) | 24 | Switch and Switch 2 changes |
| [Archive: Windows Store](archive/patch-notes/archive-windows-store/) | 23 | Windows app changes |
| [Archive: Stadia](archive/patch-notes/archive-stadia/) | 3 | Google Stadia changes |
| [Developer Updates](archive/developer-updates/) | 62 | dev blog posts from Game Info |

Nothing else from the forums is included — no FAQs, rules, guides, or
discussion threads.

---

## Repository layout

```
archive/
  index.md                          every article, by section, newest first
  manifest.json                     ids, timestamps, image names and hashes
  summaries.json                    the AI TL;DR text, by article id
  images/<hash>-<name>.<ext>        every image, stored once
  patch-notes/<section>/<slug>.md   one article
  developer-updates/<slug>.md
dbd_archive.py                      the bot that produced all of the above
```

A file keeps the article's own forum slug, so the source URL is recoverable
from the filename: `558-10-1-2-bugfix-patch.md` came from
`forums.bhvr.com/dead-by-daylight/kb/articles/558-10-1-2-bugfix-patch`.

### Images

Only images inside the article body are saved — the in-body hero banner
(`BUGFIX PATCH 10.1.2`) and the decorative red and white divider bars between
sections. The knowledge-base page banner above the title is site furniture
rather than part of the post, and is not saved.

Images live in one shared `archive/images/` folder, named by the first 16 hex
digits of their SHA-256 plus the original filename. Identity is the digest
alone, so a file that appears on two hundred pages — the divider bars, for
instance — is stored once and referenced from each article. That takes 1906
files down to 667. Every image is recorded in `manifest.json` with its source
URL, byte size and full digest.

---

## Running the bot

Python 3.9 or newer. No dependencies — standard library only, so it still runs
years from now.

```sh
python3 dbd_archive.py                      # archive everything
python3 dbd_archive.py --section live       # one section (repeatable)
python3 dbd_archive.py --dry-run            # fetch and convert, write nothing
python3 dbd_archive.py --rerender           # rewrite Markdown, reuse stored images
python3 dbd_archive.py --force              # redo everything from scratch
python3 dbd_archive.py --delay 2.0          # be gentler on the server
python3 dbd_archive.py --out some/dir       # write somewhere else
```

Section names are the directory names above: `live`, `player-test-build`,
`archive-steam`, `archive-ps4`, `archive-xbox-one`, `archive-nintendo-switch`,
`archive-windows-store`, `archive-stadia`, `developer-updates`.

A first run takes roughly an hour and writes about 600 MB, most of it the large
GIFs in Developer Updates. Later runs take seconds unless something changed.

### How it behaves

- **Incremental.** An article whose `dateUpdated` still matches `manifest.json`
  is skipped, and an image already stored is never refetched. Re-running to
  pick up a newly posted patch costs a few hundred cheap requests.
- **Resumable.** The manifest is checkpointed after every article, so an
  interrupted run picks up where it stopped.
- **Polite.** One request at a time, throttled by `--delay`, with four retries
  and exponential backoff on network errors and HTTP 429.
- **Honest about failures.** An article that fails is reported to stderr and the
  run continues; unhandled HTML tags are listed at the end.

### How it works

The bot reads BHVR's public Vanilla knowledge-base API
(`/api/v2/knowledge-categories`, `/api/v2/articles`) rather than scraping
rendered pages, so what lands in the Markdown is the article body as authored —
no navigation, no theme chrome, no JavaScript needed.

Bodies are converted by a small HTML parser and Markdown writer in
`dbd_archive.py`. It handles headings, nested lists, emphasis, links, tables,
code and images, unwraps BHVR's `home/leaving?target=` redirector back to the
real URL, renders forum quotes as Markdown blockquotes and spoiler blocks as
collapsible `<details>`, and drops interface chrome such as spoiler toggle
buttons and inline SVG icons.

After the articles are written, two passes tidy the result: summaries from
`summaries.json` are injected under the front matter, then the navigation
lines are rebuilt so a newly added article wires itself into its neighbours.
Both are idempotent — nothing changes if nothing changed.

### Regenerating the summaries

`archive/summaries.json` maps article id to summary text. Replace or edit an
entry and re-run the bot; the page picks it up. Delete an entry and that page
loses its TL;DR. The articles themselves are never touched by this.

---

## Weekly sync

[`.github/workflows/archive.yml`](.github/workflows/archive.yml) re-runs the
bot every Sunday and commits anything new, so posts made before the knowledge
base comes down in October 2026 are not missed. It can also be run on demand
from the Actions tab.

A quiet week produces no commit. Delete the workflow once the archive is
locked.

---

## Licence

The archived text and images remain the property of Behaviour Interactive and
are reproduced here for preservation and reference only. The bot itself
(`dbd_archive.py`) is free to reuse.
