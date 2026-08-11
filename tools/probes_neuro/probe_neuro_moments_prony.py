#!/usr/bin/env python3
"""Probe N-R1 [vector N5.1]: {1,2}-mark identifiability curve and Prony-style
2-component reconstruction from measured finite-T moments.

Convention: flat-window Gram G_ij = sinc(pi*lambda*(x_i - x_j)) with x rescaled to
mean spacing 1 (same as tools/m3_zeros_check.py / probes_music_ling/probe_music_moments.py).
m_k = tr(G^k)/n.

The {1,2}-mark model (marks in {1,2}, sum of marks = N) predicts, in the submeasure
normalization, the full moment sequence from m2 alone:
    m1 = 1,  m2 = 2 - p1,  m3 = 3*m2 - 2,  m4 = 7*m2 - 6   (p1 = simple fraction).
This is the SAME family the near-CUE law saturates (m2(law)=1.31817, m3(law)=1.9545,
m4(law)=3.2272; attack-nevanlinna). It also agrees with the GUE limit at leading order
(m2,m3,m4) = (4/3, 2, 10/3) but NOT with the HL* sequence's m4 = 13/4 (the unresolved
provenance flag in attack-nevanlinna).

Questions:
  (a) Do the measured finite-T (m2, m3, m4) lie on the {1,2}-mark curve
      (residuals r3 = m3 - (3*m2-2), r4 = m4 - (7*m2-6))? -> internal consistency of
      the two-component/multiplicity model at finite T.
  (b) Implied simple fraction p1 = 2 - m2 vs the finite-T certificate value
      (~0.70 at these heights, attack-sandbox world (a)).
  (c) m4 measured vs 10/3 ({1,2}-mark/Gram value) vs 13/4 (HL* value): a cheap bearing
      on attack-nevanlinna's unresolved 13/4-vs-10/3 provenance flag.
  (d) Free 2-atom Prony fit: fit a 2-atom measure (atoms a<=b, weight w) to (m1,m2,m3);
      report the atoms (are they near {1,2}?) and the predicted m4 vs measured.

Run: cd tools && uv run --quiet --with numpy python probes_neuro/probe_neuro_moments_prony.py
"""
import numpy as np
import itertools

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
    sp = np.diff(gammas).mean()
    x = gammas / sp
    d = x[:, None] - x[None, :]
    G = np.sinc(la * d)
    m1 = np.trace(G) / n
    G2 = G @ G
    m2 = np.trace(G2) / n
    G3 = G2 @ G
    m3 = np.trace(G3) / n
    G4 = G3 @ G
    m4 = np.trace(G4) / n
    return m1, m2, m3, m4

def prony2(m1, m2, m3):
    """Free 2-atom fit: w*delta_a + (1-w)*delta_b matching (m1, m2, m3).
    Unknowns (a, b, w); solve moments 1..3. Returns (a, b, w, pred_m4) or None.
    Equations (center: mean = m1, use central moments for stability):
      m1 = w a + (1-w) b
      m2 = w a^2 + (1-w) b^2
      m3 = w a^3 + (1-w) b^3
    Work with centered variable y = x - m1: c2 = m2 - m1^2, c3 = m3 - 3 m1 m2 + 2 m1^3.
    For 2 atoms at u, v with weights: c2 = w u^2 + (1-w) v^2, c3 = w u^3 + (1-w) v^3
    and u + ... use the classical trick: (u+v) c2 - c3 = w u^2 v + (1-w) v^2 u = u v (w u + (1-w) v)
    = u v * 0  (mean zero). So u v = ( (u+v) c2 - c3 ) / 0 -- degenerate; use instead the
    standard Prony polynomial: atoms are roots of z^2 - s1 z + s2 where
      s1 = (m3 - m2 m1) / (m2 - m1^2)   ... see below.
    """
    # standard Prony (power moments, two exponentials): with m0 = 1 (total mass 1)
    # m1 = w a + (1-w) b ; m2 = w a^2 + (1-w) b^2 ; m3 = w a^3 + (1-w) b^3
    # (a+b) = (m3 - m1 m2)/(m2 - m1^2)  ;  a b = (m1 m3 - m2^2)/(m2 - m1^2)
    den = m2 - m1 * m1
    if abs(den) < 1e-12:
        return None
    s = (m3 - m1 * m2) / den          # a + b
    p = (m1 * m3 - m2 * m2) / den     # a b
    disc = s * s - 4 * p
    if disc < 0:
        return None
    sd = np.sqrt(disc)
    a = (s + sd) / 2
    b = (s - sd) / 2
    if abs(a - b) < 1e-12:
        return None
    w = (m1 - b) / (a - b)
    # predicted 4th moment from the fit
    m4p = w * a**4 + (1 - w) * b**4
    return a, b, w, m4p

def main():
    x10k = load("data/zeros_computed_10000.txt")
    print("== N-R1 [N5.1] {1,2}-mark identifiability curve + Prony fit, flat-window Gram lambda=1 ==")
    print("GUE limit (m2,m3,m4) = (4/3, 2, 10/3);  HL* (m2,m3,m4) = (4/3, 2, 13/4)")
    print("{1,2}-mark curve: m3 = 3*m2 - 2,  m4 = 7*m2 - 6  (parametrized by p1 = 2 - m2)\n")
    bands = [(0, 1000, "idx 0-1000   (h~14-1420)"),
             (1000, 4000, "idx 1000-4000 (h~1420-5800)"),
             (4000, 7000, "idx 4000-7000 (h~5800-10800)"),
             (7000, 10000, "idx 7000-10000 (h~10800-17000)")]
    for lo, hi, name in bands:
        g = x10k[lo:hi]
        m1, m2, m3, m4 = moments(g)
        r3 = m3 - (3 * m2 - 2)
        r4 = m4 - (7 * m2 - 6)
        p1 = 2 - m2
        fit = prony2(m1, m2, m3)
        print(f"{name}: n={g.size:5d}")
        print(f"   m1={m1:.4f} m2={m2:.4f} m3={m3:.4f} m4={m4:.4f}")
        print(f"   {1,2}-mark residuals: r3=m3-(3m2-2)={r3:+.4f}   r4=m4-(7m2-6)={r4:+.4f}")
        print(f"   implied p1 = 2 - m2 = {p1:.4f}   (finite-T certificate ~0.70, attack-sandbox)")
        print(f"   m4 vs {10/3:.4f} (mark/Gram) and {13/4:.4f} (HL*): d10/3={m4-10/3:+.4f}  d13/4={m4-13/4:+.4f}")
        if fit:
            a, b, w, m4p = fit
            print(f"   free 2-atom Prony fit: atoms a={a:.4f} b={b:.4f} w={w:.4f}  pred m4={m4p:.4f} vs meas {m4:.4f} (diff {m4p-m4:+.4f})")
        else:
            print("   free 2-atom Prony fit: FAILED (degenerate)")
        print()

    # whole-10k moments omitted: O(N^2) Gram build + matmul at n=10000 is too heavy for a
    # probe; band-wise moments are the comparable objects (music-ling R5 convention).

if __name__ == "__main__":
    main()
