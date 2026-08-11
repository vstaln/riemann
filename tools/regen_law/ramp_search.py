#!/usr/bin/env python3
"""Search: do configurations with f(j) ~ c*j (ramp spectra) exist? Optimize positions.
If yes, their structure reveals the family. Also check mixtures of a few ramp-like configs."""
import numpy as np
from scipy.optimize import minimize

N = 256

def spectrum(positions, N=256):
    j = np.arange(1, N+1)
    z = np.zeros(N, dtype=complex)
    for x in positions:
        z += np.exp(2j*np.pi*j*x/N)
    return np.abs(z)**2

def ramp_objective(params, n, N=256, c=None):
    # positions sorted, distinct
    x = np.sort(params)
    f = spectrum(x, N)
    if c is None:
        # free c: minimize ||f - c j|| with c = <f,j>/<j,j>
        c = f[:255].dot(np.arange(1,256))/np.arange(1,256).dot(np.arange(1,256))
    resid = np.sqrt(np.mean((f[:255] - c*np.arange(1,256))**2))
    return resid

# try: positions = k + eps_k with eps in {0, 1/2} (binary jitter) - optimize the jitter pattern?
# First: just check what spectrum the "half-integer lattice" gives and simple variants
def test_cfg(name, positions):
    f = spectrum(positions)
    # best-fit ramp c
    t = np.arange(1, 256)
    c = f[:255].dot(t)/t.dot(t)
    rel = np.max(np.abs(f[:255]-c*t)/np.maximum(c*t, 1e-9))
    print(f"{name}: best-fit c = {c:.4f}, max rel dev = {rel:.4f}, f(1)={f[0]:.2f}, f(255)={f[254]:.2f}")

# half-lattice: even positions
test_cfg("even lattice (128 pts, mark2?)", list(range(0, 256, 2))*1)
# 256 pts at 0.5-spacing: x = k/2
test_cfg("x=k/2, k=0..255", [k/2 for k in range(256)])
# two interleaved: x = 2k and x = 2k+1
test_cfg("all 0..255", list(range(256)))
# jittered: x = k + (k mod 2)*0.5
test_cfg("alternating jitter", [k + (0.5 if k%2 else 0.0) for k in range(256)])
# x = k + frac(k*phi) for irrational-like phi rational
test_cfg("k + (k*3/8 mod 1)", [k + (k*3/8 % 1) for k in range(256)])
test_cfg("k + (k*5/16 mod 1)", [k + (k*5/16 % 1) for k in range(256)])
test_cfg("k + (k*1/3 mod 1)", [k + (k*1/3 % 1) for k in range(256)])
# random jittered
rng = np.random.default_rng(0)
test_cfg("random jitter eps~U(0,0.5)", [k + 0.5*rng.random() for k in range(256)])

# Optimize: find positions minimizing deviation from a ramp
print("\n--- optimize a small perturbation to match ramp c*j ---")
def obj(x):
    f = spectrum(np.sort(x))
    t = np.arange(1, 256)
    c = f[:255].dot(t)/t.dot(t)
    return np.sum((f[:255] - c*t)**2)

rng = np.random.default_rng(1)
for trial in range(3):
    x0 = np.arange(N) + 0.5*rng.random(N)*0.2
    res = minimize(obj, x0, method='Nelder-Mead', options={'maxiter': 300, 'xatol': 1e-4, 'fatol': 1e-6})
    f = spectrum(np.sort(res.x))
    t = np.arange(1,256)
    c = f[:255].dot(t)/t.dot(t)
    print(f"trial {trial}: obj = {res.fun:.2e}, best c = {c:.4f}, f(1)={f[0]:.3f} f(2)={f[1]:.3f} f(128)={f[127]:.2f} f(255)={f[254]:.2f}")
