# Decision Log

Every open question for the Level-to-Level strategy, grouped by topic. Each has a **Default**
(what gets built if you say nothing), a **Status**, and an **Answer** line.

Status key: DECIDED = answered and recorded. OPEN = waiting on you. DEFAULT = not answered, the
default stands unless you say otherwise. CLARIFY = answered, but one detail needs a yes or no.

Rounds 1 to 6 answered 2026-09-19. M1 chart reviews recorded 2026-09-20 (D-56 to D-60). Nothing is
waiting on you; the beta script stays optional.

---

## A. Platform and execution

### D-01  TradingView plan and data  (DECIDED)
**Answer:** Premium, with the US stocks bundle and CME Group real-time data. That gives 20k bars,
Bar Magnifier, Deep Backtesting and webhooks. CL and SI confirmed real-time. You noted the 1-minute
chart on CL and SI gets hard to read in low volume; the bot runs on 5-minute candles, and an
optional thin-market filter exists for those symbols (D-49).

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

### D-17  VWAP and 200 EMA  (DECIDED, revised by D-64)
**Answer:** score bonus only, session VWAP and the 15-minute 200 EMA. The hooks are built hidden in
M3 at zero weight; the weights come from the M4 backtest split (D-64).

---

## D. Entries

### D-18  Reversal entry mode  (DECIDED)
**Answer:** rejection bar plus follow-through bar on the execution timeframe, rejection may extend
past the level. Later options: higher-timeframe rejection with a 1-minute trigger (M6), sweep-reclaim-retest (M7).

### D-19  Rejection candle thresholds  (DECIDED)
**Answer:** as proposed. Wick at least 50 % of the candle, candle range at least 0.6 of the
5-minute ATR, engulfing means the body covers the prior body.

### D-20  Break entry details  (DECIDED at default, explained in chat)
**Answer:** A break trade starts when a 5-minute candle closes through a level by more than the
confirmation distance, not when it merely wicks through. Entry happens at the open of the next
candle. If a later candle closes back on the wrong side of the level before the first target, the
trade exits right there instead of waiting for the stop, since the break has failed. The retest
option waits for price to come back to the level after the break and buys or sells there with a
limit order; later entry, fewer fake-outs, sometimes no fill. Default stays immediate entry with
the failed-break exit on; retest is a switch.

### D-21  Execution timeframe  (DECIDED)
**Answer:** 5-minute. 1-minute trigger mode later (D-42).

### D-22  Stop placement for reversal trades  (DECIDED)
**Answer:** off the level: far edge of the zone plus a buffer. Wick-based stop kept as an option. Tick cap in D-45.

---

## E. Score, ranking, and confluence

### D-23  Where the hold / break statistics come from  (DECIDED)
**Answer:** live counters, then one Deep Backtesting run to seed the priors. Offline study optional.

### D-24  REV versus BRK eligibility rule  (DECIDED)
**Answer:** You read it right: this is about measuring which level types hold most often so the
bot leans on those for reversals and trades the weaker ones as breaks. You believe 4-hour highs and
lows are the strongest and want research before anything is locked. Recorded as `rankGate = OFF`
by default: every level type may be traded both ways and the measured ranking only moves the score.
The hard split becomes a switch to turn on after the Deep Backtesting run. Your 4-hour belief seeds
the priors once measured. With break trades off (D-50), the ranking simply favors the strongest types for reversals.

### D-25  Score weights and minimum  (DECIDED, revised)
**Answer:** Reliability 40, stack 20, level history 15, HTF rejection 10, bias 15, minimum 60.
Revised after you said the higher-timeframe rejection helps a little but is not required, and that
a level which already rejected today is a plus. A fresh top-ranked level with no other help scores
64, so first tests trade on their own.

### D-26  What counts as a hold and a break  (DEFAULT, distances revised by D-67)
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

### D-30  Daily caps and re-entry  (DECIDED)
**Answer:** For backtesting, all caps off: no signal count, no loss count, no dollar limit. Each
stays in the settings for later. Loss and profit limits are a percent of the account (D-44). The
cooldown after a stop-out is now measured in minutes, default 12, since 12 candles on a 15-minute
chart would skip good entries; you had the 1-minute chart in mind. One re-entry per zone per day
stays. One open position at a time stays.

### D-31  Trade geometry minimums  (DECIDED at default)
**Answer:** not objected to. Min reward-to-risk 1.0, target at least 0.15 daily ATR away, max stop
0.35 daily ATR, tick cap off (D-45).

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

### D-36  Chart cleanliness  (DECIDED at default, explained in chat)
**Answer:** In plain words: the script only draws levels that are near the current price, roughly
one average day's range above and below, so the chart is not covered in lines. Each line gets a
two- or three-letter tag at its right end, such as PDH or MO, instead of long text. Levels look the
same whether touched or not; you asked that the signal score, not the drawing, reflect whether a level
has been relevant. The statistics box sits in the top-right corner and can be hidden. Small triangles and diamonds mark stop moves and target promotions. All of it has toggles.

### D-37  Alert content  (DEFAULT)
**Default:** PickMyTrade field names plus our own logging fields (plan 4.10).

### D-38  Working loop  (DEFAULT)
**Answer:** implied yes.

### D-39  Reference material  (DECIDED)
**Answer:** All six YouTube transcripts received on 2026-09-19 and saved under
`reference/transcripts/`. The rules they contain are folded into the plan (D-51 to D-55) and listed
in `docs/RESEARCH.md` section 5. The three Facebook reels are closed as not needed: you judged the
YouTube material covers the method. The beta script remains optional.

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

## K. New in round 3

### D-48  Backtest log  (DECIDED)
Your ask: after each backtesting session, record how the version reacted, its stats, issues, and
the changes made between sessions, so problems get diagnosed instead of guessed at.
**Answer:** `docs/BACKTEST_LOG.md` holds a template with those fields. `CLAUDE.md` in the repo root
tells every Claude session to write an entry after each backtest and to ask for missing fields.
I will prompt you for the numbers each time you report a session.

### D-49  Thin-market filter for CL and SI  (DEFAULT)
Low-volume periods make the 1-minute chart on CL and SI hard to read. Optional filter: skip entries
when the last 20 candles' volume is under 40 % of that window's 20-day average.
**Default:** OFF; try it in backtesting on CL and SI.

---

## M. New from the Socrates transcripts

### D-52  Volume confirmation  (DECIDED, from the transcripts)
His most repeated rule: "all I need is volume once we hit a key level"; "the volume's there it's
going to move, the volume's not there it's not going to move"; holding through the next level only
"if the volume is following suit". The plan had no volume check. Added: a reversal entry needs the
follow-through bar's volume at or above the 20-bar average (multiplier input), and ladder promotion
needs the close-through bar's volume at or above the same average.
**Default:** both ON on the Index profile (NQ, MNQ, ES, MES), OFF on energy, metals and generic,
multiplier 1.0. Your call from round 6: the volume rule is for NQ and MNQ only. Turn off to compare in backtests.

### D-53  Break then retest at daily levels  (NOTED)
He says his go-to is "waiting for a daily high or a daily open, we would retest that, and then we
would distribute", and on the live recap: "every time we reach our daily open I like to break it
first; I made a mistake by not waiting for the break". That is a break trade with a retest entry at
the daily open, daily high or daily low. You decided break trades are off (D-50), which stands.
Recorded so that if the switch ever goes on, retest mode at the daily levels is the first variant to test.

### D-54  Asia-open continuation for gold-type assets  (LATER)
On gold he says the move around 20:15 to 20:45 CT (21:15 to 21:45 New York) "will follow the trend
within the entirety of the New York session" and calls it high accuracy. Untested. Recorded as a
later optional bias for the metals and energy profiles: during the Asia session, bias = direction
of the prior New York session. It also connects to your own feeling that SI and CL trade well at the Asia open.
**Default:** not built until backtests of the base product are done.

### D-55  His daily risk rules  (NOTED)
One to four trades a day; two losing trades in a row ends the day; a hard account lockout; a
dollar target that he raises when winning and lowers after a rough first trade. Our caps already
cover these as settings (all OFF for backtesting per D-30). One addition: `maxConsecLosses` as a
separate input from `maxLossesPerDay`, since his rule is consecutive.
**Default:** OFF.

---

## N. From the first M1 chart review, 2026-09-20

### D-56  New York session runs to the futures close  (DECIDED)
You expected the NY high at the late-afternoon 29,993 print; the script had the NY session ending
at 15:00 CT, the cash close, so that print fell outside it. The NY session is now 08:30 to 16:00 CT
on every futures profile, cash open to futures close. Crude and metals keep their pit-hour windows
as inputs. Your Asia, London, daily and midnight levels all matched the candles.

### D-57  Level display  (DECIDED)
Your asks: larger label text, a short-code or full-name option, lines that start at the candle
that made the level and stop shortly right of price, and every level drawn including the quarter
and year ones. Recorded and built in M1 v0.3: candle-anchored lines with a right-anchored
fixed-length alternative, label size input, short codes or full names, optional price in the label,
all levels drawn by default with a switch to limit to nearby ones. Spaceman parity levels added:
previous quarter high, low and mid, year mid, previous 4-hour mid, current 4-hour open.

### D-58  One line per level, full names, labels further out  (DECIDED)
Second review: you did not want nearby levels combined into one box, wanted full names as the
default with short codes as the option, and wanted labels pushed further right of price. Built in
M1 v0.4: every level draws on its own line; only levels at the same price within one tick share a
label; full names by default; label offset 20 bars. The cluster tolerance still exists for the
trading zones in M2; it no longer affects drawing.

### D-59  Session levels develop live  (DECIDED)
Second review: your chart's last candle was Friday 15:59, one minute before the New York window
closed, and the script only published a session after it completed, so the NY high shown was
Thursday's. You expect the running session's high to show while the session is live. Session
levels now update live and freeze when the session ends; "Completed only" is a switch. For the
trading logic, a developing session extreme counts as a target, not an entry level, until the
session completes.

### D-60  Match the Spaceman indicator's display  (DECIDED)
You supplied the Spaceman source. Adopted: plain coloured text labels with no box at the end of
the line, size normal, merging only at the identical price with " / ", per-level toggles (Open,
Prev H/L, Prev Mid per family, Monday Range and Mid, session H/L and Open), a global colour
switch, a line style input, year high and low that include today, and a Monday range that
develops during Monday. Kept on purpose: lines start at the exact candle of the high or low
rather than the period's first candle, levels come from the chart's own candles, sessions are
entered in your timezone, and custom levels exist. Notes in `reference/spaceman_notes.md`.

### D-61  Stagger labels that sit too close  (DECIDED)
Your note: levels too far apart to merge still had labels on top of each other. Labels closer
than a set number of ticks now step right into successive columns, up to four, so every name
stays readable. Distance, step and column count are inputs. Lines are unaffected.

### D-62  Bookmark tags are back, and the stagger has to actually separate  (DECIDED)
Your note on v0.6: the stagger was needed but did not separate the names, and you preferred the
earlier filled tags that looked like bookmarks. So: "Boxed" is the default label style again (a
filled tag with its point on the line end; "Text only" stays as the option). The stagger distance
is now a share of the daily ATR with a tick floor, and it grows with the square root of the chart
timeframe so one setting fits 1-minute and 5-minute charts. The step between columns is 40 bars
by default, wider than a full-name tag, and a level's line now runs all the way to its own tag,
so a staggered tag still hangs off its line. A label takes the first column whose previous label
is far enough below it, and the tag count per column is not limited.

### D-63  Tags share within the touch tolerance; columns sized by name length  (DECIDED)
From the v0.7 screenshots: the 1-minute chart was clean, the 5-minute chart had four tags within
11 points, one more than the three columns, so the fourth landed on another tag, and full-name
tags in one column nearly touched the next. Three changes. Levels within the touch tolerance
(0.01 daily ATR, floor 2 ticks) now share one tag with the names joined by a slash and the tag
pointing at their mean; each level keeps its own line, and setting the share distance and its
floor to 0 restores identical-price-only sharing. Each stagger column is as wide as its longest
name, from a bars-per-character input that scales with the label size, so short codes pack
tighter than full names. Five columns by default.

### D-64  Hidden confluence hooks: VWAP and the 15-minute 200 EMA  (DECIDED)
Your question: can confluences work without showing on the chart, and which one or two are worth
it. Yes: anything the script computes can feed the score without being drawn. Two hooks, built in
M3 with the score, hidden, weight 0 by default: session VWAP (its side, and how far price sits
from it in daily-ATR units, the "stretch" into a level) and a 15-minute 200 EMA trend vote. The
first M4 backtests split the hold rate by each hook; a hook gets weight only if the split moves the
hold rate by a real margin on a real sample. The only visible traces are letters on the signal
label, a "Show confluence lines" switch that is off, and the split in the statistics. POC, VAH,
VAL and options levels stay manual custom levels and are not computed. Nothing new is drawn.
This pulls VWAP and the EMA forward from M7 to M3 as hooks only; M7 keeps the weighting.

### D-65  M2 build notes: SR tolerance, pivots, verdicts, priors  (DECIDED)
Made while building M2, recorded here before the code: the SR cluster tolerance is its own input,
default 0.04 daily ATR with an 8-tick floor, twice the zone tolerance, because higher-timeframe
swing points scatter more than the labeled levels do (D-51 said "the normal cluster tolerance";
the M2 review tunes it). Pivots are 1 bar left and 1 right on the 4-hour by default, inputs.
Pivot highs and lows both count as touches of one level, the level sits at the mean of its
touches, and its line starts at the first touch. Verdicts are taken on confirmed bars only, so the
table changes only on bar close. The classifier runs per level instance, so every member of a
zone gets its own verdict, which is the plan's "credit every member" rule. The "reaches the next
zone" shortcut for HELD waits for M3's zone list; M2 uses the hold distance alone. A NEUTRAL
verdict does not use up an instance's one counted interaction. Priors are one text input,
`code:rate:count, ...`, instead of eighty separate inputs.

### D-66  Break-retest switch ON, zones hidden, M2 review fixes  (DECIDED)
From the plan review and the first M2 chart (CL 1-minute). Three things you decided:
1. **Break trades ON by default, retest entry only**, to match Socrates's go-to at the daily open,
   daily high and daily low. Still never straight off a breakout: break, then retest, then enter.
   The BRK detector moves from M7 to M3 and is built beside the REV detector, so the level
   ranking's second half (weak types traded as breaks) is live again. M4 backtests compare
   REV-only against REV plus BRK.
2. **Zones stay, hidden.** The chart keeps one line per level. Zones from the cluster tolerance
   exist only for the stack score and the stop edge, built in M3, never drawn.
3. **The rest of the plan stands** as reviewed.
And the M2 fixes from the CL chart, recorded before the code:
- SR tolerance default 0.08 daily ATR (0.04 found 0 levels from 21 pivots on CL). An SR level is
  a zone: price at the midpoint of its touches, half the spread as its width, and that width
  widens the touch band and the break and hold thresholds.
- Verdicts are judged on closes of a verdict timeframe, default 5 minutes, so the 1-minute and
  5-minute charts produce the same statistics; the verdict window is 150 minutes instead of 30 bars.
- A prior weight of 10 interactions at 0.5 for every type so one lucky touch cannot top the
  ranking. The table shows raw hold rates; the rank uses the weighted rate. Per-type priors override.
- First M4 backtest runs the base product with every optional filter off (volume confirmation,
  news blackout, opening blackout, cooldown), then adds them one at a time, each logged.

### D-67  Hold and break verdicts use the same distance  (DECIDED)
From the MNQ 5-minute chart on M2 v0.2: 36 % hold, 64 % break over 2,151 interactions. That split
was made by the thresholds, not the market: a break needed a close 0.03 daily ATR through the
level while a hold needed a close 0.10 away, and a coin-flip market "breaks" about three times
in four under those numbers. Both distances are now 0.05 daily ATR with a 4-tick floor, so a
level with no edge scores near 50 % and the hold rate reads as the reversal-versus-break odds
you asked for. The ranking is relative and was never damaged; the raw rates were misleading. The
BRK setup in M3 gets its own break-confirm input, separate from the verdict distance.

### D-68  M2 sign-off and M3 build notes  (DECIDED)
M2 passed on the MNQ 5-minute chart: S/R (5) at about 29,505 and S/R (3) at about 29,215 sit on
visible 4-hour pivot clusters, verdict marks match the candles, counts are the right size. (Your
settings had Hold confirm at 0.16 by a slip; it belongs at 0.05, D-67.) Build notes for M3,
recorded before the code:
- Signals evaluate on the chart's confirmed bars, so the 5-minute chart is the signal chart (D-21)
  until the 1-minute trigger mode arrives in M6.
- Zones are rebuilt every bar from the enabled levels within the cluster tolerance, never drawn.
  Today's high and low join as target-only members (D-15); 15-minute structure waits for M5.
- Zone history precedence for the score: broke today (3) beats held today (15) beats touched with
  no verdict (6); untouched is fresh (12).
- Zone reliability is the best member's rank; a zone of unknown types scores the neutral 20.
  Break-rank is 100 minus hold-rank.
- One signal per bar, highest score wins. After a signal the zone's members are blocked for that
  test and re-arm when a whole bar trades clear of the band; M4 adds the cooldown in minutes.
- Break trades: after a confirmed close through (own input, 0.03 daily ATR, body at least 0.5
  chart ATRs), a limit rests at the broken edge for 6 bars; a fill on the retest is the signal, a
  close back through the zone cancels it, a fill is checked before a cancel on the same bar.
- Alerts use `alert()` with the plan's JSON body, one per signal; the TradingView alert is created
  with the condition "Any alert() function call".
- HTF rejection scores 0 and bias scores neutral (7) until M6. Hooks (D-64) are computed every
  bar at zero weight and shown as letters on the label.

### D-69  Plain-language working style  (DECIDED)
Your ask after the first M3 compile error: explain things as if to someone with no coding
knowledge. From now on every message describes what a change does on the chart and what to look
for, in everyday words, with no variable names or programming terms outside the script paste.
Recorded in `CLAUDE.md` so every future session follows it.

### D-70  First M3 chart: break history, signal cooldown, compact tags  (DECIDED)
The MNQ 5-minute chart on M3 v0.2 showed 557 reversal signals and 1 break signal in about 70
days, repeat signals on the same level a few candles apart, and tags wide enough to cover the
candles. The statistics themselves read well (59 % hold overall, Monday and NY highs on top).
Three changes:
- A break trade scored its "level history" as 3 points because the level had just broken, so a
  single-level break could never reach the minimum score. Now a first break of a level scores
  like a first test (12) and a level that already held or broke earlier today scores 6.
- A level stays quiet for 12 minutes after a signal (input, 0 turns it off). This is the M4
  re-entry cooldown pulled forward for signals; M4 keeps its own after a stop-out.
- Tags show direction, setup, level and score; entry, stop, targets, hook letters and the score
  breakdown sit in the tooltip. "Full" puts everything back on the tag.

### D-71  Held and broke marks off by default  (DECIDED)
Your call after the M3 v0.3 chart: the chart should carry trade signals only; whether a level
held or broke is already in the statistics table, and you judge the signals by eye. The marks
stay available in the settings for checking the statistics.

---

## L. New in round 4

### D-50  Break trades are optional, and retest-only  (DECIDED, revised by D-66: switch ON)
Your point: the strategy is taking the trade off a pivot and trailing it to the target, so break
entries do not really fit. Agreed. A level that price rips through is already handled by the target
ladder, which keeps a running reversal trade alive through the level. A standalone break entry only
matters when we happen to be flat, so it becomes a switch, OFF by default, built in M7 for backtest
comparison. Round 6: entering straight off a breakout is bad, entering on the retest after a break
is fine. So the switch means break, then retest, then enter; no immediate breakout entry is built.
Everything in the plan that mentions BRK applies only when that switch is on.

### D-51  Untagged support and resistance levels  (DECIDED, revised from the transcripts)
Your ask: places price has touched repeatedly that are not one of the labeled levels. The videos
show exactly how Socrates does it: on the 4-hour chart he draws a line wherever price "kept coming
to a certain number", only where it "pivoted a bunch of times, not just once"; on the 1-hour he
checks which of those lines sit on a key level from the indicator; on the 5-minute he trades the
ranges between them. Added as level type SR: swing highs and lows on the 4-hour chart clustered
within the normal cluster tolerance, kept when 3 or more touches fall within the last 10 days. They
join zones like any level, their touch count feeds the stack score, an SR line on a labeled level
makes a stronger zone, they get their own hold-rate statistics, and they can trigger reversal
trades. Built in M2.
**Default:** ON, 3 touches, 10 days, 4-hour pivots. All four are inputs.

---

## J. New in round 2, from your May rules document

### D-43  Opening blackout  (DECIDED)
**Answer:** ON, 30 minutes after the cash open, index profile. You would rather remove the losing
trade than shrink it, so there is no reduced-size variant.

### D-44  Daily loss and profit limits  (DECIDED)
**Answer:** The $800 figure is relative to account size, so it is gone. Replaced by two percent
inputs: `maxDailyLossPct` and `dailyTargetPct`, both OFF for backtesting. Once live you want a loss
limit of 2 to 3 % and a target of 3 to 5 %. The target only stops new entries; a trade that is
already trailing keeps running, so a big winner is never cut short by the target.

### D-45  Stop cap in ticks  (DECIDED)
**Answer:** The 50-tick stop belonged to a different strategy. Cap stays off until backtests show
what stop sizes pay; nothing is set in stone before that.

### D-46  Size by score  (DECIDED)
**Answer:** You like the idea. Standard fixed sizing for now, size-by-score stays in the settings
to experiment with during backtesting.

### D-47  TradeZella export  (CLOSED, not needed)
**Answer:** Your call: the journal predates this strategy and would only show personal tendencies.
Session and level statistics come from the bot's own backtests instead. The search for the file is
over. Profiles stay as proposed.
