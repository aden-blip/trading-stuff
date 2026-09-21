#!/usr/bin/env python3
"""Trade-list report for L2L.

Reads a TradingView Strategy Tester export (list of trades, CSV, two rows per trade) made
with M4 v0.5 or later, where every entry carries the order comment
"REV|BRK <zone codes> s<score> k<stack> h<history> <window>" and every exit says T1, stop or
flat. Prints markdown tables: breakdowns by setup, window, stack, score, history, level
family and code, direction, hour, weekday, exit reason, month; the run-up and drawdown
distributions; and what-if tables (tighter target, tighter stop, one contract off at a
run-up, breakeven stop) computed from each trade's run-up and drawdown.

Usage:  python3 tools/trade_list_report.py <export.csv> [--pointvalue 2]

Times are the chart's time zone (Central for the owner's charts). Excursions in the export
are gross of one commission side; the script adds it back. Money figures are for the
exported position size (2 contracts by default); points are per contract.
"""
import argparse
import collections
import csv
import datetime as dt
import re
import statistics

TAG = re.compile(r"^(REV|BRK) (\S+) s(\d+) k(\d+) h(\d+) (\S+)$")
FAMILY = {}
for codes, fam in [
    (["PDH", "PDL", "PDM", "DO", "MO"], "Daily"),
    (["PWH", "PWL", "PWM", "WO"], "Weekly"),
    (["PMH", "PML", "PMM", "MOO"], "Monthly"),
    (["PQH", "PQL", "PQM", "QO", "YH", "YL", "YM", "YO"], "Quarter/Year"),
    (["P4H", "P4L", "P4M", "P4O", "4HO"], "4-hour"),
    (["MNH", "MNL", "MNM"], "Monday"),
    (["AH", "AL", "AO"], "Asia"),
    (["LH", "LL", "LO"], "London"),
    (["NH", "NL", "NO"], "New York"),
    (["HOD", "LOD"], "Day high/low"),
]:
    for c in codes:
        FAMILY[c] = fam
HIST = {12: "first test", 6: "touched", 15: "held", 3: "broke"}


def family(code):
    if code in FAMILY:
        return FAMILY[code]
    if code.startswith("PV"):
        return "Pivot"
    if code == "SR":
        return "S/R"
    return "Custom" if code else "?"


def parse_time(s):
    return dt.datetime.strptime(s, "%Y-%m-%d %H:%M")


def load(path, pointvalue):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    trades = {}
    for r in rows:
        n = int(r["Trade number"])
        t = trades.setdefault(n, {"n": n})
        typ = r["Type"]
        if typ.startswith("Entry"):
            t["dir"] = 1 if "long" in typ else -1
            t["entry_time"] = parse_time(r["Date and time"])
            t["tag"] = r["Signal"]
            t["entry_px"] = float(r["Price USD"])
        else:
            t["exit_time"] = parse_time(r["Date and time"])
            t["exit"] = r["Signal"]
            t["exit_px"] = float(r["Price USD"])
        t["qty"] = float(r["Size (qty)"])
        t["net"] = float(r["Net PnL USD"])
        t["comm"] = float(r["Commission USD"])
        t["mfe_usd"] = float(r["Favorable excursion USD"])
        t["mae_usd"] = float(r["Adverse excursion USD"])
        t["bars"] = int(r["Duration (bars)"])
    out = []
    for n in sorted(trades):
        t = trades[n]
        m = TAG.match(t["tag"])
        if not m:
            raise SystemExit(f"trade {n}: unreadable tag {t['tag']!r}")
        t["setup"], zone, sc, k, h, w = m.groups()
        t["zone"] = zone
        t["codes"] = [c for c in zone.split("+") if c]
        t["score"], t["stack"], t["hist"] = int(sc), int(k), int(h)
        t["window"] = w
        usd_per_pt = t["qty"] * pointvalue
        t["usd_per_pt"] = usd_per_pt
        t["gross"] = t["net"] + t["comm"]
        t["pts"] = t["gross"] / usd_per_pt
        half = t["comm"] / 2.0
        t["mfe"] = max(0.0, (t["mfe_usd"] + half) / usd_per_pt)
        t["mae"] = max(0.0, (-t["mae_usd"] + half) / usd_per_pt) if t["mae_usd"] < 0 else 0.0
        t["month"] = t["entry_time"].strftime("%Y-%m")
        t["week"] = t["entry_time"].strftime("%G-W%V")
        t["hour"] = t["entry_time"].hour
        t["wday"] = t["entry_time"].strftime("%a")
        out.append(t)
    return out


def stats(trs, key="net"):
    n = len(trs)
    if n == 0:
        return None
    vals = [t[key] for t in trs]
    wins = [v for v in vals if v > 0]
    losses = [v for v in vals if v <= 0]
    gp, gl = sum(wins), -sum(losses)
    net = gp - gl
    pf = gp / gl if gl > 0 else float("inf")
    pts = sum(t["pts"] for t in trs) / n if key == "net" else None
    return dict(n=n, win=100.0 * len(wins) / n, pf=pf, net=net, avg=net / n, pts=pts,
                avgwin=(gp / len(wins)) if wins else 0.0, avgloss=(gl / len(losses)) if losses else 0.0)


def pf_str(pf):
    return "inf" if pf == float("inf") else f"{pf:.2f}"


def table(title, groups, order=None, min_n=1, note=None):
    print(f"\n### {title}\n")
    if note:
        print(note + "\n")
    print("| Group | Trades | Win % | PF | Net USD | USD/trade | Pts/trade | Avg win | Avg loss |")
    print("|---|---|---|---|---|---|---|---|---|")
    keys = order if order is not None else sorted(groups)
    for k in keys:
        if k not in groups:
            continue
        s = stats(groups[k])
        if s is None or s["n"] < min_n:
            continue
        print(f"| {k} | {s['n']} | {s['win']:.1f} | {pf_str(s['pf'])} | {s['net']:,.0f} | {s['avg']:.1f} | {s['pts']:.1f} | {s['avgwin']:.0f} | {s['avgloss']:.0f} |")


def group(trs, fn):
    g = collections.defaultdict(list)
    for t in trs:
        g[fn(t)].append(t)
    return g


def drawdown(vals):
    peak = cum = 0.0
    dd = 0.0
    for v in vals:
        cum += v
        peak = max(peak, cum)
        dd = max(dd, peak - cum)
    return dd


def sim_table(title, trs, variants, note=None):
    """variants: list of (label, fn) where fn(t) -> new net USD for the trade."""
    print(f"\n### {title}\n")
    if note:
        print(note + "\n")
    print("| Variant | Trades changed | Win % | PF | Net USD | USD/trade | Closed-trade max DD |")
    print("|---|---|---|---|---|---|---|")
    base = [t["net"] for t in trs]
    s = stats(trs)
    print(f"| as traded | 0 | {s['win']:.1f} | {pf_str(s['pf'])} | {s['net']:,.0f} | {s['avg']:.1f} | {drawdown(base):,.0f} |")
    for label, fn in variants:
        new = [fn(t) for t in trs]
        changed = sum(1 for a, b in zip(base, new) if abs(a - b) > 0.005)
        fake = [dict(net=v, pts=0.0) for v in new]
        s = stats(fake)
        print(f"| {label} | {changed} | {s['win']:.1f} | {pf_str(s['pf'])} | {s['net']:,.0f} | {s['avg']:.1f} | {drawdown(new):,.0f} |")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--pointvalue", type=float, default=2.0, help="USD per point per contract (MNQ 2)")
    ap.add_argument("--slip", type=float, default=0.5, help="slippage per market/stop fill, points (2 ticks on MNQ)")
    a = ap.parse_args()
    trs = load(a.path, a.pointvalue)
    slip = a.slip
    qty = trs[0]["qty"]
    upp = trs[0]["usd_per_pt"]
    comm = trs[0]["comm"]

    s = stats(trs)
    first, last = trs[0]["entry_time"], trs[-1]["exit_time"]
    print(f"# Trade-list report\n")
    print(f"File: {a.path}")
    print(f"Trades: {s['n']}, {first:%Y-%m-%d %H:%M} to {last:%Y-%m-%d %H:%M}, size {qty:g}, {upp:g} USD per point, commission {comm:.2f} a round trip.")
    print(f"Win {s['win']:.2f} %, PF {pf_str(s['pf'])}, net {s['net']:,.2f} USD, {s['avg']:.2f} USD a trade, {s['pts']:.2f} points a trade per contract.")
    print(f"Avg win {s['avgwin']:.2f} USD, avg loss {s['avgloss']:.2f} USD, closed-trade max drawdown {drawdown([t['net'] for t in trs]):,.2f} USD.")
    stops = [t for t in trs if t["exit"] == "stop"]
    t1s = [t for t in trs if t["exit"] == "T1"]
    if stops:
        print(f"Median stop-out loss {statistics.median(-t['pts'] for t in stops):.1f} points, mean {statistics.mean(-t['pts'] for t in stops):.1f}.")
    if t1s:
        print(f"Median T1 win {statistics.median(t['pts'] for t in t1s):.1f} points, mean {statistics.mean(t['pts'] for t in t1s):.1f}.")
    hold = [t["bars"] for t in trs]
    print(f"Hold: median {statistics.median(hold):.0f} bars, mean {statistics.mean(hold):.1f}; winners median {statistics.median([t['bars'] for t in trs if t['net'] > 0]):.0f}, losers median {statistics.median([t['bars'] for t in trs if t['net'] <= 0]):.0f}.")

    table("By exit reason", group(trs, lambda t: t["exit"]), ["T1", "stop", "flat"])
    table("By setup", group(trs, lambda t: t["setup"]), ["REV", "BRK"])
    table("By direction", group(trs, lambda t: "long" if t["dir"] > 0 else "short"), ["long", "short"])
    table("By window (script's tag)", group(trs, lambda t: t["window"]), ["ASIA", "LON", "NY", "OTH"])
    table("By setup and window", group(trs, lambda t: f"{t['setup']} {t['window']}"))
    table("By stack (levels in the zone)", group(trs, lambda t: f"k{t['stack']}" if t["stack"] < 3 else "k3+"), ["k1", "k2", "k3+"])
    table("By score", group(trs, lambda t: f"s{t['score'] // 10 * 10}-{t['score'] // 10 * 10 + 9}"))
    table("By level history", group(trs, lambda t: f"h{t['hist']} {HIST.get(t['hist'], '?')}"))
    table("By level history and setup", group(trs, lambda t: f"{t['setup']} h{t['hist']} {HIST.get(t['hist'], '?')}"))
    table("By hour of entry (chart time)", group(trs, lambda t: f"{t['hour']:02d}:00"))
    table("By weekday of entry", group(trs, lambda t: t["wday"]), ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri"])
    table("By month of entry", group(trs, lambda t: t["month"]))
    table("By week of entry", group(trs, lambda t: t["week"]))

    fam = collections.defaultdict(list)
    code = collections.defaultdict(list)
    for t in trs:
        fams = set()
        for c in t["codes"]:
            code[c].append(t)
            fams.add(family(c))
        for f in fams:
            fam[f].append(t)
    table("By level family (a trade counts once per family in its zone)", fam)
    table("By level code (a trade counts once per code in its zone)", code, order=sorted(code, key=lambda c: -stats(code[c])["net"]), min_n=5)
    single = [t for t in trs if t["stack"] == 1]
    table("Single-level zones by code (clean attribution)", group(single, lambda t: t["codes"][0]),
          order=sorted({t["codes"][0] for t in single}, key=lambda c: -stats([t for t in single if t["codes"][0] == c])["net"]), min_n=5)

    # Retries: same zone, same direction, previous attempt lost and exited within 120 minutes before this entry.
    last_by_zone = {}
    for t in trs:
        key = (t["zone"], t["dir"])
        prev = last_by_zone.get(key)
        t["retry"] = bool(prev and prev["net"] <= 0 and 0 <= (t["entry_time"] - prev["exit_time"]).total_seconds() <= 120 * 60)
        last_by_zone[key] = t
    table("Retries (same zone and direction within 2 hours after a losing attempt)", group(trs, lambda t: "retry" if t["retry"] else "first attempt"), ["first attempt", "retry"])

    # Overnight and long holds
    table("Held past a session change (entered 16:00-19:00 or after 23:00 chart time)", group(trs, lambda t: "evening entry" if (16 <= t["hour"] < 19 or t["hour"] >= 23) else "other"), ["evening entry", "other"])

    # Excursions
    losers = [t for t in trs if t["net"] <= 0]
    winners = [t for t in trs if t["net"] > 0]
    print("\n### Run-up before the loss (losing trades: how far they went in favour first)\n")
    print("| Reached at least (pts) | Losing trades | Share of losers | Their net USD |")
    print("|---|---|---|---|")
    for x in [5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150]:
        sub = [t for t in losers if t["mfe"] >= x]
        print(f"| {x} | {len(sub)} | {100.0 * len(sub) / max(1, len(losers)):.0f} % | {sum(t['net'] for t in sub):,.0f} |")
    print("\n### Run-up relative to the stop (stop-outs only; stop distance taken as the loss)\n")
    print("| Reached at least | Stop-outs | Share |")
    print("|---|---|---|")
    for r in [0.25, 0.5, 0.75, 1.0, 1.5, 2.0]:
        sub = [t for t in stops if t["mae"] > 0 and t["mfe"] >= r * t["mae"]]
        print(f"| {r:.2f} x stop | {len(sub)} | {100.0 * len(sub) / max(1, len(stops)):.0f} % |")
    print("\n### Drawdown before the win (winning trades: how far against them first)\n")
    print("| Went against by at least (pts) | Winning trades | Share of winners | Their net USD |")
    print("|---|---|---|---|")
    for x in [5, 10, 15, 20, 25, 30, 40, 50, 75]:
        sub = [t for t in winners if t["mae"] >= x]
        print(f"| {x} | {len(sub)} | {100.0 * len(sub) / max(1, len(winners)):.0f} % | {sum(t['net'] for t in sub):,.0f} |")

    # What-ifs
    def tighter_target(y):
        return lambda t: (y * upp - comm) if t["mfe"] >= y else t["net"]

    def tighter_stop(sd):
        return lambda t: (-(sd + slip) * upp - comm) if t["mae"] >= sd else t["net"]

    def partial(x):
        # one contract off at +x (limit, no slippage), the other keeps the actual result
        return lambda t: (x * a.pointvalue + t["pts"] * a.pointvalue * (qty - 1) - comm) if t["mfe"] >= x else t["net"]

    def breakeven(x):
        # after +x both contracts get a stop at entry; a trade that later lost is assumed to have come
        # back through entry (it did, it ended below it); winners are assumed not to have (best case)
        return lambda t: (-slip * upp - comm) if (t["mfe"] >= x and t["net"] <= 0) else t["net"]

    def partial_be(x):
        return lambda t: (x * a.pointvalue + (t["pts"] if t["net"] > 0 else -slip) * a.pointvalue * (qty - 1) - comm) if t["mfe"] >= x else t["net"]

    sim_table("What if the target were closer (all trades that reached it take it)", trs,
              [(f"target {y} pts", tighter_target(y)) for y in [20, 30, 40, 50, 60, 80, 100, 120, 150]],
              note="Exact: a trade whose run-up reached the target would have filled there before whatever it did next.")
    sim_table("What if the stop were tighter (every trade that went against by that much is stopped)", trs,
              [(f"stop {sd} pts", tighter_stop(sd)) for sd in [10, 15, 20, 25, 30, 40, 50]],
              note="Exact for the trades it stops; it cannot add what a saved trade would have done next.")
    sim_table(f"What if one contract came off at a run-up (the other rides as traded)", trs,
              [(f"half off at +{x} pts", partial(x)) for x in [10, 15, 20, 25, 30, 40, 50, 75]],
              note="Exact for the first contract; the second keeps the actual exit.")
    sim_table("What if the stop moved to entry after a run-up (both contracts)", trs,
              [(f"breakeven after +{x} pts", breakeven(x)) for x in [10, 15, 20, 25, 30, 40, 50, 75]],
              note="Best case: losers that had reached the run-up are taken as scratched (they did come back through entry); winners are assumed never to have come back to entry after the run-up, which the export cannot show.")
    sim_table("What if one contract came off at a run-up and the stop on the other moved to entry", trs,
              [(f"half off at +{x}, runner to breakeven", partial_be(x)) for x in [10, 15, 20, 25, 30, 40, 50, 75]],
              note="Same best-case assumption for the runner on winning trades.")

    table("By level history and window", group(trs, lambda t: f"h{t['hist']} {HIST.get(t['hist'], '?')} {t['window']}"))
    table("By level history and stack", group(trs, lambda t: f"h{t['hist']} {HIST.get(t['hist'], '?')} " + (f"k{t['stack']}" if t["stack"] < 3 else "k3+")))

    # Stop-out and target sizes
    print("\n### Stop-outs by size (points lost per contract)\n")
    print("| Size | Stop-outs | Share | USD lost | Ran up first by 0.5x the stop |")
    print("|---|---|---|---|---|")
    for lo, hi in [(0, 25), (25, 50), (50, 75), (75, 100), (100, 150), (150, 999)]:
        sub = [t for t in stops if lo <= -t["pts"] < hi]
        ran = sum(1 for t in sub if t["mfe"] >= 0.5 * t["mae"])
        print(f"| {lo}-{hi if hi < 999 else ''} | {len(sub)} | {100.0 * len(sub) / max(1, len(stops)):.0f} % | {sum(t['net'] for t in sub):,.0f} | {ran} |")
    print("\n### Target exits by size (points won per contract)\n")
    print("| Size | T1 exits | Share | USD won |")
    print("|---|---|---|---|")
    for lo, hi in [(0, 50), (50, 100), (100, 150), (150, 200), (200, 300), (300, 999)]:
        sub = [t for t in t1s if lo <= t["pts"] < hi]
        print(f"| {lo}-{hi if hi < 999 else ''} | {len(sub)} | {100.0 * len(sub) / max(1, len(t1s)):.0f} % | {sum(t['net'] for t in sub):,.0f} |")

    # Days
    days = group(trs, lambda t: t["entry_time"].strftime("%Y-%m-%d %a"))
    dnet = {d: sum(t["net"] for t in v) for d, v in days.items()}
    order = sorted(dnet, key=lambda d: dnet[d])
    print(f"\n### Days\n\n{len(days)} days with a trade; {sum(1 for d in dnet if dnet[d] > 0)} positive, {sum(1 for d in dnet if dnet[d] <= 0)} not.\n")
    print("| Worst days | Trades | Net USD | Losses in a row at most |")
    print("|---|---|---|---|")
    for d in order[:8]:
        v = days[d]
        run = best = 0
        for t in v:
            run = run + 1 if t["net"] <= 0 else 0
            best = max(best, run)
        print(f"| {d} | {len(v)} | {dnet[d]:,.0f} | {best} |")
    print("\n| Best days | Trades | Net USD |")
    print("|---|---|---|")
    for d in order[-5:][::-1]:
        print(f"| {d} | {len(days[d])} | {dnet[d]:,.0f} |")
    print("\n| Without the worst N days | Net USD |")
    print("|---|---|")
    for n in [0, 3, 5, 10]:
        print(f"| {n} | {sum(dnet[d] for d in order[n:]):,.0f} |")

    # Daily loss cap (removal only: the trades that would have replaced skipped ones are unknown)
    print("\n### What if trading stopped for the day after N losing trades (calendar day, chart time)\n")
    print("Removal only: a skipped trade frees the strategy to take another one the export cannot show.\n")
    print("| Cap | Trades kept | Win % | PF | Net USD | USD/trade | Closed-trade max DD |")
    print("|---|---|---|---|---|---|---|")
    for n in [0, 1, 2, 3, 4, 5]:
        kept = []
        for d in sorted(days):
            losses = 0
            for t in days[d]:
                if n and losses >= n:
                    continue
                kept.append(t)
                if t["net"] <= 0:
                    losses += 1
        kept.sort(key=lambda t: t["n"])
        st = stats(kept)
        print(f"| {'none' if n == 0 else n} | {st['n']} | {st['win']:.1f} | {pf_str(st['pf'])} | {st['net']:,.0f} | {st['avg']:.1f} | {drawdown([t['net'] for t in kept]):,.0f} |")

    # Removal what-ifs chosen after looking at this sample
    rules = [
        ("skip retries", lambda t: t["retry"]),
        ("skip touched-today levels (h6)", lambda t: t["hist"] == 6),
        ("skip zones with a 4-hour open (4HO or P4O)", lambda t: "4HO" in t["codes"] or "P4O" in t["codes"]),
        ("skip the 08:00 and 17:00-18:59 hours", lambda t: t["hour"] in (8, 17, 18)),
        ("skip scores 80 and up", lambda t: t["score"] >= 80),
        ("skip the London window", lambda t: t["window"] == "LON"),
    ]
    print("\n### What if these trades were skipped (chosen after reading this sample; the long sample must confirm each)\n")
    print("Removal only, as above. Each rule alone, then all together.\n")
    print("| Rule | Trades skipped | Trades kept | Win % | PF | Net USD | USD/trade | Closed-trade max DD |")
    print("|---|---|---|---|---|---|---|---|")
    def show(label, pred):
        kept = [t for t in trs if not pred(t)]
        st = stats(kept)
        print(f"| {label} | {len(trs) - len(kept)} | {st['n']} | {st['win']:.1f} | {pf_str(st['pf'])} | {st['net']:,.0f} | {st['avg']:.1f} | {drawdown([t['net'] for t in kept]):,.0f} |")
    for label, pred in rules:
        show(label, pred)
    show("all six together", lambda t: any(pred(t) for _, pred in rules))
    show("history and 4-hour open rules only", lambda t: t["hist"] == 6 or "4HO" in t["codes"] or "P4O" in t["codes"])

    # Dependence on the best trades
    ordered = sorted(trs, key=lambda t: -t["net"])
    print("\n### Dependence on the best trades\n")
    print("| Without the best N trades | Net USD | PF |")
    print("|---|---|---|")
    for n in [0, 1, 3, 5, 10, 20]:
        rest = ordered[n:]
        st = stats(rest)
        print(f"| {n} | {st['net']:,.0f} | {pf_str(st['pf'])} |")
    print("\n### Ten best and ten worst trades\n")
    print("| # | Entry (chart time) | Tag | Exit | Pts | Net USD | Run-up pts | Drawdown pts | Bars |")
    print("|---|---|---|---|---|---|---|---|---|")
    for t in ordered[:10] + ordered[-10:]:
        print(f"| {t['n']} | {t['entry_time']:%Y-%m-%d %H:%M} | {t['tag']} | {t['exit']} | {t['pts']:.1f} | {t['net']:,.0f} | {t['mfe']:.0f} | {t['mae']:.0f} | {t['bars']} |")


if __name__ == "__main__":
    main()
