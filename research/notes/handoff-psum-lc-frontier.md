# 🔄 HANDOFF — psum/l/c joint frontier (2026-08-13)

**State: passed to next agent. Everything below is CHECKED, committed (5ad8ddb), pushed.**

## What was tried this session (all closed or diagnosed)

### 1. Joint (psum, l, c) re-optimization — the one CONJECTURED-open slot
Frontier note (`psum-frontier-673481.md`) flagged: q-shape was only scaled across psum,
never re-optimized. This session probed it fully:

- **Bound math (closed-form, CHECKED)**: at psum=1/335, beating record 0.6734808616745137
  needs **eps ≥ 0.00599038** at α=1.464 (H=0.6724674), or **eps ≥ 0.00593879** at α=√2
  (H=0.6725007). At psum=1/340 needs eps ≥ 0.00592462 (α=1.464).
- **tawan-scaled certification (CHECKED, interval verifier)**: 1/335 certifies eps=0.00596
  (1,052,044 nodes) but FAILS 0.00597 (terminal cell (4220,8007,8027,8027,7995,4220)/4000,
  low=0.0059584). 1/330 fails 0.00605 (needs 0.006058). **Deficit ~3e-5 eps everywhere.**
- **α-play closes nothing**: H(α) needs α ≤ ~1.432 for H ≥ 0.67249, but certification fails
  at α ≤ 1.45 for the needed eps. Only (l,c) re-optimization at α=1.464 could close the gap.
- **Symmetric and antisymmetric (l,c) perturbations** of tawan's shape both FAIL to certify
  0.005991 at 1/335 — the two binding cell families conflict (one wants dl₁>0, the other
  dl₁<0; coefficients ±0.95 per 1e-5).

### 2. Adversarial LP-verifier loop (`tools/adv_lp_loop.py`)
- **v1 (point-eval LP)**: LP max-min over ~5,481 sampled configs gave optimistic 0.00624,
  but verifier rejected at 0.0060 (LP family not closed — missed near-uniform and
  large-gap-4th-coordinate configs). Iterating with terminal cells did not converge.
- **v2 (interval-exact LP)**: replicates verifier `box_lower` at point cells exactly
  (p_i·g_i/grid, q_i·w_lower_on_cell, pair terms via RangeMinimum over spans).
  **KEY DIAGNOSIS**: interval-exact LP at psum=1/335, eps=0.005991 is INFEASIBLE with
  |c| ≤ 0.06, yet the interval-min is only **0.005757** — far below tawan's *certified*
  0.00596. Why: **the verifier's convex tangent prune lifts cells above naive interval
  bounds**. tawan's certification depends on convexity certification (exact LDL in arb,
  `tangent_lower` in verify_coboundary_floor.py line 336).

## The structural takeaway (for the next agent)

**LP feasibility with interval-only bounds is NOT the right filter.** The tangent plane
bound `tangent_lower` is **affine in (l,c)** (F is affine in (l,c); tangent uses fixed
kernel derivatives + midpoint/radius of the box). The natural next step:

> Add **tangent-plane constraints** (one per adverse box) to the LP: for each box in the
> adverse set, require `tangent_lower(box) ≥ target`, where tangent_lower is linear in
> (l,c) with coefficients from `squared_kernel_derivatives` at the box midpoint and
> second-derivative table minima. Also require the Hessian be PD (LDL-certified) —
> that's a nonlinear constraint, so either check it a-posteriori or restrict to a
> sub-class where convexity is automatic.

If that LP is feasible at eps ≥ 0.0059904 (psum=1/335, α=1.464), the verifier run
should certify and produce bound ≈ 0.673482+ > record. **That is the only remaining
in-class path to beat 0.673481 without new theorem structure.**

## Fallback directions (cheaper, already partially known)
- V2: block size k≠6 certificate redesign (re-enters certificate design).
- V3: joint psum-lattice — essentially what was probed; closed unless tangent-LP works.
- Truly new unconditional moment structure beyond m₃ (m₃ is PROVEN dead unconditionally)
  is the theorem-level need for the 0.6818 ceiling.

## Reproduce
```
uv run --quiet --with mpmath --with scipy --with numpy --with python-flint \
  python3 tools/adv_lp_loop.py 335 0.005991 1.464 10
```
(expect: v2 LP infeasible at iter 0; that IS the finding, see commit message.)
