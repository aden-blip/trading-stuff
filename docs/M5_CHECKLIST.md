# M5 checklist: the trade manager in the tester

Same paste as before. The info box must read `L2L M5 v0.1`. New settings group "Trade manager
(M5)" with the stage switch ON by default.

## Checks

1. **Compiles and the tester runs.** Report the first error line if not.
2. **OFF reproduces M4.** Settings, Trade manager, untick "Move the stop in stages", Deep
   Backtesting "Last 365 days" at 500,000: 2,963 trades, net -57,794.60 USD, profit factor
   0.84 (session 15). If those numbers differ, something else changed and the run is not
   comparable; report the grey settings line and the numbers.
3. **ON, the same run.** Tick the switch again (Defaults button), same range and capital.
   Screenshot the Overview, then export the list of trades and send the file. The exit
   column now has five words: T1, stop, half, be, flat.
4. **On the chart (normal range):** navy tags "1/2R ..." and "BE ..." at the price where the
   stop moved, on the candle whose run-up earned the move; the exit tag of a trade stopped
   after a move reads "half" or "be" with the points. The Paper trades row of the info box
   counts "moved stop" exits, and the Tester rows still sit within a few trades of the Paper
   rows.
5. **One trade by hand.** Pick a trade with a BE tag: the stop tag's price should be the entry
   plus 2 ticks (or 0.02 execution ATRs if larger), and it should appear on the first closed
   candle whose high (long) or low (short) was a full R from the entry. The stop tag never
   moves back.
6. **Alerts.** Unchanged setup ("Any alert() function call"). New STOP messages report each
   move with the stage and the price.

## Report back

- The two Overviews (OFF and ON) and the exported list of the ON run.
- Any exit that looks wrong: a "be" exit far from the entry, a "half" exit that is not about
  half the first risk, a stop tag on a candle that did not reach the threshold.
