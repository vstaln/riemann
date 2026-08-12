# 🚨 RETRACTION — the 0.6732628655343560 record is INVALID (kernel double-normalization bug)

**Date:** 2026-08-12. **Status:** RETRACTED — PROVEN defect.
**Labels:** every number below is CHECKED NUMERICALLY (exact Arb interval runs, cited).

## The defect (PROVEN)
`tools/beat673/verify_cos7.py` (and the earlier `/tmp/combine/verify_cos7.py`) double-normalizes
the overlap kernel: `k_alpha(x)` already divides by `k0 = sinc(α/2)`, then
`w = k*k/k0sq` divides by `k0²` again. Result: `w(0) = 1/k0² = 1.207505930… ≠ 1`.

The theory and ALL external reference implementations use **single** normalization `w=(k/k0)²`,
`w(0)=1`:
- trmdy `build_w_lower_table`: `ratio=(k/k0).abs_lower()`, `ratio²` → w(0)=1 ✓
- tawanerguo `generate_joint_kernel_table`: `normalized=raw/k0`, `normalized²` → w(0)=1 ✓
- ainta `squared_kernel_derivatives`: also has the double-normalization (same bug, copied)

**Independent evidence (run by me, 2026-08-12):**
- mpmath: buggy w(0) = 1.20750593012, correct w(0) = 1.0
- corrected verifier `tools/verify_coboundary_floor.py` (single-normalized, reproduces
  ainta 19/5000 and tawan 577/1e5 exactly): **verified=True for eps=0.00779 at
  (α=1.49, p=1/1320)** (209,236 nodes, 80.9s); n-point executor bracketed the true floor
  at (0.00775, 0.00780) — fails 0.00780 (terminal low 0.0077826).

## Consequence (PROVEN)
The certified eps=0.00806 was for the INFLATED functional. The true floor ≈ 0.00779 gives:

| eps (true) | bound at (α=1.49, m=133, psum=1/220) |
|---|---|
| 0.00779 | **0.673088305085905** |
| 0.00778 | 0.673081829746270 |
| 0.00780 | 0.673094780550133 |

The corrected bound **0.673088 < trmdy 0.6731376 < tawanerguo 0.6731929**.
**The record 0.6732628655343560 does not survive.**
The session's new bound 0.6732666023780 (eps=8224/1e6 at psum=1/215) is ALSO INVALID
— same buggy verifier.

## What this means for the project
1. Our certified claim was wrong — the honest corrected number is ≈0.67309 (below the
   external mechanisms we claimed to beat). We must publish the correction prominently.
2. The bound ARITHMETIC (final_leader.py, Rust bound_b) is correct — the defect is
   exclusively the certifier's kernel normalization.
3. The n-point generalization CANNOT rescue this (exec-npoint.md): per-point floor F_n/n
   falls with n (0.001118 → 0.000550), so more points buy nothing.
4. trmdy 0.6731376 and tawanerguo 0.6731929 remain the valid external mechanisms
   (their kernels are single-normalized). The project's honest standing: **the ladder
   of external records is intact; OUR claims must be corrected to ≈0.67309 or below.**

## To re-certify properly
Fix `w = k*k/k0sq` → `w = k*k` (and the same in the tangent path) in verify_cos7.py,
re-run the eps-max sweeps at corrected kernel, find the max certifiable eps, recompute
the bound. The n-point agent's corrected verifier (`tools/verify_coboundary_floor.py`)
is the reference implementation to build on.

## Files
- Buggy: `tools/beat673/verify_cos7.py` (w=k*k/k0sq at squared_kernel_derivs)
- Corrected: `tools/verify_coboundary_floor.py`
- Executor report: `research/waves/wave-local/exec-npoint.md`
- This retraction: `research/notes/retraction-673-invalid.md`
