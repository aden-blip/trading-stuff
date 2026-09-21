# M4 checklist: the strategy in the tester

Same paste as before, but the script is now a strategy: when it is added to the chart,
TradingView opens the Strategy Tester panel at the bottom. Use the 5-minute MNQ chart. The info
box must read `L2L M4 v0.2`. Every filter is off by default: that is the base run.

## Checks

1. **Compiles and the tester runs.** The Strategy Tester panel shows Overview, Performance
   Summary and List of Trades with numbers in them. Arrows, exit marks and the tables draw as in
   M3.
2. **Costs.** Strategy settings, Properties tab: initial capital 50,000, commission 0.80 per
   contract, slippage 2 ticks. Those are the MNQ defaults from the research notes. For CL/MCL
   and SI/SIL change them there (0.95 with 1 tick, 1.60 with 2 ticks). Order size comes from the
   script's Contracts input (2), not from the Properties tab.
3. **Cross-check.** In the info box, the Tester rows against the Paper rows. Closed trades should
   match, give or take one or two. Tester net in points should sit below Paper points by about
   1.8 points per trade, which is the costs (0.80 per side and 2 ticks of slippage on each
   market or stop fill; a limit fill has no slippage, so trades that end at the target cost a
   little less).
4. **Entries fill at the next candle's open.** Hover a signal tag: "E next open, about ...". In
   the List of Trades the entry time is the candle after the tag.
5. **Flat every day.** In the List of Trades no trade stays open past 15:55 CT [16:55 NY]; the
   ones closed by the flatten carry the comment "flat".
6. **Deep Backtesting.** In the tester's header switch on Deep Backtesting (Premium), set the
   range as far back as the data goes, run. Screenshot the Overview and the Performance Summary,
   plus both chart tables. This is the run the decisions wait for.
7. **Filters one at a time.** Settings, Filters: turn on one switch, run, screenshot the
   Overview, turn it off. New York only, opening blackout, news blackout, chop band.
8. **Alerts.** One alert with "Any alert() function call", as before; the ENTRY and EXIT messages
   are unchanged.

## Report back

- Screenshots of the Overview and the Performance Summary for the base run, on the normal chart
  and under Deep Backtesting, with the two chart tables visible.
- The Tester rows and the Paper rows of the info box, so the cross-check is on record.
- Any trade in the List of Trades that looks wrong: an entry not on the candle after its tag, an
  exit price off its stop or target, a trade open past the flatten.
