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
