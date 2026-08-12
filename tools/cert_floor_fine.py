#!/usr/bin/env python3
"""Fine float floor search seeded by interval-verifier terminal cells.

The interval verifier's failing terminal cells reveal candidate points for
the true minimum of F_B.  This script evaluates F_B at high precision at
those patterns across a range of alpha, then refines with Nelder-Mead,
to bracket the TRUE floor (upper bounds from point evaluations, and lower
bounds from the interval verifier where it certifies).
"""
from __future__ import annotations

import math
import random

import mpmath as mp

mp.mp.dps = 40

P = [mp.mpf(c) / 1_920_000 for c in (946, 1177, 877, 877, 1177, 946)]
Q = [mp.mpf(31343) / 100_000, mp.mpf(1) / 3, mp.mpf(105971) / 300_000,
     mp.mpf(105971) / 300_000, mp.mpf(1) / 3, mp.mpf(31343) / 100_000]
W = {(i, j): mp.mpf(2) / (7 - (j - i)) for i in range(7) for j in range(i + 1, 7)}
PAIRS = sorted(W)


def sinc(z):
    return mp.sin(z) / z


def F(g, alpha):
    k0 = 2 * mp.sin(alpha / 2) / alpha
    y = [mp.mpf(0)]
    for gi in g:
        y.append(y[-1] + gi)
    tot = mp.mpf(0)
    for i in range(6):
        tot += P[i] * g[i] + Q[i] * (lambda x: (0.5 * (sinc(mp.pi * x - alpha / 2) + sinc(mp.pi * x + alpha / 2)) / k0) ** 2)(g[i])
    for i, j in PAIRS:
        x = y[j] - y[i]
        tot += W[(i, j)] * (0.5 * (sinc(mp.pi * x - alpha / 2) + sinc(mp.pi * x + alpha / 2)) / k0) ** 2
    return tot


def H(alpha):
    a = alpha
    i0 = 2 * mp.sin(a / 2) / a
    i2 = mp.mpf(1) / 2 + mp.sin(a) / (2 * a)
    const = mp.sin(a / 2) / a + 2 * mp.cos(a / 2) / (a * a)
    jv = -2 * i2 / (a * a) + const * i0
    c = i0 * i0 / (i2 + jv)
    return 2 - 1 / c


# Patterns from interval-verifier terminal cells (failing) at various alpha:
PATTERNS = [
    # alpha 1.42: (2.0121,1.0469,2.0124,2.0019,2.0001,1.0511) F=0.0062237
    (2.0121, 1.0469, 2.0124, 2.0019, 2.0001, 1.0511),
    # alpha 1.50: (2.0139,1.0559,1.9939,2.0039,1.9981,1.0576) F=0.0063514
    (2.0139, 1.0559, 1.9939, 2.0039, 1.9981, 1.0576),
    # alpha 1.55 found pattern
    (2.005, 1.059, 1.996, 2.006, 2.01, 2.018),
    # symmetric variants
    (1.0469, 2.0121, 2.0019, 2.0124, 1.0511, 2.0001),
    (2.005, 1.05, 1.995, 2.005, 2.01, 1.06),
    (1.0, 1.0, 2.0, 2.0, 1.0, 1.0),
    (2.0, 1.0, 2.0, 2.0, 1.0, 2.0),
]


def nelder_mead(f, x0, iters=2000, step=0.2):
    n = len(x0)
    sim = [list(x0)]
    for i in range(n):
        v = list(x0)
        v[i] += step
        sim.append(v)
    vals = [f(tuple(s)) for s in sim]
    for _ in range(iters):
        order = sorted(range(len(sim)), key=lambda k: vals[k])
        sim = [sim[k] for k in order]
        vals = [vals[k] for k in order]
        centroid = [sum(sim[k][i] for k in range(n)) / n for i in range(n)]
        xr = [centroid[i] + (centroid[i] - sim[-1][i]) for i in range(n)]
        vr = f(tuple(xr))
        if vals[0] <= vr < vals[-2]:
            sim[-1], vals[-1] = xr, vr
            continue
        if vr < vals[0]:
            xe = [centroid[i] + 2 * (xr[i] - centroid[i]) for i in range(n)]
            ve = f(tuple(xe))
            if ve < vr:
                sim[-1], vals[-1] = xe, ve
            else:
                sim[-1], vals[-1] = xr, vr
            continue
        xc = [centroid[i] + 0.5 * (sim[-1][i] - centroid[i]) for i in range(n)]
        vc = f(tuple(xc))
        if vc < vals[-1]:
            sim[-1], vals[-1] = xc, vc
        else:
            for i in range(1, n + 1):
                sim[i] = [sim[0][k] + 0.5 * (sim[i][k] - sim[0][k]) for k in range(n)]
                vals[i] = f(tuple(sim[i]))
    return vals[0], tuple(sim[0])


def floor_at(alpha, seed_rng):
    best = None
    best_pt = None
    # seed from patterns
    for s in PATTERNS:
        v = F(s, alpha)
        if best is None or v < best:
            best, best_pt = v, s
    # random restarts refined by NM
    for _ in range(80):
        x0 = tuple(seed_rng.uniform(0, 3.5) for _ in range(6))
        v, pt = nelder_mead(lambda g: F(g, alpha), x0, iters=1200)
        if best is None or v < best:
            best, best_pt = v, pt
    return best, best_pt


def main():
    rng = random.Random(7)
    print(f"{'alpha':>6} {'floorUB~':>12} {'H':>12} {'argmin'}")
    for a in [x / 100 for x in range(140, 162, 1)]:
        alpha = mp.mpf(a) / 1
        alpha_f = float(a)
        fl, pt = floor_at(alpha, rng)
        h = H(alpha)
        print(f"{alpha_f:6.2f} {mp.nstr(fl, 10):>12} {mp.nstr(h, 10):>12}  {[round(float(x),3) for x in pt]}")


if __name__ == "__main__":
    main()
