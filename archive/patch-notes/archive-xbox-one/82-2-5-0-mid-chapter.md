---
title: "2.5.0 | Mid-Chapter"
section: "Archive: Xbox One"
article_id: 82
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/82-2-5-0-mid-chapter"
author: "Peanits"
published: "2020-02-28T20:00:09+00:00"
updated: "2020-02-28T22:04:23+00:00"
archived: "2026-09-26T19:28:20Z"
---

<!-- summary -->
## AI TL;DR

Mid-Chapter 2.5.0 adds lobby controls to switch characters without opening the selection panel, new idle animations for all Survivors at the campfire, and redirects clicks on locked characters to their store page. Audio returns to default music with rebalanced footstep, music and VO volumes, while numerous killer and survivor perks receive text, timer, notification and scaling adjustments (e.g., Bamboozle, Blood Warden, Iron Maiden, Leader, Prove Thyself). Hook distribution and chest spacing are overhauled, a crow bomb appears on Grim Pantry, and the UI now hides killer loadouts during matches, requires item pickup, and shows mori icons. The update also fixes audio, visual, map collision, perk and HUD bugs, and refines vault momentum, chest drop rates and scoring terminology.
<!-- /summary -->

<!-- nav -->
&larr; [2.4.0 | Darkness Among Us](81-2-4-0-darkness-among-us.md) · [Archive: Xbox One](../../index.md#archive-xbox-one) · [2.5.1 | Hotfix](83-2-5-1-hotfix.md) &rarr;
<!-- /nav -->

# 2.5.0 | Mid-Chapter

## Features & Content

- Feature - Added controls to change characters in the lobbies and the store without accessing the character selection panel.
- Feature - Added new main menu idle animations for all Survivors. These can be observed at the campfire.
- Feature - Clicking on an unpurchased character from offline lobby will automatically redirect to this character's store page.

## Balance

**Audio adjustments**

- Changed the lobby music back to the default music.
- Remixed volume levels for footsteps, music & VOs.
- Removed the attenuation on VOs and footsteps that were integrated in the 2.4.0 release.

**Killer related**

Perk changes:

- Bamboozle: Updated text to reflect the perk does not work with pallets.
- Blood Warden: Added a timer on the perk in the HUD to better indicate when and for how long Blood Warden is active.
- Iron Maiden: Reduced Survivor location notification from 4 seconds to 3 seconds.
- Spies from the Shadows: Increased the chances of a visual notification to 100% for all tiers. Added crow outline in Loud Noise notification. Increased the notification range from 16/24/36 meters to 32/40/48 meters.
- Surveillance: Increased audible repair sounds by a distance by 8 meters. Any regressing generators will be highlighted by a white aura. If regression on a generator is interrupted, it will be highlighted by a yellow aura for 8/12/16 seconds.

The Legion:

- Manually ending Frenzy no longer depletes the remainder of your Power gauge.
- Reduced the intensity of the blurred VFX during Frenzy.

The Pig:

- Adjusted the Combat Straps add-on in accordance to the crouch duration change, decreased value from 1 second to 0.3 seconds.
- Changed the Terror Radius fade time for when crouching / uncrouching to fade out/in ~4 seconds, down from 6.6 seconds.
- Decreased the base crouch and uncrouch duration from 2 seconds to 1.3 seconds.
- Increased Terror Radius from 28 meters to 32 meters.

The Pig: Scoring Adjustments

- Hit during dash attack: increased from 250 to 500.
- Initiate dash attack: increased from 50 to 100.

**Map changes**

- Added extra hooks spawning spots around certain buildings to improve hook distribution.
- Backwater Swamp: Adjusted height of bulrushes.
- Backwater Swamp: Increased the spawning probability of the hooks in the center portion of the map to prioritize this portion of the map in favor of the edges.
- Badham Preschool: Now forcing a hook to spawn in the back of the preschool school if the basement is not there.
- Changed the basement reference point (used to calculate hook to basement distance) to the top of the basement stairs instead of being in the middle of the basement.
- Grim Pantry: Added a new crow bomb to the map.
- Procedural System - Added a minimum distance between chests so that jigsaw boxes don't spawn too close together.
- Procedural System - Hook distribution adjustments: changed the amount and distribution of hooks for each map. Every map now has a baseline minimum distance between hooks, a minimum number of hooks and a maximum number of hooks. Procedural System - Hook offerings now modify the newly introduced minimum distance between hooks. This distance will ultimately be ignored in the case where the minimum number of hooks requirements are not fulfilled. The effect of each offering is as such: Moldy Oak (Uncommon) = -1.5m, Rotten Oak (Rare)= -2.5m, Putrid Oak (Very Rare) = -3.5m, Petrified Oak (Survivor Very Rare) = +1m.
- Reduced basement to hook minimum distance to 16 meters.
- The Game: Added a few extra signs to help players navigate to the stairs.
- Totem placement improvements: Recent upgrades to the totem interaction method allows the level design team to place the totems closer to other objects and as such, totem placement and hiding spots will be continuously improved starting with this update.

**Status Effect updates**

- All status effects that are timer based no longer stack or automatically reset the timer, but rather, take the highest remaining status timer and ignore the other.
- If the new timer is the higher one, the previous timer is discarded and the status effect icon will visually reset to 100%. If the new timer is the lower one, the new timer is discarded and the status effect icon remains at its current progression.

**Survivor perk changes**

- Distortion: Updated text to reflect that this perks effect does not trigger when survivors are in the dying state or affected by traps.
- Leader: All action speeds, with the exception of repair speed, are increased to 15%/20%/25% instead of 3%/6%/9%. The effect now persists for 15 seconds after the perk owner is out of range. Only one Leader effect at a time.
- Prove Thyself: For every other Survivor working on a generator within a 4m range, gain 10% repair speed bonus. This same bonus is also applied to all other Survivors within range. Gain 50%/75%/100% more Bloodpoints for coop actions. Only one Prove Thyself effect at a time.
- Technician: All tiers reduce audible repair sounds by a distance of 8 meters, up from 0/-4/-8.

**UI Updates**

- Hidden Killer Loadout: Removed the ability for Survivors to view the Killers perks, add-ons and offerings in the tally screen during an on-going match. Killer information will be revealed once all Survivors have exited the match.
- Item Interaction: Items found in chests without already holding an item now require being picked up. This makes the interaction consistent with when you have an item already in hand and allows you to see what you have found before you commit to picking it up.
- Mori Icon: If The Killer has played a mori offering, the offering's icon will be displayed in the in-game HUD when the conditions are valid and they are standing over a downed Survivor.

**Miscellaneous**

- Adjusted the Vault mechanic so that survivors come out of the vault with momentum, instead of being set to 0 movement speed after a vault.
- After seeing the positive reaction to higher rarity items being looted from chests during the Winter Solstice, we've updated chest drop rates to support this after the event ends.
- Changed the Medium Vault speed to last 0.9 seconds down from 1 second.
- Created a new Medium Vault animation to distinguish the medium from the slow and fast vaults.
- Renamed the "Hooked" scoring event to "Caught!" and the "Hook" scoring event to "Hooked". Fixed an issue that made it impossible to gain progress on coop Daily Rituals (The Initiation).

## Bug Fixes

**Audio & Localization:**

- Fixed an issue that caused missing audio at the end of a Sacrifice.
- Fixed an issue that caused missing audio for disarming, stepping and getting out of a bear trap.
- Fixed an issue that caused the menu music to disappear when backing out of a Kill Your Friends, or when sent back to the offline lobby screen after a public match.
- Minor localization and translation improvements.

**Killer related:**

- Adjusted the intensity of the Spirit's Phase Walk VFX. The VFX changed due to the update to Unreal Engine 4.20 and the lighting changes introduced in 2.4.0.
- Fixed an issue that caused permanent heavy bleeding when healing after the Wraith performed a Surprise attack using the Sloppy Butcher perk and/or the "Blind Warrior" - White add-on.
- Fixed an issue that caused the Hillbilly's arm to stretch during his mori.
- Fixed an issue that caused the Legion's Killer Instinct to display the location of escaped Survivors.
- Fixed an issue that caused the Legion's attack VFX to be out of sync with their attack.
- Fixed an issue that caused the Legion's camera to snap up or down if the camera was moved in either direction during the Feral Frenzy cooldown.
- Fixed an issue that caused the Legion's power not to stop and reset when getting blinded by a flashlight while in Feral Frenzy.
- Fixed an issue that caused the Madness notification bubbles to end abruptly from Survivors perspectives.
- Fixed an issue that caused the Shape's Mirror Shard add-on not to show Survivor auras for the amount of time stated in the add-on.
- Fixed an issue that caused the Wraith's blade wipe animation to block most of the screen.
- Fixed an issue that could cause a desync in player states when getting out of a bear trap after attempting to vault over a window with a bear trap in front of it.
- Fixed an issue that could cause a desync in player states when picked out of a bear trap by the Trapper.

**Map specific:**

- Adjusted the lighting in the basement houses in the Lampkin Lane and Badham Preschool maps.
- Fixed an issue in Lampkin Lane that was preventing edge-object trees from spawning near the sidewalk between street tiles.
- Fixed an issue that allowed the Nurse to blink out of world through a corner wall in the bathroom of The Game map.
- Fixed an issue that caused a hook in front of the warehouse to gloat in the Coal Tower map.
- Fixed an issue that caused a partially transparent wall decal to appear in an empty doorway in The Game map.
- Fixed an issue that caused an impassable gap between a rock and a tree in the Family Residence map.
- Fixed an issue that caused an impassable gap between a tree and a chest on the Rancid Abattoir map.
- Fixed an issue that caused an invisible collision that blocked player movement on the hills in the Family Residence map.
- Fixed an issue that caused incorrect character placement when entering/exiting a specific locker in the Mount Ormond Resort map.
- Fixed an issue that caused players to float after falling on top of a totem and cleansing it, next to the unique tree in the Shelter Woods map.
- Fixed an issue that could cause multiple generators to spawn in one area in multiple maps that use the indoor generators (ie: Lampkin Lane, The Game, etc).
- Fixed an issue that made it impossible for hatchets, bottles and chainsaws to go through open windows and doorways into the chalet building in the Mount Ormond Resort map.
- Fixed an issue that made it impossible for the Legion to Frenzy vault over a specific pallet in the Grim Pantry map.
- Fixed an issue that made it impossible to damage the short side of a specific generator on the bottom floor of The Game map.
- Fixed an issue that made it impossible to interact with one side of a generator in the Mount Ormond Resort map.
- Fixed an issue that made it impossible to pass a Survivor repairing a generator from the long side in one of the houses in Lampkin Lane.
- Fixed an issue that made it impossible to pick up Survivors when they were in between a tree and a rock in the Mount Ormond Resort map.
- Fixed an issue that made it impossible to vault from one side of a fence vault in Lampkin Lane.
- Fixed an issue where a pile of wood was blocking an opening in one of the fences in Lampkin Lane.
- Misc LOD fixes.

**Perks:**

- Fixed an issue that caused the Endurance timer from Borrowed Time to be removed from the player unhooked if the player unhooking got downed.
- Fixed an issue that caused the loud noise indicator and scratch marks from the Diversion perk to appear on the Survivor who threw the pebble, if thrown outside of the Killers terror radius.
- Fixed an issue with Plunderer's Instinct causing a lower rate of Event items to appear in chests.

**UI & HUD:**

- Added more logging to help identify the issue that caused players to encounter invisible skill checks. We will be closely monitoring the impact of this change.
- Fixed an issue that caused disconnected clients to have the incorrect status in the scoreboard.
- Fixed an issue that caused frame rate drops when navigating through the Loadout.
- Fixed an issue that caused interaction prompts to be visible for certain items when in Madness Tier III.
- Fixed an issue that caused the Killer to have a superfluous Spectate button on the tally screen.
- Fixed an issue that could cause Loadout items to appear through tally screen pages.

**Miscellaneous**

- Fixed an issue that allowed Survivors to enter a locker through the Killers collision.
- Fixed an issue that allowed injured Survivors to finish Mending another Survivor before entering the dying state if the killer hit them.
- Fixed an issue that allowed the Legion to have infinite Frenzy in Kill Your Friends.
- Fixed an issue that caused cosmetics from previous special event to automatically get unequipped.
- Fixed an issue that caused the flower and finger key ring to be missing on the Clown's outfits from "The Showman" Collection. Icons have been updated to reflect this.
- Fixed an issue that caused the non-Killer host not to see blood pouring VFX on failed generator skill checks when waking up from the Dream State.
- Fixed an issue that could allow players to gain control of their character before others.
- Fixed an issue that made it impossible to heal/mend yourself when holding the sprint button, and standing still.
- Fixed an issue with generator repair efficiency for multiple Survivors working on the same generator. The efficiency debuff (-10%) should now be applied at the correct rate.
- Misc cosmetic clipping & camera adjustments and improvements.

## Known Issues

- A Survivor who has Prove Thyself equipped does not gain any repair speed bonus for each survivor working on the same generator.\[FIXED INTERNALLY\]
- When a Survivor disconnects their icon does not update to the "Disconnected" status.\[In Progress\]
- The Bloodweb doesn't refresh properly when switching characters while on the level up prompt.\[FIXED INTERNALLY\]
- Survivors prevented from interactions after going in the basement
- Survivors teleported after going in the basement
- Invisible characters

<!-- nav -->
&larr; [2.4.0 | Darkness Among Us](81-2-4-0-darkness-among-us.md) · [Archive: Xbox One](../../index.md#archive-xbox-one) · [2.5.1 | Hotfix](83-2-5-1-hotfix.md) &rarr;
<!-- /nav -->
