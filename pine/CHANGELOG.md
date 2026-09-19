# Changelog

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
