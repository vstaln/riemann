#!/usr/bin/env python3
"""attack_conditioning.py -- second variation / conditioning of Q at the cosine optimum.

Q(v) = [int v^2 + int int |s-s'| v(s)v(s')] / (int v)^2,   v : [-1/2,1/2] -> R
minimizer v0(u) = cos(sqrt(2) u);  Q(v0) = c = 1/2 + (1/sqrt2) cot(1/sqrt2) = 1.32749929632...
certificate constant = 2 - Q(v0) = 0.6725007036794116.

Facts (PROVEN attack-kernel.md; validator-corrected validation-001 target 2):
  M = I + T,  (Tv)(u) = int |u-v| v(v) dv,  M >> 0 with min eigenvalue 1 - 2/pi^2 ~ 0.79736.
  Stationarity: M v0 = c * D0 * 1,  D0 = <v0,1> = sqrt(2) sin(1/sqrt2).
On the tangent space T = {<w,1> = 0}:  Q((v0 + e w)/D0) = c + e^2 <w,Mw>/D0^2  EXACTLY (no O(e^3)).
Hessian on T is the quadratic form 2 M / D0^2; conditioning of the constant =
  spread of <w,Mw>/<w,w> over w in T  =  constrained eigenvalues of M on T (= nonzero
  eigenvalues of P M P, P = I - 11^T/N).

Run:  uv run --with numpy python3 tools/attack_conditioning.py
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "2")
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
from numpy.polynomial import chebyshev as C

SQRT2 = np.sqrt(2.0)


def build(N):
    h = 1.0 / N
    us = (np.arange(N) + 0.5) * h - 0.5
    M = np.eye(N) + np.abs(us[:, None] - us[None, :]) * h
    return us, h, M


def inn(a, b, h):
    return np.dot(a, b) * h


def Q(v, M, h):
    return inn(v, M @ v, h) / inn(v, np.ones_like(v), h) ** 2


def main():
    import sys
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    us, h, M = build(N)
    one = np.ones(N)
    v0 = np.cos(SQRT2 * us)
    D0 = inn(v0, one, h)
    c = Q(v0, M, h)
    c_an = 0.5 + 1.0 / SQRT2 / np.tan(1.0 / SQRT2)
    cert = 2.0 - c_an
    print(f"N = {N}")
    print(f"Q(v0) = {c:.15f}   analytic c = {c_an:.15f}   diff = {abs(c-c_an):.2e}")
    print(f"certificate constant 2 - Q = {2.0-c:.15f}   (analytic 0.6725007036794116)")
    print(f"D0 = <v0,1> = {D0:.12f}   (analytic sqrt2 sin(1/sqrt2) = {SQRT2*np.sin(1/SQRT2):.12f})")
    print(f"||v0||_2 = {np.sqrt(inn(v0,v0,h)):.12f}   ||v0||_2^2/D0^2 = {inn(v0,v0,h)/D0**2:.6f}")
    resid = np.max(np.abs(M @ v0 - c * D0))
    print(f"stationarity max|M v0 - c*D0*1| = {resid:.2e}")

    # ---- exact-quadratic identity: Q(v0+e g) - c = e^2 [<g,Mg> - c <g,1>^2]/D0^2 + O(e^3) ----
    print("\n-- quadratic identity check: delta(e) vs e^2 [<g,Mg>-c<g,1>^2]/D0^2 (exact for <g,1>=0) --")
    shapes = {
        "sin(pi u)": np.sin(np.pi * us),
        "cos(2pi u)": np.cos(2 * np.pi * us),
        "cos(pi u)": np.cos(np.pi * us),
        "4u^2": 4.0 * us**2,
    }
    for name, g in shapes.items():
        g1 = inn(g, one, h)
        aw = (inn(g, M @ g, h) - c * g1**2) / D0**2
        for eps in (1e-3, 1e-2, 1e-1):
            delta = Q(v0 + eps * g, M, h) - c
            pred = eps**2 * aw
            print(f"  {name:11s} <g,1>={g1:+.4f}  e={eps:.1e}: delta={delta:.6e} pred={pred:.6e} ratio={delta/pred:.8f}")

    # ---- Hessian / condition number ----
    print("\n-- eigenvalue analysis of M = I+T --")
    evals = np.linalg.eigvalsh(M)
    print(f"  lambda_min(M) = {evals[0]:.8f}  (analytic 1 - 2/pi^2 = {1 - 2/np.pi**2:.8f})")
    kpos = 2.3993572804844673  # smallest positive root of (k/2)tanh(k/2)=1 (validation-001)
    print(f"  lambda_max(M) = {evals[-1]:.8f}  (analytic 1 + 2/k^2, k={kpos:.6f}: {1 + 2/kpos**2:.8f})")
    P = np.eye(N) - np.outer(one, one) / N
    B = P @ M @ P
    evB = np.linalg.eigvalsh(B)
    lam_min_T, lam_max_T = evB[1], evB[-1]
    print(f"  constrained on T (w perp 1): lambda_min|_T = {lam_min_T:.8f}, lambda_max|_T = {lam_max_T:.8f}")
    print(f"  CONDITION NUMBER kappa (full T) = lambda_max|_T / lambda_min|_T = {lam_max_T/lam_min_T:.4f}")
    # even subspace: even functions are w_i = w_{N-1-i}; restricted matrix B_e[k,l] = B[k,l] + B[k,N-1-l]
    Be = B[: N // 2, : N // 2] + B[: N // 2, N // 2 :][:, ::-1]
    evBe = np.linalg.eigvalsh(Be)
    lam_min_e, lam_max_e = evBe[1], evBe[-1]
    print(f"  constrained on T n even:     lambda_min = {lam_min_e:.8f}, lambda_max = {lam_max_e:.8f}")
    print(f"  CONDITION NUMBER kappa (even T) = {lam_max_e/lam_min_e:.4f}")
    print(f"  Hessian on T = 2M/D0^2: eigenvalues {2*lam_min_T/D0**2:.4f} .. {2*lam_max_T/D0**2:.4f}")

    # ---- perturbation table: v = v0 + e*g, e=0.01, ||g||_inf = 1 (1% pointwise) ----
    print("\n-- perturbation table: 1% pointwise perturbation, v = v0 + 0.01*g, ||g||_inf = 1 --")
    print("   (g normalized to sup-norm 1; delta = Q(perturbed) - c; const -> 0.6725007 - delta)")

    def row(name, g):
        g = np.asarray(g, dtype=float)
        gin = np.max(np.abs(g))
        g = g / gin
        g1 = inn(g, one, h)
        alpha = (inn(g, M @ g, h) - c * g1**2) / D0**2
        eps = 0.01
        delta = Q(v0 + eps * g, M, h) - c
        print(f"  {name:22s} <g,1>={g1:+.3f} alpha={alpha:.5f}  delta(1%)={delta:.3e}  const={cert-delta:.6f}  rel={delta/cert*100:.4f}%")

    row("sin(pi u)  [odd]", np.sin(np.pi * us))
    row("cos(pi u)  [odd]", np.cos(np.pi * us))
    row("cos(2pi u) [even]", np.cos(2 * np.pi * us))
    row("4u^2       [even]", 4.0 * us**2)

    # frequency detuning of the cosine itself: Q(cos(lambda u))
    print("\n-- frequency detuning: Q(cos(lambda u)) - c (a genuine small-frequency cosine) --")
    for dl in (-0.02, -0.01, -0.005, 0.005, 0.01, 0.02):
        lam = SQRT2 * (1 + dl)
        v = np.cos(lam * us)
        delta = Q(v, M, h) - c
        print(f"  lambda = sqrt2*({1+dl:+.3f}) = {lam:.4f}: delta = {delta:.6e}  rel const = {delta/cert*100:.4f}%")
    # curvature d^2Q/dlambda^2 at sqrt2 via three-point formula
    lam0 = SQRT2
    v0l = np.cos(lam0 * us)
    d = 1e-3
    vp = np.cos((lam0 + d) * us)
    vm = np.cos((lam0 - d) * us)
    d2 = (Q(vp, M, h) - 2 * Q(v0l, M, h) + Q(vm, M, h)) / d**2
    print(f"  d^2Q/dlambda^2 at sqrt2 ~= {d2:.4f}  (so delta ~ 0.5*d2*(dl*lambda)^2)")

    # polynomial (Chebyshev) approximations
    print("\n-- polynomial (Chebyshev) approximations of cos(sqrt2 u) --")
    for deg in (4, 6, 10, 16):
        coef = C.chebfit(us, v0, deg)
        g = C.chebval(us, coef)
        rel2 = np.sqrt(inn(g - v0, g - v0, h) / inn(v0, v0, h))
        relinf = np.max(np.abs(g - v0)) / np.max(np.abs(v0))
        delta = Q(g, M, h) - c
        print(f"  deg={deg:2d}: ||g-v0||_2/||v0||_2 = {rel2:.3e}  ||g-v0||_inf = {relinf:.3e}  delta = {delta:.3e}  rel const = {delta/cert*100:.3e}%")

    # boundary ramps (the paper's C^infty compact-support smoothing)
    print("\n-- boundary ramp: v = cos(sqrt2 u)*chi, chi: 1 on bulk, 0 at +-1/2 over width w --")

    def ramp(w, smooth):
        d = 0.5 - np.abs(us)
        t = np.clip(d / w, 0.0, 1.0)
        chi = t * t * (3 - 2 * t) if smooth else t
        return np.cos(SQRT2 * us) * chi

    for w in (0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5):
        for smooth in (False, True):
            v = ramp(w, smooth)
            delta = Q(v, M, h) - c
            relinf = np.max(np.abs(v - v0))
            print(f"  w={w:.3f} smooth={str(smooth):5s}: max|v-v0|={relinf:.3f}  delta = {delta:.5f}  rel const = {delta/cert*100:.3f}%")

    # large-shape deviations for contrast (from attack-kernel table)
    print("\n-- large-shape deviations for contrast (not 1% perturbations) --")
    box = np.ones(N)
    print(f"  flat box 1:        delta = {Q(box,M,h)-c:.6f}  (const {2-Q(box,M,h):.6f}, attack-kernel 2/3)")
    for k in (1, 2, 4):
        g = (1 - 4 * us**2) ** k
        print(f"  (1-4u^2)^k, k={k}:    delta = {Q(g,M,h)-c:.6f}  (const {2-Q(g,M,h):.6f})")

    # random directions: typical/worst sensitivity at 1% relative L2 perturbation
    print("\n-- random directions w perp 1, ||w||_2 = 0.01*||v0||_2 (1% relative-L2 perturbation) --")
    rng = np.random.default_rng(0)
    nrm = np.sqrt(inn(v0, v0, h))
    deltas = []
    for _ in range(200):
        w = rng.standard_normal(N)
        w = w - one * (inn(w, one, h) / inn(one, one, h))
        w = w / np.sqrt(inn(w, w, h)) * (0.01 * nrm)
        deltas.append(Q(v0 + w, M, h) - c)
    deltas = np.array(deltas)
    print(f"  delta: min = {deltas.min():.4e}, median = {np.median(deltas):.4e}, max = {deltas.max():.4e}")
    print(f"  rel const: min {deltas.min()/cert*100:.4f}%, median {np.median(deltas)/cert*100:.4f}%, max {deltas.max()/cert*100:.4f}%")


if __name__ == "__main__":
    main()
