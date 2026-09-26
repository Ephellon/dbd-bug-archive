---
title: "2.5.1 | Hotfix"
section: "Archive: PS4"
article_id: 47
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/47-2-5-1-hotfix"
author: "Peanits"
published: "2020-02-28T18:52:39+00:00"
updated: "2020-03-02T19:30:27+00:00"
archived: "2026-09-26T17:09:49Z"
---

<!-- summary -->
## AI TL;DR

Hotfix 2.5.1 resolves a range of survivor and UI problems on PS4, including interaction failures in the basement, stuck survivors at the campfire, and a broken vault-rush window on Badham Preschool. It also fixes Prove Thyself not applying to its owner, incorrect Self-Care tier text in all languages, and a missing Game Over score event for The Pig. Several stability issues are addressed: crashes from disconnects during Mori or status effects, loading hangs, and tally-screen errors. HUD survivor icons now update more reliably after disconnects, Bloodweb refreshes correctly when swapping characters or opening mystery boxes, and exploits involving prestige and simultaneous character swaps are blocked.
<!-- /summary -->

<!-- nav -->
&larr; [2.5.0 | Mid-Chapter](46-2-5-0-mid-chapter.md) · [Archive: PS4](../../index.md#archive-ps4) · [2.5.3 | Hotfix](48-2-5-3-hotfix.md) &rarr;
<!-- /nav -->

# 2.5.1 | Hotfix

## Bug Fixes

- Fixed an issue that could cause survivors to be unable to trigger interaction or cause the character to be teleported back to the basement after spending some time inside the basement.
- Fixed an issue that could cause some Survivors to be standing at the campfire.
- Fixed an issue that caused Prove Thyself not to affect the perk owner.
- Fixed the incorrect values displayed in all tiers of the Self-Care description, in all supported languages.
- Fixed an issue that made it impossible to rush vault a specific window in Badham Preschool.
- Fixed an issue that caused the Game Over score event to not work properly for The Pig.
- Fixed a crash that could happen when a survivor would disconnect during a Mori.
- Fixed a crash related to status effects that could happen at any time during gameplay.
- Fixed an issue that caused certain customization items to have placeholder string in all non-English languages.
- Partially fixed an issue that caused the Survivor icons in the HUD not to update upon a disconnect. Some disconnection scenarios may still result in the icon not being properly updated and are being investigated.
- Tentatively fixed an issue causing players to get stuck loading into a game if a player would disconnect during the loading sequence. This is a difficult to reproduce issue, and we'll be tracking the result of the change on the Live environment after this update.
- Added more logging to help identify the issue that could cause players to encounter the Bloodweb screen turning a solid color, and being unable to progress.
- Fixed an issue that caused the Bloodweb not to refresh when switching characters on the level up prompt.
- Fixed an issue that caused the Bloodweb not to refresh when switching characters while opening a Mystery Box.
- Fixed a prestige issue that allowed abusing the UI to Prestige low level characters.
- Fixed an issue that allowed players to swap characters at the same time as purchasing a node in the Bloodweb, causing the items purchased to appear on the wrong character, and causing the Bloodweb paths to break.
- Fixed an issue that could cause a crash in the tally screen of a Kill Your Friends match.

<!-- nav -->
&larr; [2.5.0 | Mid-Chapter](46-2-5-0-mid-chapter.md) · [Archive: PS4](../../index.md#archive-ps4) · [2.5.3 | Hotfix](48-2-5-3-hotfix.md) &rarr;
<!-- /nav -->
