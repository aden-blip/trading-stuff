# M2 checklist: untagged levels, verdicts, statistics

Same install as M1 (`docs/M1_CHECKLIST.md`): copy the raw file from GitHub or the chat paste, replace
the script in the Pine Editor, confirm the END OF FILE line is present, save, add to chart. The info
box must read `L2L M2 v0.2`.

## Checks

1. **Compiles and draws.** Everything from M1 still shows. New: cyan "S/R (n)" lines, verdict marks
   on the candles ("PDH held", "P4L broke", "AO neutral"), a statistics table bottom right.
2. **SR lines land where you would draw them.** On the MNQ 5-minute chart, compare the S/R lines with
   the untagged lines you would draw on the 4-hour. Too many: raise "Touches needed" or lower the
   "SR tolerance". Too few or missing an obvious one: lower touches to 2, raise the tolerance, or
   set the pivot bars to 2 and 2 for cleaner swings. Tell me which inputs you changed and why.
3. **Ten verdicts by eye.** Pick ten marks. For each: did price come from the side the mark implies
   (held above a level means it was tested from above and bounced), did a "held" close the hold
   distance away, did a "broke" close through by the break distance? Report any that read wrong.
4. **Counts change only on bar close.** Watch a live bar near a level: the table and the
   "Interactions" row in the info box must not change until the candle closes. On a 1-minute chart
   held and broke marks land on 5-minute closes only; neutral marks can land on any bar.
5. **Totals agree.** The info box "Interactions ... counted" equals the table's Total N.
6. **Replay.** Bar replay from a day ago: the same S/R lines, the same marks, the same counts up to
   that point. Nothing should appear or vanish as replay steps forward, apart from new verdicts.
7. **Other symbols.** CL and SIL: sensible S/R lines, no errors, table fills.
8. **Priors.** Type `PDH:0.62:40` into "Priors" and confirm the PDH row's rank moves up. The
   hold % column stays raw; only the rank uses priors.

## Report back

- A screenshot of the 5-minute MNQ chart with the table visible.
- Which SR inputs you changed, if any.
- Any verdict that read wrong, with the level name and the time.
