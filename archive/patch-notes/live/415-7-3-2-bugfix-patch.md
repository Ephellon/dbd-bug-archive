---
title: "7.3.2 | Bugfix Patch"
section: "Live"
article_id: 415
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/415-7-3-2-bugfix-patch"
author: "Peanits"
published: "2023-10-26T14:27:37+00:00"
updated: "2023-10-26T14:53:57+00:00"
archived: "2026-09-26T17:08:44Z"
---

<!-- summary -->
## AI TL;DR

The Skull Merchant’s Low Power Mode add-on was overhauled, halting drone rotation entirely and removing the 25% power-cooldown reduction. Shattered Square now spawns up to 18 pallets to avoid empty sections, with loop safety tweaked. The patch also bundles extensive fixes: audio no longer plays from collected memory shards; numerous animation and clipping issues for Huntress, Xenomorph, female survivors, Legion, Cannibal and Demogorgon were resolved; map-specific spawn and collision bugs on Nostromo Wreckage, MacMillan Estate, Temple of Purgation, Eyrie of Crows, Raccoon City Police Station, Coldwind Farm, Disturbed Ward, and Father Campbell’s Chapel were corrected; Haunted By Daylight lighting resets correctly; Skull Merchant claw traps and drone tracking work after disconnects; and a rare mid-trial disconnect bug was fixed.
<!-- /summary -->

<!-- nav -->
&larr; [7.3.1 | Bugfix Patch](414-7-3-1-bugfix-patch.md) · [Live](../../index.md#live) · [7.3.3 | Bugfix Patch](417-7-3-3-bugfix-patch.md) &rarr;
<!-- /nav -->

# 7.3.2 | Bugfix Patch

![PatchNotesBanner732.jpg](../../images/db2ef9e8990124cf-patchnotesbanner732.jpg)

## Release Schedule

Update releases: 11a.m. ET

![PatchNotesDivider.png](../../images/ca641380905546af-microsoftteams-image-281-29.png)

## Content

### Killer - The Skull Merchant

- Reworked Low Power Mode Add-on:
  - Now decreases Drone Rotation speed by 100%, effectively stopping rotation.
  - No longer decreases Power cooldown by 25%.

### Environment/Maps

The maximum number of pallets spawned in the Shattered Square Map has been increased to 18 to prevent large areas of the map from spawning with no pallets. The quality of the loops were also updated to reduce their safety. We hope this adds better gameplay for both roles.

*Note: The map is not guaranteed to generate with this many pallets and will instead prematurely stop spawning pallets if the minimum pallet requirement has been reached and there are no more valid positions far enough from other pallets.*

![PatchNotesDivider.png](../../images/ca641380905546af-microsoftteams-image-281-29.png)

## Bug Fixes

### Audio

- Memory fragment shards that have been collected or have despawned no longer produce SFX.

### Characters

- Fixed an issue that caused The Huntress reload animation to cause motion sickness when paired with the Iron Maiden perk.
- Fixed an issue that caused The Xenomorph pick-up animation from a Locker to jitter in a specific Locker inside the Main Building.
- Fixed an issue that caused the heads of all female Survivors to clip through the Hook during the struggle phase.
- Fixed an issue that caused The Legion's upper body to be contorted while the camera snaps back into position after performing Memento Mori.
- Fixed an issue that allowed The Cannibal's camera to clip through Lockers when performing a basic attack on them.
- Fixed an issue that caused survivors to experience clipping with the artist when picking up and putting down survivors.
- The Demogorgon’s Portals’ auras now properly appear after having performed a Mori.

### Environment/Maps

- Fixed a potentially broken Killer spawn point on Nostromo Wreckage.
- Fixed a killer blocking collision on MacMillan Estate Realm.
- Fixed an issue on Suffocation Pit where the Nightmare could not place his Dream Snares.
- Fixed a killer blocking collision issue on the Temple of Purgation.
- Fixed an issue where branches of trees could clip through the main building in Eyrie of Crows.
- Fixed an issue where the Tonic Fumes of the clown could go through ceiling in buildings of the MacMillan Estate Realm.
- Fixed an issue on Raccoon City Police Station where The Nemesis' tentacles could go through walls.
- Fixed an issue in Coldwind Farm where items could be hidden in the ground near the corn rows.
- Fixed an issue on Disturbed Ward where survivors could heal each other through walls.
- Updated the layout of the combine harvester where small killers could not interact with survivors that are standing on one side.
- Fixed an issue where players could land on top of pews in the Father Campbell's Chapel.
- Fixed an issue in Eyrie of Crows where survivors healing each other can end up stuck in roots.

### Event - Haunted By Daylight

- Lighting now properly resets when entering the Void during The Dredge’s Nightfall or while in The Nightmare’s Dreamworld.

### Killer - The Skull Merchant

- Claw traps are properly destroyed when a survivor disconnects without being replaced by a bot in a Custom Game.
- The Map now properly tracks the Skull Merchant’s’ drones when equipped with Red Twine Add-On.

## Misc

- Fixed an issue that could disconnect players mid-trial.

<!-- nav -->
&larr; [7.3.1 | Bugfix Patch](414-7-3-1-bugfix-patch.md) · [Live](../../index.md#live) · [7.3.3 | Bugfix Patch](417-7-3-3-bugfix-patch.md) &rarr;
<!-- /nav -->
