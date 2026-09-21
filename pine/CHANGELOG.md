# Changelog

## M4 v0.1, 2026-09-21

- Milestone 4: the script is now a TradingView strategy. One position at a time; market entries
  fill at the next candle's open, as the tester and a bridge fill them; resting limits (break
  retests, the reversal limit modes) fill at their price; every entry carries its stop and first
  target as tester orders; the flatten order is placed one candle early so it fills at the open
  of the flatten candle (15:55 CT). Costs in the script are the MNQ defaults (0.80 per side,
  2 ticks slippage), initial capital 50,000; change them in Properties for other contracts.
- Filters module [F] as inputs, all off for the base run: allowed session windows, opening
  blackout, news blackout, chop band, daily trade and losing-trade caps, daily loss limit and
  daily target.
- Resting orders are checked for geometry, gate, score and filters when placed, as the tester
  requires; a fill is the signal. No new orders while a position is open; every other resting
  order is cancelled when one fills or a market entry is placed, inside the same candle through
  the tester's cancel group. The tally reads a candle along the tester's assumed path (open,
  nearer extreme, other extreme, close) to pick the fill, price a gap fill at the open, and
  count a stop or target hit later on the fill candle.
- The paper tally follows the same fill model and stays on the chart; the info box adds the
  tester's closed trades and net after costs, in currency and points, for the cross-check. The
  Contracts input drives both orders and alerts.

## M3 v0.15, 2026-09-20

- Paper trades by level type and by stack (D-84): the statistics table gains three columns
  while the paper trade is on, Trades, T1 % and Net per level type, a trade at a stacked zone
  counting in every member type's row; the breakdown table gains three rows, 1 level in the
  zone, 2 levels, 3 or more. No trading rule changed.
- Compile fix: the level-type tallies are declared above the statistics table that draws
  them (undeclared identifier tyPN).

## M3 v0.14, 2026-09-20

- Reversal entry and stop as test switches (D-83), from the first breakdown: entry at the close
  of the follow-through candle (default), a limit at the level after the follow-through, or a
  limit at the level right after the rejection candle; stop beyond the zone (default), beyond
  the rejection wick, or the farther of the two. A resting reversal limit shows as a REV signal
  on the candle that fills it, is cancelled by a close back through the zone, and expires after
  a bar count (6).
- A limit that fills and crosses its stop on the same candle now counts as a stop, for break
  retests too, as the strategy tester would count it. Break trade numbers drop a little.

## M3 v0.13, 2026-09-20

- Paper breakdown table (D-82): the paper trades split by score (5/10 or less, 6, 7, 8 or
  more), by setup (REV, BRK) and by session window (Asia, London, New York, other hours), each
  row with the trade count, the share that reached the first target, the average gain of those,
  the average loss of the stopped ones and the net points. The header shows the first trade's
  date and the trading days covered. On by default while the paper trade is on; a position
  setting (middle right by default). No trading rule changed.

## M3 v0.12, 2026-09-20

- Range filter as a test switch, off by default (D-81, your AMD read): inside a narrow range
  (last 120 minutes narrower than 0.5 daily ATR), reversal entries at levels in the middle half
  are skipped; the top and bottom quarters stay live. Grey `?` names the range.

## M3 v0.11, 2026-09-20

- One trade at a time (D-80): the indicator follows each taken signal as a paper trade, in at
  the signal, out at the stop, the first target or the flatten time (15:55 CT), with no new
  trades from 15:00 CT to the flatten. Signals while a trade is open are skipped, with a grey
  `?` explaining when Explain missed signals is on. Exit marks with the points made or lost,
  two info-box rows (trades by outcome, net points), and an EXIT alert message. Switch it off
  to see every setup as before.

## M3 v0.10, 2026-09-20

- Score reads out of what is reachable today (D-79): raw points over the points the current
  weights can produce, 82 before M6 and 100 after, so a 64 shows as 78 and 8/10. The hover box
  adds "Raw 64 of 82 reachable". Review minimum 50 (5/10), the same trades as the raw 40 of v0.9.

## M3 v0.9, 2026-09-20

- Review defaults (D-78): minimum score 40 while the score can only reach 82 (the HTF and bias
  parts arrive in M6); volume confirmation Off until the M4 backtest tests it. Both are settings,
  so a v0.8 paste can be set the same way by hand. No other change.

## M3 v0.8, 2026-09-20

- "My pivots": ten price boxes in the settings for pivot lines you draw by hand on a higher
  timeframe (D-75). Each is a level with every rule: zones, stack, its own hold-rate row (PIV),
  reversal and break signals, explanation tags. Pink lines tagged Pivot 1 to 10; 0 means empty.
  Info box row "My pivots".
- D-74 corrected from your notes: 29,895 was a 4-hour pivot you marked by hand, and the NY High
  short box is a plan for the Sunday open, not a Friday trade. Break trades were never off.

## M3 v0.7, 2026-09-20

- "Explain missed signals" switch (D-74): grey `?` tags on candles where a setup formed but a
  rule stopped it, with the reason in the hover box (score under the minimum with the breakdown,
  volume below average, no target or stop too wide, cooldown, a level still forming). The
  "Rules and candles" option also marks rejection candles with no follow-through and break
  retests that never filled. Off by default.

## M3 v0.6, 2026-09-20

- Signal tags show the score out of 10, for example `▲ 8/10` (D-73). The hover box adds the exact
  0 to 100 number; the alert message and the minimum-score setting stay on the 0 to 100 scale.

## M3 v0.5, 2026-09-20

- Signal tags show an arrow and the score only, size normal; setup, level, entry, stop, targets
  and the breakdown are in the hover box (D-72). Compact and Full remain as options.

## M3 v0.4, 2026-09-20

- Held and broke marks are off by default; the chart carries trade signals only (D-71).

## M3 v0.3, 2026-09-20

- Break trades: a first break of a level scores like a first test, so single-level break signals
  can reach the minimum score (D-70).
- Signal cooldown per level, 12 minutes by default.
- Compact signal tags (direction, setup, level, score) with entry, stop, targets, hook letters
  and the score breakdown in the tooltip; "Full" detail as an option.

## M3 v0.2, 2026-09-20

- Compile fix: the two-direction setup loop counted with a negative step, which Pine rejects.
  Variables shadowing the London open and NY high levels renamed.

## M3 v0.1, 2026-09-20

- Hidden zone list every bar: members, stack, freshness, today's verdicts, best rank; today's
  high and low as target-only members.
- REV detector: rejection bar (wick, poke and close back, engulfing) plus follow-through bar,
  volume confirmation on the Index profile, strong-rejection skip as an option.
- BRK detector: confirmed close through a zone rests a retest limit at the broken edge; the fill
  is the signal, a close back through cancels, six bars to live.
- Score: reliability from the rank (hold-rank for REV, break-rank for BRK), stack, level history,
  HTF 0 and bias neutral until M6, hooks at zero weight. Minimum 60. Rank gate as a switch.
- Trade geometry: stop off the zone plus buffer, TP1 and TP2 from the next zones at least the
  minimum distance away, minimum reward to risk, maximum stop.
- Signal labels with entry, stop, targets, score and hook letters; breakdown in the tooltip.
  `alert()` JSON per signal. Session VWAP and 15-minute 200 EMA computed, drawn only on request.
- Info box: zones and signal counts. Requests 6 of 40.

## M2 v0.3, 2026-09-20

- Hold and break verdict distances both default to 0.05 daily ATR (D-67). Settings change only;
  no other code differs from v0.2.

## M2 v0.2, 2026-09-20

- SR levels are zones: price at the midpoint of the touches, half the spread as a width that
  widens the touch band and the break and hold thresholds. SR tolerance default 0.08 daily ATR.
- Verdicts judged on closes of a verdict timeframe (default 5 minutes) with the window in minutes
  (default 150), so 1-minute and 5-minute charts agree.
- Prior weight input (default 10 at 0.5) for the ranking; the table shows raw hold rates.

## M2 v0.1, 2026-09-20

- Untagged support and resistance (SR): completed bars of the pivot timeframe (4-hour default)
  give pivot highs and lows; pivots inside the lookback are clustered within the SR tolerance and
  a cluster with enough touches is a level, priced at the mean of its touches, line from the first
  touch, tag "S/R (n)". Strongest clusters kept. Inputs per D-65.
- Interaction classifier per level instance: touch, approach side from the prior close,
  HELD / BROKE / NEUTRAL on confirmed bars only, first HELD or BROKE counted, every verdict can be
  marked on the chart ("Counted only" by default, rolling 150 marks).
- Statistics table per level type: N, hold %, break %, neutral, rank percentile; totals row;
  priors as one text input `code:rate:count`.
- Level slots unified: 38 labeled, up to 20 custom, up to 30 SR, one loop for touch, verdict and
  drawing. Info box shows the SR count, pivot count and interactions counted.
- Hidden VWAP and 200 EMA hooks are M3 (D-64); nothing new is drawn in M2.

## M1 v0.8, 2026-09-20

- Levels within the touch tolerance share one tag, names joined with a slash, tag at their mean
  price; every level keeps its own line. Share distance is a daily-ATR input with a tick floor,
  0 and 0 means identical prices only (D-63).
- Stagger columns are as wide as their longest name, from a bars-per-character input scaled by
  the label size. Five columns by default. Text-only labels start at the column edge.
- Fixed step and text pad inputs removed.

## M1 v0.7, 2026-09-20

- Boxed bookmark tags are the default label style again; text only stays as an option (D-62).
- Stagger distance is a share of the daily ATR with a tick floor, scaled by the square root of the
  chart timeframe. Step widened to 40 bars, three columns, and each label takes the first column
  with room below it. A level's line now runs to its own tag, so staggered tags stay attached.
- Label positions are capped 480 bars past the last candle, inside TradingView's drawing limit.

## M1 v0.6, 2026-09-20

- Labels that would sit within a set distance of each other step right into up to four columns
  so nearby levels stay readable. Stagger distance, step and column count are inputs.

## M1 v0.5, 2026-09-20

- Spaceman alignment: text-only coloured labels by default (boxed optional), size normal, line
  end 30 bars right of price, merge only at identical prices with " / ", per-level toggles,
  global colour, line style. Year high/low include today; Monday range develops live.

## M1 v0.4, 2026-09-20

- Session levels develop live while the session runs and freeze when it ends; "Completed only" switch.
- One line per level; labels merge only within one tick; boxes removed. Full names by default,
  short codes as the option, label offset 20 bars.
- Period tracker ignores a boundary on the very first bar of history.

## M1 v0.3, 2026-09-20

- New York session default 08:30 to 16:00 CT on every profile (D-56).
- Day, week, month and 4-hour levels measured from chart candles with the bar of each extreme, so
  lines start at the candle that made the level. Week and month fall back to higher-timeframe
  requests on short histories. Five requests total.
- Added PQH, PQL, PQM, YM, P4M and 4HO for Spaceman parity.
- Display: candle-anchored or right-anchored lines, longest-line cap, label offset, label size,
  short codes or full names, optional price, line width. All levels drawn by default; near-price
  limit is a switch.

## M1 v0.2, 2026-09-20

- Midnight open now requires the bar to sit in the first hour of the day in the anchor zone, so
  the Sunday reopen and any other gap no longer count as a midnight. Charts above 60 minutes
  keep the plain date change.
- First live check on MNQ 5-minute passed: profile, timezone, tolerances, clustering, session
  and daily levels consistent with the candles.

## M1 v0.1, 2026-09-19

- First script: `l2l.pine`, module [A] Level Engine, as an indicator.
- Level types: PDH PDL PDM DO MO, PWH PWL PWM WO, PMH PML PMM MOO, QO YO YH YL, P4H P4L P4O,
  MNH MNL MNM, Asia / London / New York session high low open, custom levels from a text input.
- Clustering into zones with daily-ATR tolerance and tick floor; a zone of two or more levels
  draws as a box with the codes joined.
- Fresh / touched state per level instance, reset at the daily rollover; optional `*` marker only.
- Timezone input, instrument profile (auto from the symbol root), midnight-open anchor.
- Info box and optional history plots for replay checks.
- Not yet: SR touch-cluster levels (M2), statistics (M2), signals (M3), strategy (M4 on).
