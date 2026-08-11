# Task: Q2 — Does the strengthened (Gram-constrained) inequality beat the in-class ceiling 0.6818?

## Role
RESEARCHER, LP/optimization + rank–trace structure. Read `research/notes/discovery-gram-stability-673.md`,
PLAN.md, hooks/agents.md first.

## Context (self-contained)
The main program proved an **in-class ceiling** for the bandwidth-one certificate class:
- The certificate reads (rank r, trace, Hilbert–Schmidt norm², n₊ = positive inertia) of the
  compressed Weil form, plus the bandwidth-one pair-correlation rows s_j = S(j)/N (Montgomery,
  unconditional).
- The LP dual shows the certified value is **v = p₁ + |E(1)|** where p₁ = certified simple-point
  fraction; the shadow price of p₁ is exactly 1.
- The in-class ceiling is **p₀ + |E(1)| = 0.68183123059534187426**, attained in-class by the
  near-CUE **256-law** (a distribution on zero configurations whose two-moment data match bandwidth
  one; simple fraction p₀ = 0.68182868746383147426). The ceiling was proven for the certificate
  class reading ONLY the quantities (rank, tr, HS², n₊) — i.e. the LP was free to pick any
  configuration consistent with those four numbers and the rows.

The external "stability refinement" adds a NEW constraint: the simple-zero atoms' inner products are
NOT free — they are determined by zero ordinate differences through the kernel
k(x) = K(x)/K(0), K(x) = ∫_{−1/2}^{1/2} cos(√2t)cos(2πxt)dt, and the refined inequality carries the
extra positive term tr Ψ(M) ≥ (stability bound) with Ψ(t) = (t−1)² on [0,2], 2t−3 beyond.

**Q2 asks:** does the strengthened inequality (equivalently: the extra Gram-structure constraint)
beat the in-class ceiling 0.6818 for simple zeros? Two sub-questions:
- Q2a: Does the 256-law's Gram structure satisfy the stability constraint, or does the ceiling law
  VIOLATE it (in which case the ceiling is not attained in the constrained class)?
- Q2b: With the Gram constraint enforced, what is the new in-class ceiling — does it move above
  0.6818?

## Approach hints
1. Write down what the Gram matrix M of simple-zero atoms looks like for a configuration with gap
   distribution g: M_{ij} = k(γ_i − γ_j) with the kernel evaluated at ordinate differences. For a
   "law" (ensemble), tr Ψ(M) is an ensemble expectation of a functional of consecutive gaps.
2. The 256-law is a distribution over zero configurations pinned by its pair-correlation rows.
   You do NOT have its exact gap law on the phone. Construct the best available surrogate with
   MATCHING two-moment content (e.g. a CUE-type gap model, or a determinantal-point-process
   approximation of the zeros) and compute tr Ψ(M) for it. LABEL the surrogate clearly — this part
   is CONJECTURED/empirical.
3. The clean LP question: does adding the constraint "tr Ψ(M) ≥ ε_stab > 0" to the dual change the
   optimum v* = p₁ + |E(1)|? Reason about the structure: the ceiling law (256-law) was chosen by the
   LP because it attains the worst case p₁ = p₀ with the rows pinned. If the 256-law's own Gram
   structure satisfies tr Ψ ≥ ε_stab, the constraint is slack and the ceiling stands. If the
   256-law violates it, the LP must find a worse-case law satisfying the constraint — which likely
   pushes p₁ DOWN (not up!), unless the constraint interacts with the rows. Analyze carefully which
   way it cuts. (A plausible resolution: the stability term helps Theorem D's CONSTANT within the
   method, but the in-class ceiling is a different object — the constrained class may have a LOWER
   achievable v, not higher. Determine the truth of this.)
4. Numerical experiments (cheap): for model gap laws (CUE, arithmetic-progression gaps, the
   "everything simple" world), compute tr Ψ(M) and compare with the stability bound 19/5000-scale
   number; see whether realistic laws sit above or below it.

## Deliverables
- `research/notes/ceiling-gram-constraint.md` — analysis with labels (which parts PROVEN, which
  CONJECTURED, which numerical).
- Supporting script `tools/ceiling_gram_check.py` with cited command.
- One-line verdict up top: e.g. "CEILING STANDS (constraint slack for all in-class laws)" or
  "CEILING MOVES to X" or "INCONCLUSIVE — blocker: ...".

## Compute budget
< 10 min wall. Prefer analysis; numerics vectorized.
