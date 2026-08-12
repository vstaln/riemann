# ADT-55 / ADT-56 — Bounded-differences (McDiarmid) concentration for the per-block → liminf passage

**Execution note — status: LIVE (being filled as computed)**
Date: 2026-08-12 · Executor: EXECUTION agent (idea-factory ADT-55/ADT-56, top-30 #14)
Scripts: `tools/adt55_concentration.py` (+ any variants) · All numbers code-backed via
`proot-distro login ubuntu -- python3 ...`.

## 0. Idea restated (from analogy-ideas.md #626/#636 + master §4 #14)

- **ADT-55**: the empirical mean of a *block functional* over 7-pt blocks concentrates around its
  law-mean with an *exponential* (McDiarmid) tail, provided the functional has bounded differences
  in each zero coordinate. This replaces the *vacuous* first-moment (Markov) per-block passage with
  a *quantitative* one — no span condition needed. Needs: (i) bounded-differences constant c
  (verifiable on data), (ii) law-mean pinned by data or theorem.
- **ADT-56**: quantify P(Σ6 gaps > 9) (the bad-block fraction) via empirical mean+variance and
  Markov/Chebyshev/Chernoff, so the ε-floor degrades by a *quantified* (not vacuous) factor.

## 1. Definitions (fixed here)

- Zero ordinates: `γ_1 < ... < γ_N`, `γ_n = Im(ζ zero n)`, normalized to mean gap 1:
  `g_n = γ_n / (mean gap over the corpus)`. (Corpus convention from SPAN-03.)
- **7-pt block b** = 7 consecutive normalized ordinates `(g_j, ..., g_{j+6})`.
  - sliding: windows `j = 0..N-7`,  B_s = N−6 blocks.
  - disjoint: `j = 0, 7, 14, ...`, B_d = ⌊N/7⌋ blocks.
- **f1(block) = 1{span ≤ 9}**, span = g_{j+6} − g_j  (good-block indicator; model-II S=9).
- **f2(block) = tr Ψ(block) = Σ_{1≤i<l≤7} k²(g_{j+l} − g_{j+i})**, the pair-energy functional
  (the certificate's ε-object), with k(x) = K(x)/K(0), K(x) = ∫_{−1/2}^{1/2} cos(√2 t) cos(2πxt) dt,
  K0 = √2 sin(1/√2) = 0.91872536986556843778.
- **Block average**: `F = (1/B) Σ_b f(block_b)`.

## 2. Task list

- [x] define F (above)
- [ ] build zero corpus (gammas500.npy absent; build + time)
- [ ] verify bounded-differences numerically (perturb one zero → ΔF ≤ c/B; report empirical c)
- [ ] McDiarmid tail + implied liminf lower bound on the block average
- [ ] compare vs SPAN-03 Markov (worst-case H0 vs empirical mean) and A6-01 Chebyshev
- [ ] ADT-56: bad-block fraction via empirical mean/σ + tail bounds
- [ ] state the lemma + data requirements
- [ ] final honesty labels + summary

## 3. Log

(computations appended below as run)

## 4. Interim remarks

- Worst-case Markov for the *span* is vacuous-looking because E[span] worst-case = 6/H0 = 8.92 is
  close to the threshold 9 — but that is a *worst-case over laws* bound. McDiarmid targets a
  different object (the block *average*, not the single-block probability); its dependence on the
  mean is additive, so concentration around a *data-pinned* mean is meaningful even if the
  worst-case mean is unhelpful. That is the honest content of ADT-55.
