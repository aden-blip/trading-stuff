# What the M7 v0.1 export says (417 trades, 2025-09-22 to 2026-09-16)

Files: `trades_M7v0.1_method_deep-365d_500k.csv`, `report_M7v0.1_deep-365d.md`,
`compare_M7v0.1_halves.md`. Halves split at 2026-03-20: H1 210 trades, H2 207.

Baseline: 417 trades, win 26.6 %, PF 0.93, net -1,426.40, -3.42 a trade, max drawdown 3,834.
By half: H1 PF 1.01 (+77), H2 PF 0.87 (-1,503). Costs are 7.20 a trade, so the year made
+1,576 before costs, about +3.78 a trade. First configuration ever to be gross-positive.

## Survives both halves

**1. Reversals with two or more higher-timeframe rejections.** The single strongest and most
stable slice in any export so far.

| Group | Trades | PF | Net | Per trade | H1 per trade | H2 per trade |
|---|---|---|---|---|---|---|
| f0 | 69 | 0.90 | -363 | -5.26 | -9.37 | +1.13 |
| f1 | 108 | 0.60 | -2,343 | -21.69 | -15.72 | -26.47 |
| f2 or more | 71 | 1.49 | +1,443 | +20.32 | **+19.07** | **+21.24** |

The two halves give almost the same per-trade number on either side of the split. f1 is the
worst group in the export and loses in both halves, which matches D-94 point 2: on a 5-minute
chart a count of 1 is usually the signal's own rejection candle, so f1 means no independent
higher-timeframe evidence at all. Two or more is the first count that brings a bigger candle in.

This was not picked out of this data. The feature was built in M6, D-94 measured it on the old
configuration and found the halves disagreed, and D-100 point 4 named the higher-timeframe read
as the method's requirement and the largest missing lever. It separates cleanly once the
method's other conditions are on.

**2. The breakeven stop, as a ceiling.** Moving the stop to the entry once a trade has run half
its risk in profit. Losers are exact (their own run-up decides); winners are assumed never
scratched, so these are ceilings, not forecasts.

| Set | As traded | + breakeven at 0.5R | H1 | H2 | Max DD |
|---|---|---|---|---|---|
| all 417 | -1,426 (PF 0.93) | +6,317 (PF 1.50) | +3,407 | +2,910 | 3,834 -> 1,158 |
| gate on (240) | +1,279 (PF 1.12) | +4,555 (PF 1.61) | +2,566 | +1,989 | 1,191 -> 611 |
| reversals f2+ only (71) | +1,443 (PF 1.49) | +2,601 (PF 2.45) | +972 | +1,629 | 738 -> 511 |

Why this is worth running now when D-93 turned the manager off: there, scratching early freed the
strategy to take more trades and every trade lost on average. M7 caps the day at four trades and
two losses, so a scratch no longer buys an extra loser. The mechanism that sank it is blocked.

21 % of stop-outs first ran a full stop distance in profit, and 47 % of losers ran at least 5
points in favour, which is where the gain comes from.

Half off at a target and letting the rest run fails: every partial-exit variant is worse than as
traded, and the best of them (half off at +0.5R with the runner at breakeven) is +1,061 in H1 and
-138 in H2.

**3. Score is inverted.** The lowest band is the only profitable one: s50s 152 trades, PF 1.24,
+1,705, positive in both halves (H1 +336, H2 +1,369). s60s -1,544, s70s -1,085, s90s -625.
Consistent with D-85 and D-100 point 6. The score is worse than useless as a ranking.

**4. Single levels beat stacked ones.** k1 300 trades PF 0.99, k2 90 trades PF 0.76, k3+ 27
trades PF 0.78. The score pays *more* for a stack, so it is scoring the wrong way round here
too. The halves disagree on k2 (H1 +287, H2 -1,323), so this is a reading, not a gate.

## Loses in both halves

- **Wednesday**: 94 trades, PF 0.49, -2,653 (H1 -224, H2 -2,428). Third independent sample
  agreeing, after D-91 point 3 on the M6 year.
- **Thursday**: 85 trades, PF 0.74, -1,135 (H1 -678, H2 -457).
- **f1 reversals**, above.
- **PDL** -998 (H1 -489, H2 -509), **the custom levels** -795 (H1 -135, H2 -661),
  **the New York level family** -663 (H1 -101, H2 -562).

## Fails the halves test, so not acted on

- **Break trades**: 169 trades, PF 0.98 overall, but H1 PF 1.19 (+653) and H2 PF 0.82 (-817).
  They are now the unstable half of the strategy, and they have no higher-timeframe test at all —
  the count is only computed for reversals. This reverses the reading in D-99 point 6, which was
  taken on the old configuration.
- The 09:00 hour (H1 +864, H2 -2,724), longs against shorts (H1 +46 / H2 -1,847 against
  H1 +8 / H2 +366), the daily family (H1 +537, H2 -1,798), PDH (H1 +1,026, H2 -1,289),
  the Monday family, the k2 stack, h12 and h6 level history.

## Not the answer

A closer target: every variant is worse (20 points -3,660, 30 points -2,944, 40 points -2,813
against -1,426 as traded). The current target placement is right and does not need moving again.
