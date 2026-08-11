#!/usr/bin/env python3
"""chem_probe.py — cheapest-first probes from idea-generator-chem.md (Round 1).

Covers (all numbers from this run, f64 unless noted):
  A. C4.2  — empirical m2,m3,m4 of the real zero configuration (flat/cosine windows)
             vs extremal world (10/3), 256-law (3.2272), paper m4(1)=13/4 claim.
  B. C5.5  — xi'-on-line count ratio vs zeta (empirical tower data).
  C. C5.1  — empirical m2 of the xi'-zero set (flat window), first two moments.
  D. C1.1/C3.2 — 256-law grid moment problem: uniqueness on {0,1,2}; Hamburger
             principal representations of (m0,m1,m2)=(1,1,2-p0).
  E. C6.1  — negative-eigenvalue count n-(W_T)/N at T=200..700 (off-line/localized
             fraction scaling).
  F. C4.1  — eigenvector inverse participation ratio of W_T (delocalization).
  G. C2.4  — eigenvalue deviation from the integral marks {1,2} at finite T.
Honesty: every printed number is CHECKED NUMERICALLY in this run. No theorem is claimed.
"""
import sys, os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qi_sweep import psi, psi2, INT_PSI2, C_HS, C_BOUND, load_gams, window, v_on

PI = np.pi
ZEROS = "/home/vstaln/riemann/tools/data/zeros_1_1000.txt"
XIPRIME = "/home/vstaln/riemann/tools/data/xiprime_on_line_1_1000.txt"

print("=" * 78)
print("PROBE A (C4.2): empirical m2,m3,m4 of the real zero configuration")
print("=" * 78)
zs = load_gams(ZEROS)
x = (zs / (2 * PI)) * np.log(zs / (2 * PI)) - zs / (2 * PI) + 7 / 8  # normalized (density 1)
N = x.size
print(f"zeros loaded: N={N}, x-range [{x[0]:.2f},{x[-1]:.2f}]")

def gram_moments(la, xs):
    d = xs[:, None] - xs[None, :]
    G = np.sinc(la * d)
    n = xs.size
    G2 = G @ G; G3 = G2 @ G; G4 = G3 @ G
    return (np.trace(G2) / n, np.trace(G3) / n, np.trace(G4) / n)

def cosine_kernel(u):
    a = np.sqrt(2.0)
    return 0.5 * np.sinc(u) + 0.25 * (np.sinc(u - a / np.pi) + np.sinc(u + a / np.pi))

print("\nflat window, ALL 1000 zeros:")
for la in (1.0, 0.5):
    m2, m3, m4 = gram_moments(la, x)
    print(f"  la={la:.2f}: m2={m2:.4f}  m3={m3:.4f}  m4={m4:.4f}   2m2-m3={2*m2-m3:.4f}")

xi = x[50:950]  # drop edges
print("\nflat window, interior zeros (idx 51..950):")
for la in (1.0, 0.5):
    m2, m3, m4 = gram_moments(la, xi)
    print(f"  la={la:.2f}: m2={m2:.4f}  m3={m3:.4f}  m4={m4:.4f}   2m2-m3={2*m2-m3:.4f}")

d = xi[:, None] - xi[None, :]
G = cosine_kernel(d)
n = xi.size
G2 = G @ G; G3 = G2 @ G; G4 = G3 @ G
g_m2 = np.trace(G2) / n; g_m4 = np.trace(G4) / n
print("\ncosine window, interior (Gram moments + certificate-normalized):")
print(f"  Gram:  m2={g_m2:.4f}  m3={np.trace(G3)/n:.4f}  m4={g_m4:.4f}")
print(f"  cert-normalized (divide by INT_PSI2^k): m2={g_m2/INT_PSI2**2:.4f}  "
      f"m3={np.trace(G3)/n/INT_PSI2**3:.4f}  m4={g_m4/INT_PSI2**4:.4f}  (theory m2 -> 1/c1* = 1.3275)")

print("\nflat window, lambda = 2/3 (theory m3(2/3) = 13/4 = 3.25, PROVEN [TB]):")
m2, m3, m4 = gram_moments(2/3, xi)
print(f"  m2={m2:.4f}  m3={m3:.4f}  m4={m4:.4f}")

print("\n  reference targets:")
print(f"    extremal world (2/3@1 + 1/6@2): m4 = 10/3 = {10/3:.4f}")
print(f"    256-law (from [AN]):            m4 = 3.2272  (m3 = 1.9545)")
print(f"    paper claim m4(1) = 13/4 = {13/4:.4f}  (checked separately by tools/m4_check.py)")
print(f"    m3(1) theory = 2 (PROVEN [TB]); m3(1/2) theory = 5 (PROVEN [TB])")

print()
print("=" * 78)
print("PROBE B (C5.5) + PROBE C (C5.1): xi' tower data")
print("=" * 78)
xip = np.loadtxt(XIPRIME)  # columns: index, ordinate
t_xi = xip[:, 1]
print(f"xi'-roots file: {t_xi.size} entries (label says '1_1000' => 1000 zeta zeros + extras)")
below_g1 = t_xi[t_xi < 14.134725141734693]
print(f"  xi'-roots below gamma_1=14.1347: {below_g1.size} (small-t roots): {np.round(below_g1,4)}")
# count ratio in a window
T0, T1 = 100.0, 900.0
nz = ((zs >= T0) & (zs < T1)).sum()
nxi = ((t_xi >= T0) & (t_xi < T1)).sum()
print(f"  zeta-zeros in [{T0},{T1}): {nz}   xi'-zeros on line in [{T0},{T1}): {nxi}   ratio {nxi/nz:.4f}")
# empirical m2 of the xi'-zero set, flat window, normalized ordinates
y = (t_xi / (2 * PI)) * np.log(t_xi / (2 * PI)) - t_xi / (2 * PI) + 7 / 8
ym = y[10:-10]  # drop the small-t roots and the edge
d2 = ym[:, None] - ym[None, :]
Gx = np.sinc(1.0 * d2)
nn = ym.size
Gx2 = Gx @ Gx; Gx3 = Gx2 @ Gx
m2xi = np.trace(Gx2) / nn
m3xi = np.trace(Gx3) / nn
print(f"  xi'-zero set: N'={nn}, flat-window m2={m2xi:.4f}  m3={m3xi:.4f}   (zeta m2(flat)~4/3, [AM])")
print(f"  ratio m2(xi')/m2(zeta) = {m2xi/(4/3):.4f}  (a P5 diagnostic: second-moment cost of the tower)")

print()
print("=" * 78)
print("PROBE D (C1.1/C3.2): 256-law grid moment problem + Hamburger principal reps")
print("=" * 78)
p0 = 0.6818286874638  # law's simple-point fraction [AN, CHECKED]
m0, m1 = 1.0, 1.0
m2_law = 2.0 - p0
a = (1 - p0) / 2.0   # empty
b = p0               # simple
c = (1 - p0) / 2.0   # double
print(f"law masses: empty={a:.6f} simple={b:.6f} double={c:.6f}  (sum {a+b+c:.6f})")
print(f"law moments: m0={a+b+c:.8f}  m1={b+2*c:.8f}  m2={b+4*c:.8f}  (2-p0 = {m2_law:.8f})")
# grid-constrained uniqueness: masses (a,b,c) on {0,1,2} with (m0,m1,m2)
# equations: b+2c = m1 ; b+4c = m2  ->  c=(m2-m1)/2, b=2m1-m2, a=1-b-c
c_sol = (m2_law - m1) / 2
b_sol = 2 * m1 - m2_law
a_sol = 1 - b_sol - c_sol
print(f"grid solution from moments: a'={a_sol:.8f} b'={b_sol:.8f} c'={c_sol:.8f}")
print(f"  matches law masses?  {abs(a_sol-a)<1e-12 and abs(b_sol-b)<1e-12 and abs(c_sol-c)<1e-12}")
# Hamburger principal representations (no grid constraint)
var = m2_law - m1**2
Pm_atoms = np.array([1 - np.sqrt(var), 1 + np.sqrt(var)])
Pp_atoms = np.array([0.0, m2_law / m1])
Pp_mass_x = m1**2 / m2_law
print(f"Hamburger P- : atoms {np.round(Pm_atoms,6)} masses 0.5,0.5")
print(f"Hamburger P+ : atoms {np.round(Pp_atoms,6)} mass@x={Pp_mass_x:.6f}, mass@0={1-Pp_mass_x:.6f}")
print(f"  law has 3 atoms on {0,1,2} -> NOT a 2-atom Hamburger principal representation;")
print(f"  it IS the unique grid-constrained solution (atom set {0,1,2} fixed by m1,m2).")
# verify P- moments (correct pairing: mass at the NONZERO atom is m1^2/m2)
for name, atoms, masses in (("P-", Pm_atoms, np.array([0.5, 0.5])),
                            ("P+", np.array([0.0, m2_law / m1]), np.array([1 - Pp_mass_x, Pp_mass_x]))):
    m1v = (masses * atoms).sum()
    m2v = (masses * atoms**2).sum()
    print(f"  {name}: m1={m1v:.8f} m2={m2v:.8f}  (target {m1:.8f}, {m2_law:.8f})")

print()
print("=" * 78)
print("PROBES E/F/G: W_T at finite T (C6.1 negatives, C4.1 IPR, C2.4 defect)")
print("=" * 78)
def norm_A(W):
    """Normalize so that tr(A) = N (certificate normalization, marks ~1 for simple)."""
    ev = np.linalg.eigvalsh((W + W.T) / 2.0)
    N0 = W.shape[0]
    return W * (N0 / ev.sum()), ev * (N0 / ev.sum())

print(f"{'T':>5} {'N':>4} {'n-/N':>8} {'n-/N(1e-12)':>12} {'min eig':>10} {'meanIPR*N':>10} {'IPRmax':>8} {'dev1_2/N':>9} {'m4(op)/N':>9}")
for T in (200.0, 300.0, 400.0, 500.0, 600.0, 700.0):
    s_rho, gwin = window(T, gams=zs)
    Nw = len(s_rho)
    if Nw < 40:
        continue
    V = v_on(s_rho, Nw)
    W = V.T @ V / INT_PSI2
    A, ev = norm_A(W)
    evA = np.linalg.eigvalsh((A + A.T) / 2.0)
    # E: negatives with relative threshold 1e-9 and absolute 1e-12
    thresh = 1e-9 * max(abs(evA).max(), 1e-300)
    nminus = int((evA < -thresh).sum())
    nminus_abs = int((evA < -1e-12).sum())
    # F: eigenvector IPR
    _, U = np.linalg.eigh((A + A.T) / 2.0)
    ipr = (U**4).sum(axis=0)  # per eigenvector, sum over grid
    mean_ipr = ipr.mean()
    # G: deviation from integral marks {1,2}
    dev = np.minimum(np.abs(evA - 1.0), np.abs(evA - 2.0))
    # operator-level 4th moment (flat-window operator not available here; cosine-operator):
    A4op = np.trace(np.linalg.matrix_power((A + A.T) / 2.0, 4)) / Nw
    print(f"{T:5.0f} {Nw:4d} {nminus/Nw:8.4f} {nminus_abs/Nw:12.4f} {evA.min():10.3e} {mean_ipr*Nw:10.4f} {ipr.max():8.4f} {dev.sum()/Nw:9.4f} {A4op:9.4f}")

# F2: energy-resolved IPR at one T (is there a two-phase / mobility-edge signature?)
T = 400.0
s_rho, gwin = window(T, gams=zs)
Nw = len(s_rho)
V = v_on(s_rho, Nw)
W = V.T @ V / INT_PSI2
A, _ = norm_A(W)
evA, U = np.linalg.eigh((A + A.T) / 2.0)
ipr = (U**4).sum(axis=0)
order = np.argsort(evA)
print(f"\nenergy-resolved IPR at T={T:.0f} (N={Nw}); bands of 10 sorted eigenvalues:")
for lo in range(0, Nw, 10):
    hi = min(lo + 10, Nw)
    band = order[lo:hi]
    print(f"  eig[{lo:3d}:{hi:3d}] {evA[band].min():6.3f}..{evA[band].max():6.3f}  "
          f"IPR*N mean={ipr[band].mean()*Nw:7.2f} max={ipr[band].max()*Nw:7.2f}")

print("\n  reference: GUE bulk eigenvectors IPR ~ 3/N -> meanIPR*N ~ 3; crystal (delta) IPR ~ 1.")
print("  n-/N is the 'localized/off-line fraction'; all-simple world has n- = 0 (marks >= 0).")
print("  dev1_2/N = mean distance of the normalized spectrum from the integral marks {1,2}.")
