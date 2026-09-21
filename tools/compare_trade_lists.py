#!/usr/bin/env python3
"""Compare a long tester export against its two halves (and an optional second export).

Usage:  python3 tools/compare_trade_lists.py <long export.csv> [<second export.csv>]

Prints the same breakdowns as trade_list_report.py side by side for the whole sample, its
first half, its second half and the second file, plus what-if tables in R (R = the trade's
own stop for stop-outs, the month's median stop-out otherwise). A finding counts only when
it holds on both halves (D-88).
"""
import sys, os, collections, statistics, datetime as dt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import trade_list_report as R

deep = R.load(sys.argv[1], 2.0)
lo, hi = deep[0]['entry_time'], deep[-1]['entry_time']
mid = lo + (hi - lo) / 2
h1 = [t for t in deep if t['entry_time'] < mid]
h2 = [t for t in deep if t['entry_time'] >= mid]
sets = [('all', deep), (f'H1 to {mid:%d %b}', h1), (f'H2 from {mid:%d %b}', h2)]
if len(sys.argv) > 2:
    sets.append(('second file', R.load(sys.argv[2], 2.0)))

# R proxy: own stop for stop-outs, else the median stop-out loss of the same month
def add_R(trs):
    bym = collections.defaultdict(list)
    for t in trs:
        if t['exit'] == 'stop':
            bym[t['month']].append(-t['pts'])
    allmed = statistics.median([-t['pts'] for t in trs if t['exit'] == 'stop'])
    for t in trs:
        t['R'] = -t['pts'] if t['exit'] == 'stop' else (statistics.median(bym[t['month']]) if bym[t['month']] else allmed)
for _, trs in sets:
    add_R(trs)
    last = {}
    for t in trs:
        key = (t['zone'], t['dir'])
        prev = last.get(key)
        t['retry'] = bool(prev and prev['net'] <= 0 and 0 <= (t['entry_time'] - prev['exit_time']).total_seconds() <= 7200)
        last[key] = t

def cell(trs):
    s = R.stats(trs)
    if not s: return '- | - | - | -'
    return f"{s['n']} | {s['win']:.0f} % | {R.pf_str(s['pf'])} | {s['net']:,.0f}"

def comp(title, fn, order=None, min_n=20):
    print(f"\n### {title}\n")
    print("| Group | " + " | ".join(f"{name}: n, win, PF, net" for name, _ in sets) + " |")
    print("|---|" + "---|" * len(sets))
    keys = order or sorted({fn(t) for t in deep})
    for k in keys:
        cells = []
        for name, trs in sets:
            sub = [t for t in trs if fn(t) == k]
            cells.append(cell(sub))
        if any(len([t for t in trs if fn(t) == k]) >= min_n for _, trs in sets):
            print(f"| {k} | " + " | ".join(cells) + " |")

comp("By exit reason", lambda t: t['exit'], ['T1', 'stop', 'half', 'be', 'trail', 'flat'])
comp("By setup", lambda t: t['setup'], ['REV', 'BRK'])
comp("By direction", lambda t: 'long' if t['dir'] > 0 else 'short', ['long', 'short'])
comp("By window", lambda t: t['window'], ['ASIA', 'LON', 'NY', 'OTH'])
comp("By stack", lambda t: f"k{t['stack']}" if t['stack'] < 3 else 'k3+', ['k1', 'k2', 'k3+'])
comp("By score", lambda t: f"s{t['score']//10*10}s")
comp("By level history", lambda t: f"h{t['hist']} {R.HIST.get(t['hist'],'?')}", ['h12 first test', 'h6 touched', 'h15 held', 'h3 broke'])
if any(t.get('htf') is not None for t in deep):
    comp("By higher-timeframe rejections (reversals, M6)", lambda t: f"f{t['htf']}" if t.get('htf') is not None else 'BRK', ['f0', 'f1', 'f2', 'f3', 'f4', 'BRK'])
comp("By level history, REV only", lambda t: (f"REV h{t['hist']} {R.HIST.get(t['hist'],'?')}" if t['setup']=='REV' else 'BRK'), ['REV h12 first test', 'REV h6 touched', 'REV h15 held', 'REV h3 broke', 'BRK'])
comp("By level history and window", lambda t: f"h{t['hist']} {t['window']}")
comp("By hour of entry", lambda t: f"{t['hour']:02d}", [f"{h:02d}" for h in range(24)], min_n=1)
comp("By weekday", lambda t: t['wday'], ['Sun','Mon','Tue','Wed','Thu','Fri'])
fam = lambda t: None
def famkeys(t):
    return sorted({R.family(c) for c in t['codes']})
print("\n### By level family (a trade counts once per family in its zone)\n")
print("| Family | " + " | ".join(f"{name}: n, win, PF, net" for name, _ in sets) + " |")
print("|---|" + "---|" * len(sets))
fams = sorted({f for t in deep for f in famkeys(t)})
for f in fams:
    print(f"| {f} | " + " | ".join(cell([t for t in trs if f in famkeys(t)]) for _, trs in sets) + " |")
print("\n### By level code (a trade counts once per code in its zone), sorted by 365d net\n")
print("| Code | " + " | ".join(f"{name}: n, win, PF, net" for name, _ in sets) + " |")
print("|---|" + "---|" * len(sets))
codes = sorted({c for t in deep for c in t['codes']}, key=lambda c: -sum(t['net'] for t in deep if c in t['codes']))
for c in codes:
    if len([t for t in deep if c in t['codes']]) >= 30:
        print(f"| {c} | " + " | ".join(cell([t for t in trs if c in t['codes']]) for _, trs in sets) + " |")
comp("Zones with a 4-hour open (4HO or P4O)", lambda t: '4H open in zone' if ('4HO' in t['codes'] or 'P4O' in t['codes']) else 'no 4H open', ['4H open in zone', 'no 4H open'])
comp("Retries within 2 hours of a losing attempt", lambda t: 'retry' if t['retry'] else 'first attempt', ['first attempt', 'retry'])
comp("Evening entries (16:00-18:59 or 23:00 and later)", lambda t: 'evening' if (16 <= t['hour'] < 19 or t['hour'] >= 23) else 'other', ['evening', 'other'])
comp("By month", lambda t: t['month'], min_n=1)

# What-ifs in R and in points
def sims(title, variants):
    print(f"\n### {title}\n")
    print("| Variant | " + " | ".join(f"{name}: win, PF, net, DD" for name, _ in sets) + " |")
    print("|---|" + "---|" * len(sets))
    for label, fn in [('as traded', lambda t: t['net'])] + variants:
        cells = []
        for name, trs in sets:
            new = [fn(t) for t in trs]
            s = R.stats([dict(net=v, pts=0.0) for v in new])
            cells.append(f"{s['win']:.0f} % | {R.pf_str(s['pf'])} | {s['net']:,.0f} | {R.drawdown(new):,.0f}")
        print(f"| {label} | " + " | ".join(cells) + " |")
upp, comm, slip, pv, qty = 4.0, 3.2, 0.5, 2.0, 2
def be_R(x):   # ceiling: losers that reached x*R scratched, winners untouched
    return lambda t: (-slip*upp - comm) if (t['mfe'] >= x*t['R'] and t['net'] <= 0) else t['net']
def staged():  # D-32 ceiling on losers: +0.5R -> stop at -0.5R, +1R -> scratch
    def fn(t):
        if t['net'] > 0: return t['net']
        if t['mfe'] >= 1.0*t['R']: return -slip*upp - comm
        if t['mfe'] >= 0.5*t['R']: return max(t['net'], -(0.5*t['R'] + slip)*upp - comm)
        return t['net']
    return fn
def partial_R(x):
    return lambda t: (x*t['R']*pv + t['pts']*pv*(qty-1) - comm) if t['mfe'] >= x*t['R'] else t['net']
def partial_be_R(x):
    return lambda t: (x*t['R']*pv + (t['pts'] if t['net'] > 0 else -slip)*pv*(qty-1) - comm) if t['mfe'] >= x*t['R'] else t['net']
def target_R(y):
    return lambda t: (y*t['R']*upp - comm) if t['mfe'] >= y*t['R'] else t['net']
def stop_R(sd):
    return lambda t: (-(sd*t['R'] + slip)*upp - comm) if t['mae'] >= sd*t['R'] else t['net']
sims("Ceilings in R (losers exact, winners assumed untouched)", [
    ('D-32 stages on losers: -0.5R after +0.5R, scratch after +1R', staged()),
    ('breakeven after +0.5R', be_R(0.5)), ('breakeven after +0.75R', be_R(0.75)), ('breakeven after +1R', be_R(1.0)), ('breakeven after +1.5R', be_R(1.5))])
sims("Exact: one contract off at a run-up in R, the other as traded", [
    ('half off at +0.5R', partial_R(0.5)), ('half off at +0.75R', partial_R(0.75)), ('half off at +1R', partial_R(1.0)), ('half off at +1.5R', partial_R(1.5))])
sims("Ceiling: half off in R and the runner's stop to entry", [
    ('half off at +0.5R, runner BE', partial_be_R(0.5)), ('half off at +1R, runner BE', partial_be_R(1.0)), ('half off at +1.5R, runner BE', partial_be_R(1.5))])
sims("Exact: target in R instead of the next level", [
    ('target 1R', target_R(1.0)), ('target 1.5R', target_R(1.5)), ('target 2R', target_R(2.0)), ('target 3R', target_R(3.0))])
sims("Exact: tighter stop as a share of the stop", [
    ('stop 0.5R', stop_R(0.5)), ('stop 0.75R', stop_R(0.75))])

# Run-up before loss, in R
print("\n### Losers: run-up before the loss, in R (R = own stop for stop-outs, the month's median stop otherwise)\n")
print("| Reached at least | " + " | ".join(f"{name}: share of losers, their net" for name, _ in sets) + " |")
print("|---|" + "---|" * len(sets))
for x in [0.25, 0.5, 0.75, 1.0, 1.5, 2.0]:
    cells = []
    for name, trs in sets:
        losers = [t for t in trs if t['net'] <= 0]
        sub = [t for t in losers if t['mfe'] >= x*t['R']]
        cells.append(f"{100*len(sub)/len(losers):.0f} % | {sum(t['net'] for t in sub):,.0f}")
    print(f"| {x} R | " + " | ".join(cells) + " |")
print("\n### Winners: drawdown before the win, in R\n")
print("| Went against by at least | " + " | ".join(f"{name}: share of winners" for name, _ in sets) + " |")
print("|---|" + "---|" * len(sets))
for x in [0.1, 0.25, 0.5, 0.75, 1.0]:
    cells = []
    for name, trs in sets:
        w = [t for t in trs if t['net'] > 0]
        cells.append(f"{100*sum(1 for t in w if t['mae'] >= x*t['R'])/len(w):.0f} %")
    print(f"| {x} R | " + " | ".join(cells) + " |")

# Skip rules
rules = [
    ("skip retries", lambda t: t['retry']),
    ("skip touched-today (h6)", lambda t: t['hist'] == 6),
    ("skip held-today (h15)", lambda t: t['hist'] == 15),
    ("skip touched and held today (one reversal per level per day)", lambda t: t['hist'] in (6, 15)),
    ("skip zones with a 4-hour open", lambda t: '4HO' in t['codes'] or 'P4O' in t['codes']),
    ("skip 08:00 and 17:00-18:59", lambda t: t['hour'] in (8, 17, 18)),
    ("skip scores 80+", lambda t: t['score'] >= 80),
    ("skip London window", lambda t: t['window'] == 'LON'),
    ("skip BRK", lambda t: t['setup'] == 'BRK'),
]
print("\n### Skip rules (removal only)\n")
print("| Rule | " + " | ".join(f"{name}: kept, win, PF, net" for name, _ in sets) + " |")
print("|---|" + "---|" * len(sets))
for label, pred in rules:
    print(f"| {label} | " + " | ".join(cell([t for t in trs if not pred(t)]) for _, trs in sets) + " |")

# Dependence on best trades, deep
ordered = sorted(deep, key=lambda t: -t['net'])
print("\n### Whole sample: without the best N trades\n")
for n in [0, 5, 10, 20, 50]:
    s = R.stats(ordered[n:]); print(f"- without best {n}: net {s['net']:,.0f}, PF {R.pf_str(s['pf'])}")
print("\n### Whole sample: ten best trades\n")
for t in ordered[:10]:
    print(f"- #{t['n']} {t['entry_time']:%Y-%m-%d %H:%M} {t['tag']} {t['exit']} {t['pts']:.0f} pts {t['net']:,.0f} USD, run-up {t['mfe']:.0f}, bars {t['bars']}")
days = R.group(deep, lambda t: t['entry_time'].strftime('%Y-%m-%d %a'))
dnet = {d: sum(t['net'] for t in v) for d, v in days.items()}
order = sorted(dnet, key=lambda d: dnet[d])
print(f"\n### Whole sample days: {len(days)} traded, {sum(1 for d in dnet if dnet[d] > 0)} positive; worst 8:\n")
for d in order[:8]:
    print(f"- {d}: {len(days[d])} trades, {dnet[d]:,.0f}")
print("\nwithout worst N days: " + ", ".join(f"{n}: {sum(dnet[d] for d in order[n:]):,.0f}" for n in [0, 5, 10, 20]))
