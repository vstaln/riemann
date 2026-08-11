#!/usr/bin/env python3
"""B3.1 (biology note): mixture identifiability + empirical third moment on real zeros.

(a) Count-level mixture model of the zero configuration (ideal model):
    a1 simple on-line atoms (eigenvalue 1), a2 double on-line atoms (eigenvalue 2),
    p off-line (1,1)-planes (eigenvalues +-c, c=1 here; trace 0, HS2 2c^2 each).
    Observable moments:
      tr  = a1 + 2*a2
      HS2 = a1 + 4*a2 + 2*p*c^2
      m3  = a1 + 8*a2 + p*(c^3 + (-c)^3) = a1 + 8*a2   (planes cancel!)
    With real data (tr,HS2)=(N,4N/3): a1 = N - 2a2, p = (N/3 - 2a2)/2, a2 in [0,N/6].
    So m3/N ranges over [1,2] across the family: two moments underdetermine the
    mixture; the third moment completes identification (3 equations, 3 unknowns).

(b) Empirical Gram-matrix moments of the first 1000 LMFDB zeros (flat window
    lambda=1 and cosine window), vs the ideal-model predictions:
      all-simple world: m3 = 1; extremal law: m3 = 2; GUE/HL*: m3 = 2.
    The empirical value near 2 despite all zeros being simple quantifies the
    off-diagonal (cross-term) pollution of the third moment -- the size of the
    "second-moment gap" in disguise.

Run:  uv run --quiet python mixture_id.py
"""
import numpy as np

SQRT2 = np.sqrt(2.0)
PI = np.pi

print("=== B3.1 (a) count-level mixture model ===")
N = 6.0  # use a concrete N; scale-invariant below
a2 = np.linspace(0.0, N / 6.0, 1001)
a1 = N - 2 * a2
p = (N / 3.0 - 2 * a2) / 2.0
m3 = a1 + 8 * a2
assert np.all(p >= 0) and np.all(a1 >= 0)
print(f"mixture family from (tr,HS2)=(N,4N/3) with c=1: a2 in [0,{N/6:.2f}], "
      f"p = (N/3 - 2*a2)/2 >= 0")
print(f"  m3/N ranges over [{m3.min()/N:.4f}, {m3.max()/N:.4f}] across the family "
      f"(all-simple a2=0 -> m3/N=1 ; extremal a2=N/6 -> m3/N=2)")
print("  -> two moments leave a 1-parameter family; the third moment (skewness)")
print("     completes identification: this is the mixture-identifiability structure.")
print("  -> but note: in the IDEAL model m3 is blind to p (planes cancel); the")
print("     off-diagonal cross-terms are exactly what the real data add (part b).")

# ---------------- (b) empirical moments on real zeros ----------------
print("\n=== B3.1 (b) empirical Gram-matrix moments, first 1000 LMFDB zeros ===")
zs = np.loadtxt('/home/vstaln/riemann/tools/data/zeros_1_1000.txt')[:, 1]
# normalized ordinates, unit density (same convention as tools/empirical_m3.py)
x = (zs / (2 * PI)) * np.log(zs / (2 * PI)) - zs / (2 * PI) + 7 / 8
n = x.size
d = x[:, None] - x[None, :]
print(f"N={n}, x in [{x[0]:.2f}, {x[-1]:.2f}], mean spacing {np.mean(np.diff(x)):.4f}")

def trace_moments(G):
    n = G.shape[0]
    G2 = G @ G; G3 = G2 @ G; G4 = G3 @ G
    return (np.trace(G2) / n, np.trace(G3) / n, np.trace(G4) / n)

# flat window, lambda = 1 (sine kernel on unit-density ordinates)
Gf = np.sinc(d)                       # np.sinc(t)=sin(pi t)/(pi t)
m2f, m3f, m4f = trace_moments(Gf)
print(f"flat window lam=1:  m2={m2f:.6f}  m3={m3f:.6f}  m4={m4f:.6f}")

# cosine window: K_c(u) = 1/2 sinc(u) + 1/4 [sinc(u - sqrt2/pi) + sinc(u + sqrt2/pi)]
a = SQRT2 / PI
Gc = 0.5 * np.sinc(d) + 0.25 * (np.sinc(d - a) + np.sinc(d + a))
m2c, m3c, m4c = trace_moments(Gc)
print(f"cosine window:     m2={m2c:.6f}  m3={m3c:.6f}  m4={m4c:.6f}")

print("\npredictions:  ideal-model all-simple m3 = 1 ; extremal law m3 = 2 ;")
print("              GUE/HL* m2 = 4/3 = 1.3333, m3 = 2, m4 = 13/4 = 3.25")
print(f"empirical excess of m3 over the all-simple ideal value 1:")
print(f"  flat:    m3 - 1 = {m3f - 1:.4f}   (fraction of the m3=1..2 gap: {(m3f-1)/1:.4f})")
print(f"  cosine:  m3 - 1 = {m3c - 1:.4f}")
print(f"empirical m4 vs extremal law m4 = 10/3 = {10/3:.6f} and GUE 13/4 = {13/4:.6f}:")
print(f"  flat:    {m4f:.4f}   cosine: {m4c:.4f}")
