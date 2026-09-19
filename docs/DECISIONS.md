# Decision Log

Every open question for the Level-to-Level strategy, grouped by topic. Each has a **Default**
(what gets built if you say nothing), a **Status**, and an **Answer** line.

Status key: DECIDED = answered and recorded. OPEN = waiting on you. DEFAULT = not answered, the
default stands unless you say otherwise. CLARIFY = answered, but one detail needs a yes or no.

Round 1 answered 2026-09-19. Items still needing you: D-01, D-03, D-04, D-10, D-27, D-35, D-39, D-40, D-41.

---

## A. Platform and execution

### D-01  TradingView plan and data  (CLARIFY)
**Default:** Premium-tier features: 20k bars, Bar Magnifier, Deep Backtesting, webhooks.
**Answer:** Paid plan at about $100 per month. That matches Premium month to month ($69.95) plus
data add-ons. Two things to confirm: the plan page says "Premium", and "CME real-time" shows as
active under your market data. Without the add-on the chart is 10 minutes delayed.

### D-02  One script or two  (DEFAULT)
**Default:** one strategy script with display toggles. M1 to M3 ship as an indicator anyway.
**Answer:** not discussed.

### D-03  Bot, bridge, and broker  (CLARIFY)
**Default:** alert JSON in PickMyTrade's field names, verified on a Tradovate sim account in M4.
**Answer:** Tradovate cash account, sometimes prop firms, bridge undecided. Research
(`docs/RESEARCH.md` section 4): PickMyTrade covers Tradovate, Rithmic, ProjectX/TopstepX and the
Apex / Topstep / MyFundedFutures prop firms, and its alert format supports stop updates, break-even,
trailing, close, and close-then-reverse, which is everything the trade manager needs. Prop firms
allow supervised automation, not unattended bots. Confirm: build to PickMyTrade's format?

### D-04  Costs and contract  (CLARIFY)
**Default:** MNQ, commission $0.80 per side, slippage 2 ticks per side. Per-contract table in
`docs/RESEARCH.md` section 2.
**Answer:** Research done. Tradovate charges $1.29 per side standard and $0.39 per side micro on
the Free plan, $0.99 / $0.29 on the $99 Monthly plan, $0.59 / $0.09 on Lifetime, plus exchange,
clearing and NFA fees. Published tests put Tradovate market-order slippage at about 1.2 ticks
average, 1.2 to 3 ticks on NQ, 4 to 8 ticks on news days. Confirm: which Tradovate plan are you on,
and which contract do you trade most, MNQ or NQ?

### D-05  Position sizing  (DEFAULT)
**Default:** fixed, 2 contracts of MNQ; risk-based sizing available as an option.
**Answer:** not discussed.

---

## B. Instruments and time

### D-06  Session windows  (DECIDED)
**Default:** killzone style, entered in Central Time with a timezone input.
**Answer:** Killzone style is fine, in Central Time, with the option to switch. Recorded as:
Asia 19:00 to 23:00 CT, London 01:00 to 04:00 CT, New York 08:30 to 15:00 CT for index (other
profiles in D-41). Timezone input default America/Chicago. The midnight open stays anchored to
00:00 New York (23:00 CT) with an option for local midnight.

### D-07  What "daily open" means  (DECIDED)
**Answer:** exchange day open, 17:00 CT (18:00 NY) on CME futures.

### D-08  Monday range  (DECIDED)
**Answer:** full exchange session, Sunday 17:00 CT to Monday 16:00 CT.

### D-09  Previous 4-hour bar boundaries  (DEFAULT)
**Default:** the chart's own 4-hour bars.
**Answer:** not discussed.

### D-10  Entry window and flatten time  (CLARIFY)
**Default:** index profile entries 08:30 to 14:30 CT, flatten 14:55 CT.
**Answer:** "Right before the end of the day, 15:55 seems accurate." The number came from my
proposal, which was in New York time. In Central Time there are two candidates:
- **14:55 CT** = 15:55 NY, five minutes before the stock market closes. Recommended: the 14:00 to
  15:00 CT hour after the cash close is thin and choppy on NQ.
- **15:55 CT** = 16:55 NY, five minutes before the futures session ends.
Confirm which. Energy and metals profiles flatten before their own settlements (D-41).

### D-11  When a level becomes fresh again  (DECIDED)
**Answer:** at the end of each day, which is the daily rollover at 17:00 CT.

### D-12  Other symbols  (DECIDED)
**Answer:** NQ/MNQ, CL/MCL, SI/SIL. ES rarely. The strategy should work on any symbol. Recorded as
instrument profiles (plan section 5.2) plus a generic profile. Acceptance tests now include CL, MCL, SI, SIL.

### D-13  Continuous contract  (DEFAULT)
**Answer:** not discussed.

---

## C. Levels

### D-14  Cluster tolerance unit  (DEFAULT)
**Answer:** not discussed. Daily ATR based with a tick floor.

### D-15  Extra level types  (DECIDED)
**Answer:** Your reading is correct. Today's high and low and the 15-minute swing points are used
only as targets, and the swing points drive the trailing stop. They are not drawn unless one of them
is the active TP1 or TP2 of an open trade. They never trigger entries.

### D-16  Custom levels input  (DECIDED)
**Answer:** included, since options levels, POC, VAH and VAL are part of how you trade and none of
them can be computed cleanly in Pine.

### D-17  VWAP and 200 EMA  (DEFAULT)
**Default:** score bonus only, session VWAP and the 15-minute 200 EMA, built in M7.
**Answer:** not discussed.

---

## D. Entries

### D-18  Reversal entry mode  (DECIDED)
**Answer:** You enter when a wick forms off the level and price starts to turn, often before the
candle closes, sometimes past the level, and sometimes the wick is on a higher timeframe. You asked
for whatever is most reliable with the least drawdown. Recorded as **rejection bar plus
follow-through bar** on the execution timeframe (plan 4.4): the rejection may extend past the level,
entry happens when the next bar closes in the rejection direction. Two later options: higher
timeframe rejection with a 1-minute trigger (M6), and sweep-reclaim-retest (M7).

### D-19  Rejection candle thresholds  (DEFAULT)
**Answer:** not discussed.

### D-20  Break entry details  (DEFAULT)
**Answer:** not discussed. Immediate entry, failed-break exit ON, retest mode as an option.

### D-21  Execution timeframe  (DECIDED)
**Answer:** 5-minute. The 1-minute trigger mode comes later as an option.

### D-22  Stop placement for reversal trades  (DECIDED)
**Answer:** off the level. Stop = far edge of the zone plus a buffer (0.03 daily ATR, 4-tick
floor). Trade-off noted: when the rejection wick went well past the level, a retest of that wick
can stop the trade out even though the level holds. Options remain for "beyond the wick" and
"farther of the two".

---

## E. Score, ranking, and confluence

### D-23  Where the hold / break statistics come from  (DECIDED)
**Answer:** Explained in plan 4.3. Live counters on the chart, then one Deep Backtesting run to
read real hold rates off the table and type them into the prior inputs. Offline study optional later.

### D-24  REV versus BRK eligibility rule  (DEFAULT)
**Answer:** not discussed.

### D-25  Score weights and minimum  (DEFAULT)
**Answer:** not discussed. Reliability 40, stack 20, first test 15, HTF rejection 15, bias 10, minimum 60.

### D-26  What counts as a hold and a break  (DEFAULT)
**Answer:** not discussed.

### D-27  Higher-timeframe confluence  (CLARIFY)
**Default:** HTF rejection at the same zone on 5m / 15m / 1h / 4h as the primary check; EMA trend votes optional and OFF.
**Answer:** Reworked from EMA votes to rejection checks after you said the higher-timeframe wick is
what you look for. Confirm that this matches how you use 5m, 15m, 1h and 4h.

---

## F. Filters and bias

### D-28  Chop filter  (DECIDED)
**Answer:** try it as designed, tune after the first backtests.

### D-29  Bias sources  (DECIDED)
**Answer:** Opens, Mag 7 and VIX on for NQ/MNQ, sector breadth off, score-only. On any symbol other
than NQ/MNQ the VIX and Mag 7 are ignored; detected from the symbol root, overridable.

### D-30  Daily caps and re-entry  (DEFAULT)
**Answer:** not discussed.

### D-31  Trade geometry minimums  (DEFAULT)
**Answer:** not discussed.

---

## G. Trade management

### D-32  Staged stops  (DECIDED)
**Answer:** as proposed. +0.5R halves the risk, +1R break-even plus cushion, +1.5R structure trail, measured on the bar's high or low.

### D-33  Partial exits  (DECIDED)
**Answer:** OFF by default, available. When ON and the partial is taken at TP1, the stop on the
remainder moves to break-even plus cushion on that same bar, so no risk remains.

### D-34  Target ladder  (DECIDED)
**Answer:** Explained with a worked example in plan 4.7. Four levels, promote on a close 0.03 daily
ATR beyond the target, trail only once the ladder runs out, hard-TP1 option for the simple version.

### D-35  Flip at target  (CLARIFY)
**Default:** OFF until M7 passes its tests; multiplier 1.5x; a flip requires a normal qualifying reversal setup at the target zone on the exit bar.
**Answer:** Explained in plan 4.7. Confirm: multiplier 1.5x or 2x, and require the same rejection
confirmation as a normal reversal trade (recommended) or fill a limit at the level with no confirmation?

---

## H. Output and workflow

### D-36  Chart cleanliness  (DEFAULT)
**Answer:** not discussed.

### D-37  Alert content  (DEFAULT)
**Answer:** not discussed. Now shaped to PickMyTrade field names (plan 4.10).

### D-38  Working loop  (DEFAULT)
**Answer:** implied yes.

### D-39  Reference material  (CLARIFY)
**Answer:** Socrates Investments (YouTube and Facebook), the SpacemanBTC key-levels indicator,
LuxAlgo's help, ICT fair value gaps and consequent encroachment. Findings in `docs/RESEARCH.md`
section 5. Still wanted: the specific video or post links you learned from, and your beta script.

---

## I. New this round

### D-40  News blackout filter  (OPEN)
No entries from 2 minutes before to 5 minutes after scheduled releases, times in a text input,
default 07:30 and 09:00 CT, energy profile adds Wednesday 09:30 CT. Added because Tradovate
slippage runs 4 to 8 ticks on news days and it aggregates data during bursts.
**Default:** ON.
**Answer:**

### D-41  How you trade CL/MCL and SI/SIL  (OPEN)
Proposed profiles: energy main session 08:00 to 13:30 CT, entries to 13:00, flatten 13:25 CT
before the 13:30 settlement; metals main session 07:20 to 12:30 CT, entries to 12:00, flatten
12:20 CT before the 12:25 silver settlement. Do you trade CL and SI only in those pit hours, or
through the day? Flatten before settlement, or hold into the afternoon?
**Default:** as proposed.
**Answer:**

### D-42  1-minute trigger mode  (DEFAULT)
Chart on 1m with the rejection detected on 5m or 15m and the entry on the first 1m close in the
rejection direction. Built as an option in M6 after the 5-minute version is proven.
**Default:** later, optional.
**Answer:**
