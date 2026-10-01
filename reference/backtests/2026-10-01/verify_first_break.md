# Adversarial check of the first-break finding, 2026-10-01

Five independent lenses were run against the claim that a reversal at a session high or low
pays when it is the first trade that day at a level that had been broken. **All five refuted
it at high confidence.** Verdicts below as returned, lightly formatted.

## Lens: out-of-sample — REFUTED (high confidence)

**Reproduced the numbers exactly, but the rule fails every out-of-sample test that matters: the same first/later split applied to the neighbouring slices nobody looked at reverses sign, and in the blind half of M6 the "first break" profit is two trades wide.**

### Numbers

REPRODUCTION (exact match to the primary analyst): M6 session REV hist3, n=276, +5,798. FIRST n=240, win 37.9%, PF 1.28, +8,915, +37.15/trade. LATER n=36, win 19.4%, PF 0.46, -3,117. M7 FIRST n=42, PF 1.19, +341. (A variant that ranks only over session codes gives 231/45 and +10,256/-4,458, so the split is also sensitive to how multi-code zones are ranked.)

1. M6 HALVES, BLIND TEST. Derive on H1 (FIRST n=107, PF 1.69, +6,755; LATER n=14, -1,837, permutation p=0.005) and apply blind to H2: FIRST n=133, PF 1.10, +2,160, +16.24/trade, bootstrap 95% CI on the mean [-57.69, +93.63] — includes zero. LATER in H2: n=22, -1,280, -58.20/trade, permutation p=0.23 — not distinguishable from drawing 22 trades at random from the same 276. The blind half's +2,160 falls to +86 if you remove its single best trade and to -1,348 if you remove its best two of 133. Over the full year, removing the 8 largest winners of 240 flips +8,915 to -163; median FIRST trade is -123.

2. CROSS-EXPORT. M7 FIRST +341 over 42 trades (+8.11/trade) is one trade wide: minus the best trade it is -275, minus the best two -478; median -59; 7 of its 12 months are negative. Its two "agreeing" halves are +141 (n=26, -62 without one trade) and +200 (n=16, -416 without one trade). M7 does not confirm anything — it is 42 trades of noise around zero.

3. WALK FORWARD, M6 by month. FIRST positive in 11 of 13 months (Sep25 -69, Oct +1,219, Nov +2,248, Dec +365, Jan +717, Feb +1,014, Mar -1,172, Apr +293, May +5, Jun +1,819, Jul +727, Aug +1,153, Sep +595). That looks good, but Nov+Jun alone are +4,067 of +8,915. LATER is where it breaks: of the 11 months that contain later trades, 4 are positive (Oct +238, Apr +413, Jul +814, and Jun/Sep flat-to-small), and 84% of the whole -3,117 is two months — Mar26 and May26 together -2,622 over 16 trades, with 11 of the 36 later trades falling in May alone. Excluding those two months LATER is n=20, -495, -24.75/trade, PF 0.82 — effectively flat. In the freshest stretch, Jun-Sep26, LATER is n=6, PF 1.76, +496 — positive. By quarter, LATER: 2025Q4 -366 (n=7), 2026Q1 -2,236 (n=10), 2026Q2 -1,011 (n=13), 2026Q3 +496 (n=6).

4. GENERALITY (the decisive test). Apply the identical first/later split to slices never examined. REV hist3 on NON-session codes: FIRST n=291, PF 0.76, -10,887; LATER n=54, PF 1.29, +1,899 — the opposite sign on a LARGER later sample than the claim's. Session codes with hist6 (touched): FIRST n=153, PF 0.68, -5,784; LATER n=7, PF 1.21, +142 — again reversed. Session hist15 (held): FIRST -7,533, LATER -4,150 — both negative. There is no consistent "first good, later bad" mechanism anywhere else in the book.

CONTEXT the claim omits: the whole M6 export nets -57,795 over 2,963 trades and M7 nets -1,426 over 417. Mar26 and May26, which carry the LATER loss, cost the whole book -7,825, so the "later breaks lose" result is partly just two bad months for everything.

### What would change the verdict

What survives: session REV hist3 as a slice is mildly positive in both M6 halves (+4,918 / +880) and in 11 of 13 months, and that is worth keeping as a direction. What does not survive is the first-vs-later filter, which is the actual claim. The whole claimed gain over simply taking all 276 is the removal of 36 trades, and 36 trades cannot carry a rule: its loss is two months deep, it is insignificant in the blind half (p=0.23), it turns positive in the most recent quarter, and it reverses outright on the adjacent code and history slices. I would change my verdict if a fresh year, or a different instrument, showed the later-break slice losing with n well above 100 and with the loss spread across most months rather than concentrated in Mar/May, and if the non-session-code reversal disappeared. I could not test anything outside these two exports of the same year on the same instrument, so a genuine liquidity-taking effect cannot be ruled out — it just is not visible here. One caution for the write-up: even the surviving FIRST slice rests on a handful of trades (8 of 240 carry all of it, median trade is a loss), so it should not be described to the owner as "profitable" in any dependable sense.

---

## Lens: multiple-comparisons — REFUTED (high confidence)

**Refuted: the +37.15/trade is the best of ~70 comparable slices and sits inside the noise band (search-corrected p≈0.60), and the "first vs later" mechanism is a day-selection artifact — on the 29 days that contain both, the FIRST trades (-98.00/trade) are worse than the later ones (-86.59/trade).**

### Numbers

REPRODUCTION (exact match to the analyst): M6 REV/hist==3/session codes n=276 avg +21.01; FIRST n=240 win 37.9% PF 1.28 net +8,915 avg +37.15 (H1 +6,754.6 / H2 +2,160.4); LATER n=36 win 19.4% PF 0.46 net -3,117.2 avg -86.59. M7 FIRST n=42 PF 1.19 net +340.6 avg +8.11 (H1 +140.8 / H2 +199.8); M7 LATER n=2.

(1) THE SEARCH GRID (setup x hist state x level code x first/later, M6): 342 non-empty cells; 97 with n>=20, 70 with n>=30, 41 with n>=50, 8 with n>=100. The claimed cell ranks #6 of 70 at n>=30, #4 of 41 at n>=50, #1 of 8 at n>=100. Cells beating it at n>=30 and also positive in both halves: REV h15 SR3 first (n=33, +75.32), REV h3 P4L first (n=57, +63.98), REV h15 NL first (n=49, +56.29), REV h3 AO first (n=67, +56.01), REV h3 P4M first (n=74, +47.88). 10 of the 70 n>=30 cells are positive in both halves, so the "both halves agree" rule screens out almost nothing once 70 cells have been looked at — it is a ~14% filter, not a test.

(2) RANDOMISATION (M6, 4,000-20,000 draws, both trade-level and day-block shuffles; day-block respects same-day correlation and gave essentially identical results): claimed cell's own t vs zero = +1.50 (per-trade sd 384.5, naive SE 24.82, day-clustered SE 24.67, day-bootstrap 95% CI -10.3 .. +86.2, P(true avg<=0) = 0.063). Search-corrected p-values for that cell: max-t over the 70 cells with n>=30 → p=0.602 (day-block 0.602); same requiring both-halves-positive → p=0.569 (0.573); max-avg over the 70 cells → p=0.996. The only framing that survives is max-avg restricted to the 4 cells with n>=150 → p=0.015, and that framing is circular (it pretends the analyst only ever considered the four biggest aggregates). Shuffling net across the REV population and asking whether the cell beats the POPULATION mean gives p=0.0009, but the REV population averages -24.08/trade and the whole export -19.51/trade, so that only says the slice is less bad than a losing strategy, not that it makes money.

(3) THE MECHANISM FAILS ITS OWN TEST. Of 165 days with eligible trades, only 29 contain both a first and a later trade — all 36 "later" trades live in those 29 days. Same-day comparison: FIRST n=46 avg -98.00 (net -4,508.2) vs LATER n=36 avg -86.59 (net -3,117.2); same-day gap = -11.42, i.e. the wrong sign. FIRST trades on the other 136 days: n=194 avg +69.19 (net +13,423.2). So the headline gap of +123.73 decomposes into a same-day "being first" effect of -11.42 and a day-selection effect of +167.20. Within-day permutation test (net shuffled inside each day, preserving day and level structure): p=0.664 for the first-group average and for the first-minus-later gap. The free (structure-ignoring) shuffle inside the 276-trade pool gives p=0.024 — the entire apparent significance comes from ignoring that the later trades are concentrated on 29 bad days. The signal is "days that only produce one broke-level session reversal are good days", which is not knowable at the moment the first trade is taken.

(4) "FIRST" IS NOT A GENERAL EFFECT: first-minus-later for REV session trades by history state: h3 +123.73, h6 -58.03, h15 +33.04; BRK: h6 -178.71, h12 +72.40. Signs are random across cohorts.

(5) M7 IS NOT A CONFIRMATION: +8.11/trade on 42 trades, t=+0.40, day-bootstrap 95% CI -28.8 .. +51.6, P(avg<=0)=0.372; its "later" arm is 2 trades. It is equally consistent with zero and with +37; it has no power to confirm or refute.

PLAIN ANSWER TO Q3: +37.15/trade on 240 trades is INSIDE the noise band. Expected best-of-70 under pure noise reaches this level roughly 60% of the time, and the slice is not even reliably above zero on its own (one-sided p≈0.063 before any correction).

Scripts: /tmp/claude-0/-home-user-trading-stuff/6989730c-7669-5053-bda1-37ab57e05047/scratchpad/{repro,grid,perm,perm2,paired,maxstat,final}.py

### What would change the verdict

What would change the verdict: (a) a genuinely held-out period — not a half-split of the same 365 days, and not M7, which is the same year re-run with a different config and so shares the same days and the same luck; (b) a same-day test that comes out positive, i.e. on days containing both, the first trade beating the later one. Right now it loses by 11/trade. (c) a pre-registered reason to look at hist==3 session levels specifically, rather than it being cell #6 of 70. What I could not test: whether the "quiet day" signal is tradeable through some observable known before the first entry (e.g. ATR, overnight range, news) — that is a different and possibly real finding, but it is not the claim under test and would itself need a fresh search budget. Also note my grid treats each level code independently and reconstructs the search space as I believe the analyst explored it (setup x hist x code x ordinal = 342 cells); if the analyst also varied score, stack, window, hour or weekday, the true search space is larger and the corrected p-value is worse, not better. One sanity limit: the within-day test rests on just 29 mixed days, so it cannot prove the first/later effect is exactly zero — but it does show the headline gap is not where the analyst located it.

---

## Lens: artifact — REFUTED (high confidence)

**Refuted: "first break" is not what separates the winners — 46 of the 240 "first" trades sit on level/days that get revisited and lose -153.77 each (PF 0.20, bad in both halves), so the rule keeps the worst trades in the sample; the profitable part is "the level was only tested once that day", which is only knowable after the fact, and the FIRST bucket itself is not statistically distinguishable from zero out of sample (H2 +16.24/trade, P(mean<=0)=0.34; M7 +8.11/trade, P=0.37).**

### Numbers

REPRODUCED (M6, REV + hist==3 + session codes, rank = min over codes): ALL 276 PF 1.15 +5,798 (+21.01/tr); FIRST 240 win 37.9% PF 1.28 +8,915 (+37.15); LATER 36 win 19.4% PF 0.46 -3,117 (-86.59). M7: ALL 44 PF 1.11 +219; FIRST 42 PF 1.19 +341 (+8.11); LATER 2 (-121).

1. THE DECOMPOSITION THAT KILLS IT. Split FIRST by whether that (day, session code) is tested again later the same day:
   FIRST on a revisited level/day: n=46, win 13.0%, PF 0.20, -7,073, -153.77/tr. Halves: H1 -86.67/tr (n=19), H2 -200.98/tr (n=27) — bad in both.
   FIRST where the level/day is tested once only: n=194, win 43.8%, PF 1.68, +15,988, +82.41/tr. Halves: H1 +95.47 (n=88), H2 +71.57 (n=106) — good in both.
   All trades on a revisited level/day (46 firsts + 36 laters): n=82, PF 0.30, -10,190, -124.27/tr.
   So the live separator is not the ordinal. Within the revisited level/days the FIRST trade (-153.77) is WORSE than the later ones (-86.59) — the opposite of the claimed liquidity mechanism. The tradable "take only the first" rule keeps all 46 of the worst trades in the book and removes only 36 of the 82.

2. THE FILTER BARELY FILTERS, AND THE EDGE IT CLAIMS IS INHERITED. FIRST is 240/276 = 87% of the hist==3 population. Marginal value of first-ness over simply taking all hist==3: +3,117, i.e. +11.3/trade spread over 276 trades. And the hist==3 layer itself fades: H1 +40.64/tr (PF 1.40) to H2 +5.68/tr (PF 1.03), and M7 +4.98/tr. M7's "confirmation" is vacuous: FIRST = 42 of 44 trades, LATER = 2 trades.

3. SIGNIFICANCE / FRAGILITY OF PART A. FIRST mean +37.15, median -123.2, stdev 384.5, t = 1.50. Day-block bootstrap (days as blocks, 165 days): all +37.15 CI [-10.13, +86.10] P(mean<=0)=0.064; H1 +63.13 CI [+6.49, +120.31] P=0.015; H2 +16.24 CI [-54.70, +93.49] P=0.335. M7 FIRST +8.11 CI [-29.05, +52.18] P=0.367, against an M7 session-REV baseline of +0.55/tr. Top 3 trades = 52% of the +8,915; top 10 = 119% (drop the 10 best and the bucket is negative). By quarter: 2025Q4 +72.3/tr, 2026Q1 +9.0, Q2 +37.8, Q3 +37.0.

4. DEFINITIONAL QUIRK — THE TAG IS A ZONE-LEVEL OR, NOT THE SESSION LEVEL. pine/l2l.pine line 1306: hNew = vt == 3 ? 3 : (vt == 2 and h != 3) ? 15 : ... is applied per level while walking the levels stacked in one zone, so a zone reads "broke" if ANY stacked level carries a standing broke verdict, and a later "held" cannot overwrite it inside the zone. Mean stack of these trades is 2.33 and only 69 of 276 are stack==1, so for ~75% of the sample "the level's history tag reads broke" may refer to a different level than the AH/AL/LH/LL/NH/NL code. REV also reads zHist, which includes a verdict made on the current bar (zHistP, the pre-bar state, is used only by BRK, line 2149) — so for a stacked neighbour the tag can be set by the signal's own candle, the mirror of D-91 point 2. The coded level itself cannot be tagged broke by its own rejection candle (f_rejBar requires backSide: the close is back on the hold side), so stack==1 is the clean form of the claim — and it fails: stack==1 FIRST n=57 PF 1.19 +1,445 (+25.34/tr) but H1 +60.73 / H2 -8.82 (PF 0.95), i.e. negative in the second half, breaking the both-halves rule. stack>=2 FIRST n=183 PF 1.30 +40.82/tr. Rank-definition sensitivity: MIN over codes 240/36; MAX over codes 218/58 (+44.58 / -67.60); MIN over session codes only 231/45 (+44.40 / -99.07).

5. CONTROLS — these the claim does survive. Reweighting FIRST to LATER's hour-band x window x direction mix (100% weight coverage) only moves FIRST from +37.15 to +25.58. LATER-weighted FIRST-minus-LATER differences, stratified one factor at a time: hour band +111.80, weekday +118.77, direction +123.49, stack +123.15, score band +134.38, htf count +122.21, window +132.61, session code +114.91 (raw diff +123.73). Permutation of the first/later label within strata: hour band x window p=0.027, score band x stack p=0.020, pooled p=0.025 (one-sided). Hour profile: FIRST 00-07 CT +70.00/tr (n=96, +6,720 = 75% of the whole net) vs non-h3 session-REV baseline -11.20 there; 08-10 +22.56 (base -17.97); 11-15 -35.30 (base -24.72); 17-23 +55.53 (base -46.30). So neither hour nor weekday manufactures the gap — but the whole claimed edge is concentrated in the overnight 00-07 hours.

6. MECHANICS — no geometry artifact, and what there is runs the wrong way. Realized stop distance (stop exits) FIRST med 47.0 / mean 54.3 pts vs LATER med 44.2 / 48.1; target distance (T1 exits) FIRST med 96.0 / mean 115.7 vs LATER med 112.9 / 106.7; median R:R 2.04 FIRST vs 2.55 LATER, so later breaks get the slightly wider target. MAE med 38.7 vs 39.7 (identical). Difference is in realized outcome: MFE mean 67.7 vs 50.9, stop-out rate 60% vs 78%, bars med 10 vs 7. Score 69.5 vs 70.2, stack 2.33 vs 2.25, htf 0.80 vs 1.08, long share 46% vs 47% — the two groups are the same setups.

7. "LATER IS WORSE" IS NOT SPECIFIC TO "BROKE". Same rank split at other history tags, session REV: hist==15 FIRST 414 PF 0.87 (-18.20/tr) vs LATER 81 PF 0.60 (-51.24); hist==6 FIRST 153 PF 0.68 (-37.80) vs LATER 7 PF 1.21. Repeat trades are worse generally, which is a day-quality effect, not a liquidity property of broken session levels. Context baselines: whole M6 book 2,963 PF 0.84 -57,795; all REV 2,276 PF 0.83; session REV 934 PF 0.92; by tag hist 6 PF 0.70, hist 15 PF 0.83, hist 3 PF 1.15.

### What would change the verdict

What would change the verdict: a real-time-observable proxy for "this broken session level will be tested only once today". That split is the strongest thing in the data (194 trades +82.41/tr PF 1.68, both halves, vs 82 trades -124.27/tr PF 0.30, both halves) and it is worth hunting — but as stated it uses the rest of the day, so it is not a filter, and the ordinal "first" does not approximate it (46 of the 240 firsts are the revisited, losing kind). What I could not test: LATER is 36 trades in M6 and 2 in M7, so Part B of the claim can never be established on this data whichever way it points; and there are no stop/target fields in the export, so stop and target distances are inferred from realized exit prices on stop and T1 exits only (flat exits excluded, 18 FIRST / 2 LATER). The stack==1 reading that isolates a genuine prior break of the session level itself rests on 57 FIRST trades and is negative in the second half. Finally, 75% of the FIRST bucket's net is made in 00-07 CT overnight hours, so the number is also more slippage-sensitive than the book average.

---

## Lens: robustness — REFUTED (high confidence)

**The first-break edge does not survive perturbation: 73% of the +8,915 comes from 5 of 240 trades, the bootstrap 95% CI on per-trade P&L spans zero, the M7 confirmation holds at only one split date out of nine, and the identical rank rule inverts sign on non-session levels — so "first is good, later is bad" is noise-sorting, not a mechanism.**

### Numbers

BASELINE (exact reproduction of 240/36 requires ranking over ALL REV+hist3 trades using ALL zone codes; the literal recipe restricted to session codes gives 231 first / 45 later, +10,256 / -4,458). M6 FIRST n=240 net +8,915, +37.15/trade, win 37.9%, PF 1.28. LATER n=36 net -3,117. M7 FIRST n=42 net +341, +8.11/trade.

(1) HALF-SPLIT +/-2,4,6,8 WEEKS. M6 survives all 9 splits (H1/H2 nets: +4,204/+4,711; +4,613/+4,302; +5,494/+3,421; +5,986/+2,929; +6,755/+2,160; +4,693/+4,222; +5,263/+3,652; +4,616/+4,299; +4,032/+4,883). M7 FAILS 8 of 9 — H1 net by split: -438, -438, -270, -37, +141 (the one used), -10, -85, -148, -211. 4-way time split of M6: seg2 (2026-01-13..2026-04-06) = -105, flat.

(2) LEAVE-ONE-OUT. Top 5 trades = +6,509 = 73% of net. Drop top 1/3/5 DAYS: +7,096 / +4,288 / +1,920 (20% / 52% / 78% of net removed). Top 1/3/5 WEEKS: +7,318 / +4,371 / +2,537. Top 1/3/5 MONTHS: +6,667 / +3,629 / +1,461 (84% removed). Drop top 10 trades (4% of sample): net -1,731, PF 0.95, and H2 = -7,371. Median trade -123.20. Dropping the 5 WORST days instead raises net to +12,231.

(3) BOOTSTRAP, 40,000 draws, per-trade net USD (2 contracts): mean +37.15, 95% CI [-10.36, +86.87], 90% CI [-3.23, +78.29], P(mean<=0) = 6.5%, P(mean<=7.20) = 11.3%. Lower bound is NOT above zero and NOT above cost. Day-block bootstrap [-10.57, +86.47]; week-block [+0.34, +72.98] (narrower only because winners are tied to same-week losers). H2 alone: +16.24/trade, 95% CI [-57.04, +93.56], P(<=0) = 34.4%, top 3 trades = 207% of H2's net. FIRST-minus-LATER difference: +123.73, 95% CI [+26.28, +214.57], P(diff<=0) = 0.007 (the only part that is statistically solid).

(4) RULE PERTURBATION. Ranks 0-1: n=270, +6,423, +23.79/trade (both halves +, but edge per trade cut 36%). Grouping per calendar day / 17:00 CT session day / per window: +8,915 / +8,854 / +8,259, all both-halves +. Single-code zones only: n=57, +1,445, H1 +1,700 / H2 -256 FAILS. Multi-code only: n=183, +7,470, passes. Excluding NL: n=219, +4,574, H1 +5,635 / H2 -1,061 FAILS. NL alone = 21 trades (8.75%) carrying +4,341 (49% of net), +206.70/trade. Per code both-halves test: AL and NL pass; AH (-202), LH (-121), LL and NH FAIL; AH and LH net negative.

SPECIFICITY (decisive). Same rank rule, REV+hist3, NON-session codes: rank 0 = -10,887 (n=291) while later = +1,899 (n=54) — ordering inverted. All codes pooled: rank 0 = -1,972 (n=531). Session codes with hist==15: rank 0 = -7,533 (n=414); hist==6: -5,784 (n=153); any hist: -1,409 (n=713). Equity path: max peak-to-trough drawdown 3,035 USD (0.34x final net), longest losing streak 10 trades. Commission in export is 3.20/trade; +12 USD/trade extra slippage leaves +6,035, +20 leaves +4,115.

### What would change the verdict

What survives is the FIRST-vs-LATER contrast, not first-break profitability: the difference in per-trade P&L is +123.73 with a 95% CI of [+26.28, +214.57]. But that contrast is driven mostly by how bad the 36 later trades are (-86.59/trade), and the same contrast reverses on non-session levels, so it is likely that 36 is just a small bad-luck bucket. I could not test out-of-sample in the true sense: M7 is a different strategy config over the same 365 days, not a later period, so there is no genuinely unseen data here. I would change my verdict if a forward sample of roughly 150+ new first-break trades (another 6-9 months) came in at a per-trade net whose own bootstrap lower bound cleared the cost, AND if the edge appeared across at least four of the six session codes rather than concentrating in NL, AND if net stayed positive after removing the top 5 trades. If the NL concentration is real rather than tail luck, the right claim is a much narrower one about New York session lows, tested on its own data — not a six-code session rule.

---

## Lens: tradeability — REFUTED (high confidence)

**The first-break session rule does not survive contact with a real run: nearly six in ten of its winning trades sit outside the New York window the strategy now trades, 57 percent of its winners had already run further against the entry than the current stop allows, and the version that actually exists under today's settings is 42 trades a year worth +341 dollars with a drawdown bigger than the profit and a losing-side sample of two trades.**

### Numbers

REPRODUCTION. Loading both exports and ranking reversal trades whose history tag reads "broke" at a session level by calendar day and level code, I get M6 231 first / 45 later (first: win 39.0%, PF 1.33, +10,256, +44.40 a trade, H1 +6,653 / H2 +3,603; later: 45 trades, PF 0.39, -4,458). Using a trading-day boundary instead gives 228 / 48 and PF 1.28, which matches the primary's quoted PF, so the 240/36 split is a day-boundary variant of the same 276-trade universe. M7 reproduces exactly: 42 first-break trades, PF 1.19, +341, H1 +141 / H2 +200; 2 later-break trades, -121. Direction of the claim holds in every variant I tried, so the arithmetic is not the problem.

1. FREQUENCY, STREAK, DRAWDOWN. Under the live (M7) settings the rule admits 42 trades in 358 days on 41 of 205 trading days, one signal every five trading days. Net +341 dollars on 2 contracts for a year, +8.11 a trade, +2.83 points a contract. Longest losing streak 7 trades (30 Mar to 29 May 2026). Maximum closed-trade drawdown 495 dollars, which is 1.45 times the whole year's profit. 8 of 12 months losing; quarters -342, +410, -227, +500. Per-trade spread 131.5 dollars, t = 0.40, 95 percent range for the year -1,329 to +2,010. Drawing 42 reversals at random from M7's 248 reversals beats +341 in 23.7 percent of 20,000 draws, so the rule is not distinguishable from picking at random. On the big M6 sample the sequence is better behaved (max closed drawdown 2,464, longest streak 9, 2 losing months of 13) but see point 2.

2. DOES IT EXIST UNDER THE CURRENT SETTINGS. No, mostly not. Of the 231 M6 first-break trades only 95 are in the New York window; 136 (59%) are Asia, London or other hours, which the current window excludes outright. Restricting to New York collapses it: PF 1.33 to 1.06, +10,256 to +891, and the halves disagree (+3,414 then -2,523), so it fails the project's both-halves rule in the window it would actually run in. Adding the four-trade and two-loss daily caps barely moves that (94 trades, +1,008, same half disagreement). Geometry is not comparable: M6 first-break trades average -53.6 points a loss and +114.4 a win with median adverse excursion 38.8 points, against M7's -15.2, +39.0 and 15.1. The current stop (rejection wick capped at 0.03 daily ATR, about 19.5 points) would have stopped out 51 of the 90 M6 winners (57%), holding +26,179 of the +40,910 won; a crude restatement of all 231 trades under a 19.5-point stop takes +10,256 to +117. The edge is the old wide stop, not the level logic.

3. SELECTION ON THE STRATEGY'S OWN OUTPUT. The rule only filters what was offered: about 42 admitted signals a year now. Its marginal value over the simpler "reversal where the history tag reads broke, at a session level" is +121 dollars a year, which is exactly the two later-break trades it removes. And "reversal where the tag reads broke, at any level at all" already gives 56 trades at +340 - the session-level and first-versus-later parts of the claim add nothing on top. The profitable half also leans on a handful of trades: in M6 the top five winners are +6,509 of the +10,256, and removing the best ten trades leaves -390.

4. VERDICT. Not strong enough to act on. At best strong enough to keep as a tag to watch, with the understanding that the losing side of the claim currently rests on two trades.

### What would change the verdict

What would change the verdict: a fresh year of data (or a second instrument) in which the New-York-only, wick-stop configuration produces 100 or more first-break session trades that are positive in both halves - the current live sample is 42 trades with a two-trade control group, which cannot support the claim either way. What I could not test: I cannot re-run TradingView here, so the stop-geometry transplant is an arithmetic restatement using each trade's recorded worst adverse move, not a real backtest; a trade stopped at 19.5 points might on some days have re-entered, and the breakeven-stop lever noted in the log for M7 was not combined with this filter. I also could not reproduce the primary's exact 240/36 split - the day-boundary choice alone moves the first-break net by about 1,600 dollars on the same 276 trades, which is itself a sign of how little the split is anchored.

---
