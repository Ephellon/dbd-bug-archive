---
title: "2.7.1 | Hotfix"
section: "Archive: Steam"
article_id: 26
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/26-2-7-1-hotfix"
author: "Peanits"
published: "2020-02-28T17:42:30+00:00"
updated: "2020-03-02T15:21:14+00:00"
archived: "2026-09-26T17:09:33Z"
---

<!-- summary -->
## AI TL;DR

Network disconnect handling and End Game Collapse behavior were overhauled, fixing loops of disconnect audio, erroneous host messages, infinite loading screens, and various end-game timer issues. The hotfix also resolved a range of killer and survivor bugs—Ash’s voice-overs, The Shape’s standing-kill radius, The Clown’s gas crosshair, The Trapper’s window-vault snag, The Wraith’s blood-drip glitch, The Plague’s emblem scoring, and Nea’s missing textures—plus aura dimming on Mount Ormond Resort, window-vault stutter on Shrimp Boat, and added logging for entity-blocking and camera anomalies.
<!-- /summary -->

<!-- nav -->
&larr; [2.6.4 | Hotfix](25-2-6-4-hotfix.md) · [Archive: Steam](../../index.md#archive-steam) · [3.0.1 | Hotfix](27-3-0-1-hotfix.md) &rarr;
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
- Fixed an issue that caused Nea's Prestige and Legacy torso to have missing textures on her arms.

<!-- nav -->
&larr; [2.6.4 | Hotfix](25-2-6-4-hotfix.md) · [Archive: Steam](../../index.md#archive-steam) · [3.0.1 | Hotfix](27-3-0-1-hotfix.md) &rarr;
<!-- /nav -->
