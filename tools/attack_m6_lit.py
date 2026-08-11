#!/usr/bin/env python3
"""attack_m6_lit.py — 6th-moment literature-verification numerics (EXECUTIONER, Round LM1).

Produces every number in research/notes/attack-m6-literature.md.

Parts:
  A. Exact sine-kernel Gram-matrix moments m1..m3(lambda) via VERIFIED closed forms
     (m2 = 1/lambda + lambda/3  [Montgomery, PROVEN];
      m3 = 3 + 3/la + 1/la^2 - la - 6 J2(la)(1 + 1/la)  [program-verified, attack-thirdmoment.md])
  B. Christoffel function Lambda_m(0) from a moment vector (mu0=1, m1..m_{2m})
     via the Hankel-matrix normal equations, in mpmath (high precision).
     Cross-checks: Lambda_1(0) = 1 - 1/m2 (analytic); paper's Lambda_2(0;1) = 5/36.
  C. Implied constants:
        CMS:     n_theta(G)/d  >= 1 - Lambda_m(0)                       [7.5(d)]
        Prop4.5: p1 >= 2*lambda*(1 - Lambda_m(0)) - 1  (d = lambda*N)   [7.5(f) count]
  D. Atom LP (scipy linprog): min mu({1}) over measures on {0,1,2,...} with the
     moments — the direct moment+integrality bound on simple zeros.
  E. (separate script) sine-process MC for m4..m6.
Run: uv run --quiet --with mpmath --with numpy --with scipy python tools/attack_m6_lit.py
"""
import mpmath as mp
from mpmath import mpf, quad, inf
import numpy as np
mp.mp.dps = 40

# ---------- Part A: exact m1..m3 ----------
def S(u): return mp.sinc(mp.pi*u)
def K(u, la): return mp.sinc(mp.pi*la*u)
def J2(la):
    # J2(la) = int_0^inf sinc(pi la u)^2 sinc(pi u)^2 du   (verified: J2(1)=1/3, J2(2/3)=7/18, J2(1/2)=5/12)
    return quad(lambda u: K(u, la)**2 * S(u)**2, [0, inf])

def moments_exact(la):
    m1 = mpf(1)
    m2 = 1/la + la/3
    J = J2(la)
    m3 = 3 + 3/la + 1/la**2 - la - 6*J*(1 + 1/la)
    return m1, m2, m3, J

# ---------- Part B: Christoffel Lambda_m(0) ----------
def christoffel(mom, deg):
    """mom = [mu_0, mu_1, ..., mu_{2*deg}].  Lambda_deg(0) = mu_0 - b^T H^{-1} b,
    H_{ij} = mu_{i+j} (i,j=1..deg), b_i = mu_i."""
    mu = [mpf(x) for x in mom]
    H = mp.matrix(deg, deg)
    b = mp.matrix(deg, 1)
    for i in range(deg):
        b[i, 0] = mu[i+1]
        for j in range(deg):
            H[i, j] = mu[i+j+2]          # mu_{i+j+2}: index (i+1)+(j+1) = i+j+2
    Hinv = H**-1
    lam = mu[0] - (b.T * Hinv * b)[0, 0]
    return float(lam)

print("="*78)
print("PART A+B: exact sine-kernel moments + Christoffel functions")
print("="*78)
print(f"{'lambda':>8} {'m1':>7} {'m2':>10} {'m3':>10} {'J2':>10} {'Lam1(0)':>9} {'Lam2(0)':>9} {'1-Lam1':>8} {'1-Lam2':>8} {'p1>=2l(1-Lam2)-1':>18}")
for la in (mpf('0.25'), mpf('1')/3, mpf('0.5'), mpf('2')/3, mpf('0.8'), mpf('1')):
    m1, m2, m3, J = moments_exact(la)
    mom4 = [1, m1, m2, m3]   # for Lambda_2 need m4 too; use paper's m4 at la=1, and report
    L1 = christoffel([1, m1, m2], 1)
    # Lambda_2 needs m4: paper value 13/4 at la=1; for la<1 use m4(la) later (Part D/E).
    row = (f"{float(la):8.4f} {float(m1):7.2f} {float(m2):10.5f} {float(m3):10.5f} {float(J):10.5f} "
           f"{L1:9.6f}")
    print(row)
    # sanity: Lambda_1(0) analytic = 1 - 1/m2
    assert abs(L1 - (1 - 1/float(m2))) < 1e-9, "Lambda_1 mismatch"

print()
print("Lambda_2(0) with m4 variants at lambda = 1  (paper 13/4 vs program 346/105):")
for name, m4 in [("paper 13/4", mpf(13)/4), ("program 346/105", mpf(346)/105), ("extremal 10/3", mpf(10)/3)]:
    L2 = christoffel([1, 1, mpf(4)/3, 2, m4], 2)
    print(f"  m4 = {name} = {float(m4):.6f}:  Lambda_2(0) = {L2:.8f}  1-Lambda_2 = {1-L2:.8f}  "
          f"1-2*Lambda_2 = {1-2*L2:.8f}   (paper Lambda_2(0;1) = 5/36 = {5/36:.6f})")

print()
print("="*78)
print("PART C: Christoffel-route constants at lambda = 1/4, 1/3 (k=4,6 inputs)")
print("="*78)
print("Structural fact (PROVEN, paper Prop 4.5 + Prop 7.4): p1 >= 2*lambda*(1-Lambda_m(0)) - 1.")
print("d = lambda*N (rank cap Prop 7.4); for lambda <= 1/2 the count 2n+/d - 1 is void.")
print()
print(f"{'lambda':>8} {'Lam2(0;m4=13/4)':>18} {'Lam2(0;m4=346/105)':>20} {'2l(1-Lam2)-1 (13/4)':>20} {'2l(1-Lam2)-1 (346/105)':>22}")

def table_row(la, m2, m3):
    out = [f"{float(la):8.4f}"]
    for m4 in (mpf(13)/4, mpf(346)/105):
        L2 = christoffel([1, 1, m2, m3, m4], 2)
        c = 2*la*(1 - L2) - 1
        out.append(f"{L2:18.8f}")
    for m4 in (mpf(13)/4, mpf(346)/105):
        L2 = christoffel([1, 1, m2, m3, m4], 2)
        c = 2*la*(1 - L2) - 1
        out.append(f"{float(c):20.6f}")
    print(" ".join(out))

for la in (mpf('0.25'), mpf('1')/3):
    m1, m2, m3, J = moments_exact(la)
    table_row(la, m2, m3)
print("(Both constants NEGATIVE: the Prop 4.5 count is void at lambda <= 1/2 — the Cap, Prop 7.4.)")

print()
print("="*78)
print("PART D: atom LP — min mu({1}) over measures on {0,1,2,3,...} with the moments")
print("(support = eigenvalues m_rho in {0,1,2,...}; simple zeros = eigenvalue 1)")
print("="*78)
try:
    from scipy.optimize import linprog
    K = 40  # eigenvalues 0..K
    def atom_lp(moments):
        # variables: mu_0..mu_K (K+1), objective: mu_1
        A_eq = [[1.0]*(K+1)]
        for r in range(1, len(moments)):
            A_eq.append([float(j**r) for j in range(K+1)])
        res = linprog([0,1]+[0]*(K-1), A_eq=A_eq, b_eq=[float(x) for x in moments],
                      bounds=[(0,None)]*(K+1), method="highs")
        return res.fun if res.success else float('nan')
    for name, mom in [("paper (1,4/3,2,13/4)", [1, 1, mpf(4)/3, 2, mpf(13)/4]),
                      ("program (1,4/3,2,346/105)", [1, 1, mpf(4)/3, 2, mpf(346)/105])]:
        v = atom_lp(mom)
        print(f"  {name}:  min mu({{1}}) = {v:.6f}   (paper claim via Prop 4.5 count: 13/18 = {13/18:.6f})")
    print("  Note: extremal config {2/3@1, 1/6@2, 1/6@0} has m4 = 10/3 != 13/4, so it is NOT")
    print("  admissible for the paper's 4-moment data (m4 mismatch) — no contradiction with 13/18.")
except ImportError:
    print("  scipy not available; skipped")
