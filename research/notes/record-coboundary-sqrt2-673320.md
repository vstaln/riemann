# 🏆 NEW RECORD (certified) — 0.673320 via coboundary redistribution at the H-peak √2

**Date:** 2026-08-13 (overnight). **Status:** CHECKED NUMERICALLY (Arb interval verifier, grid 4000).
**Labels:** per hooks/agents.md — all numerics CHECKED NUMERICALLY with exact commands below.

## The record

tawanerguo's Bellman coboundary redistribution — non-uniform per-gap pressure
`p = (946,1177,877,877,1177,946)/1920000` (sum = 1/320) and nearest weights
`q = (31343/1e5, 1/3, 105971/3e5, 105971/3e5, 1/3, 31343/1e5)` — transferred
**unchanged** to the H-peak α=√2, certifies a HIGHER floor than at its native α=1.47:

| target | α=√2 verified | nodes |
|---|---|---|
| 577/1e5 | True | 307,314 |
| 580/1e5 | True | 343,896 |
| 585/1e5 | True | 424,128 |
| **590/1e5** | **True** | **509,944** |
| 600/1e5 | (in progress) | — |

## The bound (exact mpmath, CHECKED NUMERICALLY)

`bound = (H(√2) − τ)/(1 − B/m)`, τ = psum·(m−6)/m = (1/320)(m−6)/m, H(√2)=0.6725007036794116.

| eps | bound | m* |
|---|---|---|
| 0.00577 (tawan's own) | 0.6732351 | 183 |
| 0.00585 | 0.6732872 | 180 |
| **0.00590** | **0.6733197** | 179 |
| 0.00595 | 0.6733521 | 178 |
| 0.00600 | 0.6733846 | 176 |

**NEW CERTIFIED BOUND: 0.673320 (eps=0.00590, α=√2, psum=1/320, m=179).**

## Leaderboard (honest)

- **Ours (NEW): 0.673320** (α=√2, coboundary, eps=0.00590 certified, m=179)
- tawanerguo: 0.673193 (α=1.47, coboundary, eps=0.00577, m=183)
- trmdy: 0.673138
- ainta: 0.673009
- our previous corrected: 0.6730690 (α=1.49, uniform 7-pt, eps=0.007759, m=137)

## Why this beats tawanerguo

Same redistribution certifies the SAME (actually higher) floor, but at the H-peak √2
where H=0.6725007 > H(1.47)=0.6724587. The redistribution is robust to the 4% shift in
α (kernel zeros barely move: √2 vs 1.47), while the H-window gains +4.2e-5. The result:
eps climbs from 0.00577 to 0.00590 at the same node budget, and the bound climbs
+1.3e-4 to 0.673320.

## Honesty ledger

- CHECKED NUMERICALLY: verify_floor(cosine_kernel(√2), uniform w, cap_scheme='coboundary',
  p_coeff, q_coeff, target 590/1e5) → verified=True (509,944 nodes, grid 4000).
- CHECKED NUMERICALLY: bound arithmetic (exact mpmath, 30 dps).
- The p,q are tawanerguo's (from BELLMAN_COBBOUNDARY_PROOF.md), NOT re-optimized at √2 —
  so 0.673320 is a LOWER bound on what re-optimization could achieve.
- CONJECTURED: re-optimizing p,q at √2 raises eps further (target 0.0060 → 0.673385,
  or beyond).
- NOT YET: independent audit on a second machine; Lean-level formalization.

## Exact reproduction command

```
cd /home/vstaln/riemann
uv run --with mpmath --with python-flint python3 -c "
import sys; sys.path.insert(0,'tools')
from verify_coboundary_floor import verify_floor, cosine_kernel
w={(i,j):2.0/(7-(j-i)) for i in range(7) for j in range(i+1,7)}
p=[c/1920000 for c in [946,1177,877,877,1177,946]]
q=[31343/100000,1/3,105971/300000,105971/300000,1/3,31343/100000]
r=verify_floor(cosine_kernel(1.4142135623730951),w,1.0/3000,6,590/100000,grid=4000,cap_scheme='coboundary',pressure_coeffs=p,nearest_coeffs=q,max_nodes=5000000)
print(r['verified'], r['nodes'])
"
```
