# DISCOVERY — External extensions of Theorem D beat 0.6725 via Gram-structure stability

**Date:** 2026-08-11 (round 2.5). **Status:** VERIFIED-EXTERNALLY (main program reran their
verifiers: ainta 7/7 pass, trmdy 13/13 pass; both Arb/python-flint interval-certified), NOT yet
independently adjudicated in depth. Source repos: ainta-zeta-simple-zeros,
trmdy-zeta-simple-zeros-673137, tawanerguo-cn/zeta-simple-zeros (not yet cloned).

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

## The mechanism — THE KEY INSIGHT

The rank–trace inequality's equality case requires the simple-zero atoms to be **mutually
orthogonal**. But for the optimized window, the atom inner products are **determined by zero
ordinate differences** through the kernel k(x) = K(x)/K(0), K(x) = ∫_{−1/2}^{1/2} cos(√2t)cos(2πxt)dt
— so orthogonality is *impossible*. The stability refinement keeps this structure:

**‖P+Q‖²_F ≥ 4tr(P+Q) − 3r − 4b + tr Ψ(M)** (ainta eq. 2.1), Ψ(t) = (t−1)² on [0,2], 2t−3 beyond,
M = V*V the Gram matrix of simple-zero atoms.

The extra **tr Ψ(M) > 0** term is:
- **inside the two-moment data** (a function of the Gram matrix the certificate already builds);
- **provably positive** because the kernel cannot vanish at all three pairwise differences of any 3
  consecutive gaps (u, v, u+v ≤ 4);
- quantified: 3-point gives ε₄ ≥ 221/10⁶ → 67.2519767%; 7-point six-variable bound ≥ 19/5000 →
  67.3008528%.

## Standing adjudication questions (the live frontier)

- Q1: Does the stability refinement transfer to the ON-LINE proportion (Theorem A, 2/3 → ?) and the
  DISTINCT proportion (Theorem C, 5/6 → ?)? (The external repos target simple zeros only.)
  **Q1 STATUS (2026-08-12, phone):** analysis in `research/notes/transfer-stability-online.md`.
  Method-level transfer verified numerically (ε_C = ε_D = 4.45e-4; ε_A ≥ ε_D — same kernel, gap
  domain; multiplicity scaling only increases tr Ψ). Constant-level: C = CONJECTURED (needs C's
  chain algebra); A = INCONCLUSIVE (blockers: A's equality case needs equal multiplicities +
  orthogonality; "2/3 is arithmetic" finding suggests data-saturation; equality case may involve
  different vectors). Script: `tools/online_kernel_check.py`.
- Q2: Does the strengthened inequality beat the in-class ceiling 0.6818 for simple zeros? (The
  ceiling was proven for the certificate class reading only rank, tr, HS², n₊; the stability term
  tr Ψ(M) adds a constraint the ceiling law may violate. Adjudicate: does the 256-law's Gram
  structure satisfy tr Ψ ≥ the stability bound, or does the strengthened inequality push the class
  ceiling up?)
- Q3: How far does the consecutive-zeros ladder go? (3 → 7 → 9 → 11 points; is there a limit?)
- Q4: Adversarial check — is there a flaw in the stability-refinement deduction (the o(N)
  uniformity, the window-bounds certification, the block-averaging step, the constant algebra)?

## Known constants (for cross-checking)

- H0 = 3/2 − (1/√2)·cot(1/√2) = 0.67250070367941164573 (Theorem D)
- three-point bound: (H0 − ε/4)/(1 − ε/2) with ε = 221/10⁶ → 0.672519767... (67.2519767%)
- seven-point bound: (1345000·H0 − 2680)/1340003 → 0.673008527927... (67.3008528%)
- in-class ceiling p₀ + |E(1)| = 0.68183123059534187426; p₀ = 0.68182868746383147426 (256-law)
- 2/3 = 0.66666666666666666667 (Theorem A); 5/6 distinct (Theorem C)
