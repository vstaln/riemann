#!/usr/bin/env python3
"""Calibrate the proxy against the real verifier. Uses flint arb to replicate
verify()'s box_lower exactly at given 6-gap configs (in grid units), plus
a dense-ish random scan of the box to find the empirical min of F for the
default weights. Prints F at the 'failing terminal box' seeds."""
import sys, math
import numpy as np
from flint import arb, fmpq

sys.path.insert(0, "/root/riemann/tools/beat673/sweep_proxy")
from common import Ker, default_weights, PAIRS, P

GRID = 4000
ALPHA_NUM, ALPHA_DEN = 149, 100
P_NUM, P_DEN = 1, 1320


def F_arb(gaps_units):
    """Replicate box_lower with arb for a terminal (single-cell) box."""
    ctx_prec = 192
    from flint import ctx
    ctx.prec = 192
    alpha = arb(fmpq(ALPHA_NUM, ALPHA_DEN))
    a = alpha / 2
    k0 = a.sinc()
    weight = {}
    for (i, j), v in default_weights().items():
        weight[(i, j)] = arb(fmpq(int(round(v * 7)), 7))  # not exact; use below
    # exact default weights
    weight = {}
    for (i, j) in PAIRS:
        s = j - i
        weight[(i, j)] = arb(fmpq(2, 7 - s))
    pressure = arb(fmpq(P_NUM, P_DEN))
    low_prefix = [arb(0)]
    for gi in gaps_units:
        low_prefix.append(low_prefix[-1] + arb(fmpq(int(gi), GRID)))
    result = pressure * low_prefix[-1]
    for (i, j) in PAIRS:
        span = j - i
        left = low_prefix[j] - low_prefix[i]
        # kernel at the separation (float via mpmath inside arb is not needed;
        # use the exact midpoint separation)
        sep = fmpq(int(gaps_units[i + 1] if False else 0), 1)
        # separation in units: sum of gaps i+1..j (grid units / GRID)
        sep_q = fmpq(sum(int(gaps_units[k]) for k in range(i, j)), GRID)
        z1 = arb.pi() * arb(sep_q) - a
        z2 = arb.pi() * arb(sep_q) + a
        k = (z1.sinc() + z2.sinc()) / (2 * k0)
        w = k * k / (k0 * k0)
        result += weight[(i, j)] * w
    return float(result.lower())


def F_float_units(gaps_units):
    """Float proxy at gaps given in grid units /4000."""
    ker = Ker()
    w = default_weights()
    g = np.array(gaps_units, dtype=float) / GRID
    y = [0.0]
    for gi in g:
        y.append(y[-1] + gi)
    total = P * float(g.sum())
    for i, j in PAIRS:
        total += w[(i, j)] * ker.w(y[j] - y[i])
    return total


def main():
    seeds = [
        [4207, 7951, 7939, 4188, 7896, 4204],
        [4201, 7972, 7967, 4186, 7947, 4222],
        [4212, 7964, 7936, 4188, 7897, 4200],
        [4208, 7948, 7947, 4186, 7896, 4204],
    ]
    for sd in seeds:
        print(f"seed {sd}: arb F={F_arb(sd):.10f}  float F={F_float_units(sd):.10f}")
    # random scan over the box [0, 11*grid]^6 for the default weights
    rng = np.random.default_rng(3)
    best = math.inf
    best_g = None
    for _ in range(4000):
        g = rng.uniform(0.0, 11 * GRID, 6)
        v = F_float_units(g)
        if v < best:
            best, best_g = v, g
    print(f"random-scan min (float) = {best:.10f} at {[round(x/GRID,3) for x in best_g]}")
    print(f"gap to 8065e-6 = {best - 8065e-6:+.3e}")


if __name__ == "__main__":
    main()
