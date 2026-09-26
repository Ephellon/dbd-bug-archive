---
title: "4.2.0 | Descend Beyond"
section: "Archive: Steam"
article_id: 228
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/228-4-2-0-descend-beyond"
author: "Peanits"
published: "2020-09-08T14:25:32+00:00"
updated: "2020-09-08T15:09:59+00:00"
archived: "2026-09-26T17:09:41Z"
---

<!-- summary -->
## AI TL;DR

The Blight joins the roster as a new killer and Felix Richter arrives as a new survivor in the Descend Beyond chapter, accompanied by five new offerings that affect realm, basement and hatch spawns. The patch also refreshes generators, pallets, lockers and chests, adds breakable walls to Springwood and Yamaoka Estate, and corrects flashlight aiming.

A broad set of fixes addresses lingering issues for many killers (Deathslinger stun, Hillbilly speed, Legion masks, Oni blood-fury, Plague arc, Shape stance, Trapper aura), survivor navigation glitches, perk interaction errors, graphics crashes, rank-update problems and PTB-specific collision and animation bugs for the Blight and other characters.
<!-- /summary -->

<!-- nav -->
&larr; [4.1.3 | Bugfix Patch](227-4-1-3-bugfix-patch.md) · [Archive: Steam](../../index.md#archive-steam) · [4.2.1 | Bugfix Patch](233-4-2-1-bugfix-patch.md) &rarr;
<!-- /nav -->

# 4.2.0 | Descend Beyond

![420UpdateBanner.png](../../images/2e62bbf2f4587595-420updatebanner.png)

## New Chapter

Unleash The Blight, an alchemist consumed by his research. Ambition brought him to the Entity's realm but his hunger for power destroyed him. Mutated and mad, his power, Blighted Corruption, provides him with unnatural abilities to quickly pursue and ambush Survivors.

Plan your escape with Felix Richter, a successful architect who was torn away from his lavish lifestyle. Resourceful and bold, he has clever methods to stand against the oncoming evil and plan out the one thing that matters to him most—returning home.

- Added a new Killer - **The Blight.**
- Added a new Survivor - **Felix Richter.**
- Added a new Rare Offering for Killers and Survivors - **Sacrificial Ward** - cancels other offerings that would send you to a specific realm.
- Added a new Common Offering for Killers and Survivors - **Bloodied Blueprint** - reveals the aura of basement hooks to you for 20 seconds at the start of the trial. If the map has a Killer Shack, this offering increases the chance that the basement will spawn below it.
- Added a new Common Offering for Killers and Survivors - **Torn Blueprint** - reveals the aura of basement hooks to you for 20 seconds at the start of the trial. If the map has a main building, this offering increases the chance that the basement will spawn below it.
- Added a new Common Offering for Killers and Survivors - **Annotated Blueprint** - If the map has a Killer Shack, this offering increases the chance that the Hatch will spawn within it.
- Added a new Common Offering for Killers and Survivors - **Vigo’s Blueprint** - If the map has a main building, this offering increases the chance that the Hatch will spawn within it.

![PatchNotesDivider.png](../../images/d693987990e49c09-patchnotesdivider-281-29.png)

## Features & Content

Many in-game objects in Dead By Daylight haven't been changed significantly since the game's launch. As part of our ongoing effort to enhance the game's visuals, many of these objects got visual updates in this patch to bring them closer to our long-term vision for the appearance of the game. Some realms also got visual updates, with more coming later in future patches.

- Visual updates of several common in-game objects:
  - Visual update of the **Generators,** including changes to models, animations and VFX. The Survivor repairing animations and VFX were also updated.
  - Visual update of the **Pallets**, including models and VFX.
  - Visual update of the **Lockers.**
  - Visual update of the **Chests**, including the model and changes to the Survivor's interaction. This Survivor interaction has been updated
- Visual updates to some maps, including additions of breakable walls:
  - **Springwood** - Updated Badham Preschool Maps I - V
  - **Yamaoka Estate** - Updated Family Residence and Sanctum of Wrath
- Update aiming when using the flashlight. Up to 4.1.0, the flashlight would aim up and to the right of the center of the screen. In 4.1.0, the aiming animation was updated, which caused the flashlight to aim more towards right of center. Now, the aim should be squarely in the center.

![PatchNotesDivider.png](../../images/d693987990e49c09-patchnotesdivider-281-29.png)

## Bug Fixes

### Killer

- Fixed an issue that caused survivors not to be stunned when shot by the Deathslinger.
- Fixed an issue that caused the Hillbilly's carry and lunge speed to be reduced when equipped with the Tuned Carburetor add on.
- Fixed an issue that caused all Legion characters to use Julie's animation when the 'Empty Stare' mask was equipped.
- Fixed an issue that may cause the Oni to lose the ability to enter Blood Fury.
- Fixed an issue that caused the Oni's blood orbs to sometimes flicker in and out of visibility.
- Fixed an issue that caused the Plague's Vile Purge to arc higher than previously.
- Fixed an issue that cause the Shape not to change stances while in Tier 3 Evil Within.
- Fixed an issue that caused the Trapper's bear trap aura not to appear during the tutorial.

### Survivor

- Fixed an issue that caused survivors to be stuck at the bottom of the Hill on various maps.
- Fixed several issues that may cause survivors to be misaligned during Moris.

### Perk

- Fixed an issue that caused a regressing generator not to turn red once reaching 0 progress when using the Surveillance perk.
- Fixed an issue that caused the "Pull Down" prompt to be replaced for Survivors standing next to a pallet while injured and with the Self-Care perk equipped.
- Fixed an issue that caused survivors to see the auras of breakable walls when equipped with the Windows of Opportunity perk and suffering from the Blind effect.

### Other

- Fixed a crash that would sometimes happen when selecting the Low or Medium Graphics Quality from Medium and above.
- Reduced rank update errors.
- HTML markup in player names during social notifications (toast invites) are now handled properly.

![PatchNotesDivider.png](../../images/d693987990e49c09-patchnotesdivider-281-29.png)

## Changes From PTB

Many players on PTB noticed the Blight would unintentionally collide with objects while rushing, or fail to hit objects they would expect to collide with. This version of the character reduces that unwanted behavior, making the Blight's power more reliable and effective. His add-ons were also adjusted to add more diversity.

### The Blight

- Fixed an issue where the Blight would play two cooldown animations after a dash attack. The weapon wipe animation on a successful dash attack and the miss animation after a missed dash attack have both been removed and replaced with the cooldown injection animation. This also fixes various incorrect behaviour during the 'double cooldown' such as being able to pick up survivors or attack without playing an attack animation.
- Decreased the radius of the velocity-based rush collision detector and added a secondary collision detector for objects that are both at very close range and directly in the center of view.
- Increased the dash attack's initial speed from 6.9 m/s to 9.2 m/s.
- Increased the base turn rate during rush.
- Slightly reduced the initial speed boost at the beginning of a lethal rush.
- Dash attacks will now continue even if the attack input is released.
- Updated the Blight's height from "Tall" to "Average" and difficulty from "Intermediate" to "Hard".
- Reworked the target projection from the add-on "Chipped Monocle". It was previously projecting in the direction the player was facing based on their current speed. However, due to the sliding movement while rushing, it has been updated to project a collision the direction the player is currently moving. A special case was added for the slam phase to project a collision while not moving at full dash speed. The end result should be that the Chipped Monocle makes it clearer how the Blight's trajectory changes while rushing, as well as being a more accurate estimate of the collision location.
- Complete add-on pass - 16/20 add-ons updated. An updated list of add-ons is included below.

<details>
<summary>Spoiler</summary>

Some other bonuses (such as "add one additional rush token") were replaced with more interesting effects. With these changes, we hope to support a wide variety of viable and interesting play styles.

A general pass was done on the add-ons to increase the diversity of effects and possible builds with the character. There were previously 4 add-ons that could affect rush speed and 3 for affecting rush turn rate; these have been reduced to 2 each to make room for more unique add-ons.

**Chipped Monocle (Common)**

Displays the target location of a slam

**Compound Seven (Common)**

Automatically face the nearest survivor within 16 meters after a slam

**Foxglove (Common)**

Reduces the recovery time after rushing by 0.25 seconds

**Placebo Tablet (Common)**

Reduces movement speed while rushing by 15%

Increases Bloodpoints from rush score events by 100%

**Canker Thorn (Uncommon)**

Reduces recovery time after rushing by 0.5 seconds

**Shredded Notes (Uncommon)**

Decreases the time required to recharge a rush token by 0.33 seconds

Decreases the maximum number of rush tokens by 1

**Blighted Rat (Uncommon)**

Increases rush speed by 4% for each consecutive rush

**Plague Bile (Uncommon)**

Increases turn rate while rushing by 10%

**Pustula Dust (Uncommon)**

Increases the duration of the slam by 0.75 seconds

**Compound Twenty-One (Rare)**

When initiating a slam, reveals the auras of survivors within 16 meters of the collision location for 6 seconds

**Umbra Salts (Rare)**

Increases turn rate while rushing by 15%

**Rose Tonic (Rare)**

Increases the duration of the slam by 1 second

Unchanged from PTB

**Blighted Crow (Rare)**

Increases rush speed by 6% for each consecutive rush

**Adrenaline Vial (Rare)**

Reduces turn rate while rushing by 90%

Decreases the time required to recharge a rush token by 0.66 seconds

Increases the maximum look angle while rushing by 50%

Increases the maximum number of rush tokens by 2

**Summoning Stone (Very Rare)**

Hitting a survivor with a lethal rush will call upon the Entity to block pallets within 12 meters of your location for 6 seconds

Unchanged from PTB

**Alchemist's Ring (Very Rare)**

Hitting a survivor with a lethal rush will instantly recharge all rush tokens

**Soul Chemical (Very Rare)**

See the auras of survivors within 8 meters while rushing

**Vigo's Journal (Very Rare)**

Gain the Undetectable status effect while rushing

Unchanged from PTB

**Compound Thirty-Three (Ultra Rare)**

Any survivors within 16 meters of a slam will suffer from the Hindered status effect for 3 seconds

Slamming pallets or breakable walls will destroy them and stun the Blight for 1.5 seconds

**Iridescent Blight Tag (Ultra Rare)**

Upon using all rush tokens, hitting a survivor with a lethal rush attack will put them in the dying state

Unchanged from PTB

</details>

![PatchNotesDividerSmolWhite.png](../../images/3e51648d555c8a4c-patchnotesdividersmolwhite.png)

### PTB Bug Fixes

- Fixed an issue that caused The Oni to enter an incorrect visual state after being stunned during the Yamaoka's Wrath animations.
- Fixed an issue that caused the Plague to not slow down after using Vile Purge.
- Fixed an issue that caused the Damage prompt to be missing from generators after cleansing Hex: Ruin multiple times with the Hex: Undying perk equipped.
- Fixed an issue that caused the Doctor's illusionary pallets not to be affected by the Hex: Blood Favor perk.
- Fixed an issue that might cause the Nightmare's dream pallets not to be affected by the Hex: Blood Favor perk.
- Fixed an issue that caused frame rates to drop when a generator is completed.
- Reduced the number of occurrences of Save Game Error 112.
- Make the errors more explicit when the game fails to grant/withdraw Bloodpoints.
- Fixed an issue that caused the Bloodweb to be usable without consuming Bloodpoints.

<!-- nav -->
&larr; [4.1.3 | Bugfix Patch](227-4-1-3-bugfix-patch.md) · [Archive: Steam](../../index.md#archive-steam) · [4.2.1 | Bugfix Patch](233-4-2-1-bugfix-patch.md) &rarr;
<!-- /nav -->
