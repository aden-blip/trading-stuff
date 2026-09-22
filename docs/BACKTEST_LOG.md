# Backtest Log

One entry per backtest session, newest first. The point is to see how each version behaved, what
broke, and what changed between sessions, so problems can be diagnosed instead of guessed at.
Fill every field; write "not measured" rather than leaving one blank.

Template:

```
## YYYY-MM-DD  Session N  (script version, e.g. M4 v0.1)

Symbol / timeframe / date range:
Costs used (commission per side, slippage ticks):
Settings changed from defaults:

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

By setup: REV trades / win % / net P&L vs BRK trades / win % / net P&L:
By level type (top 3 and bottom 3 by net P&L):
By session (Asia / London / New York) where relevant:

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):

Issues found (bugs, repainting, alerts, drawing problems):

Changes made before the next session (setting or code, and why):

Screenshots or trade list attached under reference/backtests/<date>/ :
```

---

## 2026-09-22  Session 21  (M7 v0.1)

Symbol / timeframe / date range: MNQ1! 5-minute, Deep Backtesting "Last 365 days DEEP", 500,000
capital, Central time.
Costs used (commission per side, slippage ticks): 0.80 cash per contract per side, 2 ticks
slippage, 2 contracts. 7.20 USD a round-trip trade.
Settings changed from defaults: none. This is the first run of the M7 v0.1 defaults, which are
the method as described (D-101): levels only where price has already turned, New York only,
opening blackout on, four trades and two losses a day, volume confirmation on, the first target
at the nearest level, the stop at the rejection wick with the cap at 0.03 daily ATR.

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 417 | 26.62 | 0.93 | -1,426.40 | 3,842.00 (0.77 %) | not measured | not measured | not measured |

By setup: REV 248 trades, 26.2 % win, -1,263 USD; BRK 169 trades, 27.2 % win, -164 USD. In
halves, breaks are the unstable half: H1 PF 1.20 (+701), H2 PF 0.80 (-864). The on-chart paper table (a different and much shorter sample, 123
trades over 73 days) reads REV 65 trades, 23 % reaching the first target, +133.75 points, and
BRK 58 trades, 19 %, -79.25 points. That is the opposite of the year's finding in D-99 point 6,
which is exactly why a 73-day paper sample decides nothing.
By level type (top 3 and bottom 3 by net P&L): best Asia high +678, London low +453, previous
week low +252; worst Asia low -1,040, previous day low -998, three-touch SR -781. Only London
low is positive in both halves with a steady profit factor (1.16 and 1.17).
By session (Asia / London / New York) where relevant: New York 123, Asia 0, London 0, other
hours 0 in the paper table, so the session window is working as intended.

How it reacted: the trade count fell from 2,963 to 417, inside the 250 to 450 predicted in D-101
point 5, so the settings reset took. The average stop in the paper table is about 19.5 points
against 52 to 63 on the old default, so the wick stop and the cap are both binding. The first
target is reached on 21 % of paper trades at an average of +65.75 points against an average stop
of -19.50, a payoff over 3 to 1, where the old default reached its target on 23 % at a much wider
stop.

**The headline: this is the first gross-positive run.** Net -1,426.40 over 417 trades is -3.42 a
trade; costs are 7.20 a trade, or 3,002.40 over the run, so before costs the year made +1,576.00,
about +3.78 a trade. Every previous configuration lost money before costs as well as after
(D-99 point 1: -12.3 a trade raw). The trigger plus the method's conditions is the first
combination that has ever had a positive raw edge.

Two readings from the paper table that the export needs to confirm or kill:
- A single level in the zone beat stacked levels: 96 trades at +323.75 points against 20 trades
  at -246.50 for two levels. If that holds in the tester it contradicts the stack component of
  the score, which pays more for stacked zones.
- The score does not rank: 6/10 and 7/10 are positive, 5/10 or less and 8/10 or more are
  negative. Consistent with D-85 and D-100 point 6, that the score is dead weight.

Issues found: none. The script compiled, the version markers read L2L M7 v0.1, the session
filter held, and no drawing or alert problem was reported.

Changes made before the next session (D-102 point 7): two runs, one change each. Run A sets
"Reversals need at least this many" to 2. Run B is run A plus the trade manager on with both
stages at 0.5 R and the trail set out of reach, which is a plain stop to the entry after half an
R. Wednesday is the next single change after those two; the first code item stays the VIX.

Screenshots or trade list attached under reference/backtests/<date>/ : `2026-09-22/` holds the
screenshot's numbers, `trades_M7v0.1_method_deep-365d_500k.csv`, `report_M7v0.1_deep-365d.md`,
`compare_M7v0.1_halves.md` and `findings_M7v0.1.md`.

**Export read (D-102).** Halves at 2026-03-20: H1 210 trades PF 1.01 (+77), H2 207 trades PF 0.87
(-1,503). What survives both halves: reversals with two or more higher-timeframe rejections, 71
trades at PF 1.49 and +20.32 a trade, the halves giving +19.07 and +21.24, the steadiest slice in
any export so far; exactly one rejection is the worst group in the file and loses in both halves.
The breakeven stop after half an R is the largest lever, taking the whole set from -1,426 to a
ceiling of +6,317 with the drawdown falling from 3,834 to 1,158 and both halves strongly positive
(losers exact, winners assumed never scratched, so the real number is lower). The score is
inverted: its lowest band is the only profitable one. Single-level zones beat stacked ones.
Wednesday loses in both halves for the third sample running. Partial exits and a closer target are
both worse than as traded.

---

## 2026-09-22  Session 20  (M6 v0.4/v0.5, run A of D-98: the stop cap alone; screenshot, export awaited)

Symbol / timeframe / date range: MNQ1!, 5-minute, Deep Backtesting "Last 365 days" at
22:41 CT [23:41 NY] on 21 Sep. One screenshot of the Key stats panel plus the chart's paper
breakdown table (chart range: 74 trading days since 7 Jun 2026, the same window as the
session 13 screenshot, so the paper rows compare directly). The list of trades not yet
exported.
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, 2
contracts, initial capital 500,000. Script execution: on bar close only (bar magnifier off).
Settings changed from defaults: "Stop no wider than, daily ATR" 0.03 with a 40-tick floor
(run A of D-98). Everything else default: manager off, HTF count on with weight 0 and gate
off, reversal entry at the close of the follow-through candle, reversal stop beyond the zone,
filters off.

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| not measured (export awaited) | not measured | 0.823 (base 0.836) | -59,501.60 USD, -11.90 % (base -57,794.60) | 61,949.80 USD, 12.39 % (base 63,402.00) | not measured | not measured | not measured |

By setup / by level type / by session: not measured until the export arrives.

Paper breakdown table, same 74-day chart window as session 13, cap on against cap off:
| Group | Trades | T1 % | Avg T1 | Avg stop | Points |
|---|---|---|---|---|---|
| All, cap off | 825 | 23 % | +135.00 | -52.00 | -2,026.00 |
| All, cap on | 1,662 | 11 % | +127.75 | -19.25 | -3,131.00 |
| REV, cap off | 681 | 24 % | +136.75 | -59.50 | -2,442.75 |
| REV, cap on | 1,449 | 10 % | +129.75 | -19.00 | -3,236.25 |
| BRK, cap off | 144 | 15 % | +123.00 | -22.50 | +416.75 |
| BRK, cap on | 213 | 13 % | +117.25 | -19.75 | +105.00 |

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
1. **The cap works as specified.** The average stop fell from 52 to 19 points, and 0.03 of the
   daily ATR is about 19 points on MNQ at the moment, so the cap is binding on nearly every
   trade and the 40-tick floor never had to.
2. **The hit rate fell with it, to the coin-flip rate.** The share reaching the first target
   went from 23 % to 11 %. D-97 predicted exactly this from the export replay: the reward
   stayed near 128 points while the risk fell to 19, so the break-even hit rate rose above
   what the entry delivers. The measured 11 % is the stop over stop plus target rate of a
   random entry with this geometry.
3. **Per trade less bad, in total worse, because the trades doubled.** On the same 74 days
   the paper tally went from 825 trades at -2.46 points a trade to 1,662 at -1.88. A quick
   stop frees the bot for the next setup, and every setup loses on average, so the year
   reads -59,501.60 against the base -57,794.60. This is the D-93 pattern again, the one the
   staged manager produced: a better trade and a worse year.
4. The export replay of D-97 said a 12-point stop on the same entries would be -24,075. The
   tester says -59,501.60 on the freed-up trades. The gap between the two is the cost of the
   extra trades the replay could not show, and it is the whole reason the tester run was
   needed.

Issues found (bugs, repainting, alerts, drawing problems): none. Script execution shows "on
bar close" locked on and the three optional recalculation modes off, as intended.

Changes made before the next session (setting or code, and why): none yet. Next: the export
of this run for the split by setup, hour and level type, then runs B and C of D-98, the two
limit-at-the-level entries with the wick stop and the same cap. The cap alone is not the fix,
as the replay warned; the entry is still the thing under test.

Screenshots or trade list attached under reference/backtests/<date>/ : screenshot in the chat;
the export, when it comes, goes under `reference/backtests/2026-09-22/`.

---

## 2026-09-21  Session 19  (M6 v0.1, the exported list of the base run, read by higher-timeframe count and in halves)

Symbol / timeframe / date range: MNQ1!, 5-minute, Deep Backtesting "Last 365 days", trades
from 21 Sep 2025 21:25 to 18 Sep 2026 13:50 CT [22:25 NY to 14:50 NY]. The 2,963 closed
trades are the M4 export of session 15 trade for trade: every month has the same count and
the same net, the 687 break trades match one for one by time and tag, and the reversal
tags differ only by the new count (f0 to f4) before the window. The file's last trade,
number 2,964, was still open when the list was exported and is left out;
`tools/trade_list_report.py` now skips an open trade instead of stopping on it. File and
readouts saved under `reference/backtests/2026-09-21/`
(`trades_M6v0.1_base_deep-365d_500k.csv`, `report_M6v0.1_deep-365d.md`,
`compare_M6v0.1_halves.md`). Halves as in session 15: to 20 Mar 2026 (1,609 trades) and
from 21 Mar (1,354).
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, 2
contracts, initial capital 500,000.
Settings changed from defaults: none (manager OFF, HTF count on, HTF weight 0, gate off).

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 2,963 | 26.46 % | 0.84 (halves 0.84 and 0.84) | -57,794.60 USD, -11.56 % of 500,000; -19.51 a trade | 63,245.40 USD closed-trade | 375.81 USD | 161.74 USD | median 6 candles; winners 13, losers 4 |

By setup: REV 2,276 trades, 30 %, PF 0.83, -54,810; BRK 687, 15 %, 0.92, -2,984 (as session 15).
By level type / by session / by hour / by month: the same trades as session 15, not re-read.
By higher-timeframe count (reversals only). The count is how many of the last completed
5-minute, 15-minute, 1-hour and 4-hour candles before the signal poked into the zone,
closed back on the approach side and left a wick of at least 0.4 of their range. On the
5-minute chart the 5-minute candle in that check is the rejection candle of the signal's
own two-candle pattern, so a count of 1 mostly says "the rejection candle had a long
wick"; the higher-timeframe test proper is a count of 2 or more. The export carries the
total only, not which candles counted.
| Count | Trades | Win % | PF | Net USD | USD a trade | First half PF / net | Second half PF / net |
|---|---|---|---|---|---|---|---|
| 0 of 4 | 675 | 29.8 % | 0.80 | -19,619 | -29.1 | 0.91 / -3,295 | 0.74 / -16,324 |
| 1 of 4 | 1,054 | 29.1 % | 0.79 | -30,258 | -28.7 | 0.80 / -11,994 | 0.78 / -18,264 |
| 2 of 4 | 441 | 30.8 % | 0.91 | -5,568 | -12.6 | 0.77 / -5,564 | 1.00 / -4 |
| 3 of 4 | 99 | 36.4 % | 1.11 | +1,317 | +13.3 | 0.96 / -256 | 1.28 / +1,573 |
| 4 of 4 | 7 | 28.6 % | 0.47 | -682 | -97.5 | 0.13 / -657 | 0.95 / -26 |

As a gate would take them ("Reversals need at least" N of 4):
| At least | Trades | Win % | PF | Net USD | First half: trades, PF, net | Second half: trades, PF, net |
|---|---|---|---|---|---|---|
| 1 | 1,601 | 30.0 % | 0.84 | -35,191 | 818, not measured, -18,471 | 783, not measured, -16,721 |
| 2 | 547 | 31.8 % | 0.93 | -4,933 | 283, 0.79, -6,477 | 264, 1.04, +1,543 |
| 3 | 106 | 35.8 % | 1.05 | +635 | 64, 0.86, -913 | 42, 1.25, +1,548 |
The reversals a gate of 2 would drop (count 0 or 1): 1,729 trades, PF 0.80, -49,877 (0.84 /
-15,289 and 0.76 / -34,588 by half).
Count 2 or more by month: positive in five months (Jan +349, Apr +162, May +2,128, Jun
+2,548, Aug +1,195) and negative in eight; February (-3,076) and March (-3,418) together
lose more than the group's whole year. Count 2 or more by window: Asia 82 trades, PF 1.36,
+3,603; London 54, 0.99, -62; New York 223, 0.74, -8,860; other hours 188, 1.02, +385. New
York is the loser inside this group as it is in the whole sample (0.79).

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
1. Over the year the count makes the reversals less bad in a straight line: PF 0.80, 0.79,
   0.91 and 1.11 for counts 0 to 3, and -29, -29, -13 and +13 USD a trade. The halves do
   not agree on that order. First half: 0.91, 0.80, 0.77, 0.96, so a count of 2 did worse
   than a count of 0; second half: 0.74, 0.78, 1.00, 1.28, in order. Under the rule of
   D-88 and D-93 (a finding counts only when both halves agree) the count does not
   separate the trades.
2. As a gate, "at least 2" keeps 547 of the 2,276 reversals and takes the year from
   -54,810 to -4,933 (PF 0.93), but it is -6,477 (0.79) in the first half and +1,543
   (1.04) in the second: less bad, not good, and only in one half. "At least 3" is +635
   on 106 trades, -913 then +1,548 by half, about two trades a week and a loser in the
   first half. Neither clears the bar for the weight or the gate.
3. A count of 4 is seven trades, too few to read.
4. What is stable across every reading of this year (sessions 15, 16, 17 and 19): the
   payoff of a level rejection on MNQ 5-minute stays near two to one and the hit rate a
   few points under what that payoff needs to break even, whichever way the trades are
   sliced (score, stack, level history, window, hour, level type, higher-timeframe
   count, and the managed stops). Only removal filters change it, and none of them into a
   profit on both halves.

Issues found (bugs, repainting, alerts, drawing problems): none in the trades. The readout
tool stopped on the open last trade (fixed). The chart check of a few labels against the
15-minute and 1-hour charts (M6 checklist item 4) was not done; the count is read here from
the tags only.

Changes made before the next session (setting or code, and why): none to the script. D-94:
the HTF weight stays 0 and the gate stays off; the M6 concept is measured and the next
decision is the owner's (D-93 point 4): the instrument, the timeframe, or the trigger. The
cheapest tests need no code change (the same script on the MNQ 15-minute chart, or on MCL),
and they are the owner's to pick. The one check still open on M6 itself is optional: a gate
run at "at least 2" to confirm the -4,933 on the tester, since a skipped signal frees the
strategy for trades the export cannot show; it tells whether that group is break-even, not
whether it is a strategy.

Screenshots or trade list attached under reference/backtests/<date>/ : the export and both
readouts are saved under `reference/backtests/2026-09-21/`; the screenshots of the run are
with session 18.

---

## 2026-09-21  Session 18  (M6 v0.1, base run: the M4 trades with the higher-timeframe count in the tag; screenshots only)

Symbol / timeframe / date range: MNQ1!, 5-minute, Deep Backtesting "Last 365 days" at
00:12 CT [01:12 NY] on 21 Sep; the window has moved one day since the M4 export of session
15, so the first trades of the range differ slightly. Two screenshots (Overview, Performance
analysis with the by-signals panel); the list of trades not yet exported.
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, 2
contracts, initial capital 500,000.
Settings changed from defaults: none (manager OFF, HTF count on, HTF weight 0, gate off).

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 2,963 (M4: 2,963) | 26.46 %, 784 won (M4: 784) | 0.836 (M4 0.84) | -57,783.20 USD, -11.56 % (M4 -57,794.60); -19.51 a trade | 63,402.00 USD, 12.58 % | not measured | not measured | not measured |

Gross profit 294,632.20, gross loss 352,428.40, commission load 3.22 %, outliers 78,140.80
(15.63 %), largest profit 3,064.80, largest loss 872.20, buy and hold +20.94 %. The
by-signals panel shows the new tags, for example "REV NL s62 k1 h3 f0 ASIA" and "REV 4HO s51
k1 h6 f2 ASIA": the count is in the export's Signal column.

By setup / by level type / by session / by higher-timeframe count: not measured until the
export arrives.

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
As intended, the M6 v0.1 base is the M4 strategy: the same 2,963 trades and 784 winners,
eleven dollars apart over the year from the moved window. The split by the higher-timeframe
count is the whole point of the run and waits for the file.

Issues found (bugs, repainting, alerts, drawing problems): none reported; the chart was not
screenshotted.

Changes made before the next session (setting or code, and why): none. Next: the export of
this run, read with `tools/trade_list_report.py` (by count and cumulative) and
`tools/compare_trade_lists.py` (both halves); the weight and the gate follow only if the
count separates the trades on both halves (D-93).

Screenshots or trade list attached under reference/backtests/<date>/ : screenshots in the
chat; the export, when it comes, goes under `reference/backtests/2026-09-21/`.

---

## 2026-09-21  Session 17  (M5 v0.2, stages plus the trail, Last 365 days at 500,000; screenshots only)

Symbol / timeframe / date range: MNQ1!, 5-minute, Deep Backtesting "Last 365 days", 21 Sep
2025 to 18 Sep 2026 CT. Two screenshots (Overview, Performance analysis); the list of trades
was not exported, so the same-entries comparison of D-92 is outstanding.
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, 2
contracts, initial capital 500,000.
Settings changed from defaults: none (manager on: 0.5R half, 1R breakeven, 1.5R trail, swing
5 candles, 0.5 and 2.0 chart ATRs).

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 4,208 (v0.1 3,926, M4 2,963) | 24.33 %, 1,024 won | 0.814 (v0.1 0.802, M4 0.84) | -65,874.60 USD, -13.17 %; -15.65 a trade (v0.1 -16.72, M4 -19.51) | 71,219.80 USD, 14.22 % | not measured | not measured | not measured |

Gross profit 287,461.20, gross loss 353,335.80, commission load 4.68 %, outliers 104,718.80
(20.94 %), largest profit 1,325.80 (M4 3,064.80: the trail cut the year's biggest runner),
largest loss 818.20, buy and hold +19.96 %. Best five signals shown by the tester: +1,137.80,
+1,116.60, +1,112.80, +1,093.00, +1,082.20; the other 3,132 signal groups -71,417.00.

By setup / by level type / by session: not measured (no export).

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
The trail added 282 trades over v0.1 and 231 USD of loss; per trade it is the least bad of the
three (-15.65 against -16.72 and -19.51), and the total is the same. The winners it makes
are small: the largest profit fell from 3,064.80 to 1,325.80 because a trail two chart ATRs
behind the close cannot ride a trend day. On the year's numbers the manager with the trail
does not beat the hard-target trades: -65,875 against -57,795. The same-entries reading (the
file) is still owed, but nothing in the headline suggests it clears the D-92 bar: the trail
would have to be worth more than the 23,807 the extra trades cost, and the per-trade gain
over v0.1 is about one dollar.

Issues found (bugs, repainting, alerts, drawing problems): none reported; chart not
screenshotted, so the navy stop line and the TRAIL tags are unchecked.

Changes made before the next session (setting or code, and why): D-93. The manager's switch
goes OFF by default (the code stays, all inputs stay), and the work moves to the entries:
M6 v0.1 counts, for every reversal, the higher-timeframe candles that rejected the zone and
writes the count into the tag, so one export at defaults splits the trades by it.

Screenshots or trade list attached under reference/backtests/<date>/ : screenshots in the
chat of 2026-09-20 (owner's clock); the v0.2 export, when it comes, goes under
`reference/backtests/2026-09-21/`.

---

## 2026-09-21  Session 16  (M5 v0.1, staged stops, Last 365 days at 500,000; the OFF check and the ON export)

Symbol / timeframe / date range: MNQ1!, 5-minute, Deep Backtesting "Last 365 days", trades
21 Sep 2025 to 18 Sep 2026 CT. Files under `reference/backtests/2026-09-21/`:
`trades_M5v0.1_stages_deep-365d_500k.csv`, `report_M5v0.1_deep-365d.md`, and the trade-by-trade
comparison with the M4 run `compare_M4_M5v0.1.md` (tool `tools/compare_runs.py`, matching on
entry time and tag).
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, 2
contracts, initial capital 500,000 for the ON run.
Settings changed from defaults: none for the ON run (manager on, halve the risk at +0.5R,
breakeven at +1R, cushion 2 ticks or 0.02 execution ATRs). The OFF check was run at 50,000 (the
owner's report: "about -44k"), which is session 9's M4 figure on that range at that capital
(-44,558.40, the account hits the margin floor in June), so the switch OFF reproduces M4.

Headline stats (ON):
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 3,926 (M4: 2,963) | 18.24 %, 716 won | 0.802 (M4 0.84) | -65,643.20 USD, -13.13 %; -16.72 a trade (M4 -19.51) | 68,240.00 USD, 13.61 % | 371.64 USD | 103.35 USD | median 4 candles, winners 10, losers 3 |

Gross profit 266,095.80, gross loss 331,739.00, commission load 4.72 %, outliers 110,188.20
(22.04 %), largest profit 3,064.80, largest loss 734.20, buy and hold +19.96 %. Exits: T1 633
(+240,569), stop 1,528 (-246,898), half 738 (-77,965, -26 points each), be 932 (-4,713, -5 USD
each), flat 95 (+23,363). The tester's "breakevens" reads 0 because every scratch carries costs.

By setup: REV 3,140 trades, 20.3 %, PF 0.81, -57,979; BRK 786, 10.1 %, 0.74, -7,664.
By level type / by session: as the M4 readout, nothing new; the monthly table in the
comparison file: the manager helped December (-8,413 to -3,757), February (-11,995 to -7,405)
and July (-18,304 to -12,049) and hurt March, April, May, August.

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
1. On the same entries the stages help a little. 2,671 trades appear in both runs (same entry
   time and tag). As M4 traded them: -52,188. As M5 traded them: -41,836, +10,352. The half
   stage: 482 exits; 412 of them were M4 stops (saved 39,447), 52 were M4 winners (cost
   27,492), 18 were flats (cost 2,937): +9,018. The breakeven stage: 611 exits; 445 M4 stops
   (saved 60,107), 126 M4 winners (cost 52,429), 40 flats (cost 6,344): +1,334, a wash. In
   all the stages saved 99,554 on losers and gave back 89,202 on winners; the M4 export's
   ceiling (+59,412) counted only the first half of that.
2. The extra trades eat it. Scratching early frees the strategy, and it took 1,255 trades the
   M4 run could not take: -23,807 at -19.0 a trade, the same rate as every other trade (292
   M4 trades disappeared, worth -5,606). Net: -65,643 against -57,795. The manager makes the
   same trade about 20 % less bad; the entries lose on average, so more of them is worse.
3. Where the breakeven stage loses: the entries that ran two stops or more in profit in the
   M4 run and came back to the entry. 323 of the 611 breakeven exits; M4 made +33,706 on them
   (110 reached the target, the rest ran and stopped out), M5 scratched all of them. The
   entries that ran less than two stops before coming back: 264 trades, M4 -34,969, M5
   scratched. So the breakeven stop pays on the small runs and costs on the big ones, and
   the missing piece is the third stage of D-32, the trail, which keeps part of a big run
   instead of giving it all back.
4. A wait after an exit is not a fix. Trades entered 5 to 15 minutes after the previous exit
   lose at the same rate as trades entered two hours later (PF 0.82 to 0.83 either way), so a
   wait only trades less. Not built.

Issues found (bugs, repainting, alerts, drawing problems): none reported; the chart itself
was not screenshotted, so the navy stop tags and the info box rows are unchecked.

Changes made before the next session (setting or code, and why): D-92. M5 v0.2 adds the
third stage, the trail (+1.5R: the stop follows the higher of the last confirmed swing and a
chase stop two execution ATRs behind the close), a "trail" exit tag, and a plotted line of the
stop in force. Thresholds unchanged. The v0.2 run is judged on the same-entries comparison
against the M4 file, not on the headline alone.

Screenshots or trade list attached under reference/backtests/<date>/ : saved, see above.

---

## 2026-09-21  Session 15  (M4 v0.5, the 365-day exported trade list, split in halves)

Symbol / timeframe / date range: MNQ1!, 5-minute, Deep Backtesting "Last 365 days", trades
from 21 Sep 2025 21:25 to 18 Sep 2026 13:50 CT [22:25 NY to 14:50 NY]. 2,963 trades against
2,510 in session 9: that run at 50,000 hit the margin floor in June, this one at 500,000
trades the whole year. The trades in the overlap with the chart-range run are not the same
set (the level ranks accumulate from the start of the data). File and readouts saved under
`reference/backtests/2026-09-21/` (`trades_M4v0.5_defaults_deep-365d_500k.csv`,
`report_deep-365d.md`, `compare_365d_halves_summer.md`); the halves split is
`tools/compare_trade_lists.py`. Halves: to 20 Mar 2026 (1,609 trades) and from 21 Mar
(1,354).
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, 2
contracts, initial capital 500,000.
Settings changed from defaults: none.

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 2,963 | 26.46 % | 0.84 (halves 0.84 and 0.84) | -57,794.60 USD, -11.56 % of 500,000; -19.51 a trade, -4.1 points a trade | 63,245.40 USD closed-trade | 375.81 USD | 161.74 USD | median 6 candles; winners 13, losers 4 |

Exits: 689 at the target (median 89 points), 2,142 at the stop (median 34 points), 132
flattened (95 in profit, +25,347).

By setup: REV 2,276 trades, 30 %, PF 0.83 (0.83 / 0.82 by half), -54,810; BRK 687, 15 %,
0.92 (0.86 / 0.99), -2,984.
By level type: 4-hour open the worst in every sample, 620 trades, PF 0.65 (0.71 / 0.61),
-27,174; daily open -11,438 (0.77 / 0.67); previous 4-hour high -8,608; London high -8,143;
Monday mid -8,114; weekly open -7,262; previous week mid -6,701 (PF 0.42); New York open
-6,847. The 4-hour family -38,401 on 1,539 trades, PF 0.80 in both halves; zones holding a
4-hour open PF 0.74 in both halves against 0.88 without. Positive in both halves: the New
York low, +6,047 (1.70 / 1.39). The summer winners (previous 4-hour mid, midnight open) are
losers or flat over the year.
By session (Asia / London / New York) where relevant: New York 1,268 trades, PF 0.79
(0.83 / 0.75), -33,396; Asia 0.90 (0.72 / 0.98), -5,028; London 0.88 (0.90 / 0.85); other
hours 0.86 (0.86 / 0.87). The summer's Asia edge is gone. By hour, losing in both halves:
08:00-09:59 CT [09:00-10:59 NY] -20,173; 13:00 -6,653; 17:00-18:59 [18:00-19:59 NY], the
Globex reopen, -15,034; 21:00 -7,559. Winning in both halves: 04:00, +3,178. Wednesday
-27,196, PF 0.65 (0.70 / 0.62); the other five days -30,600 between them.
By level history: h15 -39,998 (PF 0.75 / 0.79), h6 -13,586 (0.69 / 0.84), h3 -3,190
(1.05 / 0.91), h12 -1,020 (break trades). Correction to session 14: the verdicts are judged
on 5-minute closes (the "Verdict closes on" input, 5), so the rejection candle itself
usually records the "held" verdict before the follow-through signal: 989 of the 1,215
held-tagged reversals were the first trade at their zone that day. The tag mostly says
whether the rejection candle closed at least the hold distance away from the level (h15) or
not (h6), or whether the level broke earlier today (h3); it is not "a second test of a level
that already held". The direct test of that idea: a reversal after a losing trade at the
same zone earlier that day, 403 trades, PF 0.85, the same as first trades (0.83); after a
winning trade at the same zone that day, 56 trades, PF 0.49 (0.66 / 0.29), too few to act on.
By score and by stack: noise, the halves disagree (60s +3,335 then -12,400; 70s -14,983
then +707; 90s +5,006 then -8,774). Retries within two hours: PF 0.94 against 0.83 for first
attempts, the summer reading did not hold.
By month: December -8,413, February -11,995, March -10,075 and July -18,304 carry
-48,786 (PF 0.66 on 992 trades); the other eight months together -9,008 (PF 0.96 on 1,971).

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
1. Stable in every sample: 47 % of losing trades were half a stop in profit first, 26 % a
   full stop, 17 % one and a half stops (26 / 27 / 27 % at a full stop by sample). The
   losers that had reached a full stop in profit cost 79,138 USD over the year, more than
   the whole loss. The other side is just as stable: 47 % of winners went half a stop
   against first and 18 % a full stop against before winning.
2. Exact what-ifs in R (the trade's own stop for stop-outs, the month's median stop for the
   rest): every one is worse. Target at 1R / 1.5R / 2R / 3R: -89,892 / -88,297 / -69,131 /
   -50,476. Stop at 0.5R / 0.75R: -60,384 / -88,676. One contract off at +0.5R / +1R:
   -57,244 / -73,843. Ceilings with the losers exact and the winners untouched: the D-32
   stages (stop to -0.5R after +0.5R, to entry after +1R) +59,412 with a closed-trade
   drawdown of 6,393, positive in both halves (+24,933 / +34,479); breakeven after +1R
   +18,358; after +1.5R -16,500. What the stages cost on winners the export cannot show and
   only the script can measure.
3. Removal-only filters that hold in both halves make it less bad, not good: no entries
   08:00-09:59 and 17:00-18:59 -22,587 (PF 0.90; halves 0.82 / 0.97); that plus no zones
   with a 4-hour open -8,950 (0.95; -10,001 / +1,052); no zones with any 4-hour level
   -19,394 (0.88 / 0.89). The best of them is break-even in one half and a loser in the
   other, on half the trades.
4. Without the ten best trades the year is -73,321; without the fifty best -107,192. 307
   days traded, 129 positive; the worst 28 Jul -3,448, 29 Jul -3,047, 24 Jun -2,938, 21 Nov
   -2,901.

Issues found (bugs, repainting, alerts, drawing problems): none in the trades.

Changes made before the next session (setting or code, and why): none to the script. D-91:
the trade manager (M5) is built next, the level-history switch of D-90 is withdrawn, and the
hour and level-type filters wait to be re-read on the managed trades.

Screenshots or trade list attached under reference/backtests/<date>/ : the export and both
readouts are saved under `reference/backtests/2026-09-21/`.

---

## 2026-09-21  Session 14  (M4 v0.5, the exported trade list of the chart-range run read trade by trade)

Symbol / timeframe / date range: MNQ1!, 5-minute, 7 Jun 2026 20:25 to 18 Sep 2026 13:45 CT
[21:25 NY to 14:45 NY], the same 769 trades as sessions 7 and 13, exported from the tester as a
list of trades (two rows a trade: entry with the v0.5 tag, exit with T1 / stop / flat, and each
trade's run-up and drawdown). File and full readout saved under `reference/backtests/2026-09-21/`
(`trades_M4v0.5_defaults_chart-range_50k.csv`, `report_chart-range.md`), produced by
`tools/trade_list_report.py`, which any later export runs through unchanged.
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, 2
contracts, initial capital 50,000. Money figures below are for the 2 contracts (4 USD a point);
points are per contract.
Settings changed from defaults: none.

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 769 | 26.79 % | 0.864 | -16,929.80 USD, -22.02 a trade, -4.7 points a trade | 23,946.80 USD closed-trade (tester 24,103.40 with open trades) | 522.55 USD | 221.27 USD | median 9 candles, mean 20; winners median 20, losers median 6 |

Exits: 172 at the target (median 124 points, mean 137), 555 at the stop (median 48.5 points,
mean 55), 42 flattened at 15:55 CT [16:55 NY] of which 34 in profit (+13,095 USD).

By setup: REV 623 trades, 29.4 %, PF 0.86, -16,049 USD; BRK 146 trades, 15.8 %, PF 0.93,
-881 USD (break trades lose 96 USD when wrong against 256 for reversals: tighter stops).
By level history (the level's state today, before the trade): first test of the day 98
trades, PF 1.00, +22; touched today 174 trades, 17.2 %, PF 0.60, -9,775; held today 297
trades, 27.9 %, PF 0.72, -16,928; broke today 200 trades, 38.0 %, PF 1.30, +9,751. The
"held" loss shows in every window but the off-hours (Asia -4,447, London -4,985, New York
-9,894) and in every stack size; the "touched" loss shows in every window. The "broke" gain
is mostly five big winners (without them +2,922 on 195 trades). The score gives held 15 points,
first test 12, touched 6, broke 3: on this sample the points run the wrong way.
By score: 50s PF 0.97 (-843), 60s 0.93, 70s 0.88, 80s 0.77, 90s 0.54 (-4,431 on 45 trades);
the higher the score the worse, in a straight line, as D-83 and D-84 read on paper.
By stack: one level PF 0.80 (-8,662), two levels 1.00 (+210), three or more 0.77 (-8,477).
By level type (a trade counts once per level in its zone): worst 4H open -11,024 on 169
trades (PF 0.63), London high -7,701 (0.47), previous 4H high -5,031, previous day mid -4,104
(12.8 % winners), previous 4H low -3,459; best previous 4H mid +3,914 (1.25), midnight open
+3,209 (1.26), New York low +3,083 (1.53). The 4-hour family as a whole -13,440 on 436 trades;
the two 4-hour opens (4HO, P4O) together -13,831.
By session (Asia / London / New York) where relevant: Asia 132 trades, PF 1.16, +3,383;
London 83, 0.64, -5,030; New York 308, 0.77, -12,020; other hours 246, 0.91, -3,263. The
long sample (session 10) already showed Asia's edge does not hold, so every window and hour
figure here is a hypothesis, not a result. By hour of entry the losing hours are 08:00-08:59
(71 trades, -5,817, the cash open), 13:00-14:59 (-5,391), 17:00-18:59 (-7,078, the 17:00 CT
[18:00 NY] Globex reopen) and 01:00-02:59 (-5,485); the winning hours 04:00, 10:00-11:59,
20:00 and 22:00-00:59.
Retries (same zone and direction within two hours of a losing attempt): 39 trades, PF 0.55,
-3,570; first attempts PF 0.89.
Days: 90 days traded, 42 positive. The worst three days (28 Jul, 24 Jun, 29 Jul) cost 10,430;
28 Jul had twelve losses in a row. July alone -13,430 (weeks 29 and 31 -14,000 between them);
June, August and September together -3,500. Without the worst ten days the run is +7,742.

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
1. The losers are not trades that never worked. 80 % of losing trades were 5 points in
   profit at some point, 56 % were 20 points up, 46 % were 30 up, 31 % were 50 up. Measured
   against each trade's own stop, 48 % of stop-outs had been half a stop in profit and 26 %
   a full stop in profit before they reversed and hit the stop. The exact part of the
   arithmetic: the losers that had reached +25 points lost 68,976 USD between them; a stop at
   entry after +25 would have scratched them (they all came back through entry). What the
   same rule would have cost on winners the export cannot show (77 % of winners went 10
   points against at some time, but not whether before or after their run-up), so the
   breakeven table in the report is a ceiling: +50,569 at +25 points, +26,079 at +50 points.
   One contract off at a run-up with the other left as traded is exact and does not turn the
   sign: half off at +50 gives -11,385 against -16,930, drawdown 15,277 against 23,947.
2. Closer targets alone do not turn the sign either (exact): a 40 to 50 point target gives
   about -6,000 with 50 to 55 % winners. Tighter stops alone: 40 to 50 points gives about
   -5,100, PF 0.95. Stop size: 20 % of stop-outs were 75 points or more and cost 53,294 USD,
   43 % of all the gross loss; the ten worst trades are all New York morning reversals with
   stops of 158 to 186 points.
3. The one selection reading that is broad-based: a level that already held or was already
   touched today loses on its next test, everywhere. The first test of the day and the retest
   of a level that broke earlier are flat to positive. That is the trend-day signature
   without a trend gate: the level holds in the morning, the move resumes, the second
   reversal at it breaks.
4. Hypotheses that need the long sample (each chosen after looking at this file, so each
   must hold on the other nine months before it counts): skip touched-today levels (-7,155
   instead of -16,930 on its own), no zones with a 4-hour open (-5,862), no entries in the
   08:00 and 17:00-18:59 hours (-4,035), no scores of 80 and up (-7,103). Together they leave
   211 trades at +5,228, which is what fitting six rules to one summer looks like, not a
   result. A daily loss cap (1 to 5 losers) does not help in any consistent way.

Issues found (bugs, repainting, alerts, drawing problems): none in the trades. Entry times
are the candle after the tag, flats are at 15:55 CT, and no trade shows an exit off its stop
or target. Evening entries (17:00-19:00 CT and after 23:00) hold through the night to the next
flatten by design; they are 105 trades at PF 0.63.

Changes made before the next session (setting or code, and why): none to the script. D-90
records what the file decides: the trade manager (M5, the plan's staged stops and partials)
is the next build, because the in-trade arithmetic is the one lever the export measures
exactly and it does not touch the reversal concept; the selection readings wait for the
365-day export (date chip "Last 365 days", capital chip 500,000, same defaults), run through
the same tool and split in halves.

Screenshots or trade list attached under reference/backtests/<date>/ : the export and the
readout are saved under `reference/backtests/2026-09-21/`.

---

## 2026-09-21  Session 13  (M4 v0.5, defaults on the chart range: tags confirmed, same trades as v0.3)

Symbol / timeframe / date range: MNQ1!, 5-minute, 7 Jun 2026 to 20 Sep 2026, the chart's
loaded history (the tester's date chip reads "Jun 7, 2026 - Sep 20, 2026" with no DEEP mark;
the capital chip reads "50K USD"). Not the Deep Backtesting run yet.
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, 2
contracts, initial capital 50,000.
Settings changed from defaults: none (the owner pressed Defaults after the switch tests).

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 769 | 206 won, 26.79 % | 0.864 | -16,929.80 USD, -33.86 %; -22.02 USD a trade | 24,103.40 USD, 44.46 % | 522.55 USD (gross profit 107,645.80 over 206) | 221.27 USD (gross loss 124,575.60 over 563) | not measured |

Identical to session 7 to the cent: gross profit 107,645.80 (215.29 %), gross loss 124,575.60
(249.15 %), commission load 2.29 %, expectancy -22.02 USD (-0.02 %), outliers 31,194.60 USD
(62.39 %), largest profit 3,064.80, largest loss 747.20, buy and hold +2.69 %.

By setup / by level type / by session: the tester's new "Profits and losses, by signals" panel
groups trades by the v0.5 order comment. Five groups named, the rest folded into "Other, 707"
at -26,056.80 USD (each tag carries the score, so almost every tag is its own group; the panel
is not a useful breakdown, the export is):
| Tag | Reading | Net |
|---|---|---|
| REV MO+P4M s77 k2 h1x | reversal at the midnight open stacked with the previous 4-hour mid, score 77, history 12 or 15 (cut off), window cut off | +3,064.80 |
| REV NL s51 k1 h3 ASIA | reversal at the New York low alone, score 51, the level had broken before, Asia | +2,074.80 |
| REV DO+P4O+P4M s61 k... | reversal at the daily open stacked with the previous 4-hour open and mid, score 61, rest cut off | +1,496.80 |
| REV 4HO s52 k1 h6 ASIA | reversal at the 4-hour open alone, score 52, level touched before, Asia | +1,343.80 |
| REV NO+LO s63 k2 h15 NY | reversal at the New York open stacked with the London open, score 63, level had held, New York | +1,146.80 |
The five sum to 9,127.00 USD, the "five best trades made 9,127" of session 7. All five are
reversal trades; two are Asia, one New York.

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
A confirmation run, nothing else: v0.5 (order comments only) produces the same 769 trades and
the same figures as v0.3, as it should. The tags reach the tester, so the exported list will
carry them.

Issues found (bugs, repainting, alerts, drawing problems): none. The run was made on the
chart range at 50,000 rather than under Deep Backtesting at 500,000, so it is the
confirmation and not the export run. The tester header's "Script execution" chip shows a
badge of 2; not investigated, the figures match the earlier run.

Changes made before the next session (setting or code, and why): none. Next: the date chip
to "Last 365 days" (the chip then shows DEEP), the capital chip to 500,000, then export the
list of trades and send the file. If the export is not offered under Deep Backtesting, export
this chart-range run instead (769 trades) and the long sample waits.

Screenshots or trade list attached under reference/backtests/<date>/ : not saved; the
screenshot is in the chat of 2026-09-21.

---

## 2026-09-21  Session 12  (M4 v0.3, switch test 4: stacked zones only, all hours; Last 365 days)

Symbol / timeframe / date range: MNQ1!, 5-minute, Deep Backtesting "Last 365 days".
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, 2
contracts, initial capital 500,000.
Settings changed from defaults: Score group, Reliability 0 and Level history 0; Filters top
box off (all hours). Owner confirmed the window filter was off this time.

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 2,344 | 628 won, 26.79 % | 0.880 | −33,259.80 USD, −6.65 % of 500,000; −14.19 USD a trade | 44,028.60 USD, 8.71 % | 387.71 USD (gross profit 243,481.40 over 628) | 161.27 USD (gross loss 276,741.20 over 1,716) | not measured |

Commission load 3.08 %. Buy and hold +19.73 %. Outliers 62,115.40 USD. Largest profit
3,064.80, largest loss 872.20. Payoff 2.4 to 1, break-even near 29 % winners, the run wins
26.8 %.

By setup / by level type / by session: not measured (Deep Backtesting draws nothing).

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
The best of the four long-sample runs (0.880 against 0.843 for the base) and still a loser
at −14 USD a trade. The trade count barely moved (2,344 against 2,510) although single-level
zones were 37 % of the 73-day base: with the ranking and history weights at zero, stacked
zones that the old score had rejected for a low rank or a broke-today history now pass, and
they replace the single-level trades almost one for one. So this is "stacked regardless of
rank and history", not "the base minus singles", and the gain is within what noise could
give. The equity curve is flat until March and slides after.

Issues found (bugs, repainting, alerts, drawing problems): none.

Changes made before the next session (setting or code, and why): M4 v0.5 adds order comments
so the tester's exported trade list carries every trade's setup, zone, score, stack, history
and window, plus T1 / stop / flat on exits (D-89). Next: paste v0.5, Deep Backtesting at the
longest range with defaults and capital 500,000, export the trade list, send the file; the
switch tests pause until that file is read.

Screenshots or trade list attached under reference/backtests/<date>/ : not saved; the
screenshot is in the chat of 2026-09-21.

---

## 2026-09-21  Session 11  (M4 v0.3, switch test 3: stacked zones only; Last 365 days)

Symbol / timeframe / date range: MNQ1!, 5-minute, Deep Backtesting "Last 365 days".
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, 2
contracts, initial capital 500,000 (first run at the test capital).
Settings changed from defaults: Score group, Reliability 0 and Level history 0 (the stack is
then the whole score, so single-level zones fall under the minimum and only zones with two or
more levels trade). The Asia window from session 10 was still ticked (owner confirmed), so
this run is Asia plus stacked zones: 448 trades against 532 for Asia alone. The all-hours
stacked-only run follows as session 12.

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 448 | 105 won, 23.44 % | 0.807 | −10,535.60 USD, −2.11 % of 500,000; −23.52 USD a trade | 12,579.80 USD, 2.51 % | 420.31 USD (gross profit 44,133.00 over 105) | 159.38 USD (gross loss 54,668.60 over 343) | not measured |

Commission load 3.25 %. Buy and hold +19.43 %. Outliers 11,827.40 USD. Largest profit
1,252.80, largest loss 636.20.

By setup / by level type / by session: not measured (Deep Backtesting draws nothing).

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
Flat to slightly positive until February, a dip in March, then a slow slide to −2 % of the
larger account by September. The profit factor, 0.807, is the lowest of the three long-sample
runs so far (base 0.843, Asia 0.841). If the Asia window was on, this says stacked zones do not
help inside Asia; the all-hours version decides the stack question. Either way the 73-day
"two-level zones in the black" reading looks like sample noise, as the Asia one did.

Issues found (bugs, repainting, alerts, drawing problems): the run carried the previous
test's window filter (above). From here every test report states the trade count and the grey
settings line, and the Filters top box is off unless the test is about windows.

Changes made before the next session (setting or code, and why): none. Next: the same
weights with the Filters top box off (all hours, stacked only), then fewer levels, stronger
rejection candles, the range filter, break trades off, New York only.

Screenshots or trade list attached under reference/backtests/<date>/ : not saved; the
screenshot is in the chat of 2026-09-21.

---

## 2026-09-21  Session 10  (M4 v0.3, switch test 2: Asia window only; Last 365 days)

Symbol / timeframe / date range: MNQ1!, 5-minute, Deep Backtesting "Last 365 days" (late Aug
2025 to 20 Sep 2026; the whole range this time, no margin stop).
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, 2
contracts, initial capital still 50,000 (the 500,000 for tests was not yet set; with 532 trades
the run was not cut short).
Settings changed from defaults: Filters, "Entries only inside the checked windows" on, Asia
(19:00 to 23:00 CT [20:00 to 00:00 NY]) the only window ticked.

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 532 | 127 won, 23.87 % | 0.841 | −10,218.40 USD, −20.44 %; −19.21 USD a trade | 11,693.20 USD, 22.72 % | 425.00 USD (gross profit 53,974.60 over 127) | 158.50 USD (gross loss 64,193.00 over 405) | not measured |

Commission load 3.15 %. Buy and hold +19.42 %. Outliers 33.98 % of the gross. Payoff about
2.7 to 1, break-even near 27 % winners, the run wins 24 %.

By setup / by level type / by session: not measured (Deep Backtesting draws nothing on the
chart).

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
About two trades a night. Flat to −5 % from September to March, then a steady slide to −20 %
by September 2026, with the same profit factor as the all-hours base (0.841 against 0.843).
The 73-day reading that Asia was the one positive window (session 5: +892.50 points on 137
trades) does not hold on the year; it was the sample noise D-85 warned about. Not a keeper.

Issues found (bugs, repainting, alerts, drawing problems): none. The filter took this time
(the trade count is the check).

Changes made before the next session (setting or code, and why): none to the rules. Next
switch test: stacked zones only (Reliability 0 and History 0 together), then fewer levels,
stronger rejection candles, the range filter, break trades off, New York only. Initial
capital 500,000 in Properties from here.

Screenshots or trade list attached under reference/backtests/<date>/ : not saved; the
screenshot is in the chat of 2026-09-21.

---

## 2026-09-21  Session 9  (M4 v0.3, first Deep Backtesting run, "Last 365 days")

Symbol / timeframe / date range: MNQ1!, 5-minute, Deep Backtesting "Last 365 days"; the
equity curve runs from late Aug 2025 and stops around 12 Jun 2026, where the account is
nearly gone (−89 %) and two contracts no longer clear the 5 % margin, so no trade opens
after that.
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, 2
contracts, initial capital 50,000.
Settings changed from defaults: the owner reports "just Asia selected" in the Filters group.
The trade count says the filter was not active: 2,510 trades over about 205 trading days is
12 a day, the all-hours rate (the 73-day base ran 10.5 a day; the Asia window held 18 % of the
base trades). The master switch "Entries only inside the checked windows" was most likely left
off, in which case the window boxes do nothing. Treated as the long-sample base run until a
rerun with the master switch on says otherwise.

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 2,510 | 662 won, 26.37 % | 0.843 | −44,558.40 USD, −89.12 % | 48,439.60 USD, 89.90 % | 361.03 USD (gross profit 239,000.60 over 662) | 153.44 USD (gross loss 283,559.00 over 1,848) | not measured |

Commission load 3.36 %. Buy and hold over the range +13.10 %. The five best trades made
7,889 USD, the other 2,502 lost 52,447 USD.

By setup / by level type / by session: not measured (Deep Backtesting draws nothing on the
chart, so the paper tables still show the 73-day chart range).

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
The equity curve loses steadily across the whole year: about −5 % by November 2025, −40 % by
February, −60 % by March, a bounce in April, then down to −89 % by June. So the base loss is
not one bad fortnight; the raw trigger loses in every season of the sample, at a profit factor
(0.843) that matches the 73-day run (0.864). The average winner is smaller here than in the
73-day run (361 USD against 523) and so is the average loser (153 against 221): the older
data is lower-priced and quieter, so distances in daily-ATR units come out smaller in dollars.

Issues found (bugs, repainting, alerts, drawing problems): with 50,000 of capital a losing
run hits the margin floor before the range ends, which cuts the trade count and makes runs
hard to compare. For the switch tests the initial capital goes to 500,000 in the Properties
tab, so no run is cut short; profit factor, trade count and net in USD are the comparison,
not the percentages.

Changes made before the next session (setting or code, and why): none to the rules. Next:
rerun the base on the long range with initial capital 500,000 (the reference), then the
window test with the master switch on and only Asia ticked (expect a few hundred trades),
then the rest of the list. The bias-gate proposal is withdrawn (D-88).

Screenshots or trade list attached under reference/backtests/<date>/ : not saved; the
screenshot is in the chat of 2026-09-21.

---

## 2026-09-21  Session 8  (M4 v0.3, switch test 1: Reliability weight 0; 73-day sample)

Symbol / timeframe / date range: MNQ1!, 5-minute, 7 Jun 2026 to 20 Sep 2026, the chart's data
(Deep Backtesting not yet on; the tester's date chip still shows the chart range).
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, 2
contracts.
Settings changed from defaults: Score group, Reliability 40 -> 0 (the score then reads out of
the 42 points that stack, history and bias can produce).

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 795 | 208 won, 26.16 % | 0.837 | −20,648.60 USD, −41.30 %; −26.22 USD a trade | 27,935.40 USD, 53.59 % | 513.13 USD (gross profit 106,730.40 over 208) | 217.33 USD (gross loss 127,574.00 over 587) | not measured |

Against the base run (769 trades, 0.864, −16,929.80, drawdown 44.46 %): more trades, a lower
profit factor, a deeper drawdown. Not a keeper on this sample.

By setup / by level type / by session: not measured for this run.

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
Taking the ranking out of the score lets in 26 more trades and they lose; the score's other
parts (stack, history) do not select better on their own. The ranking was not the cause of the
base loss, and the "top types lose" reading of D-85 is about the types, not the weight.

Issues found (bugs, repainting, alerts, drawing problems): the owner's third screenshot, taken
after the test, shows the defaults again (the grey settings line under the script name reads
"... 14 40 20 15 10 15 50 ...", where 40 is the reliability weight), so it looked as if the
tester ignored the change. It did not: the second screenshot is the changed run. A change
takes effect only after OK in the settings window, and the settings line is the check. Tests
so far are on the 73-day chart range, not the long sample.

Changes made before the next session (setting or code, and why): none. Next: turn Deep
Backtesting on (the date chip in the tester header, start date years back), rerun the base,
then the remaining switches on that range.

Screenshots or trade list attached under reference/backtests/<date>/ : not saved; the three
screenshots are in the chat of 2026-09-21.

---

## 2026-09-21  Session 7  (M4 v0.3, base run: the tester's figures, cross-check passed)

Symbol / timeframe / date range: MNQ1!, 5-minute, 7 Jun 2026 to the Sunday 20 Sep evening
session, 73 trading days (breakdown table header); the chart's loaded history, about 20,600
candles. Screenshot at 20:38 CT [21:38 NY] with the info box, both tables and the level lines
drawn (the owner re-added the script; the earlier blank was the mid-candle timing).
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, set in
the script. Order size 2 contracts.
Settings changed from defaults: none (all filters off, entry at the close of the follow-through
candle, stop beyond the zone, reliability weight 40).

Headline stats (info box, then the tester's Overview at 20:49 CT [21:49 NY]; the Performance
Summary tab not yet screenshotted):
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 769 closed (paper tally 770) | 206 won, 26.79 % (paper: 171 reached T1, 22 %) | 0.864 | −16,929.80 USD after costs on 2 MNQ, −33.86 % of the 50,000; −4232.50 points per contract; −22.02 USD a trade (expectancy) | 24,103.40 USD, 44.46 % | 522.55 USD, 130.6 points per contract (gross profit 107,645.80 over 206 winners; paper +137.75 per T1 exit) | 221.27 USD, 55.3 points per contract (gross loss 124,575.60 over 563 losers; paper −54.00 per stop) | not measured |

Performance analysis tab: commission load 2.29 %; outliers 31,194.60 USD, 62.39 % of the
gross; largest profit 3,064.80 USD, largest loss 747.20 USD; the five best trades made
9,127 USD and the other 764 lost 26,057 USD. Payoff about 2.4 to 1, so break-even needs about
30 % winners; the run wins 26.8 %.

Overview extras: buy and hold over the same range +2.69 %. The equity curve (percent of the
account) sits between 0 and −5 % from 7 Jun to about 13 Jul, drops to about −22 % over the
next two weeks, drifts to −30 % by early August, dips to about −38 % around 8 Sep and ends at
−33.86 %. Most of the damage is one two-week stretch in mid-July; the trade list of those days
is worth a look once the long sample is in.

Cross-check (checklist item 3): tester 769 closed against paper 770, one apart. Tester net
−4232.50 points per contract against paper −2977.00 before costs: a gap of 1255.50 points over
769 trades, 1.63 points a trade, against an expected 1.8 for a trade that ends at the stop
(two commissions, two slipped fills) and 1.3 for one that ends at the target (no slippage on a
limit fill); weighted by the 22 % of target exits the expectation is about 1.7. The tally's fill
model matches the tester. The tester's extra winners over the tally's T1 count are the flatten
exits that closed in profit (43 flats in the tally).

By setup, by score, by stack and by level type: as session 5 (the paper tally is unchanged:
REV 623 trades about −2915, BRK 147 trades −62; scores 5 and 6 positive, 7 and 8 negative;
2-level zones +607 against −1825 and −1759 for 1 and 3+; P4M, MO and NL the winners, LH, P4H
and AL the losers).
By session (Asia / London / New York) where relevant: as session 5 (Asia +892.50, London
−1117.50, New York −2384.50, other hours −367.25, paper).

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
The base strategy loses on this sample after costs: −5.5 points a trade on average, of which
1.6 is cost; before costs −3.9 a trade. About one trade in four ends with a profit. Nothing
new in the shape of the trades against v0.15 and the session-5 reading; the D-84 conclusion
stands (the raw trigger has no edge; the ranking's top types are the losers). This is the
honest baseline for the switch tests, which now move to the long sample.

Issues found (bugs, repainting, alerts, drawing problems): none in this run. The LuxAlgo
Smart Money Concepts boxes are still on the chart (not ours). The "NY Low" tag sits on top of
the statistics table's AO row at this zoom, cosmetic. With the tester panel open the info box
and the breakdown table overlap at the top right (the pane is shorter); move the breakdown
table to "Middle left" or "Bottom left" in the paper-trade settings for tester screenshots.
The Overview screenshot also shows an open short of 2 contracts at 30,110.25 in the connected
Tradovate panel; the owner confirmed it is a discretionary trade of their own, not the
strategy's. No bridge is trading the script.

Changes made before the next session (setting or code, and why): none to the rules. M4 v0.4
(already pushed) only makes the strategy recalculate on every tick so the drawings refresh
live, and formats the tester-net figure plainly; same trades. Next: the tester's Overview and
Performance Summary for the missing fields, then the Deep Backtesting run of the same base
settings, then one switch at a time on the long sample, reliability weight 0 first (D-85).

Screenshots or trade list attached under reference/backtests/<date>/ : not saved; the
screenshot is in the chat of 2026-09-21.

---

## 2026-09-21  Session 6  (M4 v0.3, the tester trades; cross-check of six trades)

Symbol / timeframe / date range: MNQ1!, 5-minute, the chart's loaded history; screenshot of
17 and 18 Sep with the Sunday 20 Sep evening session at the right edge, 20:33 CT [21:33 NY].
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, 5 % margin, set in
the script.
Settings changed from defaults: none.

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| not measured (order ids reach 1025) | not measured | not measured | not measured | not measured | not measured | not measured | not measured |

The tester's report and the info box were not in the screenshot (taken inside a candle right
after the paste, before the strategy's first recalculation), so no figures.

By setup: not measured.
By level type (top 3 and bottom 3 by net P&L): not measured.
By session (Asia / London / New York) where relevant: not measured.

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
The tester's own entry and exit marks (E1020 to E1025, two contracts each) land on the tally's
marks: the exit of trade 1020 on "T1 +183.50" at 12:00 on the 17th; trade 1021 (7/10 long at
12:05) closed by the flatten at the close; trade 1022 (7/10 short at the 17:00 reopen) out at
22:20 on "stop −38.00"; trade 1023 (7/10 long at 22:25) held overnight, out at 09:45 on the 18th
on the −28.00 stop, its first target being the 29,996 zone that the overnight rally never
reached; trade 1024 (8/10 long) out at 11:45 on "stop −52.25"; trade 1025 (5/10 long at 12:00)
out at 13:10 on "T1 +76.75". Six trades, six matches in candle and outcome.

Issues found (bugs, repainting, alerts, drawing problems): the level lines, info box and tables
were absent in the screenshot. A strategy recalculates the live candle only at its close, so a
paste mid-candle shows none of the last-candle drawings until then. Not confirmed as the cause;
if v0.4 shows the same, the owner sends the error text from the script's status line.

Changes made before the next session (setting or code, and why): M4 v0.4 recalculates on every
tick so the drawings refresh live (orders and the tally stay on confirmed candles); the
tester-net figure uses a plain number format. Next run: the base run with the tester's Overview,
Performance Summary and the info box Tester and Paper rows, then Deep Backtesting.

Screenshots or trade list attached under reference/backtests/<date>/ : not saved; the
screenshot is in the chat of 2026-09-21.

---

## 2026-09-21  Session 5  (M4 v0.2, first strategy run that drew; the tester made no trades)

Symbol / timeframe / date range: MNQ1!, 5-minute, 7 Jun 2026 to the Sunday 20 Sep evening
session, 73 trading days (breakdown table header); the chart's loaded history, about 20,600
candles.
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, set in the script.
The tester made no trades, so no cost was charged.
Settings changed from defaults: none (all filters off, entry at the close of the follow-through
candle, stop beyond the zone).

Headline stats (paper tally; the tester's own report was empty):
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 770 (171 T1, 556 stop, 43 flat) | 22 % reached T1 | not measured | −2977.00 points before costs | not measured | +137.75 per T1 exit | −54.00 per stop | not measured |

Tester rows in the info box: 0 closed, 0 won, net 0 USD. Signals: 623 REV, 147 BRK.

By setup: REV 623 trades, 24 % T1, about −2915 points; BRK 147 trades, 14 % T1, −62.00 points.
By score: 5/10 or less 94 trades +1086.00; 6/10 210 trades +954.25; 7/10 217 trades −2645.00;
8/10 or more 249 trades −2372.25. By stack: 1 level 286 trades −1824.75; 2 levels 272 trades
+607.00; 3 or more 212 trades −1759.00.
By level type (top 3 and bottom 3 by net P&L): P4M +1134.00 (96 trades, 28 % T1), MO +929.50
(75, 28 %), NL +845.25 (45, 29 %); LH −1804.00 (69, 18 %), P4H −1096.00 (92, 23 %), AL −616.00
(52, 15 %). MNH, the top of the hold-rate ranking, 22 trades −204.75.
By session (Asia / London / New York) where relevant: Asia 137 trades +892.50; London 82
−1117.50; New York 314 −2384.50; other hours 237 −367.25.

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
v0.2 compiled and drew everything: the level lines start at their candles again, the tags,
the info box and both tables are back. The paper tally under the M4 fill model (entries at
the next candle's open, resting orders checked when placed) reads a little worse than v0.15
(770 trades and −2977 against 812 and −2760), which is the cost of getting in one candle
later. Its shape is unchanged: scores of 5/10 and 6/10 positive, 7/10 and 8/10 negative;
two-level zones the only stack group in the black; Asia positive, New York the worst window;
the ranking's top types losing and the middle types winning (D-85). The tester itself made no
trades: with its default margin of 100 % of the contract value, one MNQ contract at 30,000
counts as 60,000 of cash, and every order was rejected on the 50,000 account.

Issues found (bugs, repainting, alerts, drawing problems): the tester's zero trades (margin,
above). The LuxAlgo Smart Money Concepts boxes were still on the chart; they are not ours.

Changes made before the next session (setting or code, and why): M4 v0.3 sets a 5 % margin for
longs and shorts in the script, about the exchange margin on a micro contract, so the tester
can fill the orders. No trading rule changed. Next run: the same base run, with the tester's
Overview, Performance Summary and the info box Tester and Paper rows.

Screenshots or trade list attached under reference/backtests/<date>/ : not saved; the
screenshot is in the chat of 2026-09-21.

---

## 2026-09-21  Session 4  (M4 v0.1, first strategy paste; stopped by a runtime error)

Symbol / timeframe / date range: MNQ1!, 5-minute, the chart's loaded history (about 20,590
candles; the Sunday 20 Sep evening session at the right edge, 19:49 CT [20:49 NY]).
Costs used (commission per side, slippage ticks): 0.80 per side, 2 ticks, set in the script;
the report was never produced.
Settings changed from defaults: none.

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| not measured | not measured | not measured | not measured | not measured | not measured | not measured | not measured |

The script compiled but stopped on the last candle: "Error on bar 20590: The requested
historical offset (3001) is beyond the historical buffer's limit (300)", raised by the level-line
drawing (f_drawLine). No strategy report, no info box, no tables.

By setup: not measured.
By level type (top 3 and bottom 3 by net P&L): not measured.
By session (Asia / London / New York) where relevant: not measured.

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
Every candle before the last one was processed: the signal tags and the paper exit marks drew
as in v0.15 (7/10, 8/10 and 5/10 tags; T1 +193.50, stop −38.00, stop −52.25 and T1 +76.75
visible on 17 and 18 Sep). The level lines, their tags, the info box, the statistics table and
the breakdown table were missing, because the drawing block runs before them and the error
stopped the script there. The same chart carried the LuxAlgo Smart Money Concepts boxes, which
confuse the read of the tester's trade marks; hide that indicator for the M4 screenshots.

Issues found (bugs, repainting, alerts, drawing problems): the runtime error above. A strategy
refuses a line that starts 3,000 candles back by candle count (the longest-line setting), which
the indicator version accepted (D-87).

Changes made before the next session (setting or code, and why): M4 v0.2 places the level lines
and their tags by time, from a list of one time per candle, so a line still starts at the candle
that made its level. No trading rule changed. Next run: the same base run, plus the tester's
Overview, Performance Summary and the info box Tester and Paper rows.

Screenshots or trade list attached under reference/backtests/<date>/ : not saved; the screenshot
and the error text are in the chat of 2026-09-21.

---

## 2026-09-20  Session 3  (M3 v0.14, entry and stop switches; run A = baseline)

Symbol / timeframe / date range: MNQ1!, 5-minute, 7 Jun 2026 to the Sunday 20 Sep evening
session, 73 trading days (from the table header).
Costs used (commission per side, slippage ticks): none (paper trade).
Settings changed from defaults: run A none (Reversal entry: close of the follow-through candle;
Reversal stop: beyond the zone; range filter off). Runs B, C and D (limit after the
follow-through; limit after the rejection candle; wick stop) to be added below as they come in.

Headline stats (run A, baseline):
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 812 (182 T1, 587 stop, 43 flat) | 22 % reached T1 | not measured | −2759.75 points | not measured | +135.50 | −52.50 | not measured |

By setup: REV 629 trades / 24 % / avg T1 +138.50 / avg stop −63.50 / −2808.25;
  BRK 183 / 15 % / +120.50 / −22.25 / +48.25.
By score: 5/10 or less 102 / 24 % / +908.75 (+156.00, −43.50); 6/10 226 / 24 % / +1182.75
  (+142.00, −43.00); 7/10 227 / 21 % / −2594.75 (+120.25, −54.00); 8/10 or more 257 / 22 % /
  −2256.75 (+133.75, −63.50).
By level type (top 3 and bottom 3 by net P&L): not measured.
By session: Asia window 136 / 29 % / +932.50; London window 80 / 18 % / −1123.75; New York
  window 353 / 20 % / −2254.75; other hours 243 / 24 % / −314.00.

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
The same-candle stop rule took the break trades from +1141.25 (Session 2, run A) to +48.25:
their T1 share fell from 19 % to 15 %, so about seven retests that reached the target in
v0.13 had crossed their stop inside the fill candle and now count as stops, as the tester
would count them. Reversal trades moved from −2341.75 to −2808.25 through the changed trade
sequence and one more trading day. The pattern from Session 2 is unchanged: 5/10 and 6/10
positive, 7/10 and 8/10 negative, Asia positive, London and New York negative, hit rate flat
at about one in four or five everywhere.

Issues found (bugs, repainting, alerts, drawing problems): none. The All row matches the info
box (812 trades, −2759.75). A further run (809 trades, 21 % T1, −2305.75; REV 570 / −1899.75,
BRK 239 / −406.00) arrived with the settings line still showing the default entry and stop, so
an unidentified setting had changed; set aside until the settings are confirmed.

Run E (Reversal entry "Limit at the level after the follow-through", Reversal stop "Beyond the
rejection wick", confirmed by the settings line): 908 trades, 13 % reached T1, avg T1 +125.00,
avg stop −25.25, net −3356.75. REV 512 / 12 % / +132.25 / −27.75 / −3028.25; BRK 396 / 14 % /
+117.25 / −22.00 / −328.50. By score: 5/10 or less 142 / 13 % / +59.75; 6/10 281 / 15 % /
−81.75; 7/10 239 / 12 % / −1650.75; 8/10 or more 246 / 12 % / −1683.75. By session: Asia 163 /
15 % / −16.75; London 91 / 14 % / −228.25; New York 432 / 14 % / −1634.25; other 222 / 11 % /
−1477.50. Reading (D-84): the reversal stop halved and the hit rate halved with it; per trade
the reversals lost 5.9 points instead of 4.5, and 21 % of the stop instead of 7 %. Break trades
doubled in number because the bot was free more often (unfilled limits, quick stops). Against a
coin flip (stop ÷ (stop + target)) the reversals sit under it in both geometries, the stacked
zones well under it and the single levels at it. Runs B, C and D not run; the geometry question
is answered well enough by A and E.

Run F (M3 v0.15, defaults, the same 812 trades as run A): stack rows: 1 level in the zone
312 / 19 % / avg T1 +143.00 / avg stop −46.50 / −2239.25; 2 levels 278 / 27 % / +131.25 /
−57.00 / +1527.00; 3 or more 222 / 22 % / +133.75 / −56.25 / −2047.50. Level types, the 15
shown (top by hold rate; trades / T1 % / net, a stacked trade counting in every member's row):
MNH 23 / 17 / −291.50; NH 51 / 27 / +40.50; MNL 25 / 24 / −325.25; LL 48 / 23 / −319.50;
LH 73 / 19 / −1646.25; PDH 42 / 21 / −90.25; AL 47 / 17 / −557.50; P4H 93 / 25 / −795.75;
MO 76 / 28 / +573.25; NL 47 / 32 / +792.00; NO 74 / 22 / −435.75; AO 70 / 30 / +340.00;
AH 67 / 34 / +496.00; MOO 14 / 21 / +115.25; P4M 100 / 30 / +1325.25. The remaining types
need Rows set to 40 (asked). Reading in D-85: the two-level zones are the best group, single
levels the worst; the top-ranked types lose and the middle-ranked types win, so the hold-rate
rank predicts its own verdict rule, not the trade. Too few trades per row to filter on.

Changes made before the next session (setting or code, and why): M4 v0.1, the strategy
conversion (D-86): one position at a time in the tester, market entries at the next candle's
open, resting limits at their price, hard first target, flatten filling at the open of the
15:55 candle, the [F] filters as inputs all off, MNQ costs, the paper tally kept as the
cross-check. Next session is the tester's base run and the Deep Backtesting run.

Screenshots or trade list attached under reference/backtests/<date>/ : not saved; in the chat of
2026-09-20.

---

## 2026-09-20  Session 2  (M3 v0.13, indicator paper trade with the breakdown table)

Symbol / timeframe / date range: MNQ1!, 5-minute, 7 Jun 2026 to 18 Sep 2026, 72 trading days
(from the table header). The history under this run is not identical to Session 1: the
continuous contract rolled to December on Friday. Same trade count, net moved from −1280.75 to
about −1200.50.
Costs used (commission per side, slippage ticks): none (paper trade).
Settings changed from defaults: run A none; run B Range filter On.

Headline stats (run A, range filter off):
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 807 | 23 % reached T1 | not measured | about −1200.50 points | not measured | +136.25 | −52.75 | not measured |

Run B (range filter on): 764 trades, 22 % reached T1, avg T1 +131.50, avg stop −46.25, net −651.00.

By setup: run A: REV 626 trades / 25 % / −2341.75; BRK 181 / 19 % / +1141.25.
  Run B: REV 511 / 25 % / −1081.50; BRK 253 / 15 % / +430.50.
By score: run A: 5/10 or less 100 / 25 % / +1164.00 (avg T1 +157.50, avg stop −44.50);
  6/10 226 / 26 % / +1936.25 (+142.50, −43.25); 7/10 224 / 21 % / −2259.50 (+120.25, −54.00);
  8/10 or more 257 / 23 % / −2041.00 (+134.00, −63.25).
  Run B: 90 / 22 % / +580.50; 226 / 21 % / +1676.25; 204 / 20 % / −2755.50; 244 / 25 % / −152.25.
By level type (top 3 and bottom 3 by net P&L): not measured.
By session: run A: Asia window 136 / 30 % / +1148.25; London window 80 / 18 % / −1123.75;
  New York window 348 / 22 % / −911.25; other hours 243 / 24 % / −314.00.
  Run B: Asia 124 / 21 % / −1204.25; London 76 / 22 % / −311.00; New York 337 / 22 % / +1083.00;
  other hours 227 / 22 % / −218.75.

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
The hit rate is flat, about one in four or five in every group. What separates the winning
groups from the losing ones is the payoff: 5/10, 6/10 and break trades have winners over three
times their losers and made money; 7/10, 8/10 and reversals as a whole sit near two to one and
lost. The wide stops belong to stacked zones (the stop is beyond the far side of a wide zone)
and to the reversal entry a candle or two away from the level; break entries sit at the level
and carry a 22-point average stop against a 63-point one for reversals. The range filter
changed the whole trade sequence (one trade at a time), so its 550-point improvement and the
session rows, which flipped sign between the runs, are not conclusions.

Issues found (bugs, repainting, alerts, drawing problems): none. The All row matched the info
box. Noted: a limit fill that crosses its stop within the same candle was carried to the next
candle before the stop check; fixed in v0.14 (counts as a stop at once, as the tester would).

Changes made before the next session (setting or code, and why): M3 v0.14 adds the reversal
entry switch (close of the follow-through candle; limit at the level after the follow-through;
limit at the level right after the rejection candle) and the reversal stop switch (beyond the
zone; beyond the rejection wick; the farther of the two), plus the same-candle stop rule for
limit fills (D-83). No score change. Next session compares the four settings on the breakdown.

Screenshots or trade list attached under reference/backtests/<date>/ : not saved; two
screenshots in the chat of 2026-09-20.

---

## 2026-09-20  Session 1  (M3 v0.12, indicator paper trade, not the strategy tester)

Symbol / timeframe / date range: MNQ, 5-minute; date range not reported (the chart's loaded
history; v0.13 prints the first trade's date and the trading days covered, report it next time).
Costs used (commission per side, slippage ticks): none. The paper trade fills at the signal
price, the stop price and the target price, with no commission and no slippage.
Settings changed from defaults: none. v0.12 defaults: minimum score 50, volume confirmation
Off, one trade at a time On, entry cutoff 15:00 CT [16:00 NY], flatten 15:55 CT [16:55 NY],
range filter Off, break trades On.

Headline stats:
| Trades | Win % | Profit factor | Net P&L | Max drawdown | Avg win | Avg loss | Avg time in trade |
|---|---|---|---|---|---|---|---|
| 807 (176 T1, 592 stop, 39 flat) | 21.8 % reached T1 | not measured | −1280.75 points, about −$2,560 on one MNQ before costs | not measured | not measured (a +76.00 T1 exit visible on the chart) | not measured (stops of −27.75, −38.00 and −44.50 visible) | not measured |

By setup: 569 REV signals, 238 BRK signals; outcomes per setup not measured (v0.13 adds them).
By level type (top 3 and bottom 3 by net P&L): not measured.
By session (Asia / London / New York) where relevant: not measured (v0.13 adds Asia, London,
New York and other hours).

How it reacted (what the trades looked like, where it entered too early or late, stops that made no sense):
About one trade in five reached its first target; the net is a small loss, −1.6 points a trade
on average. The trade model is the crudest possible: in at the close of the follow-through
candle, stop beyond the far side of the zone plus the buffer, out only at the first target,
the stop or the 15:55 flatten. Because the entry candle has already moved away from the level,
the stop is wide (a zone height plus a candle or two) while the first target is the next zone
at least 0.15 daily ATR away, so the reward is about two to three times the risk and the
break-even hit rate is one in three or four; one in five loses. On the visible chart the
winners were the trades where the next zone was close to a fresh level (the +76.00 6/10 long)
and the stops were mostly high-score shorts in a rising stretch (7/10 and 8/10 tags). Nothing
entered too early by the rules; the entries are late by design, one candle after the rejection.

Issues found (bugs, repainting, alerts, drawing problems): none reported. Exit marks, arrows and
the two info-box rows drew as expected. Limits of the tally, not bugs: no partials, no breakeven
stop, no trailing, no costs, break trades included, and the level ranks come from the same
candles the trades ran on (in-sample).

Changes made before the next session (setting or code, and why): M3 v0.13 adds the paper
breakdown table (by score bucket, REV versus BRK, and session window, each with trade count,
T1 share, average gain, average loss and net points, plus the first trade's date and trading
days covered), so the next screenshot shows where the edge sits before any rule is changed
(D-82). No trading rule changed. Rule changes wait for the M4 strategy tester, which runs the
same splits with costs and compares entry styles first.

Screenshots or trade list attached under reference/backtests/<date>/ : not saved; the
screenshot is in the chat of 2026-09-20. Owner to say whether screenshots should be kept in the
repo from now on.
