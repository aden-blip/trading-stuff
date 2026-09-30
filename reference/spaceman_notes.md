# Spaceman "Key Levels IDWM" V13.1: what we took from the source

The owner pasted the open-source script on 2026-09-20. Facts that shaped L2L M1 v0.5:

- **Levels:** 4H open, prev 4H high/low/mid; daily open, prev day high/low/mid; Monday range
  high/low/mid; weekly, monthly and quarterly open plus prev high/low/mid; yearly open plus the
  current year high/low/mid; London, New York and Asia session high/low/open.
- **Session levels develop live** while the session runs and keep their last value after it ends.
- **Year high/low** come from the running yearly bar, so they include today's price action.
- **Monday range** is the first daily bar of the weekly bar, which on CME futures is the Sunday
  17:00 CT to Monday 16:00 CT session.
- **Lines** start at the period's first candle and end a fixed number of bars right of now
  (default 30). "Right Anchored" gives every line the same length.
- **Labels** are plain coloured text with no box (`label.style_none`), default size medium, at the
  end of the line. Short-hand or full descriptions per family or globally.
- **Merging** only happens at the identical price, texts joined with " / ".
- **Per-family toggles:** Open, Prev H/L, Prev Mid; Monday Range and Mid; sessions as ranges.
- **Global colour** switch, line width and line style inputs.

Where L2L differs on purpose: lines start at the exact candle of the high or low rather than the
period's first candle; levels are measured from the chart's own candles with higher-timeframe
requests only as fallbacks; sessions are entered in the chosen timezone; custom levels exist.

## Pine v6 fixes to the source indicator, 2026-09-30

The owner's copy of V13.1 (with his All-Time High and Midnight Open additions) would not compile
under Pine v6. The corrected file is `reference/indicators/rpg_pivots_v13.1.pine`. Four compile
errors and three wiring slips:

- **Three "must evaluate to a bool" errors.** `London`, `US` and `Asia` were set from `time(...)`,
  which hands back a timestamp or nothing. Version 5 read that number as yes/no; version 6 wants a
  true-or-false answer. Each is now wrapped in `not na(...)`, so the `if London` / `if US` /
  `if Asia` lines below are unchanged.
- **Short title too long.** 27 characters against a 10-character limit; now `RPG Pivots`.
- **Label ceiling.** No `max_labels_count` was set, so it defaulted to 50 against roughly 38
  labels drawn. Raised to 200, and `max_lines_count` with it.
- **Three wiring slips, all cosmetic and all in the original:** the New York labels were created
  carrying the London text, the previous week low line was created at the weekly open price, and
  the previous month high line took the previous month low's timestamp. Each was overwritten a
  line or two later, so nothing showed; fixed at the source anyway.

Nothing else changed. The level set, the merging, the colours and the repainting behaviour of the
`lookahead_on` requests are all as the owner had them.
