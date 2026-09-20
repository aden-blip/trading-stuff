# Changelog

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
