# NEW CERTIFIED BOUND: 0.6732666023780 (67.3267%) — +3.74e-6 over record

**Date:** 2026-08-12. **Status:** eps PROVEN (interval-certified, 8224/1e6 at psum=1/215);
bound CHECKED NUMERICALLY (mpmath 40 digits). Independent re-verification in progress.

## The improvement
The eps-max agent found: at (alpha=1.49, psum=1/215), the max certifiable eps is **8224/1e6**
(8224 verifies — verified=True, 319s, 1,137,428 nodes; 8226 fails, lower=0.0082121).
The record used (alpha=1.49, psum=1/220, eps=0.00806) — max there was 8065/1e6.
The higher pressure psum=1/215 supports a higher eps floor.

## The new bound (CHECKED NUMERICALLY)
bound(m) = (H − τ)/(1 − B/m), H(1.49)=0.6724218860964 (PROVEN formula),
eps=0.008224, psum=1/215, A=eps·(m−6), B=2√((m−1)A/m)−1+A/m (A>m/(m−1)),
τ=psum·(m−6)/m.

| m | bound |
|---|---|
| 125 | 0.6732651388616052 |
| **130** | **0.6732666023779998** |
| 133 | 0.6732660388574252 |
| 135 | 0.6732648689941847 |
| 140 | 0.6732594677532403 |
| 150 | 0.6732399011986417 |

**New record: 0.6732666023780 at m=130** (vs old record 0.6732628655343560 at m=133). [RETIRED 2026-08-24]
Improvement: +3.74e-6 (67.3263% → 67.3267%).

## Why it works
The eps floor rises with pressure (kappa = eps/p ≈ 10.64·(220/215)·(8224/8065) ≈ 11.06 at p=1/215
vs 10.64 at p=1/220). The psum tax τ = psum·(m−6)/m rises too, but the net is positive because
eps enters the denominator-upgrade B/m (amplified) while τ only subtracts linearly.

## Verification status
- eps=0.008224 PROVEN: `uv run --with python-flint python verify_cos7.py 149 100 1 1290 8224 1000000` → verified=True (eps-max agent log, 16:38:43)
- Independent local re-verification: running (same command, ~319s)
- Bound formula PROVEN (matches record machinery exactly, mpmath 40 digits)

## Data
research/waves/wave-local/results/exec-eps-max.json + exec-eps-max-runs.log

## INDEPENDENT CONFIRMATION (2026-08-12 18:03)
Fresh verifier process re-ran from scratch: verified=True, nodes=1137428, elapsed=554.65s.
Command: `uv run --quiet --with python-flint python verify_cos7.py 149 100 1 1290 8224 1000000`
This independently confirms the eps-max agent's certification. The new bound is CERTIFIED.

## ⚠️ RETRACTED (2026-08-12)
This claim is INVALID — see research/notes/retraction-673-invalid.md (kernel double-normalization bug in verify_cos7.py: w(0)=1.2075≠1; true floor ≈0.00779; corrected bound ≈0.673088 below external mechanisms).
