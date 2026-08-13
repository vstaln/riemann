# 🚨 DISCOVERY (candidate) — tawanerguo's coboundary redistribution TRANSFERS to the H-peak α=√2, beating tawanerguo

**Date:** 2026-08-13 (overnight). **Status:** CHECKED NUMERICALLY (certified by verify_coboundary_floor.py, Arb interval, grid 4000) — pending boundary confirmation and independent audit.
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED per hooks/agents.md.

## The finding

tawanerguo's Bellman coboundary redistribution — the non-uniform per-gap pressure
`p = (946,1177,877,877,1177,946)/1920000` (sum = 1/320) and nearest-neighbor weights
`q = (31343/1e5, 1/3, 105971/3e5, 105971/3e5, 1/3, 31343/1e5)` — was optimized for
α=1.47. It **transfers unchanged to α=√2 (the window H-peak)** and certifies the SAME
floor `F_B ≥ 577/1e5 = 0.00577` there (verified=True, 307,314 nodes, grid 4000).

The consequence (bound arithmetic CHECKED NUMERICALLY, exact mpmath):

| config | H | eps | bound |
|---|---|---|---|
| tawanerguo (α=1.47, psum=1/320, m=183) | 0.6724587 | 0.00577 | 0.6731929 |
| **TRANSFER (α=√2, psum=1/320, m=183)** | **0.6725007** | 0.00577 | **0.6732351** |

**The transfer beats tawanerguo by +4.2e-5**, because α=√2 has H=0.6725007 > α=1.47's
H=0.6724587, and the SAME redistribution certifies the SAME eps=0.00577 at both.

## Why this works (CONJECTURED mechanism)

The coboundary redistribution's coefficients were chosen to break the crystal adversary
at α=1.47's kernel zeros (z1≈1.057, z2≈2.030). At α=√2 the kernel zeros shift to
z1≈1.0572782910, z2≈2.0300675301, z3≈3.0202429921 (essentially the same, since √2≈1.4142
and 1.47 differ by only 4%). The redistribution is robust to this small zero-shift — it
still certifies 577/1e5.

## If the redistribution is RE-OPTIMIZED at √2 (CONJECTURED)

The coefficients are NOT optimal at √2. The bound arithmetic shows the payoff of pushing
eps higher at √2 (m re-optimized):
- eps=0.0058 → 0.673255 (m=182)
- eps=0.0059 → 0.673320 (m=179)
- eps=0.0060 → 0.673385 (m=176)

Each +1e-4 in eps is worth ~+6.5e-5 in bound. If re-optimizing p,q at √2 certifies
eps=0.0060, the bound reaches **0.673385** (+1.9e-4 over tawanerguo).

## Honesty ledger

- CHECKED NUMERICALLY: verify_floor(cosine_kernel(√2), uniform w, cap_scheme='coboundary',
  p_coeff, q_coeff, target 577/1e5) → verified=True (307,314 nodes, grid 4000, Arb interval).
- CHECKED NUMERICALLY: bound = (H(√2) − 59/19520)/(1 − B/183) = 0.6732351414153908.
- The p,q coefficients are tawanerguo's (from BELLMAN_COBBOUNDARY_PROOF.md), NOT re-derived.
- The bound formula and H are exactly those of evaluate_coboundary_bound.py (tawan's own).
- CONJECTURED: that re-optimizing p,q at √2 raises eps (not yet run).
- NOT YET: independent audit; the α=√2 certificate is a single verifier run (grid 4000),
  not yet Lean-checked or cross-verified on a second machine.

## Commands

```
cd /home/vstaln/riemann
uv run --with mpmath --with python-flint python3 -c "
import sys; sys.path.insert(0,'tools')
from verify_coboundary_floor import verify_floor, cosine_kernel
w={(i,j):2.0/(7-(j-i)) for i in range(7) for j in range(i+1,7)}
p=[c/1920000 for c in [946,1177,877,877,1177,946]]
q=[31343/100000,1/3,105971/300000,105971/300000,1/3,31343/100000]
r=verify_floor(cosine_kernel(1.4142135623730951),w,1.0/3000,6,577/100000,grid=4000,cap_scheme='coboundary',pressure_coeffs=p,nearest_coeffs=q,max_nodes=5000000)
print(r['verified'])
"
```
