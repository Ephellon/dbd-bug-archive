---
title: "5.4.0 | Portrait of a Murder"
section: "Live"
article_id: 306
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/306-5-4-0-portrait-of-a-murder"
author: "Peanits"
published: "2021-11-30T15:27:06+00:00"
updated: "2021-11-30T16:05:51+00:00"
archived: "2026-09-26T17:09:00Z"
---

<!-- summary -->
## AI TL;DR

Added a new Killer The Artist with Grim Embrace, Scourge Hook: Pain Resonance and Hex: Pentimento, a new Survivor Jonah Vasquez with Overcome, Corrective Action and Boon: Exponential, and the new map Eyrie of Crows. Loadout and customization menus now feature numbered page markers, the Store shows a New/Sale badge, and subtitles can be toggled for in-game speech (currently only Trickster).

The remainder of the update is a broad bug-fix sweep touching tutorial UI, perk and totem interactions, sound cues, item charge handling, animation hitches, map geometry issues and several killer-specific glitches, plus a performance optimisation for The Spirit and balance adjustments to the Cenobite’s addons.
<!-- /summary -->

<!-- nav -->
&larr; [5.3.2 | Bugfix Patch](303-5-3-2-bugfix-patch.md) · [Live](../../index.md#live) · [5.4.1 | Bugfix Patch](307-5-4-1-bugfix-patch.md) &rarr;
<!-- /nav -->

# 5.4.0 | Portrait of a Murder

![540Banner.png](../../images/ef718e02ba7b05c6-540banner.png)

## Features

- Added a new Killer - The Artist
  - Perks - Grim Embrace, Scourge Hook: Pain Resonance, and Hex: Pentimento
- Added a new Survivor - Jonah Vasquez
  - Perks - Overcome, Corrective Action, and Boon: Exponential
- Added a new map - Eyrie of Crows
- Loadout and Customization menus now have Page Markers
  - Markers include the number of the page
  - Markers can be directly selected to jump to the desired page
- Added a New/Sale badge to the Store
- Added Subtitles to the HUD
  - Can be toggled in the options
  - Only applies to in-game speech (just The Trickster at this time)

## Content

- Re-enabled location restriction when snuffing Boon totems
- Updated the character portraits for Meg, Dwight, Adam, and Laurie.
- Updated the character background images in the Character Info and Store menus for Quentin, Feng, Kate, David, Jake, Nea, Adam, Meg, and Dwight.
- Added input prompts for the Anti-Hemorrhagic Syringe, Styptic Agents, and Glass Beads add-ons
- The Store DLC Purchase Popup now specifies the character associated with exclusive items

### Cenobite Addon Update

- Add-on - Liquified Gore
  - Decreased solving time modifier to 1 second (was 2 seconds)
- Add-on - Torture Pillar
  - Decreased Chain Hunt activation time to 5 seconds (was 10 seconds)
- Add-on - Larry's Remains
  - Decreased solving time modifier to 2 seconds (was 4 seconds)
- Add-on - Chatterer's Tooth
  - Increased Undetectable status to duration 25 seconds (was 12 seconds)
- Add-on - Engineer's Fang
  - Added effect: When hitting an injured Survivor with a possessed chain, only 1 additional chain will spawn
- Add-on - Iridescent Lament Configuration
  - Increased range to 24 meters (was 16 meters)

*Dev Note: The Cenobite has been overperforming since he came to DbD. These addon changes are intended to bring his five best performing addons more in line to reduce his overall power, accompanied with a buff to his worst performing addon.*

## Optimization

- Optimized The Spirit's performance

*Dev Note: The Spirit has the largest impact on performance of any Killer, technically speaking. These performance optimizations should help alleviate that on all platforms.*

## Bug Fixes

- Fixed the broken Game Manual tab on the Tutorial screen.
- Fixed an issue that allowed survivors to consume other survivor's Clairvoyance perk.
- Fixed an issue that caused blessing a totem not to disable Decisive Strike.
- Fixed an issue that caused the Clairvoyance perk not to be deactivated when speared.
- Fixed an issue that caused Boon Totem vignettes to disappear when moving between overlapping Boon ranges.
- Fixed an issue that may cause the Boon Totem vignette to linger when the survivor who applied a Boon leaves the match.
- Fixed an issue where skill checks would be absent when self-healing with the Self-Care or Boon: Circle of Healing.
- Fixed an issue that may cause the sound notification for the 4th generator completed not to trigger.
- Fixed an issue that may cause items, including medkits and toolboxes, with charge modifier add-ons to only apply 99% of their charge.
- Fixed an issue that caused a hitch to occur at the end of vaults with the Legion.
- Fixed an issue that caused Hag traps set in the Asylum's entrance not to get triggered.
- Fixed an issue that let The Nightmare place Dream Snares which would not be seen from below on top of stairs.
- Fixed an issue that may cause the Afterpiece Tonic gas not to match the affected area when the bottle explodes high above ground level.
- Fixed an issue that may cause survivors to be attacked by the Chain Hunt while they are solving the Lament Configuration.
- Fixed an issue that caused a placeholder icon to be seen when affected by another player's Leader perk.
- Fixed an issue that caused a gun SFX to be heard when entering into the tally screen as The Deathslinger.
- Fixed an issue that caused non-lethal interruptions not to grant progress towards the Quick Draw achievement.
- Fixed an issue that may cause the camera in the Killer lobby to be off center.
- Fixed an issue that may cause a hitch to occur after vaulting when using the Lithe perk.
- Fixed an issue that may cause a hitch to occur when unhooking a survivor or entering a closet.
- Fixed an issue that may cause The Cannibal to lose the ability to use his power after getting stunned.
- Fixed an issue that caused clients de-synchronizations after running in the main buildings of various maps (Yamaoka, Macmillan, Ironwork of Misery, Coal Tower).
- Fixed an issue that caused archives progress to be shareable between different accounts by switching accounts in the main menu.
- Fixed an issue that caused the end game music to stop playing after using the Legion’s Feral Frenzy.
- Fixed an issue that caused the Mori music not to play for killers playing the Nemesis.
- Fixed an issue that may cause the wrong VFX and SFX to play when a Hex Totem was destroyed by a survivor.
- Fixed an issue that prevented a Gateway’s SFX from stopping after it is closed while playing against The Cenobite.
- Fixed an issue that prevented Chainsaw SFX from playing after The Cannibal’s Tantrum impacts an object.
- Fixed an issue that prevented repair sfx from playing when repairing generators in the Survivor tutorial.
- Fixed an issue that caused the Survivor to crawl into a corner near a totem to prevent being picked up by the Killer in the main building of Yamaoka Family Residence.
- Fixed an issue that caused the Survivor to get on top of some cars near the Azarov Office.
- Fixed an issue that caused a crouching Survivor get stuck near the stairs of one of the house in Dead Dawg Saloon.
- Fixed an issue that caused Survivors and Killers to climb on top of a cart near the gallows of Dead Dawg Saloon.
- Fixed an issue that caused Killers to be unable to walk through a doorway on RPD if the hatch spawned in that location.
- Fixed an issue that caused the Survivors to not interact with one of the Nightmare's clocks in RPD map on XSX only.
- Fixed an issue that caused the "health line" visual in The Nemesis's power effect behind the Survivor HUD portraits to disappear.
- Fixed an issue that caused players to remain stuck in the result screen after a game.
- Fixed an issue that caused a wireframe to be visible on Survivors on some platforms.

## Known Issues

- There are missing Meat Barrels in the Thompson House Bathroom causing an invisible collision.
- A couple of Trickster voiceover lines are not localized.
- Type of currency (KWD) is displayed incorrectly on Windows Store
- The New and Sale flags on the Store buttons do not properly disappear when clicking on the Store buttons.

## Changes from PTB

### Features

- The Artist
  - Extended power limitation zone around Hooked survivors to 10 meters (was 8 meters)
  - Swarmed Survivors who contact an idle Dire Crow will now have their Repel action reset (previously, it would damage the Survivor)

Dev Note: These changes were made to help reduce The Artist's power to shut down unhooking, and also to make her less oppressive during short loops by giving the survivor a counterplay option.

- Perks
  - Grim Embrace
    - Generator blocking increased to 30/35/40 seconds (was 20/25/30 seconds)
    - Obsession aura reveal increased to 5 seconds (was 4 seconds)
  - Hex: Pentimento
    - Perk effects now line up with the description text properly

Dev Note: On the PTB, Hex: Pentimento would trigger the healing speed debuff first and then the repair speed debuff second, while the description listed them in the opposite order. The perk description is now correct, and the repair speed debuff is first followed by the healing speed debuff second.

### Bug Fixes

- Fixed an issue where Burning Candle and Torture Pillar had the same bonus. The Candle is now 3 seconds and the Pillar is 6 seconds.
- Fixed an issue where Engineer's Fang's text was not correct.
- Fixed an issue that prevented the killer from damaging the generator in the killer tutorial.
- Fixed an issue that caused the first generator in the survivor tutorial to start at 0% progress.
- Fixed an issue that sometimes caused a crash when playing the tutorial bot match.
- Fixed an issue that caused previously purchased Stranger Things cosmetics to be missing.
- Fixed an issue that caused the graphics resolution setting to reset to 100% every time the player relaunches the client.
- Fixed an issue where it was possible for The Artist to spawn Crows during a cooldown when lagging
- Fixed an issue where incorrect text was displayed in the tooltips for The Artist and Jonah Vasquez
- Fixed an issue where a flying Bird of Torment would be unable to pass through some windows or over small obstacles
- Fixed an issue where the Darkest Ink add-on would not be applied when the crows are swarming a survivor
- Fixed an issue where a Bird of Torment would continue past a survivor who was just unhooked or in the process of being unhooked
- Fixed an issue where the Corrective Action perk incorrectly consumes tokens when an assisting survivor succeeds a skill check
- Fixed an issue where an audio reminder about firing a Bird of Torment is played even though it had been already fired
- Fixed an issue where the Matias' Baby Shoes Add-on would not properly reveal survivors
- Fixed an issue where crows would not be applied to a survivor exiting a locker, or reapplied near another infected survivor
- Fixed an issue where Birds of Torment could not be spawned in some more enclosed spaces
- Fixed an issue where Birds of Torment would not follow the slope along some inclined floors or stairs
- Fixed an issue where killer charms would be clipping through certain hooks
- Fixed an issue where Birds of Torment could not be consistently dissipated with a flashlight
- Fixed an issue where Corrective Action would incorrectly apply to failed skill checks on co-op interactions other than healing or repairing
- Fixed an issue where a survivor's recovery bar or self-healing bars would not turn red while slowed down by Hex Pentimento
- Fixed an issue with Hex Pentimento where the survivors would become cursed when the killer rekindles a totem
- Fixed an issue where a Hex Totem would have both the Boon and Hex flame effects when cleansed, rekindled and subsequently blessed
- Fixed an issue where equipping Grim Embrace would show blocked generators with a red aura
- Fixed an issue where the incorrect cooldown times are displayed when equipping the Festering Carrion add-on
- Fixed an issue when The Artist fires a Bird of Torment just before the time runs out makes it impossible to attack or interact with anything
- Fixed an issue when using the killer Add-on Severed Hands where a survivor with a swarm of crows can spread the crows to survivors lying dead on the ground
- Fixed an issue where Corrective Action incorrectly assisted with skill checks forced by perks or add-ons
- Fixed an issue where a survivor's recovery speed would double when in range of two Totems blessed with the Boon: Exponential perk
- Fixed an issue with The Artist where firing a Bird of Torment at a survivor in a locker would not cause that survivor to be revealed with Killer Instincts
- Fixed an issue where the Overcharge killer perk progress penalty is not applied when a survivor fails an Overcharge skill check
- Fixed a crash which could happen when the Starstruck cooldown is done
- Fixed a crash where The Artist's Garden of Rot add-on would crash at the start of a trial
- Fixed an issue where the Overcome perk would activate when becoming downed instead of just injured
- Fixed an issue where The Artist would not get stunned by a pallet when placing a Dire Crow
- Fixed an issue where the Severed Tongue add-on would not apply for the correct amount of time
- Fixed an issue with the Thick Tar addon where Survivors would not receive visual feedback that their Repel action was slowed
- Fixed an issue where survivors may not be hit by a Dire Crow that spawned overlapping with them
- Fixed an issue where damage done by The Artist's Dire Crow would not count towards the Chaser emblem
- Fixed an issue where Hex: Plaything affects only one survivor
- Fixed an issue with the Corrective Action perk not adding tokens for great skill checks after having used a toolbox with the Brand New Part add-on
- Fixed an issue where a Blast Mine detonation on a generator would not dispel a swarm of crows on a nearby survivor
- Fixed an issue where Hex: The Third Seal does not apply Blindness to survivors damaged by a Dire Crow
- Fixed an issue when The Artist launching a Bird of Torment does not consume a token of Play with your Food
- Fixed an issue where the Coup de Grace perk receives extra tokens when the last generator is repaired
- Fixed an issue where the "Out isn't an option" challenge can be completed by disconnecting from a trial
- Fixed an lighting issue with reflections, sky and colors.

<!-- nav -->
&larr; [5.3.2 | Bugfix Patch](303-5-3-2-bugfix-patch.md) · [Live](../../index.md#live) · [5.4.1 | Bugfix Patch](307-5-4-1-bugfix-patch.md) &rarr;
<!-- /nav -->
