# Dark Lord

A trick-taking card game for 3 players.

---

## Overview

Three players compete across multiple hands. Each hand, one player becomes **the Dark Lord** through an auction, taking control of a face-up **Lackey hand** and playing two hands against the other two players (**the Defenders**). The first player to **250 points** wins.

---

## Components

### The Deck (44 cards)

**Traditional Suits (36 cards)** — Four suits of 9 cards each:

| Suit | Prank Card | Number Cards | Face Cards |
|------|-----------|--------------|------------|
| Spades | Spy | 2, 3, 4, 5 | Jack, Queen, King, Ace |
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

**Wild (4 cards)** — Wild cards that may be played on any trick and always count as following suit.

| Card | Effect |
|------|--------|
| **Darkness** | After this trick resolves, move the cards from this trick to the shadows. The trick does not count for either side during scoring. |
| **Death** | All Threat cards in this trick become a zero of hearts (the lowest possible rank). |
| **Disguise** | Play as a copy of another card already in the trick. Loses ties. Copies any special effects. |
| **Double** | This trick counts as two tricks during scoring. Keep this card separate from the trick as a reminder. |

---

## Setup

1. Shuffle the deck.
2. Deal **10 cards** to each player.
3. Deal **10 cards face-up** to the center of the table. This is the **Lackey hand**.
4. Deal **4 cards face-down** to the side. These are the **shadows** — out of play and not revealed until the hand is over.

All players may examine the Lackey hand before bidding begins.

---

## The Auction

The player to the dealer's left bids first and **must bid at least 1**. Bidding proceeds clockwise.

Each bid is a **number of tricks** — the minimum the Dark Lord commits to winning. Each bid must be higher than the previous bid. A player may **pass** instead of bidding. Once you pass, you are done with bidding for this hand.

When two players have passed, the remaining bidder becomes **the Dark Lord**.

### Dark Lord Assumption

1. The Lackey hand is placed across from the Dark Lord.
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

The Dark Lord leads the first trick. After that, the winner of each trick leads the next.

### Trick Play

Play proceeds normally, as in bridge. Players take turns clockwise. The Dark Lord plays their own hand and the Lackey hand as two separate hands — when it is the Lackey's turn, the Dark Lord plays a card from the Lackey hand.

If the Lackey hand wins a trick, the Lackey hand leads the next trick (with the Dark Lord choosing which card to play from it).

### Following Suit

- Players must follow the led suit if able.
- If a player cannot follow suit, they may play any card.
- The Dark Lord's hidden hand and the Lackey hand are **separate hands** for following suit. Each must independently follow suit when playing from that hand.
- Wild cards may be played at any time and always count as following suit.

### Leading with Special Cards

- **Leading with a Threat:** Other players must play a Threat if able. If they have no Threats, they may play any card. *(Threats are their own suit.)*
- **Leading with a wild card:** The player names a suit. The wild card is treated as a zero of that named suit. Other players must follow the named suit if able.

---

## Prank Cards

Each suit's Prank card has a unique ability that triggers **when the card is played**, regardless of whether it wins the trick.

| Prank | Suit | Ability |
|-------|------|---------|
| **Spy** | Spades | Ask any one player a yes-or-no question. That player must answer truthfully. |
| **Devil** | Diamonds | Choose a target player (or the Lackey hand). The target selects a card from their hand and you swap it with a card from your hand. The swap is done face-down — you don't see what you're getting until the swap is complete. If a player targets the Lackey hand, the Dark Lord chooses which Lackey card to swap. |
| **Hound** | Hearts | Choose a player. That player chooses one card from their hand to reveal to all players. |
| **Cat** | Clubs | You lead the next trick, regardless of who wins this trick. |

Prank cards are the **lowest-ranked card** in their suit — playing one means you're almost certainly losing the trick. The ability is the trade-off.

---

## Wild Cards — Detailed Rules

Wild cards may be played on any trick and always count as following suit.

**When led:** Name a suit. The wild card counts as a zero of that suit. Other players must follow the named suit if able.

**When played to an existing trick:** The wild card has no suit for the purpose of winning — its value comes from its effect.

### Darkness
After the trick resolves and a winner is determined, the trick **does not count for either side**. Move the won cards to the shadows — they do not count toward anyone's trick total. The trick still happens: abilities trigger, cards are spent.

### Death
All Threat cards played to this trick become a **zero of hearts**. No Threat card may win this trick. If all of the other cards in this trick are Threat cards, then this card wins the trick.

### Disguise
Choose one other card already played in this trick. Disguise becomes a copy of that card — same suit, same rank. If the copied card has a special effect, Disguise triggers that effect as well. Disguise **loses ties** with the card it copies.

### Double
This trick counts as **two tricks** during scoring. Keep the Double card face-up in the winner's trick pile as a reminder.

---

## Scoring

After all 10 tricks have been played, count the Dark Lord's tricks. Tricks won by the Lackey hand count toward the Dark Lord's total. A trick containing Double counts as two. A trick containing Darkness counts for neither side.

### Dark Lord Wins (meets or exceeds bid)

- **Bid × 10** points to the Dark Lord.
- **+1 point** per trick over the bid.
- If "Threats Only" was declared: double the Dark Lord's points for this hand.

### Dark Lord Fails (fewer tricks than bid)

- Each Defender gains **bid × 5** points.
- If "Threats Only" was declared: double the Defenders' points for this hand.

---

## Winning the Game

The first player to reach **250 points** wins.

If multiple players cross 250 on the same hand, the player with the higher score wins. If still tied, then it's a tie. You've met your match.

---

## Turn Summary

1. **Deal** — 10 to each player, 10 face-up to the Lackey, 4 face-down to the shadows.
2. **Auction** — Bid number of tricks. First bidder must bid at least 1. Highest bidder becomes the Dark Lord.
3. **Assumption** — Dark Lord names lesser trump (or Threats Only). Lackey hand placed across from them.
4. **Play** — 10 tricks, normal clockwise play. Dark Lord leads first.
5. **Score** — Award points based on the Dark Lord's bid and result.
6. **Rotate** — Dealer passes clockwise. Shuffle and deal a new hand.
