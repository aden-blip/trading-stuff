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
