# A6-01 EXECUTION — D2 density passage via second-moment / Chebyshev at the operative span 9

**Date:** 2026-08-12 · **Executor:** EXECUTION agent (A6-01) · **Idea:** idea-factory-master §4 #10 (A6-01 / CI-41 / PC-01)
**Status:** IN PROGRESS (write-early; fill as computed)
**Context read:** context-pack.md, idea-factory-master.md (§4 #10, §8), epistemics-audit-2026-08-12.md (D2 / risk #6),
verify-gram-stability.md (PART D D2/D3), ladder-consecutive-zeros.md (§3.2/§4), span03-markov-execution.md,
span03_empirical_check.py (data conventions).

## 1. Question

The #1 honesty risk (epistemics audit, claim #6; verify D2): the per-block → liminf passage for
7-pt blocks is "INCONCLUSIVE/UNVERIFIED" because **at span 4**, E[Σ6 gaps] = 6/p ≈ 8.9 > 4 makes
first-moment Markov vacuous. SPAN-03 established the operative (model-II) span is **9**, where the
same first-moment Markov is non-vacuous but tiny: P(span ≤ 9) ≥ 1 − 6/(9·H0) = 0.008675.
A6-01 asks: does a **second-moment (Chebyshev/Cantelli) bound on the 7-span** deliver a
materially better lower bound on f = P(span ≤ 9), and what variance estimate would a proof need
(Selberg 2-level density)?

## 2. Setup and inequality forms (PROVEN, elementary)

X = 7-span = sum of 6 consecutive simple-zero gaps, in mean-spacing-1 units (corpus convention).
μ = E X, V = Var X. We want the upper tail P(X ≥ 9); S = 9, a = S − μ (requires a > 0, i.e. μ < 9).

- **Markov (first moment, X ≥ 0):** P(X ≥ 9) ≤ μ/9  ⟹  f ≥ 1 − μ/9.
- **Chebyshev (two-sided):** P(X − μ ≥ a) ≤ V/a²  ⟹  f ≥ 1 − V/a².
- **Cantelli (one-sided Chebyshev — sharp, strictly better):** P(X − μ ≥ a) ≤ V/(V + a²)
  ⟹  f ≥ 1 − V/(V + a²).  *(This is the correct "bound the tail" form: the task's
  P(span ≥ 9) = P(span − μ ≥ 9 − μ). No boundedness/positivity assumption beyond square-integrability.)*

All three are valid for ANY distribution with given (μ, V); Cantelli is the sharpest possible
one-tail bound from (μ, V). The question is entirely about which **inputs** are proven:
- μ ≤ 6/H0 = 8.9219… is PROVEN (rank–trace p ≥ H0 + telescoping identity).  [corpus]
- V is NOT proven anywhere; only measurable (or bounded by analytic machinery — Selberg layer).

**Constant map (7-pt plug-in; PROVEN digits from corpus):**
c(f) = (H0 − a₇·f·ε₇)/(1 − b₇·f·ε₇),  a₇ = 2680/5111, b₇ = 263/269, ε₇ = 19/5000 (per-7-block
total; per-atom = ε₇/7 — audit §2(a) normalization rule), dc/dε(7-pt) = b₇·H0 − a₇ ≈ 0.13314.
c(1) must reproduce **0.67300852792777976**; c(0) = H0. 3-pt reference
c₃ = (H0 − ε₃/4)/(1 − ε₃/2), ε₃ = 221/10⁶ → 0.6725197671136777.

## 3. Constants (CHECKED NUMERICALLY by tools/a601_secondmoment.py)

(TBD — fill after run)

## 4. Empirical second-moment table — zetazero(1..500), mean-spacing-1

(TBD — fill after run)

## 5. Bound tables — worst-case inputs vs empirical inputs

(TBD — fill after run)

## 6. Thinned surrogate — variance scale at the worst-case density (p = H0, p = 0.68)

(TBD — fill after run)

## 7. Per-atom ε and constant map under fraction f of good blocks

(TBD — fill after run)

## 8. What a proof would need (Selberg / 2-level density)

(TBD — fill after run)

## 9. Verdict

(TBD — fill last)

---
*Labels: every number below is code-backed (tools/a601_secondmoment.py, run via
`proot-distro login ubuntu -- python3`; cached zetazero(1..500)). Inequality forms: PROVEN
(elementary). Inputs: worst-case μ PROVEN; V empirical CHECKED NUMERICALLY (data-conditional);
thinning surrogate CONJECTURED (model). No existing notes were modified.*
