# CURRENT FINAL CERTIFIED RECORD — 2026-08-18

**Status:** CHECKED NUMERICALLY; native Rust full certification complete. This updates the prior record below. The result is a proportion theorem only and is **not evidence for RH**.

## Current record

- **Simple zeros on the critical line:** `>= 0.6735310829992681328867805395...` (67.3531083%)
- **Distinct zeros:** `>= 0.8367655414996340664433902697...` (83.6765541%), by the PROVEN affine corollary `(1+H)/2`.

Improvement over the prior banked record:

- simple: `+0.000050221324754...`
- distinct: `+0.000025110662377...`

## Certified configuration

| parameter | value |
|---|---|
| cosine alpha | `1.464` |
| dilation lambda | `1.15` |
| p coefficients | `lambda*[946,1177,877,877,1177,946]/1920000` |
| q coefficients | `lambda*[0.31343,1/3,105971/300000,105971/300000,1/3,0.31343]` |
| pair weights | `2/(7-(j-i))`, all `0 <= i < j <= 6` |
| pressure convention | `1/3000` |
| certified floor | `epsilon=0.0069800` |
| optimizing m | `153` |
| verifier | native `tools/verifier-rs` hybrid interval verifier |
| native result | `CASE D verified=true, nodes=838372` |

Native Rust hostile acceptance set on the same code path:

- **A:** old baseline `epsilon=0.0062` → `verified=true`, `nodes=1,094,486`.
- **B:** ceiling `epsilon=0.0063` → `verified=false`, terminal cell low `0.006289525020944827`.
- **D:** lambda-dilation candidate above → `verified=true`, `nodes=838,372`.
- The three independent sanctioned arb reference runs also agreed at `838,742` nodes; native Rust D is the decisive certification used for this record.

The independent 200-bit Rust bound computation gives `m=153` and the value above. The full native run used outward-rounded interval tables, LDL convexity checks, and the tighter point-tangent fallback only when the cell tangent did not resolve a box.

## RH firewall

This is a **CHECKED NUMERICALLY** proportion-on-line record, not a proof of RH and not evidence for RH. Direct-RH levers remain open and must continue under the campaign protocol.

---

# 🏆 FINAL CERTIFIED RECORD (session 2026-08-13) — 0.673481 simple-on-line, 0.836740 distinct

**Status:** CHECKED NUMERICALLY (Arb interval verifier, grid 4000), independently re-run 3× with identical node counts.

## The record

**Simple-on-line proportion: ≥ 0.6734808616745137** (67.348%)
**Distinct zeros proportion: ≥ 0.8367404308372568** (83.674%, via the PROVEN affine corollary (1+H)/2)

Both certified by the tawanerguo Bellman coboundary redistribution transferred to α=1.464:

| parameter | value |
|---|---|
| α (cosine window) | 1.464 |
| redistribution | tawanerguo's p,q (UNCHANGED) |
| psum | 1/320 |
| certified eps | 0.0062 (620/1e5; 630/1e5 FAILS terminal-cell) |
| m | 171 |
| verifier | tools/verify_coboundary_floor.py (corrected single-normalization) |
| nodes | 1,096,556 (3 identical independent runs) |

## The bound chain (all CHECKED NUMERICALLY, exact mpmath)

bound = (H(α) − τ)/(1 − B/m),  τ = (1/320)(m−6)/m,  H(1.464) = 0.672467425578.

## Leaderboard (honest)

| bound | source | mechanism |
|---|---|---|
| **0.673481** | **Ours (this session)** | coboundary redistribution @ α=1.464, eps=0.0062 |
| 0.673435 | Ours (earlier tonight) | coboundary @ α=1.49, eps=0.0062 |
| 0.673193 | tawanerguo | coboundary @ α=1.47, eps=0.00577 |
| 0.673138 | trmdy | — |
| 0.673069 | our prior corrected | uniform 7-pt @ α=1.49, eps=0.007759 |
| 0.673009 | ainta | uniform 7-pt |

## The discovery (this session)

tawanerguo's coboundary redistribution (the mechanism giving them 0.673193) **transfers unchanged
to a RANGE of α and certifies a HIGHER floor (eps=0.0062) than at its native α=1.47 (eps=0.00577)**.
The α that maximizes the bound is the lowest α still certifying eps=0.0062, i.e. the boundary
α* ∈ (1.4638, 1.464), where H(α) is highest while the crystal floor still clears 0.0062.

## Honesty ledger

- CHECKED NUMERICALLY: verify_floor(cosine_kernel(1.464), uniform w, cap_scheme='coboundary', p,q,
  target 620/1e5) → verified=True (1,096,556 nodes), 3 independent identical runs.
- CHECKED NUMERICALLY: 630/1e5 → False (terminal-cell) — eps=0.0062 is the certified ceiling for
  unchanged coefficients.
- PROVEN: distinct = (1+H)/2 (Theorem C is the affine image of the simple-zeros constant H;
  distinct-zeros-56-refinement.md). So distinct ≥ 0.836740.
- PROVEN + CHECKED: LP re-optimization of the redistribution does NOT beat tawan (its solution has
  p_2 < 0 violating κ_i ≥ 0, and fails interval certification even at eps=0.00577;
  coboundary-reopt-corrected.md §6 addendum). tawan's coefficients remain the only certified
  redistribution.
- CONJECTURED: whether any (l,c) beats tawan remains open (the LP family is not closed under
  two-large-gap configs).
- NOT YET: Lean formalization of this specific α/redistribution; second-machine audit.

## Reproduction

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
# → True 1096556
```
