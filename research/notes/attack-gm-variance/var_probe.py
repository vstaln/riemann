#!/usr/bin/env python
"""Windowed zero-counting variance on real zeta zeros (10k zeros).

Deliverable for B10 (GM-variance flank): empirically estimate
    V(U) = Var_t[ N(t+U) - N(t) ]   (raw) and the mean-subtracted (S-fluctuation) version
for windows U at height ~T, and compare with
  - GUE number variance (1/pi^2)(log(2*pi*n) + 1 + gamma), n = U*rho (mean count in spacings)
  - the trivial / in-band-only expectation
and test the two candidate dictionaries:
  (A) B10's: alpha = U/T            -> beyond-1 = long windows U > T
  (B) corrected: probe window in form-factor space has width ~ 2*pi/(U*log T)
      -> alpha ~ 1/n, beyond-1 (alpha > 1) <-> U < 1/rho (windows shorter than ~1 spacing)

Data: tools/data/zeros_computed_10000.txt  (index gamma, 10000 zeros, gamma up to ~9879)
"""
import numpy as np
from math import log, pi
euler_gamma = 0.5772156649015329

# ---------- load zeros ----------
path = "/home/vstaln/riemann/tools/data/zeros_computed_10000.txt"
g = np.loadtxt(path, usecols=1)          # imaginary parts, ascending
N = len(g)
print(f"loaded {N} zeros, gamma_1={g[0]:.3f}, gamma_N={g[-1]:.3f}")

# ---------- window-range bookkeeping ----------
# slide t in [T0, T1_max]; keep windows fully inside [T0, T1] with all zeros of (t,t+U] present
T0 = 2000.0
T1 = g[-1] - 40.0                        # top margin so windows near the end are unaffected
def count_in(t_arr, U):
    """N(t+U) - N(t) for array of starts t_arr (zeros below t or beyond t+U excluded)."""
    lo = np.searchsorted(g, t_arr, side='right')
    hi = np.searchsorted(g, t_arr + U, side='left')
    return (hi - lo).astype(float)

def local_mean(t_arr, U):
    """(U/2pi) log(t/2pi): expected count from Riemann-von Mangoldt (local density)."""
    return (U / (2*pi)) * np.log(t_arr / (2*pi))

M = 4000                                   # number of sliding window starts
t = np.linspace(T0, T1, M)

# average local density over the window range
rho = np.mean(np.log(t / (2*pi)) / (2*pi))
T_ref = np.exp(np.mean(np.log(t)))         # geometric-mean height of the window range
print(f"window starts t in [{T0:.0f},{T1:.0f}], mean local density rho = {rho:.4f}, "
      f"T_ref = {T_ref:.0f}, log(T_ref/2pi) = {log(T_ref/(2*pi)):.3f}")

# ---------- variance curves ----------
U_grid = np.geomspace(0.15, 300.0, 45)
rows = []
for U in U_grid:
    c = count_in(t, U)
    m = local_mean(t, U)
    V_raw = c.var()                                  # variance of the raw count over t
    V_fluct = ((c - m) ** 2).mean()                  # mean-square deviation from local mean (S-fluctuation)
    rows.append((U, V_raw, V_fluct))

rows = np.array(rows)
U_arr, V_raw, V_fluct = rows[:, 0], rows[:, 1], rows[:, 2]

# GUE number variance prediction with n = U*rho
def gue(n):
    return (1/pi**2) * (log(max(n, 1e-6) * 2*pi) + 1 + euler_gamma)

# ---------- dictionary analysis ----------
# corrected: probe weight in form-factor space is sinc^2(pi * alpha * U*log(T)/2pi),
#            i.e. width D = U*log(T_ref)/2pi in spacings, alpha-scale ~ 1/D
logT = log(T_ref / (2*pi))
D = U_arr * logT / (2*pi)
# beyond-1 weight fraction: 1 - [ (2/pi) * int_0^{pi*D} sinc^2(u) du ]  (weight at |alpha|>1)
from scipy.integrate import quad          # scipy available? fall back below if not
def beyond1_frac(Dv):
    if Dv <= 0:
        return 1.0
    I = quad(lambda u: (np.sinc(u/pi))**2, 0.0, pi*Dv, limit=200)[0]
    return 1.0 - (2.0/pi) * I
bf = np.array([beyond1_frac(d) for d in D])

print("\n=== variance curve (window U in gamma-units) ===")
print(f"{'U':>8} {'n=U*rho':>8} {'V_raw':>10} {'V_fluct':>10} {'GUE':>10} "
      f"{'Vf/GUE':>7} {'alpha~1/n':>8} {'beyond1 wgt':>10}")
for i in range(len(U_arr)):
    U, Vr, Vf = U_arr[i], V_raw[i], V_fluct[i]
    n = U * rho
    if U < 1.2 or abs(np.log2(U) - round(np.log2(U))) < 1e-6 or U in (U_arr[i] for i in range(len(U_arr))):
        pass
    print(f"{U:8.3f} {n:8.3f} {Vr:10.4f} {Vf:10.4f} {gue(n):10.4f} {Vf/gue(n):7.3f} {1/max(n,1e-6):8.3f} {bf[i]:10.3f}")

# ---------- dictionary test at the five alpha values from the brief ----------
print("\n=== windows U for alpha in {0.5, 0.9, 1.1, 1.5, 2.0} ===")
print("(A) B10 dictionary alpha = U/T  ->  U = alpha*T_ref   (beyond-1 = LONG windows)")
print("(B) corrected alpha ~ 1/(U*rho) ->  U = 1/(alpha*rho) (beyond-1 = SHORT windows)")
print(f"{'alpha':>6} | {'U_A':>9} {'Vf_A':>9} {'n_A':>7} | {'U_B':>9} {'Vf_B':>9} {'n_B':>7} {'GUE_B':>9} |")
for alpha in [0.5, 0.9, 1.1, 1.5, 2.0]:
    UA = alpha * T_ref
    UB = 1.0 / (alpha * rho)
    VfA = np.interp(np.log(UA), np.log(U_arr), np.log(V_fluct)); VfA = np.exp(VfA)
    VfB = np.interp(np.log(UB), np.log(U_arr), np.log(V_fluct)); VfB = np.exp(VfB)
    nA, nB = UA*rho, UB*rho
    print(f"{alpha:6.2f} | {UA:9.1f} {VfA:9.4f} {nA:7.1f} | {UB:9.3f} {VfB:9.4f} {nB:7.3f} {gue(nB):9.4f} |")

# ---------- exact values at corrected windows + GUE table ----------
print("\n=== exact V at corrected windows (linear interpolation of log V) ===")
print(f"{'alpha':>6} {'U':>8} {'V_fluct':>10} {'GUE':>10} {'Vf/GUE':>8} {'beyond1wgt':>10}")
for alpha in [0.5, 0.9, 1.1, 1.5, 2.0]:
    UB = 1.0/(alpha*rho)
    VfB = np.exp(np.interp(np.log(UB), np.log(U_arr), np.log(V_fluct)))
    nB = UB*rho
    print(f"{alpha:6.2f} {UB:8.3f} {VfB:10.4f} {gue(nB):10.4f} {VfB/gue(nB):8.3f} {beyond1_frac(UB*logT/(2*pi)):10.3f}")

# ---------- Poisson / independent-zero prediction for comparison ----------
print("\nPoisson (independent zeros) prediction V ~ n = U*rho at the corrected windows:")
for alpha in [0.5, 0.9, 1.1, 1.5, 2.0]:
    UB = 1.0/(alpha*rho)
    print(f"  alpha={alpha}: U={UB:.3f}, Poisson V={UB*rho:.3f}")

# ---------- where does the curve cross the alpha=1 boundary? ----------
U_star = 1.0/rho
print(f"\nalpha=1 boundary (corrected): U* = 1/rho = {U_star:.3f}  (n=1 spacing); "
      f"V_fluct(U*) = {np.exp(np.interp(np.log(U_star), np.log(U_arr), np.log(V_fluct))):.3f}, "
      f"GUE(1) = {gue(1.0):.3f}")
