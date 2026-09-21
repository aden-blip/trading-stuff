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
