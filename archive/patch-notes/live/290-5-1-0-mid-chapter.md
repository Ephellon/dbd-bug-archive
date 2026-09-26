---
title: "5.1.0 | Mid-Chapter"
section: "Live"
article_id: 290
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/290-5-1-0-mid-chapter"
author: "Peanits"
published: "2021-07-27T14:28:47+00:00"
updated: "2021-07-27T14:28:47+00:00"
archived: "2026-09-26T17:09:03Z"
---

<!-- summary -->
## AI TL;DR

Players can now toggle HUD elements in the Settings menu, new tutorials with tooltips were added, lighting on Hospital was improved, and the Trickster received a full overhaul: Laceration max lowered to 6, faster decay, more knives required for Main Event, new knife-hit indicators and several addon tweaks, and the live knife count reduced to 44. Technical tweaks give unhooking priority over self-care, auto-attack on refused grabs, stun validation and corrected killer-only hearing effects. The patch also refreshes many survivor outfits and facial textures and re-enables the Raccoon City Police Department map. Most of the notes cover extensive bug fixes across gameplay, maps, animations, audio and performance.
<!-- /summary -->

<!-- nav -->
&larr; [5.0.2 | Resident Evil](288-5-0-2-resident-evil.md) · [Live](../../index.md#live) · [5.1.1 | Bugfix Patch](291-5-1-1-bugfix-patch.md) &rarr;
<!-- /nav -->

# 5.1.0 | Mid-Chapter

![510Banner.png](../../images/46329d69b5d382ae-510banner.png)

## Features & Content

- Settings Menu - Players will now be able to toggle some of the HUD elements on/off. These include: player names, the killer hook count, and the score events.
- Settings Menu - Players can now reset each category tab individually.
- Lobby - Added a new tooltip for the Store button when the Beginner Mode Tooltips are enabled.
- Lighting and material improvements on Hospital Map

![PatchNotesDivider.png](../../images/ca641380905546af-microsoftteams-image-281-29.png)

## The Trickster Gameplay Update

**Power:**

- Maximum Laceration is now 6 (was 8).
- Faster Laceration decay (full meter depletes in 15 seconds, 20 seconds if running)
- Shorter delay before Laceration starts to decay (now 10 seconds, was 20 seconds)
- Laceration removed upon successful basic attack now 3 (was 4)
- Main Event starts throwing knives 1 second sooner
- 30 knife hits required to activate *Main Event* (was 20)
- 30 second window to activate *Main Event* (was 10)
- New knife hit indicators have been added to show when knives connect with Survivors.

**Addons:**

- Melodious Murder: **Moderately decreases** knives' reload time at lockers.
- Fizz-Spin Soda: Smaller effect (starts at 2 knives thrown instead of 3; balanced with smaller maximum Laceration)
- Iridescent Photocard: When a Survivor’s Laceration Meter is two or less Blade hits away from the maximum, they are inflicted with the **Exposed** status effect.
- Death Throes Compilation: When *Main Event ends*, The Trickster's knives are replenished.
- Lucky Blade: Hitting a survivor with a Blade during *Main Event* **slightly** extends its duration**.** (0.2s)
- Waiting for You Watch: Hitting a survivor with a Blade during *Main Event* **moderately** extends its duration**.** (0.3s)

**Changes from PTB to Live:**

- Now starts with 44 knives (was 60)
- Maximum knife rate of fire bonus after throwing 8 knives is 25% (was 33%)
- Trick Pouch: Adds 4 knives to inventory (was 10)
- Bloody Boa: Adds 8 knives to inventory (was 15)
- Knife hit indicators reduced in size.

**Perks:**

- No Way Out: After hooking a Survivor for the first time, *No Way Out* gains a token. **Once the exit gates have been powered**, *No Way Out* activates.
- **When a Survivor interacts with an exit gate switch, you receive a loud noise notification.** The Entity then blocks both exit gate switches for **12 seconds**, plus an additional **6/9/12 seconds** for each token in your possession.
- Hex: Crowd Control: Effect now lasts 14/17/20 seconds (was 10/12/14 seconds)

![PatchNotesDivider.png](../../images/ca641380905546af-microsoftteams-image-281-29.png)

## Technical Updates

- The unhooking interaction now has higher priority than the Self-Care interaction. If injured, the prompt for unhooking will no longer be replaced with a prompt to self heal.
- When a Killer attempts to grab a Survivor, but the request is refused by the server (usually because the Survivor has stopped performing the interaction) the Killer will now automatically transition into an attack instead. In addition, achievement and challenge progress will be granted at the beginning of the grab attempt, regardless of whether or not the attempt is successful.
- Stun validation has been added to the hit validator. If a Killer has a pending stun on the server, the server will reject the hit. This will be most noticeably in situations such as a Killer who is attacking at the same time a survivor is throwing a pallet, and it should reduce instances where survivors appear to take damage after stunning a Killer.
- Effects that improve a Killer's hearing, such as the perk "Stridor" or the add-on "Swing Chains," will only be heard from the Killer's perspective. Survivors will no longer hear themselves as louder when the Killer is running such effects.
- Effects that modify sound are now multiplicative rather than additive. This means that sounds that are reduced to 0%, such as injured noises by the perk "Iron Will," will no longer be increased by perks such as "Stridor" and will instead remain at 0.

![PatchNotesDivider.png](../../images/ca641380905546af-microsoftteams-image-281-29.png)

**Tutorial Updates**

- Added new tutorials for both Survivor and Killer.
- Menus now have tooltips. This can be turned off in the settings.

**Survivor Visual Updates**

- Updated the original outfits of Dwight, Meg, Jake and Claudette.
- Updated textures and materials on all Prestige outfits.
- Updated the facial models and textures of Ace, Adam, Claudette, David, Dwight, Feng, Jake, Kate, Laurie, Meg, Nea, Quentin and Tapp.
- Updated various hair textures on Ace, Adam, Claudette, David, Dwight, Feng, Jake, Kate, Laurie, Meg, Nea, Quentin and Tapp.
- Updated a variety of characters outfits, textures and materials.
- Updated and fixed a variety of context specific facial animations.
- Minor changes to a variety of new Survivor models based on PTB feedback.

**Miscellaneous**

- Removed the ability for the Plague to infect breakable walls.
- Reduced Nemesis zombie network usage.
- Keys with zero charges no longer can open the Hatch.
- The map offering for Raccoon City Police Department has been re-enabled.
- Implemented changes to prevent players modifying some in-game files (such as models, textures and images).

**Archives**

- A new Tome and Rift will be added to the Archives in the next few days

![PatchNotesDivider.png](../../images/ca641380905546af-microsoftteams-image-281-29.png)

## Bug Fixes

**Gameplay & Performance**

- Fixed an issue that prevented the Nightmare from slowing down while charging the "set snare" interaction.
- Fixed an issue that could prevent the Blight from using his power after being stunned by a pallet while attacking.
- Fixed an issue that could prevent the Clown's gas from applying the Hindered effect to running survivors.
- Fixed an issue that could cause frame rate stuttering when playing as or against The Nemesis.
- Fixed an issue that could cause frame rate stuttering when using the Huntress outfit "The Mordeo".
- Fixed an issue that could cause the perk "Built to Last" to trigger when a med-kit is consumed by activating the add-ons "Anti-haemorrhagic Syringe" or "Styptic Agent."
- Fixed an issue that prevented the Demogorgon's add-on "Red Moss" from correctly applying its slowing effect to the portal exit animation.
- Fixed an issue that could prevent survivors from being affected by the Clown's blurring VFX when playing as Steve Harrington.
- Fixed an issue that could prevent certain VFX from displaying on a totem when a hex is transferred by the perk "Hex: Undying."
- Fixed an issue with bot pathing logic that could affect performance in tutorial bot matches.
- Fixed certain level issues which could affect performance in Lery's Memorial Institute.
- Fixed an issue that could cause Victor to remain stuck blocking a locker if the survivor inside it disconnects.
- Fixed an issue that could cause survivors to become desynchronized if they are being healed at the same time as they are sent to a Cage of Atonement.
- Fixed an issue that allowed players using the Nurse to pitch the camera up or down during the fatigue animation.
- Fixed an issue that prevented zombies from disturbing grass.
- Fixed an issue that could cause the "Exposed" effect from the Clown's "Red Head Pinky" add-on to last indefinitely if the survivor does not move.
- Fixed an issue that could prevent downed survivors from spawning bubble notifications when screaming due to madness.
- Fixed an issue that caused hospital hooks to emit a fleshy sound effect when struck.
- Fixed an issue that could cause a delay before displaying the blocker VFX from the Blight's "Summoning Stone" add-on.
- Fixed an issue that could cause Killers to have to reposition themselves in order to retry damaging a generator from the narrow side.
- Fixed an issue that could cause the add-on "Plaid Flannel" to briefly display the location of the previous blink.
- Fixed an issue that could allow the perk "Fixated" to affect crawling speed.
- Fixed an issue that could cause tokens for the perk "Fast Track" to be consumed when using the toolbox add-on "Brand New Part"
- Fixed certain issues with the perks "Prove Thyself", "Autodidact" and "For the People" that could affect performance
- Fixed a loading issue that could occur on the initial interaction screen and cause the framerate to drop.
- Fixed an issue that caused Nemesis' Tentacle Strike to hit survivors through some of the barred windows at the killer shack and other main buildings.
- Fixed an issue that allowed killers players to see the generator aura from the perk "Blast Mine" when playing as Victor.
- Fixed an issue that could prevent the Spirit's husk from being destroyed by flashlights when aiming at its head.
- Fixed an issue with the perk "Starstruck" that could cause survivors to exit and re-enter the terror radius to lose their exposed status rather than reset it.
- Fixed an issue with the perk "Blood Warden" that could prevent the entity spikes from appearing unless in close proximity.
- Fixed an issue that could allow Pyramid Head to skip his power cooldown by attacking at a certain time.

**Maps & Collisions**

- Fixed an issue that could cause Survivors' legs to clip through the East Office Vaults in the Raccoon City Police Department.
- Fixed an issue that caused the path to be blocked by The Nightmare's clock near the stairs in the Raccoon City Police Department.
- Fixed an issue that could allow the Nurse to blink out bounds in the Raccoon City Police Department.
- Fixed an issue that caused the survivor and killer to get stuck between two rocks near the near the Yamaoka's exit gate
- Fixed an issue that could prevent downed survivors from being picked up in a specific location in the Underground Complex map.
- Fixed an issue that could prevent projectile killer from passing through certain planks.
- Fixed an issue that could cause an invisible collision in the stairs in Coal Tower.
- Fixed an issue that caused The Nightmare to not being able to place a dream pallet at a specific location on Mother's Dwelling.
- Fixed an issue that caused some environment flickering while moving around certain maps.
- Fixed an issue that allowed bear traps to be placed under the snow inside the chair lift in Ormond Resort.

**Animations & Cosmetics**

- Fixed an issue that could cause the Trapper mask "Bronze Visor" to appear silver in the trial.
- Fixed an issue that could cause Ashley J. Williams to float temporarily after escaping a Killer's grasp with the Ashy Slashy cosmetic equipped.
- Fixed an issue that could cause Jill's crawling animation to play incorrectly.
- Fixed an issue that could cause the Wraith's weapon to be invisible in the tally screen after a trial has ended.
- Fixed an issue that could cause keys, maps, and flashlights to use placeholder textures during bot match.
- Fixed an issue that could cause pallet to appear jittering.
- Fixed an issue that could cause survivors to play the wrong animation for hook struggle failure.
- Fixed an issue that could cause killer masks to clip through the camera during the level intro.

**Audio**

- Fixed an issue that prevented exit gate switches from playing the correct sound effects when struck by a weapon.
- Fixed an issue that could prevent the privacy policy pop ups to playing the correct SFX on first boot and after revoking consent

**Other**

- Fixed an issue that could prevent player names in the HUD from exceeding 32 characters.
- Fixed an issue with a possible desynchronization between the actual item sorting and the "Sort by" description in the customization menu
- Fixed an issue where player only receives bloodpoints for completing a tutorial bot match after a reboot.
- Fixed an issue that caused keys, maps and flashlights to use placeholder textures during the tutorial matches with the bots when only the first Chunk installed.
- Fixed an issue that could cause sync errors when trying to complete the survivor tutorial.
- Tentatively fixed an issue that caused wrong pips and ranks to be displayed after a public match.
- Fixed an issue that could cause the blood splatters behind health state icons in the HUD to disappear or appear with a lower opacity than intended.
- Fixed an issue with the analog cursor that sometimes disappeared in the Menus after completing a Trial
- Fixed a lot of Hitches when loading some Hud icons during Gameplay
- Various crash fixes

![PatchNotesDividerSmolWhite.png](../../images/5104b339897e4d25-microsoftteams-image.png)

**PTB Bugfixes**

- Fixed an issue that could cause survivors to disregard the first time they are hit after unhooking themselves.
- Fixed an issue that could impact performance for players when certain debuffs were active.
- Fixed an issue that caused the newly updated perk "No Way Out" to trigger on generator completion rather than proximity to the exit gate switch.
- Fixed an issue that could cause the perk "Dead Hard" to cover less distance when being used.
- Fixed an issue that could prevent the Trapper add-ons "Logwood Dye" and "Tar Bottle" from properly darkening the trap.
- Fixed an issue that could cause incorrect camera obstruction when survivors interact with the Plague's fountain.
- Fixed an issue that caused obsession claws to appear over survivor portraits in the tutorial
- Fixed an issue in the Tally Scoreboard that could cause the Ranks unreadable
- Lots more miscellaneous bugfixes

PS5/XSX only:

- Added an error message when players on those consoles try to connect to a game hosted by a player on Steam.

Switch only:

- Screen capture feature was disabled in order to improve performance.

![PatchNotesDivider.png](../../images/ca641380905546af-microsoftteams-image-281-29.png)

## Known Issues

- Some strings related to Tome / Rift VIII are not localized to non-English languages.
- Male Legendary characters will not have facial idle animations in-game, they'll just use their default idle/injured idle throughout the game.
- Equipping an item in the store and quitting the game, will not save this customization item next time the game is launched. Consoles only.

<!-- nav -->
&larr; [5.0.2 | Resident Evil](288-5-0-2-resident-evil.md) · [Live](../../index.md#live) · [5.1.1 | Bugfix Patch](291-5-1-1-bugfix-patch.md) &rarr;
<!-- /nav -->
