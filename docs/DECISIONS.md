# Decision Log

Every open question for the Level-to-Level strategy, grouped by topic. Each has a **Default**
(what gets built if you say nothing), a **Status**, and an **Answer** line.

Status key: DECIDED = answered and recorded. OPEN = waiting on you. DEFAULT = not answered, the
default stands unless you say otherwise. CLARIFY = answered, but one detail needs a yes or no.

Round 1 and round 2 answered 2026-09-19. Waiting on you: D-19, D-20, D-24, D-30, D-31, D-36,
D-43, D-45, D-46, D-47, plus the CL / SI data check in D-01.

---

## A. Platform and execution

### D-01  TradingView plan and data  (DECIDED, one check left)
**Answer:** Premium, with the US stocks bundle and CME Group real-time data. That gives 20k bars,
Bar Magnifier, Deep Backtesting and webhooks. The $9.95 CME Group bundle covers CME, CBOT, COMEX
and NYMEX. One check: NQ trades on CME but CL is NYMEX and SI is COMEX, so open a CL chart and an
SI chart once and confirm neither shows a delayed-data badge. If either does, the bot cannot trade it live.

### D-02  One script or two  (DEFAULT)
**Default:** one strategy script with display toggles. M1 to M3 ship as an indicator anyway.

### D-03  Bot, bridge, and broker  (DECIDED)
**Answer:** Tradovate cash account, sometimes prop firms. The "bridge" question, in plain words:
TradingView cannot send an order to Tradovate. A strategy can only fire an alert, which is a text
message. A bridge is a small paid service that receives that message and places the order in your
Tradovate account, moves the stop when told to, and closes the position when told to. PickMyTrade
is the one that fits: it supports Tradovate, Rithmic and TopstepX accounts and the Apex, Topstep and
MyFundedFutures prop firms, costs $50 per month or $500 per year, has a 7-day free trial, and works
with Tradovate demo accounts, so nothing is paid until you go live. Recorded: alerts are written
in PickMyTrade's format. You do not need to sign up until M4.

### D-04  Costs and contract  (DECIDED)
**Answer:** MNQ is the main contract, Tradovate Free plan. Backtest defaults: commission $0.80 per
side (the $0.39 commission plus exchange, clearing and NFA fees), slippage 2 ticks per side.
Confirm the fee against one of your own fills when convenient.

### D-05  Position sizing  (DEFAULT, option added)
**Default:** fixed 2 contracts of MNQ, which matches the "low risk" tier in your May rules.
Option `sizeByScore`: 2 contracts at score 60 to 69, 3 at 70 to 84, 5 at 85 and up, mirroring
your 2 / 3 / 5 tiers. OFF by default. See D-46.

---

## B. Instruments and time

### D-06  Session windows  (DECIDED)
**Answer:** Killzone style in Central Time with a timezone input. Asia 19:00 to 23:00 CT, London
01:00 to 04:00 CT, New York 08:30 to 15:00 CT for index (other profiles in plan 5.2). Midnight
open anchored to 00:00 New York (23:00 CT) with an option for local midnight.

### D-07  What "daily open" means  (DECIDED)
**Answer:** exchange day open, 17:00 CT.

### D-08  Monday range  (DECIDED)
**Answer:** full exchange session, Sunday 17:00 CT to Monday 16:00 CT.

### D-09  Previous 4-hour bar boundaries  (DEFAULT)
**Default:** the chart's own 4-hour bars.

### D-10  Entry window and flatten time  (DECIDED)
**Answer:** Flatten at **15:55 CT** for every futures profile. Entries stop at 15:00 CT by default
so a trade has time to work. Entry windows are now "allowed sessions" per profile (D-41).

### D-11  When a level becomes fresh again  (DECIDED)
**Answer:** at the daily rollover, 17:00 CT.

### D-12  Other symbols  (DECIDED)
**Answer:** NQ/MNQ, CL/MCL, SI/SIL. ES rarely. Should work on anything. Instrument profiles in plan 5.2.

### D-13  Continuous contract  (DEFAULT)
**Default:** NQ1! as you have it, no special roll handling.

---

## C. Levels

### D-14  Cluster tolerance unit  (DEFAULT)
**Default:** daily ATR based with a tick floor.

### D-15  Extra level types  (DECIDED)
**Answer:** Today's high and low and the 15-minute swing points are targets only and drive the
trailing stop. Never entries, not drawn unless active as TP1 or TP2.

### D-16  Custom levels input  (DECIDED)
**Answer:** included.

### D-17  VWAP and 200 EMA  (DEFAULT)
**Default:** score bonus only, session VWAP and the 15-minute 200 EMA, built in M7.

---

## D. Entries

### D-18  Reversal entry mode  (DECIDED)
**Answer:** rejection bar plus follow-through bar on the execution timeframe, rejection may extend
past the level. Later options: higher-timeframe rejection with a 1-minute trigger (M6), sweep-reclaim-retest (M7).

### D-19  Rejection candle thresholds  (DEFAULT, open for the next round)
Wick at least 50 % of the bar range, bar range at least 0.6 execution ATRs, engulfing = body
engulfs the prior body.
**Default:** as stated.
**Answer:**

### D-20  Break entry details  (DEFAULT, open for the next round)
Enter on the bar after the closing break, or wait for a retest? If a bar closes back inside the
level before TP1, exit at once (default) or wait for the stop?
**Default:** immediate entry, failed-break exit ON, retest mode as an option.
**Answer:**

### D-21  Execution timeframe  (DECIDED)
**Answer:** 5-minute. 1-minute trigger mode later (D-42).

### D-22  Stop placement for reversal trades  (DECIDED)
**Answer:** off the level: far edge of the zone plus a buffer. Wick-based stop kept as an option. Tick cap in D-45.

---

## E. Score, ranking, and confluence

### D-23  Where the hold / break statistics come from  (DECIDED)
**Answer:** live counters, then one Deep Backtesting run to seed the priors. Offline study optional.

### D-24  REV versus BRK eligibility rule  (DEFAULT, open for the next round)
Rank types by hold rate; top half may be traded as reversals, bottom half as breaks, unknown types
(fewer than 10 samples) either at a lower score. Or strict halves only.
**Default:** halves with unknowns allowed.
**Answer:**

### D-25  Score weights and minimum  (DECIDED, revised)
**Answer:** Reliability 40, stack 20, level history 15, HTF rejection 10, bias 15, minimum 60.
Revised after you said the higher-timeframe rejection helps a little but is not required, and that
a level which already rejected today is a plus. A fresh top-ranked level with no other help scores
64, so first tests trade on their own.

### D-26  What counts as a hold and a break  (DEFAULT)
**Default:** break = close beyond the zone by 0.03 daily ATR; hold = close 0.10 daily ATR away on
the approach side or reaching the next zone first; neither within 30 bars = not counted.

### D-27  Higher-timeframe confluence  (DECIDED)
**Answer:** A bonus, never a gate. The last completed 5m / 15m / 1h / 4h candle rejecting the same
zone adds up to 10 points. First tests are still taken. EMA trend votes exist as an option, OFF.

---

## F. Filters and bias

### D-28  Chop filter  (DECIDED)
**Answer:** as designed, tune after the first backtests.

### D-29  Bias sources  (DECIDED)
**Answer:** opens, Mag 7 and VIX on for NQ/MNQ, off automatically on other symbols, sector breadth off, score only.

### D-30  Daily caps and re-entry  (DEFAULT, open for the next round)
Max 4 signals per day, max 2 losses per day, daily loss limit $800 (D-44), one position at a time,
12-bar cooldown on a zone after a stop-out, one re-entry per zone per day.
**Default:** as stated.
**Answer:**

### D-31  Trade geometry minimums  (DEFAULT, open for the next round)
Min reward-to-risk 1.0, min distance to TP1 0.15 daily ATR (about 45 NQ points on a 300-point ATR
day), max stop 0.35 daily ATR plus the optional tick cap in D-45.
**Default:** as stated.
**Answer:**

---

## G. Trade management

### D-32  Staged stops  (DECIDED)
**Answer:** +0.5R halves the risk, +1R break-even plus cushion, +1.5R structure trail, measured on the bar's high or low.

### D-33  Partial exits  (DECIDED)
**Answer:** OFF by default. When ON, the partial at TP1 moves the stop on the remainder to break-even plus cushion on the same bar.

### D-34  Target ladder  (DECIDED)
**Answer:** four levels, promote on a close 0.03 daily ATR beyond the target, trail only once exhausted, hard-TP1 option.

### D-35  Flip at target  (DECIDED)
**Answer:** Your version. Long 2 MNQ, a limit for 4 MNQ rests at the target; the fill closes the
long and leaves a 2 MNQ short from the level. Inputs `flipEnabled` (OFF by default) and `flipQty`
(default = base size). Armed only at targets that are reversal-eligible the other way. Option
`flipConfirmed` waits for a rejection like a normal entry instead of resting a limit. Details in plan 4.7.

---

## H. Output and workflow

### D-36  Chart cleanliness  (DEFAULT, open for the next round)
Draw only zones within 1 daily ATR of price, short right-edge codes, touched zones dimmed, stats
table top-right with an off switch, small management markers.
**Default:** as stated.
**Answer:**

### D-37  Alert content  (DEFAULT)
**Default:** PickMyTrade field names plus our own logging fields (plan 4.10).

### D-38  Working loop  (DEFAULT)
**Answer:** implied yes.

### D-39  Reference material  (DECIDED, partly)
**Answer:** Six Socrates YouTube links received and saved in `reference/links.md`. Transcripts
cannot be pulled from this environment, so the plan relies on the titles, the site, and a
third-party write-up of the method. If a video states a rule that differs from the plan, tell me
or paste the transcript (YouTube's "Show transcript" button, copy all) into `reference/`.
Facebook posts: paste text or screenshots into `reference/` too. Still wanted: the beta script.

---

## I. New in round 1

### D-40  News blackout filter  (DECIDED)
**Answer:** ON. No entries 2 minutes before to 5 minutes after 07:30 and 09:00 CT; energy adds Wednesday 09:30 CT.

### D-41  How you trade CL/MCL and SI/SIL  (DECIDED)
**Answer:** any time of day. Energy and metals profiles allow Asia, London and New York sessions,
entry cutoff 15:00 CT, flatten 15:55 CT. Best-hours claim in D-47.

### D-42  1-minute trigger mode  (DEFAULT)
**Default:** later, optional, M6.

---

## J. New in round 2, from your May rules document

### D-43  Opening blackout  (OPEN)
Your rules restrict 08:30 to 09:00 CT to one small trade with a wide stop because TradeZella showed
under a 20 % win rate there with most stops hit within 2 minutes. The simplest bot version is no
entries for the first 30 minutes after the cash open. A later option can allow one reduced-size
trade instead.
**Default:** ON, 30 minutes, index profile only.
**Answer:**

### D-44  Daily loss limit in dollars  (DEFAULT)
From your rules: $800 per day. Once hit, no entries until the next rollover.
**Default:** 800, adjustable, 0 = off.

### D-45  Stop cap in ticks  (OPEN)
Your manual stop is 50 ticks on MNQ. The bot's stop sits off the level, and its entry comes one
bar later than yours, so 50 will reject most setups. Proposal: no cap until the first backtest, then
set the cap where the backtest shows stops stop paying for themselves. Or name a number now.
**Default:** off, then tuned.
**Answer:**

### D-46  Size by score  (OPEN)
Your 2 / 3 / 5 contract tiers mapped to score bands 60 to 69, 70 to 84, 85 and up. Fits "more size
on more conviction". Max 5 contracts as in your rules.
**Default:** OFF, fixed 2.
**Answer:**

### D-47  TradeZella export  (OPEN)
No TradeZella data exists in your Drive, Dropbox, Gmail or Wispr notes, and I cannot see your other
Claude chats. Export your trades from TradeZella as a CSV and drop it into `reference/` and I will
compute win rate and P&L by symbol, session and hour, which settles the CL / SIL Asia-open question
and tunes the allowed-sessions defaults.
**Default:** none; profiles stay as proposed.
**Answer:**
