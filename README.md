# dbd-bug-archive

Every Dead by Daylight patch note and developer update, saved before
[the forums](https://forums.bhvr.com/dead-by-daylight/kb/patchnotes) take them
down in October 2026. 479 articles, 2018 to 2026, with all their images.

### **→ [Open the archive](archive/index.md)**

| You want | Do this |
| --- | --- |
| To browse | Open [the index](archive/index.md) and pick a section |
| A specific version | Press <kbd>t</kbd> and type it with dashes — `10-1-2`, not `10.1.2` |
| Any mention of something | Press <kbd>/</kbd> and search — `Decisive Strike` |
| A Table of Contents | Press the <img width="36" height="36" alt="image" align="middle" src="https://github.com/user-attachments/assets/004d6040-bc1c-4552-85a9-49516f1d8448" /> (Outline button) at the top right |

Each page links to the previous and next patch, top and bottom, so you can read
straight through a section without coming back here.

## What's here

| Section | Articles | What it covers |
| --- | ---: | --- |
| [Live](archive/patch-notes/live/) | 135 | the main game everyone plays |
| [Player Test Build](archive/patch-notes/player-test-build/) | 66 | the test server, before changes go live |
| [Archive: Steam](archive/patch-notes/archive-steam/) | 57 | Steam-only fixes |
| [Archive: PS4](archive/patch-notes/archive-ps4/) | 56 | PlayStation-only fixes |
| [Archive: Xbox One](archive/patch-notes/archive-xbox-one/) | 53 | Xbox-only fixes |
| [Archive: Nintendo Switch](archive/patch-notes/archive-nintendo-switch/) | 24 | Switch and Switch 2 |
| [Archive: Windows Store](archive/patch-notes/archive-windows-store/) | 23 | Windows app |
| [Archive: Stadia](archive/patch-notes/archive-stadia/) | 3 | Google Stadia |
| [Developer Updates](archive/developer-updates/) | 62 | the dev team explaining what's coming and why |

Patch notes and developer updates only — no FAQs, guides, or forum threads.

## One thing to know

Each page starts with an **AI TL;DR**. That summary was written by a machine, to
help you tell at a glance whether this is the patch you wanted.

Everything below the title is BHVR's original article, word for word. **If the
summary and the article disagree, the article is right.**

---

<details>
<summary><b>How it's organised</b></summary>

<br>

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

Filenames keep the forum's own slug, so the original URL is recoverable from
the name: `558-10-1-2-bugfix-patch.md` came from
`forums.bhvr.com/dead-by-daylight/kb/articles/558-10-1-2-bugfix-patch`. Slugs
write versions with dashes, which is why the file finder wants `10-1-2`.

Each article opens with front matter giving its title, section, article id,
source URL, author, and publish / update / archive timestamps.

**Images.** Only images inside the article body are saved — the hero banner and
the decorative divider bars. The page banner above the title is site furniture,
not part of the post, so it is skipped.

They live in one shared `archive/images/` folder, named by the first 16 hex
digits of their SHA-256 plus the original filename. Identity is the digest
alone, so a divider bar used on two hundred pages is stored once and referenced
from each. That takes 1906 files down to 667. Every image is listed in
`manifest.json` with its source URL, size and full digest.

</details>

<details>
<summary><b>Running the bot</b></summary>

<br>

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

A first run takes about an hour and writes roughly 600 MB, most of it the large
GIFs in Developer Updates. Later runs take seconds unless something changed.

**How it behaves**

- **Incremental.** An article whose `dateUpdated` still matches
  `manifest.json` is skipped, and a stored image is never refetched.
- **Resumable.** The manifest is checkpointed after every article, so an
  interrupted run picks up where it stopped.
- **Polite.** One request at a time, throttled by `--delay`, with four retries
  and exponential backoff on network errors and HTTP 429.
- **Honest about failures.** A failed article is reported to stderr and the run
  continues; unhandled HTML tags are listed at the end.

**How it works**

It reads BHVR's public Vanilla knowledge-base API
(`/api/v2/knowledge-categories`, `/api/v2/articles`) instead of scraping
rendered pages, so what lands in the Markdown is the article as authored — no
navigation, no theme chrome, no JavaScript.

Bodies are converted by a small HTML parser and Markdown writer in
`dbd_archive.py`: headings, nested lists, emphasis, links, tables, code and
images; BHVR's `home/leaving?target=` redirector unwrapped back to the real
URL; forum quotes as blockquotes and spoilers as collapsible `<details>`;
interface chrome such as spoiler toggles and inline SVG icons dropped.

Two passes then tidy up — summaries injected under the front matter, then the
navigation lines rebuilt so a new article wires itself into its neighbours.
Both are idempotent.

**Summaries.** `archive/summaries.json` maps article id to summary text. Edit
an entry and re-run the bot to update that page; delete one and that page loses
its TL;DR. The articles themselves are never touched.

</details>

<details>
<summary><b>Weekly sync</b></summary>

<br>

[`.github/workflows/archive.yml`](.github/workflows/archive.yml) re-runs the
bot every Sunday and commits anything new, so posts made before the knowledge
base comes down are not missed. It can also be run on demand from the Actions
tab.

A quiet week produces no commit. Delete the workflow once the archive is
locked.

</details>

---

An unofficial preservation effort, not affiliated with or endorsed by Behaviour
Interactive. The archived text and images remain their property and are
reproduced here for reference only. The bot (`dbd_archive.py`) is free to reuse.
