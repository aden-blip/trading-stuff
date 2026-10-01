import importlib.util, collections
spec = importlib.util.spec_from_file_location("tlr", "tools/trade_list_report.py")
tlr = importlib.util.module_from_spec(spec); spec.loader.exec_module(tlr)

trades = tlr.load("reference/backtests/2026-09-22/trades_M7v0.1_method_deep-365d_500k.csv", 2.0)
trades.sort(key=lambda t: t["entry_time"])

# Which level types he names as good, and which he calls bad.
GOOD = {"P4H","P4L","P4M","P4O","4HO",          # 4-hour high/low/open
        "DO","MO",                               # daily open, midnight open
        "PQH","PQL","PQM","QO","YH","YL","YM","YO"}  # quarterly / yearly
KEEP = {"PDH","PDL","PDM","PWH","PWL","PWM","WO","PMH","PML","PMM","MOO","MNH","MNL","MNM"}
BAD  = {"AH","AL","AO","LH","LL","LO","NH","NL","NO","HOD","LOD"}   # session highs/lows

def bucket(codes):
    s = set(codes)
    if s & BAD:  return "session H/L (he says no)"
    if s & GOOD: return "his named levels"
    if s & KEEP: return "prev day/week/month"
    if any(c.startswith("PV") for c in s): return "my pivots"
    if "SR" in s: return "drawn S/R"
    return "other"

def stat(rows):
    n = len(rows)
    if not n: return None
    net = sum(t["net"] for t in rows)
    w = [t for t in rows if t["net"] > 0]
    gp = sum(t["net"] for t in w); gl = -sum(t["net"] for t in rows if t["net"] <= 0)
    pf = gp/gl if gl else float("inf")
    return n, 100.0*len(w)/n, pf, net, net/n

half = len(trades)//2
H1, H2 = trades[:half], trades[half:]

print("| group | trades | win %% | PF | net | per trade | 1st half /tr | 2nd half /tr | agree |")
print("|---|---|---|---|---|---|---|---|---|")
groups = collections.defaultdict(list)
for t in trades: groups[bucket(t["codes"])].append(t)
for g, rows in sorted(groups.items(), key=lambda kv: -sum(x["net"] for x in kv[1])):
    n, wr, pf, net, pt = stat(rows)
    a = stat([t for t in H1 if bucket(t["codes"]) == g])
    b = stat([t for t in H2 if bucket(t["codes"]) == g])
    aa = "%+.2f" % a[4] if a else "-"
    bb = "%+.2f" % b[4] if b else "-"
    ag = "yes" if a and b and (a[4] > 0) == (b[4] > 0) else "NO"
    print("| %s | %d | %.1f | %.2f | %+.0f | %+.2f | %s | %s | %s |" % (g, n, wr, pf, net, pt, aa, bb, ag))

print()
print("Per level code (10+ trades), worst first:")
print("| code | family | trades | win %% | PF | net | per trade | h1 /tr | h2 /tr | agree |")
print("|---|---|---|---|---|---|---|---|---|---|")
bycode = collections.defaultdict(list)
for t in trades:
    for c in set(t["codes"]): bycode[c].append(t)
for c, rows in sorted(bycode.items(), key=lambda kv: sum(x["net"] for x in kv[1])/len(kv[1])):
    if len(rows) < 10: continue
    n, wr, pf, net, pt = stat(rows)
    a = stat([t for t in H1 if c in t["codes"]]); b = stat([t for t in H2 if c in t["codes"]])
    aa = "%+.2f" % a[4] if a else "-"; bb = "%+.2f" % b[4] if b else "-"
    ag = "yes" if a and b and (a[4] > 0) == (b[4] > 0) else "NO"
    print("| %s | %s | %d | %.1f | %.2f | %+.0f | %+.2f | %s | %s | %s |" % (c, tlr.family(c), n, wr, pf, net, pt, aa, bb, ag))
