---
title: "2.4.0 | Darkness Among Us"
section: "Archive: Xbox One"
article_id: 81
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/81-2-4-0-darkness-among-us"
author: "Peanits"
published: "2020-02-28T19:59:34+00:00"
updated: "2020-02-28T22:02:30+00:00"
archived: "2026-09-26T19:28:20Z"
---

<!-- summary -->
## AI TL;DR

Upgrading to Unreal Engine 4.20 brings realistic volumetric fog, re-balanced lighting, fog, sound and occlusion, and a reduced Killer red-stain visibility. The new Darkness Among Us chapter adds the Deep Wound status effect—Survivors must mend before bleed-out and Borrowed Time’s timer is cut to 10/15/20 s—while the updated matchmaking system was trialled in PTB. Additional content includes the Best New Trapper Mask for all, map-theme info in the pause menu, a map-scheduler for ranked play, and UI tweaks such as Killer stat displays. The patch is otherwise dominated by extensive bug fixes covering audio, Killer animations, map geometry, perk interactions, UI/HUD, and Xbox One controller/overlay issues.
<!-- /summary -->

<!-- nav -->
&larr; [2.3.2 | Hotfix](80-2-3-2-hotfix.md) · [Archive: Xbox One](../../index.md#archive-xbox-one) · [2.5.0 | Mid-Chapter](82-2-5-0-mid-chapter.md) &rarr;
<!-- /nav -->

# 2.4.0 | Darkness Among Us

## Dev Notes

**Unreal Engine update**

The updated engine has added support for many new features (especially in Audio & Rendering), but also caused some incompatibility with existing features the game relied on. As such, we have re-balanced a few very important components of the game (lighting, fog, sound & occlusion)

- Added support for more realistic volumetric fog in all exterior maps.
- Adjusted audio balance and occlusion levels across all maps.
- Adjusted lighting across all themes and maps, quality settings, as well as Killer specific lighting conditions (The Nightmare's dream world, etc).
- Reduced the distance at which a Killer's red stain is visible to Survivors.

**New Matchmaking System**

We tested the new matchmaking system during the 2.4.0 PTB. For more info about the nature of this new matchmaking system and when it will roll out on the live environment, please consult this [post.](https://forum.deadbydaylight.com/en/discussion/31987/new-matchmaking-system-information#latest)

**Deep Wound status**

With our latest chapter, Darkness Among Us, we are introducing a new status effect to the world of Dead by Daylight: **Deep Wound**. You may already be familiar with the effect if you have ever been on the receiving end of a Borrowed Time save. The perk, Borrowed Time, has now been updated to reflect this new status effect.

Deep Wound indicates that a Survivor has been afflicted with a devastating internal injury and has a limited amount of time in which to be mended before being put into the dying state.

Survivors now have the ability to mend themselves, or others, without requiring a med-kit. Just find a safe place to stop running and spend a bit of time repairing those internal injuries. The Deep Wound timer now pauses while the Survivor is in a chase and The Killer is shown a location indicator if the Survivor goes down because of Deep Wound.

For these reasons, Borrowed Time’s bleed-out timer has been reduced to 10/15/20 seconds (previously 15/20/25 seconds) before putting the afflicted Survivor into dying state.

The portrait icon in the bottom-left of the screen indicates the amount of time the Survivor has before they go down. The screen effects while in Deep Wound have also been modified from the desaturated look of the original Borrowed Time to now incorporate more blood to make it very clear that you are still in peril.

## Features & Content

- Content - Made the "Best New Trapper Mask" customization item (CVA Award) available to all players.
- Feature - Added a new status effect for Survivors: Deep Wound. Survivors afflicted with the Deep Wound status effect need to mend before being able to heal themselves, or be healed by others. Survivors can mend each other.
- Feature - Added the theme, map and tile information in the Pause menu. This feature is to better help our players and the Dev team when reporting map specific issues. Please be sure to include that information when reporting any map issues.
- Feature - Integrated an updated version of the Unreal Engine (4.20, from 4.13).
- Feature - Map Scheduler: Added a server configuration to allow control of map frequency during Online Ranked matches. This will allow us to add or remove emphasis on certain maps or themes during specific periods. Map selection offerings will still normally take precedence over these.
- Feature - Opening the Store from the offline lobbies will redirect the user to the currently selected character's catalog page.

## Balance

**UI Updates**

- Updated layout for the character information screen. Killer information screens now show basic stats (Max Base Speed, Base Terror Radius, and Height).

**Survivor perks**

- Borrowed Time: Unhooked Survivors are now affected by the Deep Wound Status effect. Changed the Bleedout timer from 15/20/25 seconds to 10/15/20 seconds. VFX have been updated. Please see the dev message: "Deep Wound" for more details.
- Diversion: Scratch marks will now appear at the location of the loud noise from the pebble.

**Other balance changes**

- Hiding inside of lockers now blocks the auras of Survivors while they are inside.
- Increased the brightness of auras.
- Made it possible for Survivors to cancel being healed by walking away. Prior to this change, survivors needed to run in order to cancel being healed.
- Snap Out Of It is no longer affected by the A Nurse's Calling perk. Actions such as Snap Out Of It and Mending are not healing actions, thus perks should not affect them.
- Survivors who activate a map or key item while crouched now stay crouched.
- When in a locker once the Bleedout timer has ended, Survivors will automatically exit the locker.

## Bug Fixes

**Audio & Localization**

- Major localization and translation improvements.

**Killer specific**

- Fixed an issue that caused Survivors hooked by the Hag to be a bit offset from the hook.
- Fixed an issue that caused Survivors to flip into the dead position when mori'd by the Shape with either Judith's Tombstone or Tombstone Piece add-ons.
- Fixed an issue that caused an audio discrepancy between two game client who are facing in opposite directions (towards and away) from the Hillbilly's chainsaw.
- Fixed an issue that caused blood VFX from the environment to appear brighter when the Spirit uses her power.
- Fixed an issue that caused the Clown's knife to become misaligned when interrupting a Survivor vaulting towards them.
- Fixed an issue that caused the Killers red stain to be visible on their own character's model.
- Fixed an issue that caused the Nurse to clip into Survivors during her mori kill.
- Fixed an issue that caused the Nurse to go into the fatigued state when blink interrupting a Survivor.
- Fixed an issue that caused the Spirit's Husk to start a fresh idle animation instead of using the players current animation during her Phase Walk.
- Fixed an issue that caused the Spirit's head to disappear towards the end of the camera pan intro sequence at the start of a match.
- Fixed an issue that caused the Survivor stepped in trap loud noise bubble to appear when the Trapper was holding a bear trap near any other notification bubble.
- Fixed an issue that caused the Survivor to move in front of the camera when the Spirit attacks while carrying a Survivor on her shoulder.
- Fixed an issue that caused the blood from Survivors to be visible while the Spirit charged her power.
- Fixed an issue that caused the camera to be incorrectly placed from Survivor perspective when being mori'd by the Shape with either Judith's Tombstone or Tombstone Piece add-ons.
- Fixed an issue that caused the held items to briefly appear out of the Killers' hand when interrupting a Survivor vaulting towards them.
- Fixed an issue that caused the wrong LOD to sometimes load on The Spirit's customization.
- Fixed an issue that made it impossible for the Trapper to pick up Survivors from a bear trap when it was placed too close to a totem.
- Fixed an issue that made it impossible to blind a Killer with a flashlight if there was a downed Survivor in front of them.

**Map specific**

- Fixed an issue that allowed players to walk on a large rock in the Autohaven Wrecker's maps.
- Fixed an issue that allowed the Killer to interrupt a chest search across from a fence in Lampkin Lane.
- Fixed an issue that caused a small pile of logs to spawn in between two hedges in Lampkin Lane.
- Fixed an issue that caused an impassable gap between a fence wall and a rock in The Pale Rose map.
- Fixed an issue that caused an impassable gap for Killers when two trees spawned too close together in the Mother's Dwelling map.
- Fixed an issue that caused an inaccessible chest in the Grim Pantry map.
- Fixed an issue that could cause a stuck spot in the Grim Pantry map between a log and a hill.
- Fixed an issue that made it impossible to open or escape through the hatch when spawned on a specific hill in the Mother's Dwelling map.
- Fixed an issue that made it impossible to repair a generator from one of the shorts sides next to the van in the street in Lampkin Lane.

**Perks**

- Fixed an issue that allowed Survivors to spam the Diversion perk while repairing a generator.
- Fixed an issue that caused Adrenaline to trigger during the pick-up and interrupt animations.
- Fixed an issue that caused the attack cooldown to be applied on Hex: No One Escapes Death, after it was removed in patch 2.3.0.
- Fixed an issue that caused the bleedout timer from Borrowed Time perk to cancel completely when stepping in a bear trap.
- Fixed an issue that caused the hooks destroyed by a sacrifice not to respawn with the Hangman's Trick perk.

**Miscellaneous**

- Fixed an issue that caused Survivors to overlap on one another in the match result screen.
- Fixed an issue that caused Survivors to snap back underneath the hook when unhooking themselves.
- Fixed an issue that caused an inconsistency in the way that perks, powers and add-ons dynamically modify the Terror Radius.
- Fixed an issue that caused healing progress not to reset when being interrupted and hooked.
- Fixed an issue that caused players to be invisible to others until moving if spawned in the Shack.
- Fixed an issue that caused the Clown's stomach to jiggle too much in the tally screen.
- Fixed an issue that caused the Killer Prestige items to be awarded in the wrong order.
- Fixed an issue that caused the Mangled status effect to stack when applied from different sources (add-ons, perks).
- Fixed an issue that caused the Object of Obsession perk not to work when the character body was not facing a non-host Killer in a Kill Your Friends match.
- Fixed an issue that caused the Rite of the Spirit Daily Ritual to unlock without meeting the requirements.
- Fixed an issue that caused the Spectator camera to remain in spectate when the last player would leave the match.
- Fixed an issue that could cause items to disappear when swapping items in a chest.
- Fixed an issue that could cause the damage protection from getting unhooked to either not trigger, or be applied long after the player has regained control of their character.
- Fixed an issue that made it possible for a Survivor to obtain an Iridescent Unbroken Emblem in a game where they were pulled out of a bear trap and hooked.
- Misc cosmetic clipping & camera adjustments and improvements.

**UI & HUD**

- Changed the "Survivors" tab in the pause menu to "Match Details".
- Fixed an issue that caused the Killer add-ons not to appear in the tally screen in a Kill Your Friends match with a non-host Killer.
- Fixed an issue that caused the prices to be missing from customization tooltips that were only purchasable with Auric Cells.
- Fixed an issue that caused the tooltips from Page 1 to carry over to Page 2 of the Map Select in Match Management in Kill Your Friends.
- Fixed an issue that made it impossible to open profiles or read perk, add-ons, items or offering descriptions on the match result screen after spectating.
- Fixed an issue that made it impossible to scroll through the DLC confirmation texts with the controller sticks.
- Misc UI improvements.

**XB1 specific**

- Fixed an issue that caused multiple "Controller Disconnected" messages when repeatedly disconnecting and reconnecting the controller.
- Fixed an issue that caused the Options menu not to work on the match result screen if the host has disconnected
- Fixed an issue that caused the host of a public lobby to appear on the Xbox One overlay. The lobby should not be joinable, and a Game Version Mismatch error message would be received after attempting the connection.
- Fixed an issue that made it impossible to unlock the "Where Did They Go!?" achievement as a Survivor and caused the Killer to unlock it instead.
- Fixed an issue that made it possible to unlock the "Risk It All" achievement with event items.

<!-- nav -->
&larr; [2.3.2 | Hotfix](80-2-3-2-hotfix.md) · [Archive: Xbox One](../../index.md#archive-xbox-one) · [2.5.0 | Mid-Chapter](82-2-5-0-mid-chapter.md) &rarr;
<!-- /nav -->
