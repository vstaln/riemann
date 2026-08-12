# 🏆 RECORD REFINEMENT — α-optimization: 0.673481 at α=1.464 (was 0.673435 at α=1.49)

**Date:** 2026-08-13 (overnight). **Status:** CHECKED NUMERICALLY (Arb interval verifier, grid 4000).

## The finding

The coboundary redistribution certifies eps=0.0062 (620/1e5) not just at α=1.49 (our first
record) but across a RANGE of α. Since H(α) is maximized at √2 and DECREASES as α rises above
√2≈1.414, the best bound comes from the LOWEST α that still certifies eps=0.0062.

The eps=0.0062 certification boundary is at α* ∈ (1.463, 1.464):

| α | eps=0.0062 | nodes | H(α) |
|---|---|---|---|
| 1.46 | False | 514,451 (terminal) | 0.6724727 |
| 1.462 | False | 508,520 | — |
| 1.463 | False | 503,074 | — |
| **1.464** | **True** | **1,096,556** | **0.6724674** |
| 1.465 | True | 1,064,638 | 0.6724660 |
| 1.47 | True | 999,112 | 0.6724587 |
| 1.48 | True | 907,190 | 0.6724459 |
| 1.49 | True | 826,548 | 0.6724219 |

**NEW RECORD: 0.6734809** at (α=1.464, psum=1/320, eps=0.0062, m=171).

Also: **eps=0.0063 fails at ALL α tested** (1.465, 1.47, 1.49 all terminal-cell) — so eps=0.0062
is the certified ceiling for tawan's UNCHANGED redistribution.

## Leaderboard (honest)

- **Ours (NEW): 0.673481** (α=1.464, eps=0.0062, m=171)
- Ours: 0.673435 (α=1.49, eps=0.0062, m=171)
- Ours: 0.673385 (α=√2, eps=0.0060, m=176)
- tawanerguo: 0.673193 (α=1.47, eps=0.00577, m=183)
- trmdy: 0.673138 · ainta: 0.673009 · our prior: 0.6730690

## Distinct-zeros corollary (PROVEN, distinct-zeros-56-refinement.md)

Theorem C's 5/6 = (1+H)/2 affine image. Our H=0.673481 → **distinct ≥ (1+0.673481)/2 = 0.836740**,
beating Anthropic's optimized 0.83625 by +4.9e-4.

## Honesty ledger

- CHECKED NUMERICALLY: verify_floor at α=1.464, eps=620/1e5 → verified=True (1,096,556 nodes).
- CHECKED NUMERICALLY: bound arithmetic (exact mpmath) → 0.6734809 at m=171.
- eps=0.0063 FAILS at all tested α (terminal-cell) — the 0.0062 ceiling for tawan's coefficients.
- p,q are tawanerguo's UNCHANGED. LP re-optimization (to break 0.0062) in progress separately.
- CONJECTURED: a re-optimized (l,c) could raise eps past 0.0062 (see coboundary-reopt-corrected.md).
- NOT YET: Lean formalization.

## Exact reproduction command

```
cd /home/vstaln/riemann
uv run --with mpmath --with python-flint python3 -c "
import sys; sys.path.insert(0,'tools')
from verify_coboundary_floor import verify_floor, cosine_kernel
w={(i,j):2.0/(7-(j-i)) for i in range(7) for j in range(i+1,7)}
p=[c/1920000 for c in [946,1177,877,877,1177,946]]
q=[31343/100000,1/3,105971/300000,105971/300000,1/3,31343/100000]
r=verify_floor(cosine_kernel(1.464),w,1.0/3000,6,620/100000,grid=4000,cap_scheme='coboundary',pressure_coeffs=p,nearest_coeffs=q,max_nodes=8000000)
print(r['verified'], r['nodes'])
"
```
