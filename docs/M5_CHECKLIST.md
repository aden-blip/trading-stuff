# M5 checklist: the trade manager in the tester

Status: measured in sessions 16 and 17, switch OFF by default since M6 v0.1 (D-93). The
checks below apply whenever the manager is turned on again.

Same paste as before. The info box must read `L2L M5 v0.2`. Settings group "Trade manager
(M5)": the stage switch ON by default, the three R thresholds (0.5, 1.0, 1.5), the breakeven
cushion, the trail's swing width and distances, the marks, the stop line.

## Done in v0.1 (session 16)

- OFF reproduces M4: the owner's OFF run at 50,000 gave about -44k, session 9's M4 figure on
  that range and capital. The ON run at 500,000: 3,926 trades, -65,643.20, PF 0.802, read
  trade by trade against the M4 file (D-92).

## Checks for v0.2

1. **Compiles and the tester runs.** Report the first error line if not.
2. **ON, Deep Backtesting "Last 365 days" at 500,000, defaults.** Screenshot the Overview and
   export the list of trades; send the file. The exit column now has six words: T1, stop,
   half, be, trail, flat. The run is judged trade by trade against the M4 file, not on the
   headline (D-92).
3. **On the chart (normal range):** a navy line under a long (over a short) while the trade is
   open: flat at the first stop, a step up at the 1/2R tag, a step to the entry at the BE tag,
   then climbing candle by candle after the TRAIL tag. It never steps back. A trade stopped
   on the climbing part reads "trail" with its points.
4. **One trade by hand.** Pick a trade with a TRAIL tag. On any candle after it, the line
   should sit at the higher of: the last swing low (a low with five higher lows on each side)
   minus half the chart ATR, and that candle's close minus two chart ATRs, unless the
   previous stop was already higher. The chart ATR is the 14-candle ATR of the chart.
5. **Paper against Tester.** The info box: the Paper trades row counts T1, stop, half/be,
   trail and flat; the Tester rows within a few trades of it.
6. **Alerts.** Unchanged setup. STOP messages report every stop move with the stage.

## Report back

- The Overview and the exported list of the v0.2 run.
- Any trade whose navy line steps back, or whose "trail" exit sits far from the line.
