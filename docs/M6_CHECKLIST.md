# M6 checklist: the higher-timeframe rejection in the tester

**Status after sessions 18 and 19:** items 1 to 3 are done. The base run matched M4 exactly
and the export was read by count and in halves: the count makes the trades less bad over the
year but the halves disagree, and no gate is profitable on both halves (D-94). The HTF weight
stays 0 and the gate stays off. Items 4 and 5 are optional; the next decision is the owner's
(D-93 point 4, D-94 point 3).

Same paste as before. The info box must read `L2L M6 v0.1`. Settings group "Higher-timeframe
rejection (M6)": the count is on, the gate is off, the score weight for it is 0. The trade
manager's switch is now OFF by default.

## Checks

1. **Compiles and the tester runs.** Report the first error line if not.
2. **Same trades as M4.** Deep Backtesting "Last 365 days" at 500,000, defaults: 2,963
   trades, net -57,794.60, profit factor 0.84 (session 15). If not, report the grey settings
   line and the numbers.
3. **Export the list of trades** of that run and send the file. Every reversal's tag now ends
   with f0 to f4 before the window, for example "REV PDH+P4H s72 k2 h15 f2 NY". Break trades
   carry no f.
4. **Optional, on the chart (normal range):** hover a reversal label with the label detail on Full: the
   details end with "HTF x/4". Pick one with HTF 2/4 or more and check by eye on the 15-minute
   or 1-hour chart that the last completed candle before the signal poked into the level and
   closed back with a long wick.
5. **Optional gate run:** set "Reversals need at least" to 2, same range and capital
   (Deep Backtesting "Last 365 days", 500,000), screenshot the Overview and export. The
   export said -4,933 on 547 trades for that group; the tester run shows what the freed-up
   slots add. It tells whether the group is break-even, not whether it is a strategy.

## v0.2: the "Signals only" switch

Same paste. The info box must read `L2L M6 v0.2`.

1. **Compiles and runs with the switch off:** the tester shows the same trades as before
   (Deep Backtesting "Last 365 days" at 500,000: 2,963 trades, net -57,794.60).
2. **Switch on** (Signals group, "Signals only: labels, no trades"): the entry arrows, the
   stop line and the "in a long" text go; the Strategy Tester panel shows no trades; the info
   box's Tester row reads "signals only, no orders"; the signal labels stay, and more of them
   appear, because no running trade blocks the next setup.
3. **Switch off again:** the trades come back exactly as in step 1.

Report the first error line if it does not compile, and a screenshot of the chart with the
switch on.

## v0.3: the position visual

Same paste. The info box must read `L2L M6 v0.3`.

1. **Compiles and runs.** Report the first error line if not.
2. **At each signal:** a green box from the entry to the first target and a red box from the
   entry to the stop, lines at the entry, the stop and the targets, dotted lines at every
   0.5R up to the farthest target, and labels SL, E, T1, T2 and the R steps at the right end
   of the newest one. The newest runs to the right and follows price; when the next signal
   comes it stops at that bar and the new one starts.
3. **Older positions** stay behind with their labels moved to their start bar; only the last
   8 remain (setting "Positions kept").
4. **Trading mode** (Signals only off): Deep Backtesting "Last 365 days" at 500,000 still
   gives 2,963 trades, net -57,794.60; the visual changes no trade.
5. **The tester's arrows:** Style tab, untick "Trades on chart", then "Save as default" at
   the bottom of the settings window. They do not appear in Signals only mode at all.

Report a screenshot of a stretch with two or three signals.

## Report back

- Done: the Overview and the exported list of the base run (sessions 18 and 19).
- Optional: any reversal whose HTF count looks wrong against the higher-timeframe chart;
  the Overview and export of the gate run if it is made.
