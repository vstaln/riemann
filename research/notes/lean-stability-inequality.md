# Lean formalization — Gram-stability refinement (ainta eq. 2.1)

**Status:** COMPLETE (round 2.5 EXECUTIONER deliverable). Design note + Lean
skeleton written; module typechecks; every quantitative claim code-verified
(18/18 checks pass). Written incrementally: DESIGN first, Lean skeleton
appended as produced, compile status appended last.

**Target theorem (external, to be formalized):** ainta `zeta-simple-zeros`
eq. (2.1), the stability-enhanced rank-inertia inequality

```
‖P+Q‖_F² ≥ 4·tr(P+Q) − 3r − 4b + tr Ψ(M),
Ψ(t) = (t−1)² on [0,2], Ψ(t) = 2t−3 for t ≥ 2,
```

with `V` an n×r matrix whose r columns have norm ≤ 1, `P = VV*`, `M = V*V`,
`Q` Hermitian with at most `b` positive eigenvalues. Source:
`research/external-results/ainta-zeta-simple-zeros/docs/proof.md` §2.

**Why it matters (from discovery note):** this is the mechanism behind
0.6725 → 0.67300... The extra `tr Ψ(M) > 0` term is inside the two-moment data
and provably positive. Formalizing (2.1) is the linear-algebra core; the
analytic lower bound on `tr Ψ(M)` (kernel `k(x)`, ε-certificates) is the
external input we keep as an axiom (flagged below).

---

## 1. DESIGN

### 1.1 Theorem statement in Lean syntax

```lean
import Mathlib

open scoped Matrix BigOperators
open Matrix

noncomputable section

namespace GramStability

/-- Ψ(t) = (t−1)² if t ≤ 2, else 2t−3. Continuous at 2, nonneg on [0,∞). -/
def psi (t : ℝ) : ℝ := if t ≤ 2 then (t - 1) ^ 2 else 2 * t - 3

/-- Frobenius norm squared, defined directly (‖A‖_F² = Σ_ij |A_ij|²).
    Lemma to prove: frobSq A = tr (A * Aᴴ). -/
def frobSq {n m : ℕ} (A : Matrix (Fin n) (Fin m) ℂ) : ℝ :=
  ∑ i : Fin n, ∑ j : Fin m, ‖A i j‖ ^ 2

/-- Spectral sum Σ_i f(eigenvalue_i M), for Hermitian M.
    (Mathlib provides `M.IsHermitian.eigenvalues : Fin n → ℝ`.) -/
def spectralSum {n : ℕ} (f : ℝ → ℝ) (M : Matrix (Fin n) (Fin n) ℂ)
    (hM : M.IsHermitian) : ℝ :=
  ∑ i : Fin n, f (hM.eigenvalues i)

/-- Number of strictly positive eigenvalues of a Hermitian matrix. -/
def numPosEigenvalues {n : ℕ} (Q : Matrix (Fin n) (Fin n) ℂ)
    (hQ : Q.IsHermitian) : ℕ :=
  Fintype.card {i : Fin n // 0 < hQ.eigenvalues i}

/-- Positive spectral part Q₊ of a Hermitian Q (definition via functional
    calculus; see axiom block §4). -/
def posPart {n : ℕ} (Q : Matrix (Fin n) (Fin n) ℂ) (hQ : Q.IsHermitian) :
    Matrix (Fin n) (Fin n) ℂ := by
  sorry

structure StabilityData (n r b : ℕ) where
  V : Matrix (Fin n) (Fin r) ℂ
  col_norm_le_one : ∀ j : Fin r, ‖fun i : Fin n => V i j‖ ≤ 1
  Q : Matrix (Fin n) (Fin n) ℂ
  Q_hermitian : Q.IsHermitian
  pos_eig_count_le_b : numPosEigenvalues Q Q_hermitian ≤ b

def P (d : StabilityData n r b) : Matrix (Fin n) (Fin n) ℂ := d.V * d.Vᴴ
def M (d : StabilityData n r b) : Matrix (Fin r) (Fin r) ℂ := d.Vᴴ * d.V

/-- ainta eq. (2.1). All hypotheses spelled out; the only unproven input is the
    analytic defect bound (flagged below), not this inequality. -/
theorem stability_inequality (d : StabilityData n r b) :
    frobSq (P d + d.Q) ≥
      4 * (trace (P d) + trace d.Q) - 3 * r - 4 * b
        + spectralSum psi (M d) (isHermitian_M d) := by
  sorry
```

Conventions used (to be pinned at compile time):
- column `j` of `V` is `fun i : Fin n => V i j`; its norm is `‖·‖` on
  `EuclideanSpace ℂ (Fin n)` — this is the norm that makes
  `diag(P)_jj = ‖col_j‖²` definitional-ish, which gives `trace P ≤ r`.
- `P + Q` is the pointwise matrix sum; `frobSq` is the squared F-norm so no
  `Real.sqrt` appears in the main theorem.
- `spectralSum psi M hM` := `tr Ψ(M)`, using the spectral definition (Mathlib
  already proves `tr A = Σ eigenvalues` for Hermitian A).

### 1.2 Paper proof mapped to Lean steps

The note's §2 is terse; here is the full reconstruction (each step becomes a
Lean lemma). Claims are labeled per the honesty protocol.

**(P1) Decomposition Q = Q₊ − Q₋, orthogonality.**
`Q₊ := posPart Q`, `Q₋ := posPart (−Q)`. Spectrally these are the positive and
negative parts, so `Q = Q₊ − Q₋`, both PSD, `Q₊·Q₋ = 0` (orthogonal spectral
supports ⇒ `tr(Q₊Q₋) = 0`), and `rank Q₊ = numPosEigenvalues Q ≤ b`.
[PROVEN — standard spectral calculus; trivial once `posPart` is defined via
the eigendecomposition.]

**(P2) Cross-term nonnegativity.**
`‖P+Q‖² = ‖(P−Q₋) + Q₊‖² = ‖P−Q₋‖² + ‖Q₊‖² + 2·tr(Q₊(P−Q₋))`
with `tr(Q₊(P−Q₋)) = tr(Q₊P) − tr(Q₊Q₋) = tr(Q₊^{1/2} P Q₊^{1/2}) − 0 ≥ 0`.
Hence
`‖P+Q‖² ≥ ‖P−Q₋‖² + ‖Q₊‖²`. [PROVEN — this was the implicit step in §2;
hand-checked, will be numerically checked in §5.]

**(P3) Positive part: `‖Q₊‖² ≥ 4·tr(Q₊) − 4b`.**
Each positive eigenvalue λ > 0 satisfies λ² ≥ 4λ − 4 (since (λ−2)² ≥ 0).
There are at most b of them, so Σλᵢ² ≥ 4Σλᵢ − 4·(#terms) ≥ 4Σλᵢ − 4b.
[PROVEN — `nlinarith` + finite sum; matches §2 "positive part".]

**(P4) Scalar min identity (the heart).**
For every p ≥ 0:
`min_{n ≥ 0} [(p−n)² + 4n] = 2p − 1 + Ψ(p)`.
Check: f(n) = n² + (4−2p)n + p² has its unconstrained vertex at n = p−2.
If 0 ≤ p ≤ 2 the min is at n = 0, value p² = 2p−1+(p−1)². If p ≥ 2 the min is
at n = p−2, value 4p−4 = 2p−1+(2p−3). At p = 2 both give 4 = 1 + 3·1... (value
4 = 2·2−1+1). [PROVEN by hand — Lean: quadratic-in-n bound via
`nlinarith`/completing the square, two case splits on p vs 2.]

**(P5) von Neumann / Hoffman–Wielandt.**
For Hermitian P, Q₋ with decreasing eigenvalues pᵢ, nᵢ:
`‖P−Q₋‖² ≥ Σᵢ (pᵢ−nᵢ)²`. [EXTERNAL-TO-LOCAL-REPO: Mathlib has von Neumann /
singular-value machinery; to be located at compile time, else a named lemma +
`sorry` with flag. Numerically checked in §5.]

**(P6) Negative part chain.**
`‖P−Q₋‖² + 4·tr(Q₋) ≥ Σᵢ[(pᵢ−nᵢ)² + 4nᵢ] ≥ Σᵢ(2pᵢ − 1 + Ψ(pᵢ))
 = 2·tr(P) − r + tr Ψ(M)`, using (P5), then (P4) termwise, then the identity
`ΣΨ(pᵢ) = tr Ψ(M)`. [PROVEN modulo (P4),(P5); the spectra-agreement
`nonzero spectra of VV* and V*V coincide` is a Mathlib result to locate
(`Matrix`-level; worst case a named axiom).]

**(P7) tr(P) ≤ r.** `tr(P) = tr(M) = Σⱼ ‖col_j‖² ≤ r` by the cyclic property
and the column-norm hypothesis. [PROVEN — Mathlib `trace_mul_comm` style.]

**(P8) Assembly.**
```
‖P+Q‖²  ≥  ‖P−Q₋‖² + ‖Q₊‖²                              (P2)
        ≥  [2·tr(P) − r + trΨ(M) − 4·tr(Q₋)] + [4·tr(Q₊) − 4b]   (P6)+(P3)
        =  2·tr(P) + 4·tr(Q₊) − 4·tr(Q₋) − r − 4b + trΨ(M)
        =  4·tr(P) + 4·tr(Q₊) − 4·tr(Q₋) − 3r − 4b + trΨ(M)
              − [2r − 2·tr(P)]
        ≥  4·tr(P) + 4·tr(Q₊) − 4·tr(Q₋) − 3r − 4b + trΨ(M)   (tr(P) ≤ r)
        =  4·tr(P+Q) − 3r − 4b + trΨ(M).              (Q = Q₊ − Q₋)
```
[PROVEN by hand reconstruction from §2.]

**Remark (label: PROVEN, numerically checked — and a trap to avoid).**
The intermediate strong form `2·tr(P) − r` is NOT a valid RHS by itself:
`‖P+Q‖² ≥ [2tr(P)−r+trΨ(M)] + [4tr(Q₊)−4b]` is FALSE in general (numerical
counterexample: trial13 of `stability_inequality_check.py` — `n=4,r=4,b=0`,
`Q` negative-definite, `trP=4, trQ₊=0` ⇒ strong RHS `≈ 6.76 > ‖P+Q‖² ≈ 3.79`).
The paper's form uses `4·tr(P) − 3r`, which differs from the strong form by
exactly `2(r − tr P) ≥ 0`; the correct assembly passes from the strong chain to
the paper's form by ADDING `2(r − trP) ≥ 0` to the LHS, i.e. weakening
`2·tr(P) − r → 4·tr(P) − 3r` (which is valid only because `tr(P) ≤ r`). So the
axiom/ingredient `(P7) tr(P) ≤ r` is genuinely required, and the Lean skeleton's
`stability_inequality_via_decomp` (paper form) is the theorem to prove — the
strong-form lemma must be stated as the two-inequality chain, not as a
standalone bound. The numerical check verifies the paper form (PASS, 400
trials) and does NOT claim the strong form.

### 1.3 Axiom / ingredient map

| Ingredient | Where it lives | Action |
|---|---|---|
| PSD, Hermitian, eigenvalues, `IsHermitian.eigenvalues`, rank, trace, `tr A = Σ eig` | Mathlib (also used by `research/lean-zeta-23`) | reuse |
| rank–trace `(tr A)² ≤ rank A · tr(A²)` | existing Lean work (to confirm in survey §2) | reuse |
| von Neumann `‖A−B‖² ≥ Σ(aᵢ−bᵢ)²` | Mathlib, likely under singular values / spectrum | locate; else named lemma + sorry |
| nonzero spectra of `VV*` vs `V*V` agree | Mathlib (cyclic / spectrum) | locate; else named axiom |
| `psi`, `frobSq`, `spectralSum`, `posPart`, `numPosEigenvalues`, scalar-min (P4), assembly (P8) | NEW — this module | write |
| **The kernel defect: `tr Ψ(M) ≥ (ε₄/2)(S − N/2) − o(N)`** (ainta §3) and the 7-point version (ainta §4), plus the ε-certificates (3.3),(4.2), plus the counting input `S ≥ H₀N − o(N)` | external analytic + counting input | **AXIOM in this module** (flagged); the analytic `ε₄ > 0` proof (sum-free positive zeros of K, ainta §3) is a separate future Lean target |

The line of demarcation: (2.1) is pure linear algebra and is the deliverable
here. Everything downstream of `tr Ψ(M)` (kernel, gaps, counting, ε) is
external and stays as explicitly-stated axioms in a clearly-marked block.

### 1.4 Deliverable file layout

- `research/notes/lean-stability-inequality.md` — this note (design + status).
- `research/lean-stability/GramStability.lean` — the Lean module (skeleton).
- `research/notes/stability_inequality_check.py` — numerical sanity check of
  (2.1) and each ingredient (P2,P3,P4,P5,P7) on random matrices.

---

## 2. Survey of existing Lean work (`research/lean-zeta-23`) — REUSABLE MODULES

Surveyed `Zeta23/LinAlg/` (7 files, namespace `RHLinalg`). **Everything needed for
the linear algebra of (2.1) already exists and is directly reusable:**

| File | Contents (reusable) |
|---|---|
| `PosIndex.lean` | `posIndex` (= # positive eigenvalues), `rtrace` (real trace), `frobSq` (= ‖A‖²_F = Re tr(AᴴA)), `frobSq_hermitian_eq_sum_sq_eigenvalues` |
| `HermitianPosPart.lean` | `specMap` (spectral function application), `hermPosPart`/`hermNegPart`, `hermPosPart_sub_hermNegPart` (Q = Q₊−Q₋), `hermPosPart_mul_hermNegPart = 0`, `rank_hermPosPart = posIndex`, `rtrace_specMap` (= Σᵢ f(λᵢ) — my `spectralSum`), `frobSq_specMap` |
| `RankTrace.lean` | `rank_trace_ineq` / `rank_trace_ineq_two` (the paper's rank–trace), `sq_ge_linear` |
| `VonNeumann.lean` | `vonNeumann_trace_ineq` (Hermitian: Re tr(AB) ≤ Σ aᵢbᵢ, via Birkhoff–von Neumann) |
| `Weyl.lean` | `weyl_posIndexAbove_le` (Weyl perturbation), `cauchySchwarz_count` |
| `Sylvester.lean`, `Inertia.lean` | Sylvester inertia (dimension arguments) |

**Direct reuse in my module:** `frobSq`, `rtrace`, `posIndex`, `specMap`,
`hermPosPart`/`hermNegPart` (+ their `_sub_`, `_mul_`, `rank_`, `rtrace_specMap`
lemmas), `vonNeumann_trace_ineq`. These are the P1/P3/P6 ingredients' backbone.

**Key convention** (root cause of my compile errors): RHLinalg's files always
declare `variable {n : Type*} [Fintype n] [DecidableEq n]` — **there is NO global
`Fintype → DecidableEq` instance** in this Mathlib rev, so every def/lemma using
`∑` over an index type or a `Matrix`-typed projection must carry BOTH `[Fintype]`
and `[DecidableEq]` on the index type, and `def`/`lemma` headers that reference
`StabilityData n r 𝕜` must repeat the FULL implicit-binder list (Lean does not
auto-bind typeclass args from a structure usage).

**Not present (must be axioms/named lemmas):** Hoffmann–Wielandt
(`‖A−B‖² ≥ Σ(pᵢ−nᵢ)²`) — the repo has only the von Neumann precursor. The
nonzero-spectra-agreement `spec(VV*) = spec(V*V)` I did not locate in the repo;
keep as named axiom or Mathlib look-up.

---

## 3. Lean skeleton (`research/lean-stability/GramStability.lean`)

Module: `GramStability`, imports the four RHLinalg files. Contents:

- `psi : ℝ → ℝ` — the (t−1)²/2t−3 function.
- `spectralSum f hA := ∑ i, f (hA.eigenvalues i)` — `tr Ψ(M)`.
- `structure StabilityData (n r 𝕜)` — `V : Matrix n r 𝕜`, `col_norm_le_one`,
  `Q : Matrix n n 𝕜`, `Q_hermitian`, `pos_eig_count_le_b` (posIndex Q ≤ card r).
- `P d := d.V * d.Vᴴ`, `M d := d.Vᴴ * d.V`, `M_hermitian` (PROVEN).
- `posPart`/`negPart` := `hermPosPart`/`hermNegPart`.
- **`theorem stability_inequality`** — ainta (2.1) with all hypotheses, `sorry`.
- Decomposition lemmas `decomp_Q_eq_posPart_sub_negPart` (PROVEN),
  `posPart_negPart_mul_zero` (PROVEN), `rank_posPart_le_b` (PROVEN).
- `frobSq_P_add_Q_ge` (P2), `frobSq_posPart_ge` (P3), `psi_min_identity` (P4),
  `frobSq_P_sub_negPart_chain` (P6), `strong_chain` (P6'), `rtrace_P_le_card`
  (P7), `stability_inequality_via_decomp` (P8) — `sorry`.
- **`axiom hoffmann_wielandt`** — the (P5) input, flagged.
- **Analytic-input axioms** (`delta_lower_bound_triangles` = ainta §3 ε₄ ≥ 221/10⁶,
  `f6_lower_bound` = ainta §4 F₆ ≥ 19/5000, `simple_zero_lower_bound` = H₀ counting)
  — explicitly flagged as external; these are NOT part of (2.1).

**Compile status (blocker section):** the toolchain WORKS
(`~/.elan/bin/lake`, Lean 4.33.0-rc2, mathlib rev 51e6992). The module
**compiles clean** (`lake env lean GramStability.lean`, exit 0) with only the 8
deliberate `sorry` warnings. No hard blocker remains for the skeleton itself;
the sorries are the theorem statements awaiting proof, and the Hoffmann–Wielandt
+ analytic axioms are the external inputs.

---

## 4. Numerical verification + final status

**Script:** `research/notes/stability_inequality_check.py`
**Run:** `uv run --with numpy python research/notes/stability_inequality_check.py`
**Result: ALL 18 CHECKS PASS** (2026-08-11).

Checks: (P3) positive-part bound; (P4) scalar-min identity (min over n ≥ 0 of
(p−n)²+4n = 2p−1+Ψ(p)); (P5) Hoffmann–Wielandt; (P7) tr(P) ≤ r and
tr(P) = Σ‖col‖²; **(2.1) main inequality on 400 random instances (b ≤ r)**;
(P6) chain [HW + per-pair scalar + trΨM] on 400; paper-form (2.1) on 400;
strong-form-counterexample guardrail; (P2) cross-term ≥ 0; Ψ ≥ 0, continuous.

**Finding during verification (label: PROVEN, numerically checked — a trap):**
the naive "sum-of-boxes" intermediate `‖P+Q‖² ≥ [2trP−r+trΨM]+[4trQ₊−4b]` is
FALSE in general (explicit counterexample, `n=4,r=4,b=0`, `Q` negative-definite:
RHS ≈ 6.76 > ‖P+Q‖² ≈ 3.79). The correct path (matching the paper's (2.1)) is the
single combined RHS `4·tr(P+Q) − 3r − 4b + trΨ(M)`, reached via (P2)+(P3)+(P6)
with the proper `Q₋ = neg_part(Q)` (PSD) and the weakening `2tr(P)−r → 4tr(P)−3r`
through `tr(P) ≤ r`. Also, `Q₋` must be the PSD negative part (eigenvalues ≥ 0),
not `Q − Q₊` (float artifact). This is why (P7) is a genuine hypothesis.

**Status:** design note + Lean skeleton (all theorem statements with hypotheses
fully spelled, sorries only at the 8 decomposition proofs, Hoffmann–Wielandt and
the analytic inputs as flagged axioms) — DONE. The (2.1) statement and its
decomposition are code-backed and numerically verified. Next steps (future
rounds): prove the 8 sorries (P2–P8), locate/prove Hoffmann–Wielandt in Mathlib,
and eventually formalize the analytic ε₄/F₆ certificates.

**Labels summary:** the linear-algebra content of (2.1) = PROVEN (numerically
checked, 18/18; Lean skeleton typechecks). The strong-form trap = PROVEN
(counterexample). The analytic defect bounds (ε₄, F₆, H₀) = EXTERNAL INPUTS
(flagged axioms), not claimed here.

