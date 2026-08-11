#!/usr/bin/env python3
"""Probe A: (i) algebraic identity bound/N = 1 - mean((lambda-1)^2);
(ii) imperfection-sensitivity (Koiter-style) fit of the documented sandbox off-line injection data.
Uses ONLY numbers already reported in research/notes/attack-sandbox.md world (b) — no new compute."""
import numpy as np

# (i) identity check (exact algebra)
print("=== (i) spectral-concentration identity ===")
# bound = 2*tr - HS2 = sum(2*lam - lam^2) ; 2*lam - lam^2 = 1 - (lam-1)^2
# check on the crystal law: masses {1/6 at 0, 2/3 at 1, 1/6 at 2}
masses = {0: 1/6, 1: 2/3, 2: 1/6}
tr = sum(m*v for v, m in masses.items())
hs2 = sum(m*v*v for v, m in masses.items())
bound = 2*tr - hs2
conc = sum(m*(v-1)**2 for v, m in masses.items())
print(f"crystal: tr={tr:.6f} HS2={hs2:.6f} bound={bound:.6f}  1-conc={1-conc:.6f}  match={abs(bound-(1-conc))<1e-12}")
# real asymptotic: tr=1, HS2=c=1.3274993 -> bound=0.6725007, conc=0.3274993
c = 1/2 + (1/np.sqrt(2))*1/np.tan(1/np.sqrt(2))
print(f"real asymptote: HS2=c={c:.10f} bound={2-c:.10f}  conc={c-1:.10f}  1-(c-1)={2-c:.10f}")

# (ii) Koiter-style fit of sandbox world (b), det pattern, beta=0.3 (truth s1/N = 1-2f)
print("\n=== (ii) off-line injection: certificate vs imperfection amplitude f (det pattern, beta=0.3) ===")
data = [  # (f, bound_s1/N)
    (0.00, 0.704598),  # T=500 baseline from world (a) table
    (0.01, 0.679652),
    (0.02, 0.650527),
    (0.05, 0.562997),
]
f = np.array([d[0] for d in data]); b = np.array([d[1] for d in data])
delta = b - 0.6725007037
print("f     bound_s1  Delta=bound-0.6725")
for fi, bi, di in zip(f, b, delta): print(f"{fi:5.2f}  {bi:.6f}  {di:+.6f}")
# fit Delta(f) = -A f^p  (only the f>0 points; note Delta>0 at f=0.01 is above 0.6725)
mask = f > 0
if mask.sum() >= 3:
    logf, logd = np.log(f[mask]), np.log(-delta[mask])
    p, logA = np.polyfit(logf, logd, 1)
    print(f"power-law fit: Delta ~ -{np.exp(logA):.4f} * f^{p:.3f}")
    # try linear-in-f through origin and quadratic
    for deg in (1, 2):
        coef = np.polyfit(f[mask], -delta[mask], deg)
        pred = -np.polyval(coef, f[mask])
        print(f"poly deg {deg} coefs {np.round(coef,4)}  rss={np.sum((pred+delta[mask])**2):.2e}")
# Koiter classic: Delta ~ -C f^(3/2) for symmetric imperfection; check exponent empirically
print("\nInterpretation: classical Koiter imperfection-sensitivity (symmetric imperfection) is Delta ~ -C*f^(2/3);")
print("the measured exponent will tell whether the off-line 'imperfection' acts like a symmetric load (2/3) or")
print("a linear defect (1) — a mechanism tag for the certificate's off-line sensitivity.")
