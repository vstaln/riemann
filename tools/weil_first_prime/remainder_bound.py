#!/usr/bin/env python3
"""Explicit remainder for Suzuki (2.2)/(4.5): r(t) and r''(t).

r(t) := g_arch(t) − (1/2)|t|log|t| − A|t|   (primes stripped from g)
PROVEN: r(t) = −(7/8) t² + O(t⁴) for 0<t<log 2.
This script:
  1. Checks t⁴ coefficient against −3/128 (Taylor of polar + Hurwitz n=4).
  2. Tabulate r''(s) + 7/4 on [0, 2 a3] (the kernel argument in (4.5)).
  3. Evaluates the (4.5) pieces on even cosine / first odd sine vs probe T.
  4. Prints a crude lower bound using L≥0 and ‖r''‖_∞ — expected vacuous —
     and a split bound (7/4)a(∫w)² − a‖ρ''‖_∞(∫|w|)² − |Hankel|.

Belief this changes: whether the O(a³) leftover after the 7/8 lemma is
smaller than the 10^{-3} gap at a₂ (if yes, an explicit δ exists; if not,
(4.5) with ‖·‖_∞ remainder is the same wall as the crude prime bound).

Usage: python3 tools/weil_first_prime/remainder_bound.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dirichlet_vs_prime import L_a  # noqa: E402
from lower_bound import A2, A3, GAMMA, LOG2, PRIME2_COEFF  # noqa: E402
from probe import T_of_G, autocorrelation, even_basis  # noqa: E402
from screw_kernel import A_SUZUKI, g_of_t  # noqa: E402

A = A_SUZUKI
C2A1 = 2.0 * A + 1.0


def g_arch(t: float) -> float:
    """g without the von Mangoldt ramp (r is archimedean)."""
    # g_of_t includes primes for |t|≥log 2; subtract them.
    at = abs(t)
    g = g_of_t(t)
    if at >= LOG2 - 1e-15:
        from probe import von_mangoldt_upto

        prime = 0.0
        for n, Lam in von_mangoldt_upto(math.exp(at) + 1e-12):
            lg = math.log(n)
            if lg > at + 1e-14:
                continue
            prime += (Lam / math.sqrt(n)) * (at - lg)
        g -= prime
    return g


def r_of_t(t: float) -> float:
    at = abs(float(t))
    if at < 1e-14:
        return 0.0
    return g_arch(t) - 0.5 * at * math.log(at) - A * at


def r_dd(t: float, h: float = 1e-5) -> float:
    """r''(t) for t>0 by 5-point stencil. r even ⇒ r''(0)=lim."""
    t = abs(float(t))
    if t < 4 * h:
        t = 4 * h
    return (
        -r_of_t(t + 2 * h)
        + 16.0 * r_of_t(t + h)
        - 30.0 * r_of_t(t)
        + 16.0 * r_of_t(t - h)
        - r_of_t(t - 2 * h)
    ) / (12.0 * h * h)


def cosine_w(n: int = 801) -> tuple[np.ndarray, np.ndarray, float]:
    ts = np.linspace(-1.0, 1.0, n)
    w = np.cos(0.5 * math.pi * ts)
    nrm = float(np.trapezoid(w * w, ts))
    return ts, w, nrm


def sine_w(n: int = 801) -> tuple[np.ndarray, np.ndarray, float]:
    ts = np.linspace(-1.0, 1.0, n)
    w = np.sin(math.pi * ts)  # odd, vanishes at ±1
    nrm = float(np.trapezoid(w * w, ts))
    return ts, w, nrm


def double_kernel(ts: np.ndarray, w: np.ndarray, a: float, kernel) -> float:
    """∬ K(a(x-y)) w(x) w(y) dx dy, trapezoid."""
    n = len(ts)
    dx = float(ts[1] - ts[0])
    wt = np.full(n, dx)
    wt[0] *= 0.5
    wt[-1] *= 0.5
    acc = 0.0
    for i in range(n):
        s = a * (ts[i] - ts)
        Kv = np.array([kernel(float(si)) for si in s])
        acc += float(np.sum(Kv * w * wt)) * w[i] * wt[i]
    return acc


def hankel_lag(ts: np.ndarray, w: np.ndarray, lag: float) -> float:
    """∫ w(x) w(x-lag) dx on [-1,1] (zero outside)."""
    shifted = np.interp(ts - lag, ts, w, left=0.0, right=0.0)
    return float(np.trapezoid(w * shifted, ts))


def T_of_w(a: float, w: np.ndarray, ts: np.ndarray, primes: bool) -> float:
    """R(a,w) via probe T on v(x)=w(x/a)."""
    xs = a * ts
    v = w  # same samples; dx scales: T/G0 invariant? 
    # v(x)=w(x/a), xs = linspace(-a,a). Re-sample:
    xs = np.linspace(-a, a, len(ts))
    v = np.interp(xs / a, ts, w)
    dx = float(xs[1] - xs[0])
    nrm = float(np.trapezoid(v * v, xs))
    taus, G = autocorrelation(v, dx)
    return T_of_G(taus, G, a, primes=primes) / nrm


def main() -> None:
    print("=== Taylor of r: t² = −7/8, t⁴ vs −3/128 ===")
    print(f"{'t':>10} {'r/t^2':>14} {'(r+7/8 t^2)/t^4':>18}")
    t4s = []
    for t in (1e-3, 2e-3, 5e-3, 1e-2):
        rt = r_of_t(t)
        t4 = (rt + 0.875 * t * t) / (t ** 4)
        t4s.append(t4)
        print(f"{t:10.4f} {rt/(t*t):14.8f} {t4:18.8f}")
    print(f"  −3/128 = {-3.0/128:.8f}")
    print(f"  r''(0) via stencil at t=4e-5: {r_dd(0.0):.8f}  want −7/4={-1.75:.8f}")

    print("\n=== r''(s)+7/4 on [0, 2 a3] (argument of (4.5) kernel) ===")
    S = 2.0 * A3
    ss = np.linspace(0.0, S, 221)
    rpp = np.array([r_dd(float(s)) for s in ss])
    rho = rpp + 1.75
    i_max = int(np.argmax(np.abs(rho)))
    print(f"  S=2 a3={S:.6f}")
    print(f"  r''(0+)={rpp[1]:.6f}")
    print(f"  sup|r''+7/4|={abs(rho[i_max]):.6f} at s={ss[i_max]:.4f}")
    print(f"  r''(S)={rpp[-1]:.6f}  ρ''(S)={rho[-1]:.6f}")
    print(f"  min r''={float(np.min(rpp)):.6f}  max r''={float(np.max(rpp)):.6f}")
    for s in (0.0, 0.1, A2, LOG2, 0.8, S):
        print(f"    s={s:.4f}  r''={r_dd(s):+.6f}  ρ''={r_dd(s)+1.75:+.6f}")

    print("\n=== (4.5) pieces vs T, even cosine w=cos(πt/2) ===")
    ts, w, nrm = cosine_w(401)
    Lw = L_a(w, ts, 1.0) / nrm
    iw = float(np.trapezoid(w, ts))
    print(f"  L/‖w‖²={Lw:.6f}  ∫w={iw:.6f}  (∫w)²/‖w‖²={iw*iw/nrm:.6f}  16/π²={16/math.pi**2:.6f}")
    print(
        f"{'a':>8} {'T':>10} {'log-c+L':>10} {'rank1':>10} "
        f"{'ρ''term':>10} {'prime':>10} {'sum':>10} {'T-sum':>10}"
    )
    for a, pr in [
        (0.10, False),
        (0.20, False),
        (A2 * 0.99, False),
        (A2, True),
        (A2 + 0.01, True),
        (0.5 * (A2 + A3), True),
    ]:
        Trel = T_of_w(a, w, ts, primes=pr)
        logc = math.log(1.0 / a) - C2A1
        rank1 = (7.0 / 4.0) * a * (iw * iw / nrm)
        # ρ'' term: −a/‖w‖² ∬ ρ''(a(x-y)) w w,  ρ''=r''+7/4
        def rho_pp(s, _a=a):
            return r_dd(abs(s)) + 1.75

        rho_int = double_kernel(ts, w, a, rho_pp)
        rho_term = -a * rho_int / nrm
        prime_term = 0.0
        if pr and 2.0 * a + 1e-14 >= LOG2:
            lag = LOG2 / a  # (log 2)/a in the scaled coordinate
            # (4.5) coefficient: (1/a)(Λ(2)/√2) * (G_w(lag)+G_w(-lag)) / ‖w‖²
            # G_w(lag)=∫ w(x)w(x-lag) dx. Even ⇒ 2 G_w(lag).
            # Match probe: T_prime/G0 = −√2 log 2 · G_v(log 2)/G_v(0).
            # Scaling: G_v(log 2) = a ∫ w(t) w(t − log2/a) dt = a G_w(lag),
            # G_v(0)=a ‖w‖², so G_v(log2)/G_v(0)=G_w(lag)/‖w‖².
            # T_prime/G0 = −PRIME2_COEFF * G_w(lag)/nrm
            prime_term = -PRIME2_COEFF * hankel_lag(ts, w, lag) / nrm
        sm = logc + Lw + rank1 + rho_term + prime_term
        print(
            f"{a:8.4f} {Trel:10.6f} {logc+Lw:10.6f} {rank1:10.6f} "
            f"{rho_term:10.6f} {prime_term:10.6f} {sm:10.6f} {Trel-sm:10.6f}"
        )
        sys.stdout.flush()

    print("\n=== same pieces, first odd sine w=sin(πt) ===")
    ts, w, nrm = sine_w(401)
    Lw = L_a(w, ts, 1.0) / nrm
    iw = float(np.trapezoid(w, ts))
    print(f"  L/‖w‖²={Lw:.6f}  ∫w={iw:.3e} (odd)")
    print(f"{'a':>8} {'T':>10} {'log-c+L':>10} {'ρ''term':>10} {'prime':>10} {'sum':>10} {'T-sum':>10}")
    for a, pr in [(0.20, False), (A2, True), (0.5 * (A2 + A3), True)]:
        Trel = T_of_w(a, w, ts, primes=pr)
        logc = math.log(1.0 / a) - C2A1
        def rho_pp(s):
            return r_dd(abs(s)) + 1.75
        rho_term = -a * double_kernel(ts, w, a, rho_pp) / nrm
        prime_term = 0.0
        if pr and 2.0 * a + 1e-14 >= LOG2:
            lag = LOG2 / a
            prime_term = -PRIME2_COEFF * hankel_lag(ts, w, lag) / nrm
        sm = logc + Lw + rho_term + prime_term  # rank1=0
        print(
            f"{a:8.4f} {Trel:10.6f} {logc+Lw:10.6f} {rho_term:10.6f} "
            f"{prime_term:10.6f} {sm:10.6f} {Trel-sm:10.6f}"
        )

    print("\n=== crude lower bounds (even cosine) ===")
    # L≥0; |∬ ρ'' ww| ≤ ‖ρ''‖_∞ (∫|w|)² ≤ 2 ‖ρ''‖_∞ ‖w‖² on [-1,1]
    ts, w, nrm = cosine_w(401)
    absint = float(np.trapezoid(np.abs(w), ts))
    print(f"  (∫|w|)²/‖w‖²={absint**2/nrm:.6f}  (≤2)")
    S = 2.0 * A3
    ss = np.linspace(0.0, S, 221)
    sup_rho = max(abs(r_dd(float(s)) + 1.75) for s in ss)
    sup_rpp = max(abs(r_dd(float(s))) for s in ss)
    print(f"  sup_[0,2a3]|ρ''|={sup_rho:.6f}  sup|r''|={sup_rpp:.6f}")
    print(f"{'a':>8} {'log-c':>10} {'+rank1':>10} {'−a·2·supρ':>12} {'−|p|':>10} {'crude':>10} {'T':>10}")
    for a in (0.10, 0.20, A2, A2 + 0.01, 0.5 * (A2 + A3)):
        logc = math.log(1.0 / a) - C2A1
        rank1 = (7.0 / 4.0) * a * (16.0 / math.pi ** 2)
        err = a * sup_rho * (absint ** 2 / nrm)
        p = 0.0
        if 2.0 * a >= LOG2 - 1e-14:
            lag = LOG2 / a
            p = -abs(-PRIME2_COEFF * hankel_lag(ts, w, lag) / nrm)
        crude = logc + rank1 - err + p  # dropped L≥0; actually add Lw if we want
        Trel = T_of_w(a, w, ts, primes=(2 * a >= LOG2))
        print(f"{a:8.4f} {logc:10.6f} {rank1:10.6f} {-err:12.6f} {p:10.6f} {crude:10.6f} {Trel:10.6f}")

    print("\n=== VERDICT ===")
    t = 1e-3
    t4 = (r_of_t(t) + 0.875 * t * t) / (t ** 4)
    print(f"  (r+7/8 t²)/t⁴ at 1e-3 = {t4:.6f}  (−3/128={-3/128:.6f})")
    print("  If (4.5) sum matches T to ~1e-3, the split is implemented.")
    print("  If crude lower bound is negative at a2, ‖·‖_∞ remainder is vacuous (same wall).")


if __name__ == "__main__":
    main()
