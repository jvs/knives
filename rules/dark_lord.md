# Dark Lord

**A cooperative card game for two players.**

The Dark Lord has returned, and only the League of Defenders can stop him!

---

## Components

- **Defender Deck** (~45-50 cards): Fighters, Items, Spells
- **Danger Deck** (~15-20 cards): Monsters, Events
- **City Cards** (6 total, use 3 per game)

---

## Setup

1. Separate the Danger cards from the Defender cards. Shuffle both decks.
2. Pick **3 City cards** and stack them face-up in a row. *(Easy mode: pick 4 cities.)*
3. Deal **5 Defender cards** to each player.
4. The youngest player is the **Leader** for the first battle. The other player is the **Backup**.

---

## Turn Structure

Each battle follows these phases:

### 1. Draw Phase

Each player draws Defender cards until their hand has 5 cards. *(If you have more than 5, discard down to 5 instead.)*

If the Defender deck runs out, shuffle the discard pile to form a new deck.

### 2. Prize Phase

Flip Defender cards from the top of the deck until there are **3 face-up prize cards** in the center.

### 3. Danger Phase

Draw **two Danger cards**: flip one face-up (**The Boss**) and leave one face-down (**The Shadow Boss**).

- If the face-up card is an **Event**, apply its effect immediately, then flip another card face-up. Repeat until you reveal a Monster — that's the Boss.
- The face-down card stays hidden until the Battle Phase.

### 4. Play Phase

Starting with the Leader, players take turns playing cards from their hand. On your turn you may play cards or pass.

**Rules for playing cards:**
- A player may play **at most one Fighter** per battle.
- Spells can be played freely (unless restricted by an event or monster effect).
- Items must be assigned to a Fighter when played. A Fighter can hold items up to its **Slots** stat.
- Squires must be assigned to a Fighter. A Fighter can have at most **one Squire**.
- Some cards cost **Aura** to play. Some cards grant Aura when played.

When both players pass consecutively, the Play Phase ends.

### 5. Reveal Phase

**Reveal the Shadow Boss.** Flip over the face-down Danger card.
- If it's an **Event**, apply its effect, then flip over another card from the Danger deck. Repeat until you reveal a Monster — that's the Shadow Boss.


### 6. Battle Phase

If a monster or event says "at the start of battle," resolve those effects now. Monsters win ties. For all other ties, the Leader decides the order of the effects.

**Combat.** All combatants (Fighters and Monsters) attack in **Speed order**, highest first.

- **Tie-breaking:** Monsters win ties. For all other ties, the Leader decides the order.
- **Monster targeting:** Monsters target the **Leader's** fighters first. If the Leader has no surviving fighters, monsters target the Backup's fighters.
- **Fighter targeting:** When a monster doesn't specify a target, the controlling player chooses which monster to attack.
- Subtract Attack from the target's Health. If Health drops to 0, the card is destroyed and discarded (along with its items and squire).
- Each combatant attacks **once** per battle.

### 7. Resolution

**If all Monsters are destroyed — Players win the battle!**

- Each player picks **one prize card** to add to their hand. The player with the most remaining Aura picks first. If tied, the Leader picks first.
- The third prize card is discarded.
- All played Spells are discarded.
- Fighters that survived remain on the field for the next battle. They **keep their current Health** (no healing) but **recover full Aura** at the start of the next battle. Items and Squires on surviving fighters also remain.
- The player who picked first becomes the **Leader** for the next battle. The other player becomes the **Backup**.

**If any Monster survives — Players lose the battle!**

- The top City card is **destroyed** (removed from the game). Apply any "when destroyed" effects.
- All played cards (fighters, items, squires, spells) are discarded.
- All monsters are discarded (even surviving ones).
- The Leader remains the Leader for the next battle.

---

## Game Over

- **Players lose** when their last City is destroyed.
- **Players win** when the Danger deck is empty at the start of the Danger Phase. (Finish the current battle first.)

---

## Conflicts and Decisions

Whenever the rules say "players pick" or multiple effects happen simultaneously, the **Leader decides**. The Leader can (and should) discuss options with the Backup, but has final say.

---

## Card Types

### Fighters

Fighters are played to the field and persist across battles until destroyed.

| Stat | Description |
|------|-------------|
| Attack | Damage dealt per attack |
| Aura | Magic points granted to the controlling player |
| Health | Damage absorbed before destruction |
| Slots | Number of items the fighter can hold |
| Speed | Determines attack order (higher = faster) |

**Squires.** Some Fighters can be played as a Squire instead. Assign the Squire to one of your Fighters. Play it sideways to indicate it's a Squire. A Squire is discarded when its Fighter is destroyed. Squires provide bonuses to their assigned Fighter.

### Items

Items are assigned to a Fighter when played and stay with that fighter until the fighter is destroyed or the item is otherwise removed. Items cannot be reassigned (unless a card effect says otherwise).

### Spells

Spells are one-time effects played during the Play Phase. They are discarded after the battle.

### Monsters

Monsters appear from the Danger deck. They have Attack, Health, and Speed. Some have special abilities that trigger at specific times. Some monsters target all fighters (noted in their description).

### Events

Events appear from the Danger deck. When drawn, apply their effect immediately, then draw another Danger card. Events modify the current battle's rules.

### Cities

Cities are laid out at the start of the game. Each city has:
- **Passive Bonus:** An effect that's active while the city is in play.
- **Destroyed Effect** *(optional)*: Something bad that happens when the city falls.

Cities are destroyed front to back (first city in the row is destroyed first).

---

## Trashing

Some card effects **trash** a card — removing it from the game entirely rather than discarding it. Trashed cards are never shuffled back into the Defender deck. This permanently thins the deck, for better or worse.

---

## Aura (Magic Points)

- Each fighter grants its Aura stat in magic points to the controlling player.
- Aura is tracked **per player** (not pooled).
- Some cards cost Aura to play; some cards grant Aura when played.
- At the start of each battle, each player's Aura resets to the total Aura of their surviving fighters.
- *(Optional rule: Each player starts each battle with 1 free Aura, even with no fighters.)*

---

## Example Cards

*These are rough sketches for playtesting. Stats are placeholders.*

### Example Spells

| Name | Cost | Effect |
|------|------|--------|
| Lock | 1 | Place sideways over one prize card. It can't be discarded by other effects until someone takes it. |
| Ew | 0 | Discard one prize card. Draw a new one to replace it. |
| Yoink | 1 | Take one prize card into your hand. Draw a new one to replace it. |
| Supermarket Sweep | 2 | Discard all prize cards. Draw three new ones. |
| Card Swap | 0 | Each player picks a card from their hand, places it face-down, then exchange. |
| Dismiss | 1 | Discard one fighter in play (and all its items and squire). |
| Item Swap | 0 | Take one item from each of two fighters and assign each to the other. |
| Brain Wave | 1 | Draw two Defender cards. |
| Tiny Rock | 0 | Deal 1 damage to any target (fighter or monster). |

### Example Fighters

*(Stats: Speed / Attack / Health / Aura / Slots)*

| Name | Stats | Squire Effect |
|------|-------|---------------|
| *TBD — build out during card design* | | |

### Example Squire Effects

- Boost one or more stats.
- If the fighter would be destroyed, destroy the squire instead.
- Make an extra attack with Speed 0.
- When the fighter is destroyed, return its items to your hand. Then discard down to 5.

### Example Items

| Name | Effect |
|------|--------|
| Omega Buster Sword | At the end of battle, destroy one target. |
| Turbo Thrusters | +5 Speed |
| Zombie Contract | When this fighter would be destroyed, destroy the Zombie Contract instead. Fighter becomes a zombie with 1 Health and 1 Aura. |
| Ogre Extract Stimulants | +5 Attack. If the fighter survives the battle, reduce its Health to 1. |
| Shield Generator | Subtract 1 from all attacks that target this fighter. |
| Big Boy Breakfast | +2 Health |
| Big Boy Pants | +1 Health, +1 Attack |

### Example Monsters

*(Stats: Speed / Attack / Health)*

| Name | Stats | Ability |
|------|-------|---------|
| Death | 0/0/1 | At the start of battle, destroy all fighters. |
| Witch | 3/2/4 | At the start of battle, draw another danger card and add it to the battle. |
| Dragon | 5/4/8 | At the end of battle, destroy all fighters. Discard remaining prize cards and draw three new ones. |
| Ogre | 2/3/6 | Players can't cast spells during this battle. |
| Goblin | 4/1/3 | At the start of battle, discard all items on all fighters. |
| Manticore | 6/3/5 | When this card is revealed, immediately destroy all fighters on the field. |
| Evil Wizard | 3/2/4 | At the start of battle, deal 1 damage to all fighters. |

### Example Events

| Name | Effect |
|------|--------|
| Fear | No squires may be summoned this battle. Destroy any squires on the field. |
| Lightning | At the start of battle, destroy the fighter with the lowest Aura. Leader breaks ties. |
| Shadow | Players must play cards face-down during the Play Phase. No discussing plays. Reveal all cards when the Play Phase ends. |
| Sabotage | At the start of battle, discard all items on all fighters. |
| Sniper | At the start of battle, destroy one fighter. Leader picks which one. |

---

## Design Notes & Open Questions

- **Card counts:** Need ~45-50 defender cards and ~15-20 danger cards for a base set. Exact numbers depend on playtesting.
- **Difficulty curve:** Early danger cards should be easier. Consider ordering the danger deck by difficulty tiers (shuffle within tiers) rather than fully random.
- **Utility cards:** Need more "weird" spells that skilled players can exploit — deck manipulation, information gathering (peek at shadow boss), repositioning effects.
- **Expansion ideas:** New city cards, new danger tiers, challenge modes (e.g., "no spells run," "solo mode," "three-player variant").
- **Balance targets:** A good game should feel winnable but tense. Aim for ~50-60% win rate on normal (3 cities) for experienced players.
