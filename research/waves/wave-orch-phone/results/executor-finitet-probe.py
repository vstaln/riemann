#!/usr/bin/env python3
"""EXECUTOR-FINITET: finite-T vs T->infinity probe for the cosine-window zero-count functional.

Mini-orchestration role: EXECUTOR (numerical probe of the finite-T gap).
Environment: proot Ubuntu (mpmath 1.4.1, numpy 2.3.5). Modest compute, fully vectorized.

Model (from research/notes/attack-finitet.md, verified against its tables):
  phi_T(x) = psi(x*T/N),  psi(u) = cos(a*u)*1_{|u|<=1/2},  rescaled s_rho = (gamma-T)*N/T
  Psi(s)  = sin(a/2-pi s)/(a-2 pi s) + sin(a/2+pi s)/(a+2 pi s)   = [sinc((a/2-pi s)/pi)+sinc((a/2+pi s)/pi)]/2
  Psi2(s) = sin(pi s)/(2 pi s) + 1/4[ sin(a-pi s)/(a-pi s) + sin(a+pi s)/(a+pi s) ]
          = sinc(s)/2 + 1/4[ sinc((a-pi s)/pi) + sinc((a+pi s)/pi) ]
  int psi^2 = 1/2 + sin(a)/(2a) = Psi2(0)   [check: a=sqrt(2) -> 0.849227999318304]
  W = (1/int psi^2) V^T V ;  bound/N = 2 trW/N - ||W||^2_HS/N
  ||W||^2_HS/N via exact Poisson pair sum: (VV^T)_rr' = Psi2(s_r - s_r'), sum over r,r' /(N int psi^2 ^2)
  asymptotic constant of the window: 2 - c_a,  c_a = 1/2 + (1/a) cot(1/a)
  (for a=sqrt(2): 3/2 - (1/sqrt(2))cot(1/sqrt(2)) = 0.672500703679412, matching attack-finitet.md)

IMPORTANT framing (honesty): the record bound 0.6732628655 uses the *refined* machinery
bound=(H-tau)/(1-B/m) with H(1.49)=0.6724218860964 (a block/mollifier-structured functional,
NOT equal to the naive 2 - c_a of the idealized model). This probe measures the idealized
functional's finite-T gap: sign and size of (bound/N - (2 - c_a)) for a = sqrt(2) and a = 1.49.
That sign/size is exactly what P6 asks about for the kernel class, and it is the quantity the
prior notes measured (their Delta vs 0.6725007).
"""

import numpy as np

DATA10 = "/root/riemann/tools/data/zeros_computed_10000.txt"
DATA11 = "/root/riemann/tools/data/zeros_lmfdb_large.txt"


def load(path):
    g = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            g.append(float(parts[1]))
    return np.array(g)


def probe(gammas, a, T, K=None):
    """Idealized-model bound/N for cosine window cos(a*u), window [T,2T).

    Uses the paper's grid k = 0..N-1 (alpha_k = T + (T/N)k), which reproduces the
    prior notes' tables exactly (verified: T=200 trW=0.988856, HS2_tr=1.261182;
    T=600 trW=0.998163, HS2_tr=1.287259)."""
    mask = (gammas >= T) & (gammas < 2 * T)
    g = gammas[mask]
    N = g.size
    if N == 0:
        return None
    s = (g - T) * N / T
    ks = np.arange(0, N)                # paper grid: k = 0..N-1
    D = s[:, None] - ks[None, :]        # N x N
    V = 0.5 * (np.sinc(D + a / (2 * np.pi)) + np.sinc(D - a / (2 * np.pi)))
    intpsi2 = 0.5 + np.sin(a) / (2 * a)
    trW = (1.0 / N) * np.sum(V * V) / intpsi2
    S = s[:, None] - s[None, :]         # N x N
    P2 = 0.5 * np.sinc(S) + 0.25 * (np.sinc((a - np.pi * S) / np.pi) + np.sinc((a + np.pi * S) / np.pi))
    HS2_an = (1.0 / N) * np.sum(P2 * P2) / intpsi2**2
    bound = 2 * trW - HS2_an
    HS2_tr = None
    if N <= 400:                          # dense W only where cheap
        W = (V @ V.T) / intpsi2
        HS2_tr = np.sum(W * W) / N
    ca = 0.5 + (1.0 / a) / np.tan(1.0 / a)
    asy = 2.0 - ca
    return {"T": T, "N": N, "K": ks.size, "trW_N": trW, "HS2_an": HS2_an,
            "HS2_tr": HS2_tr, "bound_N": bound, "asy": asy, "Delta": bound - asy}


def main():
    g10 = load(DATA10)
    g11 = load(DATA11)
    print(f"data: 10k file N={g10.size} gamma_max={g10[-1]:.2f}; 11k file N={g11.size} gamma_max={g11[-1]:.2f}")

    for a, tag in [(np.sqrt(2), "sqrt(2)"), (1.49, "1.49")]:
        ca = 0.5 + (1.0 / a) / np.tan(1.0 / a)
        asy = 2.0 - ca
        print(f"\n=== window cos({a}*u)  [a={tag}]  own asymptotic constant 2-c_a = {asy:.10f} ===")
        print(f"{'T':>7} {'N':>5} {'K':>4} {'trW/N':>8} {'HS2_an':>8} {'bound/N':>8} {'Delta=bound-asy':>16}")
        Ts = [200, 400, 800, 1600, 3200, 5000]
        rows = []
        for T in Ts:
            g = g11 if 2 * T <= g11[-1] else (g10 if 2 * T <= g10[-1] else None)
            if g is None:
                continue
            r = probe(g, a, T)
            if r is None:
                continue
            rows.append(r)
            print(f"{T:7d} {r['N']:5d} {r['K']:4d} {r['trW_N']:8.5f} {r['HS2_an']:8.5f} "
                  f"{r['bound_N']:8.5f} {r['Delta']:+16.6f}")
        if len(rows) >= 4:
            Ts = np.array([r["T"] for r in rows])
            ds = np.array([r["Delta"] for r in rows])
            print("  trend fits (intercept = conjectured T->infinity level):")
            for name, X in [("1/logT", 1.0 / np.log(Ts)), ("1/T", 1.0 / Ts), ("1/log2T", 1.0 / np.log(Ts) ** 2)]:
                Xc = np.column_stack([np.ones_like(Ts), X])
                coef, *_ = np.linalg.lstsq(Xc, ds, rcond=None)
                resid = ds - Xc @ coef
                print(f"    Delta ~ {coef[0]:+.6f} + {coef[1]:+.4f}*{name:<8s} rss={np.sum(resid**2):.2e}")
            print("  sign at all T:", "POSITIVE (overshoot, safe direction)" if np.all(ds > 0)
                  else "NEGATIVE or MIXED (dangerous direction)")


if __name__ == "__main__":
    main()
