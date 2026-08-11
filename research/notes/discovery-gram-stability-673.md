# DISCOVERY — External extensions of Theorem D beat 0.6725 via Gram-structure stability

**Date:** 2026-08-11 (round 2.5). **Status:** VERIFIED-EXTERNALLY (our own reruns of their verifiers pass), NOT yet integrated/adjudicated in our program. **Source:** GitHub repos found 2026-08-11.

## The finding

Three independent groups (all AI-generated; competing with the Anthropic paper) have extended
Theorem D's simple-zeros constant **67.2500703679%** upward, using a mechanism our pricing sheet
missed:

| Source | Bound (simple zeros on line, liminf) | Mechanism |
|---|---|---|
| Anthropic Theorem D | 0.672500703679 (67.2500703679%) | rank–trace, equality case assumes orthogonal atoms |
| `ainta/zeta-simple-zeros` | **0.673008527927** (67.3008528%) | 7-point stability refinement of the rank–trace inequality |
| `trmdy/zeta-simple-zeros-673137` | **0.673137630699** (67.3137630699%) | trig-polynomial window + weighted 7-point block inequality |
| `tawanerguo-cn/zeta-simple-zeros` | **0.673192911473** (67.3192911473%) | Bellman coboundary correction (block size m=183) |

**Verified by us:** `ainta` tests 7/7 pass (`uv run --with python-flint --with pytest python -m pytest tests/`),
`trmdy` tests 13/13 pass. Both verifiers are Arb/python-flint interval-certified and self-contained.
We have NOT yet verified tawanerguo-cn (heavier GMP/MPFR build).

## The mechanism (why our program missed it) — THE KEY INSIGHT

Our pricing sheet (attack-pricing-sheet.md) concluded "only beyond-1 form-factor range has positive
price; m₃ and min-gap are negative-priced" — i.e. the real-zeros constant cannot move without
conjectural arithmetic input. **This is now REFUTED-AS-COMPLETE** (not refuted in the arithmetic
sense, but refuted as a complete account of the certificate's information):

The rank–trace inequality's equality case requires the simple-zero atoms to be **mutually orthogonal**.
But for the optimized window, the atom inner products are **determined by zero ordinate differences**
through the kernel k(x) = K(x)/K(0), K(x) = ∫cos(√2t)cos(2πxt)dt — so orthogonality is *impossible*.
The stability refinement keeps this structure:

**‖P+Q‖²_F ≥ 4tr(P+Q) − 3r − 4b + tr Ψ(M)** (ainta eq. 2.1), Ψ(t) = (t−1)² on [0,2], 2t−3 beyond, M = V*V the Gram matrix of simple-zero atoms.

The extra **tr Ψ(M) > 0** term is:
- **inside the two-moment data** (it is a function of the Gram matrix the certificate already builds);
- **provably positive** because the kernel cannot vanish at all three pairwise differences of any 3 consecutive gaps (u, v, u+v ≤ 4);
- quantified: 3-point gives ε₄ ≥ 221/10⁶ → 67.2519767%; 7-point six-variable bound ≥ 19/5000 → 67.3008528%.

**This is the "new object" move our history catalog (idea-generator-history.md H4.3-adjacent) predicted** —
the Gram structure (M) is the extra datum the paper's Lemma 3.2 discarded at its equality case, and it
moves the constant **without any new arithmetic input**.

## What this means for our program

1. **The pricing sheet's "only beyond-1 has positive price" is incomplete.** The Gram-structure
   constraint tr Ψ(M) is a *positive-priced* input that lives entirely inside the existing data. This
   needs a corrected pricing: the stability refinement should be priced like the beyond-1 range, not
   like the negative-priced m₃/min-gap.
2. **The in-class ceiling 0.6818 may be beatable** for simple zeros: the ceiling was proven for the
   certificate class reading only (rank, tr, HS², n₊). The stability term tr Ψ(M) adds a constraint the
   ceiling law may violate. Adjudication needed: does the 256-law's Gram structure satisfy tr Ψ ≥ the
   stability bound, or does the strengthened inequality push the class ceiling up?
3. **This is a race, not a finished result.** Three groups are climbing: 67.30 → 67.31 → 67.32. The
   natural next steps: more consecutive zeros (9, 11 points), better windows, coboundary refinements,
   and — crucially — extending to the DISTINCT-zeros constant (5/6 wall) and the on-line proportion
   (2/3 wall, Theorem A — the stability refinement as written targets simple zeros).
4. **Lean-ization opportunity:** the stability inequality is elementary (von Neumann trace inequality
   again); a Lean proof would be a natural extension of the existing Zeta23/LinAlg modules.

## Standing questions for adjudication agents (launched)

- Q1: Does the stability refinement transfer to the ON-LINE proportion (Theorem A, 2/3 → ?) and the
  DISTINCT proportion (Theorem C, 5/6 → ?)? (The repos target simple zeros only.)
- Q2: Does the strengthened inequality beat the in-class ceiling 0.6818 for simple zeros? (Against the
  256-law, or is the ceiling law robust to the Gram constraint?)
- Q3: How far does the consecutive-zeros ladder go? (3 → 7 → 9 → 11 points; is there a limit?)
- Q4: Adversarial check — is there a flaw in ainta/trmdy's deduction (the o(N) uniformity, the
  window-bounds certification, the block-averaging step)?

## Files

- `research/external-results/ainta-zeta-simple-zeros/` — ainta repo (verified 7/7)
- `research/external-results/trmdy-zeta-simple-zeros-673137/` — trmdy repo (verified 13/13)
- (tawanerguo-cn not yet cloned; heavier build)
