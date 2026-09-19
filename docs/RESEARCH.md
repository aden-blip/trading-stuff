# Research Notes

Facts gathered for the plan, with sources. Dated 2026-09-19. Numbers change; re-check before going live.

---

## 1. TradingView plan mapping

- Premium is $59.95 per month billed annually or $69.95 month to month after the April 2026 increase.
  Real-time CME data is a separate add-on at about $9.95 per month; US stock exchanges are extra.
  A bill near $100 per month is Premium month to month plus data add-ons.
- Premium gives 20k historical bars per chart, Bar Magnifier, Deep Backtesting, 400 alerts, and webhooks.
- Essential and Plus have **no webhook notifications**, so Premium is the minimum for any bot.
- Ultimate is $199.95 per month with 40k bars and 64 data requests per script instead of 40.
- Confirmed 2026-09-19: Premium with the US stocks bundle and CME Group real-time data.
- The CME Group real-time package is one $9.95 bundle covering CME, CBOT, COMEX and NYMEX. NQ is
  on CME, CL on NYMEX, SI on COMEX. If a CL or SI chart shows a delayed-data badge, the bundle is
  not what is active and the bot cannot trade those live.

Sources: [TradingView pricing](https://www.tradingview.com/pricing/),
[April 2026 price change](https://chartinglens.com/blog/tradingview-price-increase-2026),
[real-time data add-ons](https://optimusfutures.com/blog/tradingview-real-time-data/),
[historical bars by plan](https://www.tradingview.com/support/solutions/43000480679-historical-intraday-data-bars-and-limits-explained/),
[Bar Magnifier](https://www.tradingview.com/support/solutions/43000669285/).

## 2. Tradovate commissions

Per side, per contract, before exchange, clearing and NFA fees:

| Plan | Price | Standard (NQ, CL, SI) | Micro (MNQ, MCL, SIL) |
|---|---|---|---|
| Free | $0 | $1.29 | $0.39 |
| Monthly | $99 per month | $0.99 | $0.29 |
| Lifetime | $1,499 once | $0.59 | $0.09 |

Exchange, clearing and NFA fees are added on every trade on every plan. Clearing and routing add
about $0.19 to $0.25 per contract, NFA is $0.02 per side, and exchange fees run from about $0.35
per side on index micros to $1.60 or more per side on some standard contracts. Metals exchange fees
rose $0.05 to $0.10 per side on July 20, 2026.

The Tradovate all-in rate page blocked automated fetches, so use one of your own fills to confirm.
Tradovate's fee schedule is at
[All-in rates and trading fees](https://support.tradovate.com/s/article/Tradovate-Understanding-All-In-Rates-and-Trading-Fees?language=en_US).

**Prop-firm reference point.** TopstepX publishes all-in round-turn costs, which are a good proxy
for "commission plus every fee":

| Contract | Round turn | Per side |
|---|---|---|
| NQ | $3.78 | $1.89 |
| MNQ | $1.22 | $0.61 |
| ES | $3.78 | $1.89 |
| MES | $1.22 | $0.61 |
| CL | $4.02 | $2.01 |
| MCL | $1.52 | $0.76 |
| SI | $4.32 | $2.16 |
| SIL | $2.72 | $1.36 |

Source: [TopstepX commissions and fees](https://help.topstep.com/en/articles/8284213-what-are-the-commissions-and-fees-in-the-trading-combine-and-express-funded-account).

**Backtest defaults (per side, entered in the strategy Properties).** Tradovate Free plan estimates,
rounded up:

| Contract | Commission per side | Slippage per side |
|---|---|---|
| MNQ | $0.80 | 2 ticks |
| NQ | $2.85 | 2 ticks |
| MCL | $0.95 | 1 tick |
| CL | $3.00 | 1 tick |
| SIL | $1.60 | 2 ticks |
| SI | $3.15 | 2 ticks |

Sources: [Tradovate pricing](https://www.tradovate.com/pricing/),
[futures commissions explained](https://damnpropfirms.com/trading-guides/futures-commissions-explained-what-you-actually-pay/),
[Tradovate fees explained](https://damnpropfirms.com/trading-guides/tradovate-fees-explained-commissions-data-plans/).

## 3. Tradovate slippage and "slow data"

What the published tests say. Note that the only slippage studies found are from PickMyTrade, a
bridge vendor, with light methodology (about 1,000 live market orders on ES, NQ and CL during peak
hours, VPS hosted).

- Tradovate: about 1.2 ticks average slippage on market orders; 1.2 to 3 ticks on NQ; Reddit reports of 4 to 8 ticks on news days.
- Rithmic-connected brokers: about 0.7 ticks average.
- ProjectX / TopstepX: about 2.1 ticks average, occasional lag at peaks.
- Across brokers: 3 to 5 ticks during news events; limit orders got price improvement 30 to 40 % of the time.
- Latency: Tradovate measured around 53 ms from a Central American test point, comparable to or better than Rithmic from there.
- Why it feels slow: Tradovate runs on Google Cloud and **aggregates or throttles market data during
  extreme volatility** (CPI, FOMC) to keep the browser responsive, which shows up as chart delay and
  order-confirmation lag. Bracket orders are held server side, so a resting stop is not affected by your screen lagging.

What this means for the strategy:

- Entries are market orders at bar close, stops are stop-market orders, soft-target exits are market
  orders. Expect 1 to 2 ticks on each in normal conditions on NQ, so 2 to 4 ticks per round trip.
  On MNQ that is $1 to $2 per contract; on NQ $10 to $20.
- The chart and alerts run on TradingView's CME feed, not Tradovate's. The order fills on Tradovate.
  A small difference between the alert price and the fill is normal.
- Set slippage to 2 ticks per side for NQ/MNQ backtests, 1 tick for CL/MCL, 2 ticks for SI/SIL.
- Add a news blackout so the bot does not enter into the 4 to 8 tick windows.
- Limit entries at the level (REV limit mode, sweep-retest mode, flip) have no slippage but can miss the fill.
- If slippage on Tradovate ever becomes the deciding factor, a Rithmic-connected account through the same bridge is the documented step down in slippage.

Sources: [1,000 trade slippage data 2026](https://blog.pickmytrade.io/real-slippage-data-1000-trades-futures-brokers-2026/),
[Rithmic vs Tradovate vs ProjectX slippage test 2025](https://blog.pickmytrade.trade/futures-slippage-test-rithmic-tradovate-projectx-2025/),
[Rithmic vs Tradovate latency deep dive](https://traderfuel.net/trading-tech/rithmic-vs-tradovate/),
[Rithmic vs Tradovate comparison](https://www.quantvps.com/blog/rithmic-vs-tradovate).

## 4. Bridges and prop-firm automation rules

**What a bridge is.** TradingView cannot send an order to Tradovate. A strategy can only fire an
alert, which is a text message sent to a web address. A bridge is a paid service that owns that
address: it reads the message and places the order in your Tradovate account, moves the stop when
a later message says so, and closes the position when told to. Without a bridge the strategy is a
signal service you execute by hand. TradingView's built-in Tradovate panel is for manual trading only.

**PickMyTrade.** $50 per month, $135 per quarter or $500 per year, unlimited alerts and accounts,
7-day free trial with no card, and it works against Tradovate demo accounts, so nothing is paid
until you go live. Connects TradingView alerts to Tradovate, Rithmic, ProjectX and TopstepX accounts,
and to prop firms including Apex, Topstep and MyFundedFutures. Average execution under 200 ms.
Its alert JSON supports: `symbol`, `data` (buy / sell / close), `quantity`, `price` for limit
orders, `sl`, `tp`, `update_sl` and `update_tp` to modify an open position's stop or target,
`breakeven`, `trail`, `trail_trigger`, `reverse_order_close` (close the opposite position before
entering), `pyramid`, `account_id`, and multi-account copying with a quantity multiplier.
That covers every event the trade manager emits.

**TradersPost.** Also supports Tradovate, plus stocks, options and crypto. Alternative if PickMyTrade does not suit.

**Prop firms.** Apex, Topstep, TradeDay and MyFundedFutures allow automated or semi-automated
trading with restrictions: no high-frequency trading, no co-location or latency arbitrage, use a
supported platform. Apex's current rules permit supervised alert-driven automation and ban
unattended 24/7 bots and rented commercial EAs. Rules change; confirm with the firm in writing before running live.

Sources: [PickMyTrade pricing](https://pickmytrade.trade/pages/pricing/),
[PickMyTrade Tradovate demo](https://docs.pickmytrade.trade/docs/tradovate-demo-account/),
[PickMyTrade JSON alert fields](https://docs.pickmytrade.trade/docs/tradingview-json-alert-configuration/),
[PickMyTrade supported prop firms](https://pickmytrade.trade/en/supported-propfirms/),
[PickMyTrade webhook FAQ](https://pickmytrade.io/faq/tradingview-webhooks/),
[TradersPost TradingView docs](https://docs.traderspost.io/docs/learn/signal-sources/tradingview),
[prop firms that allow automated trading](https://propfirmpinescripts.com/guides/prop-firms-that-allow-automated-trading.html).

## 5. Source strategy references

**Socrates Investments.** Futures-only, NQ and gold among others, daily live streams. The public
description uses supply and demand, pivots and daily levels, with stop-loss and position-sizing
discipline. YouTube: [@Socrates_Investments](https://www.youtube.com/@Socrates_Investments).
Site: [socratesinvestments.com](https://socratesinvestments.com/).

The six videos you pointed at are listed in `reference/links.md`. Their titles: scalping the
Nasdaq using the VIX for entries; how he sees pivots for entries and exits; charting pivots on the
4-hour; a live trading recap; a breakdown of the key-level pivot system; and charting the
methodology for entry and exit points. Transcripts are blocked from this environment, so the
rules below come from the site and the third-party write-up; the videos can correct them once you
paste a transcript.

A third-party NinjaTrader implementation of the method
([repository](https://github.com/izacturner95-sketch/Anthropic-claude-code-ninjatrader-SOCRATES))
spells out rules that line up with this plan:

- A book of reference levels: prior daily and weekly pivots, swing highs and lows, order blocks from displacement candles.
- Liquidity sweep: price moves beyond a level and then reclaims it.
- Confirmation: a market structure shift with displacement.
- Entry on the **retest**, never on the sweep itself.
- Gates: VIX moving inversely to the trade, and the Magnificent 7 participating in the same direction. Both optional.
- Stop below the previous low, target at the previous high, with a maximum risk in ATR.
- Sessions: regular hours 08:45 to 14:45 CT, or the full Globex session flat by 15:55 CT.

Our plan keeps the level book, the VIX and Mag 7 gates for NQ, and structure-based stops and
targets. The sweep-reclaim-retest entry is added as an optional REV trigger in M7.

**SpacemanBTC "Key Levels IDWM".** The indicator you called "spaceman". It plots previous day high,
low and 50 % level plus the day open, the same for the week and the month, and a custom-timeframe
version. Our level list is a superset of it.
Sources: [Key Levels IDWM](https://www.tradingview.com/script/PV6TowBV-Key-Levels-SpacemanBTC-IDWM/),
[Key Levels custom timeframe with backtest](https://www.tradingview.com/script/QtlWjD43-Key-Levels-CustomTF-Backtest-SpacemanBTC/).

**ICT terms you mentioned.** A fair value gap is the three-candle imbalance between candle one's
high and candle three's low (bullish) or the mirror. Consequent encroachment is the 50 % line of
that gap. Both are parked as a possible later level type (section 11 of the plan).

**LuxAlgo.** Helped produce the earlier script; the target ladder and ATR normalization ideas in the
plan come from that conversation.

## 6. Your own rules document (Google Drive, May 2026)

Found while looking for TradeZella data: "Rebel Trades Trading Rules and Goals". Only the
strategy-relevant lines are recorded here.

- NQ, MNQ and NAS100 only at that time; no Asia session trading.
- Size tiers: 2, 3 or 5 contracts, all with a 50-tick stop; max 5 contracts.
- Daily loss limit $800.
- 08:30 to 09:00 CT: TradeZella showed under a 20 % win rate with most stops hit within 2 minutes,
  so that window was limited to one 1-contract trade with a 100-tick stop.
- A quarter of all trades ran into profit and still closed as losers.
- Lock out after the session ends.

How the plan uses it: opening blackout (D-43), daily loss limit in dollars (D-44), optional stop
cap in ticks (D-45), optional size-by-score tiers (D-46), staged stops to address the
profit-then-loss pattern, and the index profile defaulting to the New York session only.

The claim that CL and SIL trade best at the 19:00 CT Asia open could not be confirmed. Two
searches on 2026-09-19 covered Drive, Dropbox, Gmail attachments, Wispr notes, Claude artifacts and
docs, and the Claude Code session list. The only trade log found, "Copy of Daryl's Trades" in Drive,
is another trader's journal template, not your data. The chat where the trades were uploaded is a
claude.ai conversation, which is not readable from a Claude Code session. D-47 is closed: you decided
the journal predates this strategy and would only show personal tendencies.
