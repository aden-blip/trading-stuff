# Level-to-Level (L2L) Strategy: Design Plan

Status: BUILDING. Milestone 1 in review. Version 0.11, 2026-09-20.

Changes in 0.11, from the first display reviews (D-62, D-63):
- Labels are boxed bookmark tags by default; text only is the option.
- Levels within the touch tolerance share one tag, names joined with " / ", each level on its own line.
- Tags that would still overlap step right into columns sized by their longest name.

Changes in 0.10, aligned with the Spaceman source (`reference/spaceman_notes.md`):
- Labels are plain coloured text by default, size normal, at the end of the line; boxed is the option.
- Labels merge only at the identical price, joined with " / ".
- Toggles per level like Spaceman: Open, Prev H/L, Prev Mid for each family; Monday Range and Mid;
  session H/L and Open; midnight open; previous 4-hour open.
- Global colour switch and line style input.
- Year high and low include today's price action; Monday's range develops live during Monday.

Changes in 0.9, from the second M1 chart review:
- **Session levels develop live.** While a session runs, its high, low and open update as new
  extremes print, then freeze when the session ends. "Completed only" remains as a switch, and the
  trading logic in M3 will treat a developing session extreme as a target, not an entry level.
- **One line per level.** Drawing no longer merges nearby levels into boxes; only levels at the same
  price within one tick share a label. Zones for trading are still built in M2 from the cluster tolerance.
- Labels default to full names with short codes as the option, placed 20 bars right of price.

Changes in 0.8, from the first M1 chart review:
- **New York session runs to the 16:00 CT futures close** on every futures profile. The cash-close
  version cut off the late-afternoon high you expected to see as the NY high. Pit-hour windows for
  crude and metals stay available as inputs.
- Day, week, month and 4-hour levels are now measured from the chart's own candles, so every line
  can **start at the candle that made it**. Higher-timeframe requests are used only as fallbacks
  and for quarter, year and the daily ATR.
- Spaceman parity: previous quarter high / low / mid, year mid, previous 4-hour mid and the current
  4-hour open added.
- Display: all levels drawn by default, candle-anchored lines with a short right extension, label
  size input, short codes or full names, optional price in the label.

Changes in 0.7, final planning round:
- Volume confirmation applies to the **Index profile only** (NQ, MNQ, ES, MES). Off on energy, metals and generic.
- The break switch means **break, then retest, then enter**. A straight breakout entry is not built.
- Facebook reels closed as not needed. Planning is complete; M1 starts.

Changes in 0.6, from the six Socrates transcripts (`reference/transcripts/`):
- **Volume confirmation** on reversal entries, ON by default. His rule is "a key level with volume, that is it".
- **SR levels come from the 4-hour chart**, where he marks places that pivoted "a bunch of times, not
  just once", then checks which of those lines sit on a labeled key level. That alignment is our stack score.
- Ladder promotion can require volume behind the close-through, ON by default.
- His go-to at the daily open, daily high and daily low is **break, then retest**. Noted under the
  break-trade switch as the first variant to test if that switch ever goes on.
- VIX agreement means the VIX turning the opposite way at the same moment, not a slow average.
- Asia-open continuation for gold-type assets noted as a later bias option for SI and CL.

Changes in 0.5, after the fourth review round:
- **Break trades are optional and OFF.** The core is the reversal off a pivot and the trail to the
  target; the ladder already carries a trade through a level that rips. Break entries move to M7 as a switch.
- New level type **SR**: untagged support and resistance where price has touched repeatedly, built
  from clustered 15-minute swing points. Entry-eligible, built in M2.
- Levels are drawn the same whether touched or not; the signal score carries that information.
- The TradeZella journal is not needed; statistics come from the bot's own backtests.

Changes in 0.4, after the third review round:
- Daily caps are all **off for backtesting** and stay available as settings: signal count, loss count,
  and a loss limit as a **percent of account** instead of dollars. A daily **profit target in percent**
  only blocks new entries; it never closes a running trade.
- Cooldown after a stop-out is measured in **minutes**, not candles, so it means the same thing on every timeframe.
- Level-type ranking affects the **score only** until we have enough data; the hard split into
  reversal-only and break-only types is a switch you turn on after research.
- Opening blackout confirmed: skip the trades, no reduced-size variant.
- Stop cap and size-by-score stay off until backtesting says otherwise.
- New **backtest log** (`docs/BACKTEST_LOG.md`) with a rule in `CLAUDE.md` that every backtest session gets an entry.
- Optional **thin-market filter** for CL and SI when volume dries up.

Changes in 0.3, after the second review round:
- Premium plan confirmed with the CME Group real-time bundle. MNQ is the main contract, Tradovate Free plan.
- Flatten is **15:55 CT** for every futures profile. Entries per profile use **allowed sessions** instead of one window.
- Flip redesigned the way you described it: a resting limit at the target for the open size plus the
  flip size, so one fill closes the trade and leaves the opposite position. Toggle, off by default.
- Higher-timeframe rejection is a **bonus**, never a requirement. First tests still trade. A "level
  history" score replaces the plain first-test score.
- From your own rules document: an **opening blackout** for the first 30 minutes after the cash open,
  a **daily loss limit in dollars**, an optional **stop cap in ticks**, and optional **size by score** tiers.
- What a bridge is, and what PickMyTrade costs, in `docs/RESEARCH.md` section 4.

Changes in 0.2, after the first review round:
- "Fade" is now **reversal trade (REV)**. The close-and-go-the-other-way feature at a target is now **flip**, so the two never get confused.
- All clock times are shown in **Central Time**, with New York in brackets. The script gets a timezone input.
- **Instrument profiles** added for NQ/MNQ, CL/MCL, SI/SIL with their own session and flatten presets.
- Reversal entries redesigned around **rejection plus follow-through**, with the stop off the level.
- Multi-timeframe confluence reworked around **higher-timeframe rejection at the same level**.
- Costs and slippage defaults taken from research (see `docs/RESEARCH.md`).
- Partial exits, when enabled, move the stop to break-even the moment TP1 is taken.

Companion files: `docs/DECISIONS.md` (questions, status, answers) and `docs/RESEARCH.md`
(platform, broker, cost and source-strategy findings with links). References like "D-06" point at the decision log.

---

## 0. Vocabulary

| Term | Meaning |
|---|---|
| Level | One horizontal price from the level list (previous day high, midnight open, and so on). |
| Zone | One or more levels that sit within a few ticks of each other, treated as one stronger level. |
| Reversal trade (REV) | The zone holds and we trade away from it. Long off support, short off resistance. |
| Break trade (BRK) | A candle closes through the zone and we trade in the direction of the break. |
| Target ladder | The ordered list of the next zones in the trade's direction: TP1, TP2, TP3, TP4. |
| Promotion | Price closes through the current target, so that target becomes the new floor for the stop and the next zone becomes the target. |
| Flip | At a target that rejects, close this trade and open the opposite trade from that zone. |
| Fresh | A zone that has not been touched since the daily rollover. |
| Daily rollover | 17:00 CT (18:00 NY), when the CME exchange day changes. |

---

## 1. What we are building

One TradingView Pine Script v6 **strategy** that:

- draws the key horizontal levels from higher-timeframe data and clusters the ones that overlap,
- measures how often each level type holds versus breaks and ranks the types against each other,
- fires REV signals when a level holds; break trades on a closed candle through a level exist as a switch, OFF by default,
- scores every signal 0 to 100 and only trades above a minimum,
- targets the next key level and, if price closes through it, promotes to the level after that,
- protects the trade in stages (half risk, then break-even plus cushion, then structure trail),
- reports performance by level type and by setup type,
- sends one JSON alert per event so a webhook bridge can place and manage the orders at Tradovate or a prop-firm account,
- works on NQ/MNQ first, then CL/MCL and SI/SIL, and on anything else by measuring every distance in volatility units instead of points.

"Clean working product" is defined by the acceptance tests in section 9, not by feature count.

### Not in v1 (designed now, built last or parked; see section 11)

- Flip with a size multiplier. Designed in 4.7, built in M7.
- Volume profile (POC / VAH / VAL), CME options levels, Nasdaq heatmap. Handled through a manual "custom levels" input, not computed in the script.
- Direct broker execution from Pine. Pine cannot place broker orders; the bridge does.

---

## 2. Platform facts that shape the design

| Constraint | Value | Consequence for us |
|---|---|---|
| Your plan | Premium, confirmed, with the US stocks bundle and CME Group real-time data | 20k bars per chart, Bar Magnifier, Deep Backtesting, 400 alerts, webhooks. |
| Real-time CME data | The $9.95 CME Group bundle covers CME, CBOT, COMEX and NYMEX | NQ trades on CME, CL on NYMEX, SI on COMEX. Open a CL and an SI chart once and make sure neither shows a delayed-data badge (D-01). |
| `request.*()` calls per script | 40 | Every higher-timeframe level group, MTF check, and breadth symbol costs one call. Budget in 4.1. |
| Intraday history | 20k bars on Premium; Deep Backtesting runs a strategy over all history | On a 5-minute chart 20k bars is about 3.5 months of NQ. Deep Backtesting extends that to years for statistics. |
| Bar Magnifier | Available on Premium | The backtest can use 1-minute data inside each 5-minute bar, so "hit target and stop in the same bar" is resolved properly. |
| Drawings | 500 lines, 500 boxes, 500 labels | Draw only nearby levels and recycle line objects. |
| Compiling | Only inside TradingView | I cannot compile Pine here. You paste, run, and report; I fix. Milestones are small for this reason. |

Bridge: PickMyTrade is the working assumption (D-03). It connects to Tradovate, Rithmic and ProjectX/TopstepX accounts and to the Apex, Topstep and MyFundedFutures prop firms, and its alert JSON supports stop and target updates on an open position, break-even, trailing, close, and close-then-reverse. Prop firms allow supervised automation with restrictions; details in `docs/RESEARCH.md`.

---

## 3. Architecture

One script, ten modules, in this order so that an error points at one module:

```
[A] Level Engine      -> level list (type, price, zone, fresh/touched state)
[B] Interaction       -> each touch classified HOLD / BREAK / NEUTRAL, feeds [C]
[C] Stats & Ranking   -> hold rate per type, rank, REV/BRK eligibility
[D] Setup Detector    -> REV candidates on the execution bar close (BRK only when switched on)
[E] Score             -> 0-100 from reliability, stack, first test, HTF rejection, bias
[F] Filters           -> chop, time window, news blackout, daily caps, min R:R, min distance, max risk
[G] Trade Manager     -> ladder, staged stops, trailing, soft targets, partials, flatten, flip
[H] HTF Confluence    -> rejection checks and optional trend votes from 5m / 15m / 1h / 4h
[I] Bias Inputs       -> opens, Mag 7, VIX (NQ/MNQ only), sectors
[J] Output            -> lines, labels, table, alert JSON
```

Data flow: A -> B -> C; D reads A, C, H, I; E scores D; F gates E; G manages what passes; J shows everything.

### Rules that apply everywhere

1. **No repainting.** Levels come only from completed periods (`[1]` offset with lookahead on) or
   from opens that are known the moment a period starts. Signals evaluate on bar close only.
   A signal that was on the chart stays on the chart.
2. **Every distance is in volatility units with a tick floor.** Level geometry (cluster tolerance,
   touch tolerance, break confirmation, stop buffer, minimum target distance) uses a **daily ATR
   unit**, so the level set is identical on the 1m and 5m chart and transfers across symbols.
   Candle-size and trailing distances use the execution-timeframe ATR. Section 6 has the numbers.
3. **Stops only tighten.** The trade manager never widens a stop.
4. **One position at a time.** Flip is the only exception, and it closes first, then opens.
5. **Bar-close truth.** Backtest and live alerts both come from confirmed bars, so what the backtest
   shows is what the bridge receives.
6. **All times in one timezone input.** Default `America/Chicago`. Every session and time-of-day
   input is read in that zone. The midnight open stays anchored to 00:00 New York because that is
   how the level is defined; it shows as 23:00 CT. An option lets you anchor it to local midnight instead.

---

## 4. Module specifications

### 4.1 [A] Level Engine

Level types. Each has a short code used on labels and in the stats table.

| Code | Level | Source | Refreshes |
|---|---|---|---|
| PDH / PDL / PDM | Previous day high / low / mid | chart candles grouped by exchange day, so each line starts at the candle that made it | daily rollover |
| DO | Daily open (exchange open, 17:00 CT on CME) | `D` open | daily rollover |
| MO | Midnight open (00:00 NY = 23:00 CT) | first chart bar at or after the anchor | daily |
| PWH / PWL / PWM / WO | Previous week high / low / mid, weekly open | `W` | weekly |
| PMH / PML / PMM / MOO | Previous month high / low / mid, monthly open | `M` | monthly |
| PQH / PQL / PQM / QO | Previous quarter high / low / mid, quarterly open | `3M`, previous bar and open | quarterly |
| YO / YH / YL / YM | Yearly open, current-year high / low / mid as of the prior daily close | `12M` open; running max/min on the `D` series | daily |
| P4H / P4L / P4M / P4O / 4HO | Previous 4-hour high / low / mid / open, current 4-hour open | chart candles grouped by 4-hour boundary | every 4 hours |
| MNH / MNL / MNM | Monday range high / low / mid (full Sunday 17:00 CT to Monday 16:00 CT session) | chart bars | weekly |
| AH / AL / AO | Asia session high / low / open, last completed session | chart bars + session window | per session |
| LH / LL / LO | London session high / low / open | chart bars + session window | per session |
| NH / NL / NO | New York (main) session high / low / open, per instrument profile | chart bars + session window | per session |
| CUS | Custom levels typed in (options levels, POC, VAH, VAL, anything) | text input | manual |
| SR | Untagged support / resistance: a price where swing highs and lows on the `srPivotTF` chart (default 4-hour, where Socrates draws his "blue lines") have clustered `srMinTouches` or more times within the last `srLookbackDays` days. Entry-eligible like any labeled level; the touch count feeds the stack score, and an SR line that sits on a labeled level makes a stronger zone, which is exactly the alignment he checks on the 1-hour. | 4h pivots, clustered | rolling |
| STR | Structure swing high / low from 15m pivots. **Targets only**, never entries. | pivots | rolling |
| HOD / LOD | Today's developing high / low. **Targets only**, never entries. | chart bars | live |

STR, HOD and LOD are not drawn unless one of them is the active TP1 or TP2 of an open trade.

**Session windows** (killzone style, D-06), Central Time with New York in brackets:

| Session | Default | Applies to |
|---|---|---|
| Asia | 19:00 to 23:00 CT (20:00 to 00:00 NY) | all profiles |
| London | 01:00 to 04:00 CT (02:00 to 05:00 NY) | all profiles |
| New York, all futures profiles | 08:30 to 16:00 CT (09:30 to 17:00 NY), cash open to futures close | NQ, MNQ, ES, MES, CL, MCL, SI, SIL, GC, MGC |
| New York, pit-hour alternatives | 08:00 to 13:30 CT for crude, 07:20 to 12:30 CT for metals, available in the inputs | CL, MCL, SI, SIL |

Session levels **develop live** while their session runs and freeze when it ends (D-59). For
trading, a developing session extreme is a target only; it becomes an entry level once the
session has completed. A "Completed only" switch shows the last finished session instead.

**Request budget.** Day, week, month and 4-hour levels are measured from the chart's own candles,
which is what gives each line its origin candle. Requests: D 1 (daily ATR, year high and low),
W 1 and M 1 as fallbacks when the chart history is too short, 3M 1, 12M 1 = 5. HTF rejection
checks 5 / 15 / 60 / 240 = 4. Mag 7 = 7. QQQ = 1. VIX = 1. Sectors = 11 (off by default).
Total 29 of 40 with everything on, 18 with sectors off, 9 on CL or SI where breadth is off.
Each request returns a tuple such as `[high[1], low[1], open]` so one call serves several levels.

**Level instance identity.** An instance is (type, price, born-at time). When its period rolls the
old instance retires and a new one is born. Statistics attach to instances, so "first interaction"
is unambiguous.

**Clustering.** Sort active levels by price and walk the list; any level within `clusterTol` of the
running zone joins it. A zone stores min price, max price, member codes, and member count. Zone
strength = member count. The zone is what gets touched, traded, broken, and targeted; the statistics
still credit every member type.

`clusterTol = max(clusterUnit * dailyATR, clusterTicks * mintick)`. Defaults 0.02 daily ATR, floor
4 ticks. On NQ with a 300-point daily ATR that is 6 points.

**Fresh state.** A zone is fresh until price trades within `touchTol` of it after the daily rollover (D-11).

**Drawing** (D-57, D-58). Every level is drawn by default, like the Spaceman indicator; a switch
limits drawing to levels within `drawRange` daily ATRs of price. **Every level is its own line**,
starting at the candle that made it and ending some bars to the right of the current candle, where
its label sits; a right-anchored fixed-length mode is the alternative. Labels default to full names
with short codes as the option, in a chosen text size, optionally with the price. Levels within
the share distance (`mergeUnit`, default the touch tolerance) share one tag so names do not
overlap, and tags that would still overlap step right into columns sized by name length. Zones
for trading are built from the cluster tolerance in M2 and are not drawn as boxes. Touched and fresh levels look
the same; the score carries that information (D-36).

### 4.2 [B] Interaction Classifier

Runs on every execution bar for every active zone. It produces one verdict per zone instance for
the statistics and produces touch / reject / break events for the setup detector.

States per zone: `IDLE -> TOUCHED -> (HELD | BROKE | NEUTRAL)`.

- **Approach side.** When a bar first trades within `touchTol` of the zone, record which side price
  came from using the prior bar's close. From above means the zone acts as support; from below
  means resistance.
- **BROKE.** A bar closes beyond the far side of the zone by at least `breakConfirm`
  (default 0.03 daily ATR, floor 4 ticks).
- **HELD.** Before any BROKE, price closes at least `holdConfirm` away from the zone on the approach
  side (default 0.10 daily ATR), or reaches the next zone, whichever comes first.
- **NEUTRAL.** Neither happens within `verdictWindow` bars (default 30 execution bars). Not counted.
- Only the **first** interaction per instance counts toward the statistics. Later interactions still
  generate setup events.

### 4.3 [C] Stats & Ranking

Per level type: `holds` and `breaks` running counters (`var` arrays, persisted across the loaded history).

```
holdRate = (priorN * priorRate + holds) / (priorN + holds + breaks)
```

`priorRate` and `priorN` are inputs per type (defaults 0.5 and 0, so the script starts neutral).

**Where the counts come from, in plain language (D-23).** The script can only count what is on the
chart. A 5-minute NQ chart holds about 3.5 months of bars on Premium, so a level type like the
monthly high will have only a handful of examples and its hold rate will bounce around. Two things
fix this without extra work from you: run **Deep Backtesting** once (a Premium feature that runs
the strategy over every bar TradingView has, years of them) and read the hold rates off the table,
then type those into the `priorRate` / `priorN` inputs so the live chart starts from real numbers.
An offline study on downloaded data is the stronger version of the same idea and is optional (M8).

Ranking: sort types by `holdRate` descending. `rankPct` is the percentile position (top = 100).

Eligibility (D-24). Default `rankGate = OFF`: every level type may be traded both ways and the
ranking only moves the score, so a type that keeps breaking scores low for reversals and high for
breaks without being banned. `rankGate = ON` is the switch for after the research: top half by hold
rate may be traded as reversals only, bottom half as breaks only, types with fewer than
`minSamples` interactions allowed both ways. Your starting belief that 4-hour highs and lows are the
strongest becomes the seed for the priors once we have measured it in the Deep Backtesting run.
With break trades off (D-50) the ranking simply favors the strongest types for reversals.

Table (toggle): type, N, hold %, break %, rank, preferred (REV / BRK), trades, win %, net P&L.
Footer: REV versus BRK totals.

### 4.4 [D] Setup Detector

Evaluated on the execution-bar close. At most one new signal per bar; ties resolved by score.

**REV (zone holds).** Built around how you trade it by hand: a wick off the level, price starting
to turn, entry without waiting for a perfect close, sometimes past the level. The bot needs a
closed bar to act on, so it uses two bars:

1. **Rejection bar.** Trades into the zone (it may extend past it) and shows one of these, each toggleable:
   - *Wick rejection*: the wick on the zone side is at least `wickRatio` (default 0.5) of the bar
     range, the close is back on the approach side, and the bar range is at least `minBarATR`
     (default 0.6 execution ATR) so dojis do not qualify.
   - *Poke and close back*: the bar traded through the zone's far side and closed back on the approach side.
   - *Engulfing*: this bar's body engulfs the prior bar's body in the rejection direction, and the pair touched the zone.
2. **Follow-through bar.** The next bar closes in the rejection direction (for a long: a green
   close above the zone's near edge). Entry at that close, which the emulator fills at the next bar open.
   - Option `strongSkip` (default OFF): if the rejection bar's wick is at least 60 % of its range and
     it closes in the far third, enter at the rejection bar's close without waiting.
3. The zone is REV-eligible ([C]) and the filters pass ([F]).
4. **Volume confirmation** (D-52, ON by default on the Index profile, OFF elsewhere): the
   follow-through bar's volume is at least `volConfirmMult` (default 1.0) times the 20-bar average
   volume. Socrates enters at a key level only with volume behind the move; this is the bot's
   version of that rule. Your call: it applies to NQ and MNQ only.

Two more entry triggers are planned as options, not defaults:

- **HTF rejection plus 1-minute trigger (M6).** Chart on 1m; the rejection bar is detected on the
  5m or 15m; entry when the first 1m bar after that candle closes in the rejection direction.
  Closest to your manual timing.
- **Sweep, reclaim, retest (M7).** Price wicks through the zone, closes back inside, then a limit
  order rests at the zone edge for `retestBars` bars. This is the Socrates-style entry.

Stop (D-22): the far edge of the zone plus `stopBuffer`, default 0.03 daily ATR with a 4-tick floor
(about 9 NQ points on a 300-point ATR day). Options: the rejection bar's extreme, or the farther of
the two. A separate cap, `maxStopTicks` (default 0 = off), rejects any setup whose stop would be
wider than that many ticks. Your manual habit is a 50-tick stop on MNQ; a bot that enters one bar
later than you do needs more room, so the right number comes out of the backtests (D-45).
Ladder: the next zones in the bounce direction, skipping any closer than `minTargetDist`.

**BRK (zone fails). Optional, OFF by default, built in M7 (D-50).** The core of this strategy is
the reversal off a pivot and the trail to the target. A level that price rips through is already
handled by the ladder, which keeps a running trade alive through it. A standalone break entry only
matters when we happen to be flat at that moment, so it is a switch for backtest comparison, not
part of the base product. Your rule: entering straight off a breakout is bad, entering on the
retest after a break is fine. So the switch means **break, then retest, then enter**; there is no
immediate breakout entry. Socrates's own go-to at the daily open, daily high and daily low is
exactly that (D-53). Rules, for when it is on:

1. A bar closes beyond the zone's far side by at least `breakConfirm`. A wick through does not count.
2. Optional momentum filter: bar body at least `minBreakBodyATR` execution ATRs.
3. The zone is BRK-eligible and the filters pass.

Entry: after the confirmed close through, rest a limit at the zone edge for up to `retestBars` bars
and cancel if unfilled; the retest must hold, meaning no close back through the zone while the
limit rests. Stop: back inside the zone (zone edge plus buffer on the wrong side). Option
"failed-break exit" (default ON): if a bar closes back through the zone before TP1, exit at that
close instead of waiting for the stop. Ladder: the next zones beyond the broken one.

Both setups require:

```
(TP1 - entry) / (entry - stop) >= minRR
stop distance <= maxRiskATR * dailyATR
TP1 distance  >= minTargetDist
```

### 4.5 [E] Score (0 to 100)

| Component | Points | Rule |
|---|---|---|
| Reliability | 0 to 40 | `rankPct * 0.4`, using hold-rank for REV and break-rank for BRK; unknown type = 20 |
| Stack | 0 to 20 | 1 member = 5, 2 = 12, 3 or more = 20 |
| Level history today | 0 to 15 | fresh, first test = 12; already rejected cleanly today (classifier said HELD) = 15; touched with no verdict = 6; broken through earlier today = 3 |
| HTF rejection | 0 to 10 | timeframes among 5m / 15m / 1h / 4h whose last completed candle rejected the same zone: 0 = 0, 1 = 5, 2 = 8, 3 or more = 10. A bonus, never a requirement. |
| Bias | 0 to 15 | with bias = 15, neutral = 7, against = 0 |

`minScore` default 60. Weights are inputs. A fresh level of a top-ranked type with no
higher-timeframe help and neutral bias scores 40 + 5 + 12 + 0 + 7 = 64, so first tests trade on
their own. The label shows the total and the HTF count, for example `REV PDL+AL  S 78  HTF 1/4`.

### 4.6 [F] Filters

- **Chop.** Band = `chopPct` of price (default 0.25 %) or `chopATR` daily ATRs (option). Window =
  `chopMinutes` (default 30), converted to bars from the chart timeframe. If highest minus lowest
  over the window is within the band, chop is ON and the band is frozen. Chop turns OFF on the first
  close outside the frozen band. No entries while ON. We tune this after the first backtests (D-28).
- **Allowed sessions.** Three checkboxes, Asia / London / New York, plus an optional custom window.
  Entries only inside a checked session. Index profile default: New York only. Energy and metals:
  all three, since you trade them at any time. For 24/7 symbols the filter can be disabled.
- **Entry cutoff.** No new entries after `entryCutoff`, default 15:00 CT, so a trade has time to work before the flatten.
- **Opening blackout.** No entries for `openingBlackoutMin` minutes after the New York open, default
  30 (08:30 to 09:00 CT). Your own stats put that window under a 20 % win rate with most stops hit
  within 2 minutes, and you would rather skip that trade than shrink it (D-43).
- **Flatten.** At `flattenTime` close everything and cancel orders. **15:55 CT** for every futures profile (D-10).
- **News blackout (new, D-40).** No entries from `blackoutBefore` to `blackoutAfter` minutes around
  the times in a text input. Default `07:30, 09:00` CT, 2 minutes before and 5 after, ON.
  Energy profile adds Wednesday 09:30 CT. Tradovate aggregates data during bursts and slippage is
  4 to 8 ticks on news days, so this protects both the fills and the stats.
- **Caps, all OFF for backtesting, all available as settings.** `maxSignalsPerDay` (0 = off),
  `maxLossesPerDay` (0 = off), `maxDailyLossPct` (percent of account, 0 = off; you want 2 to 3 % once
  live), `dailyTargetPct` (0 = off; you want 3 to 5 % once live). A tripped cap blocks new entries
  until the next daily rollover. The profit target **never closes an open trade**: a trade that is
  trailing keeps trailing past the target. One open position at a time always.
- **Re-entry.** After a stop-out the same zone is blocked for `cooldownMinutes` (default 12, which is
  12 candles on the 1-minute chart and about 2 on the 5-minute), and at most one re-entry per zone per day.
- **Thin-market filter (option, OFF).** Skip entries when the last 20 candles' volume is below
  `thinVolumePct` of the same window's 20-day average (default 40 %). Meant for CL and SI when the
  1-minute chart gets unreadable on low volume (D-49).
- **Geometry.** `minRR` (default 1.0), `minTargetDist` (default 0.15 daily ATR, floor 10 ticks),
  `maxRiskATR` (default 0.35 daily ATR).
- **Bias gate (option).** ON: only trade in the bias direction. OFF (default): bias only affects the score.

### 4.7 [G] Trade Manager

State per position: `entry, initStop, curStop, R (= |entry - initStop|), ladder[], tpIdx, stage, brokenLevels[], partialTaken`.

**Staged stops** (D-32, confirmed). Thresholds in R, measured on the bar's high or low.

| Stage | Trigger | Stop moves to |
|---|---|---|
| 0 INITIAL | entry | `initStop` |
| 1 RISK-HALVED | +0.5R | halfway between `initStop` and entry |
| 2 BREAK-EVEN+ | +1.0R | entry plus cushion, cushion = max(`beTicks`, `beATR` execution ATRs) |
| 3 TRAILING | +1.5R, or any promotion | max(`curStop`, structure stop, chase stop), re-checked every bar |

Structure stop = the most recent confirmed swing low (for a long) minus `structATR` execution ATRs.
Chase stop = close minus `chaseATR` execution ATRs. Swings come from `ta.pivotlow / ta.pivothigh`
with a right-side lookback, so they are confirmed and do not repaint.

**Target ladder.** At entry the manager stores the next zones in the trade direction (up to
`maxLadder`, default 4). On every bar close, if the bar's extreme reached `ladder[tpIdx]`:

- The bar closed beyond the target by at least `contConfirm` (default 0.03 daily ATR), and, with
  `promoteNeedsVolume` ON (default), its volume is at least the 20-bar average: **promote**. His
  hold rule is "if the volume is following suit we can play the game"; without volume the level is
  treated as reached and the trade exits.
  `tpIdx += 1`, `curStop = max(curStop, target - stopBuffer)` so the broken level becomes the floor,
  stage becomes 3.
- Otherwise: **soft-target exit** at this bar's close. Price reached the level and did not accept it.
- Ladder exhausted: stay in on trailing only until stopped or flattened.
- Option `hardTP1`: rest a limit at TP1 instead (the classic take-profit) for the simple version.

Worked example, long REV off PDL 19,850, stop 19,841 (R = 9 points). Ladder above: MO 19,900,
P4H 19,940, PDH 20,010.

1. Price reaches 19,900 and the 5-minute bar closes at 19,896. Touched, not accepted. Exit at 19,896, +46 points.
2. Instead the bar closes at 19,912, which is more than 9 points through. Promote: stop moves to
   19,894, the target becomes 19,940, trailing turns on.
3. Price reaches 19,940 and closes at 19,935. Exit at 19,935, +85 points.
4. If price had also closed through 19,940 and 20,010, the ladder is exhausted and the trade rides
   the structure trail until the stop is hit or the flatten time arrives.

**Partial exits** (D-33, OFF by default). When ON: close `partialPct` (default 50 %) at the first
touch of TP1, and at that same bar move the stop on the remainder to entry plus cushion, so no
risk remains on the trade. The remainder then follows the ladder. Needs at least 2 contracts.

**Flip** (D-35, toggle, OFF by default, built in M7). Your version: long 2 MNQ toward a target,
and a resting **limit order for 4 MNQ** sits at the target. When price touches the target the limit
fills, the 2 long are closed at the level, and you are short 2 from the level, targeting the ladder
back the way you came. Inputs: `flipEnabled`, `flipQty` (net size of the new position, default =
base size), so the limit is always `open size + flipQty`.

Rules around it:

- The flip limit is armed only when the target zone is REV-eligible in the opposite direction and
  the would-be flip trade clears `minScore` with its confirmation component unknown. At a weak
  target the normal soft-target and ladder logic runs instead.
- While a flip limit is armed, TP1 for that trade is hard (the limit itself), so there is no
  promotion at TP1. That is the trade-off: a level that rips through fills the flip, and the new
  position stops out quickly off the level for a small loss instead of riding the ladder.
- Option `flipConfirmed` (OFF by default): wait for the rejection bar plus follow-through at the
  target, like a normal REV entry, instead of resting a limit. Later fill, fewer rip-through losses.
- The flipped position is a normal REV trade from then on: stop off the level, staged stops, its own ladder.

Flatten: `flattenTime` closes everything.

Order mapping in Pine: `strategy.entry` (market or limit), `strategy.exit(stop = curStop)`
re-issued every bar, `strategy.close` for soft-target, partial and flatten exits, `strategy.cancel`
for stale limits. `process_orders_on_close = false`, so market fills happen at the next bar open,
the same as a bridge would fill them.

### 4.8 [H] HTF Confluence

Your higher-timeframe read is about what the candles do at the level, so that is the primary check.

- **HTF rejection (primary).** For each of 5m, 15m, 1h, 4h, fetch the last *completed* candle
  (`[1]`, lookahead on). If it traded into the current zone and closed back on the approach side
  with a wick of at least `htfWickRatio` (default 0.4) of its range, that timeframe counts as a
  rejection. The count feeds the score (4.5) and the label. It is a bonus: a first test with no
  higher-timeframe help still trades.
- **Trend votes (optional, OFF by default).** Close above or below EMA(`mtfEmaLen`, default 50) on
  each timeframe; `minVotes` aligned required. Kept for anyone who wants a trend gate.

### 4.9 [I] Bias Inputs

All optional. Score-only unless the bias gate is on (D-29).

- **Opens**: price above or below the daily open, the midnight open, and the NY open, +1 / -1 each.
  Net +2 or more is bullish, -2 or less is bearish. All profiles.
- **Mag 7 breadth**: AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA above today's open. 5 or more
  bullish, 2 or fewer bearish. **NQ and MNQ only**, detected from the symbol root, overridable.
  Valid only while US stocks trade (08:30 to 15:00 CT by default), neutral otherwise.
- **VIX**: the VIX moving the opposite way to NQ over the last `vixBars` 5-minute bars (default 3)
  counts as agreement, the same way counts as against, flat is neutral. Socrates shorts NQ at a
  level when the VIX is turning up off its own level at that moment. **NQ and MNQ only.**
- **Sector breadth**: the 11 SPDR sector ETFs above their open. OFF by default.
- **Heatmap**: not readable from Pine. Mag 7 breadth plus QQQ-versus-open is the stand-in.

Bias = majority of the enabled sources; a tie is neutral.

### 4.10 [J] Output

- Level lines and zone boxes (4.1). Current stop line and TP1 / TP2 lines while in a trade.
- Signal label on the entry bar: `LONG REV PDL+AL  S 78  E 19876.0  SL 19867.0  T1 19920 (MO)  HTF 2/4`.
- Management markers: a small triangle when the stop moves stage, a diamond when a target is promoted.
- Stats table (4.3), position selectable, off switch.
- Alerts: one `alert()` per event. The body follows the PickMyTrade field names so it can be pasted
  into their alert setup once D-03 is confirmed. Fields used: `symbol`, `data` (buy / sell / close),
  `quantity`, `price` (limit entries only), `sl`, `tp` (hard-TP mode only), `update_sl`,
  `reverse_order_close`. Our own fields ride along for logging: `event`, `setup`, `level`, `score`, `tp1`, `tp2`.

```json
{"symbol":"MNQ","data":"buy","quantity":2,"sl":19867.0,"reverse_order_close":true,
 "event":"ENTRY","setup":"REV","level":"PDL+AL","score":78,"tp1":19920.0,"tp2":19965.0}
```

Events: ENTRY, STOP_MOVE (`update_sl`), TP_PROMOTE (`update_sl`), PARTIAL (close with quantity),
EXIT (close), FLATTEN (close), FLIP (one resting limit for open size plus `flipQty`, or close then
opposite entry in confirmed mode). Exact field names get verified
against the bridge on a Tradovate sim account in M4.

---

## 5. Cross-symbol behaviour

### 5.1 Units

- `dailyATR`: 14-period ATR on the daily series, taken from the same `D` request, as of the previous
  daily close. Used for all level geometry.
- `execATR`: 14-period ATR on the chart timeframe. Used for candle-size filters, the break-even
  cushion, and trailing.
- `syminfo.mintick` and `syminfo.pointvalue` for tick floors, P&L, and sizing.

### 5.2 Instrument profiles (D-12, D-41)

Detected from the symbol root, overridable with an input. Times in CT (NY in brackets).

| Profile | Symbols | Main session (NH/NL/NO) | Allowed sessions | Entry cutoff | Flatten | VIX / Mag 7 | Notes |
|---|---|---|---|---|---|---|---|
| Index | NQ, MNQ, ES, MES | 08:30 to 16:00 (09:30 to 17:00) | New York | 15:00 | 15:55 | NQ / MNQ only | Opening blackout 08:30 to 09:00. Cash close 15:00 CT, futures close 16:00 CT |
| Energy | CL, MCL | 08:30 to 16:00 (09:30 to 17:00); pit hours 08:00 to 13:30 available | Asia, London, New York | 15:00 | 15:55 | off | Settlement 13:30 CT. EIA report Wednesday 09:30 CT is in the news blackout |
| Metals | SI, SIL, GC, MGC | 08:30 to 16:00 (09:30 to 17:00); pit hours 07:20 to 12:30 available | Asia, London, New York | 15:00 | 15:55 | off | Silver settles 12:25 CT, gold 12:30 CT |
| Generic | anything else | 08:30 to 15:00 | New York | 15:00 | 15:55 | off | Crypto: sessions and flatten off |

Your May rules said no Asia trading on NQ, which is why the index profile defaults to New York only.
Your best-hours claim for CL and SIL at the 19:00 CT Asia open stays unmeasured, and you decided the
old journal would only show personal tendencies (D-47), so the energy and metals profiles allow every
session. The stats table reports P&L per session so the bot's own backtests settle it.

Cost defaults per profile are in `docs/RESEARCH.md`; they go into the strategy Properties, which
Pine cannot set per symbol from an input.

### 5.3 Sessions per asset class

- CME futures: exchange day 17:00 to 16:00 CT; sessions as above.
- Stocks: the exchange day is the regular-hours day unless the chart shows extended hours. Overnight
  sessions produce no bars, so Asia and London levels are simply absent. The engine must tolerate a
  missing session.
- Crypto: 24/7, daily bar at 00:00 UTC on most exchanges, time window off by default.

### 5.4 Where the statistics come from

Live counters on the chart now, Deep Backtesting to seed the priors once the strategy runs (4.3),
an offline study later if we want more (M8).

---

## 6. Proposed default parameter sheet

| Group | Parameter | Default | Unit |
|---|---|---|---|
| General | timezone | America/Chicago | |
| General | midnight open anchor | New York | |
| Levels | clusterUnit / clusterTicks | 0.02 / 4 | daily ATR / ticks |
| Levels | touchTol | 0.01 / 2 | daily ATR / ticks |
| Levels | drawRange | 1.0 | daily ATR |
| Levels | srLevels / srMinTouches / srLookbackDays / srPivotTF | ON / 3 / 10 / 240 | switch / touches / days / minutes |
| Interaction | breakConfirm | 0.03 / 4 | daily ATR / ticks |
| Interaction | holdConfirm | 0.10 | daily ATR |
| Interaction | verdictWindow | 30 | execution bars |
| REV | wickRatio / minBarATR | 0.5 / 0.6 | ratio / exec ATR |
| REV | strongSkip | OFF | |
| REV | volConfirm / volConfirmMult | ON for Index, OFF elsewhere / 1.0 | switch / multiple of the 20-bar average |
| REV | stopBuffer (off the level) | 0.03 / 4 | daily ATR / ticks |
| REV | maxStopTicks | 0 (off) | ticks |
| BRK | breakTrades (break, retest, enter) | OFF | switch |
| BRK | minBreakBodyATR | 0.5 | exec ATR |
| BRK | retestBars | 6 | execution bars |
| Filters | minScore | 60 | points |
| Filters | minRR | 1.0 | R |
| Filters | minTargetDist | 0.15 / 10 | daily ATR / ticks |
| Filters | maxRiskATR | 0.35 | daily ATR |
| Filters | chopPct / chopMinutes | 0.25 % / 30 | percent / minutes |
| Filters | allowed sessions / entry cutoff / flatten | per profile / 15:00 / 15:55 | CT |
| Filters | news blackout | 07:30, 09:00 CT, 2 before / 5 after | minutes |
| Filters | openingBlackoutMin | 30 | minutes |
| Filters | maxSignalsPerDay / maxLossesPerDay | 0 (off) / 0 (off) | count |
| Filters | maxDailyLossPct / dailyTargetPct | 0 (off) / 0 (off), later 2 to 3 / 3 to 5 | percent of account |
| Filters | cooldownMinutes | 12 | minutes |
| Filters | thinMarket / thinVolumePct | OFF / 40 | percent |
| Stats | rankGate / minSamples | OFF / 30 | switch / interactions |
| Manager | stage thresholds | 0.5 / 1.0 / 1.5 | R |
| Manager | beTicks / beATR | 2 / 0.02 | ticks / exec ATR |
| Manager | structLookback / structATR / chaseATR | 5 / 0.5 / 2.0 | bars / exec ATR |
| Manager | maxLadder / contConfirm | 4 / 0.03 | levels / daily ATR |
| Manager | promoteNeedsVolume | ON | switch |
| Bias | vixBars | 3 | 5-minute bars |
| Manager | partials / partialPct | OFF / 50 | percent |
| Manager | flip / flipQty / flipConfirmed | OFF / base size / OFF | contracts |
| Sizing | baseQty | 2 | contracts |
| Sizing | sizeByScore tiers (60 to 69 / 70 to 84 / 85 and up) | OFF (2 / 3 / 5) | contracts |
| Score | weights: reliability / stack / level history / HTF / bias | 40 / 20 / 15 / 10 / 15 | points |
| HTF | timeframes / htfWickRatio | 5, 15, 60, 240 / 0.4 | minutes / ratio |
| HTF | trend votes | OFF | |
| Costs | commission / slippage | per profile, see RESEARCH.md | per side / ticks |

Every parameter becomes an input with a tooltip. No magic numbers in the code.

---

## 7. Milestones

Each milestone is a complete, runnable script that you paste into TradingView and check against
its acceptance list before we move on. Nothing from a later milestone leaks into an earlier one.

| # | Deliverable | You verify |
|---|---|---|
| M0 | This plan, decisions recorded | Answer `docs/DECISIONS.md` |
| M1 | Level engine as an **indicator**: all labeled level types, custom levels, clusters, labels, fresh / touched state, timezone, profiles | Levels match what you would draw by hand on NQ for 3 sessions. The same script on CL and SI draws sensible levels. No level moves on bar replay. |
| M2 | SR touch-cluster levels, interaction classifier, stats table | SR levels land where you would draw untagged support and resistance. Table counts change only on bar close. Spot-check 10 touches by eye. |
| M3 | Reversal setup detector, score, labels, signal alerts (still an indicator) | Signals appear where you would expect reversal trades. Scores read right. One alert per signal. |
| M4 | Strategy v1: entries, initial stop, hard TP1, filters, caps, flatten, costs, bridge JSON checked on a sim account | Backtest runs. Trade list matches the labels. Flat at the profile's flatten time every day. |
| M5 | Trade manager: staged stops, ladder, soft targets, trailing, partials | Replay 5 trades and confirm every stop move and promotion by hand. |
| M6 | HTF rejection, bias inputs, score integration, 1-minute trigger mode | Labels show HTF x/4. Bias toggles change scores as expected. |
| M7 | Flip, break trades as a switch, VWAP / 200 EMA confluence, sweep-reclaim-retest entry | A flip opens only when the target zone shows a qualifying REV setup. Break trades stay off unless switched on. |
| M8 | Python study for priors (optional) | A priors table produced from real data. |

Repo layout once code starts: `pine/l2l.pine` (the script), `pine/CHANGELOG.md`, `docs/`
(plan, decisions, research, test checklist), `research/` (M8), `reference/` (your beta script,
the LuxAlgo output, links).

---

## 8. Working agreement

- I write Pine here; you compile in TradingView. When it fails, paste the first error line with its
  line number. When it runs, send a screenshot of one session.
- Each milestone ships with a checklist. We do not start the next until the checklist passes on NQ or MNQ.
- **Every backtest session gets a log entry** in `docs/BACKTEST_LOG.md`: settings used, symbol and
  dates, the headline stats, what went wrong, and what we changed before the next session. I write
  the entry from what you report and ask for anything missing. `CLAUDE.md` in the repo root carries
  this rule so any future session follows it.
- One file, module headers from section 3, every parameter an input.
- Defaults are frozen per instrument profile, never per symbol, to limit overfitting.

---

## 9. Acceptance tests for "working"

1. Compiles in Pine v6 with no warnings.
2. No repainting: bar replay from a day earlier shows the same levels, signals, and exits as the live chart.
3. Levels are identical on the 1m and 5m chart of the same symbol at the same moment.
4. Alerts: exactly one ENTRY alert per signal and one EXIT per exit, none on historical bars.
5. The trade list matches the labels one for one.
6. Runs on NQ1!, MNQ1!, CL1!, MCL1!, SI1!, SIL1! and BTCUSD without errors and without NQ-specific numbers.
7. Stats table totals equal the number of classified interactions.
8. With costs set, the backtest still reports metrics per level type and per setup type.
9. Changing the timezone input moves every session and time input together and nothing else.

---

## 10. Risks and honest caveats

- **Bar-close granularity.** Turn Bar Magnifier on for backtests so intrabar order is resolved with 1-minute data.
- **Thin statistics.** Rankings on a few months of data are noise. Run Deep Backtesting and seed the priors before trusting the ranking.
- **Overfitting.** With about 40 parameters it is easy to tune a backtest that will not repeat. Hence frozen defaults per profile.
- **Two data feeds.** Alerts fire on TradingView's CME feed; orders fill on Tradovate's. Small mismatches are normal, larger ones happen during news bursts when Tradovate aggregates data. The news blackout and 2-tick slippage setting account for this.
- **Prop-firm rules.** Apex and Topstep allow supervised automation, not unattended bots. Rules change; confirm with the firm before running live.
- **Live stop modification** depends on the bridge. PickMyTrade documents `update_sl`; M4 verifies it on a sim account.
- **Your own numbers.** Your May rules note that a quarter of your trades ran into profit and still
  closed as losers. The staged stops exist for exactly that; keep them on when comparing backtests to your manual results.

---

## 11. Parked ideas (not in v1)

- Flip with a size multiplier (designed in 4.7, built in M7).
- Volume profile POC / VAH / VAL computed in-script (heavy; use the custom-levels input instead).
- CME options and gamma levels (paid feed; custom-levels input).
- Nasdaq heatmap (not accessible from Pine; Mag 7 breadth stands in).
- ICT fair value gaps and consequent encroachment as extra levels (possible later as a level type; not in the source strategy's core).
- Lower-timeframe intrabar confirmation of target rejection via `request.security_lower_tf`.
