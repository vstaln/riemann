#!/usr/bin/env python3
"""Certificate-parameter optimization sweep for the simple-zeros-on-line bound.

Reconstructs the three external formula families from their exact repo
constants and sweeps the parameter space to find the maximum certified /
conjectured bound.

Families (all reproduce the repos' headline numbers exactly):

  F1 (ainta 3-point):  bound = (H0 - eps/4)/(1 - eps/2),  certified eps=221/1e6.
  F2 (ainta 7-point):  bound = (1345000*H0 - 2680)/1340003, certified eps=19/5000.
  F3 (trmdy):          bound = (m*H - eta*Bp*(m-1))/(m - R), H=672457/1e6,
                       eps=1/200, p=1/2300, q=6, Bp=q*p, A=eps*(m-q),
                       R = h(A) = 2*sqrt(A)-1 (A>=1) [else A], eta = R/A.
  F4 (tawanerguo):     H_alpha = 2 - 1/c(alpha) with cosine window v=cos(alpha s),
                       local F_B >= 577/1e5 (certified m=183, alpha=1.47),
                       A = local*(m-6), B = Phi_m(A), tax = pressure, m=183:
                       bound = (H_alpha - tax)/(1 - B/m).

Master algebra used for the *joint* sweep (all variants of the same chain):
  per-window inequality  F(g) = p*sum g_i + sum_{i<j} a_ij w(y_j-y_i) >= eps
  summed over m-q windows:  E_B + p*(sum of gap charges)*span >= eps*(m-q)
  A := eps*(m-q);  profile tr Psi(G) >= h(E), chord h(E) >= (h(A)/A) E;
  eta := h(A)/A;  block Gram Psi >= eta*(A - p*span_charge);
  averaging over m offsets (interior gap charged <= m-1 times, span total N):
  Delta(M) >= (R/m) S - eta*p*(m-1) N/m;
  S/N >= (m*H - eta*p*(m-1)) / (m - R).

The honest distinctions:
  * "certified"  = every ingredient is proven: eps from a verified interval
    certificate (ainta 19/5000, trmdy 1/200, tawanerguo 577/1e5), H from a
    verified window enclosure, and the algebraic chain exact.
  * "conjectured"= parameters where some ingredient is NOT proven at that
    point (unverified eps, unverified H, or an extrapolated A), listed with
    the specific missing proof.
"""

from __future__ import annotations

import itertools
import math

import mpmath as mp

mp.mp.dps = 80

# --------------------------------------------------------------------------
# Kernel / window helpers (mpmath, closed forms verified vs quadrature)
# --------------------------------------------------------------------------

def sinc(z):
    if z == 0:
        return mp.mpf(1)
    return mp.sin(z) / z


def window_functional_cos(alpha):
    """c1, H for v(s) = cos(alpha s) on [-1/2,1/2]."""
    a = mp.mpf(alpha)
    i0 = 2 * mp.sin(a / 2) / a
    i2 = mp.mpf(1) / 2 + mp.sin(a) / (2 * a)
    const = mp.sin(a / 2) / a + 2 * mp.cos(a / 2) / (a * a)
    jv = -2 * i2 / (a * a) + const * i0
    c = i0 * i0 / (i2 + jv)
    return c, 2 - 1 / c


def h_profile(E):
    """Sharp profile h(E) = E (E<=1), 2*sqrt(E)-1 (E>=1)."""
    E = mp.mpf(E)
    return E if E <= 1 else 2 * mp.sqrt(E) - 1


def phi_m(A, m):
    """tawanerguo trace-energy envelope Phi_m(A)."""
    A = mp.mpf(A)
    m = mp.mpf(m)
    if A <= m / (m - 1):
        return A
    return 2 * mp.sqrt((m - 1) * A / m) - 1 + A / m


def block_bound_master(H, eps, p, m, q, cap, chord="h"):
    """Master chain: bound = (m*H - eta*Bp*(m-1))/(m - R).

    cap: the block-Gram-to-energy cap: 'h' (2sqrt(E)-1, trmdy), or
         'phi' (Phi_m, tawanerguo).  A = eps*(m-q), Bp = q*p.
    """
    H = mp.mpf(H)
    eps = mp.mpf(eps)
    p = mp.mpf(p)
    m = mp.mpf(m)
    q = mp.mpf(q)
    A = eps * (m - q)
    if cap == "h":
        R = h_profile(A)
    else:
        R = phi_m(A, m)
    eta = R / A
    Bp = q * p
    return (m * H - eta * Bp * (m - 1)) / (m - R)


# --------------------------------------------------------------------------
# Family reproductions
# --------------------------------------------------------------------------

H0 = mp.mpf(3) / 2 - (1 / mp.sqrt(2)) / mp.tan(1 / mp.sqrt(2))
print("H0 (Anthropic MT) =", mp.nstr(H0, 30))

# F1: ainta 3-point
eps3 = mp.mpf(221) / 10**6
b3 = (H0 - eps3 / 4) / (1 - eps3 / 2)
print("F1 ainta 3pt      =", mp.nstr(b3, 30))

# F2: ainta 7-point
b7 = (mp.mpf(1_345_000) * H0 - 2680) / mp.mpf(1_340_003)
print("F2 ainta 7pt      =", mp.nstr(b7, 30))

# F3: trmdy
H_tr = mp.mpf(672_457) / 10**6
b_tr = block_bound_master(H_tr, mp.mpf(1) / 200, mp.mpf(1) / 2300, 257, 6, "h")
print("F3 trmdy          =", mp.nstr(b_tr, 30))

# F4: tawanerguo
alpha_tw = mp.mpf(147) / 100
_, H_tw = window_functional_cos(alpha_tw)
local_tw = mp.mpf(577) / 100_000
m_tw = 183
tax_tw = mp.mpf(59) / 19_520
A_tw = local_tw * (m_tw - 6)
B_tw = phi_m(A_tw, m_tw)
b_tw = (H_tw - tax_tw) / (1 - B_tw / m_tw)
print("F4 tawanerguo     =", mp.nstr(b_tw, 30))
print("  H_window        =", mp.nstr(H_tw, 30))
print("  B               =", mp.nstr(B_tw, 30))

# Master-chain reproduction of the tawanerguo number (should match b_tw).
# The tawanerguo form is (H - tax)/(1 - B/m); the master chain with a
# block-energy interpretation:  eps*(m-q) = A,  Bp*(m-1)/m = tax  =>
# p = tax*m/(q*(m-1)), eps = A/(m-q).
p_tw_equiv = tax_tw * m_tw / (6 * (m_tw - 1))
eps_tw_equiv = A_tw / (m_tw - 6)
b_tw_check = block_bound_master(H_tw, eps_tw_equiv, p_tw_equiv, m_tw, 6, "phi")
print("F4 via master     =", mp.nstr(b_tw_check, 30), " (should match)")

print()

# --------------------------------------------------------------------------
# SWEEP 1: ainta 3-point / 7-point as a function of eps
# --------------------------------------------------------------------------

def f1(eps):
    eps = mp.mpf(eps)
    return (H0 - eps / 4) / (1 - eps / 2)


def f2(eps7):
    """7-point formula re-expressed with eps7 = 19/5000 and m = 269."""
    eps7 = mp.mpf(eps7)
    m7 = 269
    A = eps7 * (m7 - 6)
    # R = h(A) = min(1, 2sqrt(A)-1); A < 1 for eps7 <= 19/5000.
    R = h_profile(A)
    p7 = mp.mpf(1) / 3000
    q7 = 6
    eta = R / A
    return (m7 * H0 - eta * (q7 * p7) * (m7 - 1)) / (m7 - R)


# What eps is needed to reach 0.6818?
target = mp.mpf("0.68183123059534187426")
print("--- Sweep 1: eps required for bound = 0.68183123 ---")
for name, fn in (("3pt", f1), ("7pt", f2)):
    # binary search on eps in (0, 0.5)
    lo, hi = mp.mpf("1e-9"), mp.mpf("0.5")
    for _ in range(200):
        mid = (lo + hi) / 2
        if fn(mid) < target:
            lo = mid
        else:
            hi = mid
    print(f"  {name}: eps needed = {mp.nstr(hi, 25)}")
    # best certified eps
    print(f"    certified eps (ainta 221/1e6, 19/5000) -> bound {mp.nstr(fn(mp.mpf(221)/10**6), 20)} / {mp.nstr(fn(mp.mpf(19)/5000), 20)}")

print()

# --------------------------------------------------------------------------
# SWEEP 2: tawanerguo formula over (m, pressure, A) with certified pieces
# --------------------------------------------------------------------------

print("--- Sweep 2: tawanerguo (H_1.47 fixed, block m, local eps, tax) ---")

# (a) vary m, keep certified local=577/1e5 and the block-energy A = local*(m-6).
# The tax: in the repo, pressure total = (m-6)/320, averaged tax = (m-6)/(320 m)...
# Actually repo tax = 59/19520 = ?  Let's check: (m-6)/(320*m) at m=183:
# 177/(320*183) = 177/58560 = 0.00302254... but repo tax = 59/19520 = 0.00302254...
# 59/19520 = 0.0030225409836...  and 177/58560 = 0.0030225409836... yes equal!
# (they simplify 177/58560 = 59/19520).  So tax(m) = (m-6)/(320*m).
def tax_m(m):
    return mp.mpf(m - 6) / (320 * m)


results = []
for m in [64, 96, 128, 160, 183, 200, 256, 320, 384, 512, 640, 768, 896, 1024]:
    A = local_tw * (m - 6)
    B = phi_m(A, m)
    tax = tax_m(m)
    b = (H_tw - tax) / (1 - B / m)
    results.append((m, A, B, tax, b))
print(f"{'m':>5} {'A':>10} {'B':>12} {'tax':>12} {'bound':>18}")
for m, A, B, tax, b in results:
    print(f"{m:>5} {mp.nstr(A, 8):>10} {mp.nstr(B, 10):>12} {mp.nstr(tax, 12):>12} {mp.nstr(b, 18):>18}")
best_m = max(results, key=lambda r: r[4])
print("best m (certified local, certified H):", best_m[0], mp.nstr(best_m[4], 30))

print()

# (b) Vary the certified local constant eps_cert (what if a larger 7-point
# floor were proven?) -- extrapolation, labeled CONJECTURED.  For each eps
# the A changes and B=Phi_m(A) must be recomputed; tax fixed at certified m=183.
print("--- Sweep 2b: local floor eps at m=183, tax 59/19520 (CONJECTURED beyond 577/1e5) ---")
for eps_local in [mp.mpf(577) / 10**5, mp.mpf(6) / 10**3, mp.mpf(8) / 10**3,
                  mp.mpf(1) / 10**2, mp.mpf(15) / 10**3, mp.mpf(2) / 10**2,
                  mp.mpf(3) / 10**2, mp.mpf(5) / 10**2]:
    A = eps_local * (m_tw - 6)
    B = phi_m(A, m_tw)
    tax = tax_m(m_tw)
    b = (H_tw - tax) / (1 - B / m_tw)
    print(f"  eps={mp.nstr(eps_local, 8):>8}  A={mp.nstr(A, 8):>8}  B={mp.nstr(B, 10):>10}  bound={mp.nstr(b, 25)}")

print()

# (c) The limit as m -> inf with eps fixed (tax -> 1/320, B/m -> 0):
print("--- Sweep 2c: m -> inf limit (tax -> 1/320, B/m -> 0) ---")
lim = (H_tw - mp.mpf(1) / 320) / 1
print("  limit bound =", mp.nstr(lim, 30))

print()

# --------------------------------------------------------------------------
# SWEEP 3: joint optimization over the whole master chain
# --------------------------------------------------------------------------

print("--- Sweep 3: master chain over (H, eps, p, m, q, cap) ---")

# What combinations are consistent with the certified pieces?
# Certified anchors:
#   (a) H0 window, ainta 7pt:  eps=19/5000, p=1/3000, m=269, q=6, cap=h
#   (b) trmdy window:          eps=1/200, p=1/2300, m=257, q=6, cap=h
#   (c) tawanerguo:            eps_local=577/1e5 (per-7-window), tax 59/19520,
#                              m=183, cap=phi
# The master chain form used by (a),(b) has p as the one-gap pressure and
# eps the per-window floor; (c) uses the block-energy form directly.

def sweep3_table():
    rows = []
    # trmdy-style: fixed certified eps/p, vary m
    for m in [64, 96, 128, 160, 192, 224, 257, 288, 320, 384, 448, 512, 640, 768, 1024]:
        rows.append(("trmdy m", m, block_bound_master(H_tr, mp.mpf(1)/200, mp.mpf(1)/2300, m, 6, "h")))
    # ainta-style: fixed certified eps/p, vary m
    for m in [64, 96, 128, 160, 192, 224, 269, 320, 384, 448, 512]:
        rows.append(("ainta7 m", m, block_bound_master(H0, mp.mpf(19)/5000, mp.mpf(1)/3000, m, 6, "h")))
    # phi-cap version of tawanerguo with its certified local: vary m
    for m in [64, 96, 128, 160, 183, 224, 256, 320, 384, 448, 512]:
        A = local_tw * (m - 6)
        tax = tax_m(m)
        B = phi_m(A, m)
        rows.append(("tawan phi m", m, (H_tw - tax) / (1 - B / m)))
    return rows

rows = sweep3_table()
best = max(rows, key=lambda r: r[2])
print(f"{'label':>12} {'m':>5} {'bound':>20}")
for label, m, b in rows:
    print(f"{label:>12} {m:>5} {mp.nstr(b, 20):>20}")
print("best (certified ingredients):", best[0], best[1], mp.nstr(best[2], 30))

print()

# --------------------------------------------------------------------------
# The asymptotic / conjectured frontier: what is the max of the chain?
# --------------------------------------------------------------------------

print("--- Frontier analysis ---")

# For the trmdy chain with certified eps, p: as m -> inf, A = eps(m-q) -> inf,
# R = 2sqrt(A)-1 ~ 2 sqrt(eps m), eta ~ 2/sqrt(eps m) -> 0, so
# bound -> (m H - eta Bp (m-1))/(m - R) ~ H - eta Bp -> H.  The m->inf limit
# is just H (pressure vanishes).  Check numerically:
for m in [10**3, 10**4, 10**5]:
    b = block_bound_master(H_tr, mp.mpf(1)/200, mp.mpf(1)/2300, m, 6, "h")
    print(f"  trmdy m=10^{int(math.log10(m))}: bound = {mp.nstr(b, 25)}  (-> H_tr = 0.672457)")

# The interesting limit is m -> inf with eps*m -> const (so A stays bounded):
# that keeps R finite while eta = R/A ~ R/(eps m) -> 0: again bound -> H.
# So within a FIXED certified (eps, p, H), the chain max is H + O(1/sqrt(m)):
# no eps-rescaling can beat H without a larger certified eps.  Numerically the
# maxima above are all just below H_tr/H0 with small +eps corrections.

# The real lever is eps (the certified 7-point floor) and H (the window).
# For the joint limit at fixed A: solve for the max over (m, eps) with the
# constraint eps*(m-q) = A fixed (this is exactly the tawanerguo family):
#   bound = (H - tax(m))/(1 - Phi_m(A)/m),  tax(m) = (m-6)/(320 m).
# As m -> inf at fixed A: Phi_m(A) -> 2 sqrt(A) - 1 (branch 2), tax -> 1/320,
# so bound -> (H - 1/320)/1 = H - 1/320.  For H = H_tw = 0.6724587:
print("  tawan m->inf at fixed A: bound ->", mp.nstr(H_tw - mp.mpf(1)/320, 30))
print("  tawan best finite m:", mp.nstr(best_m[4], 30), " at m =", best_m[0])

# Compare with the 0.6818 ceiling:
print()
print("  in-class ceiling      :", mp.nstr(mp.mpf("0.68183123059534187426"), 30))
print("  gap best-certified    :", mp.nstr(mp.mpf("0.68183123059534187426") - best[2], 20))
print("  gap best-conjectured  :", mp.nstr(mp.mpf("0.68183123059534187426") - lim, 20))

print()

# --------------------------------------------------------------------------
# What eps would be needed to reach the ceiling with the trmdy/tawan chains?
# --------------------------------------------------------------------------

print("--- eps needed to reach 0.6818 (master chain, cap=h, p=1/2300, m=257) ---")
for target in [mp.mpf("0.6818"), mp.mpf("0.68183123059534187426")]:
    lo, hi = mp.mpf("1e-3"), mp.mpf("0.5")
    ok = False
    for _ in range(300):
        mid = (lo + hi) / 2
        b = block_bound_master(H_tr, mid, mp.mpf(1)/2300, 257, 6, "h")
        if b < target:
            lo = mid
        else:
            hi = mid
    b_hi = block_bound_master(H_tr, hi, mp.mpf(1)/2300, 257, 6, "h")
    print(f"  target {mp.nstr(target, 10)}: eps* = {mp.nstr(hi, 20)} (bound there {mp.nstr(b_hi, 20)})")
    # What per-7-window floor does that imply, and how far is it from the
    # certified 1/200 = 0.005?
    print(f"    vs certified 1/200 = 0.005: ratio {mp.nstr(hi / mp.mpf('0.005'), 8)}")

print()

# --------------------------------------------------------------------------
# Conjectured joint point: combine the best window (H_tr? or is there a better
# certified window in the family?) with a *hypothetical* larger eps.
# --------------------------------------------------------------------------

print("--- Conjectured parameter point (label: CONJECTURED) ---")
# Try: trmdy window (H=672457/1e6 certified) with the certified eps=1/200 and
# the *phi* cap instead of h (both are proven caps; phi is tighter for m>1).
b_phi257 = block_bound_master(H_tr, mp.mpf(1)/200, mp.mpf(1)/2300, 257, 6, "phi")
print("  trmdy eps=1/200, p=1/2300, m=257, cap=phi:", mp.nstr(b_phi257, 30))

# Largest eps that is plausibly certifiable: the trmdy per-window floor at
# the *weighted* design is 1/200; tawanerguo's redistributed one is 577/1e5.
# Both were reached by numerical search + verification.  A "next" floor is
# CONJECTURED; use 0.01 as an exploratory point with the trmdy window.
for epsc in [mp.mpf(1)/200, mp.mpf("0.0075"), mp.mpf("0.01"), mp.mpf("0.015"), mp.mpf("0.02")]:
    b = block_bound_master(H_tr, epsc, mp.mpf(1)/2300, 257, 6, "phi")
    print(f"  CONJ trmdy window, eps={mp.nstr(epsc, 8)}, m=257, cap=phi: {mp.nstr(b, 25)}")

print()
print("--- Done ---")
