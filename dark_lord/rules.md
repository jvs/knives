# Dark Lord

A trick-taking card game for 3 players.

---

## Overview

Three players compete across multiple hands. Each hand, one player becomes **the Dark Lord** through an auction, taking control of a face-up **Lackey hand** and playing two hands against the other two players (**the Heroes**). The first player to **250 points** wins.

---

## Components

### The Deck (44 cards)

**Traditional Suits (36 cards)** — Four suits of 9 cards each:

| Suit | Prank Card | Number Cards | Face Cards |
|------|-----------|--------------|------------|
| Spades | Snitch | 2, 3, 4, 5 | Jack, Queen, King, Ace |
| Diamonds | Devil | 2, 3, 4, 5 | Jack, Queen, King, Ace |
| Hearts | Hound | 2, 3, 4, 5 | Jack, Queen, King, Ace |
| Clubs | Cat | 2, 3, 4, 5 | Jack, Queen, King, Ace |

Rank order within a suit (low to high): Prank, 2, 3, 4, 5, Jack, Queen, King, Ace.

**Threats (4 cards)** — The greater trump suit. Threats always beat any card from a traditional suit, including lesser trump.

| Card | Rank | ATK |
|------|------|-----|
| Beast | 6 | 666K |
| Ogre | 7 | 720K |
| Dragon | 8 | 850K |
| Witch | 9 | 999K |

(The ATK values are not used. They have no effect on gameplay.)

**Spells (4 cards)** — Spell cards may be played on any trick and always count as following suit.

| Spell | Effect |
|------|--------|
| **Angel of Death** | There is no trump for this trick (greater or lesser). Highest card of the led suit wins. (Resolves during trick resolution.) |
| **Evil Twin** | Play as a copy of another card already in the trick. Loses ties. Copies any special effects. |
| **Nightmare Zone** | After this trick resolves, move the cards from this trick to the shadows. The trick does not count for either side during scoring. |
| **Tome of Tricks** | This trick counts as two tricks during scoring. Keep this card separate from the trick as a reminder. |

---

## Setup

1. Shuffle the deck.
2. Deal **10 cards** to each player.
3. Deal **10 cards face-up** to the center of the table. This is the **Lackey hand** (or just "the Lackey").
4. Deal **4 cards face-down** to the side. These are the **shadows** — out of play and not revealed until the hand is over.

All players may examine the Lackey before bidding begins.

---

## The Auction

The player to the dealer's left bids first and **must bid at least 1**. Bidding proceeds clockwise.

Each bid is a **number of tricks** — the minimum the Dark Lord commits to winning. Each bid must be higher than the previous bid. A player may **pass** instead of bidding. Once you pass, you are done with bidding for this hand.

When two players have passed, the remaining bidder becomes **the Dark Lord**.

### Dark Lord Assumption

1. The Lackey is placed across from the Dark Lord.
2. The Dark Lord names a **lesser trump suit** (one of the four traditional suits) or declares **"Threats Only"** (no lesser trump; only Threats are trump).
3. The Dark Lord leads the first trick.

---

## Trump Hierarchy

Cards from strongest to weakest:

1. **Threats** (greater trump) — Witch > Dragon > Ogre > Beast
2. **Lesser trump** (the suit named by the Dark Lord) — normal rank order within the suit
3. **Led suit** — the suit of the first card played in a trick
4. **Off-suit cards** — cannot win a trick

Threats are always the top trump. Lesser trump beats non-trump suits. If no Threat or trump is played, the highest card of the led suit wins.

If "Threats Only" was declared, there is no lesser trump — only Threats outrank the led suit.

---

## Playing a Hand

The Dark Lord controls two hands: their own hand (hidden, like any player's) and the Lackey (face-up, visible to all). These are separate hands — each follows suit independently, and each plays in its own seat in the turn order.

The Dark Lord leads the first trick. After that, the winner of each trick leads the next. If the Lackey wins a trick, the Lackey leads the next trick (with the Dark Lord choosing which card to play from it). Play proceeds clockwise. On the Lackey's turn, the Dark Lord plays a card from the Lackey.

### Following Suit

- Players must follow the led suit if able.
- If a player cannot follow suit, they may play any card.
- The Dark Lord's own hand and the Lackey follow suit **independently**. Each must follow the led suit using only the cards available in that hand.
- Spells may be played in any trick and always count as following suit.

### Leading with Special Cards

- **Leading with a Threat:** Other players must play a Threat if able. If they have no Threats, they may play any card. *(Threats are their own suit.)*
- **Leading with a Spell:** The player names a suit. The spell is treated as a zero of that named suit. Other players must follow the named suit if able.

---

## Prank Cards

Each suit's Prank card has a unique ability. Prank abilities take effect **immediately when played** (before the trick resolves), except where noted.

Prank cards are the **lowest-ranked card** in their suit — playing one means you're almost certainly losing the trick. The ability is the trade-off.

| Prank | Suit | Ability |
|-------|------|---------|
| **Snitch** | Spades | Name a specific card (e.g., "Witch" or "King of Hearts"). If any player holds that card, they must reveal it to all players. The card stays in their hand. |
| **Devil** | Diamonds | Choose a target player (or the Lackey). Each of you selects a card from your hand and exchanges them face-down. Both players add the received card to their hand immediately. If the target is the Lackey, the Dark Lord chooses which Lackey card to swap, and both cards are revealed (since the Lackey is face-up). |
| **Hound** | Hearts | Choose a player. That player chooses one card from their hand to reveal to all players (keeping it in hand). |
| **Cat** | Clubs | You lead the next trick, regardless of who wins this trick. If the Lackey plays the Cat, the Lackey leads next. If the Dark Lord plays the Cat from their own hand, they lead next from their own hand. *(Takes effect after the trick resolves.)* |

---

## Spells — Detailed Rules

Spells may be played on any trick and always count as following suit.

**When led:** Name a suit. The spell counts as a zero of that named suit. Other players must follow the named suit if able.

**When played to an existing trick:** The spell has no suit for the purpose of winning — its value comes from its effect.

### Angel of Death
There is no trump for this trick (greater or lesser). Highest card of the led suit wins. (Resolves during trick resolution.)

### Evil Twin
Choose one other card already played in this trick. Evil Twin becomes a copy of that card — same suit, same rank. If the copied card has a special effect, Evil Twin triggers that effect as well. Evil Twin **loses ties** with the card it copies.

### Nightmare Zone
After the trick resolves and a winner is determined, the trick **does not count for either side**. Move the won cards to the shadows — they do not count toward anyone's trick total. The trick still happens: abilities trigger, cards are spent.

### Tome of Tricks
This trick counts as **two tricks** during scoring. Keep the Tome of Tricks card face-up in the winner's trick pile as a reminder.

### Spell Interactions

When multiple spells appear in the same trick, resolve their effects in combination:

- **Angel of Death + Nightmare Zone:** Trump is negated, highest of the led suit wins — then the whole trick goes to the shadows. The Angel negates trump cards; the Nightmare Zone makes it not matter.
- **Evil Twin + Angel of Death:** Evil Twin copies the Angel's effect, but it's redundant — trump is already negated for the trick. The Evil Twin has no suit and can't win.
- **Evil Twin + Nightmare Zone:** Evil Twin copies the Nightmare Zone effect. The trick still goes to the shadows (it was going there anyway).
- **Evil Twin + Tome of Tricks:** Evil Twin copies the Tome. The trick counts as two tricks during scoring. (Only one Tome reminder is needed.)
- **Angel of Death + Tome of Tricks:** Trump is negated, and the trick counts double. Both effects apply independently.
- **Three or more spells in one trick:** Apply all effects. If both Angel of Death and Nightmare Zone are present, trump is negated *and* the trick goes to the shadows. The Tome has no impact if the trick is going to the shadows anyway.

---

## Scoring

After all 10 tricks have been played, count the Dark Lord's tricks. Tricks won by the Lackey count toward the Dark Lord's total. A trick containing Tome of Tricks counts as two. A trick containing Nightmare Zone counts for neither side.

### Dark Lord Wins (meets or exceeds bid)

- **Bid × 10** points to the Dark Lord.
- **+1 point** per trick over the bid.
- If "Threats Only" was declared: double the Dark Lord's points for this hand.

### Dark Lord Fails (fewer tricks than bid)

- Each Hero gains **bid × 5** points.
- If "Threats Only" was declared: double the Heroes' points for this hand.

*The scoring is asymmetric by design: the Dark Lord risks more (controlling two hands against two opponents) and earns more for winning. Heroes earn less per hand but share the reward and face less risk.*

---

## Winning the Game

The first player to reach **250 points** wins.

If multiple players cross 250 on the same hand, the player with the higher score wins. If still tied, then it's a tie. You've met your match.

---

## Turn Summary

1. **Deal** — 10 to each player, 10 face-up to the Lackey, 4 face-down to the shadows.
2. **Auction** — Bid number of tricks. First bidder must bid at least 1. Highest bidder becomes the Dark Lord.
3. **Assumption** — Dark Lord names lesser trump (or Threats Only). Lackey placed across from them.
4. **Play** — 10 tricks, normal clockwise play. Dark Lord leads first.
5. **Score** — Award points based on the Dark Lord's bid and result.
6. **Rotate** — Dealer passes clockwise. Shuffle and deal a new hand.
