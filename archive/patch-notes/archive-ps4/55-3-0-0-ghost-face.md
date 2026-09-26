---
title: "3.0.0 | Ghost Face"
section: "Archive: PS4"
article_id: 55
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/55-3-0-0-ghost-face"
author: "Peanits"
published: "2020-02-28T18:57:55+00:00"
updated: "2020-03-02T19:51:07+00:00"
archived: "2026-09-26T17:09:51Z"
---

<!-- summary -->
## AI TL;DR

Ghost Face joins the roster, bringing new lobby character rotation and fresh menu music. The update also retunes swing animations and adds hit-visual effects for killers, introduces stun VFX, makes survivors’ heads follow camera direction, and refines vaulting, cosmetic lighting, and map window layouts while adding new maze tiles for Yamaoka Estate. Perks receive several cooldown and efficiency adjustments for both survivors and killers, and emblem scoring events are expanded. The bulk of the patch consists of extensive bug fixes - addressing stuck survivors, add-on glitches, animation and clipping issues, map geometry and texture problems, perk misbehaviour, UI anomalies, audio quirks, and network-related disconnects. Known visual and audio issues remain.
<!-- /summary -->

<!-- nav -->
&larr; [2.7.1 | Hotfix](54-2-7-1-hotfix.md) · [Archive: PS4](../../index.md#archive-ps4) · [3.0.1 | Hotfix](56-3-0-1-hotfix.md) &rarr;
<!-- /nav -->

# 3.0.0 | Ghost Face

## Features & Content

- Feature - Added the ability to rotate characters in the lobby.
- Feature - Added new menu and lobby music.
- Content - Added a new Killer (The Ghost Face).

## Balance

**Gameplay:**

- All Killer swing animations have been modified to match the distance at which they can hit a survivor. This was done to help mitigate situations where a Killer would hit a survivor but their weapon/ hand would not look like it was reaching the Survivor.
- In addition to Killer swing animations matching their hit distance we have also added swing VFX to mitigate when hits looked like they should have missed targets when in fact they found a target and hit. (There will be more work done to make hits look better when they connect)
- Added stun VFX for Killers when hit by pallets.
- Survivors will now turn their heads where their camera is looking. This happens when a Survivor interacts with an object in the environment and when they are not downed or incapacitated.
- Adjusted fast vault conditions: Players can no longer trigger fast vaults when beside windows or in contact with the wall.

**Art adjustments:**

- Adjusted certain darker cosmetics that gave players an advantage to be lighter.
- Re-worked some characters hair.
- Adjusted Killer Instinct VFX to remove red fill effect, increase frequency of pulse, add an offset to where symbol is displayed, modified the scaling of the symbol to stay more consistent. These changes also affect the Killer power, Feral Frenzy, of The Legion.

**Audio adjustments:**

- Adjusted the chase volume for Survivors.

**Map changes:**

- Removed the RNG factor from the window setups in the rooms of Lery's Memorial Institute; each small room now spawns with the same window configuration.
- Edge Object repopulation pass in The MacMillan Estate maps, there are more obstacles in between the map tiles now.
- Introduced new maze tiles for the Yamaoka Estate theme.

**Survivor Emblem changes:**

**Added events for Lightbringer emblem scoring:**

- 20 points for cleansing a dull totem.
- 5 points if a dull totem is cleansed while you are in a chase.
- 10 points if a Hex totem is cleansed while you are in a chase.
- 1/3 point for each 1% of a generator repaired while you are in a chase (Capped to a maximum of 33.3 scored for each generator).

**Added event for Benevolent emblem scoring:**

- 10 points for sabotaging a hook within 10 meters of a Killer carrying a Survivor, if the carried Survivor then wiggles free.

**Added event for Evader emblem scoring:**

- 50 points for stunning the Killer with a pallet.

**Survivor perk changes:**

- Streetwise: Increased efficiency values to 15%/20%/25% up from 10%/12%/15%.
- Windows of Opportunity: Reduced cooldown values to 30/25/20 seconds down from 60/50/40.
- Mettle of Man: We have changed the condition for getting tokens. It is no longer for being hit by a Killer's basic attack. Instead earn tokens by taking "Protection Hits". It still requires 3 tokens to activate. Survivors will still need to be injured in order to trigger the Endurance effect and avoid being put into the dying state. This means that Mettle of Man will require more work from the Survivor to trigger Mettle of Man's Endurance status effect.
- Unbreakable: Increased recovery speed to 25%/30%/35% up from 15%/20%/25%.

**Killer perk changes:**

- Pop Goes The Weasel: Changed Regression values from 15%/20%/25% to a flat 25% across all tiers. Changed window of activation from 30 seconds to 40/50/60 seconds.
- Territorial Imperative: Reduced cooldown to 30/25/20 seconds down from 60/45/30.
- Enduring: Updated Enduring to a flat reduction in pallet stun duration of 40/45/50% rather than an increase to stun recovery speed of 55/65/75%. Enduring will now only affect pallet stuns.

## Bug Fixes

**Killer related:**

- Fixed an issue that could cause Survivors to become stuck for the rest of the match when The Trapper placed a bear trap under them while they were already performing an interaction.
- Fixed an issue that caused The Clown's Redhead's Pinky Finger add-on to apply the Exposed status effect on Survivors without a direct bottle hit.
- Fixed an issue that could cause permanent Exhaustion when affected by The Clown's gas bottles with the Solvent Jug add-on equipped.
- Fixed an issue that caused The Clown to clip through most vaulting windows.
- Fixed an issue that caused The Shape's camera to become slanted and allowed him to walk on assets when cancelling his mori.
- Fixed an issue that caused The Hag's Rusty Shackles add-on to play the terror radius when the trap was triggered.
- Fixed an issue that caused The Wraith's "The Serpent" - Soot add-on not to fully uncloak him immediately after breaking a pallet or damaging a generator.
- Fixed an issue that caused The Nurse to be missing her hand and weapon when blink attacking a Survivor before getting fatigued.

**Map specific:**

- Fixed an issue that caused grass to move when a player was above or below the area. This issue was most commonly seen around the basement when it was in the Shack.
- Fixed an issue that could cause the right door on lockers to appear warped.
- Fixed an issue that made it impossible for Killers to interrupt a Survivor repairing a generator from a specific side in the Wretched Shop map.
- Fixed an issue that made it impossible to open the hatch with a key when it spawned facing a car pile in the Gas Heaven map.
- Fixed an issue that made it possible to get stuck in the basement stair collision under certain conditions, when the basement spawned in the office building in the Azarov's Resting Place map.
- Fixed an issue that caused tree branches and leaves to clip through the walls on the top floor of the farm house in the Thompson House map.
- Fixed an issue that could cause a desync between clients and host around the slaughterhouse in the Rancid Abattoir map.
- Fixed an issue that caused some assets to have missing textures on the slaughterhouse building in the Rancid Abattoir map.
- Fixed an issue that caused tree branches and leaves to clip through the walls on the top floor of certain houses in the Lampkin Lane map.
- Fixed an issue that caused a generator to clip into part of a maze wall in The Pale Rose map.
- Fixed an issue that could cause a desync between clients and host around the Ferry Boat in The Pale Rose map.
- Fixed an issue that caused blood and dirt wall textures to disappear at certain camera angles in the Lery's Memorial Institute map.
- Fixed an issue that allowed Survivor to cleanse the hill totem from on top of the rocks in the Mount Ormond Resort map.
- Fixed an issue that caused the Entity not to appear on a specific hook in The Temple of Purgation map.
- Fixed an issue that made it impossible for The Nurse to blink around the exterior of the temple tile in the Temple of Purgation map.
- Fixed an issue that made it impossible for The Nurse to blink around the exit tiles in the Temple of Purgation map.
- Misc LOD fixes.

**Perks:**

- Fixed an issue that caused Mettle of Man to give the Killer a point in the Malicious Emblem category when activated.
- Fixed an issue that caused The Legion's Killer Instinct not to be visible with Dark Devotion.
- Fixed an issue that caused the Territorial Imperative perk to trigger on hooked and hiding Survivors.
- Fixed an issue that caused the Resilience perk not to affect window vaults.

**Miscellaneous:**

- Fixed an issue that could cause a disconnect or make it impossible to execute a mori when the Survivor was recovering.
- Fixed an issue that caused only Billy's hair to show in the Jigsaw box aura when within 5 meters.
- Fixed an issue that caused Claudette with the Side-parted Curls head customization not to trigger Hag traps.
- Adjusted the bear trap interaction zone that caused Survivors to snap into the disarm trap animation.
- Fixed an issue that caused Survivors vaulting over windows during the Dream State transition to clip through the window.
- Fixed an issue that caused the Entity blocker to sometimes not block windows.
- Fixed an issue that caused a window to block directly after the initial Entity blocker timer had ended.
- Fixed an issue that caused the Survivor camera to become offset when interrupted entering a locker by the Killer.
- Fixed an issue that caused Survivors to appear floating in lobbies and on the tally screen.
- Adjusted the flashlight items aim when held by Ash's Ashy Slashy hand customization item to be more in line with regular cosmetics.
- Adjusted the smoke opacity LODs that caused the hatch and Hex totem VFX to be visible from far away.
- Fixed an issue that caused the notification bubble for a Survivor stepping in a bear trap to be misplaced and wobble.
- Fixed an issue that caused Survivors to lose their Offerings if the Killer disconnected right after the offering burn screen.
- Fixed an issue that caused the Sealed Envelope Offering to not be personal.
- Fixed an issue that caused The Hunt Ritual to generate with progress already applied.
- Fixed an issue that caused Killer's to lose 4 pips when disconnecting through a cable pull and re-establishing a Network connection on the splash screen.
- Added more logging to better help understand and track the issues where players are losing pips or not gaining progress on their rank.
- Fixed an issue that caused the user to return to a broken tally screen when resuming the application after suspending it during the loading screen into a public match.
- Fixed an issue that caused progress on the Deranged Pursuit trophy when downing a Survivor with the Deep Wound status effect from the Borrowed Time perk.
- Updated the intro video.
- Misc cosmetic clipping and improvements.

**Audio & Localization:**

- Fixed an issue that caused the Entity gargle noises to remain on the hooks when a Survivor was unhooked.
- Fixed an issue that caused the loud noise notification from Spies From The Shadows to have a muffled sound effect in comparison to the other loud noises.
- Fixed an issue that caused no interrupt audio stinger when being pulled out of a locker.
- Fixed an issue that caused The Shape's stinger theme to play and overlap the menu music.
- Adjusted Ash's VO in the menus.
- Fixed multiple audio issues related to the environments.
- Minor localization and translation improvements.

**UI & HUD:**

- Fixed an issue that caused the inventory pages to revert in a Kill Your Friends lobby to the last one used in a Public match when a Survivor joined or changes characters.
- Fixed an issue that caused the Revoke Consent tooltip to be cut off in French.
- Removed the progress bar when executing a mori Kill after it was fully charged.
- Misc UI improvements.

## Known issues:

- The Barbecue & Chili and Remember Me perks visually only stack up to 3 tokens.
- The Spirit's passive phasing is missing VFX.
- Heartbeat audio will overlap itself.
- No music for Killers when carrying Survivors.
- Survivors won't be able to see The Plague's vomit on windows.
- Generators in the Tutorials do not show progress until interacted with.
- The heartbeat and terror radius for The Trapper is missing in the Survivor Tutorial.

<!-- nav -->
&larr; [2.7.1 | Hotfix](54-2-7-1-hotfix.md) · [Archive: PS4](../../index.md#archive-ps4) · [3.0.1 | Hotfix](56-3-0-1-hotfix.md) &rarr;
<!-- /nav -->
