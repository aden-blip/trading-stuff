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
