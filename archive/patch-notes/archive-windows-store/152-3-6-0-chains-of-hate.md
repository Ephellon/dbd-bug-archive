---
title: "3.6.0 | Chains of Hate"
section: "Archive: Windows Store"
article_id: 152
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/152-3-6-0-chains-of-hate"
author: "Peanits"
published: "2020-03-10T14:27:50+00:00"
updated: "2020-03-10T15:00:36+00:00"
archived: "2026-09-26T16:42:21Z"
---

<!-- summary -->
## AI TL;DR

New survivor Zarina Kassir, new killer The Deathslinger and the new map Dead Dawg Saloon - Grave of Glenvale arrive, alongside a high-ping HUD icon that warns at 150 ms (white) and 300 ms (red).

Balance updates overhaul hook sabotage, toolbox repair speed, and the Doctor’s madness system - removing passive decay, simplifying tiers, and reworking affliction add-ons. The Plague, Trapper and other killers receive minor tweaks, and survivor perks Saboteur and Ace in the Hole are adjusted. The patch also bundles extensive bug fixes covering emblem progress, custom-game flow, killer animations, map collisions, cosmetics clipping, audio mismatches and language display issues.
<!-- /summary -->

<!-- nav -->
&larr; [3.5.2 | Hotfix](120-3-5-2-hotfix.md) · [Archive: Windows Store](../../index.md#archive-windows-store) · [3.6.1 | Hotfix](168-3-6-1-hotfix.md) &rarr;
<!-- /nav -->

# 3.6.0 | Chains of Hate

## Features & Content

- Content - Added a new Survivor (Zarina Kassir)
- Content - Added a new Killer (The Deathslinger)
- Content - Added a new map (Dead Dawg Saloon - Grave of Glenvale)
- Content - Added a high-ping indicator to the HUD, displayed when the local ping to the server is above a certain threshold (white icon for 150ms, red icon for 300ms).

## Balance

**Hooks and Sabotage**

- Removed skill checks for Hook sabotage.
- Survivors will no longer be able to sabotage a Bear Trap with a Toolbox or the Perk Saboteur.
- Killers may not hook a Survivor on a hook that is currently being sabotaged.
- Dropping a Survivor now increases the Wiggle progression by 25% (down from 33%).

**Toolboxes, items and add-ons**

- Survivors will no longer be able to sabotage a Bear Trap with a Toolbox.
- Toolboxes now repair fewer charges of a generator, but have a greater speed boost.
- Doubled the chance to trigger a skill check when repairing a Generator with a Toolbox.
- When a Survivor item reaches zero charges, they may keep it. If they escape with that item, it will be automatically refilled for the next trial.
- Dropped items with zero charge behave the same way as items with charges; they can be picked up again later.
- When a Survivor escapes a trial with an item, that item loses its addons.
- Removed the possibility for all Splinter Offerings to spawn in the Bloodweb.
- Disabled all Splinter Offerings.

**Killer Changes**

- The Plague now starts with one Corrupted Fountain.
- The Trapper's Bear Traps can no longer be sabotaged.
- The Trapper's Bear Traps can now be reset without needing to pick them up first.

**The Doctor Changes**

With the update The Doctor received in the last mid-chapter, there are now two ways to inflict Madness: Shock Therapy, and Static Blast. To make it clearer what is required to increase a Survivor’s Madness level, we are making the following changes:

- Madness no longer decays passively over time.
- Shock Therapy will add half of a Madness level to any Survivors hit.
- Static Blast will add a full Madness level to any Survivors hit.
- Reverse skill checks now happen 2/3 of the time an insane skill check is triggered by default.

In numbers:

Previously, the thresholds for madness tier 1, 2 and 3 were **5**, **55**, and **105** points respectively.

Shock therapy granted **30** points of madness and static blast granted **50**.

While outside the terror radius, madness would decay by **0.5** points per second.

These thresholds were based on how much passive madness gain the Doctor used to have. Without that mechanic, the madness thresholds can be simplified.

The new tiers for madness 1, 2 and 3 are **1**, **2** and **3** points respectively.

Shock therapy grants **0.5** points of madness and static blast grants **1**

There is no passive madness decay. The only way to reduce madness is to Snap Out Of It.

Previously, the "Order" add-ons increased the amount of madness inflicted by Static blast. They now reduce Static Blast's cooldown instead.

Previously, the "Discipline" add-ons increased the amount of madness inflicted by Shock Therapy. They now reduce the detonation delay of Shock Therapy instead.

Further add-on changes:

The Doctor's madness can be customized by using his "Affliction" add-ons: Order, Discipline, Calm, Restraint and Obedience. Add-ons of the same type granted similar debuffs, but each one varied slightly in magnitude or madness threshold. The end result was that it was often unclear which add-on did what, and the lower rarity add-ons often seemed very unappealing in comparison to the higher rarity ones.

The "Afflictions" have now been standardized to be the same across all rarities. Only the passive bonus is different.

**Order (Illusionary Pallets)**

- Order - Class 1/2/3: Reduces the cooldown of Static Blast by 2/4/6 seconds

The Affliction of Order used to vary in terms of what madness tier was required to show pallets, and how far away from the doctor pallets could spawn. These variables are now the same across Order - Class 1, Order - Class 2 and Order - Carter's Notes

Survivors with Madness suffer from the **Affliction of Order**:

- Broken pallets may appear to be replaced with Illusionary Pallets that persist until approached.
- A new Illusionary Pallet is generated at the location of a random broken pallet very 20 seconds.
- The Doctor shares in his patients' Madness in order to read the auras of Illusionary Pallets.

**Discipline (Illusionary Killer Stain):**

- Discipline - Class 1/2/3: Now reduces the detonation delay of Shock Therapy by -0.1 seconds, -0.2 seconds and -0.3 seconds.

The Affliction of Discipline used to vary in terms of how long the effect would stay active and whether they required a chase to activate. These variables are now the same across Discipline - Class 2, Discipline - Class 3 and Discipline - Carter's Notes

Survivors with Madness suffer from the **Affliction of Discipline**:

- Madness II: While in a chase, survivors perceive an Illusionary Red Stain and Terror Radius as though The Doctor were right behind them. This effect persists for 6 seconds after the chase ends.
- Madness III: Illusionary Red Stain and Terror Radius are constantly active.
- The Doctor shares in his patients' Madness in order to see the Illusionary Red Stain.

**Restraint (Illusionary Doctor):**

- Restraint - Class 1,2,3: Now reveals Survivors' auras for 1/2/3 seconds.

The Affliction of Restraint used to vary in terms of how much extra duration would be granted to illusionary doctor hallucinations. These variables are now the same across Restraint - Class 2, Restraint - Class 3 and Restraint - Carter's Notes.

The passive bonuses of the restraint add-ons have not been changed.

Survivors with Madness suffer from the **Affliction of Restraint**:

- Increased Illusionary Doctor duration to 8 seconds (These hallucinations normally last 1 second)
- The Doctor shares in his patients' Madness in order to read the Auras of Illusionary Doctors at any level. (This effect is normally only active in madness 3)

**Calm (Illusionary Terror Radius)**

- Calm - Class 1,2,3: Terror radius increased/decreased by 4/6/8 meters

Additive modifiers for Terror Radius are clearer and the result of stacking multiple modifiers is simpler to calculate. This is a slight increase in the effect for Class 1 and 2, and Carter's Notes are equivalent (25% of 32 is 8)

The Affliction of Calm used to vary in terms of what madness tier was required to activate it, how long it stayed active, and how long it took between activations. These variables are now the same across Calm - Class 1, Calm - Class 2 and Calm - Carter's Notes

Survivors with Madness suffer from the **Affliction of Calm**:

- Madness II: Intermittently causes survivors to hear a distant illusionary Heartbeat (10-15 seconds active, 30-45 seconds inactive)
- Madness III: Constantly causes survivors to hear a distant illusionary Heartbeat

**Obedience (Reverse Skill Checks)**

Obedience broke the pattern of affliction add-ons and has been removed. Reverse skill checks have been integrated into the Doctor's base ability.

When afflicted by a Madness Skill Check, there is a 33% chance of an off-center skill check, a 33% chance of a reverse skill check, and a 33% chance of a reverse off-center skill check. This is baseline and requires no add-ons.

Scrapped Tape, which was previously removed, has returned to take Obedience - Class III's place.

**Iridescent King**

Previously, this add-on would inflict a random affliction on a survivor every time they were shocked. These afflictions would stack, until a survivor had all 5 afflictions after 5 shocks. However, this was mostly unnecessary, as these afflictions still had the same madness thresholds for activation. In light of the changes to the afflictions, Iridescent King has been simplified and the need to shock survivors to inflict afflictions has been removed:

Survivors with Madness suffer from the Afflictions of **Calm**, **Discipline**, **Order**, and **Restraint**:

- Intermittently causes survivors to hear a distant illusionary Heartbeat.
- While in a chase, survivors perceive an Illusionary Red Stain and Terror Radius as though The Doctor were right behind them. This effect persists for 6 seconds after the chase ends and is constantly active in Madness III.
- Broken pallets may appear to be replaced with Illusionary Pallets that persist until approached. A new Ilusionary Pallet is generated at the location of a random broken pallet every 20 seconds.
- Increases Illusionary Doctor duration to 8 seconds and grants the ability to read their auras at any level of madness.

**Electrodes:**

The electrode add-ons increased shock therapy range by a percentage at the cost of a small penalty to shock therapy charge speed. This has been changed to grant extra range (in meters) with no penalty.

(The base range of Shock Therapy is 10 meters)

Mouldy Electrode: Increases the range of Shock Therapy by 2 meters (previously +15% range, -5% charge speed)

Polished Electrode: Increases the range of Shock Therapy by 3 meters (previously +25% range, -10% charge speed)

High-Stimulus Electrode: Increases the range of Shock Therapy 4 meters (previously +35% range, -15% charge speed)

Interview Tape: Range increased from 20 meters to 24 meters

**Survivor Perks**

- Saboteur: See Hook auras in a 56 meters radius from the pickup spot if a Survivor is being carried. Sabotaging a Hook without a toolbox takes 2.5 seconds. The Sabotage action has a 60 seconds cooldown.
- The Perk Ace in the Hole now adds the ability to keep the addons when escaping a trial with an item.

**Killer Perks**

- Hangman's Trick: Reduce the Perk range to 2, 4 and 6 meters.

## Bug Fixes

- Fixed an issue that would notify the Survivors of the Hex: No One Escapes Death when certain Killers use their power while the exit gates are powered.
- Fixed an issue that caused Survivors to be hit by projectiles that visually appear to pass over their head while performing various interaction's animations.
- Fixed an issue that wouldn't award Malicious and Devout emblem progress when a Survivor disconnects.
- Fixed an issue that caused the Chaser emblem to not acquire any points when catching a Survivor in a Trapper trap (in or out of chase).
- Fixed an issue that wouldn't grant a Coop Action score event when mending or sealing a Demogorgon's portal with another Survivor.
- Fixed an issue that caused the Nurse's Spasmodic breath to infinitely increases base movement speed if the killer lunges as the timer runs out.
- Fixed an issue that would sometimes fail to award a protection hit score event to a Survivor when another healthy Survivor is near the injured Survivor.
- Fixed an issue that caused a Spectator to be unable to switch Role if at least one user is ready in a Custom Game Lobby.
- Fixed an issue that prevented starting a match in Custom Game when there is ~~having~~ a spectator.
- Fixed an issue that caused the Doctor to have his view partially blocked by the Survivor's body for a brief moment when performing an attack while carrying a Survivor.
- Fixed the Doctor view blocked by the Survivor's body when performing an attack while carrying a Survivor.
- Fixed an issue that caused players to be unable to select the 'Ready' option when returning to the Custom Game Lobby.
- Fixed the Blood drops from failing a healing skillcheck while asleep pass through certain ground tiles and any elevated tile.
- Fixed an issue that caused the Blood VFX to be missing from the screen when a survivor is affected by Deep Wounds from Borrowed time.
- Fixed an issue that caused the Prompt text to be missing upon leveling up in the Bloodweb Menu.
- Fixed an issue that caused the Killer to jitter erraticaly when moving the cursor after interrupting a Survivor vaulting over a pallet.
- Fixed an issue that caused other Survivors to have the Ready button grayed out in a Custom Game Lobby when a Survivor comes back to the Lobby after having closed the application during the Loading Screen.
- Fixed an issue that could cause Trials to start in public matches with an incomplete Lobby.
- Fixed an issue that caused The Mad House achievement to fail to trigger when 4 survivors are brought to Madness tier 3.
- Fixed an issue that caused various killers animations to be corrupted or misalinged when performing a Mori.
- Fixed an issue that allowed Killers to break a pallet while a survivor is resetting the pallet from the same side.
- Fixed an issue that caused players to be unable to click the unlock tiers button in The Rift if the current tier reward unlock overlaps with the button.
- Fixed an issue that caused Survivors to be unable to gain token with the perk Autodidact.
- Fixed an issue that caused parts of the Oni's sound effect when absorbing blood orbs to loop when stunned after striking a Survivor.
- Fixed an issue that briefly caused the Shape's unique music to trigger upon exiting the Archives to the Main Menu.
- Fixed an issue that caused the Boil Over Perk to not immediately hide hook auras when the pickup animation begins.
- Fixed an issue that caused Hex: Huntress Lullaby to fail to apply to Brand New Part installations when 5 tokens are earned.
- Fixed an issue that caused the extra points awarded for healing a survivor with No One Left Behind to not properly show in the score event.
- Fixed the Hag's post-wiggle animation when a Survivor wiggles out.
- Fixed an issue that caused users to be unable to access the Auric Cell Packs menu in the Store.

**Map Specific**

- Treatment Theatre: Fixed an issue in Lery's long shower room that caused a hatch to not allow Survivors to open it with a Key
- Treatment Theatre: Fixed an issue that displayed a floating book next to a Desk.
- Treatment Theatre: Fixed missing collision issues on various assets and ceiling.
- Fixed the SFX on some tall grass when walking on them inside The Backwater Swamp theme.
- Autohaven Wreckers: Fixed an issue that allowed Survivors to use Dead Hard to get onto tires near a crane
- Gas Heaven: Fixed an issue that allowed survivors to go through the ground near the gas pumps.
- Gas Heaven: Fixed an issue that displayed a seam near the Gas Station.
- Disturbed Ward: Fixed an issue that caused the LOD to be seen updating on the second floor of the Asylum.
- Mount Ormond Resort: Fixed a collision issue that blocked the movement of both Survivors and Killer near a broken lift.
- Mount Ormond Resort: Fixed an issue that caused Killers to get stuck on a vault point in Mount Ormond Resort after increasing their vault speed.
- Mount Ormond Resort: Fixed an issue that caused Survivors and Killers to be unable to move freely when walking at a specific corner exterior of the main building.
- Mount Ormond Resort: Fixed the collision on the railing on the second floor of the main building.
- The Thompson House: Fixed an issue that caused A survivor to get stuck when collecting the item in a chest that spawns close to the combine harvester.
- Sanctum of Wrath: Fixed an issue that caused Killers to be unable to chase Survivors between Buddha statues and a rock.
- Fractured Cowshed: Fixed an issue that displayed a seam on the ground when walking around the map.
- Mother's Dwelling: Fixed a Lighting issue that caused a wall to appear completely shadowed and then brightens when approached.
- Fixed the collision on several hill tiles that could cause the Survivor or the Killer to bounce up and down repeatedly when near a rock formation.
- Yamaoka Estate: Fixed a texture at any exit gate to disappear as the Survivor or the Killer walks away.
- Yamaoka Estate: Fixed a missing collision at the bottom of the stairs of the Family Residence.
- Coldwind Farm: Fixed an issue that could cause a Survivor to get stuck when collecting the item in a chest that spawns close to the combine harvester.

**Cosmetics**

- Spirit: Added a texture to the Spirit's bandages on her left leg on the Cursed Silk Kimono from the Tattered Tradition Outfit.
- Fixed the Doctor’s “Metal Therapy Bat” texture
- Fixed a display issue when viewing The Huntress wearing the Hunting Hitatare Torso.
- Fixed an issue that could cause a crash when viewing a Huntress wearing the Winter Hearth Torso.
- Fixed an issue that caused various Huntress Masks to clip through her neck.
- Fixed an issue that displayed distorted legs when viewing the Doctor's Ladykiller Frock Coat from a distance.
- Fixed an issue that caused the hanging piece of cloth on the Doctor's Straight Jacket Torso to be clipping through his body.
- Fixed a clipping issue when viewing all of Nea's shirt models.
- Fixed a graphic issue when viewing The Clown’s “Mr. Puddles’ Disembodied Head” on the tally screen.
- Fixed a graphic issue when viewing the Trapper's Neptune's Failure Torso on the tally screen.
- Fixed an issue that caused the Wraith's Glowing Vigil head customization to clip through the Evening Wear Body customization.
- Fixed multiple clipping and lighting issues with David King's Hard Headlight Torso customization.

**Audio & Loc**

- Fixed an issue that caused the wrong language to be displayed when viewing the result screen in Brazilian Portuguese after a match.
- Fixed an issue that caused a superfluous grunt when a survivor lands after falling from any height.
- Fixed an issue that caused the font color and size of the Head On Perk to be different than usual when viewed with the game language set to Spanish.
- Polished The Trapper's Mori SFX.
- Polished The Hag's Mori SFX.
- Fixed an issue that caused Survivors carrying a toolbox when injured while running to make the Survivors' footsteps play more often.
- The Underground Complex: Fixed some floors that would trigger a wet footprint sound.
- Father Campbell's Chapel: Polished the audio when inside the chapel.

<!-- nav -->
&larr; [3.5.2 | Hotfix](120-3-5-2-hotfix.md) · [Archive: Windows Store](../../index.md#archive-windows-store) · [3.6.1 | Hotfix](168-3-6-1-hotfix.md) &rarr;
<!-- /nav -->
