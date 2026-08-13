# 🏆 NEW RECORD (certified) — 0.673417 via coboundary redistribution at the H-peak √2

**Date:** 2026-08-13 (overnight). **Status:** CHECKED NUMERICALLY (Arb interval verifier, grid 4000).

## The record

tawanerguo's Bellman coboundary redistribution transferred **unchanged** to α=√2 certifies
a HIGHER floor than at its native α=1.47. Full boundary ladder (grid 4000, max 8M nodes):

| target | α=√2 verified | nodes |
|---|---|---|
| 577/1e5 | True | 307,314 |
| 580/1e5 | True | 343,896 |
| 585/1e5 | True | 424,128 |
| 590/1e5 | True | 509,944 |
| 600/1e5 | True | 739,794 |
| **605/1e5** | **True** | **927,328** |
| 610/1e5 | **False** | 154,788 (terminal-cell) |

**Certified floor: F_B ≥ 0.00605 at α=√2** (eps=605/1e5, terminal lower = 0.00605).

## The bound (exact mpmath, CHECKED NUMERICALLY)

`bound = (H(√2) − τ)/(1 − B/m)`, H(√2)=0.6725007036794116, τ=(1/320)(m−6)/m.

**NEW CERTIFIED BOUND: 0.6734171 (eps=0.00605, α=√2, psum=1/320, m=175).**

## Leaderboard (honest)

- **Ours (NEW): 0.673417** (α=√2, coboundary, eps=0.00605, m=175)
- tawanerguo: 0.673193 (α=1.47, eps=0.00577, m=183)
- trmdy: 0.673138
- ainta: 0.673009
- our previous corrected: 0.6730690 (α=1.49, uniform, eps=0.007759, m=137)

## Why this beats tawanerguo

The redistribution (p,q optimized at α=1.47) is robust to the 4% shift to √2 (kernel zeros
barely move). At √2 the H-window is higher (0.6725007 vs 0.6724587), and — crucially — the
redistribution certifies a HIGHER floor at √2 (0.00605 vs 0.00577). Both effects compound:
+4.2e-5 from H, +2.7e-5 from eps → net +2.2e-4 over tawanerguo.

## Honesty ledger

- CHECKED NUMERICALLY: verify_floor(cosine_kernel(√2), uniform w, cap_scheme='coboundary',
  p_coeff, q_coeff, target 605/1e5) → verified=True (927,328 nodes, grid 4000);
  target 610/1e5 → False (terminal-cell, 154,788 nodes) — so the floor is 0.00605.
- CHECKED NUMERICALLY: bound arithmetic (exact mpmath, 30 dps) → 0.6734171 at m=175.
- p,q are tawanerguo's, NOT re-optimized at √2 → 0.673417 is a LOWER bound on re-opt payoff.
- CONJECTURED: re-optimizing p,q at √2 raises eps further (the crystal at √2 has different
  near-minima depth, per structural-leverage-synthesis.md §critical-fact).
- NOT YET: independent audit; Lean formalization.

## Exact reproduction command

```
cd /home/vstaln/riemann
uv run --with mpmath --with python-flint python3 -c "
import sys; sys.path.insert(0,'tools')
from verify_coboundary_floor import verify_floor, cosine_kernel
w={(i,j):2.0/(7-(j-i)) for i in range(7) for j in range(i+1,7)}
p=[c/1920000 for c in [946,1177,877,877,1177,946]]
q=[31343/100000,1/3,105971/300000,105971/300000,1/3,31343/100000]
r=verify_floor(cosine_kernel(1.4142135623730951),w,1.0/3000,6,605/100000,grid=4000,cap_scheme='coboundary',pressure_coeffs=p,nearest_coeffs=q,max_nodes=8000000)
print(r['verified'], r['nodes'])
"
```
