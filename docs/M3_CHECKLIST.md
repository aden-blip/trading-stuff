# M3 checklist: setups, score, signals

Same install as before. Use the **5-minute** chart for signals (D-21); the 1-minute trigger mode
comes in M6. The info box must read `L2L M3 v0.14`. Verdict distances are 0.05 and 0.05.

## Checks

1. **Compiles.** Everything from M2 still shows. New: signal tags under or over candles, an arrow
   and a score out of 10 such as `▲ 6/10`. Green and red are reversal trades, blue and orange are break
   trades. Hover one for the setup, the level, entry, stop, targets and the score breakdown.
2. **Signals sit where you would take reversal trades.** On MNQ 5-minute, scroll back a few days.
   A REV long should follow a wick, a poke-and-close-back or an engulfing candle at a level,
   then one bar closing the same way. Report any signal that makes no sense, with the time.
3. **Break trades read right.** A BRK label appears on the retest bar, not on the breakout bar,
   with the entry at the broken edge and the stop back inside the zone.
4. **Scores read right.** Hover a label: the tooltip shows Reliability, Stack, History, HTF (0),
   Bias (7) and Hooks (0). A fresh, top-ranked, single level should read about 6/10, with
   "64 of 100" beside it.
5. **One signal per bar, none repeating on the same test.** Two labels on consecutive bars at the
   same level means a bug; tell me.
6. **Alerts.** Create one alert on the indicator, condition "Any alert() function call", and let it
   run for a session. Each signal should produce exactly one alert with a JSON message.
7. **Hooks.** Turn on "Show VWAP and EMA lines" once to confirm they draw, then turn it off.
8. **Replay.** Bar replay: labels appear on the bar after the follow-through closes and never
   move or vanish.
9. **CL and SIL.** Signals appear at levels, no errors, volume confirmation off automatically.
10. **Explanations.** Settings, Signals, set "Explain missed signals" to "Rule rejections". Grey
    `?` tags appear on some candles; hover one and the box says which trade nearly happened and
    the rule that stopped it. Set it back to Off when you are done reviewing.
11. **My pivots.** Settings, My pivots, type `29895.5` into Pivot 1. A pink line appears with the
    tag Pivot 1, the info box row My pivots reads 1 of 10, and after its first test the
    statistics table gets a PIV row.
12. **One trade at a time.** With the default on, arrows never overlap in time: after an arrow,
    the next arrow comes only after a small teal or maroon exit tag (T1, stop or flat with the
    points). The info box shows Paper trades and Paper points. Turn the switch off and every
    setup shows again, as in v0.10.
13. **Paper breakdown.** With the paper trade on, a second table (middle right by default) lists
    the paper trades by score, by REV or BRK and by session window, with the share that reached
    T1, the average gain, the average loss and the net points. Its header shows the date of the
    first trade and the trading days covered. The All row must match the info box rows.
14. **Entry and stop switches.** Settings, Reversal setup. Set Reversal entry to "Limit at the
    level after the follow-through": REV arrows now sit on the candle that comes back to the
    level, and the hover box shows E at the level's price. Set Reversal stop to "Beyond the
    rejection wick": SL in the hover box moves to just beyond the rejection candle's wick. Put
    both back to the first option when done.

## Report back

- A 5-minute MNQ screenshot with a few signals visible, and one with a label tooltip open.
- Any signal that reads wrong, with the level name and time.
- How many signals per day it produces at the review minimum score of 50, and how many of
  those read 7/10 or better.
- A screenshot of the paper breakdown table with the defaults, and one with the range filter
  switched on.
- Four breakdown screenshots for D-83: defaults; Reversal entry "Limit at the level after the
  follow-through"; Reversal entry "Limit at the level after the rejection candle"; and, back on
  the default entry, Reversal stop "Beyond the rejection wick".
