# Trade-list report

File: reference/backtests/2026-09-22/trades_M7v0.1_method_deep-365d_500k.csv
Trades: 417, 2025-09-22 09:15 to 2026-09-16 13:45, size 2, 4 USD per point, commission 3.20 a round trip.
Win 26.62 %, PF 0.93, net -1,426.40 USD, -3.42 USD a trade, -0.06 points a trade per contract.
Avg win 170.51 USD, avg loss 66.51 USD, closed-trade max drawdown 3,834.40 USD.
Median stop-out loss 15.5 points, mean 15.8.
Median T1 win 33.4 points, mean 44.8.
Hold: median 0 bars, mean 1.6; winners median 1, losers median 0.

### By exit reason

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| T1 | 102 | 100.0 | inf | 17,960 | 176.1 | 44.8 | 176 | 0 |
| stop | 306 | 0.0 | 0.00 | -20,353 | -66.5 | -15.8 | 0 | 67 |
| flat | 9 | 100.0 | inf | 967 | 107.5 | 27.7 | 107 | 0 |

### By setup

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| REV | 248 | 26.2 | 0.90 | -1,263 | -5.1 | -0.5 | 174 | 69 |
| BRK | 169 | 27.2 | 0.98 | -164 | -1.0 | 0.6 | 166 | 64 |

### By direction

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| long | 190 | 25.8 | 0.81 | -1,801 | -9.5 | -1.6 | 156 | 67 |
| short | 227 | 27.3 | 1.03 | 375 | 1.7 | 1.2 | 182 | 66 |

### By window (script's tag)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| NY | 417 | 26.6 | 0.93 | -1,426 | -3.4 | -0.1 | 171 | 67 |

### By setup and window

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| BRK NY | 169 | 27.2 | 0.98 | -164 | -1.0 | 0.6 | 166 | 64 |
| REV NY | 248 | 26.2 | 0.90 | -1,263 | -5.1 | -0.5 | 174 | 69 |

### By stack (levels in the zone)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| k1 | 300 | 26.7 | 0.99 | -93 | -0.3 | 0.7 | 182 | 67 |
| k2 | 90 | 27.8 | 0.76 | -1,036 | -11.5 | -2.1 | 133 | 67 |
| k3+ | 27 | 22.2 | 0.78 | -297 | -11.0 | -2.0 | 175 | 64 |

### By score

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| s100-109 | 1 | 100.0 | inf | 97 | 96.8 | 25.0 | 97 | 0 |
| s50-59 | 152 | 30.9 | 1.24 | 1,705 | 11.2 | 3.6 | 189 | 68 |
| s60-69 | 118 | 22.0 | 0.75 | -1,544 | -13.1 | -2.5 | 178 | 67 |
| s70-79 | 111 | 25.2 | 0.79 | -1,085 | -9.8 | -1.6 | 148 | 63 |
| s80-89 | 20 | 35.0 | 1.03 | 26 | 1.3 | 1.1 | 124 | 65 |
| s90-99 | 15 | 13.3 | 0.33 | -625 | -41.7 | -9.6 | 153 | 72 |

### By level history

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| h12 first test | 103 | 27.2 | 1.01 | 37 | 0.4 | 0.9 | 174 | 64 |
| h15 held | 188 | 23.9 | 0.82 | -1,810 | -9.6 | -1.6 | 180 | 69 |
| h3 broke | 56 | 32.1 | 1.14 | 340 | 6.1 | 2.3 | 155 | 65 |
| h6 touched | 70 | 28.6 | 1.00 | 6 | 0.1 | 0.8 | 157 | 63 |

### By higher-timeframe rejections (reversals, M6)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| f0 of 4 | 69 | 21.7 | 0.90 | -363 | -5.3 | -0.5 | 225 | 69 |
| f1 of 4 | 108 | 22.2 | 0.60 | -2,343 | -21.7 | -4.6 | 146 | 70 |
| f2 of 4 | 53 | 30.2 | 1.21 | 523 | 9.9 | 3.3 | 186 | 66 |
| f3 of 4 | 14 | 50.0 | 2.25 | 521 | 37.2 | 10.1 | 134 | 60 |
| f4 of 4 | 4 | 75.0 | 6.75 | 398 | 99.6 | 25.7 | 156 | 69 |

### By at least N higher-timeframe rejections (cumulative)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| f>=0 | 248 | 26.2 | 0.90 | -1,263 | -5.1 | -0.5 | 174 | 69 |
| f>=1 | 179 | 27.9 | 0.90 | -900 | -5.0 | -0.5 | 158 | 68 |
| f>=2 | 71 | 36.6 | 1.49 | 1,443 | 20.3 | 5.9 | 169 | 65 |
| f>=3 | 18 | 55.6 | 2.89 | 919 | 51.1 | 13.6 | 141 | 61 |
| f>=4 | 4 | 75.0 | 6.75 | 398 | 99.6 | 25.7 | 156 | 69 |

### By level history and setup

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| BRK h12 first test | 103 | 27.2 | 1.01 | 37 | 0.4 | 0.9 | 174 | 64 |
| BRK h6 touched | 66 | 27.3 | 0.93 | -201 | -3.0 | 0.0 | 154 | 62 |
| REV h15 held | 188 | 23.9 | 0.82 | -1,810 | -9.6 | -1.6 | 180 | 69 |
| REV h3 broke | 56 | 32.1 | 1.14 | 340 | 6.1 | 2.3 | 155 | 65 |
| REV h6 touched | 4 | 50.0 | 2.26 | 207 | 51.8 | 13.8 | 186 | 82 |

### By hour of entry (chart time)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| 09:00 | 234 | 26.9 | 0.84 | -1,860 | -7.9 | -1.2 | 155 | 68 |
| 10:00 | 51 | 27.5 | 1.00 | 10 | 0.2 | 0.8 | 169 | 64 |
| 11:00 | 38 | 15.8 | 0.82 | -389 | -10.2 | -1.8 | 287 | 66 |
| 12:00 | 38 | 23.7 | 0.97 | -59 | -1.5 | 0.4 | 191 | 61 |
| 13:00 | 31 | 22.6 | 1.17 | 279 | 9.0 | 3.0 | 272 | 68 |
| 14:00 | 19 | 42.1 | 1.51 | 393 | 20.7 | 6.0 | 146 | 71 |
| 15:00 | 6 | 66.7 | 2.90 | 199 | 33.1 | 9.1 | 76 | 52 |

### By weekday of entry

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| Mon | 77 | 36.4 | 1.10 | 325 | 4.2 | 1.9 | 128 | 66 |
| Tue | 80 | 28.8 | 1.19 | 699 | 8.7 | 3.0 | 194 | 66 |
| Wed | 94 | 17.0 | 0.49 | -2,653 | -28.2 | -6.3 | 158 | 66 |
| Thu | 85 | 22.4 | 0.74 | -1,135 | -13.4 | -2.5 | 168 | 66 |
| Fri | 81 | 30.9 | 1.35 | 1,338 | 16.5 | 4.9 | 206 | 68 |

### By month of entry

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| 2025-09 | 9 | 11.1 | 0.69 | -64 | -7.1 | -1.0 | 142 | 26 |
| 2025-10 | 38 | 21.1 | 1.05 | 64 | 1.7 | 1.2 | 162 | 41 |
| 2025-11 | 30 | 26.7 | 0.86 | -200 | -6.7 | -0.9 | 155 | 66 |
| 2025-12 | 42 | 28.6 | 1.05 | 88 | 2.1 | 1.3 | 155 | 59 |
| 2026-01 | 36 | 25.0 | 1.01 | 17 | 0.5 | 0.9 | 152 | 50 |
| 2026-02 | 32 | 40.6 | 1.19 | 235 | 7.3 | 2.6 | 113 | 65 |
| 2026-03 | 36 | 27.8 | 1.18 | 322 | 8.9 | 3.0 | 216 | 71 |
| 2026-04 | 30 | 20.0 | 0.49 | -843 | -28.1 | -6.2 | 135 | 69 |
| 2026-05 | 33 | 15.2 | 0.30 | -1,290 | -39.1 | -9.0 | 111 | 66 |
| 2026-06 | 37 | 32.4 | 1.44 | 946 | 25.6 | 7.2 | 258 | 86 |
| 2026-07 | 38 | 13.2 | 0.47 | -1,658 | -43.6 | -10.1 | 289 | 94 |
| 2026-08 | 35 | 37.1 | 1.19 | 338 | 9.7 | 3.2 | 162 | 81 |
| 2026-09 | 21 | 42.9 | 1.82 | 619 | 29.5 | 8.2 | 153 | 63 |

### By week of entry

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| 2025-W39 | 7 | 14.3 | 0.87 | -21 | -3.1 | 0.0 | 142 | 27 |
| 2025-W40 | 7 | 0.0 | 0.00 | -190 | -27.2 | -6.0 | 0 | 27 |
| 2025-W41 | 10 | 10.0 | 0.37 | -137 | -13.7 | -2.6 | 79 | 24 |
| 2025-W42 | 9 | 44.4 | 3.51 | 668 | 74.2 | 19.4 | 234 | 53 |
| 2025-W43 | 6 | 16.7 | 0.46 | -147 | -24.5 | -5.3 | 127 | 55 |
| 2025-W44 | 8 | 25.0 | 0.47 | -172 | -21.4 | -4.6 | 77 | 54 |
| 2025-W45 | 9 | 33.3 | 1.33 | 110 | 12.2 | 3.9 | 146 | 55 |
| 2025-W46 | 2 | 0.0 | 0.00 | -128 | -64.2 | -15.2 | 0 | 64 |
| 2025-W47 | 11 | 27.3 | 1.11 | 60 | 5.4 | 2.2 | 198 | 67 |
| 2025-W48 | 8 | 25.0 | 0.46 | -242 | -30.2 | -6.8 | 105 | 75 |
| 2025-W49 | 11 | 27.3 | 1.18 | 95 | 8.6 | 3.0 | 209 | 67 |
| 2025-W50 | 11 | 18.2 | 0.91 | -48 | -4.4 | -0.3 | 238 | 58 |
| 2025-W51 | 9 | 44.4 | 2.07 | 309 | 34.4 | 9.4 | 149 | 58 |
| 2025-W52 | 5 | 20.0 | 0.02 | -228 | -45.6 | -10.6 | 6 | 58 |
| 2026-W01 | 9 | 33.3 | 1.24 | 69 | 7.7 | 2.7 | 120 | 49 |
| 2026-W02 | 10 | 30.0 | 1.35 | 120 | 12.0 | 3.8 | 155 | 49 |
| 2026-W03 | 6 | 16.7 | 0.19 | -200 | -33.4 | -7.5 | 46 | 49 |
| 2026-W04 | 8 | 25.0 | 0.87 | -40 | -4.9 | -0.4 | 132 | 51 |
| 2026-W05 | 9 | 22.2 | 1.07 | 27 | 3.0 | 1.6 | 196 | 52 |
| 2026-W06 | 7 | 0.0 | 0.00 | -437 | -62.5 | -14.8 | 0 | 62 |
| 2026-W07 | 11 | 72.7 | 4.59 | 727 | 66.1 | 17.3 | 116 | 68 |
| 2026-W08 | 8 | 25.0 | 0.61 | -157 | -19.6 | -4.1 | 123 | 67 |
| 2026-W09 | 6 | 50.0 | 1.54 | 102 | 17.0 | 5.0 | 97 | 63 |
| 2026-W10 | 8 | 37.5 | 2.21 | 413 | 51.7 | 13.7 | 251 | 68 |
| 2026-W11 | 11 | 27.3 | 0.66 | -191 | -17.4 | -3.5 | 125 | 71 |
| 2026-W12 | 7 | 14.3 | 0.27 | -307 | -43.9 | -10.2 | 115 | 70 |
| 2026-W13 | 5 | 20.0 | 0.41 | -172 | -34.4 | -7.8 | 119 | 73 |
| 2026-W14 | 8 | 25.0 | 1.77 | 346 | 43.3 | 11.6 | 398 | 75 |
| 2026-W15 | 9 | 22.2 | 0.66 | -175 | -19.4 | -4.1 | 168 | 73 |
| 2026-W16 | 3 | 33.3 | 0.57 | -59 | -19.5 | -4.1 | 78 | 68 |
| 2026-W17 | 9 | 22.2 | 0.64 | -168 | -18.6 | -3.9 | 147 | 66 |
| 2026-W18 | 6 | 16.7 | 0.32 | -209 | -34.9 | -7.9 | 100 | 62 |
| 2026-W19 | 3 | 0.0 | 0.00 | -184 | -61.2 | -14.5 | 0 | 61 |
| 2026-W20 | 13 | 23.1 | 0.62 | -245 | -18.8 | -3.9 | 133 | 64 |
| 2026-W21 | 11 | 9.1 | 0.09 | -618 | -56.2 | -13.2 | 59 | 68 |
| 2026-W22 | 6 | 16.7 | 0.28 | -243 | -40.5 | -9.3 | 97 | 68 |
| 2026-W23 | 10 | 50.0 | 1.95 | 297 | 29.7 | 8.2 | 122 | 63 |
| 2026-W24 | 10 | 20.0 | 0.78 | -150 | -15.0 | -3.0 | 265 | 85 |
| 2026-W25 | 9 | 22.2 | 0.77 | -156 | -17.3 | -3.5 | 257 | 96 |
| 2026-W26 | 6 | 50.0 | 5.02 | 1,156 | 192.6 | 49.0 | 481 | 96 |
| 2026-W27 | 5 | 20.0 | 1.52 | 231 | 46.2 | 12.3 | 677 | 111 |
| 2026-W28 | 8 | 0.0 | 0.00 | -776 | -97.0 | -23.4 | 0 | 97 |
| 2026-W29 | 10 | 20.0 | 0.36 | -470 | -47.0 | -10.9 | 132 | 92 |
| 2026-W30 | 8 | 12.5 | 0.69 | -196 | -24.5 | -5.3 | 434 | 90 |
| 2026-W31 | 9 | 11.1 | 0.10 | -649 | -72.1 | -17.2 | 72 | 90 |
| 2026-W32 | 7 | 0.0 | 0.00 | -666 | -95.2 | -23.0 | 0 | 95 |
| 2026-W33 | 5 | 40.0 | 0.53 | -120 | -24.0 | -5.2 | 67 | 85 |
| 2026-W34 | 8 | 37.5 | 1.93 | 348 | 43.5 | 11.7 | 241 | 75 |
| 2026-W35 | 12 | 58.3 | 3.38 | 827 | 68.9 | 18.0 | 168 | 69 |
| 2026-W36 | 12 | 50.0 | 2.82 | 705 | 58.7 | 15.5 | 182 | 64 |
| 2026-W37 | 7 | 42.9 | 0.99 | -3 | -0.5 | 0.7 | 82 | 63 |
| 2026-W38 | 5 | 20.0 | 0.46 | -133 | -26.6 | -5.8 | 115 | 62 |

### By level family (a trade counts once per family in its zone)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| Asia | 137 | 24.8 | 0.95 | -362 | -2.6 | 0.1 | 189 | 66 |
| Custom | 36 | 25.0 | 0.60 | -795 | -22.1 | -4.7 | 135 | 74 |
| Daily | 97 | 22.7 | 0.74 | -1,261 | -13.0 | -2.5 | 163 | 65 |
| Day high/low | 18 | 27.8 | 1.03 | 23 | 1.3 | 1.1 | 176 | 66 |
| London | 119 | 30.3 | 1.02 | 106 | 0.9 | 1.0 | 160 | 68 |
| Monday | 62 | 25.8 | 0.80 | -585 | -9.4 | -1.6 | 147 | 64 |
| Monthly | 14 | 42.9 | 1.24 | 134 | 9.6 | 3.2 | 114 | 69 |
| New York | 37 | 21.6 | 0.65 | -663 | -17.9 | -3.7 | 157 | 66 |
| Quarter/Year | 3 | 66.7 | 20.84 | 440 | 146.8 | 37.5 | 231 | 22 |
| Weekly | 60 | 30.0 | 1.16 | 427 | 7.1 | 2.6 | 176 | 65 |

### By level code (a trade counts once per code in its zone)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| AH | 72 | 29.2 | 1.20 | 678 | 9.4 | 3.2 | 193 | 66 |
| LL | 60 | 33.3 | 1.16 | 453 | 7.6 | 2.7 | 160 | 69 |
| PML | 5 | 60.0 | 3.11 | 290 | 58.0 | 15.3 | 142 | 69 |
| HOD | 9 | 33.3 | 1.61 | 268 | 29.8 | 8.2 | 235 | 73 |
| PWL | 34 | 29.4 | 1.15 | 252 | 7.4 | 2.7 | 197 | 72 |
| SR4 | 7 | 42.9 | 1.86 | 212 | 30.2 | 8.4 | 153 | 62 |
| PWH | 26 | 30.8 | 1.17 | 175 | 6.7 | 2.5 | 148 | 56 |
| MNH | 35 | 31.4 | 1.07 | 110 | 3.1 | 1.6 | 146 | 62 |
| PMH | 9 | 33.3 | 0.62 | -156 | -17.3 | -3.5 | 86 | 69 |
| SR5 | 6 | 33.3 | 0.35 | -226 | -37.7 | -8.6 | 61 | 87 |
| LOD | 9 | 22.2 | 0.42 | -245 | -27.2 | -6.0 | 87 | 60 |
| PDH | 50 | 28.0 | 0.89 | -263 | -5.3 | -0.5 | 153 | 67 |
| NH | 20 | 20.0 | 0.75 | -280 | -14.0 | -2.7 | 208 | 70 |
| LH | 59 | 27.1 | 0.88 | -347 | -5.9 | -0.7 | 159 | 67 |
| NL | 17 | 23.5 | 0.52 | -383 | -22.6 | -4.8 | 105 | 62 |
| MNL | 27 | 18.5 | 0.52 | -695 | -25.8 | -5.6 | 151 | 66 |
| SR3 | 23 | 17.4 | 0.45 | -781 | -33.9 | -7.7 | 159 | 74 |
| PDL | 47 | 17.0 | 0.59 | -998 | -21.2 | -4.5 | 181 | 63 |
| AL | 65 | 20.0 | 0.69 | -1,040 | -16.0 | -3.2 | 181 | 65 |

### Single-level zones by code (clean attribution)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| AH | 47 | 27.7 | 1.37 | 830 | 17.7 | 5.2 | 235 | 65 |
| LL | 40 | 37.5 | 1.46 | 765 | 19.1 | 5.6 | 163 | 67 |
| PWL | 26 | 30.8 | 1.29 | 387 | 14.9 | 4.5 | 213 | 73 |
| SR4 | 5 | 60.0 | 3.84 | 339 | 67.8 | 17.8 | 153 | 60 |
| LH | 37 | 27.0 | 0.98 | -46 | -1.3 | 0.5 | 184 | 70 |
| AL | 44 | 22.7 | 0.93 | -144 | -3.3 | -0.0 | 197 | 62 |
| PDH | 13 | 23.1 | 0.79 | -163 | -12.5 | -2.3 | 200 | 76 |
| PWH | 11 | 18.2 | 0.55 | -225 | -20.5 | -4.3 | 138 | 56 |
| MNH | 13 | 23.1 | 0.44 | -321 | -24.7 | -5.4 | 83 | 57 |
| PDL | 30 | 20.0 | 0.74 | -394 | -13.1 | -2.5 | 183 | 62 |
| MNL | 14 | 14.3 | 0.37 | -495 | -35.3 | -8.0 | 143 | 65 |
| SR3 | 12 | 16.7 | 0.29 | -516 | -43.0 | -10.0 | 108 | 73 |

### Retries (same zone and direction within 2 hours after a losing attempt)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| first attempt | 397 | 26.4 | 0.94 | -1,240 | -3.1 | 0.0 | 173 | 67 |
| retry | 20 | 30.0 | 0.80 | -186 | -9.3 | -1.5 | 121 | 65 |

### Held past a session change (entered 16:00-19:00 or after 23:00 chart time)

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| other | 417 | 26.6 | 0.93 | -1,426 | -3.4 | -0.1 | 171 | 67 |

### Run-up before the loss (losing trades: how far they went in favour first)

| Reached at least (pts) | Losing trades | Share of losers | Their net USD |
|---|---|---|---|
| 5 | 144 | 47 % | -9,834 |
| 10 | 110 | 36 % | -7,648 |
| 15 | 81 | 26 % | -5,895 |
| 20 | 57 | 19 % | -4,091 |
| 25 | 41 | 13 % | -2,953 |
| 30 | 32 | 10 % | -2,373 |
| 40 | 18 | 6 % | -1,356 |
| 50 | 13 | 4 % | -968 |
| 75 | 6 | 2 % | -471 |
| 100 | 2 | 1 % | -145 |
| 150 | 0 | 0 % | 0 |

### Run-up relative to the stop (stop-outs only; stop distance taken as the loss)

| Reached at least | Stop-outs | Share |
|---|---|---|
| 0.25 x stop | 151 | 49 % |
| 0.50 x stop | 126 | 41 % |
| 0.75 x stop | 99 | 32 % |
| 1.00 x stop | 64 | 21 % |
| 1.50 x stop | 46 | 15 % |
| 2.00 x stop | 25 | 8 % |

### Drawdown before the win (winning trades: how far against them first)

| Went against by at least (pts) | Winning trades | Share of winners | Their net USD |
|---|---|---|---|
| 5 | 71 | 64 % | 12,431 |
| 10 | 39 | 35 % | 7,379 |
| 15 | 11 | 10 % | 3,065 |
| 20 | 2 | 2 % | 1,138 |
| 25 | 0 | 0 % | 0 |
| 30 | 0 | 0 % | 0 |
| 40 | 0 | 0 % | 0 |
| 50 | 0 | 0 % | 0 |
| 75 | 0 | 0 % | 0 |

### What if the target were closer (all trades that reached it take it)

Exact: a trade whose run-up reached the target would have filled there before whatever it did next.

| Variant | Trades changed | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|
| as traded | 0 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |
| target 20 pts | 149 | 40.3 | 0.77 | -3,660 | -8.8 | 4,604 |
| target 30 pts | 100 | 34.3 | 0.84 | -2,944 | -7.1 | 4,478 |
| target 40 pts | 57 | 30.9 | 0.85 | -2,813 | -6.7 | 4,010 |
| target 50 pts | 42 | 29.7 | 0.89 | -2,200 | -5.3 | 4,000 |
| target 60 pts | 30 | 28.5 | 0.88 | -2,452 | -5.9 | 4,401 |
| target 80 pts | 18 | 27.8 | 0.91 | -1,752 | -4.2 | 3,956 |
| target 100 pts | 10 | 27.1 | 0.90 | -1,936 | -4.6 | 4,555 |
| target 120 pts | 5 | 26.9 | 0.90 | -1,929 | -4.6 | 4,227 |
| target 150 pts | 4 | 26.6 | 0.90 | -2,003 | -4.8 | 4,392 |

### What if the stop were tighter (every trade that went against by that much is stopped)

Exact for the trades it stops; it cannot add what a saved trade would have done next.

| Variant | Trades changed | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|
| as traded | 0 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |
| stop 10 pts | 323 | 17.3 | 0.76 | -3,621 | -8.7 | 5,620 |
| stop 15 pts | 212 | 24.0 | 0.84 | -3,100 | -7.4 | 5,288 |
| stop 20 pts | 63 | 26.1 | 0.89 | -2,220 | -5.3 | 4,628 |
| stop 25 pts | 5 | 26.6 | 0.93 | -1,403 | -3.4 | 3,811 |
| stop 30 pts | 1 | 26.6 | 0.93 | -1,408 | -3.4 | 3,816 |
| stop 40 pts | 0 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |
| stop 50 pts | 0 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |

### What if one contract came off at a run-up (the other rides as traded)

Exact for the first contract; the second keeps the actual exit.

| Variant | Trades changed | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|
| as traded | 0 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |
| half off at +10 pts | 221 | 27.3 | 0.79 | -2,999 | -7.2 | 4,056 |
| half off at +15 pts | 189 | 29.7 | 0.83 | -2,501 | -6.0 | 3,878 |
| half off at +20 pts | 149 | 35.7 | 0.85 | -2,543 | -6.1 | 4,122 |
| half off at +25 pts | 120 | 36.2 | 0.86 | -2,483 | -6.0 | 4,177 |
| half off at +30 pts | 100 | 34.3 | 0.88 | -2,185 | -5.2 | 4,030 |
| half off at +40 pts | 57 | 30.9 | 0.89 | -2,120 | -5.1 | 3,888 |
| half off at +50 pts | 42 | 29.7 | 0.91 | -1,813 | -4.3 | 3,879 |
| half off at +75 pts | 21 | 28.1 | 0.92 | -1,540 | -3.7 | 3,790 |

### What if the stop moved to entry after a run-up (both contracts)

Best case: losers that had reached the run-up are taken as scratched (they did come back through entry); winners are assumed never to have come back to entry after the run-up, which the export cannot show.

| Variant | Trades changed | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|
| as traded | 0 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |
| breakeven after +10 pts | 110 | 26.6 | 1.43 | 5,650 | 13.5 | 1,112 |
| breakeven after +15 pts | 81 | 26.6 | 1.27 | 4,048 | 9.7 | 1,209 |
| breakeven after +20 pts | 57 | 26.6 | 1.14 | 2,369 | 5.7 | 1,898 |
| breakeven after +25 pts | 41 | 26.6 | 1.07 | 1,314 | 3.2 | 2,171 |
| breakeven after +30 pts | 32 | 26.6 | 1.04 | 781 | 1.9 | 2,317 |
| breakeven after +40 pts | 18 | 26.6 | 0.99 | -164 | -0.4 | 2,948 |
| breakeven after +50 pts | 13 | 26.6 | 0.97 | -526 | -1.3 | 3,196 |
| breakeven after +75 pts | 6 | 26.6 | 0.95 | -986 | -2.4 | 3,457 |

### What if one contract came off at a run-up and the stop on the other moved to entry

Same best-case assumption for the runner on winning trades.

| Variant | Trades changed | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|
| as traded | 0 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |
| half off at +10, runner to breakeven | 221 | 53.0 | 1.04 | 539 | 1.3 | 1,649 |
| half off at +15, runner to breakeven | 189 | 46.0 | 1.02 | 236 | 0.6 | 1,765 |
| half off at +20, runner to breakeven | 149 | 40.3 | 0.96 | -646 | -1.5 | 2,597 |
| half off at +25, runner to breakeven | 120 | 36.5 | 0.94 | -1,113 | -2.7 | 3,013 |
| half off at +30, runner to breakeven | 100 | 34.3 | 0.94 | -1,082 | -2.6 | 3,122 |
| half off at +40, runner to breakeven | 57 | 30.9 | 0.92 | -1,489 | -3.6 | 3,445 |
| half off at +50, runner to breakeven | 42 | 29.7 | 0.93 | -1,363 | -3.3 | 3,560 |
| half off at +75, runner to breakeven | 21 | 28.1 | 0.93 | -1,320 | -3.2 | 3,602 |

### By level history and window

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| h12 first test NY | 103 | 27.2 | 1.01 | 37 | 0.4 | 0.9 | 174 | 64 |
| h15 held NY | 188 | 23.9 | 0.82 | -1,810 | -9.6 | -1.6 | 180 | 69 |
| h3 broke NY | 56 | 32.1 | 1.14 | 340 | 6.1 | 2.3 | 155 | 65 |
| h6 touched NY | 70 | 28.6 | 1.00 | 6 | 0.1 | 0.8 | 157 | 63 |

### By level history and stack

| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |
|---|---|---|---|---|---|---|---|---|
| h12 first test k1 | 88 | 26.1 | 1.02 | 78 | 0.9 | 1.0 | 186 | 65 |
| h12 first test k2 | 10 | 40.0 | 1.04 | 19 | 1.9 | 1.3 | 111 | 71 |
| h12 first test k3+ | 5 | 20.0 | 0.72 | -60 | -12.0 | -2.2 | 154 | 53 |
| h15 held k1 | 121 | 23.1 | 0.88 | -815 | -6.7 | -0.9 | 206 | 71 |
| h15 held k2 | 48 | 27.1 | 0.78 | -517 | -10.8 | -1.9 | 141 | 67 |
| h15 held k3+ | 19 | 21.1 | 0.53 | -478 | -25.1 | -5.5 | 133 | 67 |
| h3 broke k1 | 37 | 37.8 | 1.43 | 616 | 16.6 | 5.0 | 146 | 62 |
| h3 broke k2 | 18 | 22.2 | 0.78 | -213 | -11.8 | -2.2 | 188 | 69 |
| h3 broke k3+ | 1 | 0.0 | 0.00 | -63 | -63.2 | -15.0 | 0 | 63 |
| h6 touched k1 | 54 | 27.8 | 1.01 | 28 | 0.5 | 0.9 | 166 | 63 |
| h6 touched k2 | 14 | 28.6 | 0.47 | -326 | -23.3 | -5.0 | 72 | 61 |
| h6 touched k3+ | 2 | 50.0 | 5.88 | 304 | 151.8 | 38.8 | 366 | 62 |

### Stop-outs by size (points lost per contract)

| Size | Stop-outs | Share | USD lost | Ran up first by 0.5x the stop |
|---|---|---|---|---|
| 0-25 | 305 | 100 % | -20,210 | 126 |
| 25-50 | 1 | 0 % | -143 | 0 |
| 50-75 | 0 | 0 % | 0 | 0 |
| 75-100 | 0 | 0 % | 0 | 0 |
| 100-150 | 0 | 0 % | 0 | 0 |
| 150- | 0 | 0 % | 0 | 0 |

### Target exits by size (points won per contract)

| Size | T1 exits | Share | USD won |
|---|---|---|---|
| 0-50 | 75 | 74 % | 8,318 |
| 50-100 | 20 | 20 % | 5,364 |
| 100-150 | 3 | 3 % | 1,313 |
| 150-200 | 3 | 3 % | 1,970 |
| 200-300 | 1 | 1 % | 994 |
| 300- | 0 | 0 % | 0 |

### Days

205 days with a trade; 72 positive, 133 not.

| Worst days | Trades | Net USD | Losses in a row at most |
|---|---|---|---|
| 2026-06-29 Mon | 2 | -201 | 2 |
| 2026-08-05 Wed | 2 | -198 | 2 |
| 2026-07-08 Wed | 2 | -194 | 2 |
| 2026-07-09 Thu | 2 | -194 | 2 |
| 2026-06-17 Wed | 2 | -190 | 2 |
| 2026-07-10 Fri | 2 | -190 | 2 |
| 2026-08-06 Thu | 2 | -188 | 2 |
| 2026-06-12 Fri | 2 | -187 | 2 |

| Best days | Trades | Net USD |
|---|---|---|
| 2026-06-26 Fri | 2 | 894 |
| 2026-03-06 Fri | 3 | 754 |
| 2026-08-24 Mon | 3 | 682 |
| 2026-07-02 Thu | 1 | 677 |
| 2026-09-01 Tue | 1 | 616 |

| Without the worst N days | Net USD |
|---|---|
| 0 | -1,426 |
| 3 | -832 |
| 5 | -447 |
| 10 | 491 |

### What if trading stopped for the day after N losing trades (calendar day, chart time)

Removal only: a skipped trade frees the strategy to take another one the export cannot show.

| Cap | Trades kept | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|
| none | 417 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |
| 1 | 251 | 27.1 | 0.91 | -1,058 | -4.2 | 3,300 |
| 2 | 417 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |
| 3 | 417 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |
| 4 | 417 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |
| 5 | 417 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |

### What if these trades were skipped (chosen after reading this sample; the long sample must confirm each)

Removal only, as above. Each rule alone, then all together.

| Rule | Trades skipped | Trades kept | Win % | PF | Net USD | USD/trade | Closed-trade max DD |
|---|---|---|---|---|---|---|---|
| skip retries | 20 | 397 | 26.4 | 0.94 | -1,240 | -3.1 | 3,443 |
| skip touched-today levels (h6) | 70 | 347 | 26.2 | 0.92 | -1,432 | -4.1 | 3,792 |
| skip zones with a 4-hour open (4HO or P4O) | 0 | 417 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |
| skip the 08:00 and 17:00-18:59 hours | 0 | 417 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |
| skip scores 80 and up | 36 | 381 | 26.5 | 0.95 | -924 | -2.4 | 3,495 |
| skip the London window | 0 | 417 | 26.6 | 0.93 | -1,426 | -3.4 | 3,834 |
| all six together | 118 | 299 | 26.1 | 0.96 | -541 | -1.8 | 2,773 |
| history and 4-hour open rules only | 70 | 347 | 26.2 | 0.92 | -1,432 | -4.1 | 3,792 |

### Dependence on the best trades

| Without the best N trades | Net USD | PF |
|---|---|---|
| 0 | -1,426 | 0.93 |
| 1 | -2,420 | 0.88 |
| 3 | -3,775 | 0.81 |
| 5 | -4,848 | 0.76 |
| 10 | -6,835 | 0.66 |
| 20 | -9,725 | 0.52 |

### Ten best and ten worst trades

| # | Entry (chart time) | Tag | Exit | Pts | Net USD | Run-up pts | Drawdown pts | Bars |
|---|---|---|---|---|---|---|---|---|
| 321 | 2026-06-26 13:10 | REV LH s66 k1 h15 f2 NY | T1 | 249.2 | 994 | 249 | 25 | 21 |
| 223 | 2026-03-31 10:00 | REV AH s52 k1 h15 f0 NY | T1 | 170.2 | 678 | 170 | 3 | 19 |
| 325 | 2026-07-02 09:10 | BRK AH s56 k1 h12 NY | T1 | 170.0 | 677 | 170 | 16 | 3 |
| 397 | 2026-09-01 11:25 | REV LL s56 k1 h3 f0 NY | T1 | 154.8 | 616 | 155 | 9 | 27 |
| 28 | 2025-10-15 12:25 | BRK AL s52 k1 h6 NY | T1 | 115.2 | 458 | 115 | 8 | 4 |
| 351 | 2026-07-24 09:20 | BRK PWL s59 k1 h12 NY | T1 | 109.2 | 434 | 109 | 17 | 3 |
| 195 | 2026-03-06 14:15 | BRK PDL s65 k1 h6 NY | T1 | 106.2 | 422 | 106 | 1 | 2 |
| 299 | 2026-06-09 11:00 | BRK PWL s59 k1 h12 NY | T1 | 97.2 | 386 | 97 | 10 | 1 |
| 81 | 2025-12-02 09:40 | REV PDH+MNH s62 k2 h3 f1 NY | T1 | 95.8 | 380 | 96 | 5 | 2 |
| 316 | 2026-06-22 09:20 | REV MNH+NH+HOD+PWH+YH s89 k4 h6 f1 NY | T1 | 92.2 | 366 | 92 | 4 | 1 |
| 329 | 2026-07-08 09:25 | REV AL+PWL s66 k2 h15 f1 NY | stop | -23.8 | -98 | 45 | 25 | 0 |
| 332 | 2026-07-09 14:55 | REV SR3 s60 k1 h15 f1 NY | stop | -23.8 | -98 | 0 | 25 | 0 |
| 322 | 2026-06-29 09:15 | BRK AL s56 k1 h12 NY | stop | -24.0 | -99 | 0 | 25 | 0 |
| 363 | 2026-08-05 09:10 | REV PDH s52 k1 h15 f0 NY | stop | -24.0 | -99 | 17 | 25 | 0 |
| 364 | 2026-08-05 09:55 | REV AH s57 k1 h15 f0 NY | stop | -24.0 | -99 | 22 | 25 | 0 |
| 320 | 2026-06-26 13:00 | REV SR3 s62 k1 h15 f1 NY | stop | -24.2 | -100 | 4 | 25 | 0 |
| 324 | 2026-07-01 09:15 | REV LL s73 k1 h15 f0 NY | stop | -24.5 | -101 | 0 | 25 | 0 |
| 323 | 2026-06-29 09:50 | REV LL+SR3 s67 k2 h3 f2 NY | stop | -24.8 | -102 | 4 | 26 | 0 |
| 327 | 2026-07-06 09:05 | REV AH+NH+MNH+HOD s98 k3 h15 f1 NY | stop | -24.8 | -102 | 14 | 26 | 0 |
| 326 | 2026-07-03 11:50 | REV SR5 s62 k1 h15 f0 NY | stop | -35.0 | -143 | 6 | 36 | 2 |
