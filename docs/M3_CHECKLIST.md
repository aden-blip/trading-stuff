# M3 checklist: setups, score, signals

Same install as before. Use the **5-minute** chart for signals (D-21); the 1-minute trigger mode
comes in M6. The info box must read `L2L M3 v0.7`. Verdict distances are 0.05 and 0.05.

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

## Report back

- A 5-minute MNQ screenshot with a few signals visible, and one with a label tooltip open.
- Any signal that reads wrong, with the level name and time.
- How many signals per day it produces at the default minimum score of 60.
