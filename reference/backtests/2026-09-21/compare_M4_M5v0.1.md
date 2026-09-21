# Two runs, trade by trade

Base: reference/backtests/2026-09-21/trades_M4v0.5_defaults_deep-365d_500k.csv
New: reference/backtests/2026-09-21/trades_M5v0.1_stages_deep-365d_500k.csv

- base 2963 trades, new 3926; matched 2671; only in new 1255; only in base 292
- matched, as the base did: 2671 trades, win 27 %, PF 0.83, net -52,188, -19.5 a trade
- matched, as the new did: 2671 trades, win 19 %, PF 0.81, net -41,836, -15.7 a trade
- only in new (extra): 1255 trades, win 17 %, PF 0.78, net -23,807, -19.0 a trade
- only in base (dropped): 292 trades, win 26 %, PF 0.84, net -5,606, -19.2 a trade

### Matched trades: base exit against new exit

| Base exit | New exit | Trades | Base net | New net | Change |
|---|---|---|---|---|---|
| stop | be | 445 | -62,321 | -2,214 | +60,107 |
| T1 | be | 126 | 51,818 | -611 | -52,429 |
| stop | half | 412 | -82,315 | -42,868 | +39,447 |
| T1 | half | 52 | 21,975 | -5,517 | -27,492 |
| flat | be | 40 | 6,174 | -170 | -6,344 |
| flat | half | 18 | 420 | -2,517 | -2,937 |
| stop | stop | 1075 | -168,407 | -168,407 | +0 |
| T1 | T1 | 443 | 164,081 | 164,081 | +0 |
| flat | flat | 60 | 16,387 | 16,387 | +0 |

### Matched trades by the new exit

| New exit | Trades | Base net (same entries) | New net | Change |
|---|---|---|---|---|
| T1 | 443 | 164,081 | 164,081 | +0 |
| stop | 1075 | -168,407 | -168,407 | +0 |
| half | 482 | -59,920 | -50,902 | +9,018 |
| be | 611 | -4,329 | -2,995 | +1,334 |
| flat | 60 | 16,387 | 16,387 | +0 |

### Extra trades by exit

- T1: 190 trades, net 76,488
- stop: 453 trades, net -78,491
- half: 256 trades, net -27,062
- be: 321 trades, net -1,718
- flat: 35 trades, net 6,976

### By month

| Month | Base trades | Base net | New trades | New net |
|---|---|---|---|---|
| 2025-09 | 165 | -1,687 | 192 | -1,882 |
| 2025-10 | 339 | -818 | 397 | -1,396 |
| 2025-11 | 224 | 335 | 278 | -3,052 |
| 2025-12 | 200 | -8,413 | 270 | -3,757 |
| 2026-01 | 259 | 1,758 | 324 | -844 |
| 2026-02 | 238 | -11,995 | 313 | -7,405 |
| 2026-03 | 286 | -10,075 | 396 | -14,572 |
| 2026-04 | 177 | -1,283 | 257 | -4,516 |
| 2026-05 | 227 | 2,251 | 314 | -1,925 |
| 2026-06 | 265 | -5,393 | 374 | -2,822 |
| 2026-07 | 268 | -18,304 | 350 | -12,049 |
| 2026-08 | 184 | -2,864 | 286 | -10,748 |
| 2026-09 | 131 | -1,307 | 175 | -675 |
