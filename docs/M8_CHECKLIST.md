# M8 checklist: the trade in his shape

**What changed.** Three things, all in D-115. The entry rests at the level instead of arriving a
candle later; the score stops gating at 50 on a number that runs backwards; and a trade now closes
when a candle closes back through the level, which is the source method's exit rather than a fixed
stop. Everything else is untouched.

**Before you start.** An existing chart keeps its saved settings, so after pasting either reset
the settings in the dialog or remove the strategy and add it again. The info box must read
`L2L M8 v0.1` and the tester tab `L2L M8 - Strategy`.

**Tester setup, unchanged:** Deep Backtesting, "Last 365 days DEEP", capital 500,000, 5-minute
MNQ, Central time. Properties needs nothing. Under Script execution, "On bar close" stays ticked.

## Checks

1. **It compiles.** If not, send the first error line exactly as TradingView prints it.
2. **The settings really reset.** "Reversal entry" should read *Limit at the level after the
   follow-through*, "Minimum score to signal" should be **0**, and "Close the trade when a candle
   closes back through the level" should be ticked.
3. **The trade count will move, and either direction is informative.** Fewer, because a resting
   order only fills if price comes back to the level. More, because the score is no longer
   throwing signals away. Somewhere between 300 and 700 is unremarkable; under 150 or over 900
   means something is behaving unexpectedly and I need the grey settings line.
4. **"void" appears in the list of trades.** Export it and check some exits read **void** rather
   than stop or T1. If none do, the new exit is not firing and that is a bug, not a result.
5. **Send the numbers:** total trades, net profit, profit factor, percent profitable, max drawdown,
   and the grey settings line.
6. **Export the list of trades and send the file.** Saved under `reference/backtests/<date>/`.

## How it will be judged

Against **run A**, not against the old baseline: 240 trades, profit factor 1.12, +1,279. Anything
inside roughly plus or minus 1,500 is noise, since the two halves of a year swing from +77 to
-1,503 on their own. The export is split in halves before anything counts (D-88).

The number to watch beyond the headline is **how the exits divide**. In M7, 73 % of trades died on
the stop. If "void" takes a large share of those and the per-trade result improves, the source's
reading was right and the fixed stop was the wrong instrument. If void exits are worse than the
stops they replaced, that is a real finding too and it goes in the log either way.
