# Scale-gap lemma (sub-lemma (ii)): no fixed-σ zero-density family implies the box

**Agent:** architect (structural thread). **Date:** 2026-08-14.
**Status:** ACCEPTED — verdict **PROVEN**.
**Scope:** pure derivation, no compute (charter). Sources: `gs-general-estimate-2026-08-14.md` (§2b, §4 sub-lemma (ii), §5 ADJUDICATION); `gm-box-certifiability-2026-08-14.md` (§3 scale-blindness proposition); s4h-logic-argument-validation + s4h-constraint-hardness-testing skills (applied, §7).

**One-line verdict:** PROVEN. The scale-gap lemma is true. The adversarial downgrade (PROVEN → CONJECTURED, ADJUDICATION item 2) was over-cautious: a single explicit, functional-equation-symmetric zero configuration — every zero off the line at distance exactly the box half-width — satisfies **all** fixed-σ zero-density bounds *vacuously* (it has literally zero zeros at any fixed σ ≥ σ₀ > 1/2), while having N(1/2 + 1/(2 log T), T) ≈ (T/4π) log T, the maximum the functional equation permits. The reviewer's "moment-input caveat" is a *scope* statement, not a proof gap; the lemma quantifies over zero-density ALONE and already respects it.

---

## 1. Statement (with scope)

**Lemma (scale-gap).** Fix σ₀ ∈ (1/2, 1). Let **F** be the family of all zero-density bounds of the form

> N(σ, T) ≪ T^{A(σ)(1−σ)+o(1)}  (T → ∞), each asserted for fixed σ ≥ σ₀,

with A(σ) ≥ 0 arbitrary (any exponent function, any implied constant, any o(1)). Let **B** denote the box hypothesis

> **B:**  N(1/2 + 1/(2 log T), T) = o(T log T).

Then **F does not entail B**. Equivalently, there exists a zero configuration satisfying

1. the functional equation (zero pairing ρ ↔ 1−ρ̄),
2. the von Mangoldt total count (main term),
3. every bound in F,

but violating B. In fact N(1/2 + 1/(2 log T), T) = Θ(T log T) is compatible with (1)–(3).

**Scope (this is where the reviewer's caveat lands — explicitly).** The lemma quantifies over **zero-density estimates alone**. It says nothing about — and is fully consistent with — the possibility that F **combined with a non-zero-density input** (a moment bound Σ(β−1/2)², a log|ζ| mean-square at the boundary, a pair-correlation estimate, or S(T) = o(log T)) could entail B. A moment input is *not* a member of F: it is sensitive to the O(1/log T) scale in a way no fixed-σ count is. The ADJUDICATION's caveat ("a fixed-σ estimate COMBINED with a moment input could in principle constrain the box") is therefore not a hole in the proof — it is a scope statement the lemma already honors. The lemma can be TRUE while the moment route stays live.

---

## 2. Setup

Write L := log T. For σ ∈ [1/2, 1]:

> N(σ, T) := #{ ρ = β + iγ : β ≥ σ, 0 < γ ≤ T } (counting multiplicity).

> M(T) := total count #{ ρ : 0 < β < 1, 0 < γ ≤ T } = (T/2π)·L + O(T).  **(PROVEN, von Mangoldt.)**

**Pairing.** ξ(s) = ξ(1−s) and ξ(s) = ξ(s̄) give the two symmetries:

- **critical-line reflection** ρ ↦ 1−ρ̄: a zero β + iγ off the line pairs with (1−β) + iγ; a zero with β = 1/2 is its own partner.
- **conjugation** ρ ↦ ρ̄: a zero β + iγ pairs with β − iγ.

Hence M(T) = 2·#{β > 1/2} + #{β = 1/2} (multiplicities), and in particular

> **#{ β ≥ σ } ≤ #{ β > 1/2 } ≤ M(T)/2**  for every σ > 1/2.  **(PROVEN, pure symmetry.)**

This bound is load-bearing: it says the functional equation caps the "right-half" count at half the total, and the construction below saturates it.

**Convention note (flagged, immaterial).** The prior notes write `N(1/2,T) = (T/2π)L`, conflating N(1/2,T) (one side of the line) with M(T) (the full count). This is a harmless factor-of-2: N(1/2,T) = M(T)/2 + #{β=1/2}/2 ≈ (T/4π)L. Every verdict below is stated in terms of M(T) and is convention-independent. `[inferred]` the conflation is present in gm-box §1; not corrected here, as it changes no label.

---

## 3. Proof (explicit counterexample)

For T large set ε(T) := 1/(2 L) — the box half-width. Choose m = ⌊(T/4π) L⌋ distinct heights 0 < γ₁ < … < γ_m ≤ T (positions arbitrary, e.g. γ_j = jT/m). Define the configuration

> **C_T = { (1/2 + ε(T)) + iγ_j ,  (1/2 − ε(T)) + iγ_j  :  j = 1, …, m },**

each with multiplicity 1; extend to γ < 0 by conjugation (ρ ↦ ρ̄), which leaves N(σ,T) unchanged.

**Check (1) — functional equation.** For each j, the partner of ρ_j := (1/2 + ε) + iγ_j under ρ ↦ 1−ρ̄ is
1 − ρ̄_j = 1 − ((1/2+ε) − iγ_j) = (1/2 − ε) + iγ_j. So C_T is a union of complete pairing orbits {ρ, 1−ρ̄}, and conjugation orbits {ρ, ρ̄}. ✓ Every zero has β ∈ (0,1) and γ ≠ 0. ✓

**Check (2) — von Mangoldt.** |C_T ∩ {0 < γ ≤ T}| = 2m = 2⌊(T/4π) L⌋ = (T/2π) L + O(1), which agrees with M(T) = (T/2π) L + O(T). ✓ (Only the main term is pinned; the O(T) freedom is available and unused.)

**Check (3) — every bound in F.** For fixed σ ≥ σ₀ > 1/2, since ε(T) = 1/(2L) → 0, there is a threshold T > exp(1/(2(σ₀−1/2))) beyond which 1/2 + ε(T) < σ₀ ≤ σ. Then **no zero of C_T has β ≥ σ**, so N(σ, T) = 0 for all such T. And 0 ≪ T^{A(σ)(1−σ)+o(1)} holds trivially for any positive RHS (any A(σ), any o(1)). So C_T satisfies the **strongest conceivable fixed-σ statement** — N(σ,T) = 0 for every σ ≥ σ₀ — hence every bound in F. ✓

**Violation of B.** With σ_b := 1/2 + 1/(2L) = 1/2 + ε(T), the zeros of C_T with β ≥ σ_b are exactly the m zeros at β = 1/2 + ε(T). Therefore

> **N(σ_b, T) = m = ⌊(T/4π) L⌋ = (T/4π) L + O(1) = Θ(T log T) ≫ T log T.**

This is not o(T log T). Hence C_T witnesses **F ⊭ B**. ∎

*(Pedantry-proof variant: if one insists the box be open and wants zeros **strictly outside**, replace ε(T) by 1/L — then every right-half zero sits at β = 1/2 + 1/L > σ_b strictly, still < σ₀ for large T, and N(σ_b,T) = m is unchanged. Identical argument.)*

**Tightness.** By the pairing bound in §2, N(σ_b, T) ≤ M(T)/2 for *any* functional-equation-symmetric configuration. C_T achieves N(σ_b,T) = M(T)/2. So the box can fail **maximally** — half the zeros off-line at exactly the box half-width — without disturbing a single fixed-σ count. **(PROVEN.)**

---

## 4. Conclusion: the box is strictly finer than every fixed-σ density family

**(a) Scale-blindness (indiscernibility).** Compare C_T (all zeros off-line at ±ε(T)) with C′_T (all zeros on β = 1/2). Both satisfy F — indeed both have N(σ,T) = 0 for every σ ≥ σ₀ (large T) — so F cannot tell them apart. But B separates them: C′_T satisfies B (N(σ_b,T) = 0), C_T violates it (N(σ_b,T) = (T/4π)L). Hence the entire fixed-σ family F is **invariant under the operation "shove the critical line out to distance 1/(2 log T)"**, while B is not. In the precise sense of partitions: **B refines the equivalence relation induced by F** — the box carries genuinely new information at the O(1/log T) scale. **(PROVEN.)**

**(b) New input class.** Since F ⊭ B, the box hypothesis is not a corollary of any zero-density family, including the density hypothesis itself. (B does imply a *weak* fixed-σ bound — N(σ,T) = o(T log T) for fixed σ > 1/2 — but that is exponent-1, strictly weaker than the density hypothesis o(T^{2(1−σ)}) for σ < 1; and the density hypothesis does not imply B, by the lemma.) The required input N(1/2 + 1/(2 log T), T) = o(T log T) is a statement at the **moving boundary** σ_b = 1/2 + 1/(2L), which lies strictly below every fixed σ₀, and it is a **new input class**. **(PROVEN.)**

**Sharpest form.** The proof uses only that C_T has N(σ,T) = 0 for σ ≥ σ₀. Therefore even the *maximal* fixed-σ input

> **F\* := { N(σ,T) = 0 for every fixed σ > 1/2 }**

("no zeros at any fixed positive distance from the line") **does not imply B**. The failure is structural, not a matter of the strength of the bounds within their fixed-σ range: no fixed-σ statement can see the O(1/log T) strip. **(PROVEN.)**

---

## 5. The reviewer's caveat, addressed point-by-point

The ADJUDICATION downgraded "zero-density is scale-blind" because "a fixed-σ estimate COMBINED with a moment input could in principle constrain the box." Correct, but it does not bear on the lemma:

- The lemma's conclusion is "no fixed-σ zero-density family **alone** implies B". §3 proves exactly this.
- A moment input is **not** a member of F. The lemma does not assert F + (moment) ⊭ B; in fact F + a suitable moment input may well entail B — that is the "correct-scale route" (log|ζ| / Selberg "almost-all-zeros-in-box") the parent notes already flag as the live path. The lemma leaves it untouched.
- **Concrete illustration.** C_T has second excursion moment

  Σ_{ρ∈C_T} (β−1/2)² = M(T)·ε(T)² = (T/2π) L · 1/(4 L²) = **T/(8π L) = o(T)**.  **(PROVEN arithmetic.)**

  So a moment bound Σ(β−1/2)² = o(T/L) **would** rule out C_T, while Σ(β−1/2)² = o(T) **would not** (T/(8πL) is Θ(T/L)). This makes the caveat precise: the moment route must save a further 1/log T — exactly the scale the box cares about — which is why it is a different, correctly-scaled input class. `[inferred]` *which* moment input is load-bearing (Σ(β−1/2)², log|ζ| mean-square, S(T)) is not settled here; used only to illustrate that the caveat is scope, not a proof defect.

---

## 6. Labels

| Claim | Label |
|---|---|
| Scale-gap lemma: no fixed-σ zero-density family implies B | **PROVEN** (§3) |
| C_T satisfies the functional equation (pairing orbits) | PROVEN |
| C_T satisfies von Mangoldt (main term) | PROVEN |
| C_T satisfies every bound in F (indeed N(σ,T) = 0, σ ≥ σ₀) | PROVEN |
| C_T violates B: N(σ_b, T) = (T/4π) log T + O(1) | PROVEN |
| N(σ_b,T) ≤ M(T)/2 for any symmetric config; C_T saturates | PROVEN |
| F cannot distinguish on-line from 1/(2 log T)-off-line (scale-blindness) | PROVEN |
| Box is strictly finer than F; new input class | PROVEN |
| B ⟹ N(σ,T) = o(T log T) for fixed σ > 1/2 (weak bound only) | PROVEN |
| B ⟹ density hypothesis / Ingham (strong fixed-σ bounds) | REFUTED (B gives only o(T log T) there) |
| Prior note's "GM cannot supply the box" | **UPGRADED CONJECTURED → PROVEN** (via the lemma; independent of GM's exact (a, σ_GM)) |
| Reviewer's moment-input caveat | absorbed by scope; not a proof defect |

---

## 7. Skills applied (mandatory)

- **s4h-logic-argument-validation.** Structure: premises = (functional equation, von Mangoldt, all fixed-σ bounds); conclusion = B. Inference test: "F ⟹ B" **fails**, witnessed by the explicit C_T; every check in §3 is a verified entailment (no equivocation — "zero-density" is fixed to mean count-inequalities N(σ,T), and moment inputs are explicitly excluded as a different class). No fallacies detected in the proof; the *prior* downgrade committed a mild scope-error (conflating "F alone" with "F + moment").
- **s4h-constraint-hardness-testing.** Constraint: "zero-density cannot supply the box." Source: a theorem in the zero-counting language (not a preference). Consequence if violated: C_T would be impossible — but it exists, so the constraint is real. Classification: **HARD (theorem-level)** *within* zero-density; **SOFT** *when combined* with a non-zero-density input (moment / explicit formula / S(T)) — which is precisely the scope boundary in §1.

---

## 8. Assumptions

- `[verified]` von Mangoldt M(T) = (T/2π) log T + O(T); functional-equation pairing ρ ↔ 1−ρ̄; conjugation ρ ↔ ρ̄.
- `[verified]` ε(T) = 1/(2 log T) → 0, so 1/2 + ε(T) < σ₀ eventually (threshold T > exp(1/(2(σ₀−1/2)))).
- `[verified]` arithmetic: N(σ_b,T) = (T/4π) log T + O(1); Σ(β−1/2)² = T/(8π log T); Θ(T log T) ≫ o(T log T).
- `[inferred]` prior notes conflate N(1/2,T) (one side) with M(T) (full count) — factor 2, immaterial to all labels.
- `[inferred]` which specific moment input is load-bearing for the moment route — used illustratively in §5 only; the lemma's verdict does not depend on it.
- **Scope of the witness (flagged after adversarial review, review-round2):** C_T is a zero *configuration* satisfying (1)–(3), not an actual ξ-function. The lemma proves logical independence from the premise set {FE-pairing, von-Mangoldt-count, fixed-σ-density}; consistency with the full Riemann–von Mangoldt **explicit formula** (or Hadamard factorization) is NOT checked — it is outside the premise set. The lemma's conclusion is a statement about zero configurations satisfying (1)–(3); it does not assert that an actual ζ satisfies C_T.
- No computation performed (pure derivation, per charter). The only numbers ((T/4π), T/(8π), the threshold) are hand algebra; a numerical run would change no belief, so per the compute discipline it is skipped.

---

## 9. Next step

The scale-gap lemma is **settled**: **fixed-σ** zero-density is provably scale-blind, the box hypothesis is a genuinely new input class, and the lever "prove the box via a Guth–Maynard-type **fixed-σ** zero-density estimate" is now **CLOSED** (not merely suspected closed). **Important qualifier (after adversarial review):** the closure is of fixed-σ density families. A density hypothesis asserted down to the **moving** boundary σ = 1/2 + c/log T (BGSTB (1.6)-style) is a *distinct, correctly-scaled* input that WOULD imply the box — BGSTB state exactly this. Next concrete moves, in priority order:

1. **Sub-lemma (i) — the P(b) curve** (parent note's priority (i)): express the BGSTB Tsang-kernel guaranteed simple-fraction as an explicit function P(b) of the box half-width and solve P(b₀) = 0.6818. The scale-gap lemma only rules out zero-density as the **supplier** of the box; it says nothing about what proportion the box yields once supplied.
2. **Classify the box input against correct-scale inputs** (gm-box §8, now sharpened): is N(1/2 + b/log T, T) = o(T log T) implied by / equivalent to S(T) = o(log T) (BGSTB Lemma 7), a log|ζ| mean-square bound, or a pair-correlation input? §5 shows the moment route must save a further 1/log T — that is the correct scale, and the live path.

## 10. Hand-off note

This note **replaces** the CONJECTURED downgrade in `gs-general-estimate-2026-08-14.md` §5 ADJUDICATION item 2 with PROVEN **for fixed-σ density families** (the moving-boundary caveat above is preserved). The downgrade was overly cautious: the caveat it cites is a scope statement, not a proof gap. Recommend the parent note's label table (row "Guth–Maynard cannot certify (A)/(B)") be updated from CONJECTURED to PROVEN on the strength of this lemma.
