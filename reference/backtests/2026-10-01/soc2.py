import importlib.util, collections
spec = importlib.util.spec_from_file_location("tlr", "tools/trade_list_report.py")
tlr = importlib.util.module_from_spec(spec); spec.loader.exec_module(tlr)
trades = tlr.load("reference/backtests/2026-09-22/trades_M7v0.1_method_deep-365d_500k.csv", 2.0)
c = collections.Counter()
for t in trades:
    for code in set(t["codes"]): c[code] += 1
print("every code that appears, with trade count:")
for code, n in c.most_common(): print("   %-6s %-14s %d" % (code, tlr.family(code), n))
print()
for want, label in [("P4", "4-hour"), ("DO", "daily open"), ("MO", "midnight open"),
                    ("PQ", "quarterly H/L"), ("QO", "quarterly open"), ("Y", "yearly")]:
    hits = [k for k in c if k.startswith(want)]
    print("%-16s -> %s" % (label, hits if hits else "ZERO TRADES, ever"))
