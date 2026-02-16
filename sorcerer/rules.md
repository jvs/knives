# Sorcerer

A trick-taking card game for 3 players.

---

## Overview

Three players compete across multiple hands. Each hand, one player becomes **the Sorcerer** through an auction, taking control of a face-up **Apprentice hand** and playing two hands against the other two players (**the Hunters**). The first player to **250 points** wins.

---

## Components

### The Deck (42 cards)

**Traditional Suits (36 cards)** — Four suits of 9 cards each:

| Suit | Prank Card | Number Cards | Face Cards |
|------|-----------|--------------|------------|
| Spades | Snitch | 2, 3, 4, 5 | Jack, Queen, King, Ace |
| Diamonds | Devil | 2, 3, 4, 5 | Jack, Queen, King, Ace |
| Hearts | Hound | 2, 3, 4, 5 | Jack, Queen, King, Ace |
| Clubs | Cat | 2, 3, 4, 5 | Jack, Queen, King, Ace |

Rank order within a suit (low to high): Prank, 2, 3, 4, 5, Jack, Queen, King, Ace.

**Fiends (4 cards)** — The greater trump suit. Fiends always beat any card from a traditional suit, including lesser trump.

| Card | Rank |
|------|------|
| Goblin | 6 |
| Ogre | 7 |
| Dragon | 8 |
| Witch | 9 |

(Production Note: Each Fiend card indicates its rank number.)

**Wild Cards (2 cards)** — Wild cards have no suit and no rank. They may be played on any trick, even if you have cards in the led suit.

| Card | Effect |
|------|--------|
| **Joker** | Always wins the trick. |
| **Fool** | Always loses the trick. Cannot win under any circumstances. |

Wild cards cannot be led. If you must lead and hold only wild cards, reveal your hand. The player to your left leads instead.

---

## Setup

1. Shuffle the deck.
2. Deal **9 cards** to each player.
3. Deal **9 cards face-up** to the center of the table. This is the **Apprentice hand** (or just "the Apprentice").
4. Deal **6 cards face-down** to the side. These are **the Woods** — out of play and not revealed until the hand is over.
5. The dealer sorts the Apprentice by suit and rank, so all players can read it easily.

All players may examine the Apprentice before bidding begins.

---

## The Auction

The player to the dealer's left bids first and **may not pass**.

Each bid consists of a **number of tricks** and a **trump declaration** — either a lesser trump suit or "Fiends Only." For example: "4 Hearts" or "5 Fiends Only."

Bidding proceeds clockwise. Each bid must have a **higher number of tricks** than the previous bid, regardless of the trump declaration. A player may **pass** instead of bidding. Once you pass, you are done with bidding for this hand.

When two players have passed, the remaining bidder becomes **the Sorcerer**. The Sorcerer is committed to winning at least the number of tricks in their bid, with the trump they declared. The Apprentice is placed across from the Sorcerer, and the Sorcerer leads the first trick.

---

## Trump Hierarchy

Cards from strongest to weakest:

1. **Joker** — always wins the trick
2. **Fiends** (greater trump) — Witch > Dragon > Ogre > Goblin
3. **Lesser trump** (the suit named in the winning bid) — normal rank order within the suit
4. **Led suit** — the suit of the first card played in a trick
5. **Off-suit cards and the Fool** — cannot win a trick

Fiends are always the top trump. Lesser trump beats non-trump suits. If no Fiend or trump is played, the highest card of the led suit wins.

If "Fiends Only" was declared, there is no lesser trump — only Fiends outrank the led suit.

---

## Playing a Hand

The Sorcerer controls two hands: their own hand (hidden, like any player's) and the Apprentice (face-up, visible to all). These are separate hands — each follows suit independently, and each plays in its own seat in the turn order.

The Sorcerer leads the first trick. After that, the winner of each trick leads the next. If the Apprentice wins a trick, the Apprentice leads the next trick (with the Sorcerer choosing which card to play from it). Play proceeds clockwise. On the Apprentice's turn, the Sorcerer plays a card from the Apprentice.

### Following Suit

- Players must follow the led suit if able.
- If a player cannot follow suit, they may play any card.
- Wild cards may be played on any trick, even if you have cards in the led suit.
- The Sorcerer's own hand and the Apprentice follow suit **independently**. Each must follow the led suit using only the cards available in that hand.

### Leading Fiends

- **Leading with a Fiend:** Other players must play a Fiend if able. If they have no Fiends, they may play any card. *(Fiends are their own suit.)*

### Leading Restrictions

- Wild cards cannot be led. If you must lead and hold only wild cards, reveal your hand. The player to your left leads instead.
- If the Apprentice must lead and holds only wild cards, reveal the Apprentice. The player to the Apprentice's left leads instead.

---

## Prank Cards

Each suit's Prank card has a unique ability. Prank abilities take effect **immediately when played** (before the trick resolves), except where noted.

Prank cards are the **lowest-ranked card** in their suit — playing one means you're almost certainly losing the trick. The ability is the trade-off.

| Prank | Suit | Ability |
|-------|------|---------|
| **Snitch** | Spades | Look at all cards in the Woods. Shuffle them and return them face-down. |
| **Devil** | Diamonds | Choose a target: another player, the Apprentice, or the Woods. You and the target each exchange a card face-down. If the target is the Apprentice, the Sorcerer chooses which Apprentice card to exchange, and both cards are revealed (since the Apprentice is face-up). If the target is the Woods, place a card from your hand face-down in the Woods, then draw a card from the Woods at random. |
| **Hound** | Hearts | Choose one: (a) Choose a player — that player reveals one card of their choice to all players, keeping it in hand. (b) Flip one card from the Woods face-up. It remains face-up in the Woods for the rest of the hand. |
| **Cat** | Clubs | Choose who leads the next trick: yourself, another player, or the Apprentice. The chosen player leads regardless of who wins this trick. *(Takes effect after the trick resolves.)* |

---

## Scoring

After all 9 tricks have been played, count the Sorcerer's tricks. Tricks won by the Apprentice count toward the Sorcerer's total.

### Sorcerer Succeeds (meets or exceeds bid)

- Sorcerer gains **bid × 10** points.
- If "Fiends Only" was declared: double the Sorcerer's points for this hand.

### Sorcerer Fails (fewer tricks than bid)

- Sorcerer gains **nothing**.
- Each Hunter gains **bid × 5** points.
- If "Fiends Only" was declared: double the Hunters' points for this hand.

*The scoring is asymmetric by design: the Sorcerer risks more (controlling two hands against two opponents) and earns more for winning. Hunters earn less per hand but share the reward and face less risk.*

---

## Winning the Game

The first player to reach **250 points** wins.

If multiple players cross 250 on the same hand, the player with the higher score wins. If still tied, then it's a tie. You've met your match.

---

## Turn Summary

1. **Deal** — 9 to each player, 9 face-up to the Apprentice, 6 face-down to the Woods.
2. **Auction** — Bid a number of tricks and a trump declaration. First bidder may not pass. Highest bidder becomes the Sorcerer.
3. **Setup** — Apprentice placed across from the Sorcerer.
4. **Play** — 9 tricks, normal clockwise play. Sorcerer leads first.
5. **Score** — Award points based on the Sorcerer's bid and result.
6. **Rotate** — Dealer passes clockwise. Shuffle and deal a new hand.
