# dbd-bug-archive

An unofficial archive of Dead by Daylight's patch notes and developer updates,
captured from [forums.bhvr.com](https://forums.bhvr.com/dead-by-daylight/kb/patchnotes)
before their scheduled removal in October 2026.

Everything under [`archive/`](archive/) is Markdown with the original images
saved alongside it. Start at [`archive/index.md`](archive/index.md).

## What is archived

| Section | Source |
| --- | --- |
| Live | current public channel |
| Player Test Build (PTB) | beta channel |
| Archive: Steam | Steam-only changes |
| Archive: PS4 | PlayStation-only changes |
| Archive: Xbox One | Xbox-only changes |
| Archive: Nintendo Switch | Switch / Switch 2 changes |
| Archive: Windows Store | Windows app changes |
| Archive: Stadia | Google Stadia changes |
| Developer Updates | dev blog posts from Game Info |

Nothing else from the knowledge base (FAQs, rules, guides) is included.

## Layout

```
archive/
  index.md                          # every article, by section, newest first
  manifest.json                     # ids, timestamps, image hashes
  patch-notes/<section>/<slug>.md   # one article
  patch-notes/<section>/<slug>/     # that article's images
  developer-updates/<slug>.md
  developer-updates/<slug>/
```

Each article carries YAML front matter with its title, section, article id,
source URL, author, and publish / update / archive timestamps.

Images are taken from the article body only — the in-body hero banner and the
decorative divider bars are kept; the knowledge-base page banner, which is site
chrome rather than part of the post, is not.

## Running the bot

Python 3.9+, no dependencies:

```sh
python3 dbd_archive.py                     # archive everything
python3 dbd_archive.py --section live       # one section (repeatable)
python3 dbd_archive.py --dry-run            # convert, write nothing
python3 dbd_archive.py --force              # redo everything
python3 dbd_archive.py --delay 2.0          # slow down
```

Re-runs are incremental: an article whose `dateUpdated` matches `manifest.json`
is skipped, and images already on disk are left alone. Requests are throttled
and retried with exponential backoff.

The bot reads BHVR's public Vanilla knowledge-base API (`/api/v2/articles`,
`/api/v2/knowledge-categories`) rather than scraping rendered HTML, so the
output is the article body as authored.

## Licence

The archived text and images remain the property of Behaviour Interactive.
This repository is a preservation effort, not affiliated with or endorsed by
Behaviour Interactive.
