#!/usr/bin/env python3
"""Float estimate of the true floor of the UNIFORM 7-point F functional at
(alpha=149/100, p=1/1320) — matching verify_cos7.py exactly:
   F(g) = p*sum(g) + sum_{i<j, span s} (2/(7-s)) * w(y_j - y_i), y prefix sums.
Decides artifact-vs-analytic for eps ~ 0.00806 (the record's certified floor).
"""
import math
import numpy as np
from floor_float import Ker, simplex_min

def F_uniform(g, ker, p):
    y = [0.0]
    for gi in g:
        y.append(y[-1] + gi)
    total = p * g.sum()
    for s in range(1, 7):
        coef = 2.0 / (7 - s)
        for i in range(0, 7 - s):
            total += coef * ker.w(y[i + s] - y[i])
    return total

def main():
    alpha = 149 / 100
    ker = Ker(alpha)
    p = 1 / 1320
    seeds = [
        [4207, 7951, 7939, 4188, 7896, 4204],
        [4201, 7972, 7967, 4186, 7947, 4222],
        [4212, 7964, 7936, 4188, 7897, 4200],
        [4208, 7948, 7947, 4186, 7896, 4204],
    ]
    rng = np.random.default_rng(7)
    best = math.inf
    bg = None
    for si, seed in enumerate(seeds):
        for _ in range(30):
            g0 = np.clip(np.array(seed, dtype=float) / 4000 + rng.uniform(-0.4, 0.4, 6), 0.05, 25)
            v = simplex_min(g0, ker, p, 2000)
            if v < best:
                best, bg = v, g0
    print(f"uniform-F float min = {best:.12f} at g={[round(float(x),5) for x in bg]}")
    print(f"gap to 8060e-6: {8060e-6 - best:+.3e}")
    print(f"gap to 8066e-6: {8066e-6 - best:+.3e}")
    print(f"gap to 8070e-6: {8070e-6 - best:+.3e}")

if __name__ == "__main__":
    main()
