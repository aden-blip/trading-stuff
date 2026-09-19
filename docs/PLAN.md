# Level-to-Level (L2L) Strategy: Design Plan

Status: PLANNING. No code yet. Version 0.1, 2026-09-19.

Companion file: `docs/DECISIONS.md` holds every open question (D-01 to D-39) with a
recommended default. Answers get recorded there before the matching milestone is built.
References like "D-06" in this file point at that list.

---

## 1. What we are building

One TradingView Pine Script v6 **strategy** that:

- draws the key horizontal levels from higher-timeframe data and clusters the ones that overlap,
- measures how often each level type holds versus breaks and ranks the types against each other,
- fires FADE signals when a level holds and BREAK signals when a level fails on a closed candle,
- scores every signal 0 to 100 and only trades above a minimum,
- targets the next key level and, if price closes through it, promotes to the level after that (the "target ladder"),
- protects the trade in stages (half risk, then break-even plus cushion, then structure trail),
- reports performance by level type and by setup type,
- sends one JSON alert per event so a webhook bridge can place and manage the orders at the broker,
- works on NQ/MNQ first, and on other symbols by measuring every distance in volatility units instead of NQ points.

"Clean working product" is defined by the acceptance tests in section 9, not by feature count.

### Not in v1 (designed now, built last or parked; see section 11)

- Reverse-and-add at a target (stop-and-reverse with a size multiplier). Designed in 4.7, built in M7.
- Volume profile (POC / VAH / VAL), CME options levels, Nasdaq heatmap. Handled through a manual
  "custom levels" input, not computed in the script.
- Direct broker execution from Pine. Pine cannot place broker orders; the bridge does.

---

## 2. Platform facts that shape the design

These are TradingView facts, not choices.

| Constraint | Value | Consequence for us |
|---|---|---|
| `request.*()` calls per script | 40 (64 on Ultimate) | Every higher-timeframe level group, MTF vote, and breadth symbol costs one call. Budget in 4.1. |
| Intraday history per plan | Free 5k, Essential/Plus 10k, Premium 20k bars. Deep Backtesting (Premium and up) runs a strategy over all history. | On a 1-minute chart 10k bars is about 7 sessions. Statistics measured inside the script are thin on low timeframes. See 5.3. |
| Bar Magnifier | Premium and up | Without it the backtest sees only OHLC of each execution bar, so "hit target and stop in the same bar" is guessed. |
| Drawings | 500 lines, 500 boxes, 500 labels | Draw only nearby levels and recycle line objects. |
| Webhooks | Paid plan | Needed for any bot. |
| Compiling | Only inside TradingView | I cannot compile Pine here. You paste, run, and report; I fix. Milestones are small for this reason. |

Bridge candidates for a bot: PickMyTrade (Tradovate, Rithmic, IBKR, TradeStation) or TradersPost
(Tradovate, stocks, crypto). The bridge must accept "modify stop" messages for the trailing logic to
work live. Decision D-03.

---

## 3. Architecture

One script, ten modules, in this order so that an error points at one module:

```
[A] Level Engine      -> level list (type, price, zone, fresh/touched state)
[B] Interaction       -> each touch classified HOLD / BREAK / NEUTRAL, feeds [C]
[C] Stats & Ranking   -> hold rate per type, rank, fade/break eligibility
[D] Setup Detector    -> FADE and BREAK candidates on the execution bar close
[E] Score             -> 0-100 from reliability, stack, first test, MTF, bias
[F] Filters           -> chop, time window, daily caps, min R:R, min distance, max risk
[G] Trade Manager     -> ladder, staged stops, trailing, soft targets, flatten, (reversal)
[H] MTF Confluence    -> votes from 5m / 15m / 1h / 4h
[I] Bias Inputs       -> opens, Mag 7, VIX, sectors
[J] Output            -> lines, labels, table, alert JSON
```

Data flow: A -> B -> C; D reads A, C, H, I; E scores D; F gates E; G manages what passes; J shows everything.

### Rules that apply everywhere

1. **No repainting.** Levels come only from completed periods (`[1]` offset with lookahead on) or
   from opens that are known the moment a period starts. Signals evaluate on bar close only.
   A signal that was on the chart stays on the chart.
2. **Every distance is in volatility units with a tick floor.** Level geometry (cluster tolerance,
   touch tolerance, break confirmation, stop buffer, minimum target distance) uses a **daily ATR
   unit** so the level set is identical on the 1m and 5m chart. Candle-size and trailing distances
   use the execution-timeframe ATR. Section 6 has the numbers.
3. **Stops only tighten.** The trade manager never widens a stop.
4. **One position at a time.** The reversal feature (M7) is the only exception, and it closes first,
   then opens.
5. **Bar-close truth.** Backtest and live alerts both come from confirmed bars, so what the backtest
   shows is what the bridge receives.

---

## 4. Module specifications

### 4.1 [A] Level Engine

Level types. Each has a short code used on labels and in the stats table.

| Code | Level | Source | Refreshes |
|---|---|---|---|
| PDH / PDL / PDM | Previous day high / low / mid | `D` timeframe, previous bar | new exchange day |
| DO | Daily open | `D` open | new exchange day |
| MO | Midnight open (00:00 New York) | first chart bar at or after 00:00 NY | daily |
| PWH / PWL / PWM / WO | Previous week high / low / mid, weekly open | `W` | weekly |
| PMH / PML / PMM / MOO | Previous month high / low / mid, monthly open | `M` | monthly |
| QO | Quarterly open | `3M` open | quarterly |
| YO / YH / YL | Yearly open, current-year high / low (as of the prior daily close) | `12M` open; running max/min on the `D` series | daily |
| P4H / P4L / P4O | Previous 4-hour high / low / open | `240`, previous bar | every 4 hours |
| MNH / MNL / MNM | Monday range high / low / mid | chart bars inside Monday's session | weekly |
| AH / AL / AO | Asia session high / low / open (last completed session) | chart bars + session window | per session |
| LH / LL / LO | London session high / low / open | chart bars + session window | per session |
| NH / NL / NO | New York session high / low / open | chart bars + session window | per session |
| CUS | Custom levels typed in (options levels, POC, VAH, VAL, anything) | text input | manual |
| STR | Structure swing high / low, fallback targets when no key level is beyond | pivots on 15m | rolling |

**Request budget.** D 1, W 1, M 1, 3M 1, 12M 1, 240 1 = 6. MTF votes 5 / 15 / 60 = 3 (the 240
call is shared). Mag 7 = 7. VIX = 1. Sectors = 11 (off by default). Total 29 of 40 with everything
on, 18 with sectors off. Each HTF call returns a tuple such as `[high[1], low[1], open, atr[1]]` so
one call serves several levels.

**Level instance identity.** An instance is (type, price, born-at time). When its period rolls the
old instance retires and a new one is born. Statistics attach to instances, so "first interaction"
is unambiguous.

**Session windows** are inputs in New York time (defaults in D-06). Session levels always use the
most recently *completed* session, so they never move while being traded.

**Clustering.** Sort active levels by price and walk the list; any level within `clusterTol` of the
running zone joins it. A zone stores min price, max price, member codes, and member count. Zone
strength = member count. The zone is what gets touched, faded, broken, and targeted; the statistics
still credit every member type.

`clusterTol = max(clusterUnit * dailyATR, clusterTicks * mintick)`. Defaults 0.02 daily ATR, floor
4 ticks. On NQ with a 300-point daily ATR that is 6 points.

**Fresh state.** A zone is "fresh" until price trades within `touchTol` of it after the fresh-reset
time (D-11). Fresh zones score higher.

**Drawing.** Only zones within `drawRange` daily ATRs of the current price are drawn (default 1.0
above and below). Lines extend to the right with a small code label at the right edge. A zone with
two or more members draws as a thin box with the codes joined ("PDH+P4H"). Touched zones draw
dimmer. Everything else is off by default so the chart stays clean.

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
If we run the offline study (5.3) we seed them with measured values and the live counters refine them.

Ranking: sort types by `holdRate` descending. `rankPct` is the percentile position (top = 100).
Eligibility (D-24, default):

- Fade-eligible: type in the top half by rank, or fewer than `minSamples` interactions
  (unknown types are allowed but score lower).
- Break-eligible: type in the bottom half, or unknown.
- Strict mode (option): exact halves only, unknown types trade nothing.

Table (toggle): type, N, hold %, break %, rank, preferred (FADE / BREAK), trades, win %, net P&L.
Footer: FADE versus BREAK totals.

### 4.4 [D] Setup Detector

Evaluated on the execution-bar close. At most one new signal per bar; ties resolved by score.

**FADE (zone holds).** All of the following on the closing bar or the one before:

1. Price touched the zone and the approach side is known.
2. A rejection signal, any of (each can be toggled):
   - *Wick rejection*: the wick on the zone side is at least `wickRatio` (default 0.5) of the bar
     range, the close is back on the approach side, and the bar range is at least `minBarATR`
     (default 0.6 execution ATR) so dojis do not qualify.
   - *Poke and close back*: the bar traded through the zone's far side and closed back on the approach side.
   - *Engulfing*: this bar's body engulfs the prior bar's body in the rejection direction, and the pair touched the zone.
3. The zone is fade-eligible ([C]) and the filters pass ([F]).

Entry: market at the next bar open (default) or a limit at the zone edge (mode, D-18).
Stop: beyond the rejection candle's extreme plus `stopBuffer` (default), or beyond the zone plus
buffer (option, D-22). Ladder: the next zones in the bounce direction, skipping any closer than
`minTargetDist`.

**BREAK (zone fails).**

1. A bar closes beyond the zone's far side by at least `breakConfirm`. A wick through does not count.
2. Optional momentum filter: bar body at least `minBreakBodyATR` execution ATRs.
3. The zone is break-eligible and the filters pass.

Entry: market at the next bar open (default), or *retest* mode: rest a limit at the zone for up to
`retestBars` bars and cancel if unfilled. Stop: back inside the zone (zone edge plus buffer on the
wrong side). Option "failed-break exit": if a bar closes back through the zone before TP1, exit at
that close instead of waiting for the stop. Ladder: the next zones beyond the broken one.

Both setups require:

```
(TP1 - entry) / (entry - stop) >= minRR
stop distance <= maxRiskATR * dailyATR
TP1 distance  >= minTargetDist
```

### 4.5 [E] Score (0 to 100)

| Component | Points | Rule |
|---|---|---|
| Reliability | 0 to 40 | `rankPct * 0.4`, using hold-rank for fades and break-rank for breaks; unknown type = 20 |
| Stack | 0 to 20 | 1 member = 5, 2 = 12, 3 or more = 20 |
| First test | 0 to 15 | fresh = 15, touched once = 7, more = 0 |
| MTF alignment | 0 to 15 | aligned votes / total votes * 15 |
| Bias | 0 to 10 | with bias = 10, neutral = 5, against = 0 |

`minScore` default 60. Weights are inputs. The label shows the total and the MTF count,
for example `FADE PDL+AL  S 78  MTF 3/4`.

### 4.6 [F] Filters

- **Chop.** Band = `chopPct` of price (default 0.25 %) or `chopATR` daily ATRs (option, for symbols
  where a percentage is wrong). Window = `chopMinutes` (default 30), converted to bars from the chart
  timeframe so it means the same thing on 1m and 5m. If highest minus lowest over the window is
  within the band, chop is ON and the band is frozen. Chop turns OFF on the first close outside the
  frozen band. No entries while ON.
- **Time window.** Entries allowed between `entryStart` and `entryEnd` (NY time). Optional second
  window for London. For 24/7 symbols the window can be disabled.
- **Flatten.** At `flattenTime` (NY) close everything and cancel orders. Default 15:55.
- **Caps.** `maxSignalsPerDay` (default 4), `maxLossesPerDay` (default 2, 0 = off), one open position.
- **Re-entry.** After a stop-out the same zone is blocked for `cooldownBars` (default 12), and at
  most one re-entry per zone per day.
- **Geometry.** `minRR` (default 1.0), `minTargetDist` (default 0.15 daily ATR, floor 10 ticks),
  `maxRiskATR` (default 0.35 daily ATR).
- **Bias gate (option).** ON: only trade in the bias direction. OFF (default): bias only affects the score.

### 4.7 [G] Trade Manager

State per position: `entry, initStop, curStop, R (= |entry - initStop|), ladder[], tpIdx, stage, brokenLevels[]`.

Stages. Thresholds in R, measured on the bar extreme by default (D-32).

| Stage | Trigger | Stop moves to |
|---|---|---|
| 0 INITIAL | entry | `initStop` |
| 1 RISK-HALVED | +0.5R | halfway between `initStop` and entry |
| 2 BREAK-EVEN+ | +1.0R | entry plus cushion, cushion = max(`beTicks`, `beATR` execution ATRs) |
| 3 TRAILING | +1.5R, or any target promotion | max(`curStop`, structure stop, chase stop), re-checked every bar |

Structure stop = the most recent confirmed swing low (for a long) minus `structATR` execution ATRs.
Chase stop = close minus `chaseATR` execution ATRs. Swings come from `ta.pivotlow / ta.pivothigh`
with a right-side lookback, so they are confirmed and do not repaint.

Target ladder, evaluated on bar close when the bar's extreme reaches `ladder[tpIdx]`:

- Close beyond the target by at least `contConfirm` (default 0.03 daily ATR): **promote**.
  `tpIdx += 1`, `curStop = max(curStop, target - stopBuffer)` so the broken level becomes the floor,
  stage becomes 3.
- Otherwise: **soft-target exit** at this bar's close (target reached, not accepted).
- Ladder exhausted: stay in on trailing only.
- Option `hardTP1`: rest a limit at TP1 instead (the classic take-profit) for anyone who wants the simple version.

Reversal hook (built in M7, D-35): on a soft-target exit, if the target zone is fade-eligible in the
opposite direction and that fade scores at least `minScore`, open the opposite trade with
`reverseQtyMult` times the base size. A limit at the zone is the preferred entry for this case.

Flatten: `flattenTime` closes everything.

Order mapping in Pine: `strategy.entry` (market or limit), `strategy.exit(stop = curStop)`
re-issued every bar, `strategy.close` for soft-target and flatten exits, `strategy.cancel` for
stale limits. `process_orders_on_close = false`, so market fills happen at the next bar open, the
same as a bridge would fill them.

### 4.8 [H] MTF Confluence

For each confirmation timeframe (default 5, 15, 60, 240): vote = +1 if the confirmed close is above
the EMA(`mtfEmaLen`, default 50) on that timeframe, otherwise -1. Long setups need at least
`minVotesLong` bullish votes (default 2 of 4); shorts mirror. Uses `[1]` confirmed values so votes do
not flicker inside the higher-timeframe bar.

Optional second signal (D-27): **HTF rejection**. The last completed candle on a chosen confirmation
timeframe (default 15m) shows a rejection wick at the same zone. It adds to the score; it does not gate.

### 4.9 [I] Bias Inputs

All optional. Score-only unless the bias gate is on (D-29).

- **Opens**: price above or below the daily open, the midnight open, and the NY open, +1 / -1 each.
  Net +2 or more is bullish, -2 or less is bearish.
- **Mag 7 breadth**: AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA. Count the names above today's open.
  5 or more bullish, 2 or fewer bearish. Valid only while US stocks trade (default 09:30 to 16:00 NY,
  or 04:00 to 20:00 with extended-hours data). Neutral outside those hours.
- **VIX**: below its session open, or falling against its 20-bar EMA, is risk-on, which is bullish for NQ.
- **Sector breadth**: the 11 SPDR sector ETFs above their open. Off by default (11 request calls).
- **Heatmap**: not readable from Pine. Mag 7 breadth plus QQQ-versus-open is the stand-in.

Bias = majority of the enabled sources; a tie is neutral.

### 4.10 [J] Output

- Level lines and zone boxes (4.1). Current stop line and TP1 / TP2 lines while in a trade.
- Signal label on the entry bar: `LONG FADE PDL+AL  S 78  E 19876.0  SL 19851.0  T1 19920 (MO)  MTF 3/4`.
- Management markers: a small triangle when the stop moves stage, a diamond when a target is promoted.
- Stats table (4.3), position selectable, off switch.
- Alerts: one `alert()` per event with a JSON body:

```json
{"event":"ENTRY","side":"long","setup":"FADE","level":"PDL+AL","score":78,
 "symbol":"MNQ1!","qty":2,"entry":19876.0,"stop":19851.0,"tp1":19920.0,"tp2":19965.0,
 "time":"2026-09-19T14:35:00Z"}
```

Events: ENTRY, STOP_MOVE, TP_PROMOTE, EXIT, FLATTEN, REVERSE. The bridge-specific wrapper
(PickMyTrade or TradersPost) is added once D-03 is decided.

---

## 5. Cross-symbol behaviour

### 5.1 Units

- `dailyATR`: 14-period ATR on the daily series, taken from the same `D` request, as of the previous
  daily close. Used for all level geometry.
- `execATR`: 14-period ATR on the chart timeframe. Used for candle-size filters, the break-even
  cushion, and trailing.
- `syminfo.mintick` and `syminfo.pointvalue` for tick floors, P&L, and sizing.

### 5.2 Sessions per asset class

- CME futures: exchange day 18:00 to 17:00 NY; sessions as inputs.
- Stocks: the exchange day is the regular-hours day unless the chart shows extended hours. Overnight
  sessions produce no bars, so Asia and London levels are simply absent. The engine must tolerate a
  missing session.
- Crypto: 24/7, daily bar at 00:00 UTC on most exchanges, time window off by default.

### 5.3 Where the statistics come from

Inside the script, a 10k to 20k bar chart gives a few weeks of 1-minute data. Types like PMH or YO
will have single-digit samples. Three options (D-23):

1. **Live counters only.** Simplest. The ranking is noisy early and settles over weeks of running.
2. **Seeded priors.** An offline Python study over years of 1m or 5m data measures hold rates per
   type once. Those become the input defaults and the live counters refine them. Needs data
   (Databento pay-as-you-go, a broker export, or a public NQ minute dataset).
3. **Deep Backtesting** (Premium and up) runs the script over all history, so the counters cover
   years, but only during that backtest run, not on the live chart.

Recommendation: 1 now, 2 as soon as we can get data.

---

## 6. Proposed default parameter sheet

| Group | Parameter | Default | Unit |
|---|---|---|---|
| Levels | clusterUnit / clusterTicks | 0.02 / 4 | daily ATR / ticks |
| Levels | touchTol | 0.01 / 2 | daily ATR / ticks |
| Levels | drawRange | 1.0 | daily ATR |
| Interaction | breakConfirm | 0.03 / 4 | daily ATR / ticks |
| Interaction | holdConfirm | 0.10 | daily ATR |
| Interaction | verdictWindow | 30 | execution bars |
| Fade | wickRatio / minBarATR | 0.5 / 0.6 | ratio / exec ATR |
| Fade | stopBuffer | 0.02 / 2 | daily ATR / ticks |
| Break | minBreakBodyATR | 0.5 | exec ATR |
| Break | retestBars | 6 | execution bars |
| Filters | minScore | 60 | points |
| Filters | minRR | 1.0 | R |
| Filters | minTargetDist | 0.15 / 10 | daily ATR / ticks |
| Filters | maxRiskATR | 0.35 | daily ATR |
| Filters | chopPct / chopMinutes | 0.25 % / 30 | percent / minutes |
| Filters | entry window / flatten | 09:30 to 15:30 / 15:55 | NY time |
| Filters | maxSignalsPerDay / maxLossesPerDay | 4 / 2 | count |
| Manager | stage thresholds | 0.5 / 1.0 / 1.5 | R |
| Manager | beTicks / beATR | 2 / 0.02 | ticks / exec ATR |
| Manager | structLookback / structATR / chaseATR | 5 / 0.5 / 2.0 | bars / exec ATR |
| Manager | maxLadder / contConfirm | 4 / 0.03 | levels / daily ATR |
| MTF | timeframes / EMA length / min votes | 5, 15, 60, 240 / 50 / 2 | minutes / bars / votes |
| Costs | commission / slippage | per D-04 | per contract / ticks |

Every parameter becomes an input with a tooltip. No magic numbers in the code.

---

## 7. Milestones

Each milestone is a complete, runnable script that you paste into TradingView and check against
its acceptance list before we move on. Nothing from a later milestone leaks into an earlier one.

| # | Deliverable | You verify |
|---|---|---|
| M0 | This plan, decisions recorded | Answer `docs/DECISIONS.md` |
| M1 | Level engine as an **indicator**: all level types, clusters, labels, fresh / touched state | Levels match what you would draw by hand on NQ for 3 sessions. The same script on ES and BTC draws sensible levels. No level moves on bar replay. |
| M2 | Interaction classifier and stats table | Table counts change only on bar close. Spot-check 10 touches by eye. |
| M3 | Setup detector, score, labels, signal alerts (still an indicator) | Signals appear where you would expect fades and breaks. Scores read right. One alert per signal. |
| M4 | Strategy v1: entries, initial stop, hard TP1, filters, caps, flatten, costs | Backtest runs. Trade list matches the labels. Flat at 15:55 every day. |
| M5 | Trade manager: staged stops, ladder, soft targets, trailing | Replay 5 trades and confirm every stop move and promotion by hand. |
| M6 | MTF votes, bias inputs, score integration | Labels show MTF x/4. Bias toggles change scores as expected. |
| M7 | Reversal at target, custom levels input, VWAP / 200 EMA confluence | A reversal opens only when the target zone is fade-eligible. |
| M8 | Python study for priors (optional) | A priors table produced from real data. |

Repo layout once code starts: `pine/l2l.pine` (the script), `pine/CHANGELOG.md`, `docs/`
(plan, decisions, test checklist), `research/` (M8), `reference/` (your beta script and the
LuxAlgo output, for mining).

---

## 8. Working agreement

- I write Pine here; you compile in TradingView. When it fails, paste the first error line with its
  line number. When it runs, send a screenshot of one session.
- Each milestone ships with a checklist. We do not start the next until the checklist passes on NQ or MNQ.
- One file, module headers from section 3, every parameter an input.
- Defaults are frozen per instrument family (index futures, energy, metals, crypto), never per symbol,
  to limit overfitting.

---

## 9. Acceptance tests for "working"

1. Compiles in Pine v6 with no warnings.
2. No repainting: bar replay from a day earlier shows the same levels, signals, and exits as the live chart.
3. Levels are identical on the 1m and 5m chart of the same symbol at the same moment.
4. Alerts: exactly one ENTRY alert per signal and one EXIT per exit, none on historical bars.
5. The trade list matches the labels one for one.
6. Runs on NQ1!, MNQ1!, ES1!, and BTCUSD without errors and without NQ-specific numbers.
7. Stats table totals equal the number of classified interactions.
8. With costs set, the backtest still reports metrics per level type and per setup type.

---

## 10. Risks and honest caveats

- **Bar-close granularity.** A bar that hits TP1 and the stop in the same minute is resolved by the
  emulator's assumption unless Bar Magnifier is on. A 1-minute execution chart shrinks this.
- **Thin statistics.** Rankings on a few weeks of data are noise. Treat the ranking as a display
  until priors exist.
- **Overfitting.** With about 40 parameters it is easy to tune a backtest that will not repeat.
  Hence frozen defaults per instrument family.
- **Bridge latency and slippage.** Market entries fill at the next bar open in the backtest and a
  second or two later through a webhook live. The plan uses conservative slippage inputs.
- **Breadth data** depends on your data plan (real-time stocks, CBOE VIX).
- **Live stop modification** depends on the bridge supporting it. Verify before trusting the trailing
  logic with real money.

---

## 11. Parked ideas (not in v1)

- Stop-and-reverse with size multiplier (designed in 4.7, built in M7).
- Volume profile POC / VAH / VAL computed in-script (heavy; use the custom-levels input instead).
- CME options and gamma levels (paid feed; custom-levels input).
- Nasdaq heatmap (not accessible from Pine; Mag 7 breadth stands in).
- Partial exits at TP1 (easy once base size is 2 or more contracts; D-33).
- Lower-timeframe intrabar confirmation of target rejection via `request.security_lower_tf`.
