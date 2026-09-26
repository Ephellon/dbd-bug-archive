---
title: "3.5.0 | Mid-Chapter"
section: "Archive: Windows Store"
article_id: 118
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/118-3-5-0-mid-chapter"
author: "Peanits"
published: "2020-02-28T20:27:08+00:00"
updated: "2020-02-28T21:35:05+00:00"
archived: "2026-09-26T19:28:42Z"
---

<!-- summary -->
## AI TL;DR

The Doctor receives a major overhaul: Treatment Mode and static-field VFX are removed, Shock Therapy cooldown is set to 1.5 s, range increased 10 % and a new secondary ability, Static Blast, is added with its own score event. The Oni’s turn-speed limit on Demon Strike is lifted, Gatekeeper emblem scores are flattened, and Hex : Ruin now regresses idle generators. A Compendium page lets players revisit previous Tomes, a new Rift and challenges appear for Tome II, and party, lobby and tally chat become cross-compatible with Steam. The Treatment Theatre map is visually reworked, invert-camera keybinding is removed, Twitch challenges and the Cursed Legacy lobby are disabled. The update is largely a collection of extensive bug fixes covering killers, maps, perks, UI and audio.
<!-- /summary -->

<!-- nav -->
&larr; [3.4.2 | Hotfix](117-3-4-2-hotfix.md) · [Archive: Windows Store](../../index.md#archive-windows-store) · [3.5.1 | Hotfix](119-3-5-1-hotfix.md) &rarr;
<!-- /nav -->

# 3.5.0 | Mid-Chapter

## Features & Content

- Feature - Added a Compendium page in the Archives. This page allows users to go back to previous Tomes and complete challenges. Completing challenges from a previous Tome will not give the user Rift Fragments.
- Feature - Added a new Rift and Challenges for Tome II in the Archives.
- Feature - Showing/Hiding the tally screen chat is persistent after every match. This feature has been added to each type of chat (party, online and tally) and is independent for each chat.
- Feature - Added support for the party, lobby and tally chat. The chat is cross compatible with Steam users.
- Feature - Removed the invert camera in-game keybinding and from the Controls menu. This option is still available in the Settings menu.
- Content - Updated the Treatment Theatre map (see details below in the BALANCE section).
- Content - Removed Twitch Challenges feature.
- Content - Disabled the Cursed Legacy thematic lobby.

## Balance

- Gatekeeper Emblem: Flattened score value of all remaining generators so now all generators are worth the same amount (1 point per minute) regardless of the duration that they remain in the match. Also added an additional score for both gate remaining unopened at the end of the match.
- Hex: Ruin redesigned: All generators are affected by Hex: Ruin; if a generator is not being worked on, it regresses at 100/150/200% the normal regression rate. The Hex effect persists as long as the related Hex totem is standing.
- The Oni: Removed turn speed limitation on Demon Strike. Implemented a hard cap on the turn angle during Demon Strike.

**The Doctor changes**

- Updated the illusionary Doctor animation to play The Doctor's in-game idle animation instead of the menu idle animation.
- Removed Treatment Mode and the Static Field VFX. The Doctor will no longer need to switch stances to use Shock Therapy, or to use a regular attack.
- Added Doctor-specific chase music.
- Added a new special ability, Static Blast, as the secondary power (see below for more information).
- Set the cooldown of Shock Therapy to 1.5 seconds. This means it will take 1.5 seconds before The Doctor can hit with his primary weapon, use Shock Therapy or use Static Blast.
- Increased the base range of Shock Therapy by 10%.
- Range increasing add-ons no longer increase the width of the Shock Therapy, only the length. See the add-on changes below for more information.
- Reduce charging move speed to 67% normal from 70% normal to keep the speed the same at 3.08 m/s.
- Madness regresses while outside the Terror Radius, and does not regress while inside it.
- "Order" - Class I add-on: Slightly increases the Madness inflicted by Static Blast.
- "Order" - Class II add-on: Moderately increases the Madness inflicted by Static Blast.
- "Order" - Carter's Notes add-on: Considerably increases the Madness inflicted by Static Blast.
- "Calm" - Class I add-on: Slightly increases terror radius while Static Blast is ready. Slightly decreases terror radius while Static Blast is on cooldown.
- "Calm" - Class II add-on: Moderately increases terror radius while Static Blast is ready. Moderately decreases terror radius while Static Blast is on cooldown.
- "Calm" - Carter's Notes add-on: Considerably increases terror radius while Static Blast is ready. Considerably decreases terror radius while Static Blast is on cooldown.
- Moldy Electrode add-on: Slightly increases charge time and attack range of Shock Therapy.
- Polished Electrode add-on: Moderately increases charge time and attack range of Shock Therapy.
- High-Stimulus add-on: Considerably increases charge time and attack range of Shock Therapy.
- Interview Tape add-on: Rarity changed from Uncommon to Rare.
- "Obedience" - Carter's Notes add-on: Rarity changed from Very Rare to Rare. Skill checks have a considerable chance to turn counter-clockwise for Survivors with Madness 2/3.
- Scrapped Tape: Name changed to Iridescent Queen. Rarity changed from Uncommon to Ultra Rare. Survivors hit with Shock Therapy or Static Blast acquire a lingering Static Charge. If a Survivor with Static Charge is within 4 meters of another Survivor, the Survivor receives a shock with identical effects as the Shock Therapy and Static Blast.
- Iridescent King add-on: Shock Therapy and Static Blast cause the Survivor to gain a random Madness affliction.
- Renamed the Shock Therapy score event to Pacified.
- Added a score event for hitting Survivors with Static Blast (Tranquilized - 300 Bloodpoints).

**Static Blast**

Static Blast is a new mechanic for The Doctor. We removed the Treatment Mode and the ability to switch between modes. The Doctor will always be able to hit with his primary weapon, use Shock Therapy (which now has a 1.5-second cooldown), and can use Static Blast. Static Blast takes 2 seconds to activate, and has a 60 second cooldown. Effects:

- The Doctor's Static Blast causes all Survivors within his terror radius to gain 50 Madness points.
- The Doctor will laugh if the Static Blast affects any Survivor.
- Affected Survivors will scream; they give away their location if their Madness level increases.
- Survivors outside the Terror Radius hear a direction-neutral audio cue when the ability is being charged and when it fires.
- Survivors inside the Terror Radius hear direction-revealing audio cues for the charge and fire of the ability.
- Scoring event for hitting Survivors.

**Snap Out Of It adjustments**

- Missing a skill check will regress the progression bar by 1/4th instead of all the way.
- Skill checks will trigger at every quadrant of the progress bar.
- Releasing the Snap Out Of It action will keep the progress made instead of resetting.
- Snapping Out Of It sends Survivors to Madness Level 1 instead of Level 2.

**Treatment Theatre map update**

- Completely reworked the visual look and feel of the map.
- Made the map darker.
- Changed the layout to be more rectangular than square.
- Added flickering signs in the hallways near rooms that spawn generators.
- Hid totems better.
- Made each map tile unique (no repeated tiles).
- Balanced the distribution and safety of pallets.
- Balanced the distribution of hooks.
- Updated the logic of vault spawns and activations for the Doctor's Office and the Treatment Room.

**UI Improvements**

- Progress bars for Killer powers will now show the Killer's power icon.
- Added platform prompts when accepting / claiming a Challenge node in the Archives.
- Changed the level icon shapes in the Tome from squares to diamonds.
- The level navigation menu becomes golden when a Tome is mastered.

## Bug Fixes

**Killer related**

- Fixed an issue that caused not all Survivors to see blood orbs when The Oni had the Renjiro's Bloody Glove add-on equipped.
- Fixed an issue that caused The Oni's Kanobo to disappear when damaging a generator or destroying a pallet.
- Fixed an issue that caused The Wraith and The Spirit not to have their re-appearance lunge speed burst.
- Fixed an issue that could cause The Nightmare to be unable to place Dream Snares if stunned while placing one.
- Fixed an issue that caused The Trappers bear trap auras to be blocked by multiple assets in most maps.
- Fixed an issue that caused The Trapper to get stuck in an infinite loop when stepping in a bear trap that was placed close to another trap.
- Fixed an issue that caused The Trapper to step in multiple bear traps at once if they are in close proximity.
- Fixed an issue that caused The Trapper not to properly trigger his own bear traps when set by the Iridescent Stone add-on.
- Fixed an issue that caused Survivors to be able to untrap another Survivor from The Trapper's bear traps while the Survivor was being picked up out of the trap.
- Fixed an issue that caused The Doctor's Iridescent King add-on not to always apply its 5 afflictions within 5 shocks. In addition to this bug fix, we also added scoring events for feedback on which afflictions were applied.
- Fixed an issue that caused The Doctor's Shock Therapy not to interrupt Survivors using a flashlight.
- Fixed an issue that caused Survivors to block a part of The Hags screen when performing a basic attack while carrying a Survivor.
- Fixed an issue that allowed The Hag, The Hillbilly and The Demogorgon to interact with cleansed totem debris.
- Fixed an issue that caused The Ghost Face to see inside assets when attacking while having a Survivor on their shoulder.
- Fixed an issue that caused The Legion to see inside of lockers when attacking while having a Survivor on their shoulder.
- Fixed an issue that caused The Legion to perform a basic attack on the first hit of Feral Frenzy if activated while being blinded.
- Fixed an issue that caused The Legion to instantly down a Survivor with Feral Frenzy if blinded after activating it.

**Map specific**

- Fixed an issue that made it impossible to interact with a specific chest or Jigsaw box when in front of a tree in the Temple of Purgation map.
- Fixed an issue that caused the camera to clip through walls when being sacrificed on specific hooks in the Hawkins National Laboratory map.
- Fixed an issue that caused some of the flags inside the manor building to have missing textures on one side in the Family Residence map.
- Fixed an issue that made it impossible for The Nurse to blink in the area around the base of the shrine in the Sanctum of Wrath map.
- Fixed an issue that made it impossible to interact with a specific chest of Jigsaw box when it spawned facing a Buddha statue in the Sanctum of Wrath map.
- Fixed an issue that made it difficult for The Nurse to blink in or around the gazebo tile in the Yamaoka Estate maps.
- Fixed an issue that made it difficult for The Nurse to blink in or around the shrine tile in the Yamaoka Estate maps.
- Fixed an issue that made it impossible for The Nurse to blink around the shack tile in the Backwater Swamp maps.
- Fixed an issue that caused the small boats in the Backwater Swamp maps to have incorrect textures.
- Fixed an issue that caused some trees to have the wrong textures on their base in the Backwater Swamp maps.
- Fixed an issue that caused the tops of the corn to appear black in the Coldwind Farm maps.
- Fixed an issue that caused bear traps to sink into the ground on multiple areas around the silo building in the Torment Creek map.
- Fixed an issue that caused the railing just in front of the basement in the farm house to partially lack collision in the Thompson House map.
- Fixed an issue that caused a visible ground seam in the lodge of the Blood Lodge map.
- Fixed an issue that could cause a placeholder tile to spawn in the Wrecker's Yard map.
- Fixed an issue that caused the chandelier in the chapel to be floating unattached to anything in the Father Campbell's Chapel map.
- Fixed an issue that allowed players to climb on top of a rock in the Father Campbell's Chapel map.
- Fixed an issue that caused an impassable gap for Killers when a tree spawned too close to the asylum building in the Disturbed Ward map.
- Fixed an issue that caused players to be floating above the ground on most tiles in the Mount Ormond Resort map.
- Fixed an issue that caused multiple Killer belongings to be offset or floating when spawned on the watch tower in the Mount Ormond Resort map.
- Fixed an issue that caused multiple texture issues on the hills in the Mount Ormond Resort map.
- Fixed an issue that caused the windows and walls to be misaligned in the 2 story house in the Badham Preschool maps.
- Fixed an issue that caused the boarded windows to appear very dark in the Badham Preschool and Lampkin Lane maps.
- Fixed an issue that made it impossible to vault through a fence window on one side in the Lampkin Lane map.
- Fixed an issue that caused a log pile to be lacking hitbox collision, allowing projectiles and The Cannibals chainsaw not to detect collision in the Lampkin Lane map.
- Moved the generator on the top floor of a 2 story house in the Lampkin Lane map that caused players to undesirably vault the window instead of repair.
- Darkened the grass texture in the Lampkin Lane map.
- Misc LOD fixes and improvements.

**Perks**

- Fixed an issue that caused the Kindred perk to stay active when the perk owner disconnected while it was active.
- Rainbow maps will now track chests if revealed by a perk that shows chests (ie: Detective's Hunch).
- Fixed an issue that caused the Kindred perk to stay active for another player with the perk equipped if the perk owner disconnected while it was active.
- Fixed an issue that caused Sprint Burst to trigger when the button was pressed during specific interactions where the player moves but cannot sprint (vaulting, entering/exiting locker).
- Fixed an issue that caused Survivors not to get notified of Hex: Huntress Lullaby when succeeding a great skill check.
- Fixed an issue that made it impossible for The Legion to Frenzy vault over a pallet while it was being reset with the Any Means Necessary perk.

**Miscellaneous**

- Fixed an issue that could cause the 4th Survivor slot in the public lobby not to fill.
- Fixed an issue that caused Survivors killed by the End Game Collapse not to count towards the Reverent Challenge in Tome 1.
- Added a retry mechanism for sending Archive Challenge progression to the backend.
- Potentially fixed an issue that could cause Survivors to have a permanent Haste effect from perks or when getting hit.
- Potentially fixed an issue that could caused Killers to get permanently blinded by the flashlight. Added addition logging to help identify the issue.
- Fixed an issue that caused a loud noise notification to trigger on the exit gates when they were powered.
- Fixed an issue that could cause players to become stuck between a hooked Survivor and a wall when canceling an unhook action.
- Fixed an issue that caused Survivors to snap backwards when picking up and dropping an item without moving.
- Fixed an issue that could cause the Killer to crash when loading into the match as The Nurse with the Mother Mercy outfit.
- Fixed an issue that caused male Survivors hands to be floating above the Pool of Devotion when cleansing their sickness.
- Fixed an issue that caused the bear trap in the beginning of the Killer Tutorial to appear closed.
- Fixed an issue that caused the Claudette AI to move around once she begins the struggle phase in the Killer Tutorial.
- Fixed an issue that caused skirts to appear stretched and warped in the Store and in The Rift.
- Misc cosmetic and VFX fixes, improvements and optimizations.
- Fixed an issue that caused only the party leader's cross-play permissions to be taken into account.
- Fixed an issue that caused great skill checks not to count towards the Nerves of Steel achievement.

**Audio & Localization**

- Misc audio adjustments and improvements.
- Misc localization and translation improvements.

**UI & HUD**

- Fixed an issue that caused tooltips for items in the free track to overlap on the Tier progress.
- Fixed an issue that caused the Broken status effect to stay displayed on the portrait in the HUD of a Survivor that is sacrificed, killed or disconnected.
- Fixed an issue that caused the Doctor's Madness effect to stay displayed on the portrait in the HUD of a Survivor that is sacrificed, killed or disconnected.
- Fixed an issue that caused the Archives widget to disappear from the tally screen when returning to it after spectating the match.
- Fixed an issue that caused players rank to display inconsistently in the tally screen across all players if pips were lost or gained.
- Fixed an issue that caused the spectate button to appear briefly despite not being able to spectate when leaving the tally screen.
- Fixed an issue that caused medkit heals not to count towards the Benevolent emblem.
- Fixed an issue that prevented Spectators from switching between Survivor and Killer when there was only 2 players in a Custom match.
- Fixed an issue that caused the player names on the right side of the screen in a Custom Game lobby to have no function when selecting one.
- Fixed an issue that caused The Clown's Reload progress bar to behave incorrectly when the Kill prompt was present in the HUD.
- Fixed an issue that caused certain tooltips not to update when switching pages or characters.
- Fixed an issue that caused the Loadout to appear on screen after the lobby timer reached 0 seconds.
- Fixed an issue that caused the Character Info to disappear when searching for a match as a Survivor.
- Fixed an issue that allowed non-host players in a Play As Survivor lobby to open the Archives while searching for a match.
- Fixed an issue that caused the item tooltip to stay displayed when interacting with a node as a new Bloodweb level generates.
- Fixed an issue that caused the banner to refresh each time when attempting to cycle through the new content when only 1 banner was available.
- Fixed an issue that caused the switch role tooltip in Custom Game lobbies to display when the button was disabled.
- Misc UI improvements.

## Known Issues

- The Plague's vomit splash can be very loud.
- The Doctor's Iridescent Queen add-ons static charge VFX is displaced in front of Survivors if they are moving.
- Survivors do not see illusionary pallets created by The Doctor's "Order" - Carter's Notes add-on.
- Frame rate issues occur when combining The Doctor's Foul Bile and Auto-Lobotomy cosmetics.
- A crash occurs when backing out of a Custom Game lobby as a spectator.
- Survivors may get stuck together after healing a downed Survivor while against a wall.
- The Hag's red stain becomes brighter when teleporting to a trap.
- Small FPS drop when there are multiple action prompts cycling on screen for Killers and Survivors.

<!-- nav -->
&larr; [3.4.2 | Hotfix](117-3-4-2-hotfix.md) · [Archive: Windows Store](../../index.md#archive-windows-store) · [3.5.1 | Hotfix](119-3-5-1-hotfix.md) &rarr;
<!-- /nav -->
