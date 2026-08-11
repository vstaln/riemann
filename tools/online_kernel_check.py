#!/usr/bin/env python3
"""
Q1 transfer analysis — kernel numerics for the Gram-stability refinement.

Checks the structural claims the transfer depends on:
  1. Closed form of K(x) = int_{-1/2}^{1/2} cos(sqrt(2) t) cos(2 pi x t) dt  vs mpmath quad.
  2. k(x) = K(x)/K(0): values, zeros on (0,4].
  3. Three-point stability: eps4 = min trPsi(G(u,v)) over u,v>0, u+v<=4, G the 3x3
     Gram matrix of atoms at ordinates with gaps u,v.  (claim: >= 221/1e6 -> 67.2519767%)
  4. Multiplicity-scaled blocks (Theorem A atoms, with multiplicity): infimum still
     attained at the all-simple configuration (so eps_A >= eps_D).
  5. Seven-point: sample 7-ordinate configs, min trPsi of 7x7 Gram (claim >= 19/5000).
  6. Orthogonality impossibility: min over domain of max off-diagonal |k|.
  7. Constant algebra: H0, 3-pt and 7-pt formulas, hypothetical transfers.

Run: proot-distro login ubuntu -- python3 /data/data/com.termux/files/home/riemann/tools/online_kernel_check.py
"""
import numpy as np
from mpmath import mp, mpf, sin, cos, sqrt, pi, cot, quad, polyroots
from scipy.optimize import brentq

mp.dps = 40

# ----------------------------------------------------------------------------
# 1. The kernel
# ----------------------------------------------------------------------------
SQ2 = np.sqrt(2.0)
A = SQ2 / 2.0          # sqrt(2)/2

def K_np(x):
    """K(x) = int_{-1/2}^{1/2} cos(sqrt2 t) cos(2 pi x t) dt (closed form)."""
    x = np.asarray(x, dtype=float)
    d1 = SQ2 + 2.0 * np.pi * x
    d2 = SQ2 - 2.0 * np.pi * x
    t1 = np.where(np.abs(d1) < 1e-9, 0.5, np.sin(A + np.pi * x) / d1)
    t2 = np.where(np.abs(d2) < 1e-9, 0.5, np.sin(A - np.pi * x) / d2)
    return t1 + t2

K0_np = float(K_np(0.0))

def k_np(x):
    return K_np(x) / K0_np

def K_mp(x):
    return sin(A + pi * x) / (SQ2 + 2 * pi * x) + sin(A - pi * x) / (SQ2 - 2 * pi * x)

K0_mp = K_mp(0)

def K_quad_mp(x):
    x = mpf(x)
    return quad(lambda t: cos(sqrt(2) * t) * cos(2 * pi * x * t), [-mpf('0.5'), mpf('0.5')])

print("=== 1. kernel K(x): closed form vs mpmath quad ===")
for x in [mpf(0), mpf('0.5'), mpf(1), mpf('1.5'), mpf(2), mpf(3), mpf(4)]:
    cf = K_mp(x)
    qd = K_quad_mp(x)
    print(f"  K({mp.nstr(x,2):>4s}) = {mp.nstr(cf, 18):>22s}   quad = {mp.nstr(qd, 18):>22s}   |diff| = {mp.nstr(abs(cf-qd), 3)}")
print(f"  K(0) = {mp.nstr(K_mp(0), 25)}   (1/K(0) = {mp.nstr(1/K_mp(0), 12)})")

# ----------------------------------------------------------------------------
# 2. k(x) values + zeros on (0,4]
# ----------------------------------------------------------------------------
print("\n=== 2. k(x) = K(x)/K(0): table and zeros on (0,4] ===")
for x in [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]:
    print(f"  k({x}) = {k_np(x):+.8f}")

xs = np.linspace(1e-6, 4.0, 40001)
ks = k_np(xs)
sign_changes = np.where(np.diff(np.sign(ks)) != 0)[0]
zeros = [brentq(lambda t: k_np(t), xs[sc], xs[sc + 1]) for sc in sign_changes]
print(f"  zeros of k on (0,4]: {[round(z, 6) for z in zeros]}")

# ----------------------------------------------------------------------------
# 3. three-point stability eps4
# ----------------------------------------------------------------------------
def psi_np(t):
    t = np.asarray(t, dtype=float)
    return np.where(t <= 2.0, (t - 1.0) ** 2, 2.0 * t - 3.0)

def trPsi3(u, v):
    """tr Psi(G) for the 3x3 Gram of atoms at gaps u, v (u+v = outer gap)."""
    kuv, ku, kv = k_np(u + v), k_np(u), k_np(v)
    G = np.array([[1.0, ku, kuv], [ku, 1.0, kv], [kuv, kv, 1.0]])
    return float(np.sum(psi_np(np.linalg.eigvalsh(G))))

print("\n=== 3. three-point stability: min trPsi over u,v>0, u+v<=4 ===")
N = 400
u = np.linspace(1e-5, 4.0, N)
v = np.linspace(1e-5, 4.0, N)
best = (1e30, None)
for ui in range(N):
    for vi in range(N):
        if u[ui] + v[vi] > 4.0 + 1e-9:
            continue
        val = trPsi3(u[ui], v[vi])
        if val < best[0]:
            best = (val, (u[ui], v[vi]))
eps4_grid, argmin = best
print(f"  grid min trPsi (N={N}): {eps4_grid:.12e}  at u={argmin[0]:.6f}, v={argmin[1]:.6f}, u+v={argmin[0]+argmin[1]:.6f}")
print(f"  claimed lower bound 221/1e6 = {221/1e6:.12e}")

# high-precision check near argmin using the cubic for a unit-diagonal 3x3:
#   char poly in t = 1-lam:  t^3 - S t + 2abc = 0,  S = a^2+b^2+c^2
def trPsi3_mp(u, v):
    kuv, ku, kv = K_mp(u + v) / K0_mp, K_mp(u) / K0_mp, K_mp(v) / K0_mp
    assert ku == ku and kv == kv and kuv == kuv
    S = ku * ku + kv * kv + kuv * kuv
    P = 2 * ku * kv * kuv
    roots = polyroots([-1, 0, S, -P])          # t^3 - S t + 2abc = 0  ->  -t^3 + S t - 2abc = 0
    lam = [1 - r for r in roots]
    return sum((t - 1) ** 2 if t <= 2 else 2 * t - 3 for t in lam)

print("  mpmath refinement around the grid argmin:")
ub, vb = argmin
best_mp, best_at = mpf(1e30), None
for du in [mpf('-2e-3'), mpf('-1e-3'), mpf(0), mpf('1e-3'), mpf('2e-3')]:
    for dv in [mpf('-2e-3'), mpf('-1e-3'), mpf(0), mpf('1e-3'), mpf('2e-3')]:
        uu, vv = mpf(ub) + du, mpf(vb) + dv
        if uu + vv > mpf(4):
            continue
        val = trPsi3_mp(uu, vv)
        if val < best_mp:
            best_mp, best_at = val, (uu, vv)
print(f"  mpmath min: {mp.nstr(best_mp, 18)}  at u={mp.nstr(best_at[0], 10)}, v={mp.nstr(best_at[1], 10)}, u+v={mp.nstr(best_at[0]+best_at[1], 10)}")

# ----------------------------------------------------------------------------
# 4. multiplicity-scaled blocks (Theorem A atoms)
# ----------------------------------------------------------------------------
def trPsi3_m(u, v, m):
    m = np.asarray(m, dtype=float)
    sq = np.sqrt(m)
    G = np.array([
        [m[0],       sq[0]*sq[1]*k_np(u),       sq[0]*sq[2]*k_np(u+v)],
        [sq[0]*sq[1]*k_np(u), m[1],             sq[1]*sq[2]*k_np(v)],
        [sq[0]*sq[2]*k_np(u+v), sq[1]*sq[2]*k_np(v), m[2]],
    ])
    return float(np.sum(psi_np(np.linalg.eigvalsh(G))))

print("\n=== 4. Theorem A atoms: multiplicity-scaled 3x3 blocks ===")
print(f"  at the all-simple argmin (u={argmin[0]:.4f}, v={argmin[1]:.4f}):")
for m in [(1,1,1), (2,1,1), (1,2,1), (1,1,2), (2,2,1), (1,2,2), (3,1,1), (1,3,1), (2,2,2), (4,4,4)]:
    print(f"    m={m}: trPsi = {trPsi3_m(argmin[0], argmin[1], m):.6e}")
# random sanity: trPsi(m-block) >= trPsi(all-simple) - tol
rng = np.random.default_rng(42)
viol = 0
for _ in range(4000):
    uu = rng.uniform(1e-3, 4.0); vv = rng.uniform(1e-3, 4.0)
    if uu + vv > 4.0:
        continue
    base = trPsi3(uu, vv)
    m = rng.integers(1, 5, size=3)
    if trPsi3_m(uu, vv, m) < base - 1e-9:
        viol += 1
print(f"  random check: {4000} samples, violations (trPsi_m < trPsi_allsimple - 1e-9): {viol}")

# ----------------------------------------------------------------------------
# 5. seven-point: random 7-ordinate configs
# ----------------------------------------------------------------------------
def trPsi7(gaps):
    """gaps: 6 consecutive positive gaps. Gram of 7 atoms, ordinates cumulative."""
    ords = np.concatenate([[0.0], np.cumsum(gaps)])
    G = np.empty((7, 7))
    for i in range(7):
        for j in range(7):
            G[i, j] = k_np(abs(ords[i] - ords[j]))
    return float(np.sum(psi_np(np.linalg.eigvalsh(G))))

print("\n=== 5. seven-point: sampled configs (6 gaps, every consecutive triple sum <= 4) ===")
rng = np.random.default_rng(7)
vals = []
while len(vals) < 30000:
    g = rng.uniform(0.02, 4.0, size=6)
    t = g[:-2] + g[1:-1] + g[2:]
    if (t <= 4.0).all():
        vals.append(trPsi7(g))
vals = np.array(vals)
print(f"  samples: {len(vals)}, min trPsi = {vals.min():.6e}, median = {np.median(vals):.6e}")
print(f"  claimed 7-point bound 19/5000 = {19/5000:.6e}")

# directed: seeded local minimization from zero-pattern starts (scipy Nelder-Mead)
from scipy.optimize import minimize
import itertools
z = [1.057278, 2.030068, 3.020243]
starts = []
for pat in itertools.product(z, repeat=2):
    g = np.array([pat[0], pat[1], 0.5, 0.5, 0.5, 0.5])
    starts.append(g)
    g = np.array([0.5, 0.5, pat[0], pat[1], 0.5, 0.5])
    starts.append(g)
best_dir = 1e30
for g0 in starts:
    if (g0[:-2] + g0[1:-1] + g0[2:] > 4.0).any():
        continue
    res = minimize(trPsi7, g0, method='Nelder-Mead', options={'maxiter': 3000, 'xatol': 1e-6, 'fatol': 1e-9})
    if res.fun < best_dir:
        best_dir = res.fun
print(f"  directed Nelder-Mead from zero-pattern starts: min trPsi = {best_dir:.6e}")

# ----------------------------------------------------------------------------
# 6. orthogonality impossibility
# ----------------------------------------------------------------------------
print("\n=== 6. atom orthogonality is impossible in the window ===")
worst = (1e30, None)
for ui in range(N):
    for vi in range(N):
        if u[ui] + v[vi] > 4.0 + 1e-9:
            continue
        moff = max(abs(k_np(u[ui])), abs(k_np(v[vi])), abs(k_np(u[ui] + v[vi])))
        if moff < worst[0]:
            worst = (moff, (u[ui], v[vi]))
print(f"  min over domain of max(|k(u)|,|k(v)|,|k(u+v)|) = {worst[0]:.6e} at u={worst[1][0]:.4f}, v={worst[1][1]:.4f}")

# ----------------------------------------------------------------------------
# 7. constant algebra
# ----------------------------------------------------------------------------
print("\n=== 7. constant algebra ===")
H0 = mpf(3) / 2 - (1 / sqrt(2)) * cot(1 / sqrt(2))
print(f"  H0 = 3/2 - (1/sqrt2) cot(1/sqrt2) = {mp.nstr(H0, 30)}")
print(f"  published:                           0.67250070367941164573")

eps3 = mpf(221) / mpf(10 ** 6)
c3 = (H0 - eps3 / 4) / (1 - eps3 / 2)
print(f"  3-pt: (H0 - eps/4)/(1 - eps/2), eps=221/1e6  -> {mp.nstr(c3, 20)}   (published 0.672519767...)")

c7 = (mpf(1345000) * H0 - 2680) / mpf(1340003)
print(f"  7-pt: (1345000*H0 - 2680)/1340003          -> {mp.nstr(c7, 20)}   (published 0.673008527927...)")

# linear response coefficient from the 3-pt formula: d c / d eps at eps=0
resp = H0 / 2 - mpf(1) / 4
print(f"  linear response dc/deps ~ H0/2 - 1/4 = {mp.nstr(resp, 10)}")

print("\n  HYPOTHETICAL transfers (same linear response; chain algebra NOT verified):")
for name, base in [("Theorem A (on-line, 2/3)", mpf(2) / 3), ("Theorem C (distinct, 5/6)", mpf(5) / 6)]:
    c3t = base + resp * eps3
    c7t = base + resp * mpf(19) / mpf(5000)
    print(f"    {name}: 3-pt shift -> {mp.nstr(c3t, 15)}   (delta +{mp.nstr(c3t - base, 6)})")
    print(f"    {name}: 7-pt shift -> {mp.nstr(c7t, 15)}   (delta +{mp.nstr(c7t - base, 6)})")

print("\nDONE.")
