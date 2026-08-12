#!/usr/bin/env python3
"""Better float floor estimation for the cosine-window coboundary F_B.

Uses many random restarts + Nelder-Mead from the best seeds to get a
reliable float estimate of min F_B over the 6 gap coordinates.  This is a
*guide* for where to certify; the interval verifier is the ground truth.
"""
from __future__ import annotations

import math
import random

import numpy as np

# tawan redistributed coefficients
P = [c / 1_920_000 for c in (946, 1177, 877, 877, 1177, 946)]
Q = [31343 / 100_000, 1 / 3, 105971 / 300_000, 105971 / 300_000, 1 / 3, 31343 / 100_000]
W = {(i, j): 2.0 / (7 - (j - i)) for i in range(7) for j in range(i + 1, 7)}
PAIRS = sorted(W)


def sinc(z):
    return 1.0 if z == 0.0 else math.sin(z) / z


class Ker:
    def __init__(self, alpha):
        self.alpha = alpha
        self.k0 = 2 * math.sin(alpha / 2) / alpha

    def K(self, x):
        a = self.alpha
        z1 = math.pi * x - a / 2
        z2 = math.pi * x + a / 2
        return 0.5 * (sinc(z1) + sinc(z2))

    def w(self, x):
        return (self.K(x) / self.k0) ** 2


def F(g, ker):
    y = [0.0]
    for gi in g:
        y.append(y[-1] + gi)
    total = 0.0
    for i in range(6):
        total += P[i] * g[i] + Q[i] * ker.w(g[i])
    for i, j in PAIRS:
        total += W[(i, j)] * ker.w(y[j] - y[i])
    return total


def nelder_mead(f, x0, iters=3000, step=0.35):
    n = len(x0)
    sim = [np.array(x0, dtype=float)]
    for i in range(n):
        v = np.array(x0, dtype=float)
        v[i] += step
        sim.append(v)
    vals = [f(tuple(s)) for s in sim]
    for _ in range(iters):
        order = np.argsort(vals)
        sim = [sim[i] for i in order]
        vals = [vals[i] for i in order]
        centroid = np.mean(sim[:-1], axis=0)
        # reflection
        xr = centroid + (centroid - sim[-1])
        vr = f(tuple(xr))
        if vals[0] <= vr < vals[-2]:
            sim[-1], vals[-1] = xr, vr
            continue
        if vr < vals[0]:
            xe = centroid + 2 * (xr - centroid)
            ve = f(tuple(xe))
            if ve < vr:
                sim[-1], vals[-1] = xe, ve
            else:
                sim[-1], vals[-1] = xr, vr
            continue
        xc = centroid + 0.5 * (sim[-1] - centroid)
        vc = f(tuple(xc))
        if vc < vals[-1]:
            sim[-1], vals[-1] = xc, vc
        else:
            for i in range(1, n + 1):
                sim[i] = sim[0] + 0.5 * (sim[i] - sim[0])
                vals[i] = f(tuple(sim[i]))
    return vals[0], tuple(sim[0])


def floor_est(alpha, seed=0, restarts=60):
    rng = random.Random(seed)
    ker = Ker(alpha)
    best = float("inf")
    best_pt = None
    # structured seeds around the known pattern (near ~2,2,1,1,2,2-ish and ~1,1,2,2,1,1)
    seeds = [
        (2.0, 2.0, 1.0, 1.0, 2.0, 2.0),
        (1.0, 1.0, 2.0, 2.0, 1.0, 1.0),
        (2.0, 2.0, 2.0, 2.0, 2.0, 2.0),
        (1.05, 1.05, 2.03, 2.03, 1.05, 1.05),
        (1.0, 2.03, 1.0, 1.0, 2.03, 1.0),
        (2.03, 1.0, 1.0, 1.0, 1.0, 2.03),
        (1.5, 1.5, 1.5, 1.5, 1.5, 1.5),
        (1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
    ]
    for s in seeds:
        v = F(s, ker)
        if v < best:
            best, best_pt = v, s
    for _ in range(restarts):
        x0 = tuple(rng.uniform(0, 4) for _ in range(6))
        v, pt = nelder_mead(lambda g: F(g, ker), x0, iters=2500)
        if v < best:
            best, best_pt = v, pt
    return best, best_pt


def main():
    print(f"{'alpha':>6} {'floor~':>10} {'H':>12} {'argmin gaps'}")
    for alpha in [a / 100 for a in range(138, 163, 1)]:
        fl, pt = floor_est(alpha, seed=1, restarts=120)
        a = alpha
        i0 = 2 * math.sin(a / 2) / a
        i2 = 0.5 + math.sin(a) / (2 * a)
        const = math.sin(a / 2) / a + 2 * math.cos(a / 2) / (a * a)
        jv = -2 * i2 / (a * a) + const * i0
        c = i0 * i0 / (i2 + jv)
        H = 2 - 1 / c
        print(f"{alpha:6.2f} {fl:10.6f} {H:12.8f}  {[round(x,3) for x in pt]}")


if __name__ == "__main__":
    main()
