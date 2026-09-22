# M7 checklist: the method as described, run once

**What this is.** The first run of the strategy with the Socrates conditions on. Nothing in the
logic changed from M6 v0.5, only the defaults (D-101), so a compile error here would be a paste
problem, not a code problem.

**Before you start.** An existing chart keeps its own saved settings, so pasting the new script
alone changes nothing on it. After pasting, either open the settings dialog and reset it to
defaults, or remove the strategy from the chart and add it again. The info box must read
`L2L M7 v0.1` and the tester tab must say `L2L M7 - Strategy`.

**Tester setup, unchanged:** Deep Backtesting, "Last 365 days DEEP", capital 500,000, 5-minute
MNQ chart, Central time. Nothing to set in the Properties tab: the costs and the margin are
written into the script. Under Script execution, "On bar close" stays ticked and the other three
stay unticked.

## Checks

1. **It compiles and the tester runs.** If not, report the first error line exactly as it reads.
2. **The settings really reset.** In the info box, "Levels" should show far fewer than before.
   In the settings, the 4-hour group should be four unticked boxes, "Entries only inside the
   checked windows" ticked with only New York ticked under it, "Max trades per day" 4 and "Max
   losing trades per day" 2, "Volume confirmation" On, "Reversal stop" Beyond the rejection wick,
   "Stop no wider than" 0.03, "Minimum target distance" 0.03. If any of those still read the old
   value, the settings did not reset.
3. **The trade count is much smaller.** Expect somewhere around 250 to 450 trades for the year
   instead of 2,963. A number near 2,963 means the settings did not reset; a number under about
   80 means something is blocking nearly everything and I need the grey settings line plus the
   info box to find out which condition.
4. **Entries only between 09:00 and 15:00 Central.** Spot-check a handful of entry arrows. An
   entry at 17:00, 21:00 or 03:00 means the session window is not on.
5. **No more than four trades on any day, and never a third loss in a day.** Scroll a few busy
   days in the list of trades.
6. **Send the numbers:** total trades, net profit, profit factor, percent profitable, max
   drawdown, and the grey settings line under the chart title.
7. **Export the list of trades and send the file.** This is the part that decides anything: I
   split it in halves and nothing counts unless both halves agree (D-88). Saved under
   `reference/backtests/<date>/` with its readout.

## What I expect, so we read it honestly

The trade count will be thin, which means one half of the year can look good by luck. A profit
factor near or above 1.0 on both halves would be the first time that has happened and would tell
us the conditions carry the trigger. A profit factor well under 1 on both halves tells us the
trigger itself is the problem even with his conditions on, and the next work is the two
information sources the method names that the script does not have: the VIX and the split between
buying and selling volume (D-100 point 8).

Either way the export goes into `docs/BACKTEST_LOG.md` as session 21 before anything else
changes.

---

# Predictions for runs A and B, written before the runs (D-102 point 7)

Recorded so the results can be checked against them instead of explained after the fact.

## Run A — reversals need at least 2 higher-timeframe rejections

Replaying the gate over the 417-trade export removes 177 reversals and leaves 240 trades:
240 trades, win 30.0 %, PF 1.12, net +1,279, +5.33 a trade, closed-trade drawdown 1,191.
H1 PF 1.28 (+1,225), H2 PF 1.01 (+54).

**Predicted: 240 to 280 trades, PF 1.05 to 1.20, net between +800 and +1,600.**

240 is a floor, not a forecast, because the tester holds one position at a time and caps the day
at four trades and two losses. Skipping a reversal frees the strategy to take a later signal that
was blocked, and removing about 84 losing f1 trades means fewer days trip the two-loss cap. Trades
are short (winners hold about two candles) and the day averages 1.7 trades against a cap of 4, so
the effect should be small.

**What would mean something is wrong:** fewer than 240 trades (the gate cannot remove a break, and
breaks alone are 169), more than about 320 (the freed-up signals would be doing more work than the
gate), or a profit factor under 1.0 (the gate would not have survived its own out-of-sample test).

## Run B — run A plus the stop to the entry after half an R

**No prediction. The outcome turns on a number the export cannot show, and it swings the result
from good to worse than run A.**

The stop arms once a trade is half an R in profit. 35 % of the losers in the gated set ran that far
in profit before being stopped, which is where the gain comes from. The cost is winners that reach
half an R, trade back through the entry, and then go on to the target: those get scratched instead
of paid. Every winner in the set traded back past its entry at some point, so the whole question is
whether that happened before or after the run-up, and the export records only how far price went,
never in what order.

| Winners scratched | Win % | PF | Net | Max DD | H1 | H2 |
|---|---|---|---|---|---|---|
| 0 % (the ceiling) | 30.0 | 1.61 | +4,555 | 611 | +2,566 | +1,989 |
| 10 % | 27.1 | 1.27 | +1,996 | 1,492 | +2,406 | -410 |
| 20 % | 24.2 | 1.14 | +1,095 | 1,515 | +1,879 | -784 |
| 30 % | 20.8 | 1.00 | -2 | 1,981 | +1,273 | -1,275 |
| 40 % | 17.9 | 0.79 | -1,635 | 2,903 | +656 | -2,291 |

Run A alone is +1,279, so **the stop only pays above about a 15 % scratch rate in the wrong
direction**: past roughly one winner in seven it is worse than doing nothing, and past three in ten
it is worse than the baseline. The second half turns negative at a 10 % scratch rate, so even the
halves test is fragile here.

The mechanical guess is a low rate. Winners hold about two candles, the median winner makes 33
points and half an R is about 8, so a scratch needs price to run 8 points, return through the entry
and then make 33, inside one or two 5-minute candles. The usual shape is a dip first and then the
run, which never arms the stop. But that is a guess about order, and the run is what settles it.

**How to read the result:** compare run B against run A, not against the baseline. Better than
+1,279 on both halves and the stop stays. Worse on either half and it comes back off, and the
ceiling in D-102 point 3 is recorded as unreachable.
