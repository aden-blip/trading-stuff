#!/usr/bin/env python3
"""Compare two tester exports of the same range trade by trade.

Usage:  python3 tools/compare_runs.py <base export.csv> <new export.csv>

Trades are matched by entry time and order comment (the tag), so a matched pair is the same
entry under two versions of the script. Prints: the matched set under each version, the
trades only one version took, the exit-to-exit transitions with their money, and the month
table. Used to read what a manager or a filter did to the same entries (D-92).
"""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import trade_list_report as R

base = R.load(sys.argv[1], 2.0)
new = R.load(sys.argv[2], 2.0)
kb = {(t['entry_time'], t['tag']): t for t in base}
kn = {(t['entry_time'], t['tag']): t for t in new}
both = [k for k in kn if k in kb]
onlyn = [k for k in kn if k not in kb]
onlyb = [k for k in kb if k not in kn]

def s(trs):
    st = R.stats(trs)
    return f"{st['n']} trades, win {st['win']:.0f} %, PF {R.pf_str(st['pf'])}, net {st['net']:,.0f}, {st['avg']:.1f} a trade"
print(f"# Two runs, trade by trade\n\nBase: {sys.argv[1]}\nNew: {sys.argv[2]}\n")
print(f"- base {len(base)} trades, new {len(new)}; matched {len(both)}; only in new {len(onlyn)}; only in base {len(onlyb)}")
print(f"- matched, as the base did: {s([kb[k] for k in both])}")
print(f"- matched, as the new did: {s([kn[k] for k in both])}")
if onlyn:
    print(f"- only in new (extra): {s([kn[k] for k in onlyn])}")
if onlyb:
    print(f"- only in base (dropped): {s([kb[k] for k in onlyb])}")
tr = collections.defaultdict(list)
for k in both:
    tr[(kb[k]['exit'], kn[k]['exit'])].append((kb[k]['net'], kn[k]['net']))
print("\n### Matched trades: base exit against new exit\n")
print("| Base exit | New exit | Trades | Base net | New net | Change |")
print("|---|---|---|---|---|---|")
for key in sorted(tr, key=lambda k: -abs(sum(b - a for a, b in tr[k]))):
    v = tr[key]; a = sum(x for x, _ in v); b = sum(y for _, y in v)
    print(f"| {key[0]} | {key[1]} | {len(v)} | {a:,.0f} | {b:,.0f} | {b - a:+,.0f} |")
print("\n### Matched trades by the new exit\n")
print("| New exit | Trades | Base net (same entries) | New net | Change |")
print("|---|---|---|---|---|")
for ex in ['T1', 'stop', 'half', 'be', 'trail', 'flat']:
    ks = [k for k in both if kn[k]['exit'] == ex]
    if ks:
        a = sum(kb[k]['net'] for k in ks); b = sum(kn[k]['net'] for k in ks)
        print(f"| {ex} | {len(ks)} | {a:,.0f} | {b:,.0f} | {b - a:+,.0f} |")
if onlyn:
    print("\n### Extra trades by exit\n")
    for ex in ['T1', 'stop', 'half', 'be', 'trail', 'flat']:
        v = [kn[k] for k in onlyn if kn[k]['exit'] == ex]
        if v:
            print(f"- {ex}: {len(v)} trades, net {sum(t['net'] for t in v):,.0f}")
print("\n### By month\n")
print("| Month | Base trades | Base net | New trades | New net |")
print("|---|---|---|---|---|")
for mth in sorted({t['month'] for t in base} | {t['month'] for t in new}):
    a = [t for t in base if t['month'] == mth]; b = [t for t in new if t['month'] == mth]
    print(f"| {mth} | {len(a)} | {sum(t['net'] for t in a):,.0f} | {len(b)} | {sum(t['net'] for t in b):,.0f} |")
