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

## Report back

- Done: the Overview and the exported list of the base run (sessions 18 and 19).
- Optional: any reversal whose HTF count looks wrong against the higher-timeframe chart;
  the Overview and export of the gate run if it is made.
