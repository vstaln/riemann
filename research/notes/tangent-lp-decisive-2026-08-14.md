# Tangent-plane LP-verifier decisive run — psum=1/335, α=1.464, eps=0.005991 (2026-08-14)

**Status: COMPLETE. Verdict: LP INFEASIBLE at iter 0 — the tangent-plane in-class path is closed.**
*(Adjudicated 2026-08-14: the original script had a sign bug in `tangent_affine` (returned
negative gradients, certifying the reflected problem). Fixed, re-run: same verdict. The decisive
certificate is the corrected tangent LP AND the stronger exact-F point-cell LP — both infeasible.
See the ADJUDICATION section at the bottom and research/notes/review-fresh-notes-2026-08-14.md.)*

## Task
Run the tangent-plane LP-verifier loop (`tools/adv_lp_loop_v3.py`) and determine whether
any (l,c) with |c| ≤ 0.06 clears eps = 0.005991 at psum = 1/335, α = 1.464 — i.e. whether
the tangent lower bound can beat the record 0.6734808616745137.

Command (exact, pre-written):
```
cd /home/vstaln/riemann && uv run --quiet --with mpmath --with scipy --with numpy --with python-flint \
  python3 tools/adv_lp_loop_v3.py 335 0.005991 1.464 --max-iters 4
```

## Verdict

- **LP status: INFEASIBLE** (HiGHS reports infeasibility at iter 0, before any verifier run).
- **Verifier status: NOT RUN.** The interval branch-and-bound only runs if the LP is feasible;
  at iter 0 the LP was infeasible, so no verifier was invoked and no terminal cell was produced.
- **Exact eps value: 0.0059910** (the target; never certified — nothing was).
- **Terminal cell(s): none** (LP died before the first verifier run).

## Numbers cited with commands

Every number below is produced by the exact command above. Stdout, verbatim:

```
== adv LP loop v3 (tangent-plane): D=335, eps=0.005991, alpha=1.464 ==
  p0 = 0.000497512, q0 = 0.3333333333333333, |c| <= 0.06
  tables built in 0.6s + 1.4s (71902 cells)
  adverse boxes: 14652
  iter 0: LP INFEASIBLE (The problem is infeasible. (HiGHS Status 8: model_status is Infeasible)
  => no (l,c) with |c|<=0.06 makes tangent_lower >= 0.0059910 on the adverse set
```

- p0 = 1/(6·335) = 0.000497512 (printed by the tool, rounded to 9 digits).
- 71902 table cells; 14652 adverse boxes; LP solved at iter 0 → infeasible.
- Record-beating threshold eps ≥ 0.00599038 at α=1.464 is from the handoff
  (`handoff-psum-lc-frontier.md`, closed-form, CHECKED there); the target 0.005991 lies
  above it, so *feasibility* at 0.005991 was the pass/fail line.

## Claim labels

1. **The tangent-plane LP at psum=1/335, eps=0.005991, α=1.464, |c| ≤ 0.06 is infeasible**
   — **CHECKED NUMERICALLY.** Produced by HiGHS (scipy `linprog`, `method='highs'`) on
   14652 tangent-plane rows (the verifier's `tangent_lower`, affine in (l,c)) plus the
   κᵢ ≥ 0, qᵢ ≥ 0 soundness rows. *Caveat: the LP coefficients are rounded to IEEE double
   (the tool converts Arb values via `float()`), so this is solver-certified infeasibility,
   not an interval/rigorous certificate.*
2. **No (l,c) with |c| ≤ 0.06 makes `tangent_lower ≥ 0.005991` on the adverse set**
   — **CHECKED NUMERICALLY**, same command, same caveat (it is the restatement of #1).
3. **The tangent-plane path cannot beat record 0.6734808616745137 in-class**
   — **CONJECTURED** (inference from #1–2 plus the handoff's framing that tangent-LP was
   "the only remaining in-class path"). Upgrading #1 to an exact-rational or interval LP
   certificate would promote this toward PROVEN; the float-LP result is a strong but not
   rigorous negative.
4. **The 0.6818 in-class ceiling is structural** — **PROVEN** (already established in
   `structural-final-verdict.md`; not re-derived here).

## Interpretation

**What this closes.** The handoff's decisive filter was: *if the tangent-plane LP is feasible
at eps ≥ 0.0059904 (psum=1/335, α=1.464), the verifier should certify and produce a bound
≈ 0.673482+ — the only remaining in-class path to beat 0.673481.* The LP is infeasible at
eps = 0.005991 > 0.0059904, at iter 0, on the full 14652-box adverse set. So the filter says
**no (l,c) with |c| ≤ 0.06 clears the tangent bound at the required eps**, and the verifier
was never invoked.

This matches and extends the handoff's diagnosis: interval-only LP was infeasible (v2) while
tawan certifies 0.00596 via the convex tangent prune; v3 added the tangent prune itself as
LP rows and it is *still* infeasible at 0.005991. The tangent bound is the strongest available
per-box lower bound in the verifier, so adding it as constraints is the most permissive
consistent LP filter — and it still fails. The (l,c) re-optimization slot that the handoff
left open is therefore **closed**: no coefficient perturbation within the |c| ≤ 0.06 box
reaches the record-beating eps at psum=1/335.

**What this opens.** Nothing new in-class — and that is the finding. It confirms the
`structural-final-verdict.md` conclusion with one more independent angle: the coboundary
certificate family is exhausted, and the gap 0.673481 → 0.6818 is **not** closable by
coefficient/plane optimization. The record 0.6734808616745137 stands as the certified
frontier of the class. Beating it, and a fortiori reaching the 0.6818 ceiling, requires a
genuinely new unconditional input (a simple-fraction theorem with p₁ > 0.6818, or a new
kernel/redistribution family outside the coboundary class) — a theorem-level move, not an
optimization move.

## Follow-up recommendation (one lever)

**Pivot the record-pushing thread to the structural lever: seek a new unconditional input
(theorem) on the simple-zero fraction p₁, not a better certificate optimization.** Per
`structural-final-verdict.md`, the unconditional simple-fraction best (~0.405, BHTY) is far
below the p₀ = 0.6818 that the ceiling requires, and the 256-law's 0.68183 is in-class
optimal. The one lever with any remaining upside is a new analytic theorem on zero
multiplicity / simple-fraction — e.g. an explicit-formula bound on Σ(m_ρ − 1), or a
Montgomery-pair-correlation strengthening that carries multiplicity information.

*Secondary (rigor) note, not a lever: the float-LP infeasibility could be upgraded to a
rigorous certificate (exact-rational or interval LP) to move claim #3 from CONJECTURED
toward PROVEN. This is verification polish on an already-decisive negative, not a new
search direction.*

---

## ADJUDICATION (2026-08-14, after adversarial review)

**Reviewer finding (review-fresh-notes-2026-08-14.md): the original script's LP certified a
reflected sibling.** `tangent_affine` returned A, C equal to the NEGATIVES of the true (l,c)
gradients (dF/dl_k = -A_script[k], dF/dc_k = -C_script[k], checked numerically at the terminal
cell). Combined with the κ/q rows (not symmetric under (l,c)->(-l,-c)), the LP enforced
`tangent(-l,-c) >= target`, not `tangent(l,c) >= target`.

**Fix (applied to tools/adv_lp_loop_v3.py):** `A = u_{k+1} - u_k`, `C = v_{k+1} - v_k` (true
gradients, matching the `tangent = const + A.l + C.c` docstring). Re-run, verbatim:

```
== adv LP loop v3 (tangent-plane): D=335, eps=0.005991, alpha=1.464 ==
  p0 = 0.000497512, q0 = 0.3333333333333333, |c| <= 0.06
  tables built in 0.6s + 1.4s (71902 cells)
  adverse boxes: 14652
  iter 0: LP INFEASIBLE (The problem is infeasible. (HiGHS Status 8: model_status is Infeasible)
```
Same verdict with the correct certificate. Independent corrected-tangent LP (tools/lp_fix/corrected_lp.py):
`CORRECTED LP (const + A.l + C.c >= eps): False (infeasible)`, 3499 PD rows.

**The stronger, definitive certificate (tools/lp_fix/final_decisive.py, exact-F at point cells —
no tangent, no radius, no PD filter):**
```
EXACT-F LP, pressure-relevant point cells only (3640): False (infeasible)
EXACT-F LP, ALL point cells (3663):                   False (infeasible)
min F(base) over pressure-relevant cells = 0.00561239   (gap to target 0.005991 = 3.786e-4)
```
Since `tangent_lower <= F(midpoint)` on every box (the radius correction is nonnegative),
infeasibility of the exact-F LP at point cells implies infeasibility of the tangent LP on any
superset. The exact-F LP imposes NO PD condition, so the PD-at-base exclusion is not a hole.

**Narrative correction:** the note originally called the tangent LP "the strongest/most
permissive filter". Inverted — `tangent_lower` is the WEAKEST per-box lower bound
(`tangent_lower <= F(midpoint) <= box minimum`), so a weaker bound makes `lower >= target`
HARDER and the filter LESS permissive; the exact-F LP is the strongest certificate. Corrected
here; the conclusion is unchanged and now better certified.

**Claim-label audit (per review):** #1/#2 (LP infeasible / no (l,c) clears the tangent bound)
remain CHECKED NUMERICALLY but are now certified by the corrected scripts above (not the
pre-fix script). #3 (in-class path closed) stays CONJECTURED, now backed by the correct
certificate. #4 (0.6818 structural ceiling) unchanged, PROVEN elsewhere.
