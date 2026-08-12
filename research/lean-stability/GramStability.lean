/-
Copyright (c) 2026 Riemann program.
Released under Apache 2.0 license as described in the file LICENSE.

# Gram-stability refinement: `‖P+Q‖² ≥ 4·tr(P+Q) − 3r − 4b + tr Ψ(M)`

Formalization effort for ainta `zeta-simple-zeros` eq. (2.1) — the
stability-enhanced rank-inertia inequality that drives 0.6725 → 0.67300...

This is a SKELETON: the statement shapes, hypotheses, and the proof
decomposition are pinned; hard analytic/spectral inputs are named axioms
in the clearly-marked block at the bottom. Design note:
`research/notes/lean-stability-inequality.md`.

Reuses the existing `RHLinalg` development in `research/lean-zeta-23`:
`frobSq`, `rtrace`, `posIndex`, `specMap`, `hermPosPart`, `vonNeumann_trace_ineq`.
-/

import Zeta23.LinAlg.HermitianPosPart
import Zeta23.LinAlg.VonNeumann
import Zeta23.LinAlg.RankTrace
import Zeta23.LinAlg.PosIndex

noncomputable section

open Matrix Finset
open scoped ComplexOrder

namespace GramStability

set_option linter.unusedVariables false

/-! ## Ψ and the main statement -/

/-- Ψ(t) = (t−1)² if t ≤ 2, else 2t−3. Continuous at 2. -/
def psi (t : ℝ) : ℝ := if t ≤ 2 then (t - 1) ^ 2 else 2 * t - 3

/-- Spectral sum Σᵢ f(λᵢ) of a Hermitian matrix (rtrace_specMap hA f). -/
def spectralSum {n : Type*} [Fintype n] [DecidableEq n] {𝕜 : Type*} [RCLike 𝕜]
    (f : ℝ → ℝ) {A : Matrix n n 𝕜} (hA : A.IsHermitian) : ℝ :=
  ∑ i, f (hA.eigenvalues i)

lemma spectralSum_eq_rtrace_specMap {n : Type*} [Fintype n] [DecidableEq n]
    {𝕜 : Type*} [RCLike 𝕜] {f : ℝ → ℝ} {A : Matrix n n 𝕜} (hA : A.IsHermitian) :
    spectralSum f hA = RHLinalg.rtrace (RHLinalg.specMap hA f) := by
  rw [RHLinalg.rtrace_specMap]
  rfl

structure StabilityData (n : Type*) [Fintype n] [DecidableEq n]
    (r : Type*) [Fintype r]
    (𝕜 : Type*) [RCLike 𝕜] where
  V : Matrix n r 𝕜
  col_norm_le_one : ∀ j : r, ‖fun i : n => V i j‖ ≤ 1
  Q : Matrix n n 𝕜
  Q_hermitian : Q.IsHermitian
  pos_eig_count_le_b : RHLinalg.posIndex Q_hermitian ≤ Fintype.card r

def P {n : Type*} [Fintype n] [DecidableEq n] {r : Type*} [Fintype r] [DecidableEq r]
    {𝕜 : Type*} [RCLike 𝕜] (d : StabilityData n r 𝕜) : Matrix n n 𝕜 := d.V * d.Vᴴ
def M {n : Type*} [Fintype n] [DecidableEq n] {r : Type*} [Fintype r] [DecidableEq r]
    {𝕜 : Type*} [RCLike 𝕜] (d : StabilityData n r 𝕜) : Matrix r r 𝕜 := d.Vᴴ * d.V

/-- `(Vᴴ V)ᴴ = Vᴴ V`, i.e. `M` is Hermitian. -/
lemma M_hermitian {n : Type*} [Fintype n] [DecidableEq n] {r : Type*} [Fintype r] [DecidableEq r]
    {𝕜 : Type*} [RCLike 𝕜] (d : StabilityData n r 𝕜) : (M d).IsHermitian := by
  rw [Matrix.IsHermitian]
  calc
    ((d.Vᴴ * d.V)ᴴ) = d.Vᴴ * d.V := by
      rw [conjTranspose_mul]
      simp

/-- Positive part Q₊ of the Hermitian Q (from RHLinalg). -/
def posPart {n : Type*} [Fintype n] [DecidableEq n] {r : Type*} [Fintype r] [DecidableEq r]
    {𝕜 : Type*} [RCLike 𝕜] (d : StabilityData n r 𝕜) : Matrix n n 𝕜 :=
  RHLinalg.hermPosPart d.Q_hermitian

/-- Negative part Q₋ of the Hermitian Q (from RHLinalg). -/
def negPart {n : Type*} [Fintype n] [DecidableEq n] {r : Type*} [Fintype r] [DecidableEq r]
    {𝕜 : Type*} [RCLike 𝕜] (d : StabilityData n r 𝕜) : Matrix n n 𝕜 :=
  RHLinalg.hermNegPart d.Q_hermitian

/-- ainta eq. (2.1) — the main target. -/
theorem stability_inequality {n : Type*} [Fintype n] [DecidableEq n]
    {r : Type*} [Fintype r] [DecidableEq r] {𝕜 : Type*} [RCLike 𝕜]
    (d : StabilityData n r 𝕜) :
    RHLinalg.frobSq (P d + d.Q) ≥
      4 * (RHLinalg.rtrace (P d) + RHLinalg.rtrace d.Q)
        - 3 * Fintype.card r - 4 * Fintype.card r
        + spectralSum psi (M_hermitian d) := by
  sorry

/-! ## Lemma statements (the decomposition of the proof)

Each mirrors a step of the design note §1.2; the ones marked (AXIOM) are in
the axiom block at the bottom. -/

/-- (P1) Q = Q₊ − Q₋, both PSD, Q₊Q₋ = 0, rank Q₊ = posIndex Q ≤ b. -/
lemma decomp_Q_eq_posPart_sub_negPart {n : Type*} [Fintype n] [DecidableEq n]
    {r : Type*} [Fintype r] [DecidableEq r] {𝕜 : Type*} [RCLike 𝕜]
    (d : StabilityData n r 𝕜) :
    d.Q = posPart d - negPart d := by
  simpa [posPart, negPart] using
    (RHLinalg.hermPosPart_sub_hermNegPart d.Q_hermitian).symm

lemma posPart_negPart_mul_zero {n : Type*} [Fintype n] [DecidableEq n]
    {r : Type*} [Fintype r] [DecidableEq r] {𝕜 : Type*} [RCLike 𝕜]
    (d : StabilityData n r 𝕜) :
    posPart d * negPart d = 0 :=
  RHLinalg.hermPosPart_mul_hermNegPart d.Q_hermitian

lemma rank_posPart_le_b {n : Type*} [Fintype n] [DecidableEq n]
    {r : Type*} [Fintype r] [DecidableEq r] {𝕜 : Type*} [RCLike 𝕜]
    (d : StabilityData n r 𝕜) :
    (posPart d).rank ≤ Fintype.card r := by
  unfold posPart
  rw [RHLinalg.rank_hermPosPart]
  exact d.pos_eig_count_le_b

/-- (P2) ‖P+Q‖² ≥ ‖P−Q₋‖² + ‖Q₊‖² (drop the nonneg cross term). -/
lemma frobSq_P_add_Q_ge {n : Type*} [Fintype n] [DecidableEq n]
    {r : Type*} [Fintype r] [DecidableEq r] {𝕜 : Type*} [RCLike 𝕜]
    (d : StabilityData n r 𝕜) :
    RHLinalg.frobSq (P d + d.Q)
      ≥ RHLinalg.frobSq (P d - negPart d) + RHLinalg.frobSq (posPart d) := by
  sorry

/-- (P3) ‖Q₊‖² ≥ 4·tr(Q₊) − 4b, from λ² ≥ 4λ − 4 per positive eigenvalue. -/
lemma frobSq_posPart_ge {n : Type*} [Fintype n] [DecidableEq n]
    {r : Type*} [Fintype r] [DecidableEq r] {𝕜 : Type*} [RCLike 𝕜]
    (d : StabilityData n r 𝕜) :
    RHLinalg.frobSq (posPart d) ≥ 4 * RHLinalg.rtrace (posPart d) - 4 * Fintype.card r := by
  sorry

/-- (P4) min over n ≥ 0 of (p−n)² + 4n equals 2p − 1 + Ψ(p) (p ≥ 0). -/
lemma psi_min_identity (p : ℝ) (hp : 0 ≤ p) :
    sInf {x : ℝ | ∃ n : ℝ, 0 ≤ n ∧ x = (p - n) ^ 2 + 4 * n}
      = 2 * p - 1 + psi p := by
  sorry

/-- (P5) HOFFMANN–WIELANDT — the squared distance of Hermitian P − Q₋ is at
least the sum of squared eigenvalue differences. NOT in the existing repo;
kept as a named axiom (flag in note). -/
axiom hoffmann_wielandt {n : Type*} [Fintype n] [DecidableEq n]
    {𝕜 : Type*} [RCLike 𝕜] {A B : Matrix n n 𝕜}
    (hA : A.IsHermitian) (hB : B.IsHermitian) :
    RHLinalg.frobSq (A - B) ≥
      ∑ i, (hA.eigenvalues₀ i - hB.eigenvalues₀ i) ^ 2

/-- (P6) ‖P−Q₋‖² + 4·tr(Q₋) ≥ 2·tr(P) − r + tr Ψ(M). -/
lemma frobSq_P_sub_negPart_chain {n : Type*} [Fintype n] [DecidableEq n]
    {r : Type*} [Fintype r] [DecidableEq r] {𝕜 : Type*} [RCLike 𝕜]
    (d : StabilityData n r 𝕜) :
    RHLinalg.frobSq (P d - negPart d) + 4 * RHLinalg.rtrace (negPart d)
      ≥ 2 * RHLinalg.rtrace (P d) - Fintype.card r
        + spectralSum psi (M_hermitian d) := by
  sorry

/-- (P7) tr(P) ≤ r, from tr(P) = Σⱼ ‖col_j‖² and the column-norm hypothesis. -/
lemma rtrace_P_le_card {n : Type*} [Fintype n] [DecidableEq n]
    {r : Type*} [Fintype r] [DecidableEq r] {𝕜 : Type*} [RCLike 𝕜]
    (d : StabilityData n r 𝕜) :
    RHLinalg.rtrace (P d) ≤ Fintype.card r := by
  sorry

/-- (P8) Assembly: combine (P2),(P3),(P6),(P7) into (2.1) — the PAPER form
(`4·tr(P) − 3r`). The intermediate strong form `2·tr(P) − r` is NOT a valid
standalone bound (numerically false; see note remark). The proof goes through
the strong chain then weakens `2·tr(P)−r → 4·tr(P)−3r` via `tr(P) ≤ r`. -/
theorem stability_inequality_via_decomp {n : Type*} [Fintype n] [DecidableEq n]
    {r : Type*} [Fintype r] [DecidableEq r] {𝕜 : Type*} [RCLike 𝕜]
    (d : StabilityData n r 𝕜) :
    RHLinalg.frobSq (P d + d.Q) ≥
      4 * (RHLinalg.rtrace (P d) + RHLinalg.rtrace d.Q)
        - 3 * Fintype.card r - 4 * Fintype.card r
        + spectralSum psi (M_hermitian d) := by
  sorry

/-- (P6', the correct two-inequality chain) ‖P−Q₋‖² + 4·tr(Q₋) ≥ 2·tr(P) − r
+ tr Ψ(M) AND ‖P−Q₋‖² + 4·tr(Q₋) ≥ 4·tr(P) − 3r + tr Ψ(M) − 2(r − tr P) ≥
4·tr(P) − 3r + tr Ψ(M). The strong form alone is false; the paper form is what
the chain plus `tr(P) ≤ r` yields. -/
lemma strong_chain {n : Type*} [Fintype n] [DecidableEq n]
    {r : Type*} [Fintype r] [DecidableEq r] {𝕜 : Type*} [RCLike 𝕜]
    (d : StabilityData n r 𝕜) :
    RHLinalg.frobSq (P d - negPart d) + 4 * RHLinalg.rtrace (negPart d)
      ≥ 2 * RHLinalg.rtrace (P d) - Fintype.card r
        + spectralSum psi (M_hermitian d) := by
  sorry

/-! ## Axiom block: genuinely external analytic/counting inputs (FLAGGED)

These are NOT part of (2.1)'s linear algebra. They are the kernel/gap/counting
inputs that turn `tr Ψ(M)` into a concrete positive number. They stay as axioms
here (future Lean targets); (2.1) itself is meant to be fully proved. -/

section AnalyticInputs

/-- ainta §3: every triangle of normalized gap differences contributes a
positive Gram-defect. ε₄ ≥ 221/10⁶ (certificate (3.3)). -/
axiom delta_lower_bound_triangles (n : ℕ) :
    ∃ ε : ℝ, 0 < ε ∧
      ∀ (G : Matrix (Fin n) (Fin n) ℂ), G.IsHermitian →
        G.PosSemidef →
        ∀ hG : G.IsHermitian,
          spectralSum psi hG ≥ ε * (Fintype.card {i : Fin n // True} - 2)

/-- ainta §4: the 7-point window certificate (4.2), F₆ ≥ 19/5000. -/
axiom f6_lower_bound :
    ∀ g : Fin 6 → ℝ, (∀ i, 0 ≤ g i) →
      1 / 3000 * ∑ i, g i +
        ∑ s : Fin 6, 2 / (7 - (s.val + 1)) *
          ∑ i : Fin (7 - (s.val + 1)), 1 ≥ 19 / 5000

/-- Counting input (from Anthropic Theorem D / Proposition 4.4):
S ≥ H₀N − o(N). Kept as a reminder; not used inside (2.1). -/
axiom simple_zero_lower_bound :
    ∃ H0 : ℝ, H0 = 3 / 2 - (1 / Real.sqrt 2) * Real.cot (1 / Real.sqrt 2) ∧ True

end AnalyticInputs

end GramStability
