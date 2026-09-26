---
title: "3.0.1 | Hotfix"
section: "Archive: Steam"
article_id: 27
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/27-3-0-1-hotfix"
author: "Peanits"
published: "2020-02-28T17:43:38+00:00"
updated: "2020-03-02T15:22:44+00:00"
archived: "2026-09-26T19:27:48Z"
---

<!-- summary -->
## AI TL;DR

Ghost Face received a suite of balance tweaks: stalk-rate add-ons now apply only when not leaning, the base Killer Instinct duration and its add-ons were nudged upward, and the detection area for revealing him expanded by 8 %. Visual and audio polish removed the stun VFX, reduced hit camera shake, and silenced the proximity sound in Night Shroud. The hotfix also corrected numerous perk and add-on bugs, fixed animation, pallet, exhaustion and camera issues across multiple killers, addressed crashes in lobby and match end, and added logging for ranking problems while improving audio cues and resolution changes.
<!-- /summary -->

<!-- nav -->
&larr; [2.7.1 | Hotfix](26-2-7-1-hotfix.md) · [Archive: Steam](../../index.md#archive-steam) · [3.0.2 | Hotfix](28-3-0-2-hotfix.md) &rarr;
<!-- /nav -->

# 3.0.1 | Hotfix

## Balance

- Removed the stun VFX when Killers entered stun state.
- Reduced the camera shake on successful hits.

**The Ghost Face:**

- Slightly reduced the stalk rate add-ons: Telephoto Lens (to -0.25 seconds, down from -0.5 seconds total stalk time required), Night Vision Monocular (to -0.75 seconds, down from -1.0 seconds total stalk time required).
- Adjusted all stalk rate add-ons (Philly, Telephoto Lens, Knife Belt Clip and Night Vision Monocular) so that they only affect stalking while not leaning. Stalking while leaning is twice faster than normal stalking.
- Slightly increased the Killer Instinct base duration to 2 seconds from 1.5 seconds.
- Slightly increased Killer Instinct add-ons: Marked Map (to 1 second, up from 0.5 seconds), Victim’s Detailed Routine (to 1.5 seconds, up from 1.0 seconds).
- Slightly increased the Detection area in the center of screen for Survivors attempting to reveal The Ghost Face by 4% on each side of the screen (total of 8%).
- Fixed an issue that allowed The Ghost Face to stay Night Shroud when stunned by a pallet.
- Fixed an issue that allowed Ghost Face to continue stalking already Marked Survivors.
- Removed the proximity Sound that the Killer generated while in Night Shroud (only his clothes emit sound while he moves).

## Bug Fixes

- Fixed an issue that caused the Wake Up! perk to grant 5/10/15% increased action speed to all interactions at all times.
- Fixed an issue that caused the Bamboozle perk not to have an activation sound.
- Fixed an issue that caused the Barbecue & Chili, Fire Up, Remember Me and We're Gonna Live Forever perks to visually only gain up to 3 tokens.
- Fixed an issue that caused Sprint Burst not to always trigger Exhaustion.
- Fixed an issue that caused the Spies From The Shadows perk to go on cooldown whenever a Survivor triggered a crow outside of the maximum effect radius.
- Fixed an issue that caused the Play With Your Food perk to gain a token when downing the Obsession.
- Fixed an issue that caused The Legion's Nasty and Filthy Blade add-ons to increase all interaction times.
- Fixed an issue that caused The Ghost Face add-on Telephoto Lense not to impact the duration of a Survivor staying marked.
- Fixed an issue that caused The Doctor's illusionary pallets to spawn perfectly straight instead of leaning on an asset like a regular pallet.
- Tentatively fixed an issue that could cause permanent Exhaustion.
- Fixed an issue that could cause the Exhaustion status effect to appear on screen without the dial representation.
- Fixed an issue that caused a delayed reset on the users progress bar when failing a skill check.
- Fixed an issue that allowed Survivors to stay in the locker in the crawl state when the Deep Wound timer ended.
- Fixed an issue that caused The Nightmare and The Huntress' lullaby to get obstructed by occlusion.
- Fixed an issue that caused The Huntress' camera to shake on a successful hatchet hit.
- Fixed an issue that caused the Survivors' camera to shake when hit by the Killers.
- Fixed an issue that caused the Killers red stain to be visible on their model in-game.
- Added more logging to investigate the ranking issue.
- Fixed an issue that caused placeholder text strings to appear when receiving a Player Pips Error message. We have modified these strings in English. Please note that the other translations will come in a future patch.
- Fixed an issue that allowed The Trapper to place traps while falling.
- Fixed an issue that caused multiple characters not to have proper idle animations in the Store.
- Fixed an issue that caused escaping Survivors audio to keep playing within the exit threshold.
- Fixed an issue that caused the title to crash for the host when The Plague vomits as the match ended.
- Fixed an issue that could cause a crash when switching roles in the lobby.
- Fixed an issue that caused an increase of auto-save checks in the Bloodweb.
- Fixed a case that caused multiple issues in the pre-lobby when disconnecting from the Network during the loading screen into a match, and reconnecting right before returning to the pre-lobby.
- Fixed an issue that caused the Anniversary Event audio not to play automatically when launching the game.
- Fixed an issue that caused an audio stinger not to play correctly when being shocked by The Doctor or tiering up in Madness.
- Misc audio improvements.
- Fixed an issue that prevent users from changing the resolution while in Windowed mode.

<!-- nav -->
&larr; [2.7.1 | Hotfix](26-2-7-1-hotfix.md) · [Archive: Steam](../../index.md#archive-steam) · [3.0.2 | Hotfix](28-3-0-2-hotfix.md) &rarr;
<!-- /nav -->
