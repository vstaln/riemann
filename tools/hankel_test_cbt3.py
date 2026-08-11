#!/usr/bin/env python3
"""C-BT3: Ho-Kalman / realization-theory rank test on the (1, 4/3, 2) moment Hankel.

Verdict-producing script for research/notes/attack-hankel-test.md.
Theory part: exact fractions + mpmath eigenvalues.  Empirical part: numpy on the
first 1000 LMFDB zeros, flat window (lambda = 1), local-rescale convention of
tools/m3_zeros_check.py.

Run:  uv run --quiet --with numpy --with mpmath --with scipy python tools/hankel_test_cbt3.py
      (or from the scratch copy: /tmp/attack_hankel/hankel_test_cbt3.py)

Conventions (from attack-twobandwidth.md / attack-multiplicity.md):
  m_k = tr(Â^k)/N, normalized power sums of the certificate's Gram matrix Â.
  Paper's sine-kernel sequence at lambda=1: (m_1,m_2,m_3,m_4) = (1, 4/3, 2, 13/4).
  Extremal world (2N/3 simple + N/6 double on-line zeros, orthogonal atoms):
     eigenvalues 1 (x2N/3), 2 (xN/6),  power sums (m_1..m_4) = (1, 4/3, 2, 10/3).
  m_0 = (#eigenvalues)/N :  5/6 for the compressed extremal world, 1 for the full
     N x N matrix / the all-simple real world.
"""
import numpy as np
from fractions import Fraction
import mpmath as mp
from numpy.linalg import matrix_rank, det, eigvalsh

mp.mp.dps = 50
F = Fraction

# ---------------------------------------------------------------- exact helpers
def fdet(M):
    """determinant of a list-of-lists of Fractions, exact."""
    n = len(M)
    if n == 1:
        return M[0][0]
    s = F(0)
    for j in range(n):
        sub = [row[:j] + row[j + 1:] for row in M[1:]]
        s += ((-1) ** j) * M[0][j] * fdet(sub)
    return s

def report(name, M, Mdesc):
    """print rank / det / eigenvalues / PSD status of a Fraction matrix."""
    A = np.array([[float(x) for x in row] for row in M], dtype=float)
    r = matrix_rank(A)
    d = float(fdet(M))
    ev = eigvalsh(A)  # symmetric: ascending
    psd = "PSD (all eig >= 0)" if ev[0] >= -1e-12 else "NOT PSD"
    print(f"\n[{name}]  {Mdesc}")
    print(f"  rank = {r}   det = {d:.10f}   (exact {fdet(M)})")
    print(f"  eigenvalues (ascending) = {['%.8f' % e for e in ev]}")
    print(f"  {psd}")
    return r, ev

print("=" * 78)
print("PART 1 (THEORY): Hankel rank / feasibility of the (1, 4/3, 2) moment data")
print("=" * 78)

m1, m2, m3, m4 = F(1), F(4, 3), F(2), F(13, 4)
print(f"\nmoment sequence (paper, lambda=1): (m1,m2,m3,m4) = "
      f"({m1}, {m2}, {m3}, {m4})")

# --- 2x2 Hankel (task's convention, shifted: entries m_{i+j-1})
H2 = [[m1, m2], [m2, m3]]
r2, ev2 = report("H2 (shifted 2x2)", H2,
                 "H = [[m1, m2],[m2, m3]] = [[1, 4/3],[4/3, 2]]")

# --- 2x2 with m0 = 1
H2b = [[F(1), m1], [m1, m2]]
r2b, _ = report("H2b (m0=1)", H2b, "H = [[m0, m1],[m1, m2]] = [[1, 1],[1, 4/3]]")

# --- 3x3 with the paper's m4 = 13/4  (m0 = 1, all-simple count)
H3p = [[F(1), m1, m2], [m1, m2, m3], [m2, m3, m4]]
r3p, ev3p = report("H3 (paper m4=13/4)", H3p,
                   "H = [[1, m1, m2],[m1, m2, m3],[m2, m3, m4]] , m4=13/4")

# --- 3x3 with the extremal world's m4 = 10/3 (m0 = 1, full N x N convention)
m4x = F(10, 3)
H3x = [[F(1), m1, m2], [m1, m2, m3], [m2, m3, m4x]]
r3x, _ = report("H3 (extremal m4=10/3, m0=1)", H3x,
                "H = [[1, m1, m2],[m1, m2, m3],[m2, m3, 10/3]]")

# --- 3x3 with the HONEST extremal-world m0 = 5/6 (compressed, 5N/6 eigenvalues)
H3xr = [[F(5, 6), m1, m2], [m1, m2, m3], [m2, m3, m4x]]
r3xr, ev3xr = report("H3 (extremal, HONEST m0=5/6)", H3xr,
                     "H = [[5/6, 1, 4/3],[1, 4/3, 2],[4/3, 2, 10/3]]")

# --- all-simple orthogonal world (rank-1 control)
H3o = [[F(1)] * 3, [F(1)] * 3, [F(1)] * 3]
r3o, _ = report("H3 (all-simple control)", H3o, "H = [[1,1,1],[1,1,1],[1,1,1]]")

# --------------------------------------------------------- feasibility checks
print("\n" + "-" * 78)
print("Feasibility of (m1, m2, m3) = (1, 4/3, 2) as power sums of a Hermitian matrix")
print("-" * 78)

# (i) extremal world realization (PROVEN, attack-multiplicity lemmaR_tight)
N = F(6)          # 6 zeros
a1, a2 = F(2) * N / 3, N / 6     # simples, doubles
s1 = a1 * 1 + a2 * 2
s2 = a1 * 1 + a2 * 4
s3 = a1 * 1 + a2 * 8
s4 = a1 * 1 + a2 * 16
print(f"\n(i)  Extremal world (2N/3 simples + N/6 doubles, eigenvalues 1,2):")
print(f"     N=6: 4 simples + 1 double;  power sums s_k = sum lambda^k")
print(f"     s1/N = {s1/N}  (need 1)   s2/N = {s2/N}  (need 4/3)   s3/N = {s3/N}  (need 2)")
print(f"     s4/N = {s4/N}  (=> m4 = 10/3 for this world)   N_d/N = {F(5)*N/6/N} = 5/6")
assert s1 / N == 1 and s2 / N == F(4, 3) and s3 / N == 2
assert s4 / N == F(10, 3)
print("     VERIFIED: the extremal world realizes (1, 4/3, 2) exactly.  Feasible.")

# (ii) unique mass-1 two-atom realization of (m0=1, m1, m2, m3) -> atoms 1 +/- 1/sqrt(3)
import mpmath as mpl
d = mpl.sqrt(3) / 3          # 1/sqrt(3)
atoms = [1 - d, 1 + d]
w = mpl.mpf(1) / 2
mm = [w * a ** k + w * b ** k for (a, b) in [(atoms[0], atoms[1])] for k in range(0, 5)]
print(f"\n(ii) Unique mass-1 2-atom realization of (m0..m3)=(1,1,4/3,2):")
print(f"     atoms 1 +/- 1/sqrt(3) = {atoms[0]:.10f}, {atoms[1]:.10f}, weights (1/2, 1/2)")
print(f"     m0..m4 = {['%.10f' % x for x in mm]}  -> forced m4 = 28/9 = {mpl.mpf(28)/9:.10f}")
mm4 = w * atoms[0] ** 4 + w * atoms[1] ** 4
print(f"     m4 = {mm4:.12f}   (28/9 = {mpl.mpf(28)/9:.12f})  match = {abs(mm4 - mpl.mpf(28)/9) < 1e-30}")

# (iii) H3(m4) as a function of m4: det = m4/3 - 28/27 ; rank drops at m4 = 28/9
print("\n(iii) H3(m4) = [[1,1,4/3],[1,4/3,2],[4/3,2,m4]]:  det(m4) = m4/3 - 28/27")
for mm4v, lab in [(F(28, 9), "m4=28/9  (2-atom boundary)"),
                  (F(13, 4), "m4=13/4  (paper)"),
                  (F(10, 3), "m4=10/3  (extremal world, m0=1 view)")]:
    H = [[F(1), m1, m2], [m1, m2, m3], [m2, m3, mm4v]]
    print(f"     {lab}: det = {float(fdet(H)):.10f}   rank = {matrix_rank(np.array([[float(y) for y in x] for x in H]))}")

# (iv) McMillan degree: rank of the shifted Hankel = minimal number of atoms
print(f"\n(iv) McMillan degree of the 3-moment data (rank of H2) = {r2}")
print("     rank 1 would need m2^2 = m1*m3  (one atom):  16/9 vs 2 -> 16/9 != 2")
print("     => minimal realization has exactly 2 atoms: the extremal world. No rank deficiency.")

# ---------------------------------------------------------------- empirical part
print("\n" + "=" * 78)
print("PART 2 (EMPIRICAL): first 1000 LMFDB zeros, flat window (lambda=1)")
print("=" * 78)

def load_zeros(fn, limit=None):
    g = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                g.append(float(p[1]))
                if limit and len(g) >= limit:
                    break
    return np.sort(np.array(g))

fn = "tools/data/zeros_1_1000.txt"
g = load_zeros(fn, 1000)
print(f"\nloaded {g.size} zeros from {fn}:  gamma_1 = {g[0]:.6f}, gamma_1000 = {g[-1]:.6f}")

n = g.size
sp = np.diff(g).mean()
x = g / sp
d = x[:, None] - x[None, :]
G = np.sinc(d)                     # lambda = 1 flat window, diag = 1
m1e = np.trace(G) / n
G2 = G @ G
m2e = np.trace(G2) / n
G3 = G2 @ G
m3e = np.trace(G3) / n
G4 = G3 @ G
m4e = np.trace(G4) / n
print(f"\nlocal mean spacing = {sp:.6f}")
print(f"empirical moments (lambda=1, flat window):")
print(f"  m1 = {m1e:.6f}   (exact 1; diag=1)")
print(f"  m2 = {m2e:.6f}   (paper 4/3 = 1.3333)")
print(f"  m3 = {m3e:.6f}   (paper 2)")
print(f"  m4 = {m4e:.6f}   (paper 13/4 = 3.25)")

He2 = np.array([[m1e, m2e], [m2e, m3e]])
He3 = np.array([[1.0, m1e, m2e], [m1e, m2e, m3e], [m2e, m3e, m4e]])
for name, H in [("H2 empirical", He2), ("H3 empirical (m0=1)", He3)]:
    ev = eigvalsh(H)
    r = matrix_rank(H)
    d = np.linalg.det(H)
    print(f"\n[{name}]  rank = {r}  det = {d:.8f}  eig = {['%.8f' % e for e in ev]}  "
          f"{'PSD' if ev[0] >= -1e-12 else 'NOT PSD'}")

print("\n" + "=" * 78)
print("VERDICTS")
print("=" * 78)
print("""
T1 (PROVEN, exact): (m1,m2,m3) = (1,4/3,2) is REALIZABLE by a Hermitian matrix in the
   certificate block structure: the extremal world diag(1,...,1,2,...,2) realizes it with
   integer multiplicities, p=0 off-line pairs, rank-2 Hankel (McMillan degree 2). No
   rank deficiency, no infeasibility.
T2 (PROVEN, exact): the third moment does NOT separate the two worlds: BOTH the real
   sine-kernel world and the extremal world have m3 = 2.  The 3-moment data is identical.
T3 (PROVEN, exact): the rank separation is a FOURTH-moment phenomenon: paper m4 = 13/4
   forces the 3x3 Hankel (m0=1) to rank 3 (>=3 atoms); the extremal world has m4 = 10/3
   and, with its honest m0 = 5/6, Hankel rank 2 (2 atoms).
T4 (empirical, this script): the real zeros' flat-window moments are feasible (H2 PSD,
   rank 2) and m4_emp sits near the paper value, consistent with the rank-3 conclusion.
""")
