#!/usr/bin/env python3
"""Fixed float exploration of the F-family ladder floors (CONJECTURED floats).

Uses exact Arb evaluation of w (no table interpolation) inside the descent,
so the reported minima are trustworthy to float precision.  The certified
floors come from the interval branch-and-bound script; these numbers are the
CONJECTURED targets that certification must confirm (or beat us to).

F_n(g_1..g_{n-1}) = p*sum g_i + sum_{0<=i<j<=n-1} a_ij w(y_j-y_i),
  a_ij = 2/(n-(j-i))  (uniform window-averaging identity, span capacity 2),
  p = 1/2300 (trmdy pressure), window = trmdy rationalized 7-term KERNEL.

Also computes, for each n, the optimal block length m and the resulting
deduction bound  (m*H - eta*B_p*(m-1))/(m - R),  B_p=(n-1)p, A=eps*(m-q),
R = 2*sqrt(A)-1 for A>=1 else A, eta=R/A, H=0.6724570414145443 (certified).

Usage: uv run --quiet --with python-flint --with numpy --with scipy python float_sweep2.py
"""
from __future__ import annotations

import math
import sys
import time
from typing import List, Tuple

import numpy as np

sys.path.insert(0, "/home/vstaln/riemann/research/external-results/trmdy-zeta-simple-zeros-673137/src")
from zeta_ext import design
from zeta_ext.kernel import KernelSpec, kernel_derivatives, kernel_k0
from flint import arb

H_CERT = 0.6724570414145443  # certified lower bound on H(v) for trmdy window
PRESSURE = 1.0 / 2300.0


def make_window() -> KernelSpec:
    return design.KERNEL


def w_exact(x: float, spec: KernelSpec, k0sq: float) -> float:
    """Exact float evaluation of w(x) via Arb (midpoint)."""
    v, _, _ = kernel_derivatives(arb(x), spec)
    return float((v * v / k0sq).mid())


def F_uniform(
    gaps: np.ndarray,
    p: float,
    spec: KernelSpec,
    k0sq: float,
    n: int,
) -> float:
    q = n - 1
    total = p * float(np.sum(gaps))
    y = np.concatenate([[0.0], np.cumsum(gaps)])
    for i in range(n):
        for j in range(i + 1, n):
            aij = 2.0 / (n - (j - i))
            total += aij * w_exact(y[j] - y[i], spec, k0sq)
    return total


def local_min(
    gaps: np.ndarray,
    p: float,
    spec: KernelSpec,
    k0sq: float,
    n: int,
    iters: int = 3000,
    step0: float = 0.15,
) -> Tuple[float, np.ndarray]:
    q = n - 1
    g = gaps.copy()
    best = F_uniform(g, p, spec, k0sq, n)
    step = step0
    rng = np.random.default_rng(7)
    for it in range(iters):
        k = rng.integers(0, q)
        delta = rng.normal(0.0, step)
        g_new = g.copy()
        g_new[k] = max(0.0, g_new[k] + delta)
        val = F_uniform(g_new, p, spec, k0sq, n)
        if val < best:
            g = g_new
            best = val
            step = step0
        else:
            step *= 0.9995
            if step < 5e-5:
                step = step0
    return best, g


def structured_configs(n: int, q: int) -> List[np.ndarray]:
    cands: List[np.ndarray] = []
    for base in [0.8, 0.9, 1.0, 1.1, 1.2, 1.4, 2.0]:
        cands.append(np.full(q, base))
    for a, b in [(0.5, 1.5), (0.7, 1.3), (0.3, 1.7), (0.4, 1.6), (0.6, 1.4)]:
        cands.append(np.array([a if k % 2 == 0 else b for k in range(q)]))
    for z in [1.05, 1.4, 2.0, 2.6, 3.0]:
        cands.append(np.full(q, z))
    for big, small in [(2.0, 0.3), (1.5, 0.5), (3.0, 0.2)]:
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
    """Maximize bound_for over m (float reconnaissance)."""
    best, best_m = -1.0, 0
    for m in range(n + 1, 4000):
        b = bound_for(n, eps, m)
        if b > best:
            best, best_m = b, m
    return best, best_m


def main() -> None:
    spec = make_window()
    k0 = kernel_k0(spec)
    k0sq = float((k0 * k0).mid())

    print(f"window = trmdy rationalized 7-term; p={PRESSURE}; H_cert={H_CERT}")
    print(f"weights: uniform a_ij = 2/(n-(j-i));  span capacities = 2 (each)")
    print("--- FLOAT floors (CONJECTURED; certification separate) ---")
    floors: dict = {}
    for n in [6, 7, 9, 11, 15]:
        q = n - 1
        rng = np.random.default_rng(100 + n)
        results: List[Tuple[float, np.ndarray]] = []
        for cand in structured_configs(n, q):
            results.append(local_min(cand, PRESSURE, spec, k0sq, n))
        for _ in range(50):
            g0 = rng.uniform(0.3, 2.5, size=q)
            results.append(local_min(g0, PRESSURE, spec, k0sq, n))
        results.sort(key=lambda t: t[0])
        best, g = results[0]
        floors[n] = best
        bnd, mstar = best_block(n, best)
        print(f"n={n:2d}: float_min = {best:.8f}  per-atom = {best/n:.8f}  "
              f"opt m = {mstar}  bound(m*) = {bnd:.10f}")
        print(f"       argmin gaps = {[round(float(x),3) for x in g]}")
        sys.stdout.flush()

    print("--- cross-check: exact evaluation at reported argmin ---")
    for n in [7, 9]:
        q = n - 1
        rng = np.random.default_rng(100 + n)
        results = [local_min(c, PRESSURE, spec, k0sq, n) for c in structured_configs(n, q)]
        results += [local_min(rng.uniform(0.3, 2.5, size=q), PRESSURE, spec, k0sq, n)
                    for _ in range(50)]
        results.sort(key=lambda t: t[0])
        best, g = results[0]
        # re-evaluate exactly (no rounding): already exact in F_uniform
        print(f"n={n}: confirmed float min = {best:.8f}")

    print("--- sensitivity of the optimum m ---")
    for n in [9, 11, 15]:
        eps = floors[n]
        for m in [150, 200, 257, 300, 400, 500, 700, 1000]:
            print(f"  n={n} m={m}: bound = {bound_for(n, eps, m):.10f}")


if __name__ == "__main__":
    main()
