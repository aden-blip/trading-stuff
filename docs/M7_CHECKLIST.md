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
