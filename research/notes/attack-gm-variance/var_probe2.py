#!/usr/bin/env python
"""Windowed zero-counting variance on real zeta zeros (10k zeros) - v2.

Clean version:
 - exact window mean  M(t,U) = (1/2pi)[(t+U)(log((t+U)/2pi)-1) - t(log(t/2pi)-1)]
   (integral of the local density over (t, t+U])
 - per-U top margin so no window truncates against the end of the zero list
 - dictionary: probe weight in form-factor space = sinc^2(pi*alpha*U*rho),
   rho = local density, so alpha ~ 1/(U*rho);  beyond-1 (alpha>1) <-> U < 1/rho.
 - compares with GUE number variance (1/pi^2)(log(2*pi*n)+1+gamma), n = U*rho,
   and with the Poisson (independent zeros) prediction V = n.
"""
import numpy as np
from math import log, pi
euler_gamma = 0.5772156649015329

g = np.loadtxt("/home/vstaln/riemann/tools/data/zeros_computed_10000.txt", usecols=1)
N = len(g)
print(f"loaded {N} zeros, gamma_1={g[0]:.3f}, gamma_N={g[-1]:.3f}")

def exact_mean(t, U):
    """(1/2pi) int_t^{t+U} log(s/2pi) ds = (1/2pi)[(t+U)(log((t+U)/2pi)-1) - t(log(t/2pi)-1)]"""
    return (1/(2*pi)) * ((t+U)*(np.log((t+U)/(2*pi)) - 1) - t*(np.log(t/(2*pi)) - 1))

def gue(n):
    return (1/pi**2) * (log(max(n,1e-9) * 2*pi) + 1 + euler_gamma)

# beyond-1 weight fraction of the probe window sinc^2(pi*alpha*n) at |alpha|>1
def beyond1_frac(n):
    if n <= 0: return 1.0
    # (2/pi) int_0^{pi n} sinc^2(u) du,  sinc(u)=sin u / u
    du = 1e-4
    u = np.arange(du, pi*n, du)
    return 1.0 - (2.0/pi) * np.sum((np.sin(u)/u)**2) * du

def fujii(n):
    """Fujii leading term (GLSS25 Prop 2): (1/pi^2) log(2 + UL), UL = n spacings."""
    return (1/pi**2) * log(2.0 + n)

T0 = 2000.0
M = 4000
results = []
for U in [0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.8,0.9,0.93,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.8,2.0,2.2,2.5,3.0,3.5,4.0,5.0,6.0,7.0,8.0,10.0,12.0,15.0,20.0,30.0,40.0,60.0,80.0]:
    T1 = g[-1] - U - 10.0
    if T1 <= T0: break
    t = np.linspace(T0, T1, M)
    lo = np.searchsorted(g, t, side='right'); hi = np.searchsorted(g, t+U, side='left')
    c = (hi - lo).astype(float)
    m = exact_mean(t, U)
    V_fluct = ((c - m)**2).mean()
    V_raw = c.var()
    rho_t = np.log(t/(2*pi))/(2*pi)
    rho = rho_t.mean()
    n = U*rho
    results.append((U, n, V_fluct, V_raw, gue(n), beyond1_frac(n)))
    print(f"U={U:7.3f}  n={n:7.3f}  V_fluct={V_fluct:9.4f}  V_raw={V_raw:9.4f}  "
          f"GUE={gue(n):9.4f}  Vf/GUE={V_fluct/gue(n):6.3f}  Fujii={fujii(n):9.4f}  "
          f"Poisson={n:7.3f}  beyond1_wgt={beyond1_frac(n):6.3f}")

# five alpha windows under corrected dictionary alpha ~ 1/n  (n = U rho)
print("\n=== corrected-dictionary windows  U = 1/(alpha*rho), alpha in {0.5,0.9,1.1,1.5,2.0} ===")
rho_avg = np.mean(np.log(np.linspace(T0, g[-1]-3.0, 2000)/(2*pi))/(2*pi))
print(f"rho_avg over [2000, {g[-1]-3:.0f}] = {rho_avg:.4f}  ->  alpha=1 boundary U* = 1/rho = {1/rho_avg:.3f}")
print(f"{'alpha':>6} {'U':>8} {'n':>7} {'V_fluct':>9} {'GUE':>9} {'Vf/GUE':>7} {'Fujii':>9} {'Poisson':>8} {'beyond1wgt':>10}")
for alpha in [0.5,0.9,1.1,1.5,2.0]:
    U = 1.0/(alpha*rho_avg)
    T1 = g[-1] - U - 10.0
    t = np.linspace(T0, T1, 4000)
    lo = np.searchsorted(g, t, side='right'); hi = np.searchsorted(g, t+U, side='left')
    c = (hi-lo).astype(float)
    Vf = ((c - exact_mean(t,U))**2).mean()
    n = U*rho_avg
    print(f"{alpha:6.2f} {U:8.3f} {n:7.3f} {Vf:9.4f} {gue(n):9.4f} {Vf/gue(n):7.3f} "
          f"{fujii(n):9.4f} {n:8.3f} {beyond1_frac(n):10.3f}")

# B10's dictionary windows  U = alpha*T_ref  (shown to be inoperative: beyond data range)
print("\n=== B10 dictionary windows  U = alpha*T_ref  (T_ref = geometric mean height) ===")
T_ref = np.exp(np.mean(np.log(np.linspace(T0, g[-1]-3.0, 2000))))
print(f"T_ref = {T_ref:.0f}")
for alpha in [0.5,0.9,1.1,1.5,2.0]:
    U = alpha*T_ref
    print(f"alpha={alpha:.1f}: U = {U:9.1f}  (window longer than the whole zero range "
          f"[{g[0]:.0f},{g[-1]:.0f}] for alpha>=1.5; count variance there is mean-drift dominated, not a beyond-1 probe)")

print("\nalpha=1 boundary: U* = 1/rho_avg =", 1/rho_avg, " (one mean spacing at height ~T_ref)")
