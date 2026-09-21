# M6 checklist: the higher-timeframe rejection in the tester

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
4. **On the chart (normal range):** hover a reversal label with the label detail on Full: the
   details end with "HTF x/4". Pick one with HTF 2/4 or more and check by eye on the 15-minute
   or 1-hour chart that the last completed candle before the signal poked into the level and
   closed back with a long wick.
5. **Gate run, only if I ask for it after reading the file:** set "Reversals need at least"
   to the number I give, same range and capital, screenshot the Overview and export.

## Report back

- The Overview and the exported list of the base run.
- Any reversal whose HTF count looks wrong against the higher-timeframe chart.
