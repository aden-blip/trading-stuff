# Changelog

## M2 v0.1, 2026-09-20

- Untagged support and resistance (SR): completed bars of the pivot timeframe (4-hour default)
  give pivot highs and lows; pivots inside the lookback are clustered within the SR tolerance and
  a cluster with enough touches is a level, priced at the mean of its touches, line from the first
  touch, tag "S/R (n)". Strongest clusters kept. Inputs per D-65.
- Interaction classifier per level instance: touch, approach side from the prior close,
  HELD / BROKE / NEUTRAL on confirmed bars only, first HELD or BROKE counted, every verdict can be
  marked on the chart ("Counted only" by default, rolling 150 marks).
- Statistics table per level type: N, hold %, break %, neutral, rank percentile; totals row;
  priors as one text input `code:rate:count`.
- Level slots unified: 38 labeled, up to 20 custom, up to 30 SR, one loop for touch, verdict and
  drawing. Info box shows the SR count, pivot count and interactions counted.
- Hidden VWAP and 200 EMA hooks are M3 (D-64); nothing new is drawn in M2.

## M1 v0.8, 2026-09-20

- Levels within the touch tolerance share one tag, names joined with a slash, tag at their mean
  price; every level keeps its own line. Share distance is a daily-ATR input with a tick floor,
  0 and 0 means identical prices only (D-63).
- Stagger columns are as wide as their longest name, from a bars-per-character input scaled by
  the label size. Five columns by default. Text-only labels start at the column edge.
- Fixed step and text pad inputs removed.

## M1 v0.7, 2026-09-20

- Boxed bookmark tags are the default label style again; text only stays as an option (D-62).
- Stagger distance is a share of the daily ATR with a tick floor, scaled by the square root of the
  chart timeframe. Step widened to 40 bars, three columns, and each label takes the first column
  with room below it. A level's line now runs to its own tag, so staggered tags stay attached.
- Label positions are capped 480 bars past the last candle, inside TradingView's drawing limit.

## M1 v0.6, 2026-09-20

- Labels that would sit within a set distance of each other step right into up to four columns
  so nearby levels stay readable. Stagger distance, step and column count are inputs.

## M1 v0.5, 2026-09-20

- Spaceman alignment: text-only coloured labels by default (boxed optional), size normal, line
  end 30 bars right of price, merge only at identical prices with " / ", per-level toggles,
  global colour, line style. Year high/low include today; Monday range develops live.

## M1 v0.4, 2026-09-20

- Session levels develop live while the session runs and freeze when it ends; "Completed only" switch.
- One line per level; labels merge only within one tick; boxes removed. Full names by default,
  short codes as the option, label offset 20 bars.
- Period tracker ignores a boundary on the very first bar of history.

## M1 v0.3, 2026-09-20

- New York session default 08:30 to 16:00 CT on every profile (D-56).
- Day, week, month and 4-hour levels measured from chart candles with the bar of each extreme, so
  lines start at the candle that made the level. Week and month fall back to higher-timeframe
  requests on short histories. Five requests total.
- Added PQH, PQL, PQM, YM, P4M and 4HO for Spaceman parity.
- Display: candle-anchored or right-anchored lines, longest-line cap, label offset, label size,
  short codes or full names, optional price, line width. All levels drawn by default; near-price
  limit is a switch.

## M1 v0.2, 2026-09-20

- Midnight open now requires the bar to sit in the first hour of the day in the anchor zone, so
  the Sunday reopen and any other gap no longer count as a midnight. Charts above 60 minutes
  keep the plain date change.
- First live check on MNQ 5-minute passed: profile, timezone, tolerances, clustering, session
  and daily levels consistent with the candles.

## M1 v0.1, 2026-09-19

- First script: `l2l.pine`, module [A] Level Engine, as an indicator.
- Level types: PDH PDL PDM DO MO, PWH PWL PWM WO, PMH PML PMM MOO, QO YO YH YL, P4H P4L P4O,
  MNH MNL MNM, Asia / London / New York session high low open, custom levels from a text input.
- Clustering into zones with daily-ATR tolerance and tick floor; a zone of two or more levels
  draws as a box with the codes joined.
- Fresh / touched state per level instance, reset at the daily rollover; optional `*` marker only.
- Timezone input, instrument profile (auto from the symbol root), midnight-open anchor.
- Info box and optional history plots for replay checks.
- Not yet: SR touch-cluster levels (M2), statistics (M2), signals (M3), strategy (M4 on).
