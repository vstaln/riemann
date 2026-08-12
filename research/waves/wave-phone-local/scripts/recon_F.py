#!/usr/bin/env python3
# RECONNAISSANCE: pin down the exact 6-gap functional F for the record claim.
# From the paper:
#   window v(s) = cos(alpha s) on [-1/2,1/2]
#   kernel k(x) = K(x)/K(0), K(x) = int_{-1/2}^{1/2} v(t) v(x+t) dt
#     closed form: K(x) = sin((2pi x - a)/2)/(2pi x - a) + sin((2pi x + a)/2)/(2pi x + a)
#   local functional over 6 gaps g_1..g_6 (7 atoms at x_0=0, x_j = sum_{l<=j} g_l):
#     M_ij = k(x_j - x_i)   (7x7 PSD Gram, unit diagonal)
#     D = tr Psi(M) = sum_i Psi(lambda_i),  Psi(t) = (t-1)^2 on [0,2], 2t-3 beyond
#   Candidates (pressure p per gap, 6 gaps):
#     A: F = D + 6p            (per 7-block, like ainta's per-block floor)
#     B: F = D/7 + 6p/7        (per atom)
#   Calibration: ainta 7-point floor eps7 = 19/5000 = 0.0038 (alpha = sqrt2, p = 0)
import numpy as np

ALPHA_SQRT2 = np.sqrt(2.0)
ALPHA_149 = 1.49
P_1320 = 1.0/1320.0

def K(alpha, x):
    # K(x) = int_{-1/2}^{1/2} cos(a t) cos(2 pi x t) dt
    x = np.asarray(x, dtype=float)
    t1 = 2*np.pi*x - alpha
    t2 = 2*np.pi*x + alpha
    out = np.zeros_like(x)
    # handle removable singularities via sinc
    mask1 = np.abs(t1) > 1e-12
    mask2 = np.abs(t2) > 1e-12
    out[mask1] += np.sin(t1[mask1]/2)/t1[mask1]
    out[mask2] += np.sin(t2[mask2]/2)/t2[mask2]
    out[~mask1] += 0.5
    out[~mask2] += 0.5
    return out

def kfun(alpha, x):
    return K(alpha, x)/K(alpha, 0.0)

def gram7(g, alpha):
    # g: array of 6 gaps; positions x_0..x_6
    x = np.concatenate([[0.0], np.cumsum(g)])
    M = np.zeros((7,7))
    for i in range(7):
        for j in range(7):
            M[i,j] = kfun(alpha, x[j]-x[i])
    return M

def psi(t):
    t = np.asarray(t, dtype=float)
    return np.where(t <= 2.0, (t-1.0)**2, 2.0*t-3.0)

def D_of(g, alpha):
    M = gram7(g, alpha)
    w = np.linalg.eigvalsh(M)
    return np.sum(psi(w))

def F_A(g, alpha, p):
    return D_of(g, alpha) + 6*p

def F_B(g, alpha, p):
    return (D_of(g, alpha) + 6*p)/7.0

# ---- calibration: alpha = sqrt2, p = 0 ----
print("=== CALIBRATION alpha=sqrt2, p=0 (ainta 7-point eps7 = 19/5000 = 0.0038) ===")
# kernel sample
for xx in [0.0, 0.5, 1.0, 1.5, 2.0, 3.0]:
    print(f"  k({xx}) = {kfun(ALPHA_SQRT2, xx):+.6f}")
# coarse grid over gaps
best = 1e9; bestg = None
for i in range(8):
    g = np.array([0.5*i]*6)
    d = D_of(g, ALPHA_SQRT2)
    if d < best:
        best = d; bestg = g.copy()
print(f"  coarse min D (uniform gaps) = {best:.6f} at g={bestg[0]}")
# random / local search: random restarts + coordinate descent
rng = np.random.default_rng(42)
def descent(g0, alpha):
    g = g0.copy()
    step = 0.2
    for _ in range(2000):
        improved = False
        for coord in range(6):
            for sgn in [-1.0, 1.0]:
                gt = g.copy(); gt[coord] = max(0.0, gt[coord]+sgn*step)
                if D_of(gt, alpha) < D_of(g, alpha):
                    g = gt; improved = True
        if not improved:
            step /= 2
            if step < 1e-5: break
    return g, D_of(g, alpha)
gmin = None; dmin = 1e9
for trial in range(40):
    g0 = rng.uniform(0.0, 3.5, 6)
    g, d = descent(g0, ALPHA_SQRT2)
    if d < dmin: dmin = d; gmin = g
print(f"  local-search min D = {dmin:.8f} at gaps {np.round(gmin,3)}")
print(f"  -> per-atom floor D/7 = {dmin/7:.8f} (ainta per-atom 5.43e-4 = 0.000543)")
print(f"  -> D+6p with p=0      = {dmin:.8f} (ainta per-block 19/5000 = 0.0038)")
