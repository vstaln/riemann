# 🏆 NEW RECORD (certified) — 0.673385 via coboundary redistribution at the H-peak √2

**Date:** 2026-08-13 (overnight). **Status:** CHECKED NUMERICALLY (Arb interval verifier, grid 4000).

## The record

tawanerguo's Bellman coboundary redistribution transferred **unchanged** to α=√2 certifies
F_B ≥ 600/1e5 = 0.00600 (verified=True, 739,794 nodes). Full ladder (all True):

| target | α=√2 verified | nodes |
|---|---|---|
| 577/1e5 | True | 307,314 |
| 580/1e5 | True | 343,896 |
| 585/1e5 | True | 424,128 |
| 590/1e5 | True | 509,944 |
| **600/1e5** | **True** | **739,794** |

## The bound (exact mpmath, CHECKED NUMERICALLY)

`bound = (H(√2) − τ)/(1 − B/m)`, H(√2)=0.6725007036794116, τ=(1/320)(m−6)/m.

| eps | bound | m* |
|---|---|---|
| 0.00590 | 0.6733197 | 179 |
| **0.00600** | **0.6733846** | 176 |

**NEW CERTIFIED BOUND: 0.673385 (eps=0.00600, α=√2, psum=1/320, m=176).**

## Leaderboard (honest)

- **Ours (NEW): 0.673385** (α=√2, coboundary, eps=0.00600, m=176)
- tawanerguo: 0.673193 (α=1.47, eps=0.00577, m=183)
- trmdy: 0.673138
- ainta: 0.673009
- our previous corrected: 0.6730690 (α=1.49, uniform, eps=0.007759, m=137)

## Honesty ledger

- CHECKED NUMERICALLY: verify_floor(cosine_kernel(√2), uniform w, cap_scheme='coboundary',
  p_coeff, q_coeff, target 600/1e5) → verified=True (739,794 nodes, grid 4000).
- CHECKED NUMERICALLY: bound arithmetic (exact mpmath, 30 dps).
- p,q are tawanerguo's, NOT re-optimized at √2 → 0.673385 is a lower bound on re-opt payoff.
- CONJECTURED: re-optimizing p,q at √2 raises eps further (boundary > 0.0060 not yet found).
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
r=verify_floor(cosine_kernel(1.4142135623730951),w,1.0/3000,6,600/100000,grid=4000,cap_scheme='coboundary',pressure_coeffs=p,nearest_coeffs=q,max_nodes=5000000)
print(r['verified'], r['nodes'])
"
```
