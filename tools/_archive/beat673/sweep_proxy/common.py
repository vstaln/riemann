#!/usr/bin/env python3
"""Weight-profile sweep proxy. Replicates verify_cos7.py's EXACT functional.
The verifier has q=6 free coordinates = the 6 GAPS g_1..g_6 (x_0 = 0,
positions y_k = g_1+...+g_k), and
   F(g) = P * sum(g) + sum_{i<j} a_ij * w_alpha(y_j - y_i)
with box 0 <= g_i <= cutoff where cutoff ~ target/P (one-body cut). Minimize
over the box with multi-start Nelder-Mead. Calibration: default profile floor
should land ~8065e-6 (the certified record).
"""
import math
import numpy as np

ALPHA = 149 / 100
P = 1 / 1320
PAIRS = [(i, j) for i in range(7) for j in range(i + 1, 7)]


def sinc(z):
    return 1.0 if z == 0.0 else math.sin(z) / z


class Ker:
    def __init__(self, alpha=ALPHA):
        self.alpha = alpha
        self.k0 = 2 * math.sin(alpha / 2) / alpha

    def K(self, x):
        a = self.alpha
        z1 = math.pi * x - a / 2
        z2 = math.pi * x + a / 2
        return 0.5 * (sinc(z1) + sinc(z2))

    def w(self, x):
        # verifier: k = K/k0, w = k^2/k0^2 = K^2/k0^4
        return (self.K(x) / (self.k0 * self.k0)) ** 2


def default_weights():
    return {(i, j): 2.0 / (7 - (j - i)) for (i, j) in PAIRS}


def capacity_ok(weights):
    for r in range(1, 7):
        s = sum(weights.get((i, i + r), 0.0) for i in range(0, 7 - r))
        if s > 2.0 + 1e-12:
            return False, (r, s)
    return True, None


def F(g, weights, ker, p=P):
    """g: np.array len 6 (gaps). Positions y = prefix sums, x_0 = 0."""
    y = [0.0]
    for gi in g:
        y.append(y[-1] + gi)
    total = p * float(g.sum())
    for i, j in PAIRS:
        total += weights[(i, j)] * ker.w(y[j] - y[i])
    return total


def floor_min(weights, ker, p=P, gmax=10.8, iters=2500, restarts=24, seed=11,
              anchors=True):
    """Multi-start Nelder-Mead over [0,gmax]^6."""
    rng = np.random.default_rng(seed)
    n = 6
    starts = []
    if anchors:
        base = np.array([1.05, 1.99, 1.98, 1.05, 1.97, 1.05])
        for sc in (0.5, 1.0, 1.5, 2.0):
            starts.append(np.clip(base * sc, 0.05, gmax))
            starts.append(np.clip(np.roll(base, 1) * sc, 0.05, gmax))
        starts.append(np.linspace(0.2, gmax, n))
        starts.append(np.full(n, gmax))
        starts.append(np.full(n, 0.05))
        starts.append(np.array([gmax / 6] * n))
    while len(starts) < restarts:
        u = rng.uniform(0.05, gmax, n)
        starts.append(u)
    best = math.inf
    for s in starts:
        v = _nm_min(s, weights, ker, p, gmax, iters)
        if v < best:
            best = v
    return best


def _nm_min(g0, weights, ker, p, gmax, iters):
    n = len(g0)
    pts = [np.array(g0, dtype=float) for _ in range(n + 1)]
    for k in range(n):
        pts[k + 1][k] += 0.15
        pts[k + 1] = np.clip(pts[k + 1], 0.0, gmax)
    vals = [F(g, weights, ker, p) for g in pts]
    for _ in range(iters):
        order = sorted(range(n + 1), key=lambda i: vals[i])
        worst = order[-1]
        centroid = np.mean([pts[i] for i in order[:-1]], axis=0)
        r = np.clip(centroid + (centroid - pts[worst]), 0.0, gmax)
        vr = F(r, weights, ker, p)
        if vr < vals[order[0]]:
            e = np.clip(centroid + 2 * (centroid - pts[worst]), 0.0, gmax)
            ve = F(e, weights, ker, p)
            pts[worst], vals[worst] = (e, ve) if ve < vr else (r, vr)
        elif vr < vals[order[-2]]:
            pts[worst], vals[worst] = r, vr
        else:
            c = np.clip(centroid + 0.5 * (pts[worst] - centroid), 0.0, gmax)
            vc = F(c, weights, ker, p)
            if vc < vals[worst]:
                pts[worst], vals[worst] = c, vc
            else:
                for i in range(1, n + 1):
                    pts[i] = np.clip(0.5 * (pts[i] + pts[order[0]]), 0.0, gmax)
                    vals[i] = F(pts[i], weights, ker, p)
    return min(vals)


def span_profile_weights(shape_fn, sums=None):
    """a_{i,i+r} = cap * shape_fn(r,i)/sum_i shape_fn(r,i), cap=2 (or sums[r])."""
    w = {}
    for r in range(1, 7):
        n = 7 - r
        raw = [max(shape_fn(r, i), 0.0) for i in range(n)]
        tot = sum(raw)
        cap = sums[r] if sums else 2.0
        if tot <= 0:
            w.update({(i, i + r): 0.0 for i in range(n)})
        else:
            w.update({(i, i + r): cap * raw[i] / tot for i in range(n)})
    return w


if __name__ == "__main__":
    ker = Ker()
    wdef = default_weights()
    ok, viol = capacity_ok(wdef)
    fl = floor_min(wdef, ker)
    print(f"default weights capacity_ok={ok} viol={viol}")
    print(f"default floor min (proxy) = {fl:.10f}")
    print(f"delta vs 8065e-6 = {fl - 8065e-6:+.3e}")
    print(f"delta vs 8066e-6 = {fl - 8066e-6:+.3e}")
