#!/usr/bin/env python3
"""Screw function g(t) from Suzuki 2606.09096 (1.3) via the (2.2) Lerch expansion.

g even, g(0)=0,
  g(t) = (1/2)|t|log|t| + A|t| + Σ_{n≤e^{|t|}} (Λ(n)/√n)(|t|-log n) + O(t²)
A = (1/2)(log(2π)+γ-1) ≈ 0.707546.

RH ⇔ g is a Krein–Langer screw function. Compact encoding: kernel
  K(t,u)=g(t-u)-g(t)-g(u)  (since g(0)=0)
on mean-zero L²(-a,a). Q_W(v)=⟨G, Dv⟩ so this is not λ_a itself
(G is compact, min eig → 0 even when positive). The check that *can*
refute is a stable negative Nyström eigenvalue past a₂.

Usage: python3 tools/weil_first_prime/screw_kernel.py
"""
from __future__ import annotations

import functools
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe import A2, A3, von_mangoldt_upto  # noqa: E402
from lower_bound import GAMMA, PSI_QUARTER  # noqa: E402

LOGPI = math.log(math.pi)
PSI2 = 1.0 - GAMMA  # ψ(2)=1-γ
A_SUZUKI = 0.5 * (math.log(2.0 * math.pi) + GAMMA - 1.0)


def bernoulli_numbers(m: int) -> list[float]:
    B = [1.0]
    for n in range(1, m + 1):
        s = sum(math.comb(n + 1, k) * B[k] for k in range(n))
        B.append(-s / (n + 1))
    return B


_B = bernoulli_numbers(40)


def bernoulli_poly(n: int, x: float) -> float:
    return sum(math.comb(n, k) * _B[k] * x ** (n - k) for k in range(n + 1))


def hurwitz_neg_int(n: int, a: float) -> float:
    """ζ(-n, a) = −B_{n+1}(a)/(n+1) for n ≥ 0."""
    return -bernoulli_poly(n + 1, a) / (n + 1)


def zeta_hurwitz_2_minus_n(n: int) -> float:
    """ζ(2-n, 1/4). n=0 → ζ(2,1/4) not used here; n≥2 → ζ(0), ζ(-1), ..."""
    k = n - 2  # ζ(-k, 1/4) with k = n-2 ≥ 0
    return hurwitz_neg_int(k, 0.25)


def zeta2_quarter() -> float:
    """ζ(2,1/4) = Σ (n+1/4)^{-2}."""
    s = 0.0
    for n in range(20000):
        s += 1.0 / ((n + 0.25) ** 2)
    s += 1.0 / (20000 - 1 + 0.25)
    return s


ZETA2_QUARTER = zeta2_quarter()


def F_of_t(at: float, n_terms: int = 24) -> float:
    """Gradshteyn 9.554 expansion used in Suzuki §2.2, t≥0.

    e^{-t/2} Φ(e^{-2t},2,1/4)
      = 2t(log(2t)+ψ(1/4)-ψ(2)) + ζ(2,1/4)
        + Σ_{n≥2} ζ(2-n,1/4) (-2t)^n / n!
    """
    if at < 1e-18:
        return ZETA2_QUARTER
    s = 2.0 * at * (math.log(2.0 * at) + PSI_QUARTER - PSI2) + ZETA2_QUARTER
    pow_t = 1.0  # will multiply by (-2 at)^n
    fact = 1.0
    m2at = -2.0 * at
    pk = 1.0
    for n in range(1, n_terms + 1):
        pk *= m2at
        fact *= n
        if n < 2:
            continue
        s += zeta_hurwitz_2_minus_n(n) * pk / fact
    return s


def g_of_t(t: float) -> float:
    """Suzuki (1.3) with Lerch replaced by F from §2.2."""
    at = abs(float(t))
    polar = -4.0 * (math.exp(t / 2.0) + math.exp(-t / 2.0) - 2.0)
    linear = -(at / 2.0) * (PSI_QUARTER - LOGPI)
    lerch = -0.25 * (ZETA2_QUARTER - F_of_t(at))
    prime = 0.0
    if at >= math.log(2.0) - 1e-15:
        for n, Lam in von_mangoldt_upto(math.exp(at) + 1e-12):
            lg = math.log(n)
            if lg > at + 1e-14:
                continue
            prime += (Lam / math.sqrt(n)) * (at - lg)
    return polar + linear + lerch + prime


@functools.lru_cache(maxsize=None)
def g_cached(t: float) -> float:
    return g_of_t(t)


def nystrom_min_eig(a: float, n: int = 81) -> dict:
    """Nyström of K(t,u)=g(t-u)-g(t)-g(u) on mean-zero L²(-a,a)."""
    xs = np.linspace(-a, a, n)
    dx = float(xs[1] - xs[0])
    w = np.full(n, dx)
    w[0] *= 0.5
    w[-1] *= 0.5
    gx = np.array([g_cached(round(float(x), 12)) for x in xs])
    dt = xs[:, None] - xs[None, :]
    Gshift = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            Gshift[i, j] = g_cached(round(float(dt[i, j]), 12))
    K = Gshift - gx[:, None] - gx[None, :]
    sw = np.sqrt(w)
    A = (sw[:, None] * K) * sw[None, :]
    c = sw / np.linalg.norm(sw)
    P = np.eye(n) - np.outer(c, c)
    A0 = P @ A @ P
    evals = np.linalg.eigvalsh(A0)
    scale = 1.0 + float(np.max(np.abs(evals)))
    evals_nz = evals[np.abs(evals) > 1e-12 * scale]
    return {
        "a": a,
        "n": n,
        "g0": float(g_of_t(0.0)),
        "min_nz": float(np.min(evals_nz)) if len(evals_nz) else float("nan"),
        "n_neg": int(np.sum(evals_nz < -1e-10)),
    }


def main() -> None:
    print("=== F/g sanity ===")
    print(f"  A_closed = {A_SUZUKI:.12f}  (Suzuki 0.707546...)")
    print(f"  ζ(2,1/4) = {ZETA2_QUARTER:.12f}")
    print(f"  ζ(0,1/4) = {hurwitz_neg_int(0, 0.25):.12f}  (want 0.25)")
    print(f"  g(0) = {g_of_t(0.0):.6e}")
    print(f"{'t':>10} {'g(t)':>14} {'A_emp':>14} {'A_emp-A':>12} {'r/t^2':>12}")
    for t in (1e-4, 1e-3, 5e-3, 1e-2, 5e-2, 0.10, 0.20, A2 * 0.99):
        gt = g_of_t(t)
        aemp = gt / abs(t) - 0.5 * math.log(abs(t))
        rt = gt - 0.5 * abs(t) * math.log(abs(t)) - A_SUZUKI * abs(t)
        print(f"{t:10.6f} {gt:14.8e} {aemp:14.8f} {aemp - A_SUZUKI:12.4e} {rt/t/t:12.8f}")

    print("\n=== evenness ===")
    for t in (0.1, A2, A2 + 0.05, 0.5 * (A2 + A3)):
        print(f"  t={t:.6f} g={g_of_t(t):.8e}  odd_part={g_of_t(t)-g_of_t(-t):.3e}")

    print("\n=== Nyström (n_neg is the check; min_nz→0 is compact, not a gap) ===")
    print(f"{'a':>10} {'n':>4} {'min_nz':>14} {'n_neg':>6}")
    rows = []
    for a, n in [
        (0.10, 41),
        (0.20, 41),
        (A2 * 0.99, 61),
        (A2, 61),
        (A2 + 0.01, 61),
        (0.5 * (A2 + A3), 81),
        (A3 * 0.99, 81),
    ]:
        r = nystrom_min_eig(a, n)
        rows.append(r)
        print(f"{r['a']:10.6f} {r['n']:4d} {r['min_nz']:14.6e} {r['n_neg']:6d}")
        sys.stdout.flush()

    print("\n=== VERDICT ===")
    tchk = 1e-3
    aemp = g_of_t(tchk) / tchk - 0.5 * math.log(tchk)
    print(f"  A_emp(t={tchk}) = {aemp:.8f}  closed {A_SUZUKI:.8f}  rel={abs(aemp-A_SUZUKI)/A_SUZUKI:.3e}")
    if abs(aemp - A_SUZUKI) > 0.02:
        print("  FAIL: small-t expansion of g does not match Suzuki A. Parse still wrong.")
        sys.exit(1)
    if abs(hurwitz_neg_int(0, 0.25) - 0.25) > 1e-12:
        print("  FAIL: ζ(0,1/4)")
        sys.exit(1)
    if any(r["n_neg"] > 0 for r in rows if r["a"] < A2):
        print("  FAIL: negative kernel eig for a<a2.")
        sys.exit(1)
    print("  g-parse CHECKED against Suzuki A. a<a2: n_neg=0.")
    past_neg = [r for r in rows if r["a"] > A2 and r["n_neg"] > 0]
    if past_neg:
        print("  past a2: NEGATIVE Nyström eig — inspect T/g before any RH claim.")
    else:
        print("  past a2: n_neg=0 on sampled grids. Compact min_nz→0 is not λ_a.")
        print("  This encoding does not beat T for a lower bound (G accumulates at 0).")


if __name__ == "__main__":
    main()
