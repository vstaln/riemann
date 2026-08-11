#!/usr/bin/env python3
"""Probe M1.1 + M5.4 (music-ling catalog): moment "tuning" (beating) and the
xi'/xi joint-moment coupling question.

Questions:
  (a) [M1.1] Empirical flat-window Gram moments m2, m3 (lambda=1) vs closed forms
      (4/3, 2) over bands of increasing height: does the "mistuning"
      Delta_k(T) = m_k(measured) - GUE_value decay with height ("in tune" in the limit)?
  (b) [M5.4] Do the xi'-zero moments couple to the xi-zero moments? Compare m2 of the
      xi' zero set with m2 of the xi zero set on the SAME height range. If m2(xi') ~=
      m2(xi) with the same finite-height deficit, the two functionals carry overlapping
      information (weak coupling); if systematically different, the joint system is richer.

Method: flat-window Gram G_ij = sinc(pi*lambda*(x_i - x_j)) with x rescaled to mean
spacing 1 (same convention as tools/m3_zeros_check.py). m2 = tr G^2 / n, m3 = tr G^3 / n.
Data: tools/data/zeros_computed_10000.txt (xi zeros); tools/data/xiprime_on_line_1_1000.txt
(xi' zeros to height ~1419); tools/data/zeros_1_1000.txt (LMFDB xi zeros, 34 digits).
"""
import numpy as np

def load(fn):
    g = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                g.append(float(p[1]))
    return np.sort(np.array(g))

def moments(gammas, la=1.0):
    n = gammas.size
    if n < 5:
        return np.nan, np.nan, np.nan
    sp = np.diff(gammas).mean()
    x = gammas / sp
    d = x[:, None] - x[None, :]
    G = np.sinc(la * d)
    m1 = np.trace(G) / n
    G2 = G @ G
    m2 = np.trace(G2) / n
    G3 = G2 @ G
    m3 = np.trace(G3) / n
    return m1, m2, m3

def main():
    x10k = load("data/zeros_computed_10000.txt")
    print("== M1.1 moment tuning: flat-window Gram, lambda=1, m2 vs 4/3, m3 vs 2 ==")
    bands = [(0, 1000, "idx 0-1000   (h~14-1420)"),
             (1000, 4000, "idx 1000-4000 (h~1420-5800)"),
             (4000, 7000, "idx 4000-7000 (h~5800-10800)"),
             (7000, 10000, "idx 7000-10000 (h~10800-17000)")]
    for lo, hi, name in bands:
        g = x10k[lo:hi]
        m1, m2, m3 = moments(g)
        print(f"{name}: n={g.size:5d}  m1={m1:.4f}  m2={m2:.4f} (exp 1.3333, d2={m2-4/3:+.4f})"
              f"  m3={m3:.4f} (exp 2.0000, d3={m3-2:+.4f})")

    print("\n== M5.4 xi' vs xi moment coupling (same height range, h <= ~1419) ==")
    xip = load("data/xiprime_on_line_1_1000.txt")
    xi_lmfdb = load("data/zeros_1_1000.txt")
    m1p, m2p, m3p = moments(xip)
    m1z, m2z, m3z = moments(xi_lmfdb)
    print(f"xi'  (n={xip.size}):  m1={m1p:.4f}  m2={m2p:.4f}  m3={m3p:.4f}")
    print(f"xi   (n={xi_lmfdb.size}): m1={m1z:.4f}  m2={m2z:.4f}  m3={m3z:.4f}")
    print(f"ratio m2(xi')/m2(xi) = {m2p/m2z:.4f}   |m2(xi')-m2(xi)| = {abs(m2p-m2z):.4f}")
    print("(if ratio ~ 1 and both carry the same deficit, the two functionals are weakly coupled)")

    # xi' band at higher height for trend (file only reaches ~1419; note range limit)
    print("\nnote: xi' data available only to h~1419; higher-height xi' moments need computation")

if __name__ == "__main__":
    main()
