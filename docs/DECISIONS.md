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

### D-72  Signal tags show an arrow and the score only  (DECIDED)
Your call: the tag should carry just the direction and the score, with everything else in the
hover box. Default "Minimal": `▲ 76` for a long, `▼ 78` for a short, tag size normal. Green and
red are reversal trades, blue and orange are break trades. Hovering shows the setup and the
level, entry, stop, targets, hook letters and the score breakdown. "Compact" and "Full" remain
as options.

### D-73  Score shown out of 10  (DECIDED)
Your ask: "X/10". The tag now reads `▲ 8/10` or `▼ 7/10`. The engine still scores 0 to 100 so the
breakdown and the minimum-score setting keep their precision; the tag rounds to the nearest whole
point (76 becomes 8/10, 64 becomes 6/10). The hover box shows both, for example
`LONG REV PDH  8/10 (76 of 100)`. The alert message keeps the 0 to 100 number for the bridge.
With the minimum at 60, tags read 6/10 to 10/10.

### D-74  First manual-versus-script comparison, MNQ 18 Sep  (DECIDED, corrected in round 2)
You marked seven boxes on Friday 18 September (MNQ 5-minute): six trades you would have taken by
hand and one plan for the Sunday open. The script signalled four that day and only one of them
was on your list (the short at London Low / London Open, 08:35 CT [09:35 NY]). The other five
fall into four groups; item 5 is the plan.
1. **Entries in the direction of a move with no retest and no rejection candle** (long at the
   Daily Open about 22:30 CT [23:30 NY] as price climbed through it; long at the Midnight Open
   about 23:25 CT [00:25 NY] out of a tight pause before the jump). The strategy never takes
   these: a break trade needs the retest (D-23, D-66) and a reversal trade needs the rejection
   candle plus follow-through (plan 4.4). Unchanged by design. Round 2, your question whether a
   switch was off: no. Break trades are ON by default in every M3 version and you had not touched
   settings; the entry did not come because the pullback to the broken level never arrived
   inside the retest window. The strong-rejection switch (OFF) only concerns reversal candles
   and would not have changed this.
2. **Sweep and reclaim** (long at the Asia Open about 11:35 CT [12:35 NY] after the three-candle
   dip below it). Price arrived from the wrong side, so the reversal rule cannot fire. This is
   the sweep-reclaim-retest entry planned for M7. The NY Low under that dip was still forming
   during the New York session, so it was a target only (plan 4.1). Round 2, your reading: those
   three 5-minute candles are one wick on the 15-minute, price came back quickly, and the
   1-minute would have given the entry, after which the trailing stop rides the move. Agreed;
   that is now the M7 sweep definition (D-76).
3. **A level the script does not know**: both shorts at 29,895, a 4-hour pivot you marked by
   hand. The SR finder keeps only 4-hour pivots with 3 or more touches inside 10 days, so a
   single swing is not found. Resolved by D-75: your hand-drawn pivots go into the settings as
   prices and get every rule. The earlier question about 5-minute swing levels is closed, not
   needed.
4. **Close calls that depend on the score or the volume rule** cannot be settled by eye, so the
   script now explains itself: "Explain missed signals" puts a grey `?` on any candle where a
   setup formed but a rule stopped it, with the reason in the hover box. Off by default; turn
   it on for reviews. Built in M3 v0.7.
5. **A plan, not a miss**: the short box at the NY High / London High sits to the right of
   Friday's last candle. It is your plan for the Sunday open if there is no gap or big news.
   Nothing to check until it trades. One thing to watch there: the volume rule compares a
   candle with the average of the previous 20, which at the Sunday open are Friday's last hour,
   so a thin Sunday-evening candle can fail it and get a grey tag saying volume.

### D-75  My pivots: hand-drawn higher-timeframe pivots as inputs  (DECIDED)
Your ask: when you draw a pivot line on a higher timeframe, the indicator should be able to use
it. A script cannot read chart drawings, so the closest thing is ten price boxes in the settings
("My pivots"). Each price becomes a level of type PIV: it joins zones, counts toward the stack,
gets its own hold-rate row in the statistics table, and can give reversal and break signals and
grey tags. Pink lines tagged Pivot 1 to Pivot 10, starting at today's open; 0 means empty.
Custom levels (POC, VAH, options) stay a separate type so the two hold rates are not mixed. To
catch more pivots automatically, "Touches needed" under SR can be lowered from 3 to 2. Built in
M3 v0.8.

### D-76  Sweep definition for M7: a higher-timeframe wick  (DECIDED)
Your reasoning on the Asia Open long: three 5-minute candles below the level are one wick on the
15-minute, price came back quickly, and the 1-minute gave the entry. So the M7 sweep-reclaim
entry is defined as: price closes beyond a level for up to `sweepBars` chart candles (default 3
on the 5-minute, one 15-minute candle), then closes back through it. That reclaim candle is the
rejection candle; the entry comes from the 1-minute trigger (M6) or the follow-through candle.
Open for M7: whether such a short excursion should count as HELD rather than BROKE in the
statistics. Order unchanged: M4 backtests first, then M5, M6, M7.

### D-77  Alerts, named trade-management alerts, and running unattended  (DECIDED, explained in chat)
Your three questions after the script is done.
1. **Alerts tied to signals.** Already there: the indicator fires one alert message per signal.
   One TradingView alert on the script with the condition "Any alert() function call" catches
   them all; delivery to the phone app, email and the webhook. Alerts run on TradingView's
   servers, so the PC can be off. Two chores are yours: re-create the alert after every new paste
   (an alert keeps running the version it was created on), and make it open-ended (Premium)
   or it expires after two months.
2. **Named alerts for trade management.** The M5 trade manager emits one message per event
   (entry, TP1 reached, stop to break-even, trailing move, partial, exit, flatten, flip), each
   with the level names and prices. Built two ways so you can pick: the single catch-all alert
   whose message text names the event, and separate named alert conditions ("L2L: TP1 hit",
   "L2L: stop moved", and so on) so each event can be its own alert with its own sound.
3. **Running while away.** The chart and alerts already run on TradingView's servers. Orders
   need the bridge (D-03, PickMyTrade): the alert goes to its web address and it places, moves and
   closes the orders at Tradovate. Stops and targets are sent with the entry, so they rest at the
   broker even if TradingView or the bridge hiccup later. The 15:55 CT flatten and the daily loss
   limit (D-44) guard an unattended run. Cash account: no rule against it. Prop firms: Apex bans
   unattended 24/7 bots and allows supervised alert-driven automation; confirm in writing before
   running live (RESEARCH 4). Set up in M4 on a Tradovate demo account, which costs nothing.

### D-78  Review defaults: score minimum 40, volume rule off  (DECIDED)
The grey tags showed that the trades you would have taken died on two rules: "score under 60"
and "volume 0.x times the 20-bar average". Both are looser during the review, for these reasons.
1. **Score.** Today the score can only reach 82 of 100: the HTF rejection part (10) and the
   bias part (15, fixed at the neutral 7) arrive in M6. A level on its own on its first touch of
   the day scores 24 plus its reliability, and reliability is 0 to 40 by the hold-rate rank of
   its type: best type 64, middle type 44, worst 24. So with the bar at 60, only the few
   best-ranked types could fire alone; everything else needed two or more levels stacked. That
   was not the plan's intent (60 of 100, "first tests trade on their own"). The ranks also rest
   on about 70 days of one chart. **Now:** minimum 40 (4/10), which lets a middle-ranked level
   fire alone and still blocks the worst-ranked ones. The bar goes back to 60 when M6 fills the
   score, and the M4 backtest reports results by score bucket (4/10, 5/10, 6/10 and up) so the
   final bar comes from numbers, not taste.
2. **Volume.** The rule was a stand-in for "volume following suit": the follow-through candle's
   volume at or above the average of the previous 20 candles. It fails more than half of all
   candles on its own, because a few huge candles pull the average up, so most candles sit
   below it. It also measures "busier than the last 100 minutes", not buying or selling
   pressure at the level: after a busy open the calm-down candles all fail, in a quiet stretch
   anything passes. **Now:** Off (D-66 already made it an optional filter for M4 to test).
   **M4 variant to test:** Socrates reads his Bull vs Bear Power indicator, which splits each
   candle's volume into a buying share and a selling share by where the candle closed in its
   range. The faithful rule is directional: for a long, the follow-through candle's buying share
   beats its selling share; for a short the reverse. Build that as the alternative and compare
   off / average / bull-bear in the M4 backtest.
Built in M3 v0.9 as defaults only; a v0.8 paste can be set the same way by hand. The bar of 40
is superseded by D-79: with the score scaled to the reachable maximum, the review bar is 50.

### D-79  Score reads out of what is reachable  (DECIDED, your idea)
Your point: if the most a setup can score today is 82, then 82 is really 100. Agreed. The score is
now raw points divided by the points the current weights can produce, times 100: reliability 40,
stack 20, history 15, the neutral bias 7, plus any hook weights you turn on, so 82 today. A fresh
level on its own now reads 78 (8/10) for the best-ranked type, 54 (5/10) for a middle type, 29
(3/10) for the worst. When M6 adds the HTF rejection points and the full bias range, the reachable
total becomes 100 and the tags keep their meaning. Changing a weight in the settings also
rescales, so the weights are relative importance, not absolute points. Review minimum 50 (5/10),
which passes the same trades as the raw 40 of D-78; the plan's 60 returns after M6 and the M4
backtest by score bucket sets the final bar. Built in M3 v0.10.

### D-80  One trade at a time in the indicator, and what the 40-versus-60 screenshots showed  (DECIDED)
Your before-and-after on Friday 18 September (MNQ 5-minute, volume rule off): at the old bar of
60 the chart had 4 signals; at 40 it had about 25, including the ones you wanted, plus many
"that would not make sense" and some in the opposite direction minutes apart.
1. **Most of the noise is the indicator having no position.** It marks every setup. A bot in a
   trade would never take the long at the Midnight Open at 13:00 CT and the short at the Prev
   4H Open at 13:03 CT both; it would be long and stay long. Walking that day one trade at a
   time (in at the signal, out at the stop or the first target): the 09:22 long, the 10:08 short,
   the 11:47 long and the 13:00 long all reach their first target, the 10:45 long and the 11:20
   short stop out. Six trades, four winners, instead of thirteen tags. So the indicator now
   follows a paper trade (this decision) and shows only what the bot would take. The M4
   strategy replaces it with real fills, costs and slippage; M5 adds partials and trailing.
2. **The counter-trend signal cannot be told apart at the candle.** The 08:39 short at London
   Low / London Open (8/10, a big winner) and the 13:03 short at the Prev 4H Open (6/10, a
   loser) are the same shape: a rally that broke levels on the way, a rejection candle, a
   follow-through candle. Checked by eye on that day, every simple trend gate (price versus the
   session VWAP, versus the 15-minute 200 EMA, "levels broken in the last 30 minutes") blocks
   the 08:39 winner as well as the 13:03 loser, and the plan's chop filter at its default band
   would block the 06:30 and 08:39 shorts too. So no trend gate now. The planned answers stay:
   the score bucket backtest in M4 (do 6/10 trades pay?), the bull-versus-bear volume test in M4
   (D-78), bias and higher-timeframe rejection in M6, and the chop band tuned on data (D-28).
3. **Repeats at the same level** (the 06:50 short 20 minutes after the 06:30 one) disappear
   with the paper trade too, because the first trade is still open.
Inputs: entry cutoff 15:00 CT [16:00 NY] and flatten 15:55 CT [16:55 NY] from the plan, both
switchable, exit marks, two info-box rows. Built in M3 v0.11.

### D-81  Chop: trade the edges of a range, not the middle  (DECIDED as a test switch)
Your thought on the same screenshot: nothing in the script notices chop, and the signals in the
middle of the screen sit inside a range, "almost a crappy AMD setup" (accumulation, then the
sweep of the low, then the real move up). Checked against that day: the plan's chop band
(D-28, 30-minute range under 0.25 % of price) would have blocked the 06:30 and 08:39 shorts that
you liked, because a 30-minute stretch on MNQ is usually that narrow. What separates the good
trades from the bad ones there is not "range or not" but "edge or middle": the 08:39 short at
the top of the range and the 09:22 long near its bottom paid; the longs and shorts at the
Midnight Open, Daily Open and Prev 4H Open in the middle mostly did not. So the test version is
a range-edges rule: look back 120 minutes; if that stretch is narrower than 0.5 daily ATR and a
level sits in its middle half, no reversal entry there. Off by default, because on that day it
also skips the 12:28 and 13:00 longs that paid, which were the first legs of the move out of
the range. The M4 backtest measures it next to the plan's band rule; the M7 sweep-reclaim entry
is the "manipulation, then distribution" trade you describe. Built in M3 v0.12.

### D-82  Paper trade breakdown, and what the first full tally says  (DECIDED)
Your v0.12 screenshot, MNQ 5-minute, defaults (minimum score 50, volume rule off, one trade at
a time, range filter off): Paper trades 807: 176 T1, 592 stop, 39 flat; Paper points −1280.75;
Signals 569 REV, 238 BRK. About one trade in five reached its first target and the net is a
small loss before commissions and slippage (about −$2,560 on one MNQ; costs would take roughly
another 1 to 2 points a trade, 800 to 1,500 points over 807 trades). Per trade the loss is
small, −1.6 points on average. So this is not a broken bot; it is a coin that lands slightly
against us under the crudest possible trade: in at the close of the follow-through candle, stop
under the whole zone plus the buffer, out only at the first target or the stop, nothing in
between. Recorded as Session 1 in `docs/BACKTEST_LOG.md`.
1. **Why one in five.** The entry candle has already moved away from the level, so the stop
   (beyond the far side of the zone) is wide, while the first target (the next zone, at least
   0.15 daily ATR away) is not proportionally farther. The reward is about two to three times
   the risk, and at that payoff you need one winner in three or four just to break even.
   Entering nearer the level (a limit at the level, or the 1-minute trigger in M6) shrinks the
   risk without moving the target; that is the whole reason the plan has the 1-minute trigger,
   and it is your Asia Open example (wick, quick return, entry on the 1-minute).
2. **What the tally cannot say yet.** Whether the 7/10 and 8/10 trades pay while the 5/10 ones
   lose; whether REV pays and BRK drags; whether New York hours pay and the overnight hours
   lose; and what partials, a breakeven stop and trailing (M5) turn the 592 stops into. Also,
   the ranks were built on the same candles the trades ran on, so live results would if
   anything be a little worse than this tally, not better.
3. **Decision.** No rule changes on one number. First split the tally so the next screenshot
   answers the first three questions: a breakdown table by score (5/10 or less, 6, 7, 8 or
   more), by setup (REV, BRK) and by session window (Asia, London, New York, other hours), each
   with the trade count, the share that reached T1, the average gain, the average loss and the
   net points, plus the first trade's date and the trading days covered. Built in M3 v0.13, on
   by default, with a position setting. Rule changes come from the M4 strategy tester, which
   runs the same splits with costs; the entry style (close of the follow-through candle, a
   limit at the level, the 1-minute trigger) is the first thing it compares.

### D-83  The payoff decides, not the score; reversal entry and stop switches  (DECIDED)
Your two v0.13 screenshots (MNQ 5-minute, 7 Jun to 18 Sep 2026, 72 trading days; range filter
off, then on), logged as Session 2 in `docs/BACKTEST_LOG.md`.
1. **The hit rate is the same everywhere.** Every group reaches its first target about one time
   in four or five: low scores, high scores, reversals, breaks, every session window. Nothing
   the bot measures today picks winners.
2. **The payoff decides.** Every group whose average winner was more than three times its
   average loser made money: the 5/10 and 6/10 trades and the break trades. Every group under
   two and a half times lost: the 7/10 and 8/10 trades and the reversals as a whole. In the
   columns: 5/10 trades win +157 and lose −44; 8/10 trades win +134 and lose −63; break trades
   win +126 and lose −22.
3. **Why the high scores carry the wide stops.** A high score today mostly means a stacked zone,
   two or three levels close together. The zone is wider and the stop sits beyond the far side
   of the whole zone, so the stack bonus is buying a wider stop, not a better trade. Break
   trades have tight stops because their entry is at the level, the broken edge, not a candle
   or two away like the reversal entry. The score is not re-weighted on this: fix the geometry
   first, then read the buckets again.
4. **Range filter: no verdict.** It removed 43 trades and improved the net by about 550 points,
   but with one trade at a time every skipped trade changes the trades after it, and the session
   rows flipped sign between the two runs, so that gain sits inside the noise. Stays off; the
   M4 tester measures it.
5. **Sessions: no conclusion**, for the same reason. Asia went from the best window to the worst
   by skipping twelve trades.
6. **Decision, built in M3 v0.14 as test switches.** Reversal entry: the close of the
   follow-through candle (plan default), a limit at the level after the follow-through, or a
   limit at the level right after the rejection candle (your quick-return entry, no
   follow-through needed). Reversal stop: beyond the zone (plan default), beyond the rejection
   wick, or the farther of the two, the options the plan lists under D-22. A resting reversal
   limit is cancelled by a close back through the zone and expires after 6 bars (input). One
   honesty fix with it: a limit that fills and crosses its stop on the same candle counts as a
   stop, for break retests too, as the strategy tester would count it; break numbers drop a
   little from v0.13.
7. **Caveats.** 72 days, in-sample ranks, no costs, and the 5/10 bucket holds only 100 trades.
   The pattern is strong and the same in both runs, which is why it earns a test now and not a
   rule.

### D-84  The hit rate follows the stop; the raw trigger has no edge; split by level type  (DECIDED)
Your v0.14 run with the limit entry after the follow-through and the wick stop (Session 3, run
E): 908 trades, 13 % reached T1, net −3356.75. Reversals 512 trades, 12 %, average gain
+132.25, average loss −27.75, net −3028.25; breaks 396, 14 %, +117.25, −22.00, −328.50. Against
the baseline the reversal stop halved, from 63 to 28 points, and the hit rate halved with it,
from 24 % to 12 %. Per trade the reversals lost 5.9 points instead of 4.5, and measured against
the risk taken, 21 % of the stop per trade instead of 7 %.
1. **No geometry makes the raw trigger positive.** A trade that flips a coin reaches its target
   before its stop about stop ÷ (stop + target) of the time. With the baseline geometry that is
   31 %, and the reversals reached 24 %. With the tight geometry it is 17 %, and they reached
   12 %. Moving the entry and the stop only trades hit rate for payoff, and both land a little
   under a coin flip. The switches stay in the script for the M4 tester; they are not the fix.
2. **Stacked zones are worse than a coin flip, single levels are at it.** Baseline: the 5/10 and
   6/10 trades, mostly one level, reached the target 24 % of the time against a coin flip of 22
   to 23 %; the 7/10 and 8/10 trades, two or three levels, reached it 21 to 22 % against 31 to
   32 %. That ten-point gap is the one real signal in three sessions of tables, and it matches
   your read of the clusters in the middle of the range: a pile of session opens and mids near
   the current price is a chop zone, not a pivot.
3. **Decision, built in M3 v0.15.** Split the paper trades by level type and by how many levels
   sit in the zone: three columns on the statistics table (paper trades, T1 share and net points
   per level type, a stacked trade counting in every member's row) and three rows on the
   breakdown table (1 level, 2 levels, 3 or more). No rule change. If a few types carry the
   winners, the M4 defaults turn the others off for reversals. If none do, the edge has to come
   from context the bot does not have yet, the higher-timeframe rejection and bias of M6 and
   the sweep entry of M7, and M4 is built as the tester for that work, not as a finished
   strategy.
4. **M4 default unchanged:** entry at the close of the follow-through candle, stop beyond the
   zone, the plan's choice, with the entry and stop switches carried over.

### D-85  Level types and stack: nothing in the level set separates winners at this sample; M4 next  (DECIDED)
Your v0.15 screenshot (defaults, Session 3 run F, the same 812 trades as the baseline).
1. **Stack rows.** One level in the zone: 312 trades, 19 % reached the target, net −2239. Two
   levels: 278, 27 %, +1527. Three or more: 222, 22 %, −2048. So the "stacked zones lose"
   reading in D-84 was too simple: the two-level zones are the best group and the single levels
   the worst.
2. **Type columns, the top 15 by hold rate.** The types the ranking trusts most are net losers
   as reversal trades (Monday High −292, Monday Low −325, London Low −320, London High −1646,
   Prev Day High −90, Asia Low −558) and the middle of the ranking holds the winners (Prev 4H
   Mid +1325, NY Low +792, Midnight Open +573, Asia High +496, Asia Open +340). The hold-rate
   rank, 40 of the score's 82 points, predicts the verdict rule it was built on, a close 0.05
   daily ATR back from the level, not whether the trade reaches the next zone. That is why the
   7/10 and 8/10 trades lose: they carry the top-ranked types.
3. **What this is not.** With 20 to 100 trades per row, one or two trades move a row by a
   thousand points, and the rows overlap (a stacked trade counts in every member's row).
   Switching on the green types and off the red ones would be fitting 73 days of noise. No type
   filter and no weight change from this table.
4. **Decision.** The indicator has done its job as a lab: it found the question (which levels,
   in what context) and showed that 73 days cannot answer it. Milestone 4 now, for three
   reasons: Deep Backtesting runs the same rules over years of 5-minute data instead of 73 days;
   the tester adds commissions and slippage; and its trade list can be exported. The score
   weights, the entry and stop switches, the range and chop filters and the tables all carry
   over as inputs, so every split above can be re-read on the long sample before any rule
   changes. Whether the reliability weight should be 0 is the first thing to test there.
5. **Ask:** one more screenshot with Statistics, Rows set to 40, so the log holds every type.

### D-86  Milestone 4 v0.1: how the strategy places and fills orders  (DECIDED)
1. **Fill model.** Market entries fill at the next candle's open, as the plan says a bridge would
   fill them (4.7, process_orders_on_close off). Resting limits fill at their price. The flatten
   order is placed on the candle before the flatten time so it fills at the open of the flatten
   candle, 15:55 CT [16:55 NY], instead of the next session's open. The paper tally now follows
   the same model, so the two can be cross-checked in the info box; costs are the difference.
   The tally reads a candle the way the tester does: the price goes from the open to the
   extreme nearer the open, then to the other extreme, then to the close. When two resting
   orders were crossed in one candle, the one that path reaches first is the fill; an order the
   open gapped through fills at the open; and the rest of the path decides whether the stop or
   the target was hit on the fill candle. The flatten fills at the open of its candle, ahead of
   that candle's own stop or target.
2. **Resting orders.** Break retests and the reversal limit modes are real tester limit orders
   with their stop and first target attached. Geometry, gate, score and filters are checked when
   the order is placed, because the tester cannot refuse a fill later; a fill is the signal.
   Nothing is placed while a position is open, and every other resting order is cancelled when
   one fills or a market entry is placed, so one position at a time holds in the tester too
   (pyramiding 0 as the backstop). All entries sit in one cancel group, so when a resting order
   fills the tester cancels the others inside the same candle; two orders crossed in one candle
   can no longer both fill. Resting orders are cancelled inside the entry cutoff window and
   with the flatten order, after that candle's fills are read.
3. **Filters [F].** Built as inputs, all off for the base run (plan 4.6): allowed session
   windows, opening blackout (D-43), news blackout (D-40), chop band (D-28), daily trade and
   losing-trade caps, daily loss limit and daily target (D-44). They only block new entries.
4. **Costs.** MNQ defaults in the script: 0.80 per side, 2 ticks slippage, initial capital
   50,000, from docs/RESEARCH.md. Other contracts change them in the tester's Properties tab.
   Order size is the Contracts input (2), which also drives the alert quantity. Margin is 5 %
   of the contract value for longs and shorts (v0.3), about the exchange margin on a micro
   contract; the tester's default of 100 % treats one MNQ contract as 60,000 of cash and
   rejected every order on the 50,000 account, which is why the v0.2 run showed zero tester
   trades. Margin calls cannot arise from this: two contracts need about 6,000 of the 50,000.
5. **Not in v0.1:** the trade manager (M5, so exits are the hard first target only), size by
   score (D-46), the thin-market filter (D-49), the bias gate (M6), and the bridge check on a
   sim account, which follows once the tester run is read.

### D-87  Level lines are placed by time in the strategy  (DECIDED)
The M4 v0.1 paste stopped on the last candle: TradingView refused a level line starting 3,000
candles back by candle count ("The requested historical offset (3001) is beyond the historical
buffer's limit (300)"), which the indicator version had accepted, and because the drawing runs
before the info box and the tables, all of them were missing. Level lines and their tags are
placed by time, from a list of one time per candle, so a line still starts at the candle that
made its level and the longest-line setting keeps its meaning. Signal, exit and explanation
tags stay on their own candle by count. No trading rule changed. From v0.4 the strategy
recalculates on every tick (the tester's "On realtime bar tick" setting), so the drawings
refresh live as the indicator did instead of only at each candle close; orders and the tally
are placed on confirmed candles only, so the tester's history is the same either way.

### D-88  No trend-bias gate; selection stays inside the reversal concept  (DECIDED)
Proposed after the M4 base run: build the Milestone 6 bias gate (reversals only with the
higher-timeframe direction) before the Milestone 5 trade manager. The owner declined: the
strategy's purpose is to take reversals at levels, and a direction filter works against that.
Agreed. What stays in scope for finding the edge, all inside the concept and all testable with
switches before any code: fewer and stronger levels (the 40 drawn levels put price near a
level at all times, so "at a level" alone says nothing); stacked zones only (two or more
levels, the only stack group in the black so far; testable now with Reliability 0 and History
0, which leaves the stack as the whole score); stronger rejection candles (wick share, candle
size); the range-edge filter (D-81); the session windows; and later the trade manager (M5)
for the payoff. From Milestone 6 only the higher-timeframe rejection confirmation stays (a
bigger candle rejecting the same level is still a reversal signal); the bias inputs are
parked until a test asks for them. Test discipline: every change is judged on the long
sample with initial capital 500,000 in the Properties tab so no run is cut short by the
margin floor; profit factor, trade count and net in USD are compared, and a keeper must hold
on both halves of the range.

### D-89  The exported trade list is the analysis path  (DECIDED)
Four long-sample runs (base, Asia only, Asia plus stacked, stacked only) came back with
profit factors between 0.81 and 0.88, one screenshot each. Slicing by switch is slow and
answers one question per run. From M4 v0.5 every entry order carries a comment with the
trade's setup, zone code, score, stack, level-history points and session window, and every
exit says T1, stop or flat. The tester's export of a Deep Backtesting run then holds every
trade with those tags plus its run-up and drawdown, and one file answers the whole list:
expectancy by setup, window, stack, score, history and level type; how far winners and
losers travel before they resolve, which sets what a partial, a breakeven stop or a tighter
stop would have done; hold times; hour of day. Switch tests continue only for changes the
export cannot answer (entry at the level, stop at the wick, the rejection candle rules,
fewer levels), because those change the trades themselves.


### D-90  What the first trade list says: the manager comes first, the level's day history second  (DECIDED; point 2 withdrawn by D-91)
The 769-trade export of the chart-range run (session 14, tool `tools/trade_list_report.py`,
file and readout under `reference/backtests/2026-09-21/`) decides the order of work.
1. **M5, the trade manager, is the next build.** Half the stop-outs had been half a stop in
   profit and a quarter a full stop in profit before they reversed to the stop; the losers that
   had reached +25 points lost 68,976 USD between them, which a stop at entry would have turned
   into scratches. What that rule costs on winners only the script can measure, so the
   manager is built as the plan has it (D-32 staged stops in R: +0.5R half risk, +1R breakeven
   plus cushion, +1.5R trail; D-33 partials as an option; D-34 ladder and soft targets) and the
   tester measures each stage against the hard-target base. Exact readings from the file:
   one contract off at a run-up does not turn the sign on its own (-11,385 at +50), nor does a
   closer target (-6,000 at 40 to 50 points) nor a tighter stop (-5,100 at 40 to 50 points).
   The export cannot rate a wider target or a trail at all, so those wait for M5.
2. **The level's history today matters, and the score has it backwards.** A reversal at a
   level that already held today lost 16,928 USD on 297 trades, at a level already touched
   today 9,775 on 174, in every window and stack size; the first test of the day was flat and
   the retest of a level that broke earlier today positive (mostly five big trades). The score
   awards held 15 points, first test 12, touched 6, broke 3. No change to the weights yet: the
   365-day export decides, and if it agrees the change is a switch "one reversal per level
   per day" (skip held-today and touched-today levels) rather than new points, so the rule
   reads plainly on the chart. The reversal concept is untouched: the first rejection at a
   level still trades; only the second attempt at the same level in the same day does not.
3. **Hours, level types and the rest are hypotheses.** The cash-open hour and the 17:00 CT
   [18:00 NY] reopen hour lose, the two 4-hour opens lose, scores of 80 and up lose, retries
   within two hours lose. The 73-day Asia reading already failed on the long sample, so none
   of these changes a default until it holds on both halves of the 365-day export (D-88
   keeper rule). The existing switches test the ones that need no code: the opening blackout
   for the cash open, the news blackout with 1700 listed and 60 minutes after for the reopen,
   the 4-hour Open and Prev Open boxes, the minimum score. A daily loss cap showed nothing
   consistent and is parked; the retry rule is small and waits.
4. **Workflow.** Every export is saved under `reference/backtests/<date>/` with the tool's
   readout next to it, and the readout is what the log quotes. The long-sample readout is
   also split into halves (first six months against the last six) before any rule is kept.


### D-91  The 365-day list: the manager first, the level-history reading withdrawn, filters wait  (DECIDED)
The 2,963-trade export of the year (session 15, halves split with `tools/compare_trade_lists.py`,
files under `reference/backtests/2026-09-21/`).
1. **M5, the trade manager, is the next build, as the plan has it.** In every sample a
   quarter of the losing trades had been a full stop in profit before they reversed to the
   stop, and those trades cost 79,138 USD over the year. Every exact what-if from the file
   (closer target, tighter stop, one contract off) is worse than the trades as taken; the
   only lever with a large upside is the stop that moves after a run-up, and its cost on the
   winners (47 % of them went half a stop against first) can only be measured in the script.
   Ceiling for the D-32 stages, losers exact and winners untouched: +59,412 for the year,
   positive in both halves. M5 v0.1 builds the first two stages of D-32 (half the risk after
   +0.5R, breakeven plus cushion after +1R) behind a manager switch whose OFF position
   reproduces the M4 trades; the +1.5R trail, the ladder with soft targets (D-34) and the
   partial option (D-33) follow in v0.2, so each piece is measured on its own. The paper
   tally keeps mirroring the tester: both get the same moved stop at the same candle close,
   and the tally now fills a gapped open at the open as the tester does. Exits at a moved
   stop carry "half" or "be" in the export, so the next trade list shows what each stage
   did to the losers it was meant to catch and to the winners it scratches.
2. **D-90 point 2 is withdrawn.** The "held today" tag is usually set by the rejection candle
   of the very trade (verdicts are judged on 5-minute closes), so it marks a rejection that
   closed at least the hold distance away from the level, not a second test of the day. A
   reversal after a losing trade at the same zone earlier in the day performs like a first
   trade. No "one reversal per level per day" switch is built. The history points in the
   score stay as they are until the score is revisited with M6.
3. **Filters that hold in both halves are recorded, not applied.** No entries in the two
   hours after the cash open and the two hours after the 17:00 CT [18:00 NY] reopen, and no
   zones with a 4-hour open, take the year from -57,795 to -8,950 by removal alone, break-even
   in one half and a loser in the other, on half the trades. Wednesday loses in every sample
   without a mechanism beyond news. The New York low is the one level positive in both
   halves. None of this changes a default now: the manager changes what every slice is
   worth, so the filters are re-read on the managed trades, through the existing switches
   (opening blackout, news blackout with 1700 listed, the 4-hour Open and Prev Open boxes).
4. **Noise, recorded so it is not re-asked:** score buckets, stack size, session windows
   (Asia in particular), retries within two hours, and the summer's best level types all
   flip sign between halves.
5. **The year's loss sits in four months** (December, February, March, July: -48,786, PF
   0.66); the other eight are near flat (-9,008, PF 0.96). The manager is judged on those
   four months as much as on the total.


### D-92  The staged stops measured: a fifth less bad per trade, more trades; the trail is next  (DECIDED)
Session 16, the M5 v0.1 run against the M4 run trade by trade (`tools/compare_runs.py`).
1. **What the stages did.** On the 2,671 entries both runs took, the stages turned -52,188
   into -41,836. The half stage is worth +9,018 (412 stops caught for 39,447, 52 winners cut
   for 27,492); the breakeven stage +1,334 (445 stops caught for 60,107, 126 winners
   scratched for 52,429). The export's ceiling counted only the catches; the scratched
   winners cost almost as much.
2. **Why the headline got worse.** Scratching early frees the strategy for 1,255 more
   trades, and they lose at the usual -19 a trade: -23,807. The manager changes what a trade
   costs, not whether the entry has an edge; while the entry loses on average, more trades
   is worse. A wait after an exit would only trade less (the early re-entries lose at the
   same rate as the rest) and is not built.
3. **The trail is the missing stage.** 323 of the 611 breakeven exits were entries that had
   run two stops or more in profit in the M4 run before coming back: M4 made +33,706 on
   them, M5 scratched them all. D-32's third stage keeps part of such a run. M5 v0.2 builds
   it as the plan has it: from +1.5R the stop follows the higher (long) of the last confirmed
   swing low minus half an execution ATR and the close minus two execution ATRs, only ever
   tightening, checked every closed candle; exits at it are tagged "trail"; the stop in force
   is drawn as a line. Stage thresholds and the hard first target stay; the ladder, soft
   targets and partials (D-33, D-34) wait for the trail's reading.
4. **How v0.2 is judged.** Not on the headline: on the same-entries comparison against the
   M4 file (matched net, the transition table) plus the extra trades' cost. If the manager
   with the trail does not beat the hard-target M4 trades by a clear margin on the same
   entries, its default goes OFF and the work moves to the entries (M6, the higher-timeframe
   rejection, D-88).


### D-93  The manager is parked with its switch off; the entries come next, starting with the higher-timeframe rejection  (DECIDED)
Session 17: with the trail the year reads -65,875 on 4,208 trades against -65,643 for the
stages alone and -57,795 for the hard-target trades. Per trade the manager is a fifth less
bad (-15.65 against -19.51); in total it is worse, because scratching early frees the
strategy for a third more trades and every trade loses on average. The same-entries reading
of the v0.2 file is still owed and is recorded when it comes, but the bar of D-92 is not
cleared by the headline.
1. **Manager switch OFF by default.** The stages and the trail stay in the script with every
   input, so they can be turned on for any run, and they are re-judged once the entries have
   an edge: a per-trade improvement only pays on entries that make money.
2. **The entries are the work.** Every selection reading so far (D-84, D-85, D-91) says the
   raw rejection at a level has no edge on this year of MNQ, and only two filters held on
   both halves (the two hours after the cash open and after the 17:00 CT [18:00 NY] reopen;
   zones built on a 4-hour open), together worth less bad, not good. What is left inside
   the reversal concept (D-88): a bigger candle rejecting the same level. M6 v0.1 builds it
   as plan 4.8 has it: the last completed 5-minute, 15-minute, 1-hour and 4-hour candles
   are checked for a rejection of the zone (traded in, closed back, wick of 0.4 or more of
   the range); the count goes into the tag as f0 to f4 and the label as HTF x/4.
3. **Measured before weighted.** The HTF weight in the score starts at 0 and the gate at
   off, so the v0.1 base run takes the M4 trades exactly and the export splits them by the
   count. The weight (the plan's 10) and the gate ("at least N of 4") are set only if the
   count separates winners from losers on both halves of the year; a gate run then confirms,
   because a skipped trade frees the strategy for trades the export cannot show.
4. **The bias inputs stay parked** (D-88). If the higher-timeframe rejection does not
   separate the trades either, the concept as specified has been measured on this
   instrument and timeframe, and the next decision is the owner's: the instrument, the
   timeframe, or the trigger itself.

### D-94  The higher-timeframe count is measured: it does not separate the trades on both halves; weight 0 and gate off stay; the next call is the owner's  (DECIDED)
Session 19: the M6 v0.1 export (the M4 trades exactly) split by how many of the last
completed 5-minute, 15-minute, 1-hour and 4-hour candles rejected the zone. Year: PF 0.80 /
0.79 / 0.91 / 1.11 for counts 0 to 3 (675 / 1,054 / 441 / 99 trades), seven trades at 4.
First half 0.91 / 0.80 / 0.77 / 0.96, second half 0.74 / 0.78 / 1.00 / 1.28. As a gate,
"at least 2" is 547 trades, -4,933, PF 0.93 (-6,477 at 0.79, then +1,543 at 1.04); "at
least 3" is 106 trades, +635 (-913, then +1,548).
1. **The rule of D-93 point 3 is not met.** The count makes the trades less bad over the
   year, but the halves disagree on the order (a count of 2 did worse than a count of 0
   in the first half) and no gate is profitable on both halves. The HTF weight stays 0 and
   the gate stays off; both inputs remain in the script for any later run.
2. **What a count of 1 means.** On the 5-minute chart the 5-minute candle in the check is
   the rejection candle of the signal itself, so a count of 1 says the rejection candle
   had a wick of 0.4 or more of its range; only a count of 2 or more brings a bigger candle
   into it. The export carries the total, not which candles counted. If the idea is ever
   revisited, the tag names the candles (5, 15, 60, 240) so the 15-minute and the 1-hour
   can be read apart.
3. **The M6 concept as specified is measured (D-93 point 4).** With the manager (D-92,
   D-93), the score, the stack, the level history, the windows, the hours and the level
   types (D-91), and now the higher-timeframe rejection all read on the same year, the
   two-candle rejection at a key level on MNQ 5-minute has no edge that survives both
   halves. The next decision is the owner's and is not taken here: the instrument (CL/MCL
   or SI/SIL, which the plan lists after MNQ), the timeframe (a 15-minute or 1-hour chart,
   where the rejection candle is the bigger candle by itself), or the trigger (something
   other than the two-candle rejection at the level). The first two are runs of the
   present script with no code change; the third is design work. None of the recorded
   leads (the two hours after the cash open and after the 17:00 CT [18:00 NY] reopen, the
   4-hour opens, New York inside the count-2 group) is applied: they are removal filters
   that make a losing year less bad, and they wait for whichever path the owner picks.
4. **One cheap check on M6 remains, optional.** A gate run at "Reversals need at least" 2
   on the tester, same range and capital, confirms or denies the -4,933 with the trades a
   skipped signal frees up. It tells whether the count-2 group is break-even on the
   tester, not whether it is a strategy, and it is not needed before the owner's choice.

### D-95  A "Signals only" switch: labels without trades, for watching the chart  (DECIDED)
The owner asked how to stop the chart showing a trade they are not in: the tester's pretend
position, its stop line and the "in a long" text, and the fact that no new signal shows while
that pretend trade runs. M6 v0.2 adds one switch in the Signals group, "Signals only: labels,
no trades", off by default.
1. **On:** every setup that passes the entry rules gets its label, and nothing else happens:
   no order to the Strategy Tester, no paper trade, no stop line, no exit marks, no stage
   marks and no alerts (an entry alert with no exit alert behind it must never reach a
   bridge). Setups that would rest a limit order (the limit reversal styles and the break
   retests) still label at the candle where the order would have filled, so a label sits
   where a trade would have started. The same-level quiet time and the level re-arm still
   apply, so a level does not repeat its label; the daily signal cap counts the labels; the
   daily loss cap cannot apply. Because no pretend trade blocks the next setup, the chart
   shows more labels than the tester would have traded.
2. **Off (default):** as before, one trade at a time in step with the tester, and the chart
   shows the tester's trade while it is open. Backtests run with the switch off; it changes
   nothing in them.
3. The M6 measurement (D-94) stands. This is a display convenience for watching the chart or
   trading by hand, not a change to the rules.

### D-96  A position visual at every signal, running until the next signal; the tester's arrows are a chart setting  (DECIDED)
The owner's asks of 22 Sep: the tester's blue and purple arrows and their text should go, and
each signal should draw its plan, the stop, the targets and the R steps between them, running
to the right until the next signal.
1. **The tester's markers are TradingView's, not the script's.** Pine cannot switch them off.
   They are absent in "Signals only" mode (no orders), and in trading mode the Style tab of
   the script's settings has "Trades on chart"; unticked and saved as default, they stay off.
2. **M6 v0.3 draws the position at every signal** (group "Position visual"): a green box from
   the entry to the first target, a red box from the entry to the stop, lines at the entry,
   the stop, the first and second targets, a dotted line at every R step (0.5R by default,
   at most 8) from the entry to the farthest target shown, and labels for SL, E, T1 and T2
   (price and R) and for the steps. The newest position runs to the right and its labels
   follow price; the next signal stops it at that bar and starts its own, and the old labels
   move to the bar their position started on. The last 8 positions stay (input, up to 30).
   It draws the plan as of the signal: the entry is the planned one (the close for a market
   entry, the limit for a resting order) and a stop moved by the manager is not redrawn; the
   "Stop in force" line shows that. On by default in both modes; nothing in the trades
   changes.
3. **Profitability stays the job.** Nothing here changes a trade. The next step on the edge
   is still the owner's pick of D-94 (the market, the chart timeframe, or the trigger), and
   the two no-code runs (MNQ 15-minute, MCL 5-minute) remain the cheapest tests.

### D-97  Tight stops on the same entries are measured: less bad, never positive; the idea points at the entry  (DECIDED)
The owner's read (22 Sep): the stops are large; the entry should be good enough that a trade
barely goes against, and when it does the loss is cut fast, so a winner is many times a loser.
The year's export tests the stop half of that exactly, because each trade carries how far it
went against before it ended (session 15's what-ifs, extended on the M6 v0.1 file).
1. **Same entries, tighter stop, same targets:** stop 5 pts -30,947 (win 4.9 %, PF 0.56);
   8 pts -25,231 (8.2 %, 0.74); 10 pts -26,732 (9.9 %, 0.77); 12 pts -24,075 (11.7 %, 0.82);
   15 pts -29,955; 20 pts -33,050; 25 pts -33,321; as traded -57,795 (26.5 %, 0.84). The best
   of them cuts the year's loss by more than half and stays a loser. Costs are about 21,300 for
   the year (commission and two ticks each way on two contracts, 2,963 trades) and every extra
   small stop adds to them.
2. **Why: the pullback is the drawdown.** The entry is the close of the follow-through candle,
   a candle or two off the level, and the winners come back toward the level before they go:
   the median winner dipped 14 points first, 62 % of winners dipped 10 or more, half 15 or
   more, 40 % 20 or more. A 10-point stop would have stopped 490 of the 784 winners before they
   won. Each what-if lands the hit rate where a coin flip puts it, stop over stop plus target
   (10 % expected at a 10-point stop, 9.9 % measured), which is D-84's finding again: this
   entry carries no information about what comes next, so no stop or target geometry turns it
   positive.
3. **A tighter stop and a closer target together cannot be read from the file:** for 800 to
   1,500 trades both the stop distance and the closer target were crossed and the export does
   not say which came first; the bounds run from -50,000 to +175,000. Only a tester run
   settles it.
4. **The idea is about the entry, and the switches exist.** Entering at the level instead of a
   candle or two away is "Reversal entry: Limit at the level after the follow-through" or
   "Limit at the level after the rejection candle", with "Reversal stop: Beyond the rejection
   wick", so the stop sits just past the wick, not past the whole zone. Measured once, on the
   73-day paper sample without costs (session 3 run E, D-84): the stop halved from 63 to 28
   points and the hit rate halved from 24 % to 12 %, a small loss either way. Never run on the
   year with costs. Decision: the next runs are those two entry settings, each with the wick
   stop, on Deep Backtesting "Last 365 days" at 500,000, exported and read the same way
   (halves, dip before the win, hit rate against the coin flip). No code change. A "cut
   quickly" rule beyond the stop (a time-based or R-based early exit) is not built until those
   runs show the entry at the level has an edge, because point 1 says cutting faster on this
   entry does not flip the sign.

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
