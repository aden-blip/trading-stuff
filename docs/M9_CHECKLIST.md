# M9 checklist: the source method on its own

**What this is.** A third script, `pine/l2l_m9.pine`, beside M7 (the frozen baseline) and M8 (the
trade in his shape). Nothing of the owner's is in it; everything of the source's that can be written
in Pine is. See D-118 for what went in and D-116 and D-117 for what came out.

**This is its own script.** Paste it into a NEW tab in the Pine editor. The title differs from M7
and M8, so TradingView keeps all three apart and M9 arrives with fresh settings — nothing to reset.
The info box must read `L2L M9 v0.1` and the tester tab `L2L M9 - Strategy`.

**Copy page with a working copy button:** see `reference/handoff_links.md`.

**Tester setup, unchanged:** Deep Backtesting, "Last 365 days DEEP", capital 500,000, 5-minute MNQ,
Central time. Nothing to set in Properties.

## Checks

1. **It compiles.** This is 319 changed lines over M8 and Pine cannot be compiled here, so expect
   this to be the step that fails. Send the **first** red error line exactly as TradingView prints
   it — the rest are usually knock-ons from it.
2. **The settings arrived as intended.** 4-hour "Prev H/L" ticked; Daily "Open" and "Midnight open"
   ticked; Quarterly "Open" ticked; Sessions all three H/L **unticked**; Monday range unticked;
   "Find supply and demand zones" ticked; "The VIX must move against the trade and big tech with
   it" ticked; "Volume must follow suit" ticked; New York window reads `0800-1600`; opening
   blackout unticked.
3. **The info box has three new rows.** "S&D zones" (how many are live), "VIX / big tech" (which way
   the VIX is going and how many names are up or down, or "abstaining"), and "Volume side" (which
   side leads, by how much, how long since the last flip, and the velocity). If any of the three
   reads blank or zero all day, that module is not getting data and the run means nothing.
4. **The trade count.** Four new conditions in front of every trade, so expect far fewer than M8's
   401. Anywhere from about 60 to 400 is unremarkable. **Under about 30 means a gate is stuck
   shut** — most likely the big tech basket; send me the "VIX / big tech" row and I will loosen the
   count. Over 900 means a gate is not firing at all.
5. **Supply and demand zones are appearing.** The "S&D zones" row should sit between 2 and 10 live
   most of the day, and `DEM` and `SUP` should appear in the exported trade list. Zero all year
   means the impulse size is set too high for MNQ and needs lowering.
6. **Send the numbers:** total trades, net profit, profit factor, percent profitable, max drawdown,
   and the grey settings line.
7. **Export the list of trades and send the file.** Saved under `reference/backtests/<date>/`. The
   export now carries a `c0` to `c3` field on every trade — how many of the three confluences agreed
   — and that is what prices each of them separately without another run.

## What it is being judged against

| | Trades | PF | Net |
|---|---|---|---|
| M7, best version (D-102 gate) | 240 | 1.12 | +$1,279 |
| M8 v0.1, session 22 | 401 | 0.878 | −$2,183 |
| M9 v0.1 | — | — | — |

Within about $1,500 of M8 means the four new modules did nothing, which is itself an answer.

## What this still is not

No order book (Pine has no Level 2 data), no news calendar, and no 1-hour entries. Those three are
his and cannot be written here. A run of M9 is his method minus those three.
