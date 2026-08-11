#!/usr/bin/env python3
"""attack_conditioning_support.py -- supporting facts for attack-conditioning.md.

(i)  <1,T1> = 1/3 > 0  (the constant function is the single positive direction of T),
(ii) |s-s'| is conditionally negative definite: <w,Tw> <= 0 for every zero-mean w
     (explains why the tangent-space curvature of Q caps at 1: on T, <w,Mw> <= <w,w>),
(iii) sin(pi u) has T-eigenvalue -2/pi^2 (validator-corrected min of I+T = 1 - 2/pi^2 ~ 0.797),
(iv)  boundary-ramp cost is linear: delta(Q) ~ 0.45*w in ramp width w (small w).

Run:  uv run --quiet --with numpy python3 tools/attack_conditioning_support.py
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS","2")
import numpy as np
N=2000; h=1.0/N
us=(np.arange(N)+0.5)*h-0.5
T=np.abs(us[:,None]-us[None,:])*h
one=np.ones(N)
# <1,T1> should be 1/3 (positive: the constant is T's only positive direction)
print("<1,T1> =", np.dot(one, T@one)*h, " (analytic 1/3)")
# conditional negative definiteness: <w,Tw> <= 0 for all w with sum w_i h = 0
rng=np.random.default_rng(1)
worst=0.0
for _ in range(60):
    w=rng.standard_normal(N)
    w=w-np.mean(w)
    val=np.dot(w, T@w)*h
    worst=max(worst,val)
print("max <w,Tw> over 60 random zero-mean w =", worst, "(should be <= 0 up to noise)")
# also the sin(pi u) value (analytic -1/pi^2 * <w,w>)
w=np.sin(np.pi*us)
print("<sin,Tsin>/<sin,sin> =", np.dot(w,T@w)*h/np.dot(w,w)/h, " (analytic -2/pi^2 =", -2/np.pi**2,")")
# ramp linearity: delta(w)/w
def Q(v): return np.dot(v,(np.eye(N)+T)@v)*h/(np.dot(v,one)*h)**2
v0=np.cos(np.sqrt(2)*us); c=Q(v0)
print("ramp delta/w for w-ramp widths:")
for wdt in (0.002,0.004,0.008,0.016,0.032,0.064):
    d=0.5-np.abs(us); t=np.clip(d/wdt,0,1)
    v=v0*t
    print(f"  w={wdt:.3f}: delta={Q(v)-c:.6f}  delta/w={ (Q(v)-c)/wdt:.4f}")
