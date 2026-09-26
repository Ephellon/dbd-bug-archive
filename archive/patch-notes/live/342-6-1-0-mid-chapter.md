---
title: "6.1.0 | Mid-Chapter "
section: "Live"
article_id: 342
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/342-6-1-0-mid-chapter"
author: "Mandy"
published: "2022-07-19T14:30:21+00:00"
updated: "2022-07-19T14:30:21+00:00"
archived: "2026-09-26T16:40:43Z"
---

<!-- summary -->
## AI TL;DR

Mid-Chapter 6.1.0 introduces Tome 12 “DISCORDANCE,” adds five new maze tiles to McMillan Estate, and overhauls core gameplay: generators now take 90 seconds for a solo repair, killer actions (hits, kicks, pallet hits) are 10 % faster, and a baseline Borrowed Time grants unhooked survivors a temporary speed boost and Endurance. Several killer and survivor perks receive major tweaks, including Barbecue and Chili losing its bloodpoint bonus, Dark Devotion triggering on any health loss, and Borrowed Time, Dead Hard and Off The Record reworked. The prestige and bloodweb systems are rebuilt with higher BP caps, new prestige levels, and altered rewards; Shrine of Secrets now unlocks perks globally. Matchmaking incentives, UI layout, Doctor performance, and dozens of map, animation and audio bugs are also fixed.
<!-- /summary -->

<!-- nav -->
&larr; [6.0.2 | Bugfix Patch](339-6-0-2-bugfix-patch.md) · [Live](../../index.md#live) · [6.1.1 | Bugfix Patch](343-6-1-1-bugfix-patch.md) &rarr;
<!-- /nav -->

# 6.1.0 | Mid-Chapter 

![banner[1].png](342-6-1-0-mid-chapter/01-banner-5b1-5d.png)

## CONTENT

- "Tome 12: DISCORDANCE" of The Archives (starts July 20th 11AM ET)
- Added 5 maze tiles to the pool in the McMillan Estate map

![User: "patchnotesdividersmolwhite[1].png"](342-6-1-0-mid-chapter/02-patchnotesdividersmolwhite-5b1-5d.png)

## GAMEPLAY

- Generators take 90 seconds for a single survivor to repair (was 80 seconds)
- Killers kicking a generator now immediately cause a 2.5% loss of progress in addition to starting regression
- Bloodlust trigger times have been reduced to 15 seconds for Tier 1, 25 seconds for Tier 2, and 35 seconds for Tier 3 (was 15 seconds, 30 seconds, and 45 seconds)
- The following Killer actions have been sped up by 10%:
  - Cooldown time after a successful hit has been reduced to 2.7 seconds (was 3 seconds)
  - Time to kick a generator has been reduced to 1.8 seconds (was 2 seconds)
  - Time to kick a pallet or wall has been reduced to 2.34 seconds (was 2.6 seconds)
- Duration of the Survivor speed boost when hit has been reduced to 1.8 seconds (was 2 seconds)
- Survivors now have a modified version of Borrowed Time as a baseline ability, no perk required
  - Unhooked Survivors now get a 7% movement speed bonus and Endurance for 5 seconds
  - The speed bonus and Endurance effect are removed if the Survivor performs a Conspicuous Action
    - ***Includes: Repairing a Generator, healing yourself or others, cleansing or blessing a Totem, sabotaging a hook, unhooking a survivor, and opening an exit gate.***
  - Added a new section and description to the Game Manual
- Endurance status effect is now cancelled by Conspicuous Actions
- Endurance does not prevent a Survivor from entering the dying state if they are inflicted with Deep Wound

![patchnotesdividersmolwhite[1].png](342-6-1-0-mid-chapter/03-patchnotesdividersmolwhite-5b1-5d.png)

## KILLER PERKS

- **Barbecue and Chili**
  - Removed Bloodpoint bonus
- **Corrupt Intervention**
  - Added: Corrupt Intervention deactivates when any Survivor enters the dying state.
  - *Note: The perk still deactivates after 2 minutes if no Survivor has entered the dying state.*
- **Coulrophobia**
  - Added: Healing Skill Checks move 50% faster for Survivors under the effect of this perk.
- **Dark Devotion**
  - Now triggers when a Survivor loses a health state by any means (was just basic attacks)
- **Eruption**
  - Increased Generator reduction when a Survivor enters the dying state to 10% (was 6%)
  - Increased duration of Incapacitated status effect to 15/20/25 seconds (was 12/14/16 seconds)
- **Hex: No One Escapes Death**
  - Added: Once the Hex's effect is revealed to the Survivors, its Hex Totem's aura is shown to the Survivors at a range of 4 meters. This range increases steadily over the next 30 seconds to 24 meters.
- **Hex: Ruin**
  - Added: Once any Survivor is killed by any means, the Hex: Ruin Totem reverts to a Dull Totem.
  - While a generator is not being repaired by a Survivor, it will immediately and automatically regress repair progress at **50%/75%/100%** of the normal regression speed.
- **Jolt**
  - Removed the cooldown
- **Knock Out**
  - Added: Recovery speed is reduced by 25% for Survivors under the effect of this perk.
- **Lethal Pursuer**
  - Added: Any time a Survivor's aura is shown for a period of time, its duration is increased by **2 seconds**.
  - *Note: The new effect applies to the duration of the normal Lethal Pursuer effect, which means it effectively reveals survivors for 9/10/11 seconds at the start of the match.*
- **Monstrous Shrine**
  - Reworked - This perk is now Scourge Hook: Monstrous Shrine
  - **Scourge Hooks**
  - grant 10/15/20% faster Entity progression if the Killer is not within 24 meters. Basement hooks count as Scourge Hooks. T
- **Overcharge**
- Added: After Overcharge is applied to a generator, its regression speed increases from 75% of normal to 200% of normal over the next 30 seconds.
- **Pop Goes the Weasel**
  - Changed regression to be 20% of current progress (was 25% of total)
  - *Note: This is calculated after the new baseline regression when kicking a generator.*
- **Scourge Hook: Gift of Pain**
  - Increased Healing and Repairing speed penalty to 10/13/16% (was 7/8/9%)
- **Scourge Hook: Pain Resonance**
  - Removed scream effect on Survivors repairing the exploding generator, generator will spark to show regression
- **Thanatophobia**
  - Increased individual penalties for repairing, sabotaging, and Totem cleansing to 4.5/5/5.5% (was 4/4.5/5%)
  - Increased maximum penalty to 18/20/22% (was 16/18/20%)
- **Tinkerer**
  - Added: This effect can only be triggered once on each generator.

![patchnotesdividersmolwhite[1].png](342-6-1-0-mid-chapter/04-patchnotesdividersmolwhite-5b1-5d.png)

## Survivor Perks

- **Borrowed Time**
  - Reworked to account for the baseline version of the effect
  - Survivors you unhook keep their Endurance status effect for an extra 6/8/10 seconds and their movement speed bonus for an extra 10 seconds.
- **Botany Knowledge**
  - Increased healing speed bonus to 30/40/50% (was 11/22/33%)
  - Changed Medkit efficiency bonus to a -20% efficiency penalty (was +10/20/30%)
- **Calm Spirit**
  - Increased chance to avoid alerting crows to 100% (was 80/90/100%)
  - Added: Allows you to open chests and cleanse/bless totems silently, but at 40/35/30% reduced speed.
- **Dark Sense**
  - Reworked: Each time a generator is completed, Dark Sense activates. While Dark Sense is active, the Killer entering a 24-meter radius around you reveals their aura for 5/7/10 seconds. Once the aura's duration expires, Dark Sense deactivates.
  - *Note: The effect triggers if the Killer is already within 24 meters when the perk is activated.*
- **Dead Hard**
  - Removed the dash / dodge element of the perk.
  - Activating Dead Hard now grants the Survivor Endurance for 0.5 seconds
  - An animation plays when activated so Killers can see when the perk is used without the Survivor being hit
- **Decisive Strike**
  - Added: The perk and its effects are disabled if the exit gates are powered.
  - The perk is now disabled when the Survivor performs a Conspicuous Action (Defined earlier in the patch notes under the Gameplay section)
  - Stun duration is now 3s down from 5s
- **Déjà Vu**
  - Added: Gain a 5% repair speed bonus on the generators revealed by Déjà Vu.
- **Distortion**
  - Reduced the starting tokens to 3 (was 4)
  - Removed stipulation preventing the perk from activating when in a Killer Trap
  - Added: Regain a token for each 30 seconds spent inside the Killer's Terror Radius. Distortion may not have more than 3 tokens.
  - Added: Audio cue when a token is used
- **Hope**
  - Removed time limit.
- **Inner Focus**
  - Removed the distance restriction on seeing the Scratch Marks of other Survivors (was 32 meters)
- **Iron Will**
  - Reduced the grunts of pain volume reduction to 25/50/75% (was 50/75/100%)
  - Added: Does not function while Exhausted. Does not inflict Exhausted.
- **Lightweight**
  - Increased reduction of scratch mark duration to 3/4/5 seconds (was 1/2/3 seconds)
  - Added: Your scratch marks are spaced inconsistently.
- **Lucky Break**
  - Added: For each 1 second spent healing another Survivor, increase *Lucky Break's* duration by 1 second. *Lucky Break's* duration cannot increase beyond its starting value.
- **No One Left Behind**
  - Now triggers when the Exit Gates are powered (was triggered when an Exit Gate was opened)
  - Added: When unhooking a Survivor, they gain a 7%movement bonus for 10 seconds.
- **Off the Record**
  - Added: Once you are unhooked or escape from the hook,*Off the Record* activates for **60/70/80seconds**.
  - Added: Gain the Endurance status effect.
  - Added: Off The Record is disabled when the exit gates are powered.
- **Overzealous**
  - Increased repair speed buff to 6/7/8% (was 4/5/6%)
  - Added: This bonus is doubled if you cleanse an Hex totem.
- **Pharmacy**
  - Now guarantees an Emergency Med-Kit in every chest (was just the first chest opened), when injured
- **Saboteur**
  - Scourge Hooks now have a yellow aura when a Survivor is being carried.
- **Self-Care**
  - Reduced the self heal speed to 25/30/35% (was 50%)
  - Removed Med-Kit efficiency bonus
- **Sole Survivor**
  - Added: When you're the last Survivor alive, gain 75% action speed when repairing generators and 50% action speed while opening an exit gate or the Hatch.
- **Spine Chill**
  - Reworked: Get notified when the Killer within a 36-meter range. If the Killer is within range and is looking at you with a clear line of sight, your speed while repairing, sabotaging, healing, unhooking, cleansing, blessing, opening exit gates and unlocking is increased by 2%/4%/6%. The effects of *Spine Chill* linger for 0.5 seconds after the Killer looks away or is out of range. *Spine Chill's* icon indicates the strength of the Killer's Terror Radius.
- **Tenacity**
  - Added: Grunts of pain while in the dying state have their volume reduced by 75%.
- **We're Gonna Live Forever**
  - Reworked: When healing another Survivor in the dying state, your healing speed is increased by 100%. Additionally, performing any of the following actions activates this perk's secondary function: Perform a Safe Hook Rescue, Take a hit to protect a Survivor, Rescue a Survivor by stunning the Killer with a pallet, Rescue a Survivor by blinding the Killer with a Flashlight. When this perk's secondary function is active, healing another Survivor out of the dying state grants them Endurance for 6/8/10 seconds and deactivates the secondary function.

![patchnotesdividersmolwhite[1].png](342-6-1-0-mid-chapter/05-patchnotesdividersmolwhite-5b1-5d.png)

## Progression

- The Progression and Prestige systems have been reworked
- **IMPORTANT: No existing perks, items, or cosmetics will be lost if they are already unlocked on a character, even if having them would contradict the rules of the new system**.
- Global Bloodpoint soft-cap has been raised to 2,000,000 (was 1,000,000)
- Bloodpoint Categories maximum raised to 10,000 (was 8,000)
- Prestiging no longer removes any items, add-ons, offerings, perks, or perk slots
- Teachable Perks have been removed from the Bloodweb
- Level 51 in the Bloodweb requires the character to Prestige, costing 20,000 Bloodpoints
- Characters can now each be prestiged up to 100 times
- Prestiging a character has the following rewards:
- Prestige 1: The character's perks are immediately unlocked for use on all other Killers / Survivors at Tier 1
- Prestige 2: The character's perks are immediately unlocked for use on all other Killers / Survivors at Tier 2
- Prestige 3: The character's perks are immediately unlocked for use on all other Killers / Survivors at Tier 3
- Prestige 4-6: Bloodied cosmetic items (when available for the specific character)
- Prestige 7-9: Perk Charms for the character's perks
- Existing players will have their characters granted prestige levels in the new system based on the following:
- +2 additional levels per existing Prestige level
- Example: A Prestige 1 character will receive +2 levels, resulting in being Prestige 3 in the new system
- If the character has 70 or more Perks unlocked (Counting each tier of a perk separately):
  - +1 level for 70-119 Perks
  - +2 levels for 120-169 Perks
  - +3 levels for 170-219 Perks
  - +4 levels for 220-269 Perks
  - +5 levels for 270-319 Perks
  - +6 levels for 320+ Perks
- Prestige 9 is the highest level a character can be when transferring to the new system, even if the above rules say they should be higher
- Existing unlocked Teachable Perks will immediately grant access to Tier 1 of that Perk on all characters if no other mechanic has already granted access to the Perk
- Added unique Prestige Crest artwork for each prestige level
- Characters who are already at Prestige 3 on the old system will unlock a Bloody Prestige Portrait on the character selection screen
  - Can be toggled on / off in the Options menu

## Shrine of Secrets

- Teachable Perks have been removed from the Shrine of Secrets
- Purchasing a Perk on the Shrine of Secrets now immediately unlocks that Perk on all Killers / Survivors at the displayed Tier level
  - Tier 1 - 2,000 Iridescent Shards
  - Tier 2 - 4,000 Iridescent Shards
  - Tier 3 - 6,000 Iridescent Shards
- You must purchase Tier 1 before you can purchase Tier 2, and Tier 2 before Tier 3, unless you have already unlocked the Perk via the Prestige System
- Having the perk already available via the Prestige System discounts the price:
  - Tier 1 via Prestige - 2,000 Iridescent Shards for Tier 2, 4,000 Iridescent Shards for Tier 3
  - Tier 2 via Prestige - 2,000 Iridescent Shards for Tier 3
- The same Perk may be purchased multiple times on a single rotation of Shrine of Secrets
- Purchasing a Perk that you already have at Tier 3 will convert the Iridescent Shards to 100,000 Bloodpoints
  - This can only be done once Shrine of Secrets rotation per Perk (maximum of 4 times on a single rotation, assuming you have all 4 Perks already at Tier 3)

![patchnotesdividersmolwhite[1].png](342-6-1-0-mid-chapter/06-patchnotesdividersmolwhite-5b1-5d.png)

## Matchmaking Incentives

- Matchmaking Incentives have been added to the game
- Not available to players who have Cross-Play disabled
- When the Survivor:Killer ratio in the active Matchmaking queue drifts too far from optimal (4:1), players will receive BP bonuses to enter the queue as the needed role
  - *Note: Players can also expect queues with a large Incentive bonus to have faster queue times!*
- Matchmaking Incentives will appear on the Main menu and in the Lobby next to the Ready button.

![patchnotesdividersmolwhite[1].png](342-6-1-0-mid-chapter/07-patchnotesdividersmolwhite-5b1-5d.png)

## UI

- Made UI layout changes to accommodate the new Prestige Crest on multiple screens.
- Character Info button has been moved to the side tabs in the Lobby UI.
- Replaced Character Swap buttons/prompts with a Previous/Next button in the Lobby UI footer.

![patchnotesdividersmolwhite[1].png](342-6-1-0-mid-chapter/08-patchnotesdividersmolwhite-5b1-5d.png)

## Optimization

- Optimized the Doctor's performance.
  - *Dev Note: The Doctor currently has one of the largest impacts on performance for Killers. These performance optimizations should help improve that on all platforms.*

![patchnotesdividersmolwhite[1].png](342-6-1-0-mid-chapter/09-patchnotesdividersmolwhite-5b1-5d.png)

## Changes from PTB

- Reduced Prestige node cost from 50,000 to 20,000
- Increased Bloodpoint Category caps from 8,000 to 10,000
- Increased Global Bloodpoint soft-cap from 1,000,000 to 2,000,000
- Rules for converting Prestige levels from the old system to the new system have been made more rewarding, but with a maximum starting point of Prestige 9
- Reworked the Prestige Portrait reward for players who had already reached Prestige 3 on a character
- Reworked the Prestige Perk Charm visuals
- Reworked the Prestige Crest visuals
  - *Dev Note: We received a lot of feedback on the PTB about the grind not being reduced enough when only focusing on a few characters, especially in relation to the cost of the Prestige node on the bloodweb. In response, we have reduced the BP cost of the Prestige node as well as raising various BP caps to allow for more BP to be earned, stocked up, and spent. We've additionally adjusted the transition rules for the Prestige system in such a way that players who reached Prestige 3 in the old system will immediately be Prestige 9 and thus unlock all associated perks, cosmetics, and charms immediately for the character.*
- Endurance no longer stops a Survivor from going down if they have Deep Wound
- Dead Hard's Endurance duration reduced from 1 second to 0.5 seconds
- Off The Record is now disabled when the Exit Gates are powered
- Overcharge's regression has been reduced from 100%-400% to 75%-200%
- Botany Knowledge now has a Medkit efficiency penalty of -20%
- Spine Chill now has additional Terror Radius visual feedback
- Inner Focus no longer has a distance restriction on viewing scratch marks
  - *Dev Note: On the PTB we saw many instances where Survivors were able to queue up several instances of Endurance one after the other, and being able to tank far too many additional hits. Changing Endurance to not trigger when a player has Deep Wounds will prevent this from being as effective, as Survivors will now need to mend the Deep Wound in order to benefit from Endurance a second time. Off The Record was also proving to be too strong during the end game, since there are no required Conspicuous Actions at that point, and will now disable once the gates have been powered.*

![patchnotesdividersmolwhite[1].png](342-6-1-0-mid-chapter/10-patchnotesdividersmolwhite-5b1-5d.png)

## Bug Fixes

- Fixed an issue that caused players to experience rubber banding during gameplay.
- Fixed an issue that caused the Dredge's head to clip through the camera when teleporting to a locker.
- Fixed an issue that caused the Hillbilly to be able to use his momentum to reach inaccessible areas.
- Fixed an issue that caused the Artist's Scanning Crows not to reveal Killer Instinct on Survivors in the dying state.
- Fixed an issue that caused Lucky Break perk to activate during the camera pan at the start of the match when having the No Mither perk equipped.
- Fixed an issue that caused the extra fatigue duration from chain blinks to be unaffected by the Nurse's Catatonic Boy's Treasure add-on.
- Fixed an issue that caused the Built To Last perk to continue recharging the item when interrupted going into a locker.
- Fixed an issue that caused the aura reading effect from the Knock Out perk to apply to Survivors that are downed by other means than the Killers basic attack.
- Fixed an issue that caused the skill check wiggle UI to briefly appear after succeeding a Decisive Strike skill check.
- Fixed an issue that caused the Decisive Strike perk to remain active indefinitely if the Killer is stunned when the skill check need is in the success zone.
- Fixed an issue that caused the Invigorated status effect from the Clown's Afterpiece Antidote to last longer when exiting a gas cloud as it activates.
- Fixed an issue that caused the Legion's Feral Frenzy combo not to reset when blinding them mid lunge attack.
- Fixed an issue that caused the Wraith's "Shadow Dance" - White add-on to increase the locker opening speed while cloaked.
- Fixed an issue that could cause the healing progress bar to remain on screen after the healing action is completed when affected by the Hemorrhage status effect.
- Fixed an issue that caused only one Survivor to grunt when one or more Survivors stopping the healing action while affected by the Hemorrhage status effect when close by to each other.
- Fixed an issue that caused cleansing a totem while under the Broken status effect to still activate the Inner Healing perk when the broken status effect ends.
- Fixed an issue that caused the "Brand New Part" add-on to bypass the Survivors screaming when the Eruption and Scourge hook: Pain Resonance perks are triggered.
- Fixed an issue that caused Survivors to recover indefinitely with Soul Guard once affected by the Hex: Plaything or Hex: Pentimento perks.
- Fixed an issue that caused the Haste status effect icon to be missing when affected by Hex: Devour Hope.
- Fixed an issue that caused the Hex: Undying perk to reveal Survivor auras when they are near a Boon Totem.
- Fixed an issue that caused the Deathbound perk not to give progress to the Punch Drunk achievement (trophy for Sony platforms).
- Fixed an issue that caused the Pig's Ambush Dash animation to freeze when hitting an asset.
- Fixed an issue that caused a missing animation when vaccinating another Survivor.
- Fixed an issue that caused a missing animation when Survivors open an exit gate while injured and contaminated by the Nemesis' T-Virus.
- Fixed an issue that caused the Nightmare's Dream Pallet placing animation to be missing.
- Fixed an issue that caused the Hag's trigger range add-ons (Bog Water, Bloodied Water, Bloodied Mud) to have no functionality.
- Fixed an issue that caused the Cannibal's Shop Lubricant add-on not to hide the auras of downed Survivors when using the chainsaw.
- Fixed an issue that caused the Nightmare's Pill Bottle add-on not to make him invisible to awake Survivors after dropping and picking up a Survivor.
- Fixed an issue that caused the Madness Tier II effect of the Doctor's "Calm" add-ons not to match the description.
- Fixed an issue that caused the Flashbang and Firecracker items to be unusable when running down stairs.
- Fixed an issue that caused the Streetwise perk to remain active in the area when the Survivor with it was Sacrificed, Killed or disconnected.
- Fixed an issue that caused the Adrenaline perk to give progress to the Generosity challenges.
- Fixed an issue that caused the Heroic Virtue challenge to gain progress when the Killer disconnects.
- Fixed an issue that caused the Kinship perk not to give clear feedback when the perk is activated.
- Fixed an issue that caused the Nemesis' Prestige outfit to have a hole in the hand.
- Fixed an issue that sometimes caused the Killer to not be able to pick up a Survivor who's downed on the basement stairs after using ''Dead Hard''.
- Fixed an issue that caused equipped charms to not appear for other survivors in a survivor lobby.
- Fixed an issue where the Hillbilly's chainsaw revving sound effect does not continue for the entire duration of the charge animation..
- Fixed an issue that caused the Conscious Concoction charm UI icon to appear different from its actual model.
- Fixed an issue that caused survivor bots to toggle their flashlights rapidly.
- Fixed an issue that caused some users to be unable to remove EGS friends from their friends list.
- Fixed an issue that could cause the daily rituals screen to soft-lock the application.
- Fixed an issue that could cause a loss of progress when launching the game on 6.1.0 for the first time.
- Fixed an issue that caused items, addons and offerings to not be lost after a trial.
- Fixed an issue that caused legacy character customizations to disappear after rebooting the game on 6.1.0.
- Fixed an issue that enabled a Killer to body block the access to the basement in the main building in Junkyard.
- Fixed an issue where the Killer is unable to go through a specific spot on Lerys Memorial Institute.
- Fixed an issue where the Killer can't pick up a downed Survivor on top of the logs in Garden of Joy.
- Fixed an issue where a pile of debris in Lery Memorial blocks the Blight when using Blighted Corruption power.
- Fixed an issue that caused an invisible collision preventing Killers to access the basement in Coal Tower.
- Fixed an issue that caused a generator that couldn't be repaired on one side in Dead Dawg Saloon.
- Fixed an issue that caused a green glyph that can't be interacted with in Midwich Elementary School.
- Fixed an issue where some rocks can be climbed on by stepping around it in Garden of Joy.
- Fixed an issue where survivors are able to reach on top of the shelf barrels in Gideon Meat Plant.
- Fixed an issue that caused the hatch to sometimes spawn inside the basement.
- Fixed an issue that caused the Jigsaw's Annotated Plan add-on to remove 30 seconds from the reverse bear trap timer instead of 10 when the last generator is completed.
- Fixed an issue that may cause succeeding a Brand New Part skill check not to give generator repair progress.
- Fixed an issue that may cause survivors to be unable to exit some lockers when facing the Trickster.
- Fixed an issue that caused some green glyphs not to be accessible.
- Fixed an issue that make Mikaela's hair to not have the white outline aura from the Nightmare's POV in the Dream State.
- Fixed an issue that caused the smoke cloud to appear as small repeated patterns in the Punishment of the Damned VFX.
- Fixed an issue that caused the VFX of Ghost Face's Glacial Shroud to be seen through fog.

## Audio

### Characters:

- Fixed an issue where the Hillbilly's chainsaw revving SFX does not continue for the entire duration of the charge animation
- Fixed an issue where the wrong audio cue would be called when selecting a Survivor from the Role Selection menu
- Fixed an issue where the female survivors voice over would not follow the character's mouth movement when being hooked
- Fixed an issue where only one Survivor would grunt when two Survivors would stop healing closely at the same time while being affected by Hemorrhage
- Fixed an issue where, in some rare instances, some Killer's Bloodweb sound would be stuck in an infinite loop
- Added Entries for Tome 12 of the Archives

### Perks:

- Fixed an issue where the Tenacity perk would only reduce grunts of pain after Survivors would move from their initial falling point
- Added a new audio indicator when losing a token when Distortion hides a player's aura

### General:

- Fixed an issue where multiple instances of the same audio cues would play in menus
- Fixed an issue where when a Killer would hit a wooden table, the incorrect surface sound would be played
- Fixed an issue where the small pole Generators would fail to throw confetti and would not play the correct SFX once completed in specific maps
- Fixed an issue where when changing from the Play As Killer menu to the Store, the Killer's sound effects would be missing
- Fixed an issue where there was no audio cue when a Killers would be stunned while under the effect of the Orange Glyph
- Audio optimisation pass on Midwich Elementary School to prevent audio cuts

### Platform specific:

**Xbox One:**

- Fixed an issue where the game would crash when muting the game on Xbox One

**Nintendo Switch:**

- Fixed an issue where after extended periods of play, the application would run out of memory after quitting the Tally Screen.

![patchnotesdividersmolwhite[1].png](342-6-1-0-mid-chapter/11-patchnotesdividersmolwhite-5b1-5d.png)

## Fixed from PTB

- Fixed an issue that caused the post unhook endurance and speed bonus timers to start during the animation instead of at the end.
- Fixed an issue that caused the sparks emitted by a generator to be too intense when damaged.
- Fixed an issue that caused Hex: Ruin to deactivate at the beginning of the hook sacrifice animation instead of the end.
- Fixed an issue that may cause the application to crash when the Hex: No One Escapes Death perk is used.
- Fixed an issue that caused killers not to see the Haste status icon when the Hex: No One Escapes Death perk activates.
- Fixed an issue that caused the Exposed icon to disappear when Hex: No One Escapes Death is transferred to the Hex: Undying totem.
- Fixed an issue that caused killers not to be able to kill the survivors when having 5 tokens on the Hex: Devour Hope perk.
- Fixed an issue that caused the Hex: Devour Hope Exposed effect not to be revealed when injuring survivors using certain killer powers.
- Fixed an issue that caused the Lethal Pursuer perk not to reveal survivors' auras for the correct duration at the start of the trial.
- Fixed an issue that caused the aura reveal duration from some of The Shape's add-ons not to be increased by the Lethal Pursuer perk.
- Fixed an issue that caused survivors under the effects of the Prove Thyself perk not to see the perk icon or the yellow progress bar.
- Fixed an issue that caused the repair speed bonus not to be applied when a survivor is already working on a generator when it becomes revealed by the Déjà Vu perk.
- Fixed an issue that caused the repair speed bonus to continue to be applied when a survivor is working on a generator that stops being revealed by the Déjà Vu perk.
- Fixed an issue that caused survivors under the Broken status effect to be healed to full health when removing the Plague's sickness at a fountain.
- Fixed an issue that caused the aura of the Illusionary Doctor to flicker briefly in front of the killer's camera when activated.
- Fixed an issue that caused some HUD elements to become hidden for the remainder of the trial after switching to Victor when playing as the Twins.
- Fixed an issue that caused several actions not to be blocked during the tutorial.
- Fixed an issue that caused Bill's cigarette smoke to be misaligned.

![patchnotesdividersmolwhite[1].png](342-6-1-0-mid-chapter/12-patchnotesdividersmolwhite-5b1-5d.png)

## Known Issues

- *Warrior Goddess* for Feng Min has been disabled to prevent a crash
- The Rancor perk activates when the hatch is closed regardless of how many generators were left
- The Nightmare is unable to place Dream Snares in the kitchen in Badham Preschool.
- Bloodweb cap has been increased to 2 million bloodpoint, even though the tooltip still read as 1 million.
- The matchmaking incentives text is present in Play as Killer without having the BloodPoint Bonus.
- Terror Radius feedback on *Spine Chill* functions in reverse (ie Drains as the TR gets louder, instead of filling

<!-- nav -->
&larr; [6.0.2 | Bugfix Patch](339-6-0-2-bugfix-patch.md) · [Live](../../index.md#live) · [6.1.1 | Bugfix Patch](343-6-1-1-bugfix-patch.md) &rarr;
<!-- /nav -->
