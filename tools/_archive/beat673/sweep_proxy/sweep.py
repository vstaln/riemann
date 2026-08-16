#!/usr/bin/env python3
"""WEIGHT-PROFILE SWEEP (candidate C1): enumerate rational weight profiles in
the capacity box (per-span sums = 2), score with the calibrated proxy floor
(min of the verifier functional over the 6-gap box), keep profiles whose
proxy floor > 8065e-6.

Shapes (n = 7-r entries, i = 0..n-1), each scaled to per-span sum 2:
  flat, ramp_up(t), ramp_dn(t), peak(c), valley(c), ends(e), center(e)
Applied globally (all spans) and per-span-targeted (span r shaped, rest flat).

Output: ranked table of (proxy_floor, name, weights dict) to /tmp/riemann_sweep/.
"""
import sys, json, math, itertools
import numpy as np

sys.path.insert(0, "/root/riemann/tools/beat673/sweep_proxy")
from common import Ker, floor_min, capacity_ok, default_weights, PAIRS

OUT = "/tmp/riemann_sweep"


def shape_flat(n, i): return 1.0

def shape_ramp_up(t):
    def f(n, i):
        return 1.0 + t * (2 * i / (n - 1) - 1.0) if n > 1 else 1.0
    return f

def shape_ramp_dn(t):
    def f(n, i):
        return 1.0 - t * (2 * i / (n - 1) - 1.0) if n > 1 else 1.0
    return f

def shape_peak(c):
    def f(n, i):
        return 1.0 + c * (1.0 - 2 * abs(i - (n - 1) / 2) / (n - 1)) if n > 1 else 1.0
    return f

def shape_valley(c):
    def f(n, i):
        return 1.0 - c * (1.0 - 2 * abs(i - (n - 1) / 2) / (n - 1)) if n > 1 else 1.0
    return f

def shape_ends(e):
    def f(n, i):
        return 1.0 + e * (1.0 if i in (0, n - 1) else 0.0)
    return f

def shape_center(e):
    def f(n, i):
        mid = (n - 1) / 2
        return 1.0 + e * (1.0 if abs(i - mid) <= 0.51 else 0.0)
    return f


def build(shape_fn, per_span=None):
    """weights from shape_fn(r, i) over all spans; per_span dict overrides."""
    w = {}
    for r in range(1, 7):
        n = 7 - r
        sf = per_span.get(r, shape_fn) if per_span else shape_fn
        raw = [max(sf(n, i), 0.0) for i in range(n)]
        tot = sum(raw)
        if tot <= 0:
            w.update({(i, i + r): 0.0 for i in range(n)})
        else:
            w.update({(i, i + r): 2.0 * raw[i] / tot for i in range(n)})
    return w


def profile_generator():
    """Yield (name, weights) candidates."""
    yield ("default", default_weights())
    # A. global shapes
    for t in (0.5, 1.0):
        yield (f"ramp_up{t}", build(shape_ramp_up(t)))
        yield (f"ramp_dn{t}", build(shape_ramp_dn(t)))
    for c in (0.5, 1.0):
        yield (f"peak{c}", build(shape_peak(c)))
        yield (f"valley{c}", build(shape_valley(c)))
    for e in (0.5, 1.0, 2.0):
        yield (f"ends{e}", build(shape_ends(e)))
        yield (f"center{e}", build(shape_center(e)))
    # B. single-span targeted (span r shaped, others flat)
    span_shapes = {
        "ends": shape_ends(1.0), "ends2": shape_ends(2.0),
        "center": shape_center(1.0), "ramp_up": shape_ramp_up(1.0),
        "ramp_dn": shape_ramp_dn(1.0), "peak": shape_peak(1.0),
    }
    for r in range(1, 7):
        for sname, sfn in span_shapes.items():
            flat = {rr: shape_flat for rr in range(1, 7)}
            flat[r] = sfn
            yield (f"span{r}_{sname}", build(None, per_span=flat))
    # C. span-weighted: scale whole spans (some <2, some at 2) - componentwise
    #    monotonicity says saturating dominates, but check span-1 reduction
    #    (looser one-body box) as a control:
    for red, span in [(0.5, 1), (0.8, 1), (0.5, 2), (0.8, 2)]:
        w = default_weights()
        for i in range(0, 7 - span):
            w[(i, i + span)] *= red
        yield (f"red_span{span}_{red}", w)


def main():
    ker = Ker()
    results = []
    for name, w in profile_generator():
        ok, viol = capacity_ok(w)
        if not ok:
            print(f"{name}: CAPACITY VIOLATION {viol} - skipped", flush=True)
            continue
        fl = floor_min(w, ker, restarts=8, iters=1000, seed=hash(name) % 1000)
        results.append((fl, name, w))
        flag = "***" if fl > 8065e-6 else ""
        print(f"{name}: proxy floor = {fl:.10f}  (delta 8065: {fl-8065e-6:+.2e}, "
              f"8066: {fl-8066e-6:+.2e}) {flag}", flush=True)
    results.sort(reverse=True)
    print("\n=== RANKED ===")
    for fl, name, w in results[:15]:
        print(f"{fl:.10f}  {name}")
    # save top profiles as JSON (rationalized) for the laptop runner
    top = results[:10]
    with open(f"{OUT}/top_profiles.json", "w") as fh:
        json.dump([{"name": name, "floor": fl,
                    "weights": {f"{i},{j}": _to_frac(w[(i, j)])
                                for (i, j) in PAIRS}}
                   for fl, name, w in top], fh, indent=1)
    print(f"\nsaved top profiles -> {OUT}/top_profiles.json")


def _to_frac(v):
    from fractions import Fraction
    return [Fraction(v).limit_denominator(10 ** 6).numerator,
            Fraction(v).limit_denominator(10 ** 6).denominator]


if __name__ == "__main__":
    main()
