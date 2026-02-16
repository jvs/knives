# Secret Agent

A trick-taking card game for 4 players. One player is a secret agent trying to win tricks against three enforcers.

## Overview

One player is secretly the Agent. The other three are Enforcers. The Agent wins by taking at least as many tricks as the Enforcers. The Enforcers win by taking more tricks than the Agent.

The Agent has tools to give them an edge:
- Snarking: The Agent can play cards without following suit while their Badge is face down.
- Double-Cross: The Agent can unmask themselves to steal a trick.
- Raiding the Stash: When the Agent is unmasked, they pick up the Stash and improve their hand.

But watch out! The Enforcers can unmask the Agent in two ways:
- When the player across from the Agent wins two tricks, the Agent's cover is blown.
- (Design question: should the Agent's cover get blown when they win two or three tricks? That makes more sense, but does it work better?)
- A special card called the Snitch can also unmask the Agent, but it using it well requires a lot of skill and a little bit of luck.
- (Design question: Do the Enforcers need a wild card to help them unmask the agent?)
- (Design question: Should the Hound be able to unmask the Agent, in addition to or maybe instead of the Snitch? The Hound is wild, which makes it easier to play.)
- Try your best: Once unmasked, the Agent can no longer snark. They have to follow suit like everyone else!


## The Deck (40 cards)

Five suits:

- **Diamonds, Spades, Clubs** (Prank, 2, 3, 4, 5, 6, 7, Ace): Normal suits.
- **Hearts** (Prank, 2, 3, 4, 5, 6, 7, Ace): Wild. Can always be played regardless of what was led.
- **Shots** (2–9): Trump. Beats all other suits. Can only be played when void in the led suit (unless you're the secret Agent — see below).

Rank order within a suit, from lowest to highest: Prank, 2, 3, 4, 5, 6, 7, Ace. For Shots: 2 (lowest) through 9 (highest).

## Setup

1. **Deal** 9 cards to each player.
2. Place the remaining 4 cards face down on the table. This is **the Stash**.
3. **Deal badges.** Shuffle 1 Agent badge and 3 Enforcer badges. Deal one face down to each player. Look at your own Badge secretly.
4. The dealer leads the first trick.

## Playing Tricks

The leader plays any card. Each subsequent player must follow suit if able, with these exceptions:

- **Hearts** can always be played instead of following suit.
- **Shots** can only be played if you have no cards of the led suit.
- **Leading a Heart:** Hearts are the led suit. Players with hearts must follow. Highest heart wins.
- **Snarking (Agent Only):** The Agent may ignore follow-suit rules while their Badge is face down. See Agent Powers.

**Winning a trick:** Highest Shot wins. If no Shots, highest card of the led suit wins. Hearts played as wild can't win tricks. The trick winner leads next.

## Agent Powers

### Snarking (Undercover Only)

While their Badge is face down, the Agent can play any card at any time, ignoring follow-suit rules. This includes playing Shots while holding the led suit, or playing off-suit when they could follow.

Only the Agent can snark. If you catch someone not following suit, you know who the Agent is. But if their badge is face down, they can keep snarking, even though you know who they are.

**Once the Agent's Badge is face up, they must follow suit like everyone else.**

### The Double-Cross!

After a trick resolves, the Agent may flip their Badge face up, and take the trick from whoever won it. The Agent also steals the lead, and leads the next trick. The Enforcers were double-crossed!

Immediately after the Double-Cross, the Agent raids the Stash (see below).

### Cover Blown!

When the player across from the Agent wins two tricks, the Agent must flip their badge face up. Their cover has been blown!

Immediately after their cover has been blown, the Agent raids the Stash (see below).

(Design question: should the Agent's cover get blown when they win two or three tricks? That makes more sense, but does it work better?)

(Design question: So wouldn't the Agent just Double-Cross the trick, if the player across from them is about to win their second trick? If that's the case, then should that just be built into the rules?)

### Ratted Out!

If someoen plays the Snitch, targets the Agent, and flips their badge face up, the Agent is unmasked. The Snitch ratted them out!

Immediately after being ratted out, the Agent raids the Stash (see below).

(Design question: Is it unnecessarily repetitive to keep reminding players that the Agent raids the stash when they're unmasked?)


## The Stash

The Stash starts with 4 face-down cards from the deal.

### Raiding the Stash

When the Agent's Badge is flipped face up — by the Double-Cross, Cover Blown, or The Snitch — the Agent immediately raids the Stash:

1. Pick up all four cards in the Stash and add them to your hand.
2. Discard four cards face down, creating a new Stash.

---

## Prank Cards

Each suit's Prank card has a unique ability. Prank abilities take effect **immediately when played** (before the trick resolves), except where noted.


| Prank | Suit | Ability |
|-------|------|---------|
| **Snitch** | Spades | Choose a target: another player or the Stash. If you target another player, and their badge is face down, flip their badge face up. If you target the Stash, put your cards on the table, pick up the Stash, look at the cards, and then return them face down. |
| **Devil** | Diamonds | Choose a target: another player, or the Stash. You and the target each exchange a card face-down. If the target is the Stash, place a card from your hand face-down in the Stash, then draw a card from the Stash at random. |
| **Hound** | Hearts | Choose one: (a) Choose a player — that player reveals one card of their choice to all players, keeping it in hand. (b) Flip one card from the Stash face-up. It remains face-up in the Stash for the rest of the hand. |
| **Cat** | Clubs | Choose who leads the next trick. The chosen player leads regardless of who wins this trick. *(Takes effect after the trick resolves.)* |

(Design question: Is the Hound basically useless to the Agent? Is that OK, or does it need work?)

## Scoring

After all tricks are played, the team with the most tricks wins. If tied, the Agent wins.

Each round awards points to the winning side:

- **Agent wins:** The Agent gets **+4 points**.
- **Enforcers win:** Each Enforcer gets **+2 points**.

**First player to 10 points wins the game.** Shuffle and deal new Badges each round. The Agent role is random each time.
