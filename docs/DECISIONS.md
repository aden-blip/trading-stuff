# Decision Log

Every open question for the Level-to-Level strategy, grouped by topic. Each one has a
**Default** (what gets built if you say nothing) and an **Answer** line to fill in.
Reply in chat with the numbers you want changed; "defaults are fine except D-06 and D-10" is enough.

Status key: OPEN = not answered yet. DECIDED = answered and recorded.

---

## A. Platform and execution

### D-01  TradingView plan and data  (OPEN)
Which TradingView plan are you on, and do you have real-time CME futures data?
Why it matters: bars of history (5k / 10k / 20k), Bar Magnifier and Deep Backtesting (Premium and up),
webhooks (paid only). On the Free tier a 1-minute chart holds under 4 sessions, so Monday's range
would be missing by Thursday.
**Default:** assume a paid plan with 10k bars, no Bar Magnifier, futures data available.
**Answer:**

### D-02  One script or two  (OPEN)
One strategy script that draws everything (default), or a separate lightweight "levels only"
indicator for a clean chart plus the strategy for signals and trades?
**Default:** one strategy script with display toggles. Milestones M1 to M3 are shipped as an
indicator anyway, so you get a levels-only indicator for free along the way.
**Answer:**

### D-03  Bot, bridge, and broker  (OPEN)
Where will orders actually go? Tradovate, NinjaTrader, a prop-firm platform (TopstepX, Apex, etc.),
Rithmic, Interactive Brokers? Which bridge: PickMyTrade (Tradovate / Rithmic / IBKR / TradeStation),
TradersPost, something else, or alerts only for now while you place orders by hand?
The trailing logic needs the bridge to accept "modify stop" messages; not every bridge does.
**Default:** alerts with a generic JSON body for now; bridge-specific wrapper added when you pick one.
**Answer:**

### D-04  Costs and contract  (OPEN)
Which contract do you chart and trade (NQ1!, MNQ1!, a specific month)? Your commission per contract
per side and a realistic slippage in ticks. Typical retail: MNQ about 0.60 to 0.75 per side,
NQ about 2.25 per side, 1 tick slippage per side.
**Default:** MNQ, commission 0.75 per side, slippage 1 tick per side.
**Answer:**

### D-05  Position sizing  (OPEN)
Fixed contracts, or risk-based (a dollar risk per trade divided by the stop distance)?
Partial exits and the reversal multiplier both need at least 2 contracts.
**Default:** fixed, 2 contracts of MNQ; risk-based sizing available as an option.
**Answer:**

---

## B. Instruments and time

### D-06  Session windows (New York time)  (OPEN)
Two common conventions:
- Killzone style: Asia 20:00 to 00:00, London 02:00 to 05:00, New York 09:30 to 16:00.
- Contiguous: Asia 18:00 to 03:00, London 03:00 to 09:30, New York 09:30 to 16:00.
Session opens (AO, LO, NO) are the first bar of each window.
**Default:** killzone style. All six times are inputs.
**Answer:**

### D-07  What "daily open" means  (OPEN)
For CME futures the exchange day opens at 18:00 NY the evening before. You also listed the midnight
open and the NY open separately, so I read "daily open" as the 18:00 exchange open.
**Default:** daily open = exchange day open (18:00 NY on futures, 09:30 on stocks).
**Answer:**

### D-08  Monday range  (OPEN)
Monday's full exchange session (Sunday 18:00 to Monday 17:00) or Monday's regular hours (09:30 to 16:00)?
**Default:** full exchange session.
**Answer:**

### D-09  Previous 4-hour bar boundaries  (OPEN)
TradingView's 4-hour bars on CME futures start from the 18:00 session open (18:00, 22:00, 02:00,
06:00, 10:00, 14:00 NY). Use those, or align to midnight?
**Default:** the chart's own 4-hour bars.
**Answer:**

### D-10  Entry window and flatten time  (OPEN)
When may the strategy enter, and when must it be flat? Do you also want a London window?
For 24/7 symbols (BTC) should the window be off?
**Default:** entries 09:30 to 15:30 NY, flatten 15:55 NY, no London window, window off for crypto.
**Answer:**

### D-11  When a level becomes "fresh" again  (OPEN)
"Untouched so far today" needs a reset time. Exchange day open (18:00), midnight (00:00), or NY open (09:30)?
Note that with 18:00 a level tested in Asia is no longer fresh for New York.
**Default:** exchange day open (18:00).
**Answer:**

### D-12  Other symbols you actually want  (OPEN)
Which symbols beyond NQ/MNQ should this be tested on? ES, CL, GC, BTC, individual stocks?
I will only test and tune defaults for what you name.
**Default:** NQ/MNQ first, then ES and BTC as the cross-symbol checks.
**Answer:**

### D-13  Continuous contract  (OPEN)
Do you chart NQ1! (continuous) with back-adjustment on or off? Levels from before a roll date are
distorted when the roll gap is not adjusted. Most people leave it as is and accept one odd day per quarter.
**Default:** NQ1! as you have it, no special roll handling.
**Answer:**

---

## C. Levels

### D-14  Cluster tolerance unit  (OPEN)
Daily-ATR based (0.02 daily ATR, floor 4 ticks), fixed ticks, or a percent of price?
Daily ATR keeps the same level set on every chart timeframe and adapts across symbols.
**Default:** daily ATR based with a tick floor.
**Answer:**

### D-15  Extra level types  (OPEN)
Two more that fit the engine:
- Today's developing high and low (HOD / LOD). Natural targets, but they move, so entries off them are riskier.
- Structure swings (STR) from 15-minute pivots, as fallback targets when no key level lies beyond.
**Default:** both included as **targets only**, not as entry levels; toggles for each.
**Answer:**

### D-16  Custom levels input  (OPEN)
A text box where you type levels each morning (options levels, POC, VAH, VAL, anything), for
example `R: 20150, 20210 | S: 19980`. They get the code CUS and take part in clustering, stats, and scoring.
**Default:** included.
**Answer:**

### D-17  VWAP and 200 EMA  (OPEN)
These are moving levels, so they do not fit the horizontal-level engine cleanly. Options:
score bonus when a fade agrees with the side of VWAP / 200 EMA (simple), or treat them as
tradeable dynamic levels (more code, more edge cases). Which 200 EMA timeframe do you use?
**Default:** score bonus only, session VWAP and the 15-minute 200 EMA. Built in M7.
**Answer:**

---

## D. Entries

### D-18  Fade entry mode  (OPEN)
Wait for the rejection candle to close (safer, later entry) or rest a limit order at the zone
(earlier, no confirmation)?
**Default:** close-confirmed rejection. Limit mode as an option.
**Answer:**

### D-19  Rejection candle thresholds  (OPEN)
Wick at least 50 % of the bar range, bar range at least 0.6 execution ATRs, engulfing = body engulfs
the prior body. Change anything?
**Default:** as stated.
**Answer:**

### D-20  Break entry details  (OPEN)
Enter at the next bar after the closing break (default), or wait for a retest of the level
(limit at the zone, cancelled after 6 bars)? If a bar closes back inside the level before TP1,
exit immediately (default) or wait for the stop?
**Default:** immediate entry, failed-break exit ON, retest mode as an option.
**Answer:**

### D-21  Execution timeframe  (OPEN)
5-minute (cleaner, fewer whipsaws, later stops) or 1-minute (tighter stops, more noise, needs more history)?
**Default:** 5-minute for development and backtests; 1-minute supported.
**Answer:**

### D-22  Stop placement for fades  (OPEN)
Beyond the rejection candle's extreme plus buffer (structural, usually wider), or beyond the zone
plus buffer (tighter, more stop-outs on wicks)?
**Default:** beyond the rejection candle.
**Answer:**

---

## E. Score, ranking, and confluence

### D-23  Where the hold / break statistics come from  (OPEN)
Live counters inside the script (thin on low timeframes), seeded priors from an offline Python study
(needs years of minute data), or Deep Backtesting counts (Premium only, backtest-time only)?
Can you get NQ minute data (Databento, broker export, a public dataset)?
**Default:** live counters now, priors when data is available.
**Answer:**

### D-24  Fade versus break eligibility rule  (OPEN)
Rank types by hold rate. Top half may be faded, bottom half may be traded as breaks, unknown types
(fewer than 10 samples) may do either at a lower score. Or strict: only the exact half, unknowns trade nothing.
**Default:** halves with unknowns allowed.
**Answer:**

### D-25  Score weights and minimum  (OPEN)
Reliability 40, stack 20, first test 15, MTF 15, bias 10. Minimum 60 to trade.
**Default:** as stated.
**Answer:**

### D-26  What counts as a hold and a break  (OPEN)
Break: a close beyond the zone by 0.03 daily ATR. Hold: a close 0.10 daily ATR away on the
approach side, or reaching the next zone, before any break. Neither within 30 bars: not counted.
**Default:** as stated.
**Answer:**

### D-27  Multi-timeframe confluence  (OPEN)
Votes from 5m / 15m / 1h / 4h using close versus a 50 EMA, need 2 of 4 aligned.
Do you also want "HTF rejection" (last completed 15-minute candle rejected the same zone) as a score bonus?
And is EMA-versus-price really how you judge the higher timeframes, or is it structure (higher highs and lows)?
**Default:** EMA votes, 2 of 4, HTF rejection bonus ON.
**Answer:**

---

## F. Filters and bias

### D-28  Chop filter  (OPEN)
Band 0.25 % of price, window 30 minutes, released on the first close outside the frozen band.
Keep the percent, or use a daily-ATR band so it transfers to other symbols?
**Default:** percent for NQ, ATR option available.
**Answer:**

### D-29  Bias sources and how they act  (OPEN)
For NQ: opens bias, Mag 7 breadth, VIX direction ON; sector breadth OFF (costs 11 data requests).
Bias adjusts the score only (default) or blocks counter-bias trades (gate)?
Mag 7 and VIX are only valid while stocks trade; outside those hours bias is neutral.
**Default:** as stated, score only.
**Answer:**

### D-30  Daily caps and re-entry  (OPEN)
Max 4 signals per day, max 2 losses per day, one position at a time, 12-bar cooldown on a zone
after a stop-out, one re-entry per zone per day.
**Default:** as stated.
**Answer:**

### D-31  Trade geometry minimums  (OPEN)
Min reward-to-risk 1.0, min distance to TP1 0.15 daily ATR (about 45 NQ points on a 300-point ATR day),
max stop distance 0.35 daily ATR.
**Default:** as stated.
**Answer:**

---

## G. Trade management

### D-32  Staged stops  (OPEN)
+0.5R: stop to halfway. +1.0R: break-even plus cushion (2 ticks or 0.02 exec ATR, whichever is larger).
+1.5R: structure trail. Measure progress on the bar's high / low (default) or on closes only?
**Default:** as stated, measured on the bar extreme.
**Answer:**

### D-33  Partial exits  (OPEN)
Option to close half at TP1 and run the rest on the ladder. Needs 2 or more contracts.
**Default:** available, OFF.
**Answer:**

### D-34  Target ladder  (OPEN)
Up to 4 levels. Promotion needs a close beyond the target by 0.03 daily ATR. After the ladder is
exhausted: trail only (default) or exit at the last level? Also a "hard TP1" option for the simple version.
**Default:** as stated.
**Answer:**

### D-35  Reversal at target (built last)  (OPEN)
When price rejects the target zone and that zone is fade-eligible the other way with a score above
the minimum: close, then enter the opposite way with a size multiplier. Multiplier 1.5x or 2x?
Limit at the zone or close-confirmed?
**Default:** 1.5x, limit at the zone, OFF until M7 passes its tests.
**Answer:**

---

## H. Output and workflow

### D-36  Chart cleanliness  (OPEN)
Draw only zones within 1 daily ATR of price, short right-edge codes, touched zones dimmed,
stats table top-right with an off switch, management markers small.
**Default:** as stated.
**Answer:**

### D-37  Alert content  (OPEN)
One JSON alert per event (ENTRY, STOP_MOVE, TP_PROMOTE, EXIT, FLATTEN, REVERSE) with side, setup,
level code, score, qty, entry, stop, tp1, tp2. Anything else you want in it?
**Default:** as stated.
**Answer:**

### D-38  Working loop  (OPEN)
I write Pine here and cannot compile it. You paste it into TradingView, report the first error line
or send a screenshot, and we iterate one milestone at a time. OK?
**Default:** yes.
**Answer:**

### D-39  Reference material  (OPEN)
Please add your beta script and the LuxAlgo output to `reference/` in this repo (or paste them in chat),
and share the social media links that describe the strategy. I will mine them for rules and for the
pieces that already worked.
**Default:** none available; build from this plan alone.
**Answer:**
