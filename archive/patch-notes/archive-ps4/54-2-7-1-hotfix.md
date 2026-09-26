---
title: "2.7.1 | Hotfix"
section: "Archive: PS4"
article_id: 54
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/54-2-7-1-hotfix"
author: "Peanits"
published: "2020-02-28T18:57:07+00:00"
updated: "2020-03-02T19:46:51+00:00"
archived: "2026-09-26T17:09:51Z"
---

<!-- summary -->
## AI TL;DR

Ash’s voice lines, The Shape’s standing kill radius, and several killer visual quirks were fixed, alongside major network and end-game stability work. The PS4 hotfix resolves looping disconnect audio, erroneous host messages, match-cancellation warnings, infinite loading screens, and lobby-timer crashes; it also corrects End Game Collapse timing, ensures immediate sacrifice and ritual progress after collapse, and fixes progression for The Savior, Blood Dance and Reconstruction rituals. Additional tweaks address flashlight aim for Ash’s hand cosmetic, aura visibility, camera shake, weapon blood-drip glitches, map-specific vaulting bugs, inaccurate perk values, and missing Nea textures.
<!-- /summary -->

<!-- nav -->
&larr; [2.7.0 | Mid-Chapter](53-2-7-0-mid-chapter.md) · [Archive: PS4](../../index.md#archive-ps4) · [3.0.0 | Ghost Face](55-3-0-0-ghost-face.md) &rarr;
<!-- /nav -->

# 2.7.1 | Hotfix

## Bug Fixes

- Fixed an issue that could cause the disconnect audio to loop for the remainder of the match for all players if a Survivor disconnected while on a hook.
- Fixed an issue that caused an erroneous Disconnected From Host message on the main menu when getting disconnected from the network during the public lobby timer.
- Tentatively fixed an issue that could cause a "Match Canceled" message to appear when the Killer disconnected during a match.
- Fixed an issue that caused multiple gameflow issues when a client disconnects during the 5 second lobby countdown timer, and re-connected on the splash screen.
- Fixed an issue that could cause an infinite loading screen when a client lost Network connection while loading into a match.
- Fixed an issue that caused the End Game Collapse timer not to be slowed when the conditions were met and a downed Survivor had escaped.
- Fixed an issue that caused the End Game Collapse not to end when the timer ran out if the Killer picked up a Survivor at the last possible second.
- Fixed an issue that caused Survivors not to get immediately sacrificed when they were opening an exit gate or interacting with a Jigsaw box when the End Game Collapse timer ended.
- Fixed an issue that made it impossible to earn progress on The Savior Ritual when unhooking a Survivor after the End Game Collapse had started.
- Fixed an issue that made it impossible to earn progress on the Blood Dance daily ritual when healing a Survivor after the End Game Collapse had started.
- Fixed an issue that caused The Reconstruction Ritual's rate of progress to be lowered when there was more than 1 Survivor in the match.
- Fixed an issue that caused Ash not to play any VOs when selected or when joining a lobby.
- Adjusted the flashlight items aim when held by Ash's Ashy Slashy hand customization item to be more in line with regular cosmetics. A more permanent fix will come in a future patch.
- Fixed an issue that made it possible to see other players as blobs through auras.
- Fixed an issue that caused the camera to shake after The Trapper picked up a bear trap.
- Fixed an issue that caused the certain weapon customization items to continue dripping blood when The Wraith quickly cloaked after breaking a pallet/generator with the "The Serpent" - Soot add-on.
- Fixed an issue that allowed The Shape to be able to use his standing Kill within a 2.5 meter radius.
- Fixed an issue that caused the cross hair when being affected by The Clown's gas to be almost non-visible.
- Fixed an issue that caused certain Killers to get stuck when vaulting over the window on the Shrimp Boat in The Pale Rose map.
- Fixed an issue that caused some placeholder strings to appear in the description for certain Nea head cosmetics in all non-English languages.
- Fixed an issue that caused auras to appear very dim in the map Mount Ormond Resort
- Tentatively fixed an issue that caused the Survivors not to receive points when completing a generator
- Tentatively fixed an issue that caused the Survivors' camera to follow the Killer when hooked. Added extra logging to better help track identify the issue.
- Added extra logging to help identify the issue with the Entity blocker sometimes not blocking windows, with and without Bamboozle.
- Fixed an issue that prevented The Plague scoring points in the Chaser emblem when downing Survivors with Corrupt Purge
- Fixed an issue that caused the camera to shake from EGS during tally screen
- Fixed an issue that caused the Left Behind perk to have the wrong values. Values should be 55%/65%/75%.
- Fixed an issue that caused Nea's Prestige torso to have missing textures on her arms.

<!-- nav -->
&larr; [2.7.0 | Mid-Chapter](53-2-7-0-mid-chapter.md) · [Archive: PS4](../../index.md#archive-ps4) · [3.0.0 | Ghost Face](55-3-0-0-ghost-face.md) &rarr;
<!-- /nav -->
