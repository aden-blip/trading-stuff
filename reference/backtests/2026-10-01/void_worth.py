import importlib.util, statistics
spec = importlib.util.spec_from_file_location("tlr", "tools/trade_list_report.py")
tlr = importlib.util.module_from_spec(spec); spec.loader.exec_module(tlr)
T = tlr.load("reference/backtests/2026-10-01/trades_M9v0.1_source-method_deep-365d_500k.csv", 2.0)

void = [t for t in T if t["exit"] == "void"]
rest = [t for t in T if t["exit"] != "void"]
wins = [t for t in rest if t["net"] > 0]
loss = [t for t in rest if t["net"] <= 0]
aw = statistics.mean(t["net"] for t in wins)
al = statistics.mean(t["net"] for t in loss)
base = len(wins) / len(rest)
cost_now = sum(t["net"] for t in void)

print("the 76 void exits cost  : $%,.0f  ($%.1f each)".replace(",", "") % (cost_now, cost_now/len(void)))
print("everything else         : %d trades, %.1f %% win, avg win $%.0f, avg loss $%.0f" % (len(rest), 100*base, aw, al))
print()
print("If those 76 had been left alone, at the same win rate as every other trade:")
exp = len(void) * (base*aw + (1-base)*al)
print("   expected result       : $%.0f   (%.0f winners at $%.0f, %.0f losers at $%.0f)"
      % (exp, base*len(void), aw, (1-base)*len(void), al))
print("   so cutting them early : $%+.0f over the year" % (cost_now - exp))
print()
be = (cost_now/len(void) - al) / (aw - al)
print("Break-even: the void exit only pays if a candle closing back through the level")
print("cuts the win rate on those trades from %.1f %% to below %.1f %%." % (100*base, 100*be))
