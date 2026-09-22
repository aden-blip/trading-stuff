# Method audit: what the transcripts teach against what the script does

Written 2026-09-22 alongside D-99 and D-100. Sources read in full: the six Socrates transcripts
in `reference/transcripts/`, `reference/links.md`, `reference/spaceman_notes.md`, `docs/PLAN.md`,
`docs/DECISIONS.md` (D-01 to D-99), `docs/RESEARCH.md`, `docs/BACKTEST_LOG.md` (sessions 1 to 20),
`pine/l2l.pine` (M6 v0.5) and `reference/backtests/2026-09-21/report_M6v0.1_deep-365d.md`.
The six transcripts are the whole evidence base: `reference/links.md` records that the Facebook
material was never readable and nothing else was ever supplied.

**The finding in one line.** The script implements the method's level book and its rejection
candle faithfully and almost nothing else. Every one of the four conditions the method puts in
front of the trigger — a level where price has pivoted repeatedly, a directional read, volume
behind the move, and no trade in chop — is absent, switched off, or present in a form the method
does not use. So the 365-day result in D-99 measures the trigger with none of the conditions.

---

## 1. Level selection: the one rule, and the family that breaks it

The method marks a level only where price turned more than once: "I'm only marking major areas
where it pivoted a bunch of times, not just once but a bunch of times" and "I make my trade
strictly off of these blue lines" (transcript 3). On the 1-hour those hand-drawn lines are kept
only where they land on a key level: "all my blue lines that I ever create will probably be by a
major key level or a major pivot and that's the only thing that I care about" (transcript 3).

In the script that rule exists once, as the repeated-touch `SR` family (three touches, 4-hour
pivots, `pine/l2l.pine:119-127`, D-51). It carries about 100 of the year's 2,963 trades. The other
37 families are entry-eligible with no touch history required at all.

The largest group in the year has no basis in the source. The "4-hour" family in the script means
the previous 4-hour bar's high, low, mid and open plus the current 4-hour open — 1,539 trades and
-38,401 USD, the current 4-hour open alone 620 trades and -27,174 at a profit factor of 0.65. The
method never mentions previous-4-hour-bar levels; its 4-hour work is the drawn pivot lines.

The level-code table and the method agree on the axis without being told to:

| Pays | Loses |
|---|---|
| NL, PDH, PWH, QO, PMM, PMH, SR3, AO, YH, YO, MNH | 4HO, DO, P4H, P4L, P4M, P4O, WO, NO, MNM, LH, PWM, MOO |

Everything on the left is a place price turned and stopped turning there long ago. Everything on
the right is a line drawn through where price already is — a fresh open, a mid-point, a boundary
that refreshes every four hours or every day. That is the same separation as the two leaks in
D-99 point 2, arrived at from the source instead of from the data.

One corroboration worth keeping. The method says the daily open is not a reversal level: "every
time we reach our daily open I always like to break it first, so realistically I made a mistake
by not waiting for the break of that key level" (transcript 4). In the year the daily open is
343 trades and -11,438 at a profit factor of 0.71. The source predicted that before the data was
taken, which is the opposite of fitting.

## 2. The directional read: required in the source, a constant in the script

The method sets a bias before charting, from news and from the top down: "when we hop in the
market we need to get our bias before charting" and "I start at the weekly, then the daily, the
4-hour, the 1-hour, 30-minute, the 5-minute" (transcripts 5 and 6), with the higher timeframe
winning: "this timeframe outweighs my analysis on this timeframe" (transcript 4). It changes the
bias when a level holds or fails on the higher timeframe, not when an average crosses: "based on
the 1-hour it changed up a little bit, because now I noticed how we came to this price range, our
daily high, we didn't even cross it, we touched it and price quickly fell and rejected"
(transcript 6). And it reads direction off whether a session level survived: "let's say we did
not break previous London open, so maybe we're still bullish based on this fact" (transcript 3).

In the script the bias term of the score is a hard-wired constant — every trade in every
direction gets the same points (`pine/l2l.pine:1416`). Bias has no effect on any decision. The
higher-timeframe input that does exist (M6) is a candle-shape count, weight 0 and gate off after
D-94. The session-open bias specified in plan 4.9 has never been built.

This matters because D-99 point 3 found the losing core is being on the wrong side of the move,
and D-80/D-88 rejected *trend* gates by eye. A "did the higher-timeframe level hold or fail" read
and a "price above or below the prior session's opens" count are different objects from a trend
gate, and neither has been built or measured.

## 3. Volume: the only confirmation the source names, and it has never been switched on

"All I would need is volume once we hit a key level." "The volume's there, it's going to move;
the volume's not there, it's not going to move." "Are we at a key level and is there volume —
that's the only thing I need." "The only thing I'm using is key levels and volume and that is
it, I don't need anything else." (transcripts 2, 4 and 6.) The indicator named is Bull vs Bear
Power, i.e. the split between buying and selling volume, not the total.

In the script `volConfirmIn` defaults to "Off" (`pine/l2l.pine:154`), applies to reversals only,
and measures total volume against a 20-bar average — which D-78 point 2 already recorded as the
wrong measurement: "it measures busier than the last 100 minutes, not buying or selling pressure
at the level". The directional split D-78 specified was never coded. No session in
`docs/BACKTEST_LOG.md` has volume confirmation on, in either form.

## 4. No trade in chop: the hardest rule in the source, with no active version

"If we are in a day where we're ranging between key levels I don't have a trade and I shouldn't
trade, because my setup won't show up and my trades will probably hit my stop losses." "As long
as we're between my certain key levels, I like to call it chop." (transcript 6, and the same in
transcripts 2 and 3.)

Both implemented filters are off: the chop band (`chopOn` false, and D-81 notes its 0.25 % over
30 minutes is probably narrower than a normal MNQ 30-minute range, so it needs rescaling before
it is worth a run) and the range-edge filter (`rangeOn` false, run once on 73 days of paper
trades, never on the tester with costs). The script takes roughly 12 trades a day precisely
because 38 families put price near a level at all times — which is the source's own definition
of chop.

## 5. Risk rules: none of them active

| Source | Script |
|---|---|
| "between one and four trades a day" | no cap (`maxSigDay` 0); the year runs about 12 a day |
| "two losing trades in a row and my trading day is done" | not built; only a daily total exists, off |
| a lock-out number per account, a daily target | both off, never run |
| "I'm only in two lots, it's a scalp" | 2 contracts — matches |
| New York open to close, done by mid-morning | session filter off; the script trades 24 hours |
| no trades near the holidays, Friday is thin | no weekday or holiday rule |
| no cooldown after a stop-out | only a per-level signal wait |

D-30 turned the caps off for measurement, which was right. The consequence is that the strategy
has never been evaluated as the thing the source describes. It also bears directly on D-92,
D-93 and session 20, where every change that scratched trades early freed the strategy to take
more of them and each one loses on average: a hard trades-a-day cap attacks that mechanism head
on and has never been run.

## 6. The correlated instruments: an entire video with no implementation

The first transcript is the strategy's namesake — the NASDAQ and the VIX side by side on the
5-minute, entered short because "NASDAQ is rejecting our Monday high while at the same time the
VIX is starting to get some buying power up, so I'm going to enter a short based off of this
information alone", with the VIX level as the invalidation: "if this was to break lower then my
idea would clearly be shot". For NQ it also names NVDA, SPY and the big tech names; for gold, the
dollar and the other metals.

`pine/l2l.pine` contains no reference to the VIX, QQQ or any of the Magnificent 7. Plan 4.9
specifies all of it and reserves the request budget; 10 of 40 security calls are used, all on the
chart's own symbol. This is the only independent information source in the whole method — every
filter tested in D-84 through D-99 is another slice of the same MNQ 5-minute series.

## 7. Targets and stops: the geometry is inverted

The source exits at the next place price turned, and books the trade when there is nothing near:
"pivots to pivots, key level to key level", "between here and here is anywhere I would look to
take profits", and "I don't have any upper pivots close by in the 5-minute, so I will just take
profits for $320" (transcripts 1 and 2). Its stop is just past the one level: "I'm only in two
lots, it's a scalp, we can have it right above this Monday area" (transcript 1), cut fast.

The script requires the first target to be at least 0.15 daily ATR away (`tgtUnit`,
`pine/l2l.pine:169`), roughly 45 points on MNQ, so the true nearest level is skipped and the
trade aims past it — median winner 88.8 points. When no target qualifies the setup is discarded
instead of taken with another exit. The default stop is beyond the far side of a whole cluster,
52 to 63 points. So the script swings two levels out with a wide stop where the source scalps to
the first line with a tight one. D-97 and D-98 are already on the stop; the target distance has
never been varied in any run.

## 8. What the source says not to do, and where the script agrees

Respected: no order blocks, no liquidity or fair-value-gap concepts, no RSI, no moving-average
signals (the 15-minute EMA hook exists at weight 0), no chasing, no straight breakout entries,
one instrument at a time.

Violated: trading inside a range between levels, overtrading, no two-loss stop, holding through a
level without a volume check (impossible — the target ladder was never built), and the source's
own warning against complexity: "when I put more things in my trading I have more fear, I miss
entries, my biases get shot" (transcript 4) against roughly 40 parameters, 38 level families and
a five-component score. `docs/PLAN.md:811` already flags this risk in the plan's own words.

## 9. Instrument and timeframe

Gold is the source's primary market — four of the six videos — and it is not on the roadmap; the
Metals profile already supports MGC and GC, so it is a run with no code. The source's recent
entry timeframe is the 1-hour ("lately I've been getting entries on the 1-hour timeframe alone"),
which is also D-94's own suggested next step and again needs no code.

## 10. The untested list, cheapest first

Items 1 to 8 need no code change.

1. Levels where price has turned only: prior day, week, month, quarter and year highs and lows,
   the session highs and lows, Monday high and low, the three-touch repeated levels, the owner's
   own boxes. Off: every open family, every mid family, the whole previous-4-hour-bar family.
   Named in D-88 and in sessions 10 and 11 as the next test; never run.
2. New York session only. Named as pending twice; never run. Note New York is the worst window in
   the year as things stand (profit factor 0.79), so this is a real test.
3. Opening blackout on. Held on both halves in D-91 point 3; the owner's own TradeZella data
   agrees; never run.
4. Four trades a day and two losing trades a day.
5. Volume confirmation on, as it stands, to put a number on it at last.
6. Chop band, rescaled first per D-81.
7. Range-edge filter on the year with costs.
8. The first target at the true nearest level (`tgtUnit` toward the tick floor), with the stop at
   the rejection wick and the cap on.
9. Break-retest at the daily levels only — D-53's named "first variant to test". Break trades are
   already the better setup and positive in three of four session windows.
10. The VIX moving the other way over the last few 5-minute bars, as a score bonus and then as a
    gate, with the VIX's own key level as the invalidation. One security call.
11. The bull-versus-bear volume split, specified verbatim in D-78 point 2.
12. Prior-day and prior-session rejection count per level. Nothing in the script counts a
    rejection before today; the "held today" flag is usually set by the signal's own candle
    (D-91 point 2). This is the cleanest formal version of the source's selection rule.
13. Session-open bias: price above or below the prior session's open, the daily open and the
    midnight open, net two either way is directional. Plan 4.9; replaces the constant.
14. A touch entry with a resting limit at the level and no candle required — what the source
    actually does in transcript 1, and D-98 point 4's not-built item.
15. Take the setup with no qualifying target and exit on time or on R instead of discarding it.
16. Magnificent 7 or NVDA and SPY participation in the trade's direction.
17. Higher-timeframe level-hold read, distinct from the candle count D-94 measured and from the
    trend gates D-80 and D-88 rejected.
18. Multi-candle sweep and reclaim (M7, D-76); the third-party write-up calls it the core.
19. Target ladder with volume-confirmed promotion (plan 4.7, D-34, D-52).
20. Weekday rule: Wednesday is the worst day in every sample (D-91 point 3) and Sunday is -54.4 a
    trade. The source's Friday caution is contradicted by the data, which is itself a finding.
21. Gold on the existing Metals profile, and a 15-minute or 1-hour signal chart.

## 11. The two observations that matter most

**The confirmation stack is inverted.** The source needs four things to line up before it acts —
a level that has pivoted repeatedly, a level from its own short list, volume behind the move, and
a market that is not chopping — plus a bias from news and the higher timeframes, and for NQ the
VIX turning the other way. The rejection candle is its *timing*, not its *filter*. The script has
the timing implemented precisely and every one of the filters off, absent, or in a form the source
does not use. D-94's conclusion, that the two-candle rejection at a key level on MNQ 5-minute has
no edge that survives both halves, is therefore a correct measurement of the trigger alone. It is
not yet a measurement of the method.

**Every filter tested so far re-slices the same price data.** Score, stack, level history, session
windows, hour, weekday, level type, higher-timeframe rejection count, stop and target geometry:
all functions of the MNQ 5-minute series. The source contains exactly two inputs that are not —
volume, never once switched on, and the correlated instruments, zero lines of code. Both are
cheap. Neither can be skipped before the method is called measured.
