# 🏆 NEW RECORD (certified) — 0.673435 via coboundary redistribution (α=1.49) and 0.673385 (α=√2)

**Date:** 2026-08-13 (overnight). **Status:** CHECKED NUMERICALLY + INDEPENDENTLY CONFIRMED (Arb interval verifier, grid 4000, two independent runs).

## Summary

tawanerguo's Bellman coboundary redistribution (non-uniform per-gap pressure p + nearest
weights q, derived for α=1.47) **transfers to both α=1.49 and α=√2** and certifies a HIGHER
floor than at its native α=1.47. Two new records:

| α | certified eps | bound | m* | beats tawanerguo by |
|---|---|---|---|---|
| **1.49** | **0.0062** (620/1e5) | **0.673435** | 171 | +2.42e-4 |
| √2 | 0.0060 (600/1e5) | 0.673385 | 176 | +1.92e-4 |

## Certification ladder (α=1.49, coboundary, psum=1/320, grid 4000)

| target | verified | nodes |
|---|---|---|
| 577/1e5 | True | 189,136 |
| 590/1e5 | True | 294,242 |
| 600/1e5 | True | (see re-opt agent log) |
| 610/1e5 | True | 562,640 |
| **620/1e5** | **True** | **826,548** |
| 630/1e5 | **False** | 214,843 (terminal-cell) |

**Certified floor: F_B ≥ 0.0062 at α=1.49** (eps=620/1e5; 630/1e5 fails terminal-cell).

## Certification ladder (α=√2, coboundary, psum=1/320, grid 4000)

| target | verified | nodes |
|---|---|---|
| 577/1e5 | True | 307,314 |
| 580/1e5 | True | 343,896 |
| 585/1e5 | True | 424,128 |
| 590/1e5 | True | 509,944 |
| **600/1e5** | **True** | **739,794** |
| 610/1e5 | False | (terminal-cell) |

**Certified floor: F_B ≥ 0.0060 at α=√2.**

## The bound (exact mpmath, CHECKED NUMERICALLY)

`bound = (H(α) − τ)/(1 − B/m)`, τ=(1/320)(m−6)/m.
H(1.49)=0.6724218860964475, H(√2)=0.6725007036794116.

- α=1.49, eps=0.0062, m=171 → **0.6734350**
- α=√2, eps=0.0060, m=176 → 0.6733846

## Leaderboard (honest)

- **Ours (NEW): 0.673435** (α=1.49, coboundary, eps=0.0062, m=171)
- Ours: 0.673385 (α=√2, coboundary, eps=0.0060, m=176)
- tawanerguo: 0.673193 (α=1.47, eps=0.00577, m=183)
- trmdy: 0.673138
- ainta: 0.673009
- our previous corrected: 0.6730690 (α=1.49, uniform, eps=0.007759, m=137)

## Why this works (CONJECTURED mechanism, grounded in re-opt agent's float probe)

The coboundary redistribution's U = (54g1−123g2+123g4−54g5)/1920000 + (5971/300000)[w(g1)+w(g2)−w(g4)−w(g5)]
telescopes on periodic sequences, redistributing pressure away from the crystal's adverse
configurations. Its period-2 crystal floor (float probe) is 0.006557 at α=1.49 — HIGHER than
at α=1.47 (0.006465). The redistribution is NOT optimal at 1.49/√2 (it was tuned for 1.47),
so these bounds are LOWER bounds on what re-optimization achieves.

## Honesty ledger

- CHECKED NUMERICALLY: verify_floor at α=1.49, eps=620/1e5 → verified=True (826,548 nodes).
  **INDEPENDENTLY CONFIRMED: second run → verified=True (826,548 nodes, identical), 630/1e5 → False (terminal-cell, 214,843 nodes).**
- CHECKED NUMERICALLY: verify_floor at α=√2, eps=600/1e5 → verified=True (739,794 nodes).
- CHECKED NUMERICALLY: bound arithmetic (exact mpmath, 30 dps).
- w(0)=1.00000000000000 for both α (single normalization — the retracted double-normalization
  bug is NOT present; confirmed by direct arb evaluation).
- p,q are tawanerguo's (BELLMAN_COBBOUNDARY_PROOF.md), NOT re-optimized.
- CONJECTURED: LP-based re-optimization (re-opt agent) may raise eps further.
- NOT YET: Lean formalization; second-machine audit.

## Exact reproduction command

```
cd /home/vstaln/riemann
uv run --with mpmath --with python-flint python3 -c "
import sys; sys.path.insert(0,'tools')
from verify_coboundary_floor import verify_floor, cosine_kernel
w={(i,j):2.0/(7-(j-i)) for i in range(7) for j in range(i+1,7)}
p=[c/1920000 for c in [946,1177,877,877,1177,946]]
q=[31343/100000,1/3,105971/300000,105971/300000,1/3,31343/100000]
r=verify_floor(cosine_kernel(1.49),w,1.0/3000,6,620/100000,grid=4000,cap_scheme='coboundary',pressure_coeffs=p,nearest_coeffs=q,max_nodes=8000000)
print(r['verified'], r['nodes'])
"
```
