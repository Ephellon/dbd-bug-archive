# dbd-bug-archive

An unofficial archive of Dead by Daylight's **patch notes** and **developer
updates**, captured from [forums.bhvr.com](https://forums.bhvr.com/dead-by-daylight/kb/patchnotes)
before their scheduled removal in October 2026.

The `Outline` button at the top right of this module can provide a Table of Contents layout for easier navigation.

Everything under [`archive/`](archive/) is plain Markdown with the original
images saved beside it. Start at [`archive/index.md`](archive/index.md).

> This repository is a preservation effort. It is not affiliated with, endorsed
> by, or supported by Behaviour Interactive.

## What is archived

479 articles across nine knowledge-base categories:

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

## Layout

```
archive/
  index.md                          # every article, by section, newest first
  manifest.json                     # ids, timestamps, image names and hashes
  patch-notes/<section>/<slug>.md   # one article
  patch-notes/<section>/<slug>/     # that article's images, in document order
  developer-updates/<slug>.md
  developer-updates/<slug>/
```

`<slug>` is the article's own forum slug, so it keeps the source id:
`558-10-1-2-bugfix-patch.md` is
`forums.bhvr.com/dead-by-daylight/kb/articles/558-10-1-2-bugfix-patch`.

Every article opens with YAML front matter:

```yaml
---
title: "10.1.2 Bugfix Patch"
section: "Live"
article_id: 558
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/558-10-1-2-bugfix-patch"
author: "Mandy"
published: "2026-09-08T15:10:37+00:00"
updated: "2026-09-17T15:02:29+00:00"
archived: "2026-09-26T01:20:15Z"
---
```

### Images

Only images inside the article body are saved — the in-body hero banner
(`BUGFIX PATCH 10.1.2`) and the decorative red/white divider bars between
sections. The knowledge-base page banner above the title is site furniture
rather than part of the post, and is not saved.

Files are numbered in document order (`01-dbd-1012-patchnotes-hf2-16-9.png`,
`02-bar-red.png`, …) and recorded in `manifest.json` with their source URL,
byte size, and SHA-256.

## Running the bot

Python 3.9 or newer. No dependencies — standard library only, so it still runs
years from now.

```sh
python3 dbd_archive.py                      # archive everything
python3 dbd_archive.py --section live       # one section (repeatable)
python3 dbd_archive.py --dry-run            # fetch and convert, write nothing
python3 dbd_archive.py --force              # redo everything from scratch
python3 dbd_archive.py --delay 2.0          # be gentler on the server
python3 dbd_archive.py --out some/dir       # write somewhere else
```

Section names are the directory names above: `live`, `player-test-build`,
`archive-steam`, `archive-ps4`, `archive-xbox-one`, `archive-nintendo-switch`,
`archive-windows-store`, `archive-stadia`, `developer-updates`.

A full run takes roughly an hour and writes about 340 MB, most of it hero
images.

### How it behaves

- **Incremental.** An article whose `dateUpdated` still matches `manifest.json`
  is skipped, and images already on disk are left alone. Re-running to pick up
  a newly posted patch costs a few hundred cheap requests.
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
real URL, renders forum spoiler blocks as collapsible `<details>`, and drops
interface chrome such as spoiler toggle buttons and inline SVG icons.

## Weekly sync

[`.github/workflows/archive.yml`](.github/workflows/archive.yml) re-runs the
bot every Sunday and commits anything new, so posts made before the knowledge
base comes down in October 2026 are not missed. It can also be run on demand
from the Actions tab.

A quiet week produces no commit. Delete the workflow once the archive is
locked.

## Licence

The archived text and images remain the property of Behaviour Interactive and
are reproduced here for preservation and reference only. The bot itself
(`dbd_archive.py`) is free to reuse.
