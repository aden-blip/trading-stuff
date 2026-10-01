# Trade-list report

File: reference/backtests/2026-10-01/trades_M9v0.1_source-method_deep-365d_500k.csv
Trades: 502, 2025-10-01 08:30 to 2026-10-01 09:05, size 2, 4 USD per point, commission 3.20 a round trip.
Win 22.91 %, PF 0.81, net -4,094.40 USD, -8.16 USD a trade, -1.24 points a trade per contract.
Avg win 154.43 USD, avg loss 56.47 USD, closed-trade max drawdown 5,327.80 USD.
Median stop-out loss 14.5 points, mean 13.3.
Median T1 win 32.8 points, mean 39.5.
Hold: median 0 bars, mean 0.9; winners median 1, losers median 0.

### By exit reason

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| T1 | 114 | 100.0 | inf | 17,653 | 154.9 | 39.5 | 155 | 0 |
| stop | 311 | 0.0 | 0.00 | -19,718 | -63.4 | -15.1 | 0 | 63 |
| void | 76 | 0.0 | 0.00 | -2,135 | -28.1 | -6.2 | 0 | 28 |
| flat | 1 | 100.0 | inf | 106 | 105.8 | 27.2 | 106 | 0 |

### By setup

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| REV | 160 | 21.2 | 0.82 | -1,302 | -8.1 | -1.2 | 174 | 57 |
| BRK | 342 | 23.7 | 0.81 | -2,792 | -8.2 | -1.2 | 146 | 56 |

### By direction

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| long | 250 | 24.8 | 0.84 | -1,723 | -6.9 | -0.9 | 146 | 57 |
| short | 252 | 21.0 | 0.79 | -2,371 | -9.4 | -1.6 | 164 | 56 |

### By window (script's tag)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| NY | 502 | 22.9 | 0.81 | -4,094 | -8.2 | -1.2 | 154 | 56 |

### By setup and window

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| BRK NY | 342 | 23.7 | 0.81 | -2,792 | -8.2 | -1.2 | 146 | 56 |
| REV NY | 160 | 21.2 | 0.82 | -1,302 | -8.1 | -1.2 | 174 | 57 |

### By stack (levels in the zone)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| k1 | 399 | 21.8 | 0.79 | -3,650 | -9.1 | -1.5 | 157 | 55 |
| k2 | 89 | 28.1 | 0.89 | -412 | -4.6 | -0.4 | 140 | 61 |
| k3+ | 14 | 21.4 | 0.95 | -33 | -2.3 | 0.2 | 208 | 60 |

### By score

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| s100-109 | 3 | 33.3 | 1.09 | 13 | 4.5 | 1.9 | 167 | 77 |
| s20-29 | 83 | 25.3 | 0.78 | -799 | -9.6 | -1.6 | 132 | 58 |
| s30-39 | 70 | 30.0 | 1.05 | 128 | 1.8 | 1.3 | 141 | 58 |
| s40-49 | 95 | 17.9 | 0.52 | -2,204 | -23.2 | -5.0 | 142 | 59 |
| s50-59 | 72 | 23.6 | 0.84 | -488 | -6.8 | -0.9 | 150 | 55 |
| s60-69 | 35 | 17.1 | 0.54 | -800 | -22.9 | -4.9 | 154 | 59 |
| s70-79 | 110 | 20.0 | 0.88 | -544 | -4.9 | -0.4 | 185 | 52 |
| s80-89 | 15 | 26.7 | 2.17 | 692 | 46.1 | 12.3 | 320 | 54 |
| s90-99 | 19 | 31.6 | 0.87 | -93 | -4.9 | -0.4 | 101 | 54 |

### By level history

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| h12 first test | 227 | 22.9 | 0.76 | -2,467 | -10.9 | -1.9 | 146 | 58 |
| h15 held | 53 | 26.4 | 1.04 | 84 | 1.6 | 1.2 | 170 | 59 |
| h3 broke | 24 | 20.8 | 0.87 | -154 | -6.4 | -0.8 | 198 | 60 |
| h6 touched | 198 | 22.2 | 0.81 | -1,558 | -7.9 | -1.2 | 154 | 54 |

### By confluences that agreed (M9: VIX, big tech, volume side)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| c1 of 3 | 9 | 22.2 | 0.78 | -53 | -5.9 | -0.7 | 95 | 35 |
| c2 of 3 | 105 | 24.8 | 0.80 | -867 | -8.3 | -1.3 | 134 | 55 |
| c3 of 3 | 388 | 22.4 | 0.82 | -3,175 | -8.2 | -1.2 | 162 | 57 |

### By at least N confluences (cumulative)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| c>=0 | 502 | 22.9 | 0.81 | -4,094 | -8.2 | -1.2 | 154 | 56 |
| c>=1 | 502 | 22.9 | 0.81 | -4,094 | -8.2 | -1.2 | 154 | 56 |
| c>=2 | 493 | 22.9 | 0.81 | -4,042 | -8.2 | -1.2 | 155 | 57 |
| c>=3 | 388 | 22.4 | 0.82 | -3,175 | -8.2 | -1.2 | 162 | 57 |

### By higher-timeframe rejections (reversals, M6)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| f0 of 4 | 47 | 17.0 | 0.70 | -698 | -14.9 | -2.9 | 203 | 60 |
| f1 of 4 | 68 | 23.5 | 0.90 | -281 | -4.1 | -0.2 | 161 | 55 |
| f2 of 4 | 39 | 20.5 | 0.75 | -449 | -11.5 | -2.1 | 165 | 57 |
| f3 of 4 | 6 | 33.3 | 1.49 | 126 | 21.0 | 6.0 | 192 | 64 |

### By at least N higher-timeframe rejections (cumulative)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| f>=0 | 160 | 21.2 | 0.82 | -1,302 | -8.1 | -1.2 | 174 | 57 |
| f>=1 | 113 | 23.0 | 0.88 | -604 | -5.3 | -0.5 | 164 | 56 |
| f>=2 | 45 | 22.2 | 0.84 | -323 | -7.2 | -1.0 | 170 | 58 |
| f>=3 | 6 | 33.3 | 1.49 | 126 | 21.0 | 6.0 | 192 | 64 |

### By level history and setup

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| BRK h12 first test | 227 | 22.9 | 0.76 | -2,467 | -10.9 | -1.9 | 146 | 58 |
| BRK h6 touched | 115 | 25.2 | 0.93 | -325 | -2.8 | 0.1 | 147 | 53 |
| REV h15 held | 53 | 26.4 | 1.04 | 84 | 1.6 | 1.2 | 170 | 59 |
| REV h3 broke | 24 | 20.8 | 0.87 | -154 | -6.4 | -0.8 | 198 | 60 |
| REV h6 touched | 83 | 18.1 | 0.67 | -1,233 | -14.9 | -2.9 | 169 | 55 |

### By hour of entry (chart time)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| 08:00 | 187 | 23.0 | 0.85 | -1,234 | -6.6 | -0.9 | 163 | 57 |
| 09:00 | 136 | 22.1 | 0.80 | -1,293 | -9.5 | -1.6 | 173 | 61 |
| 10:00 | 58 | 31.0 | 1.04 | 89 | 1.5 | 1.2 | 129 | 56 |
| 11:00 | 32 | 21.9 | 0.77 | -308 | -9.6 | -1.6 | 146 | 53 |
| 12:00 | 24 | 16.7 | 0.48 | -533 | -22.2 | -4.8 | 122 | 51 |
| 13:00 | 26 | 26.9 | 1.04 | 37 | 1.4 | 1.2 | 144 | 51 |
| 14:00 | 33 | 15.2 | 0.49 | -647 | -19.6 | -4.1 | 124 | 45 |
| 15:00 | 5 | 20.0 | 0.43 | -141 | -28.2 | -6.2 | 106 | 62 |
| 17:00 | 1 | 0.0 | 0.00 | -64 | -64.2 | -15.2 | 0 | 64 |

### By weekday of entry

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| Mon | 94 | 26.6 | 1.01 | 21 | 0.2 | 0.9 | 140 | 50 |
| Tue | 95 | 22.1 | 0.93 | -284 | -3.0 | 0.1 | 189 | 57 |
| Wed | 114 | 25.4 | 0.76 | -1,193 | -10.5 | -1.8 | 132 | 59 |
| Thu | 108 | 21.3 | 0.86 | -698 | -6.5 | -0.8 | 185 | 58 |
| Fri | 91 | 18.7 | 0.53 | -1,941 | -21.3 | -4.5 | 130 | 56 |

### By month of entry

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| 2025-10 | 45 | 15.6 | 0.82 | -217 | -4.8 | -0.4 | 140 | 32 |
| 2025-11 | 43 | 27.9 | 1.11 | 172 | 4.0 | 1.8 | 150 | 53 |
| 2025-12 | 47 | 31.9 | 1.30 | 517 | 11.0 | 3.5 | 149 | 54 |
| 2026-01 | 45 | 24.4 | 0.74 | -379 | -8.4 | -1.3 | 97 | 43 |
| 2026-02 | 45 | 22.2 | 1.01 | 26 | 0.6 | 0.9 | 198 | 56 |
| 2026-03 | 51 | 25.5 | 1.06 | 142 | 2.8 | 1.5 | 191 | 62 |
| 2026-04 | 39 | 25.6 | 0.94 | -95 | -2.4 | 0.2 | 162 | 59 |
| 2026-05 | 32 | 15.6 | 0.42 | -932 | -29.1 | -6.5 | 132 | 59 |
| 2026-06 | 38 | 10.5 | 0.32 | -1,845 | -48.5 | -11.3 | 215 | 80 |
| 2026-07 | 41 | 24.4 | 0.70 | -705 | -17.2 | -3.5 | 163 | 75 |
| 2026-08 | 35 | 31.4 | 1.03 | 48 | 1.4 | 1.1 | 141 | 63 |
| 2026-09 | 40 | 17.5 | 0.53 | -766 | -19.2 | -4.0 | 125 | 50 |
| 2026-10 | 1 | 0.0 | 0.00 | -60 | -60.2 | -14.2 | 0 | 60 |

### By week of entry

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| 2025-W40 | 7 | 14.3 | 0.95 | -7 | -1.1 | 0.5 | 131 | 23 |
| 2025-W41 | 11 | 18.2 | 1.05 | 8 | 0.7 | 1.0 | 88 | 19 |
| 2025-W42 | 10 | 0.0 | 0.00 | -342 | -34.2 | -7.8 | 0 | 34 |
| 2025-W43 | 6 | 16.7 | 0.41 | -119 | -19.9 | -4.2 | 84 | 41 |
| 2025-W44 | 11 | 27.3 | 1.70 | 244 | 22.2 | 6.3 | 197 | 43 |
| 2025-W45 | 7 | 14.3 | 0.37 | -201 | -28.8 | -6.4 | 119 | 53 |
| 2025-W46 | 12 | 33.3 | 1.71 | 246 | 20.5 | 5.9 | 147 | 43 |
| 2025-W47 | 13 | 23.1 | 0.90 | -70 | -5.4 | -0.5 | 198 | 66 |
| 2025-W48 | 11 | 36.4 | 1.65 | 198 | 18.0 | 5.3 | 125 | 43 |
| 2025-W49 | 11 | 36.4 | 1.50 | 191 | 17.3 | 5.1 | 144 | 55 |
| 2025-W50 | 14 | 42.9 | 1.79 | 363 | 25.9 | 7.3 | 137 | 58 |
| 2025-W51 | 10 | 20.0 | 1.33 | 154 | 15.4 | 4.7 | 309 | 58 |
| 2025-W52 | 8 | 12.5 | 0.18 | -265 | -33.1 | -7.5 | 58 | 46 |
| 2026-W01 | 6 | 33.3 | 0.90 | -19 | -3.2 | 0.0 | 84 | 47 |
| 2026-W02 | 11 | 9.1 | 0.11 | -353 | -32.1 | -7.2 | 44 | 40 |
| 2026-W03 | 12 | 25.0 | 0.71 | -105 | -8.8 | -1.4 | 86 | 41 |
| 2026-W04 | 11 | 45.5 | 2.40 | 361 | 32.8 | 9.0 | 124 | 43 |
| 2026-W05 | 9 | 22.2 | 0.43 | -189 | -21.0 | -4.4 | 72 | 48 |
| 2026-W06 | 16 | 43.8 | 3.01 | 947 | 59.2 | 15.6 | 203 | 52 |
| 2026-W07 | 12 | 16.7 | 0.47 | -338 | -28.2 | -6.2 | 151 | 64 |
| 2026-W08 | 7 | 0.0 | 0.00 | -325 | -46.5 | -10.8 | 0 | 46 |
| 2026-W09 | 10 | 10.0 | 0.50 | -257 | -25.7 | -5.6 | 260 | 57 |
| 2026-W10 | 13 | 30.8 | 1.61 | 353 | 27.2 | 7.6 | 233 | 64 |
| 2026-W11 | 11 | 18.2 | 0.80 | -100 | -9.1 | -1.5 | 205 | 57 |
| 2026-W12 | 13 | 38.5 | 1.85 | 412 | 31.7 | 8.7 | 180 | 61 |
| 2026-W13 | 10 | 10.0 | 0.13 | -476 | -47.6 | -11.1 | 72 | 61 |
| 2026-W14 | 9 | 22.2 | 0.94 | -29 | -3.2 | 0.0 | 217 | 66 |
| 2026-W15 | 9 | 11.1 | 0.73 | -107 | -11.9 | -2.2 | 291 | 50 |
| 2026-W16 | 11 | 45.5 | 1.59 | 227 | 20.6 | 6.0 | 122 | 64 |
| 2026-W17 | 8 | 12.5 | 0.25 | -330 | -41.2 | -9.5 | 113 | 63 |
| 2026-W18 | 6 | 33.3 | 1.39 | 96 | 16.0 | 4.8 | 172 | 62 |
| 2026-W19 | 7 | 28.6 | 0.74 | -73 | -10.5 | -1.8 | 106 | 57 |
| 2026-W20 | 7 | 0.0 | 0.00 | -443 | -63.3 | -15.0 | 0 | 63 |
| 2026-W21 | 10 | 20.0 | 0.73 | -124 | -12.4 | -2.3 | 172 | 58 |
| 2026-W22 | 8 | 12.5 | 0.27 | -292 | -36.4 | -8.3 | 106 | 57 |
| 2026-W23 | 8 | 0.0 | 0.00 | -495 | -61.8 | -14.7 | 0 | 62 |
| 2026-W24 | 11 | 9.1 | 0.19 | -643 | -58.5 | -13.8 | 155 | 80 |
| 2026-W25 | 6 | 0.0 | 0.00 | -496 | -82.7 | -19.9 | 0 | 83 |
| 2026-W26 | 9 | 22.2 | 0.70 | -191 | -21.2 | -4.5 | 228 | 92 |
| 2026-W27 | 7 | 14.3 | 0.44 | -310 | -44.3 | -10.3 | 249 | 93 |
| 2026-W28 | 9 | 22.2 | 0.57 | -260 | -28.9 | -6.4 | 173 | 86 |
| 2026-W29 | 8 | 25.0 | 0.55 | -232 | -29.0 | -6.4 | 144 | 87 |
| 2026-W30 | 12 | 33.3 | 1.80 | 324 | 27.0 | 7.5 | 182 | 51 |
| 2026-W31 | 9 | 22.2 | 0.52 | -247 | -27.4 | -6.1 | 135 | 74 |
| 2026-W32 | 8 | 25.0 | 0.89 | -49 | -6.1 | -0.7 | 198 | 74 |
| 2026-W33 | 8 | 37.5 | 0.96 | -16 | -1.9 | 0.3 | 126 | 79 |
| 2026-W34 | 9 | 22.2 | 0.74 | -96 | -10.6 | -1.9 | 139 | 53 |
| 2026-W35 | 6 | 16.7 | 1.24 | 54 | 9.0 | 3.0 | 281 | 45 |
| 2026-W36 | 9 | 55.6 | 2.75 | 276 | 30.7 | 8.5 | 87 | 39 |
| 2026-W37 | 7 | 14.3 | 0.63 | -115 | -16.5 | -3.3 | 195 | 52 |
| 2026-W38 | 9 | 11.1 | 0.20 | -330 | -36.6 | -8.4 | 81 | 51 |
| 2026-W39 | 13 | 23.1 | 0.84 | -74 | -5.7 | -0.6 | 128 | 46 |
| 2026-W40 | 7 | 0.0 | 0.00 | -429 | -61.3 | -14.5 | 0 | 61 |

### By level family (a trade counts once per family in its zone)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| 4-hour | 146 | 24.0 | 0.88 | -755 | -5.2 | -0.5 | 160 | 57 |
| Custom | 255 | 22.4 | 0.79 | -2,368 | -9.3 | -1.5 | 156 | 57 |
| Daily | 156 | 19.9 | 0.62 | -2,665 | -17.1 | -3.5 | 139 | 56 |
| Day high/low | 1 | 100.0 | inf | 99 | 98.8 | 25.5 | 99 | 0 |
| Monthly | 5 | 40.0 | 1.29 | 64 | 12.8 | 4.0 | 142 | 74 |
| Quarter/Year | 4 | 50.0 | 2.73 | 189 | 47.3 | 12.6 | 149 | 55 |
| Weekly | 26 | 34.6 | 1.41 | 430 | 16.5 | 4.9 | 165 | 62 |

### By level code (a trade counts once per code in its zone)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| PWH | 9 | 44.4 | 2.54 | 466 | 51.8 | 13.8 | 192 | 61 |
| PWL | 17 | 29.4 | 0.95 | -36 | -2.1 | 0.3 | 143 | 63 |
| PDL | 30 | 23.3 | 0.91 | -117 | -3.9 | -0.2 | 177 | 59 |
| P4L | 76 | 25.0 | 0.95 | -162 | -2.1 | 0.3 | 160 | 56 |
| SR4 | 5 | 0.0 | 0.00 | -170 | -34.0 | -7.7 | 0 | 34 |
| PDH | 37 | 21.6 | 0.72 | -359 | -9.7 | -1.6 | 114 | 44 |
| P4H | 70 | 22.9 | 0.81 | -593 | -8.5 | -1.3 | 161 | 59 |
| DEM | 148 | 26.4 | 0.89 | -707 | -4.8 | -0.4 | 145 | 58 |
| MO | 52 | 19.2 | 0.71 | -711 | -13.7 | -2.6 | 175 | 59 |
| SR3 | 23 | 17.4 | 0.38 | -735 | -31.9 | -7.2 | 114 | 63 |
| DO | 43 | 20.9 | 0.57 | -858 | -19.9 | -4.2 | 128 | 59 |
| SUP | 102 | 20.6 | 0.80 | -940 | -9.2 | -1.5 | 174 | 57 |

### Single-level zones by code (clean attribution)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| PWH | 5 | 60.0 | 4.13 | 405 | 81.0 | 21.1 | 178 | 65 |
| SUP | 69 | 23.2 | 1.08 | 215 | 3.1 | 1.6 | 182 | 51 |
| PWL | 10 | 30.0 | 0.98 | -10 | -1.0 | 0.6 | 137 | 60 |
| P4H | 50 | 24.0 | 0.97 | -75 | -1.5 | 0.4 | 174 | 57 |
| PDH | 20 | 15.0 | 0.51 | -325 | -16.2 | -3.3 | 114 | 39 |
| P4L | 49 | 22.4 | 0.80 | -417 | -8.5 | -1.3 | 153 | 55 |
| PDL | 26 | 19.2 | 0.61 | -486 | -18.7 | -3.9 | 151 | 59 |
| SR3 | 18 | 16.7 | 0.42 | -529 | -29.4 | -6.5 | 130 | 61 |
| MO | 32 | 18.8 | 0.54 | -681 | -21.3 | -4.5 | 131 | 56 |
| DO | 24 | 16.7 | 0.37 | -766 | -31.9 | -7.2 | 113 | 61 |
| DEM | 87 | 20.7 | 0.73 | -1,098 | -12.6 | -2.4 | 164 | 59 |

### Retries (same zone and direction within 2 hours after a losing attempt)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| first attempt | 494 | 23.1 | 0.82 | -3,912 | -7.9 | -1.2 | 154 | 56 |
| retry | 8 | 12.5 | 0.56 | -183 | -22.8 | -4.9 | 232 | 59 |

### Held past a session change (entered 16:00-19:00 or after 23:00 chart time)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| evening entry | 1 | 0.0 | 0.00 | -64 | -64.2 | -15.2 | 0 | 64 |
| other | 501 | 23.0 | 0.82 | -4,030 | -8.0 | -1.2 | 154 | 56 |

### Run-up before the loss (losing trades: how far they went in favour first)

| Reached at least (pts) | Losing trades | Share of losers | Their net USD |
|---|---|---|---|
| 5 | 68 | 18 % | -3,779 |
| 10 | 62 | 16 % | -3,457 |
| 15 | 52 | 13 % | -2,934 |
| 20 | 42 | 11 % | -2,400 |
| 25 | 30 | 8 % | -1,784 |
| 30 | 24 | 6 % | -1,435 |
| 40 | 11 | 3 % | -614 |
| 50 | 8 | 2 % | -427 |
| 75 | 1 | 0 % | -59 |
| 100 | 0 | 0 % | 0 |
| 150 | 0 | 0 % | 0 |

### Run-up relative to the stop (stop-outs only; stop distance taken as the loss)

| Reached at least | Stop-outs | Share |
|---|---|---|
| 0.25 x stop | 68 | 18 % |
| 0.50 x stop | 65 | 17 % |
| 0.75 x stop | 63 | 16 % |
| 1.00 x stop | 51 | 13 % |
| 1.50 x stop | 39 | 10 % |
| 2.00 x stop | 31 | 8 % |

### Drawdown before the win (winning trades: how far against them first)

| Went against by at least (pts) | Winning trades | Share of winners | Their net USD |
|---|---|---|---|
| 5 | 62 | 54 % | 10,718 |
| 10 | 29 | 25 % | 4,981 |
| 15 | 5 | 4 % | 1,070 |
| 20 | 1 | 1 % | 191 |
| 25 | 0 | 0 % | 0 |
| 30 | 0 | 0 % | 0 |
| 40 | 0 | 0 % | 0 |
| 50 | 0 | 0 % | 0 |
| 75 | 0 | 0 % | 0 |

### What if the target were closer (all trades that reached it take it)

Exact: a trade whose run-up reached the target would have filled there before whatever it did next.

| Variant | Trades changed | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|
| as traded | 0 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |
| target 20 pts | 140 | 31.3 | 0.61 | -7,626 | -15.2 | 7,626 |
| target 30 pts | 91 | 27.7 | 0.71 | -5,873 | -11.7 | 6,020 |
| target 40 pts | 55 | 25.1 | 0.74 | -5,572 | -11.1 | 5,885 |
| target 50 pts | 37 | 24.5 | 0.79 | -4,507 | -9.0 | 5,374 |
| target 60 pts | 23 | 24.1 | 0.82 | -3,805 | -7.6 | 4,709 |
| target 80 pts | 8 | 23.1 | 0.80 | -4,311 | -8.6 | 5,147 |
| target 100 pts | 3 | 22.9 | 0.80 | -4,274 | -8.5 | 5,443 |
| target 120 pts | 1 | 22.9 | 0.81 | -4,129 | -8.2 | 5,363 |
| target 150 pts | 0 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |

### What if the stop were tighter (every trade that went against by that much is stopped)

Exact for the trades it stops; it cannot add what a saved trade would have done next.

| Variant | Trades changed | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|
| as traded | 0 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |
| stop 10 pts | 355 | 17.1 | 0.74 | -4,552 | -9.1 | 4,578 |
| stop 15 pts | 177 | 21.9 | 0.80 | -4,210 | -8.4 | 5,488 |
| stop 20 pts | 47 | 22.7 | 0.81 | -4,108 | -8.2 | 5,342 |
| stop 25 pts | 0 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |
| stop 30 pts | 0 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |
| stop 40 pts | 0 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |
| stop 50 pts | 0 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |

### What if one contract came off at a run-up (the other rides as traded)

Exact for the first contract; the second keeps the actual exit.

| Variant | Trades changed | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|
| as traded | 0 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |
| half off at +10 pts | 177 | 25.1 | 0.58 | -7,988 | -15.9 | 7,988 |
| half off at +15 pts | 165 | 26.1 | 0.65 | -6,777 | -13.5 | 6,777 |
| half off at +20 pts | 140 | 30.7 | 0.70 | -5,860 | -11.7 | 6,036 |
| half off at +25 pts | 107 | 28.9 | 0.73 | -5,467 | -10.9 | 5,891 |
| half off at +30 pts | 91 | 27.7 | 0.76 | -4,984 | -9.9 | 5,591 |
| half off at +40 pts | 55 | 25.1 | 0.77 | -4,833 | -9.6 | 5,544 |
| half off at +50 pts | 37 | 24.5 | 0.80 | -4,301 | -8.6 | 5,351 |
| half off at +75 pts | 9 | 23.1 | 0.80 | -4,292 | -8.6 | 5,267 |

### What if the stop moved to entry after a run-up (both contracts)

Best case: losers that had reached the run-up are taken as scratched (they did come back through entry); winners are assumed never to have come back to entry after the run-up, which the export cannot show.

| Variant | Trades changed | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|
| as traded | 0 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |
| breakeven after +10 pts | 62 | 22.9 | 0.95 | -959 | -1.9 | 3,627 |
| breakeven after +15 pts | 52 | 22.9 | 0.93 | -1,430 | -2.8 | 3,627 |
| breakeven after +20 pts | 42 | 22.9 | 0.90 | -1,912 | -3.8 | 3,830 |
| breakeven after +25 pts | 30 | 22.9 | 0.88 | -2,466 | -4.9 | 4,124 |
| breakeven after +30 pts | 24 | 22.9 | 0.86 | -2,784 | -5.5 | 4,357 |
| breakeven after +40 pts | 11 | 22.9 | 0.83 | -3,537 | -7.0 | 4,908 |
| breakeven after +50 pts | 8 | 22.9 | 0.83 | -3,709 | -7.4 | 5,080 |
| breakeven after +75 pts | 1 | 22.9 | 0.81 | -4,040 | -8.0 | 5,274 |

### What if one contract came off at a run-up and the stop on the other moved to entry

Same best-case assumption for the runner on winning trades.

| Variant | Trades changed | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|
| as traded | 0 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |
| half off at +10, runner to breakeven | 177 | 35.3 | 0.65 | -6,421 | -12.8 | 6,421 |
| half off at +15, runner to breakeven | 165 | 33.3 | 0.71 | -5,445 | -10.8 | 5,513 |
| half off at +20, runner to breakeven | 140 | 31.3 | 0.75 | -4,769 | -9.5 | 5,207 |
| half off at +25, runner to breakeven | 107 | 28.9 | 0.77 | -4,653 | -9.3 | 5,289 |
| half off at +30, runner to breakeven | 91 | 27.7 | 0.79 | -4,329 | -8.6 | 5,105 |
| half off at +40, runner to breakeven | 55 | 25.1 | 0.79 | -4,555 | -9.1 | 5,334 |
| half off at +50, runner to breakeven | 37 | 24.5 | 0.81 | -4,108 | -8.2 | 5,227 |
| half off at +75, runner to breakeven | 9 | 23.1 | 0.80 | -4,265 | -8.5 | 5,240 |

### By level history and window

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| h12 first test NY | 227 | 22.9 | 0.76 | -2,467 | -10.9 | -1.9 | 146 | 58 |
| h15 held NY | 53 | 26.4 | 1.04 | 84 | 1.6 | 1.2 | 170 | 59 |
| h3 broke NY | 24 | 20.8 | 0.87 | -154 | -6.4 | -0.8 | 198 | 60 |
| h6 touched NY | 198 | 22.2 | 0.81 | -1,558 | -7.9 | -1.2 | 154 | 54 |

### By level history and stack

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| h12 first test k1 | 192 | 23.4 | 0.79 | -1,728 | -9.0 | -1.5 | 149 | 57 |
| h12 first test k2 | 31 | 19.4 | 0.46 | -802 | -25.9 | -5.7 | 114 | 59 |
| h12 first test k3+ | 4 | 25.0 | 1.37 | 63 | 15.8 | 4.8 | 235 | 57 |
| h15 held k1 | 28 | 21.4 | 1.02 | 32 | 1.2 | 1.1 | 227 | 60 |
| h15 held k2 | 22 | 31.8 | 1.05 | 39 | 1.8 | 1.2 | 121 | 54 |
| h15 held k3+ | 3 | 33.3 | 1.09 | 13 | 4.5 | 1.9 | 167 | 77 |
| h3 broke k1 | 11 | 18.2 | 0.37 | -401 | -36.5 | -8.3 | 117 | 71 |
| h3 broke k2 | 9 | 22.2 | 1.46 | 167 | 18.6 | 5.4 | 266 | 52 |
| h3 broke k3+ | 4 | 25.0 | 1.57 | 80 | 20.0 | 5.8 | 222 | 47 |
| h6 touched k1 | 168 | 20.2 | 0.78 | -1,553 | -9.2 | -1.5 | 158 | 52 |
| h6 touched k2 | 27 | 37.0 | 1.15 | 185 | 6.8 | 2.5 | 142 | 73 |
| h6 touched k3+ | 3 | 0.0 | 0.00 | -190 | -63.2 | -15.0 | 0 | 63 |

### Stop-outs by size (points lost per contract)

| Size | Stop-outs | Share | USD lost | Ran up first by 0.5x the stop |
|---|---|---|---|---|
| 0-25 | 387 | 100 % | -21,853 | 65 |
| 25-50 | 0 | 0 % | 0 | 0 |
| 50-75 | 0 | 0 % | 0 | 0 |
| 75-100 | 0 | 0 % | 0 | 0 |
| 100-150 | 0 | 0 % | 0 | 0 |
| 150- | 0 | 0 % | 0 | 0 |

### Target exits by size (points won per contract)

| Size | T1 exits | Share | USD won |
|---|---|---|---|
| 0-50 | 85 | 75 % | 9,532 |
| 50-100 | 26 | 23 % | 6,751 |
| 100-150 | 3 | 3 % | 1,370 |
| 150-200 | 0 | 0 % | 0 |
| 200-300 | 0 | 0 % | 0 |
| 300- | 0 | 0 % | 0 |

### Days

239 days with a trade; 76 positive, 163 not.

| Worst days | Trades | Net USD | Losses in a row at most |
|---|---|---|---|
| 2026-06-25 Thu | 2 | -195 | 2 |
| 2026-07-02 Thu | 2 | -192 | 2 |
| 2026-07-08 Wed | 2 | -192 | 2 |
| 2026-06-17 Wed | 2 | -188 | 2 |
| 2026-06-18 Thu | 2 | -186 | 2 |
| 2026-06-12 Fri | 2 | -182 | 2 |
| 2026-07-16 Thu | 2 | -180 | 2 |
| 2026-07-17 Fri | 2 | -180 | 2 |

| Best days | Trades | Net USD |
|---|---|---|
| 2026-07-24 Fri | 4 | 616 |
| 2026-02-05 Thu | 4 | 590 |
| 2026-02-03 Tue | 4 | 500 |
| 2026-03-03 Tue | 4 | 455 |
| 2026-03-09 Mon | 3 | 399 |

| Without the worst N days | Net USD |
|---|---|
| 0 | -4,094 |
| 3 | -3,514 |
| 5 | -3,139 |
| 10 | -2,250 |

### What if trading stopped for the day after N losing trades (calendar day, chart time)

Removal only: a skipped trade frees the strategy to take another one the export cannot show.

| Cap | Trades kept | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|
| none | 502 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |
| 1 | 290 | 21.7 | 0.78 | -2,810 | -9.7 | 3,104 |
| 2 | 501 | 23.0 | 0.81 | -4,073 | -8.1 | 5,328 |
| 3 | 502 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |
| 4 | 502 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |
| 5 | 502 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |

### What if these trades were skipped (chosen after reading this sample; the long sample must confirm each)

Removal only, as above. Each rule alone, then all together.

| Rule | Trades skipped | Trades kept | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|---|
| skip retries | 8 | 494 | 23.1 | 0.82 | -3,912 | -7.9 | 5,271 |
| skip touched-today levels (h6) | 198 | 304 | 23.4 | 0.81 | -2,537 | -8.3 | 3,427 |
| skip zones with a 4-hour open (4HO or P4O) | 0 | 502 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |
| skip the 08:00 and 17:00-18:59 hours | 188 | 314 | 22.9 | 0.79 | -2,796 | -8.9 | 4,013 |
| skip scores 80 and up | 37 | 465 | 22.4 | 0.77 | -4,707 | -10.1 | 5,327 |
| skip the London window | 0 | 502 | 22.9 | 0.81 | -4,094 | -8.2 | 5,328 |
| all six together | 335 | 167 | 21.6 | 0.66 | -2,619 | -15.7 | 2,804 |
| history and 4-hour open rules only | 198 | 304 | 23.4 | 0.81 | -2,537 | -8.3 | 3,427 |

### Dependence on the best trades

| Without the best N trades | Net USD | PF |
|---|---|---|
| 0 | -4,094 | 0.81 |
| 1 | -4,606 | 0.79 |
| 3 | -5,465 | 0.75 |
| 5 | -6,217 | 0.72 |
| 10 | -7,792 | 0.64 |
| 20 | -10,265 | 0.53 |

### Ten best and ten worst trades

| # | Entry (chart time) | Tag | Exit | Pts | Net USD | Run-up pts | Drawdown pts | Bars |
|---|---|---|---|---|---|---|---|---|
| 229 | 2026-03-03 08:45 | REV SUP s82 k1 h15 f1 c3 NY | T1 | 128.8 | 512 | 129 | 8 | 3 |
| 121 | 2025-12-18 09:10 | REV DEM s82 k1 h15 f0 c3 NY | T1 | 112.0 | 445 | 112 | 13 | 3 |
| 67 | 2025-11-18 08:45 | BRK MO+PDL s40 k2 h6 c3 NY | T1 | 104.2 | 414 | 104 | 8 | 0 |
| 108 | 2025-12-11 08:35 | BRK P4H s54 k1 h12 c3 NY | T1 | 95.2 | 378 | 95 | 6 | 2 |
| 192 | 2026-02-05 09:15 | BRK P4L s33 k1 h6 c3 NY | T1 | 94.5 | 375 | 94 | 12 | 3 |
| 93 | 2025-12-03 09:10 | BRK PWH s73 k1 h12 c3 NY | T1 | 87.2 | 346 | 87 | 2 | 5 |
| 193 | 2026-02-05 09:50 | BRK P4L s33 k1 h6 c3 NY | T1 | 86.2 | 342 | 86 | 4 | 3 |
| 414 | 2026-07-24 08:30 | REV SUP s71 k1 h6 f0 c2 NY | T1 | 79.8 | 316 | 80 | 17 | 1 |
| 284 | 2026-04-07 08:55 | REV P4L+SUP s76 k2 h3 f2 c3 NY | T1 | 73.5 | 291 | 74 | 3 | 0 |
| 452 | 2026-08-25 08:35 | BRK DEM s29 k1 h12 c3 NY | T1 | 71.0 | 281 | 71 | 6 | 2 |
| 393 | 2026-07-08 09:20 | REV SUP+SUP s79 k2 h6 f1 c3 NY | stop | -23.2 | -96 | 0 | 23 | 0 |
| 394 | 2026-07-08 09:50 | BRK PDL s61 k1 h6 c3 NY | stop | -23.2 | -96 | 0 | 23 | 0 |
| 396 | 2026-07-09 09:25 | BRK DEM s29 k1 h12 c3 NY | stop | -23.2 | -96 | 0 | 23 | 0 |
| 379 | 2026-06-25 09:50 | BRK SUP s29 k1 h12 c3 NY | stop | -23.5 | -97 | 0 | 24 | 0 |
| 380 | 2026-06-25 13:10 | BRK SUP s29 k1 h12 c3 NY | stop | -23.8 | -98 | 0 | 24 | 0 |
| 382 | 2026-06-29 08:30 | REV SUP+SUP+P4H s100 k3 h15 f1 c2 NY | stop | -23.8 | -98 | 0 | 24 | 0 |
| 386 | 2026-07-01 08:15 | BRK SUP+P4L s30 k2 h6 c2 NY | stop | -23.8 | -98 | 0 | 24 | 0 |
| 389 | 2026-07-06 08:30 | BRK P4H+SUP s30 k2 h6 c2 NY | stop | -23.8 | -98 | 0 | 24 | 0 |
| 381 | 2026-06-26 10:50 | BRK SR3 s39 k1 h12 c3 NY | stop | -24.0 | -99 | 0 | 24 | 0 |
| 384 | 2026-06-29 09:35 | BRK SR3+MO s40 k2 h6 c3 NY | stop | -24.0 | -99 | 0 | 24 | 0 |
