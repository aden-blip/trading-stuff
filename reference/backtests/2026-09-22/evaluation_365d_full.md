# Full evaluation of the strategy on the 365-day trade list

Source: `reference/backtests/2026-09-21/trades_M6v0.1_base_deep-365d_500k.csv`, 2,963 closed
trades, 21 Sep 2025 to 18 Sep 2026, MNQ 5-minute, the M4/M6 default settings.
Halves split at 21 Mar 2026. A finding counts only when both halves agree (D-88).

**Costs.** 3.20 commission a round trip plus about 4.00 of slippage (2 ticks each way on two
contracts), 7.20 in all. Below, `raw` adds both back: it is the edge of the entry itself
before friction, and it is the number that decides whether a slice can ever pay.

## 1. The headline: the entry loses before it pays a cent of cost

| slice | n | net USD | raw per trade | H1 raw | H2 raw |
|---|---|---|---|---|---|
| everything | 2963 | -57,795 | -12.3 | -8.1 | -17.4 |
| reversals | 2276 | -54,810 | -16.9 | -11.8 | -22.1 |
| break retests **both halves +** | 687 | -2,984 | 2.9 | 1.2 | 6.3 |

At -12.3 a trade before any friction the trigger is not a small edge eaten by costs. It is
negative on its own. The share of trades reaching the target is 24.3 %, against 27.7 % for a
random entry with the same stop and target, so the signal carries slightly worse than no
information at all.

## 2. The two mechanical leaks, both large and both consistent

### The four-hour boundary hours

CME four-hour candles open at 17, 21, 01, 05, 09 and 13 Central. A brand-new four-hour open
is a line drawn through the current price, so the bot trades the middle of the action.

| slice | n | net USD | raw per trade | H1 raw | H2 raw |
|---|---|---|---|---|---|
| entry in a four-hour boundary hour | 963 | -36,728 | -30.9 | -11.3 | -52.3 |
| entry in any other hour | 2000 | -21,067 | -3.3 | -6.6 | 0.7 |

### The level set: opens and mids against true swing extremes

| slice | n | net USD | raw per trade | H1 raw | H2 raw |
|---|---|---|---|---|---|
| zone is a pure swing extreme or repeated-touch level | 869 | -12,349 | -7.0 | -3.7 | -10.9 |
| zone is a pure open | 743 | -13,408 | -10.8 | -6.5 | -17.5 |
| zone is a pure mid | 280 | -9,816 | -27.9 | -4.1 | -63.0 |

By level, the ten that cost the most and the six that paid:

| code | n | net USD | raw per trade |
|---|---|---|---|
| 4HO | 620 | -27,174 | -36.6 |
| DO | 343 | -11,438 | -26.1 |
| P4H | 285 | -8,608 | -23.0 |
| LH | 226 | -8,143 | -28.8 |
| MNM | 183 | -8,114 | -37.1 |
| WO | 135 | -7,262 | -46.6 |
| NO | 187 | -6,847 | -29.4 |
| PWM | 83 | -6,701 | -73.5 |
| P4L | 245 | -6,668 | -20.0 |
| LOD | 97 | -5,430 | -48.8 |
| ... | | | |
| MNH | 106 | 86 | 8.0 |
| AO | 267 | 730 | 9.9 |
| SR3 | 70 | 787 | 18.4 |
| PWH | 47 | 2,560 | 61.7 |
| PDH | 133 | 3,352 | 32.4 |
| NL | 104 | 6,047 | 65.3 |

The current four-hour open alone cost 27,174 on 620 trades. The daily open cost 11,438.
What paid was the New York low, the previous day high, the previous week high, the Asia open,
the Monday high and the three-touch repeated level: swing extremes, every one.

**The ten hand-drawn pivot boxes were empty for the entire year.** No trade in the sample was
taken at a level the owner drew. Everything tested so far is the automatic level set.

## 3. The deepest finding: the trades that fight the move are the losing core

A directional read taken from the list itself: where the entry sits against the entry prices
of the previous 24 hours, and whether the trade direction agrees with the drift of that
window. Both are known before the trade, so this is a fair test of a bias gate.

| slice | n | net USD | raw per trade | H1 raw | H2 raw |
|---|---|---|---|---|---|
| buy the low or sell the high (the reversal idea) | 782 | -28,128 | -28.8 | -25.8 | -32.7 |
| anything in the middle third of the range | 464 | -2,236 | 2.4 | 12.2 | -10.6 |
| buy the high or sell the low (with the move) | 978 | -16,304 | -9.5 | -4.5 | -15.7 |
| direction agrees with the drift | 1250 | -18,738 | -7.8 | 3.2 | -21.5 |
| direction fights the drift | 974 | -27,930 | -21.5 | -23.2 | -19.1 |
| reversal fighting the drift | 731 | -26,668 | -29.3 | -25.8 | -33.5 |
| reversal with the drift | 941 | -17,052 | -10.9 | 2.7 | -25.1 |
| break retest fighting the drift | 243 | -1,262 | 2.0 | -16.9 | 42.7 |
| break retest with the drift | 309 | -1,686 | 1.7 | 4.5 | -4.3 |

Buying the bottom of the range and selling the top, which is what a reversal at a level does
by construction, is the worst slice in the whole sample: -28.8 a trade before costs, negative
on both halves. Fighting the drift loses nearly three times what going with it loses.

## 4. The only slices positive on both halves before costs

| slice | n | net USD | net per trade | raw per trade | H1 raw | H2 raw |
|---|---|---|---|---|---|---|
| break retest, with the drift, outside boundary hours | 218 | 483 | 2.2 | 9.4 | 5.3 | 19.3 |
| either setup, with the drift, clean level and hour | 246 | 119 | 0.5 | 7.7 | 6.2 | 10.0 |
| reversal, with the drift, clean level and hour | 197 | -325 | -1.7 | 5.5 | 0.5 | 12.0 |

These are the first slices in the project that are positive on both halves. They are small,
about one trade a day, and the net per trade is a couple of dollars, so costs still eat most
of the edge. They are a direction to build in, not a strategy yet.

## 5. No geometry saves the current entry

On the cleanest slice the settings can reach (reversals at a pure swing extreme outside the
boundary hours, 527 trades), every stop from 8 to 40 points was paired with every target from
20 to 120 and replayed exactly against each trade's own excursions, with ties given to the
stop. Of 41 combinations, none was positive on the year and none on both halves. The best,
a 12-point stop with a 120-point target, still lost 1,630. Note this reading is hard on wide
targets, because a trade that stopped early never had the chance to reach one.

The reason is point 1: with the hit rate at the coin-flip rate, expectancy is zero before
costs whatever the stop and target are. Geometry moves the shape of the outcomes, not the sign.

## 6. The honest bottom line, with the fitting removed

Dropping the worst-performing levels after seeing the whole year looked good (178 trades,
+4,425, positive on both halves) but it does not survive an out-of-sample test. Choosing the
levels to drop on the first half and then trading only the second gives +1,036 at two levels
dropped, -756 at four, +510 at six. The direction flips with the count, so the gain is noise,
not a rule. The lists themselves are stable (seven of the worst eight repeat across halves),
but acting on them leaves too few trades to mean anything.

What survives with no picking at all:

| slice | n | net USD | net per trade | raw per trade |
|---|---|---|---|---|
| with the drift, pure swing extreme, outside boundary hours, whole year | 246 | +119 | +0.5 | +7.7 |
| the same, first half only | 150 | -147 | -1.0 | +6.2 |
| the same, second half only | 96 | +266 | +2.8 | +10.0 |

Payoff on that slice is 2.3 to 1, the hit rate 30.5 %, the worst run of losses 3,781 USD, and
it trades about once a day.

**That is the ceiling of the current design: break-even.** The raw edge is about 8 USD a trade
and costs are 7.20. Everything else in the strategy is leakage on top of it.

To get from break-even to profitable, one of two things has to change, and preferably both:

1. **A bigger raw edge per trade.** Three untested candidates, in order of promise: the owner's
   own hand-drawn pivot lines, which were empty for the whole year; a real directional read
   rather than the crude drift proxy used here (the script already carries a higher-timeframe
   trend vote and a session VWAP side vote, both built and both weighted zero); and an entry
   resting at the level rather than a market order a candle or two away.
2. **Lower costs.** Of the 7.20 a trade, about 4.00 is slippage from market entries and exits.
   A resting limit at the level pays no slippage on entry, which is worth roughly 2.00 a trade,
   a quarter of the whole edge.
