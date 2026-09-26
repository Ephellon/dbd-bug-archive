---
title: "Developer Update | Tools of Torment PTB"
section: "Developer Updates"
article_id: 377
source: "https://forums.bhvr.com/dead-by-daylight/kb/articles/377-developer-update-tools-of-torment-ptb"
author: "Peanits"
published: "2023-02-23T14:58:45+00:00"
updated: "2023-02-23T14:58:45+00:00"
archived: "2026-09-26T19:29:06Z"
---

<!-- summary -->
## AI TL;DR

The Skull Merchant receives PTB polish: deploying drones no longer triggers the power cooldown, now 10 seconds for reactivations, and drones activate after 3 seconds. Unhackable time rises to 10 seconds, Lock-On lasts 60 seconds with slower decay, and the Killer gains Undetectable after 2 seconds in a zone. Claw Trap battery is extended to 45 seconds, scanner speed increased, and survivors no longer see reveal indicators. Survivors can now disable drones with traps, traps no longer force an unhackable state, and failed hacks cause immediate Lock-On. Perk updates: Eruption returns to 10 % total generator regression, THWACK! loses its timer, and Background Player activates on picking up another survivor with a 4-second sprint. These changes are slated for the March 7 Chapter release.
<!-- /summary -->

<!-- nav -->
&larr; [Developer Update | February 2023](375-developer-update-february-2023.md) · [Developer Updates](../index.md#developer-updates) · [Developer Update | Tools of Torment](380-developer-update-tools-of-torment.md) &rarr;
<!-- /nav -->

# Developer Update | Tools of Torment PTB

![Announcement.png](../images/0cce4b78fac37f6b-announcement.png)

It’s been about a week since the Tools of Torment Public Test Build (PTB) went live, and we’ve been busy combing through your feedback in the days since. Today, we’d like to share a large package of polish and balance adjustments which we’ve prepared for the Chapter’s release on March 7th.

As always, we want to give our appreciation for everyone who took the time to share their thoughts on this new content. Your feedback is invaluable in shaping the game!

Now, without further ado…

![SkullMerchant.png](../images/9d73995dfe59eb62-skullmerchant.png)

## The Skull Merchant

First up, deploying a drone to begin with. In the PTB, releasing a drone would put your power on cooldown for 12.5 seconds. This could feel a little limiting considering drones already cannot be placed within a certain range of one another. **We’ve decoupled deploying drones from the power’s cooldown.** The cooldown is now solely used for reactivating existing drones, and furthermore **has been lowered to 10 seconds (was 12.5)**.

Once a drone is deployed, it would take 4 seconds to become active. This gave Survivors a lot of time to react and move away before it began locking on. For the release, **we are lowering the initialization time of newly placed drones to 3 seconds**.

Speaking of newly placed drones, Survivors were previously capable of disabling a drone after only 5 seconds. This could allow bold and coordinated Survivors to disable a drone before it could have any meaningful effect. For release, **we’re increasing the unhackable window to 10 seconds**. Once the drone becomes hackable, it will remain active for an additional 20 seconds (for a total combined active time of 30 seconds, much like the PTB). The Killer can reactivate a drone at will using their scanner.

As the Killer, staying inside an active drone’s radius for 3 seconds would grant you the Undetectable Status Effect, allowing you to ambush Survivors. This could create some awkward moments where you’d be standing around waiting for the effect to kick in, so **we’re reducing this to 2 seconds**.

For Survivors, spending too long in an active zone can be dangerous. Active drones will Lock On to Survivors in their radius, making them Exposed. However, the short duration could make it difficult for the Killer to react unless they were already chasing a Survivor. We’ve made a few changes to the Lock On mechanic for release:

- The Lock On duration has been increased to 60 seconds (was 30).
- An incomplete Lock On will start to decay after 10 seconds of exiting an active zone (was 5).
- Entering an active zone while Locked On will reset your Lock On to 60 seconds and prevent it from decaying until you leave the zone.
- The Skull Merchant can now see Survivors’ Lock On progress in order to better plan their chases.

Besides Locking On, the drones are also a powerful tool for tracking Survivors. In the PTB, we found it to be a little difficult to fully take advantage of your Eyes in the Sky, so we’ve made some changes in that department as well:

- Claw Trap battery life has been increased to 45 seconds (was 25), allowing the Killer to track Survivors for longer. The “Overcharge” Add-on has been adjusted accordingly.
- Survivors will no longer receive an indicator when their location is revealed by The Skull Merchant’s scanner.
- The Skull Merchant will move faster when checking her radar (now 4.4m/s, was 4.0m/s).
- SFX have been updated to provide a clearer notification when a Survivor has been tracked.

With all this in mind, Survivors will want to be much more wary when they come face to face with The Skull Merchant. To ensure that this doesn’t make her too frustrating to play against, we’ve taken some additional considerations to accompany these changes- but be warned, there’s risk involved!

- Approaching a drone with a Claw Traps will no longer cause it to enter an unhackable state (preventing Survivors from interacting with it).
- Survivors with a Claw Trap can now disable drones – but keep in mind that entering the drone’s range will cause it to activate and recharge your traps’ battery!
- Survivors who fail a hack will now be immediately Locked On

Whether her drones are Locking On to Survivors or she’s tracking their every move, we hope you’ll find these changes make The Skull Merchant a much bigger threat when she releases March 7th.

![Perks.png](../images/e0b9bea7d13cb9ca-perks.png)

## Perks

Alongside tweaks to the new Killer, we’ve also mode some modifications to a few perks following feedback in the PTB.

**Eruption**

During the PTB, Eruption was changed to no longer make Survivors Incapacitated, and its regression was changed from total to *current* progress . While the removal of the Status Effect worked exactly as we’d hoped, the shift to current progress proved to be a little too far.

For the Chapter release, **Eruption’s regression will return to 10% of the generator’s *total* progress**.

**THWACK!**

Beyond being a fun name to say, THWACK! causes Survivors to scream and reveal their aura to the Killer. This perk requires the Killer to hook a Survivor in order to activate. To avoid any unneeded pressure for the Killer to seek out and break a pallet or wall, **we have removed the timer from this perk**. THWACK! will now remain active indefinitely upon hooking a Survivor and only deactivate upon use.

**Background Player**

This new perk for Renato Lyra caused him to break into a sprint upon unhooking a Survivor. Many pointed out that this left the unhooked Survivor alone at the hook, making them easy prey for the Killer. Background Player is receiving a rework in time for the release.

This perk **now activates when the Killer picks up another Survivor**, and **the duration of its sprint has been reduced to 4 seconds** (was 6).

How you choose to use this speed is up to you! Whether you’re trying to get into position for a save, get closer to the hook for a rescue, or simply to *get away as fast as possible-* we leave that to you to decide.

The Tools of Torment Chapter launches March 7th. Keep your eyes to the sky, but don’t forget to check if the Killer’s heading your way every once in a while. We’ll be watching. 👀

Until next time…

The Dead by Daylight team

<!-- nav -->
&larr; [Developer Update | February 2023](375-developer-update-february-2023.md) · [Developer Updates](../index.md#developer-updates) · [Developer Update | Tools of Torment](380-developer-update-tools-of-torment.md) &rarr;
<!-- /nav -->
