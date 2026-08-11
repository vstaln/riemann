# Task: Q4 — Adversarial validation of the external stability-refinement constants

## Role
VALIDATOR (adversarial). Your job is to try to BREAK the claimed external results, not to confirm
them. Read the discovery note first:
`research/notes/discovery-gram-stability-673.md` (also PLAN.md and hooks/agents.md).

## Context (self-contained)
Anthropic's Theorem D proves liminf of the simple-zeros-on-line proportion
≥ 3/2 − (1/√2)·cot(1/√2) = **H0 = 0.67250070367941164573**. Three external repos claim better
constants for SIMPLE zeros via a "Gram-structure stability refinement" of the rank–trace inequality:

- ainta: **0.673008527927** (67.3008528%) via 3-point ε₄ ≥ 221/10⁶ → 67.2519767% and 7-point
  six-variable bound ≥ 19/5000 → 67.3008528%
- trmdy: **0.673137630699** (67.3137630699%)
- tawanerguo-cn: **0.673192911473** (67.3192911473%)

Mechanism: the rank–trace step's equality case assumes simple-zero atoms are mutually orthogonal,
but atom inner products are DETERMINED by zero-ordinate differences through the kernel
k(x) = K(x)/K(0), K(x) = ∫_{−1/2}^{1/2} cos(√2 t) cos(2π x t) dt, so orthogonality is impossible.
The refined inequality: ‖P+Q‖²_F ≥ 4tr(P+Q) − 3r − 4b + tr Ψ(M), with Ψ(t) = (t−1)² on [0,2],
2t−3 beyond, M = V*V the Gram matrix. The extra tr Ψ(M) > 0 is provably positive because "the
kernel cannot vanish at all three pairwise differences of any 3 consecutive gaps (u, v, u+v ≤ 4)".

The repos are NOT cloned on the phone. Do not try to fetch them. Verify the mathematics directly.

## Tasks (all code-backed, mpmath via `proot-distro login ubuntu -- python3`)

1. **Constant algebra.** Verify at 50 dps: H0; three_point_bound(ε) = (H0 − ε/4)/(1 − ε/2) at
   ε = 221/10⁶ (should give 0.672519767...); seven_point_bound = (1345000·H0 − 2680)/1340003
   (should give 0.673008527927...). ALSO: reverse-engineer WHY these formulas — e.g. from
   (H0 − ε/4)/(1 − ε/2), what ε means in the rank–trace argument; check the algebra of the
   seven-point formula is consistent with a claimed derivation (inflation of H0 by the stability
   term and a new denominator). Report the exact digits you get.
2. **Kernel mechanism (the core novelty).** Compute k(x) on [0,4] (mpmath quad, or closed-form via
   sinc: k(x) = [sinc((√2−2πx)/2) + sinc((√2+2πx)/2)]/2 / k(0), k(0) = √2·sin(1/√2)).
   a. Find the zero set of k on [0,4] to ~1e-12. How many zeros? Where?
   b. Adversarial target: does any (u,v) with u,v ≥ 0, u+v ≤ 4 satisfy k(u) = k(v) = k(u+v) = 0
      (within tolerance)? Do a dense grid search (e.g. 2e5 points, vectorized numpy) and report the
      minimum of Σ|k| (or max|k|) found; then refine with scipy local optimization.
   c. The certified claim is ε₄ ≥ 221/10⁶ where ε₄ is a functional of the three values
      (plausibly min of something like Σk² or the pressure functional). Estimate numerically the
      TRUE minimum of the natural functionals (k(u)²+k(v)²+k(u+v)²) over the domain — is it
      consistent with ≥ 221/10⁶? Is 221/10⁶ loose or tight? (Loose = mechanism works but bound
      improvable; tight = impressive but fragile.)
   d. Same for the 7-point variant: the six-gap weighted pressure (coefficients c_s = 2/(7−s),
      s = number of gaps crossed) — estimate min over 6 gaps (u₁..u₆ ≥ 0, Σu ≤ 4?) of the
      functional, compare with 19/5000 = 0.0038. Vectorized estimation only; do not certify.
3. **Flaw hunt (the real job).** Write down the cleanest reconstruction of the stability argument
   you can from the above pieces, then attack it: where could the o(N) uniformity, the window
   bounds, the block averaging, or the passage from finite blocks to the liminf hide an error?
   State your best candidate flaws (if any) and which ones you can rule in/out numerically.

## Deliverables
- `research/notes/verify-gram-stability.md` — labels on every claim (CHECKED NUMERICALLY with exact
  script+command, CONJECTURED, INCONCLUSIVE, or ABANDONED).
- `tools/verify_gram_stability.py` — self-contained; prints verdicts; runs in < 5 min.
- Verdict line up top: e.g. "CONSTANTS OK / KERNEL MECHANISM HOLDS / NO FLAW FOUND" or the precise
  break you found. Honesty guardrails apply: a failed attack is a result; never inflate.

## Compute budget
< 10 min wall. Vectorize. If something would take longer, do a smaller sample and document the full
command for the laptop to run later.
