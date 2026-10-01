every code that appears, with trade count:
   AH     Asia           72
   AL     Asia           65
   LL     London         60
   LH     London         59
   PDH    Daily          50
   PDL    Daily          47
   MNH    Monday         35
   PWL    Weekly         34
   MNL    Monday         27
   PWH    Weekly         26
   SR3    Custom         23
   NH     New York       20
   NL     New York       17
   LOD    Day high/low   9
   HOD    Day high/low   9
   PMH    Monthly        9
   SR4    Custom         7
   SR5    Custom         6
   PML    Monthly        5
   YH     Quarter/Year   2
   YL     Quarter/Year   1

4-hour           -> ZERO TRADES, ever
daily open       -> ZERO TRADES, ever
midnight open    -> ZERO TRADES, ever
quarterly H/L    -> ZERO TRADES, ever
quarterly open   -> ZERO TRADES, ever
yearly           -> ['YL', 'YH']
| group | trades | win %% | PF | net | per trade | 1st half /tr | 2nd half /tr | agree |
|---|---|---|---|---|---|---|---|---|
| session H/L (he says no) | 256 | 26.6 | 0.99 | -145 | -0.57 | +1.66 | -2.66 | NO |
| other | 18 | 27.8 | 0.68 | -321 | -17.81 | +23.05 | -50.50 | NO |
| prev day/week/month | 143 | 26.6 | 0.86 | -961 | -6.72 | -2.23 | -11.81 | yes |

Per level code (10+ trades), worst first:
| code | family | trades | win %% | PF | net | per trade | h1 /tr | h2 /tr | agree |
|---|---|---|---|---|---|---|---|---|---|
| SR3 | Custom | 23 | 17.4 | 0.45 | -781 | -33.94 | -34.45 | -33.67 | yes |
| MNL | Monday | 27 | 18.5 | 0.52 | -695 | -25.76 | +1.98 | -44.83 | NO |
| NL | New York | 17 | 23.5 | 0.52 | -383 | -22.55 | -35.70 | -10.87 | yes |
| PDL | Daily | 47 | 17.0 | 0.59 | -998 | -21.24 | -14.07 | -33.91 | yes |
| AL | Asia | 65 | 20.0 | 0.69 | -1040 | -16.00 | +2.80 | -33.14 | NO |
| NH | New York | 20 | 20.0 | 0.75 | -280 | -14.00 | +9.94 | -26.89 | NO |
| LH | London | 59 | 27.1 | 0.88 | -347 | -5.88 | -7.65 | -4.17 | yes |
| PDH | Daily | 50 | 28.0 | 0.89 | -263 | -5.26 | +39.45 | -53.70 | NO |
| MNH | Monday | 35 | 31.4 | 1.07 | +110 | +3.14 | +12.98 | -13.51 | NO |
| PWH | Weekly | 26 | 30.8 | 1.17 | +175 | +6.72 | -3.66 | +17.11 | NO |
| PWL | Weekly | 34 | 29.4 | 1.15 | +252 | +7.42 | -59.11 | +39.23 | NO |
| LL | London | 60 | 33.3 | 1.16 | +453 | +7.55 | +8.86 | +6.14 | yes |
| AH | Asia | 72 | 29.2 | 1.20 | +678 | +9.41 | +0.45 | +16.19 | yes |
