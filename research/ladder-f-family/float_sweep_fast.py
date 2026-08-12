#!/usr/bin/env python3
"""Fast float (CONJECTURED) floors for the F-family ladder, n points.

F_n(g) = p*sum g_i + sum_{i<j} a_ij w(y_j-y_i),  a_ij = 2/(n-(j-i)),
p = 1/2300, w = (K/K0)^2 (trmdy rationalized 7-term window kernel).

Descent uses a fine linear-interp table of w (|w''| <= 6e-6 so interpolation
error is ~1e-14 — irrelevant at these magnitudes); every reported minimum is
then RE-EVALUATED exactly via Arb before being recorded.

Usage: uv run --quiet --with python-flint --with numpy --with scipy python float_sweep_fast.py
"""
from __future__ import annotations

import math
import sys
import time
from typing import List, Tuple

import numpy as np

sys.path.insert(0, "/home/vstaln/riemann/research/external-results/trmdy-zeta-simple-zeros-673137/src")
from zeta_ext import design
from zeta_ext.kernel import kernel_derivatives, kernel_k0
from flint import arb

H_CERT = 0.6724570414145443
PRESSURE = 1.0 / 2300.0
NMAX = 6.0
NTAB = 200_001  # 3e-5 grid


def w_exact(x: float, spec, k0sq: float) -> float:
    v, _, _ = kernel_derivatives(arb(x), spec)
    return float((v * v / k0sq).mid())


def build_table(spec, k0sq: float) -> np.ndarray:
    xs = np.linspace(0.0, NMAX, NTAB)
    return np.array([w_exact(x, spec, k0sq) for x in xs])


def w_eval(x: float, tab: np.ndarray) -> float:
    if x < 0.0:
        return float(tab[0])
    if x >= NMAX:
        return 0.0
    pos = x / NMAX * (NTAB - 1)
    i = int(pos)
    if i >= NTAB - 1:
        return float(tab[-1])
    frac = pos - i
    return float(tab[i] * (1.0 - frac) + tab[i + 1] * frac)


def F_uniform(gaps: np.ndarray, p: float, tab: np.ndarray, n: int) -> float:
    total = p * float(np.sum(gaps))
    y = np.concatenate([[0.0], np.cumsum(gaps)])
    for i in range(n):
        for j in range(i + 1, n):
            aij = 2.0 / (n - (j - i))
            total += aij * w_eval(y[j] - y[i], tab)
    return total


def local_min(
    gaps: np.ndarray,
    p: float,
    tab: np.ndarray,
    n: int,
    iters: int = 8000,
    step0: float = 0.15,
) -> Tuple[float, np.ndarray]:
    q = n - 1
    g = gaps.copy()
    best = F_uniform(g, p, tab, n)
    step = step0
    rng = np.random.default_rng(1234)
    for it in range(iters):
        k = rng.integers(0, q)
        delta = rng.normal(0.0, step)
        g_new = g.copy()
        g_new[k] = max(0.0, g_new[k] + delta)
        val = F_uniform(g_new, p, tab, n)
        if val < best:
            g = g_new
            best = val
            step = step0
        else:
            step *= 0.9995
            if step < 1e-4:
                step = step0
    return best, g


def structured_configs(n: int, q: int) -> List[np.ndarray]:
    cands: List[np.ndarray] = []
    for base in [0.8, 0.9, 1.0, 1.03, 1.05, 1.1, 1.2, 1.4, 2.0]:
        cands.append(np.full(q, base))
    for a, b in [(0.5, 1.5), (0.7, 1.3), (1.03, 1.98), (1.05, 1.97), (0.3, 1.7)]:
        cands.append(np.array([a if k % 2 == 0 else b for k in range(q)]))
    for z in [1.05, 1.4, 2.0, 2.6, 3.0]:
        cands.append(np.full(q, z))
    for big, small in [(2.0, 0.3), (1.5, 0.5), (1.98, 1.04)]:
        cands.append(np.array([big if k % 3 == 0 else small for k in range(q)]))
    return cands


def bound_for(n: int, eps: float, m: int) -> float:
    q = n - 1
    B_p = q * PRESSURE
    A = eps * (m - q)
    if A <= 1.0:
        R = A
    else:
        R = 2.0 * math.sqrt(A) - 1.0
    eta = R / A
    return (m * H_CERT - eta * B_p * (m - 1)) / (m - R)


def best_block(n: int, eps: float) -> Tuple[float, int]:
    best, best_m = -1.0, 0
    for m in range(n + 1, 4000):
        b = bound_for(n, eps, m)
        if b > best:
            best, best_m = b, m
    return best, best_m


def main() -> None:
    spec = design.KERNEL
    k0 = kernel_k0(spec)
    k0sq = float((k0 * k0).mid())
    tab = build_table(spec, k0sq)
    print(f"table built: {NTAB} pts on [0,{NMAX}]; w(0)={tab[0]:.6f}")

    floors: dict = {}
    for n in [7, 9, 11, 15]:
        q = n - 1
        rng = np.random.default_rng(100 + n)
        results: List[Tuple[float, np.ndarray]] = []
        for cand in structured_configs(n, q):
            results.append(local_min(cand, PRESSURE, tab, n))
        for _ in range(80):
            g0 = rng.uniform(0.3, 2.6, size=q)
            results.append(local_min(g0, PRESSURE, tab, n))
        results.sort(key=lambda t: t[0])
        best, g = results[0]
        # exact re-evaluation
        best_exact = F_uniform(g, PRESSURE, tab, n)
        # cross-check exact with Arb directly
        y = np.concatenate([[0.0], np.cumsum(g)])
        Fex = PRESSURE * float(np.sum(g))
        for i in range(n):
            for j in range(i + 1, n):
                Fex += (2.0 / (n - (j - i))) * w_exact(y[j] - y[i], spec, k0sq)
        floors[n] = Fex
        bnd, mstar = best_block(n, Fex)
        print(f"n={n:2d}: float_min={Fex:.8f} (interp={best_exact:.8f}) "
              f"per-atom={Fex/n:.8f} opt_m={mstar} bound(m*)={bnd:.10f}")
        print(f"       argmin={[round(float(x),3) for x in g]}")
        sys.stdout.flush()

    print("--- bound(m) sensitivity ---")
    for n in [9, 11, 15]:
        eps = floors[n]
        for m in [100, 150, 200, 257, 300, 400, 600, 900, 1200, 1600, 2000]:
            print(f"  n={n} m={m}: {bound_for(n, eps, m):.10f}")


if __name__ == "__main__":
    main()
