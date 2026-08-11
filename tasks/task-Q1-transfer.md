# Task: Q1 — Does the Gram-stability refinement transfer to the ON-LINE and DISTINCT proportions?

## Role
RESEARCHER / PLANNER-adjacent. Analytical task with numerical support where possible. Read
`research/notes/discovery-gram-stability-673.md`, PLAN.md, hooks/agents.md first.

## Context (self-contained)
The Anthropic result has three constants:
- **Theorem A (on-line, zeros counted WITH multiplicity on Re=1/2):** liminf ≥ 2/3 ≈ 0.6667
- **Theorem D (simple zeros on the line):** liminf ≥ 3/2 − (1/√2)cot(1/√2) ≈ 0.672500703679
- **Theorem C (distinct zeros):** liminf ≥ 5/6 ≈ 0.8333

External groups pushed **Theorem D only** from 0.672500703679 to 0.6730–0.6732 via the
Gram-structure stability refinement: the rank–trace inequality's equality case assumes the
simple-zero atoms are mutually orthogonal, but the atoms' inner products are determined by zero
ordinate differences through the Montgomery–Taylor kernel k(x) = K(x)/K(0),
K(x) = ∫_{−1/2}^{1/2} cos(√2t)cos(2πxt)dt, so orthogonality is impossible; the extra positive term
tr Ψ(M), M = Gram matrix of simple-zero atoms, Ψ(t) = (t−1)² on [0,2], 2t−3 beyond, enters inside
the two-moment data and moves the constant.

**Q1 asks:** does the same stability term move Theorem A (2/3 → ?) and/or Theorem C (5/6 → ?)?

## Why this is nontrivial (and where the traps are)
The three theorems use different block structures of the compressed Weil form:
- Theorem D's simple-zeros count: the (1,1)-block Sylvester inertia argument separates simple
  on-line zeros from off-line pairs; the "atoms" whose orthogonality is assumed at equality are the
  simple-zero atoms.
- Theorem A counts zeros on the line WITH multiplicity — the atom/block structure is different
  (pairs {ρ, 1−ρ̄} and on-line zeros are handled differently; the equality case may involve
  different vectors).
- Theorem C (distinct) involves yet another count.

The transfer is NOT automatic: the positivity of tr Ψ(M) relies on the kernel not vanishing on
certain gap differences; whether a similar positive functional exists for the A/C block structures
is exactly the question. You do NOT have the full paper text on the phone — work from the structure
described here and from the constants, and be explicit about what you are assuming.

## Tasks
1. Reconstruct (from the description) the cleanest statement of each theorem's rank–trace equality
   case: which vectors are the "atoms", what orthogonality claim is made at equality, and what the
   kernel says about their inner products.
2. For Theorem A: identify the analogous Gram matrix (if any) and whether the same Ψ-stability
   argument applies. If it applies, what is the analogous ε (3-point / 7-point), and what constant
   does it imply? If it does NOT apply, identify the precise structural blocker (e.g. "the A-vectors
   are not pairwise-overlap-determined by gaps" vs "the A-count lacks the atom summand").
3. For Theorem C (distinct zeros, 5/6): same analysis.
4. Numerical support where possible (kernel computations are cheap in mpmath; e.g. verify any
   positivity claim you lean on).
5. Deliver a labeled verdict: PROVEN (sketch) / CONJECTURED (with the precise gap) / INCONCLUSIVE
   (blocker named) / ABANDONED (reason). A precise identification of the blocker is a result.

## Deliverables
- `research/notes/transfer-stability-online.md` — the analysis with labels.
- Any supporting script in `tools/` (e.g. `tools/online_kernel_check.py`) with cited command.
- Up top: one-line verdict.

## Compute budget
< 10 min wall; this is mostly analysis + small numerics.
