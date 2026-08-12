#!/usr/bin/env python3
"""Float (CONJECTURED) exploration of the F-family ladder floors.

F_n(g_1..g_{n-1}) = p * sum_i g_i  +  sum_{0<=i<j<=n-1} a_ij w(y_j - y_i),
  n points (q = n-1 gaps), a_ij = 2/(n - (j-i))  (window-averaging identity),
  w = (K/K0)^2 for a given KernelSpec, y_j = g_1 + ... + g_j.

We minimize F_n over nonnegative gaps by (a) a global pattern search over
periodic/structured configs and (b) local descent from many random starts,
then report the observed minimum.  This is the FLOAT estimate only -- the
certified floor requires the interval branch-and-bound (separate script).

Usage:
  uv run --quiet --with python-flint --with numpy --with scipy python float_sweep.py
"""
from __future__ import annotations

import math
import sys
import time
from typing import List, Tuple

import numpy as np

sys.path.insert(0, "/home/vstaln/riemann/research/external-results/trmdy-zeta-simple-zeros-673137/src")
from zeta_ext import design
from zeta_ext.kernel import (
    MT_SPEC,
    KernelSpec,
    build_w_lower_table,
    kernel_derivatives,
    kernel_k0,
)

GRID = 4000


def make_window() -> KernelSpec:
    return design.KERNEL


def w_value(x: float, spec: KernelSpec, k0sq: float) -> float:
    """Float evaluation of w(x) = (K(x)/K0)^2 via Arb balls (mid)."""
    from flint import arb

    v, _, _ = kernel_derivatives(arb(x), spec)
    return float((v * v / k0sq).mid())


def F_fn(
    gaps: np.ndarray,
    p: float,
    wtab: np.ndarray,
    n: int,
) -> float:
    """Evaluate F_n for the uniform window-averaging weights a_ij = 2/(n-(j-i))."""
    q = n - 1
    total = p * float(np.sum(gaps))
    y = np.concatenate([[0.0], np.cumsum(gaps)])
    for i in range(n):
        for j in range(i + 1, n):
            span = j - i
            aij = 2.0 / (n - span)
            x = y[j] - y[i]
            total += aij * wtab(x)
    return total


def make_wtab(spec: KernelSpec, k0sq: float, nmax: int = 6.0) -> np.ndarray:
    """Sample w on [0, 6] at fine grid for fast evaluation."""
    xs = np.linspace(0.0, nmax, 40001)
    return np.array([w_value(x, spec, k0sq) for x in xs])


def w_eval(x: float, wtab: np.ndarray, nmax: float) -> float:
    if x < 0.0:
        return wtab[0]
    if x >= nmax:
        return 0.0
    idx = int(x / nmax * (len(wtab) - 1))
    return float(wtab[idx])


def local_min(
    gaps: np.ndarray,
    p: float,
    wtab: np.ndarray,
    n: int,
    nmax: float,
    iters: int = 4000,
    step0: float = 0.2,
) -> Tuple[float, np.ndarray]:
    """Coordinate + stochastic descent to minimize F_n from a start config."""
    q = n - 1
    g = gaps.copy()
    best = F_fn(g, p, lambda x: w_eval(x, wtab, nmax), n)
    step = step0
    rng = np.random.default_rng(42)
    for it in range(iters):
        # pick a coordinate, propose a random move
        k = rng.integers(0, q)
        delta = rng.normal(0.0, step)
        g_new = g.copy()
        g_new[k] = max(0.0, g_new[k] + delta)
        val = F_fn(g_new, p, lambda x: w_eval(x, wtab, nmax), n)
        if val < best:
            g = g_new
            best = val
            step = step0
        else:
            step *= 0.999
            if step < 1e-4:
                step = step0
        if it % 1000 == 0:
            pass
    return best, g


def structured_configs(n: int, q: int):
    """Periodic / structured candidate configurations (gap sequences)."""
    cands: List[np.ndarray] = []
    # near-uniform (zeta-like) gaps around 1
    for base in [0.8, 0.9, 1.0, 1.1, 1.2]:
        cands.append(np.full(q, base))
    # alternating small/large
    for a, b in [(0.5, 1.5), (0.7, 1.3), (0.3, 1.7), (1.0, 1.0), (0.4, 1.6)]:
        arr = np.array([a if k % 2 == 0 else b for k in range(q)])
        cands.append(arr)
    # kernel-zero-like spacing (near-annihilating)
    for z in [1.05, 1.4, 2.0, 2.6, 3.0]:
        cands.append(np.full(q, z))
    # clustered: a few big then small
    for big, small in [(2.0, 0.3), (1.5, 0.5), (3.0, 0.2)]:
        arr = np.array([big if k % 3 == 0 else small for k in range(q)])
        cands.append(arr)
    return cands


def main() -> None:
    spec = make_window()
    k0 = kernel_k0(spec)
    k0sq = float((k0 * k0).mid())
    p = 1.0 / 2300.0
    nmax = 6.0
    wtab = make_wtab(spec, k0sq, nmax)

    print(f"window = trmdy rationalized 7-term; p = {p}; w = (K/K0)^2")
    print(f"k0^2 = {k0sq}")
    for n in [6, 7, 9, 11, 15]:
        q = n - 1
        rng = np.random.default_rng(100 + n)
        results = []
        # structured starts
        for cand in structured_configs(n, q):
            best, g = local_min(cand, p, wtab, n, nmax, iters=2500)
            results.append((best, g))
        # random starts
        for _ in range(60):
            g0 = rng.uniform(0.2, 2.5, size=q)
            best, g = local_min(g0, p, wtab, n, nmax, iters=2500)
            results.append((best, g))
        results.sort(key=lambda t: t[0])
        best, g = results[0]
        print(f"n={n} (q={q}): float_min = {best:.10f}  gaps = "
              f"{[round(float(x), 4) for x in g]}")
        print(f"    per-atom = {best/n:.10f}   target-equivalent A (m=257): "
              f"{best*(257-q):.6f}")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
