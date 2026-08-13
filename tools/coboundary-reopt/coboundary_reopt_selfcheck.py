"""Cheap self-checks for the coboundary-reopt note.

1. Verify the huge-gap asymptotic slope formula numerically:
   F_B(g;l,c) ~ kappa_i * g_i + O(1) as g_i -> oo, kappa_i = P0 + l_{i-1} - l_i.
2. Record tawan's family floor vs the corrected-LP value v* on the SAME
   constraint family (crystals + intermediate + finite huge-gap cutoffs).
3. Show the prior LP's kappa_1 < 0 (its certification failure root cause).
"""
import numpy as np

SQRT2 = np.sqrt(2.0)

def k_alpha(x, alpha):
    x = np.asarray(x, float); a = alpha / 2.0
    z1 = np.pi * x - a; z2 = np.pi * x + a
    return 0.5 * (np.sinc(z1 / np.pi) + np.sinc(z2 / np.pi)) / np.sinc(a / np.pi)

def w_alpha(x, alpha):
    return k_alpha(x, alpha) ** 2

P0 = 1.0 / 1920.0
Q0 = 1.0 / 3.0

def pair_coeffs():
    return {(i, j): 2.0 / (7 - (j - i)) for i in range(7) for j in range(i + 1, 7)}

def F0(g, alpha):
    g = np.asarray(g, float)
    y = np.concatenate([[0.0], np.cumsum(g)])
    total = P0 * np.sum(g) + Q0 * np.sum(w_alpha(g, alpha))
    for (i, j), a in pair_coeffs().items():
        total += a * w_alpha(y[j] - y[i], alpha)
    return total

def lin_coeffs(g, alpha):
    g = np.asarray(g, float)
    g0 = np.concatenate([[0.0], g, [0.0]])
    return (np.asarray(g0[1:] - g0[:-1], float)[1:6],
            np.asarray(w_alpha(g0[1:], alpha) - w_alpha(g0[:-1], alpha), float)[1:6])

def F_B(g, alpha, l, c):
    L, C = lin_coeffs(g, alpha)
    return F0(g, alpha) + np.dot(L, l) + np.dot(C, c)

def kappa_of(l):
    l0 = np.concatenate([[0.0], l, [0.0]])
    return P0 + (l0[:-1] - l0[1:])

l_tawan = np.array([54, -123, 0, 123, -54]) / 1_920_000
c_tawan = np.array([5971, 5971, 0, -5971, -5971]) / 300_000
alpha = 1.49

# --- 1. asymptotic slope check: kappa_i vs finite-difference of F_B ---
print("== huge-gap slope check (alpha=1.49) ==")
kap = kappa_of(l_tawan)
for i in range(6):
    H = 60.0
    g = np.array([1.05, 1.98, 1.05, 1.98, 1.05, 1.98]); g[i] = H
    fb = F_B(g, alpha, l_tawan, c_tawan)
    slope_num = fb / H  # approx kappa_i when F0 linear part dominates
    print(f"  i={i+1}: kappa={kap[i]:.6f}  F_B(H=60)/60={slope_num:.6f}")

# --- 2. tawan vs corrected-LP on same family (light re-solve) ---
from scipy.optimize import linprog
def base_family(n2=14, n3=4, nint=300):
    cfgs = []
    for a in np.linspace(0.8, 1.6, n2):
        for b in np.linspace(1.4, 2.6, n2):
            cfgs.append(np.array([a, b, a, b, a, b]))
    for a in np.linspace(0.85, 1.55, n3):
        for b in np.linspace(1.4, 2.5, n3):
            for cc in np.linspace(0.85, 1.55, n3):
                cfgs.append(np.array([a, b, cc, a, b, cc]))
    rng = np.random.default_rng(12345)
    for _ in range(nint):
        cfgs.append(rng.uniform(0.5, 3.0, 6))
    base = np.array([1.05, 1.98, 1.05, 1.98, 1.05, 1.98])
    for pos in range(6):
        for H in [8.0, 14.0, 21.0]:
            g = base.copy(); g[pos] = H
            cfgs.append(g)
    return cfgs

cfgs = base_family()
print(f"\n== family floor comparison, |K|={len(cfgs)} ==")
fl_t = min(F_B(g, alpha, l_tawan, c_tawan) for g in cfgs)
A, b = [], []
for g in cfgs:
    L, C = lin_coeffs(g, alpha)
    A.append(np.concatenate([-L, -C, [1.0]]))
    b.append(F0(g, alpha))
for i in range(1, 7):
    row = np.zeros(11)
    if i >= 2: row[i - 2] = -1.0
    if i <= 5: row[i - 1] = +1.0
    A.append(row); b.append(P0)
res = linprog(c=[0]*10+[-1.0], A_ub=np.array(A), b_ub=np.array(b),
              bounds=[(-0.0012,0.0012)]*5 + [(-0.06,0.06)]*5 + [(None,None)],
              method='highs')
print(f"  LP status={res.status} v*={res.x[10]:.6f}")
print(f"  tawan floor on same family = {fl_t:.6f}")
print(f"  => LP v* ({res.x[10]:.6f}) vs tawan floor ({fl_t:.6f}): "
      f"LP {'BEATS' if res.x[10] > fl_t else 'LOSES TO'} tawan on |K|")

# --- 3. prior LP's negative kappa ---
l_prior = np.array([0.0005208, 0.0006792, 0.0012, -0.001042, -0.0005208])
kap_prior = kappa_of(l_prior)
print(f"\n== prior LP kappa ==")
print(f"  prior LP kappa = {np.round(kap_prior, 6)}")
print(f"  min prior kappa = {kap_prior.min():.6f} (<0 => F_B -> -oo as that gap -> oo)")
print(f"  tawan min kappa = {kap.min():.6f} (>0)")
