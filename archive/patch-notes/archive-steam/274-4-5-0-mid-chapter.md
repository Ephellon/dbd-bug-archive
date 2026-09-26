---
title: "4.5.0 | Mid-Chapter"
section: "Archive: Steam"
article_id: 274
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/274-4-5-0-mid-chapter"
author: "Peanits"
published: "2021-02-09T15:26:36+00:00"
updated: "2021-02-09T15:26:36+00:00"
archived: "2026-09-26T17:09:44Z"
---

<!-- summary -->
## AI TL;DR

The 4.5.0 Mid-Chapter update revamps the HUD: player status moves left, objectives top-center, score alerts right, and new Hook Count and survivor-portrait widgets appear for killers and survivors. It also adds updated survivor locomotion animations, flashlight-while-crouching, and visual tweaks to maps, Nurse outfits, and the Clown’s base model.

Balance changes give The Clown separate Tonic and Antidote bottles with a faster reload and an Invigorated speed boost, adjust Trapper bear-trap escape odds and make the Wraith fully invisible past 20 m and improve uncloaking. Misc perk and Hex tweaks accompany numerous UI, audio and platform-specific bug fixes and PTB-resolved animation issues. Known issue: Thai UI text errors in tutorials.
<!-- /summary -->

<!-- nav -->
&larr; [4.4.2 | Bugfix Patch](272-4-4-2-bugfix-patch.md) · [Archive: Steam](../../index.md#archive-steam) · [4.5.1 | Bugfix Patch](275-4-5-1-bugfix-patch.md) &rarr;
<!-- /nav -->

# 4.5.0 | Mid-Chapter

![450Banner.png](../../images/d88369cf906c6df4-450banner.png)

## Content

**Tome VI & The Gilded Stampede Event**

- Tome VI for The Archives will start tomorrow on Feb. 10th at 11AM ET
- The Gilded Stampede event will start the day after on Feb. 11th at 11AM ET

**New HUD Layout - Several HUD elements have been moved or updated**

- The player status widget (player names, health states etc.) has been redesigned. Along with a number of graphical improvements to animations, the player status widget is now positioned on the left side of the screen. While this change was not made lightly, it was necessary in order to make the player names readable across all platforms and resolutions as well as make room for new HUD elements like the Hook Count.
- The objectives have been moved to the top center of the screen to give us more room to display detailed instructions.
- Score events and status effect alerts have been moved to the right side of the screen. This was primarily to bring the status effect alerts closer to the status effect indicators they reference.
- The number of visible score events has been increased when multiple events are triggered at the same time.

**New HUD Element - Hook Counts**

- Killers see a new widget which displays how many hooks they've earned during the match out of the possible total hooks. This is only visible to the Killer.
- Survivors see a new set of markers above each of the Survivor player's names. This lets the Survivor players know how many times each Survivor has been hooked. This is only visible to the Survivors.

**New HUD Element - Survivor Portraits**

- The healthy and injured health state icons have been replaced with each character's portrait.
- The Injured state has been improved from the PTB to be more obvious, especially for colorblind players.

**UI Scale Sliders**

- The Settings menu has been updated with two new slider settings that allow players to adjust the size of their UI. Players may adjust the size of the menus and HUD separately. This replaces the previous maximum scale value used in previous releases.

![PatchNotesDividerSmolWhite.png](../../images/3e51648d555c8a4c-patchnotesdividersmolwhite.png)

**Visual Update:**

- Visual updates to maps in Gideon Meat Plant and Asylum.
- Updated model and textures on 4 Nurse outfits.
- Update model, texture on the Clown base outfit and updated his VFX.

![PatchNotesDividerSmolWhite.png](../../images/3e51648d555c8a4c-patchnotesdividersmolwhite.png)

**Updated Survivor Locomotion**

**New:**

- Updated the posing for all Survivor locomotion animations.
- Added Start/Stop transition animations and quick turn animations.
- Added ability to use Flashlight while crouching.
- Updated crawling turn speed and added animation feedback for recovering.

**New from PTB:**

- Added new animation when entering the hatch while crawling.
- Updated Self-Heal fail animation.
- Slightly raised the camera when crawling.

![PatchNotesDivider.png](../../images/d693987990e49c09-patchnotesdivider-281-29.png)

## Balance

### Killers

**The Clown:**

Power:

- Clown now has two types of bottles: Tonic and Antidote.
- Tap Secondary Power to switch which will be thrown
- Hold Secondary Power to reload bottles
- Reload time is now 3 seconds (down from 5 seconds)

Antidote bottles:

- Release a gray cloud that activates and turns yellow after 2.5 seconds
- Antidote clouds last a total of 7.5 seconds and are smaller than Tonic clouds
- Overlapping Antidote and Tonic clouds causes both to disappear
- Survivors and The Clown gain the "Invigorated" status effect when they touch the Antidote cloud
- Invigorated grants 10% movement speed bonus for 5 seconds
- An Intoxicated Survivor touching a yellow Antidote cloud is no longer intoxicated
- Tonic clouds remain unchanged

Addons:

- Party Bottle: Thrown bottles emit confetti when shattering (was Ether 5 Vol%)
- Fingerless Parade Gloves: Bottles are thrown with a different arc that doesn't go as high but goes further
- Smelly Inner Soles: Greater move speed bonus when reloading (was Common, now Rare)
- Solvent Jug: Moderately increases the Invigorated effect duration
- Thick Cork Stopper: Smaller reload time reduction
- Spirit of Hartshorn: Moderately expands The Antidote cloud area (was Ether 10 Vol%)
- VHS Porn: Swaps yellow and purple color of Antidote and Tonic effects (was Rare, now is Common)
- Cigar Box: When any player becomes Invigorated, they see all other players' auras within a 16m radius
- Garish Makeup Kit: Considerably increases Invigorated Effect duration
- Tattoo's Middle Finger: Auras of Intoxicated or Invigorated survivors are revealed to you for 6 seconds

Audio:

- The Clown now has his own Terror Radius & Chase music.

![PatchNotesDividerSmolWhite.png](../../images/3e51648d555c8a4c-patchnotesdividersmolwhite.png)

**The Trapper:**

- Escaping from a Bear Trap now has a 1/6 (16.6%) chance of succeeding on each attempt, but is capped at a maximum of 6 attempts
- Addons that reduce the chance of escape increase the maximum number of attempts as well as reducing the chance per attempt

![PatchNotesDividerSmolWhite.png](../../images/3e51648d555c8a4c-patchnotesdividersmolwhite.png)

**The Wraith:**

- While cloaked, the Wraith is completely invisible (no shimmer) to Survivors when more than 20m away
- Increased the duration of the uncloak speed boost from 1.0s to 1.25s
- Restored a missing bone-rattle sound cue at the beginning of the Wraith's cloaking animation (sometimes referred to as "bell tech")
- Fixed an issue where the Wraith would appear to uncloak completely while kicking a generator or breaking a pallet or wall while cloaked. The Wraith now only uncloaks the *necessary bits*.
- Fixed an issue that caused the Wraith's add-on "**The Serpent**" to reset the uncloaking progress after completing an interaction. It will now leave the Wraith completely uncloaked and able to attack, and trigger an uncloak speed boost, after damaging a generator or breaking a pallet or wall.

### MISCELLANEOUS

**Hex: Undying:**

- While Hex: Undying is active, Survivors within 2/3/4 meters of any Dull Totem have their Aura revealed.
- When another Hex Totem is cleansed, that Totem's Hex transfers to the Hex: Undying Totem, deactivating Hex: Undying. Any tokens the transferred Hex had are transferred as well

**Misc. Perks:**

- Fixated: Now works while injured
- Iron Maiden: Effect lasts 30 seconds
- Second Wind: Durations now 28/24/20 seconds
- ~~Pebble~~ Diversion: Now charges in 40/35/30 seconds. Distance thrown now 20 meters at all tiers.

**Deep Wound:**

- Now always has a 20-second timer
- Frank's Mixtape and Stab Wound Study adjusted to have the same proportional impact on Survivors' Deep Wound timers
- Borrowed Time's tier adjustments are now the duration of the Endurance status effect at 10/12/15 seconds

**Mangled:**

- Mangled status effect always lasts until fully healed
- Vigil no longer affects Mangled
- Begrimed Head: Removed repair speed debuff, added Hemorrhage status effect
- Rusty Attachments: Only applies Mangled to injured Survivors

![PatchNotesDivider.png](../../images/d693987990e49c09-patchnotesdivider-281-29.png)

## Bug Fixes

- Fixed a hitch occurring in the Loadout Panel when selecting an item
- Fixed a hitch when opening the Bloodweb after a certain level
- Fixed an issue that could cause some survivors passively falling asleep to not count towards the "Dream Master" achievement
- Fixed some issues regarding user impersonation
- Fixed a crash that could occur on the initial interaction screen
- Fixed an issue that occurred occasionally after the killer disconnects from a match where the Player Level would display incorrect Level and Devotion values
- Fixed an issue where the Survivor could get stuck and not be able to be picked up if downed while repairing a generator.
- Fixed an issue where the Flashlight cone would not expand after successfully blinding the Killer
- Fixed an issue where the 1st generator piston would move abnormally fast.
- Fixed an issue with Steve's lips while gesturing.
- Fixed an issue with the camera when the Nurse would carry a Survivor and attack.
- Fixed an issue where Jane and Kate chest physics would not work properly.
- Fixed an issue where the Oni's armor would be floating.
- Fixed an issue where the Clown's hair would be floating.
- Fixed an issue where Totems located next to the Combine Harvester's wheel on Coldwind Farm couldn't be cleansed.

**Audio:**

- Fixed an issue where Elodie is screaming louder than other survivors.
- Fixed various surface tags for footsteps and impacts
- Fixed an issue where Doctor static attack doesn't play his sound.
- Fixed an issue with some locomotion survivor animations
- Fixed an issue with Legion customization "Hooded Leather Jacket"

**PC only:**

- Fixed a crash that could occur when pasting an empty text in the promo code

**Windows Store only:**

- Fixed an issue when launching the game and navigating directly to Play as Killer/Survivor, the user's currency would display as 0-0-0 instead of the real values.

**Switch only:**

- Fixed an issue where multiple sound effects weren't echoed on Nintendo Switch

**PS5 only:**

- Fixed an issue where the player wouldn't be brought back to the initial interaction screen when the internet connection is lost

**Xbox One, Xbox Series X, Playstation 4, Playstation 5 only:**

- Fixed a crash that would occur after loading the tutorial while the game is not completely installed

**Fixed Issues from PTB**

- Fixed an issue where Survivor would not be able to nod their head up/down anymore.
- Fixed an issue where Survivor character would stuttered changing direction quickly.
- Fixed an issue where the Survivor would play the incorrect animation when bleeding out of Deep Wound.
- Fixed an issue where the players would be able to steer character during Dead Hard.
- Fixed an issue where the Survivor would snap back to their original position after letting go of repairing a generator.
- Fixed an issue where the character would stutter when using the flashlight while moving.
- Fixed an issue where the character would remain in fall stance after vaulting.
- Fixed an issue where the character would not play the Dead Hard animation properly from idle.
- Fixed an issue where the Survivor would clip through lockers doors while rushing out.
- Fixed an issue where the Survivor carrying an item would clip through the ground.
- Fixed and issue where Ash hand would jitter while carrying an item.
- Fixed an issue where character would "T" stance when infected by the Plague and interacting with the exit gate
- Fixed an issue where character would "T" stance when interacting with fountains.

![PatchNotesDivider.png](../../images/d693987990e49c09-patchnotesdivider-281-29.png)

## Known Issues

- Some tutorial and UI texts show incorrect characters in Thai language on Steam.

<!-- nav -->
&larr; [4.4.2 | Bugfix Patch](272-4-4-2-bugfix-patch.md) · [Archive: Steam](../../index.md#archive-steam) · [4.5.1 | Bugfix Patch](275-4-5-1-bugfix-patch.md) &rarr;
<!-- /nav -->
