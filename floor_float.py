#!/usr/bin/env python3
"""Float estimate of the true floor of the 7-point uniform F functional at
(alpha=149/100, p=1/1320).  Decides artifact-vs-analytic for eps ~ 0.00806.
Mirror of tools/cert_floor_scan.py F; local restarts seeded at/near the
failing terminal boxes from the interval verifier.
"""
import math, random
import numpy as np

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

def main():
    alpha = 149 / 100
    psum = 6 / 1320          # p total = 1/1320 per gap * 6 gaps... check: p in verifier = 1/1320
    # pressure p in the verifier is fmpq(1,1320) per gap; F = p*sum(g) + weights. Use p=1/1320.
    ker = Ker(alpha)
    # failing terminal boxes (grid units /4000) -> gap guesses
    seeds = [
        [4207/4000, 7951/4000, 7939/4000, 4188/4000, 7896/4000, 4204/4000],
        [4201/4000, 7972/4000, 7967/4000, 4186/4000, 7947/4000, 4222/4000],
        [4208/4000, 7948/4000, 7947/4000, 4186/4000, 7896/4000, 4204/4000],
        [4212/4000, 7964/4000, 7936/4000, 4188/4000, 7897/4000, 4200/4000],
    ]
    rng = np.random.default_rng(7)
    best = math.inf; best_g = None; best_seed = None
    for si, seed in enumerate(seeds):
        for trial in range(25):
            g0 = np.array(seed, dtype=float) + rng.uniform(-0.3, 0.3, 6)
            g0 = np.clip(g0, 0.05, 25)
            # coordinate descent / Nelder-Mead-ish: use scipy-free simplex
            res = simplex_min(g0, ker, p=1/1320, iters=3000)
            if res < best:
                best, best_g, best_seed = res, g0, si
    print(f"alpha={alpha} p=1/1320 float_min_F = {best:.12f}")
    print(f"best_g = {[round(x,6) for x in best_g]} (seed {best_seed})")
    print(f"eps targets: 8060 -> {8060e-6 - best:+.3e}  (min below/above)")
    print(f"             8065 -> {8065e-6 - best:+.3e}")
    print(f"             8070 -> {8070e-6 - best:+.3e}")
    print(f"verdict: {'FLOOR >= 0.00806 (artifact likely)' if best > 8060e-6 else 'FLOOR < 0.00806 (analytic; record near floor)'}")

def simplex_min(g0, ker, p, iters=3000):
    n = len(g0)
    pts = [np.array(g0) for _ in range(n + 1)]
    for k in range(n):
        pts[k + 1][k] += 0.15
    vals = [F(g, ker) + p * g.sum() for g in pts]
    for _ in range(iters):
        order = sorted(range(n + 1), key=lambda i: vals[i])
        worst = order[-1]
        centroid = np.mean([pts[i] for i in order[:-1]], axis=0)
        # reflect
        r = centroid + (centroid - pts[worst])
        r = np.clip(r, 0.05, 25)
        vr = F(r, ker) + p * r.sum()
        if vr < vals[order[0]]:
            e = centroid + 2 * (centroid - pts[worst]); e = np.clip(e, 0.05, 25)
            ve = F(e, ker) + p * e.sum()
            pts[worst], vals[worst] = (e, ve) if ve < vr else (r, vr)
        elif vr < vals[order[-2]]:
            pts[worst], vals[worst] = r, vr
        else:
            c = centroid + 0.5 * (pts[worst] - centroid); c = np.clip(c, 0.05, 25)
            vc = F(c, ker) + p * c.sum()
            if vc < vals[worst]:
                pts[worst], vals[worst] = c, vc
            else:
                for i in range(1, n + 1):
                    pts[i] = 0.5 * (pts[i] + pts[order[0]])
                    vals[i] = F(pts[i], ker) + p * pts[i].sum()
    return min(vals)

if __name__ == "__main__":
    main()
