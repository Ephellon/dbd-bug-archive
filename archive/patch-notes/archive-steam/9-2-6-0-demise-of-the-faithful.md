---
title: "2.6.0 | Demise of the Faithful"
section: "Archive: Steam"
article_id: 9
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/9-2-6-0-demise-of-the-faithful"
author: "Peanits"
published: "2020-02-28T17:18:09+00:00"
updated: "2020-03-02T15:12:30+00:00"
archived: "2026-09-26T02:19:03Z"
---

# 2.6.0 | Demise of the Faithful

**Emblem changes**

[**Click here for more information**](https://forum.deadbydaylight.com/en/discussion/52295/the-emblem-system-changes-explained/p1?new=1)

## Features & Content

- Content - Added a new Killer (The Plague)
- Content - Added a new Survivor (Jane Romero)
- Content - Added a new map for the Red Forest theme (The Temple of Purgation).
- Feature - Added the matchmaking queue time display for both roles. This change follows the backend matchmaking changes (addition of queues) that were recently deployed.
- Feature - Adjusted the EULA & Privacy Policy approval flow, and added an option to revoke the consent from the settings menu.
- Feature - Changed the Character Swap controls from LT/RT to LS/RS
- Feature - Disabled changing the active characters with the Character Swap controls while the player is Ready in a lobby. This was done as an extra check to ensure there are no more accidental character swaps.
- Feature - Integrated an updated version of the Unreal Engine (4.21, from 4.20).
- Feature - Modified the progression display for certain Daily Rituals. Instead of showing the percentage and minutes, we're now showing the amount and seconds. This is applicable for the following Daily Rituals: Blood Dance, Reconstruction Ritual, Rite of Ruin, Wild Dance, and Hunt Ritual.

This update also contains some additional optimizations for all platforms. [Click here for more information](https://forum.deadbydaylight.com/en/discussion/49456/optimization-status-update-road-to-60fps)

## Balance

**Audio adjustments:**

- Added / Adjusted audio occlusion for buildings with multiple floors.
- Adjusted the basement occlusion audio balance. This will make sounds coming from the basement to be attenuated or muted in most circumstances.
- Decreased the distance at which you can hear Survivors breathing and grunting while they are hiding in lockers.

**Emblem changes:**

- Chaser Scoring: The proximity penalty has been increased. The longer a Killer stays within a close proximity (16m) to a hooked Survivor, the more points they will lose in the Chaser emblem.
- Devout Scoring: The scoring thresholds have been modified. 3 kills now also result in a Silver emblem, whereas 4 kills results in Gold. To earn an Iridescent Devout emblem, you need to perform 9 or more hook events and sacrifice all 4 Survivors.
- Gatekeeper Scoring: The scoring formula has been adjusted completely. Killers earn incremental points based on how few generators have been completed, each minute for the first nine minutes of the match - regardless of how long the match takes. At the end of the match, the Killer also gains bonus points based on how few generators have been completed. Note: If the match is over before nine minutes is up, they receive points for the remaining minutes (up to nine) based on how few generators had been completed at the end of the match.

**Gameplay:**

- Added a new scoring event for perk-based stun events (Decisive Strike/Head On) worth 500 bloodpoints. This is referred to as Killer Stun in game.
- Reduced the time before a player can heal a player who has recently moved, this should allow for players to start healing a recently canceled heal quicker than before.
- Survivors entering lockers now have the Blindness Status Effect applied to them.
- The intensity of the Terror Radius is now scaled based on the vertical distance (in addition to the horizontal distance).

**Killer perk changes:**

- Barbecue and Chili: Auras are revealed from 40 meters for all tiers of the perk instead of 52/46/40 meters.
- Deerstalker: Increased the aura reading from 16/24/36 meters to 20/28/36 meters.
- Distressing: All tiers award 100% bonus bloodpoints.
- Fire Up: Each tier grants a stackable 3/3.5/4% action speed bonus.
- Hex: Devour Hope: The perk grants 3/4/5% speed boost with 2 tokens, Exposed status applied at 3 tokens, and Kills are available at 5 tokens.
- Hex: Ruin: All tiers affect all Survivors and apply a penalty of 3/4/5% regression on a good skill checks.
- Hex: Thrill of the Hunt: All tiers grant 10% bonus Hunting bloodpoints per remaining totem. Cleansing speeds are the same.
- Iron Grasp: The effects of Survivor struggling is reduced by 75% for all tiers. The amount of time for Survivors to struggle does not change (4/8/12% respectively).
- Monitor and Abuse: The FOV values are 3/5/10 instead of slightly/ moderately/ considerably increased. Also simplified the Terror Radius value so that each tier modifies the Terror Radius by the same value, 8 meters instead of 6/7/8.
- Spies From The Shadows: Added a 5 second cooldown when the perk triggers. Reduced the trigger range from 32/40/48 meters to 20/28/36 meters.
- Thanatophobia: Tier values are incremented at a rate of 3/3.5/4% up to a maximum of 12/14/16%.

**Map changes:**

- Procedural system changes:
- Added a new line of sight check for totem spawn points within 32m from a survivor spawn point.
- Added a minimum distance of 48m between chest objects.
- Increased the minimum number of pallets to 8 (global).
- Distances between spawnable objects(generators, hooks, pallets etc) are now scaled based on a vertical factor(in addition to the baseline horizontal distance).
- Minimum distance between pallets was reduced for the Shelter Woods map.
- Some gameplay object placement changes in the Foundry building of the Ironworks of Misery map.
- Some gameplay object placement changes on the Water Tower landmark tile in The MacMillan Estate maps.
- Added door frames in The Game map.
- Added new tiles to the Red Forest maps.

**Ranking changes:**

Pipping Thresholds: We have made some changes to the Emblem system that will affect the difficulty in which players rank up and subsequently maintain their rank. The rank groups (colors) now come with their own pipping requirements. The thresholds increase through each rank group up to the red ranks making it more difficult to pip / double pip, and easier to lose a pip. See below:

- Rank 17-20 (BEIGE): 0-8 points = 0 pips; 9-13 points = +1 pip; 14-16 points = +2 pips.
- Rank 13-16 (YELLOW): 0-5 points = -1 pip; 6-9 points = 0 pips; 10-13 points = +1 pip; 14-16 points = +2 pips.
- Rank 9-12 (GREEN): 0-6 points = -1 pip; 7-10 points = 0 pips; 11-14 points = +1 pip; 15-16 points = +2 pips.
- Rank 5-8 (PURPLE): 0-7 points = -1 pip; 8-11 points = 0 pips; 12-14 points = +1 pip; 15-16 points = +2 pips.
- Rank 1-4 (RED): 0-8 points = -1 pip; 9-12 points = 0 pips; 13-15 points = +1 pip; 16 points = +2 pips.

**Survivor perk changes:**

- Decisive Strike: After being unhooked by another player or yourself, Decisive Strike becomes active for 60 seconds. If you are grabbed by the Killer while the perk is active, succeeding a skill check to cause an automatic escape and stun the Killer for 3 seconds. Succeeding or failing the skill check will disable the perk for the rest of the trial. Succeeding the skill check (and thus stunning the Killer) will result in you becoming the Obsession. [Click here for more information](https://forum.deadbydaylight.com/en/discussion/48381/decisive-strike-upcoming-changes)
- Empathy: Empathy now works within a range of 64m/96m/128m for tiers 1/2/3 respectively.
- Kindred: All Survivor's auras are shown at all tiers. If the Killer is within a 8/12/16 meter range of the hooked Survivor, their aura is revealed to all other Survivors.
- Lithe: Removed the chase condition. Lithe now only triggers on rushed vaults.
- Pharmacy: All tiers have a reduced audible distance of 8 meters.
- Technician: All tiers are set to 8 meters reduced audio range of the survivor repairing instead of 0/ 4/-8 meters.
- Wake Up: All tiers reveal auras at 128 meters.
- We'll Make It: Increased all tiers to 100% healing speed instead of 70/80/100%.

## Bug Fixes

**Audio & Localization:**

- Fixed an issue that caused the Halloween® music to play too loud during the camera intro when loading into Lampkin Lane.
- Fixed an issue that caused the Huntress to have the charging hatchet audio cue when reloading hatchets in a locker.
- Fixed an issue that caused the chase music to change while under the effects of the Clown's gas bottles.
- Fixed an issue that caused the node purchasing audio to loop if swapping characters while purchasing a node in the Bloodweb.
- Fixed the rain audio while inside in the Red Forest maps.
- Major localization and translation improvements. Among these improvements included fixing the proper Spanish translations for the Leader, Technician and Distortion perk descriptions, that were erroneously displaying the Lunar Event objective text, then reverted to out of date texts in patch 2.5.3.

**Killer related:**

- Fixed an issue that caused Play With Your Food tokens to be consumed when The Clown throws a gas bottle.
- Fixed an issue that caused The Clown's bottle to disappear at the end of his Reload animation.
- Fixed an issue that caused The Doctor not to see the illusionary pallet auras when using the "Order" add-ons.
- Fixed an issue that caused The Hag's Phantasm not to display her model when triggered.
- Fixed an issue that caused The Hag's Phantasms not to have a terror radius when the traps were triggered.
- Fixed an issue that caused The Huntress' animation to stutter when throwing a hatchet.
- Fixed an issue that caused The Huntress' hatchet cancel animation to be almost instant.
- Fixed an issue that caused The Legion to snap into position when vaulting a pallet.
- Fixed an issue that caused The Nightmare's leg to be misaligned during the pallet break and generator damage animations.
- Fixed an issue that caused The Shape's Vanity Mirror and Scratched Mirror add-ons to grant the incorrect amount of points on the first 2 hits. The points are now 300 per attack, and with the bonuses are 450 & 600 respectively.
- Fixed an issue that caused The Trapper's Honing Stone debuff icon to remain active in the HUD if rescued from a trap by another Survivor.
- Fixed an issue that caused The Trapper's Logwood Dye and Tar Bottle add-ons not to darken traps from Survivor point of view.

**Map specific:**

- Adjusted the Scratch Mark material and texture to be seen more clearly in the Mount Ormond Resort map.
- Adjusted the collision on certain rock assets that allowed the Legions camera to clip inside of them in the Mount Ormond Resort map.
- Fixed an issue that allowed players to shimmy up collision on the rocks on the hill, allowing them to old the game hostage.
- Fixed an issue that allowed the Huntress to throw her hatchets through multiple car assets in the Autohaven Wrecker's maps.
- Fixed an issue that allowed the Huntress to throw her hatchets through the storage bins in The Game map.
- Fixed an issue that allowed the Nurse to blink out of world through the top and bottom floor walls on a specific corner tile in The Game map.
- Fixed an issue that caused an impassable gap between a snow pile and a tree in the Mount Ormond Resort map.
- Fixed an issue that caused an invisible collision on one of the corners of the Resort building in the Mount Ormond Resort map.
- Fixed an issue that caused an invisible collision on the staircases in The Game map.
- Fixed an issue that caused bear traps to sink below the ground in and around the two-story house in the Badham Preschool map.
- Fixed an issue that caused bear traps to sink below the ground in the Blood Lodge map.
- Fixed an issue that caused the blood decals in the house basements to disappear at certain angles in Lampkin Lane.
- Fixed an issue that caused the wrong hook to spawn when the basement was not spawned in the preschool in the Badham Preschool map.
- Fixed an issue that could cause players to get stuck when going down a hole with a pig's head in The Game map.
- Fixed an issue that could cause rocks on the hill assets to have the wrong texture in various maps.
- Fixed an issue that made it difficult for the Nurse to blink around, on and through the Ferry Boat in The Pale Rose map.
- Fixed an issue that made it impossible to rush vault a specific window in one of the small houses in Lampkin Lane.
- Fixed an issue that made it impossible to use a key when the hatch spawned the wrong way on the Garden tile in the Family Residence map.
- Fixed an issue that made it impossible to use a key when the hatch spawned the wrong way on the Lookout tile in the Mount Ormond Resort map.
- Fixed an issue that made it possible to get stuck in a specific corner of a maze tile in the Family Residence map.
- Fixed an issue that made it possible to get stuck in a specific hill collision in the Family Residence map.
- Fixed the hex totem procedural spawn in various maps.
- Fixed the textures on the hills in the Mount Ormond Resort map.
- Misc LOD fixes.
- Optimized the lighting in the Mount Ormond Resort map that was causing low framerate.

**Miscellaneous:**

- Fixed an issue that allowed Survivors to go out of world and hold the game hostage when wiggling free or being dropped by the Killer at the exit threshold.
- Fixed an issue that caused Meg in the Killer Tutorial not to run away.
- Fixed an issue that caused owned characters and cosmetics to become unavailable after purchasing Auric Cells (which was fixed by relaunching the game).
- Fixed an issue that caused survivors to be stuck in place if another survivor was healing them and got disconnected from the network.
- Fixed an issue that caused the Deep Wound on screen blood splatters to disappear when the bleed out bar ran out while Mending.
- Fixed an issue that caused the Safe Hook Rescue score event to trigger regardless of the state of the unhooked survivor, which in turn caused improper Benevolent Emblem rewards.
- Fixed an issue that caused the trap disarm animation to have missing frames.
- Fixed an issue that could cause female Survivors to temporarily lose their running animation after pulling down a pallet.
- Fixed an issue that made it impossible to track progress on The Savior Ritual when the exit gates were powered but not opened.
- Fixed an issue that made it possible to exceed the maximum amount of points for the Devout Emblem.
- Misc cosmetic clipping and improvements.
- Tentatively fixed an issue that could cause a client to see a Hex Totem as a Dull Totem.
- Tentatively fixed an issue that could cause players to get stuck in trees.
- Fixed an issue that caused the Left For Dead achievement to be awarded without meeting the requirements.
- Fixed an issue that caused the Shock Therapy achievement not to unlock when meeting the requirements.

**Perks:**

- Fixed an issue that caused Bitter Murmur not to show all Survivors' auras when the last generator was repaired, and for less than 5/7/10 seconds respectively.
- Fixed an issue that caused Blood Warden to show Survivors' auras when outside of the exit gate, and before the requirements were met.
- Fixed an issue that caused Calm Spirit to continue to alert crows. Do note this is still applicable for the crow bomb in the Backwater Swamp maps.
- Fixed an issue that caused interaction progress to regress when being interrupted from the action and failing the Decisive Strike skill check.

**UI & HUD:**

- Fixed an issue that allowed players to switch characters and create a lobby simultaneously.
- Fixed an issue that caused Events customization tooltips to be cut-off if the item is in the center of the row of the characters catalog page in the store.
- Fixed an issue that caused a placeholder medkit item to temporarily appears in the 2nd item slot when picking up a survivor as the killer.
- Fixed an issue that caused certain Killer cosmetic category tooltips to be incorrect in the catalog section of the Store.
- Fixed an issue that caused certain Killer cosmetic icons to appear in the wrong order in the catalog section of the Store.
- Fixed an issue that caused the Killer Loadout to become visible on the tally screen if a Survivor pulled their Ethernet cable on the tally screen after dying/escaping.
- Misc UI improvements.

## Fixes and changes from PTB 2.6.0

## Balance

**Add-on changes:**

- Add-on Ashen Apple: +5 seconds.
- Add-on Hematite Seal: +10 seconds.
- Add-on Incensed Ointment: +0.3 Movement Speed.
- Add-on Iridescent Seal: Reduced the duration of Worship mode by 20 seconds.
- Add-on Limestone Seal: +5 seconds.
- Add-on Olibanum Incense: +0.3 Movement Speed.

**Emblem changes:**

- Devout: Hook event condition reduced from 10+ to 9+ hook events required for Iridescent quality. This makes it easier to achieve Iridescent quality of Devout emblem.
- Gatekeeper: Scoring defended generators points reduced. Quality threshold requirements reduced. This makes it easier to achieve all qualities of Gatekeeper emblem.

**Perk Changes:**

- Fire Up had it's values increased after testing in the PTB. Value increased up from 2/2.5/3% up to 3/3.5/4% for a new maximum of 15/17.5/20%.
- Thanatophobia had it's values decreased after testing in the PTB. Values decreased from 4/5/6% down to 3/3.5/4% for a new maximum of 12/14/16%.

## Bug Fixes

- Fixed an issue that allowed The Nurse to blink under the Temple stairs in the Temple of Purgation map.
- Fixed an issue that cause items obtained in a match to be added to the players' inventory when they quit the same match.
- Fixed an issue that caused Corrupt Purge to turn into Vile Purge while it's being used.
- Fixed an issue that caused Survivors to see The Plague's vomit stream green while she had Corrupt Purge.
- Fixed an issue that caused The Legion and The Spirit to be unable to user their power while blinded.
- Fixed an issue that caused The Plague to get the Contagious score event when vomiting on completed generators and unpowered exit gates.
- Fixed an issue that caused Tier I and II Deerstalker not to display auras at 20/28 meters respectively.
- Fixed an issue that caused improper character placement when hiding in a specific locker on a specific tile in the Red Forest maps.
- Fixed an issue that caused infected flashlights to permanently have the infected/stinky green VFX.
- Fixed an issue that caused invisible collision on the tracks in the mine building in the Suffocation Pit map.
- Fixed an issue that caused sickness to be gained when using a map item or a key with aura reading add-ons.
- Fixed an issue that caused sickness to be gained when using the Diversion perk.
- Fixed an issue that caused the 75% reduced wiggle effect not to be applied on Tiers I & II of Iron Grasp.
- Fixed an issue that caused the Evil Within tier up music to play lower in volume and muffle all other sounds.
- Fixed an issue that caused the bear trap audio to rapidly loop when vaulting into a trap.
- Fixed an issue that caused the gold assets in the Temple of Purgation map to appear textureless on Low graphic settings.Fixed an issue that made it possible to become permanently stuck inside the temple doors when in the doorway(s) while the generator on the lower floor was repaired in the Temple of Purgation map.
- Fixed an issue that caused the stun from Head On/Decisive Strike to last longer than 3 seconds.
- Fixed an issue that could cause The Plague's vomit stream to appear in a random area on the ground.
- Fixed an issue that could cause players to spawn on top of a tree when loading into the Lampkin Lane map.
- Fixed an issue that could sometimes cause the progress bar not to visually progress and cleansing animation to loop while Survivors cleansed their sickness.
- Fixed an issue that made it impossible for The Plague to infect items in a chest.
- Fixed an issue that made it impossible for The Plague to use her power in the basement and in the house in the Family Residence map.
- Fixed an issue that made it impossible to Spectate when starting the Kill Your Friends match as a spectator.
- Fixed an issue that made it impossible to blind Killers with the fire cracker items.
- Fixed an issue that made it impossible to repair a generator from one side in the Rotten Fields map.
- Fixed multiple crashes that were introduced in the PTB.
- Fixed the LODs on rocks in The MacMillan Estate maps that caused them to disappear.
- Made 2 hooks available on the lower floor of the Temple of Purgation map when the basement spawns in the Shack.
- Misc The Plague audio improvements.
- Misc customization LOD, Apex & camera improvements.

**The Plague gameplay changes:**

- Corrupt Purge base duration is now 60 seconds instead of 45 seconds.
- Increased The Plague Brutality and Deviousness scoring.
- Increased the duration of infection of environmental objects to 35 seconds instead of 20 seconds.
- Slightly increased The Plague movement speed while charging Vile Purge and Corrupt Purge.
- Slightly reduced The Plague movement Speed while fully charged and holding Vile Purge and Corrupt Purge.
- Survivor infection no longer resets once The Survivor is hooked.
- Vile Purge can now correctly infect gate switches.
- When all Pools of Devotion have been corrupted, all corrupted Pools of Devotion reset and The Killer automatically gains the Corrupt Purge effect.

**Scoring changes:**

- Added a score event (Purge 200) for downing a Survivor with max sickness.
- Increased hitting a Survivor that's not sick increased to 150 from 125 (Infection).
- Increased hitting a Survivor with Corrupt Purge from 250 to 300.
- Increased hitting a sick Survivor with the vomit from 1/0.10 seconds to 2/0.10 seconds.
