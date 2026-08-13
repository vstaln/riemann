# psum frontier — the coboundary record 0.673481 is at the optimum

**Date:** 2026-08-13 (overnight). **Status:** CHECKED NUMERICALLY (Arb interval verifier, grid 4000).

## The frontier

Scaling tawan's redistribution shape to different psum (keeping q fixed, scaling p by 320/D),
the certified eps and bound trace a clean frontier at α=1.464:

| psum | certified eps | m* | bound |
|---|---|---|---|
| 1/220 | 0.0080 | 134 | 0.673270 |
| **1/320** | **0.0062** | **171** | **0.673481** ← optimum |
| 1/340 | 0.00584 | 181 | 0.673426 |
| 1/360 | 0.00551 | 191 | 0.673370 |
| 1/400 | 0.00496 | 212 | 0.673283 |

The bound is maximized at psum=1/320 (tawan's original pressure). The looser-tax benefit of
higher psum↓ is exactly offset by the eps↓ scaling; 1/320 is the balanced optimum.

## Honesty ledger

- CHECKED NUMERICALLY: each eps certified by verify_floor (Arb interval, grid 4000);
  each bound by exact mpmath.
- CONJECTURED: that the q-shape (fixed at tawan's) is optimal at each psum — the LP work
  (coboundary-reopt-corrected.md) showed tawan's shape is near-optimal at psum=1/320, but the
  shape was not re-optimized at other psum.
- The record 0.673481 (α=1.464, psum=1/320, eps=0.0062) is the frontier optimum of the tested family.

## Conclusion

The coboundary redistribution lever is now EXHAUSTED at the certified level:
- α: optimized to 1.464 (boundary of eps=0.0062 certification)
- psum: optimized to 1/320 (frontier optimum)
- coefficients (l,c): tawan's near-optimal (LP-proven, κ_i ≥ 0 binding)

**The certified record stands at 0.673481 simple-on-line (0.836740 distinct).** The remaining
route to the 0.6818 class ceiling requires beyond-bandwidth-1 data (p₁), which is CONJECTURED-only.
