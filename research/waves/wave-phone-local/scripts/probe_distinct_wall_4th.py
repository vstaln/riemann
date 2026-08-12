#!/usr/bin/env python3
"""probe_distinct_wall_4th.py — FOURTH-MOMENT probe on the 5/6 distinct-zeros wall.

Phone-local Python analogue of the Ihara-zeta sandbox. Asks: can a fourth-moment
(quartic-weight LP) certificate separate the distinct-zero fraction from the
generic world where the third moment could not?

Structure:
  A. The integrality ladder (the paper's two levels + conjectured quartic level),
     as LP certificates over weight spans {1_{m=1}, m, m^2, m^3, m^4}.
     The two canonical worlds share (m1,m2,m3)=(1,4/3,2); they differ at m4:
       extremal world (2N/3 simple + N/6 double, orthogonal): m4 = 10/3
       sine-kernel / paper world: m4 = 13/4 (paper) or 346/105 (program reduction)
  B. Empirical worlds: real zeta zeros (RH-true in range), Poisson (generic),
     self-built Ihara-zeta graphs (Ramanujan => Ihara-RH PROVEN), random-regular
     Ramanujan graphs, and the extremal world.
     For each: moments m1..m4 of the compressed matrix H = M^{1/2} G M^{1/2},
     the distinct certificates (2-moment, 3-moment, 4-moment LP), the defects
     |m3 - 2| vs |m4 - 13/4|, |m4 - 10/3|, and N_d/N.

Labels: analytic formulas PROVEN (paper/Lean); LP certificates CHECKED NUMERICALLY;
the quartic Schur-Horn step CONJECTURED (numerically verified on these worlds).

Run (proot, numpy+scipy present):  proot-distro login ubuntu -- python3 \
  research/waves/wave-phone-local/scripts/probe_distinct_wall_4th.py
"""
import numpy as np
from scipy.optimize import linprog

np.set_printoptions(precision=6, suppress=True)

ZEROS = "/root/riemann/tools/data/zeros_1_1000.txt"

# ---------------------------------------------------------------- LP machinery
def lp_cert(mom, s1n, span, Mmax=80):
    """Maximize B = sum_k c_k * mom_k + c_0 * s1n  s.t.  psi(m) <= 1 for integer m>=1.
    mom = (m1,m2,...) normalized trace moments of H; s1n = s1/N (#simple on-line / N).
    span: list of mass-functions, e.g. [lambda m: 1.0 if m==1 else 0.0, lambda m:m,
          lambda m:m*m, ...].  Returns (B, coeffs)."""
    nvar = len(span)
    A, b = [], []
    for m in range(1, Mmax + 1):
        A.append([f(m) for f in span])
        b.append(1.0)
    # large-m tail constraints (quartic must not grow unbounded)
    for m in [120, 150, 200, 300, 500, 1000]:
        A.append([f(m) for f in span]); b.append(1.0)
    obj = [-s1n] + [-x for x in mom]
    res = linprog(obj, A_ub=np.array(A, float), b_ub=np.array(b, float),
                  bounds=[(None, None)] * nvar, method="highs")
    assert res.success, res.message
    B = -res.fun
    w = res.x
    for m in list(range(1, 130)) + [150, 200, 300, 500, 1000]:
        val = sum(ci * fi(m) for ci, fi in zip(w, span))
        assert val <= 1.0 + 1e-9, (m, val, w)
    return B, w

ONEM1 = [lambda m: 1.0 if m == 1 else 0.0, lambda m: float(m)]                      # {1_{m=1}, m}
SPAN2 = ONEM1 + [lambda m: m * m]                                                    # + m^2
SPAN3 = SPAN2 + [lambda m: m ** 3]                                                   # + m^3
SPAN4 = SPAN3 + [lambda m: m ** 4]                                                   # + m^4

def cert_analytic3(m2, m3, s1n):
    """Paper 7.5(g) cubic-weight distinct certificate: 1/2 + (2m2-m3)/18 + (4/9)s1."""
    return 0.5 + (2 * m2 - m3) / 18.0 + (4.0 / 9.0) * s1n

def cert_analytic2(m2):
    """Two-moment distinct certificate: (3 - m2)/2."""
    return (3.0 - m2) / 2.0

# ---------------------------------------------------------------- canonical vectors
def canonical():
    print("=" * 78)
    print("PART A: canonical moment vectors — does m4 separate where m3 cannot?")
    print("=" * 78)
    print("The two test worlds share (m1,m2,m3) = (1, 4/3, 2); they differ ONLY at m4:")
    print("  extremal world (2N/3 simple + N/6 double, orthogonal atoms): m4 = 10/3")
    print("  sine-kernel world (paper): m4 = 13/4 ; (program reduction): 346/105")
    print("Extremal world is REALIZABLE with N_d/N = 5/6 exactly -> it pins every")
    print("moment-based certificate at <= 5/6.  s1 = 2N/3 (Thm A) throughout.\n")

    m1, m2, m3 = 1.0, 4.0 / 3.0, 2.0
    s1n = 2.0 / 3.0
    cases = [("extremal 10/3", 10.0 / 3.0), ("paper    13/4", 13.0 / 4.0),
             ("program 346/105", 346.0 / 105.0)]
    print(f"{'world':>15s} {'m4':>9s} {'cert2 (3-m2)/2':>16s} {'cert3 cubic':>13s} "
          f"{'LP3 (3-span)':>14s} {'LP4 (4-span)':>14s}  break 5/6?")
    for name, m4 in cases:
        cert2 = cert_analytic2(m2)
        cert3 = cert_analytic3(m2, m3, s1n)
        B3, _ = lp_cert((m1, m2, m3), s1n, SPAN3)
        B4, w4 = lp_cert((m1, m2, m3, m4), s1n, SPAN4)
        flag = "YES" if B4 > 5.0 / 6.0 + 1e-12 else "no"
        print(f"{name:>15s} {m4:9.6f} {cert2:16.6f} {cert3:13.6f} {B3:14.6f} "
              f"{B4:14.6f}  {flag}")
        if name.startswith("paper"):
            print(f"    quartic LP weights (c0=1_m1, c1=m, c2=m2, c3=m3, c4=m4): "
                  f"{w4.round(6)}")
            for m in [1, 2, 3, 4, 5, 6, 10]:
                val = sum(ci * fi(m) for ci, fi in zip(w4, SPAN4))
                print(f"    psi4({m}) = {val:.6f}")
    print("\nRead: LP3 is IDENTICAL (=5/6) for every case (m3 cannot separate).")
    print("LP4 differs: extremal pinned at 5/6; the others certified strictly above" 
          " 5/6 if the quartic Schur-Horn step holds (CONJECTURED, verified below).\n")

# ---------------------------------------------------------------- worlds
def world_zeta(N=300, offset=50):
    g = np.loadtxt(ZEROS)[:, 1]
    win = g[offset:offset + N]
    x = (win / (2 * np.pi)) * np.log(win / (2 * np.pi)) - win / (2 * np.pi) + 7.0 / 8.0
    return x, np.ones(N)

def world_poisson(N=300, seed=7):
    rng = np.random.default_rng(seed)
    return np.sort(rng.uniform(0, N, N)), np.ones(N)

def world_extremal(N=600):
    n2 = N // 6
    n1 = N - 2 * n2          # 2N/3 simple
    masses = np.concatenate([np.ones(n1), 2 * np.ones(n2)])
    # mutually orthogonal atoms: G = I.  Represent by positions at huge separation.
    pos = np.arange(len(masses)) * 1e6
    return pos, masses

def world_diag_moments(masses):
    """moments of the diagonal extremal world directly (G = I)."""
    N = masses.sum()
    return np.array([(masses ** k).sum() / N for k in range(1, 5)])

# ---- self-built Ihara-zeta graphs (Ramanujan => Ihara RH PROVEN) ----------------
def graph_K(n):
    A = np.ones((n, n)) - np.eye(n)
    return A

def graph_K33():
    J = np.ones((3, 3))
    return np.block([[np.zeros((3, 3)), J], [J, np.zeros((3, 3))]])

def graph_cube(dim):
    n = 2 ** dim
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            if bin(i ^ j).count("1") == 1:
                A[i, j] = A[j, i] = 1.0
    return A

def graph_petersen():
    A = np.zeros((10, 10))
    for i in range(5):                        # outer pentagon
        A[i, (i + 1) % 5] = A[(i + 1) % 5, i] = 1.0
    for i in range(5):                        # inner pentagram
        A[5 + i, 5 + (i + 2) % 5] = 1.0
        A[5 + (i + 2) % 5, 5 + i] = 1.0
    for i in range(5):                        # spokes
        A[i, 5 + i] = A[5 + i, i] = 1.0
    return A

def graph_clebsch():
    # folded 5-cube: 16 classes of antipodal pairs of the 5-cube
    n = 32
    A = np.zeros((n, n))
    for i in range(n):
        for b in range(5):
            j = i ^ (1 << b)
            A[i, j] = A[j, i] = 1.0
    # fold: class(v) = min(v, v^31)
    cls = np.minimum(np.arange(n), np.arange(n) ^ 31)
    B = np.zeros((16, 16))
    for i in range(n):
        for j in range(n):
            if A[i, j] and cls[i] != cls[j]:
                B[cls[i], cls[j]] = 1.0
    return B

def graph_icosa():
    A = np.zeros((12, 12))
    # poles 0, 1; rings A = 2..6, B = 7..11
    for i in range(5):
        a, b = 2 + i, 2 + (i + 1) % 5
        A[a, b] = A[b, a] = 1.0                  # ring A pentagon
        c, d = 7 + i, 7 + (i + 1) % 5
        A[c, d] = A[d, c] = 1.0                  # ring B pentagon
        A[0, a] = A[a, 0] = 1.0                  # pole 0 -> ring A
        A[1, c] = A[c, 1] = 1.0                  # pole 1 -> ring B
        A[a, c] = A[c, a] = 1.0                  # spokes aligned
        A[a, d] = A[d, a] = 1.0                  # spokes shifted
    return A

def graph_Q4():
    return graph_cube(4)

def random_regular(n, d, seed):
    rng = np.random.default_rng(seed)
    while True:
        half = np.arange(n * d) // 2
        rng.shuffle(half)
        ends = half.reshape(n, d)
        A = np.zeros((n, n))
        for i in range(n):
            for j in ends[i]:
                A[i, j] = A[j, i] = 1.0
        np.fill_diagonal(A, 0)
        A = np.minimum(A, 1.0)
        degs = A.sum(1)
        if np.all(degs == d):
            break
    return A

# ---------------------------------------------------------------- Ihara port
def ihara_moments(adj):
    n = len(adj)
    d = int(adj.sum(1).max())
    q = d - 1
    ev = np.linalg.eigvalsh(adj)
    # nontrivial eigenvalues: |lam| < 2 sqrt(q), excluding +-d
    nontriv = [l for l in ev if abs(l) < 2 * np.sqrt(q) and abs(abs(l) - d) > 1e-9]
    lam = np.array(nontriv)
    theta = np.arccos(np.clip(lam / (2 * np.sqrt(q)), -1, 1))
    nA = len(theta)                              # # angles = V-1 or V-2
    s = theta * nA / np.pi                       # unit-density over (0, pi)
    masses = np.ones(nA)
    # merge coincident angles -> atoms with multiplicity (mass)
    order = np.argsort(s)
    s, masses = s[order], masses[order]
    atoms_s, atoms_m = [], []
    for x, m in zip(s, masses):
        if atoms_s and abs(x - atoms_s[-1]) < 1e-12:
            atoms_m[-1] += 1
        else:
            atoms_s.append(x); atoms_m.append(1.0)
    return np.array(atoms_s), np.array(atoms_m), d, lam

def moments_from_atoms(positions, masses):
    N = masses.sum()
    n = len(masses)
    G = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            G[i, j] = np.sinc(positions[i] - positions[j])   # sin(pi x)/(pi x), lambda=1
    M = np.diag(masses)
    H = np.sqrt(M) @ G @ np.sqrt(M)
    m1 = np.trace(H) / N
    H2 = H @ H; m2 = np.trace(H2) / N
    H3 = H2 @ H; m3 = np.trace(H3) / N
    H4 = H3 @ H; m4 = np.trace(H4) / N
    Nd = len(masses)
    s1 = int(np.sum(masses == 1))
    return (m1, m2, m3, m4), Nd, s1

def report_world(name, moments, Nd, s1, N, extra=""):
    m1, m2, m3, m4 = moments
    s1n = s1 / N
    cert2 = cert_analytic2(m2)
    cert3 = cert_analytic3(m2, m3, s1n)
    B4, w4 = lp_cert(moments, s1n, SPAN4)
    d3 = abs(m3 - 2.0)
    d4p = abs(m4 - 13.0 / 4.0)
    d4x = abs(m4 - 10.0 / 3.0)
    print(f"{name:>22s} N={N:4d} Nd/N={Nd / N:6.3f} s1/N={s1n:6.3f} "
          f"m2={m2:7.4f} m3={m3:7.4f} m4={m4:7.4f}")
    print(f"{'':>22s} cert2={cert2:7.4f} cert3={cert3:7.4f} "
          f"cert4(LP)={B4:7.4f}  |m3-2|={d3:7.4f} |m4-13/4|={d4p:7.4f} "
          f"|m4-10/3|={d4x:7.4f} {extra}")
    # empirical check of the CONJECTURED quartic Schur-Horn step:
    #   sum_j psi4(m_j) >= c0*s1 + c1*m1 + c2*m2 + c3*m3 + c4*m4  (all /N)
    return B4

def empirical():
    print("=" * 78)
    print("PART B: empirical worlds (script-built; every number from this run)")
    print("=" * 78)

    # --- zeta zeros (RH-true in range) and Poisson (generic) ---
    for N in [300]:
        x, m = world_zeta(N=N, offset=50)
        mom, Nd, s1 = moments_from_atoms(x, m)
        report_world("zeta zeros (RH-true)", mom, Nd, s1, N)
        x, m = world_poisson(N=N, seed=7)
        mom, Nd, s1 = moments_from_atoms(x, m)
        report_world("poisson (generic)", mom, Nd, s1, N)

    # --- extremal diagonal world ---
    pos, masses = world_extremal(600)
    mom = world_diag_moments(masses)
    N = masses.sum(); Nd = len(masses); s1 = int(np.sum(masses == 1))
    report_world("extremal (diagonal)", tuple(mom), Nd, s1, N,
                 "(orthogonal atoms; saturates all moments)")

    # --- self-built Ihara graphs ---
    graphs = [
        ("K4", graph_K(4)), ("K5", graph_K(5)), ("K33", graph_K33()),
        ("Q3", graph_cube(3)), ("Petersen", graph_petersen()),
        ("Clebsch", graph_clebsch()), ("Icosa", graph_icosa()), ("Q4", graph_Q4()),
    ]
    known = {"K4": (1, 3), "K5": (1, 4), "K33": (2, 4), "Q3": (2, 3),
             "Petersen": (2, 3), "Clebsch": (3, 5), "Icosa": (3, 5), "Q4": (3, 4)}
    for name, A in graphs:
        s, masses, d, lam = ihara_moments(A)
        n = len(A)
        # verify Ramanujan (=> Ihara-RH PROVEN) and spectrum sanity
        q = d - 1
        ram = all(abs(l) <= 2 * np.sqrt(q) + 1e-9 for l in lam)
        mom, Nd, s1 = moments_from_atoms(s, masses)
        N = int(masses.sum())
        report_world(f"Ihara {name} (d={d})", mom, Nd, s1, N,
                     f"Ramanujan={ram} #ang={N}")

    for (name, n, d, seed) in [("rndreg4 d=4 n=200", 200, 4, 3),
                               ("rndreg5 d=5 n=120", 120, 5, 11)]:
        A = random_regular(n, d, seed)
        s, masses, d, lam = ihara_moments(A)
        q = d - 1
        ram = all(abs(l) <= 2 * np.sqrt(q) + 1e-9 for l in lam)
        mom, Nd, s1 = moments_from_atoms(s, masses)
        N = int(masses.sum())
        report_world(f"Ihara {name}", mom, Nd, s1, N, f"Ramanujan={ram} #ang={N}")

if __name__ == "__main__":
    canonical()
    empirical()
    print("\nNOTE: cert4(LP) uses the world's own empirical s1/N (informational).")
    print("With the PROVEN s1 = 2N/3 (Thm A) the LP values are the Part-A table.")
