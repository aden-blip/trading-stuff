# M1 checklist: Level Engine

What to do with `pine/l2l.pine` and what to report back. Stop at the first failure and send it.

## Install

1. TradingView, open an **MNQ1! 5-minute** chart.
2. Pine Editor at the bottom, "Open", "New indicator", select all, delete, paste the file, "Save", "Add to chart".
3. If it does not compile: send the **first** red error line with its line number. Nothing else is needed.

## Checks

1. **Info box, top right.** Profile shows `Index (futures)`, Timezone `America/Chicago`, a daily ATR
   number that looks like a normal day's range, cluster and touch tolerances in ticks.
2. **Levels against your own lines.** Check at least these five by hand and say which are off:
   - PDH / PDL: yesterday's session high and low, where the session ran 17:00 to 16:00 Central.
   - DO: the 17:00 Central open. MO: the open of the 23:00 Central candle.
   - P4H / P4L: the high and low of the last **completed** 4-hour candle on the chart.
   - MNH / MNL: this week's Monday session high and low.
   - AH / AL, LH / LL, NH / NL: the last completed Asia, London and New York session.
   Only levels within one daily ATR of price are drawn; widen "Draw levels within" to see more.
3. **Same on 1-minute.** Switch the chart to 1-minute at the same moment. Every code and price in
   the labels should match the 5-minute chart. Report any that differ.
4. **Replay.** Turn on "Plot level history", open bar replay, jump back a day or two. The step
   lines should show the levels as they were then, with no jumps mid-day except at their own rollover
   (daily levels change at 17:00 Central, 4-hour levels every 4 hours, session levels when a session closes).
5. **Clusters.** Find a spot where two levels sit close together. They should show as one box with
   the codes joined, for example `PDH+P4H`. If two levels that clearly should merge are drawn apart,
   or two far-apart levels are merged, say which and how far apart they are in ticks.
6. **Crude and silver.** Put it on CL1! and SI1! 5-minute. Profile should read Energy and Metals,
   the New York session should use 08:00 to 13:30 and 07:20 to 12:30 Central, and the levels should
   look sensible. Also try it on any stock or BTC to make sure it does not error.
7. **Custom levels.** Type `12345:TEST` plus one real price near the market into the custom levels
   box, for example `20150:GEX`. The real one should appear with its label; the far one is skipped
   because it is out of draw range.
8. **Clean chart.** Toggle families off and on. Nothing should remain drawn from a family that is off.

## Report back

- One screenshot of the MNQ 5-minute chart with the info box visible.
- The list from check 2 with anything that is off and what the correct price is.
- Anything from checks 3 to 8 that failed.

Keep the chart timeframe at 4 hours or below; the 4-hour request is meaningless above that.
