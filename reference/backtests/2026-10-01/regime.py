import importlib.util, collections, statistics
spec = importlib.util.spec_from_file_location("tlr", "tools/trade_list_report.py")
tlr = importlib.util.module_from_spec(spec); spec.loader.exec_module(tlr)
T = tlr.load("reference/backtests/2026-10-01/trades_M9v0.1_source-method_deep-365d_500k.csv", 2.0)
T.sort(key=lambda t: t["entry_time"])

# Stop distance in points is set from the daily ATR, so a stop-out's loss size is a clean
# volatility proxy that needs no extra data.
by = collections.defaultdict(list)
for t in T: by[t["entry_time"].strftime("%Y-%m")].append(t)
print("| month | trades | win % | PF | net | avg stop-out, pts (volatility proxy) |")
print("|---|---|---|---|---|---|")
rows = []
for m in sorted(by):
    r = by[m]
    stops = [abs(t["pts"]) for t in r if t["exit"] == "stop"]
    gp = sum(t["net"] for t in r if t["net"] > 0); gl = -sum(t["net"] for t in r if t["net"] <= 0)
    pf = gp/gl if gl else float("inf")
    w = 100.0*len([t for t in r if t["net"] > 0])/len(r)
    sd = statistics.mean(stops) if stops else float("nan")
    rows.append((m, len(r), w, pf, sum(t["net"] for t in r), sd))
    print("| %s | %d | %.0f | %.2f | %+.0f | %.1f |" % (m, len(r), w, pf, sum(t["net"] for t in r), sd))

import math
good = [r for r in rows if not math.isnan(r[5])]
xs = [r[5] for r in good]; ys = [r[3] for r in good]
mx, my = statistics.mean(xs), statistics.mean(ys)
num = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
den = math.sqrt(sum((x-mx)**2 for x in xs) * sum((y-my)**2 for y in ys))
print("\ncorrelation between the month's stop size and its profit factor: %+.2f (n=%d months)" % (num/den, len(good)))

# Split every trade by how wide its own stop was, and check both halves agree.
stops_all = sorted(abs(t["pts"]) for t in T if t["exit"] == "stop")
med = statistics.median(stops_all)
print("median stop-out: %.1f points -> that is the cut between 'calm' and 'wide'\n" % med)
half = len(T)//2
H1, H2 = set(id(t) for t in T[:half]), set(id(t) for t in T[half:])
def stat(rs):
    if not rs: return None
    gp = sum(t["net"] for t in rs if t["net"] > 0); gl = -sum(t["net"] for t in rs if t["net"] <= 0)
    return len(rs), 100.0*len([t for t in rs if t["net"]>0])/len(rs), (gp/gl if gl else 99), sum(t["net"] for t in rs), sum(t["net"] for t in rs)/len(rs)
# a trade's own risk: use the loss distance for stops, and the recorded stop for the rest is
# unavailable, so bucket by the month's volatility instead - same cut, cleanly assignable.
mvol = {m: r[5] for m, *r in [(r[0], *r[1:]) for r in rows]}
calm = [t for t in T if not math.isnan(mvol.get(t["entry_time"].strftime("%Y-%m"), float("nan"))) and mvol[t["entry_time"].strftime("%Y-%m")] <= med]
wide = [t for t in T if not math.isnan(mvol.get(t["entry_time"].strftime("%Y-%m"), float("nan"))) and mvol[t["entry_time"].strftime("%Y-%m")] >  med]
print("| volatility of the month | trades | win % | PF | net | per trade | 1st half /tr | 2nd half /tr | agree |")
print("|---|---|---|---|---|---|---|---|---|")
for nm, rs in (("calm months (stop <= %.1f pts)" % med, calm), ("wide months (stop > %.1f pts)" % med, wide)):
    a = stat([t for t in rs if id(t) in H1]); b = stat([t for t in rs if id(t) in H2]); s = stat(rs)
    print("| %s | %d | %.1f | %.2f | %+.0f | %+.2f | %s | %s | %s |" % (
        nm, s[0], s[1], s[2], s[3], s[4],
        "%+.2f" % a[4] if a else "-", "%+.2f" % b[4] if b else "-",
        "yes" if a and b and (a[4] > 0) == (b[4] > 0) else "NO"))
