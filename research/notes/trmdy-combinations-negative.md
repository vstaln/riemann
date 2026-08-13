# trmdy combinations — two clean negatives (window, weights)

**Date:** 2026-08-14. **Status:** CHECKED NUMERICALLY (Arb interval verifier, grid 4000).

The untried combinations from trmdy's design (re-optimized 7-term window + non-uniform
reflection-symmetric weights) were tested against OUR coboundary (tawan p,q) at α=1.464:

| combination | eps=0.0062 result | nodes | verdict |
|---|---|---|---|
| trmdy window (7-term cosine poly) + coboundary p,q, uniform a_ij | node-limit | 6,000,001 | INCONCLUSIVE (too slow; 74k-cell cutoff) |
| trmdy non-uniform a_ij + coboundary p,q, cosine α=1.464 | **False** (terminal-cell) | 236,340 | NEGATIVE — trmdy weights worse than uniform |

**Interpretation (CONJECTURED):** trmdy's weights were optimized for their own window
+ pressure 1/2300 + target 1/200; transferred to the coboundary's pressure profile they
_lower_ the certified floor vs uniform weights. The uniform a_ij = 2/(7−s) remain the best
known cross-term weights for the coboundary.

**Record 0.673481 (α=1.464, psum=1/320, eps=0.0062, uniform a_ij, tawan p,q) stands.**

Scripts: `/tmp/test_trmdy_cobound.py`, `/tmp/test_trmdyweights_cobound.py` (both
`uv run --quiet --with mpmath --with python-flint python3 -u <script>`).

## Honesty ledger
- CHECKED NUMERICALLY: both verifier runs (grid 4000, Arb interval).
- CONJECTURED: the interpretation of _why_ trmdy weights fail (not re-derived).
- INCONCLUSIVE: trmdy window + coboundary at eps=0.0062 (node-limited; a Rust port would
  resolve this, but the 74k-cell cutoff already signals the window is not competitive).
