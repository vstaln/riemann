# Close the in-class gap: the exact LP-optimal certificate for the 256-law, and the honest split law-data vs real-data

**Agent:** EXECUTIONER (round-3 continuation of `attack-lpdual.md`; epistemics + logic + constraint-hardness lens)
**Date:** 2026-08-11
**Task:** turn the numerically-optimal bandwidth-one certificate (v\* = p₀ + |E(1)| = 0.68183123) into a rigorous, Lean-checkable theorem.
**Verdict up front:** the certificate is now **exact and rational**:  r(x) = 1 − x with
c₀ = p₀ − Σⱼ (S_max(j)/256)·(1 − j/256)  is valid against **every** S in the law's enclosure class, and its value is
**v = p₀ + 1/(6·256²) − δ**,  δ = 1.9046711470564975·10⁻⁴³ ≥ 0  (δ = 0 against the LP's midpoint data; the exact decimal is
**0.681831230595341890922618553905170067…**).  The Lean ceiling `ceiling_law256_signed` (PROVEN) bounds every valid
certificate with |r′(1)| ≤ 1, ∫|r″| = 0 by p₀ + 2.5431316·10⁻⁶ (slack 8.958·10⁻¹⁴ from decimal rounding; with exact constants
the ceiling is p₀ + 1/(6·256²) + τ/512, i.e. **the certificate attains the exact ceiling up to 5.86·10⁻⁴³ + δ** — the ceiling
is TIGHT).  The two claims are **strictly separated**: (i) the in-class optimum against the 256-law data is
0.68183123 (PROVEN up to τ-terms; LP-confirmed), (ii) the corresponding real-zero constant remains **0.6725** (Theorem D,
PROVEN) — the law's p₀ = 0.68183 is *not* a certified real-zero simple fraction, and the real near-CUE error is O(1/√log T),
~10³⁹ times the law's τ = 3·10⁻⁴⁰.  The 0.6725 → 0.6818 gap is closed **in-class**, not **for the real zeros**.

---

## 0. Honesty labels

| Claim | Label |
|---|---|
| Exact certificate r = 1−x: validity vs the whole enclosure class, exact value v = p₀ + 1/393216 − δ, stability identity, E(1) = −1/(6·256²), D(1) = 0.8239531607128352 | **PROVEN** — exact rational arithmetic, `tools/lpdual/verify_exact_cert.py` (re-derived from `LawN256.lean`, no floats) |
| Upper bound: every valid certificate with r(1) ≥ 0, \|r′(1)\| ≤ 1, ∫\|r″\| = 0 has v ≤ p₀ + 2.5431316·10⁻⁶ (and ≤ p₀ + 1/(6·256²) + τ/512 with exact constants) | **PROVEN (Lean)** — `ceiling_law256_signed`, `ceiling_nearCUE_signed` (axioms {propext, Classical.choice, Quot.sound}) |
| Hence in-class optimum (B=1, C=0) lies in [p₀ + 1/393216 − δ, p₀ + 1/393216 + 5.86·10⁻⁴³] | **PROVEN** (from the two rows above) |
| The boxed class optimum equals p₀ + \|E(1)\| exactly (no box-valid certificate beats it, any B, C) | **CHECKED NUMERICALLY** (LP, HiGHS, `tools/lpdual/`); the "box lemma" (\|r′(1)\| + ∫\|r″\| ≥ 1 for box-valid r with r(0)=1, r(1)=0) is **argued, not written** — the precise obstruction to a fully-exact optimality statement |
| EnclOK (the law's S(j) lies in the 256 integer enclosures) | **INCONCLUSIVE** — authors' certificate file not public; see `validation-enclok.md`; NOT REFUTED |
| Real-data constants: p₁ ≥ 2/3 (Thm B), ≥ 0.6725007… (Thm D), class ceiling ≤ 0.68183 | **PROVEN** (Thm B/D in the paper; ceiling PROVEN in Lean modulo EnclOK) |
| Real zeros satisfy near-CUE with τ ≈ 3·10⁻⁴⁰, or real p₁ ≥ 0.68183 | **CONJECTURED / unavailable** — beyond bandwidth 1 |
| The paper's "0.68185" (Remark 1.1) | consistent with the exact ceiling 0.68183123 at the 2·10⁻⁵ level (rounded statement); the exact value from this data is 0.681831230595 |

---

## 1. What the paper's Theorem B/D certificate actually is (which r, where the two-moment bound enters)

Source: `research/papers/claude-riemann-paper.txt` lines 185–237 (Thm A/B/D, Remark 1.1), 1919–2030 (§7.1),
1839–1842 (Proof of Thm B), 1737–1745 (Montgomery moments), 1749–1755 (E′_T).

**The 0.6725 certificate is NOT an r(x) in the ceiling class — it lives in the trace-ratio normalization.**
The paper's method bounds the simple-fraction s₁ via the ratio functional (7.3)

  c_λ(v) = λ(∫v)² / (∫v² + λ²∬|s−s′|v(s)v(s′)dsds′)  (v ≥ 0, supp v ⊆ [−1/2, 1/2]),

whose optimum (Cauchy–Schwarz on the positive-definite operator 1 + λ²T) is attained at the **Montgomery–Taylor window
v\*(s) = cos(√2λs)** (7.4), with c\*₁ = 0.7532960… and proportion **2 − 1/c\*₁ = 3/2 − (1/√2)·cot(1/√2) = 0.6725007036794116…**
(Theorem D; `Functional.lean` HD(1) — PROVEN).  The flat-top version (Theorem B) gives H(λ) = 2 − 1/λ − λ/3, i.e. 2/3 at
λ = 1.

**Where the two-moment bound enters:** the denominator ∥eG∥²_F = tr eG² is Montgomery's *second moment*
∫₋_λ^λ (λ−|α|)F(α)dα = λ + λ³/3, and Theorem 5.8 (= BGSTB24 Thm 1) proves this evaluation holds **unconditionally from the
prime side**, independent of the zeros' location.  This is the *only* pair-correlation input; it is a mean-square (L²) datum,
uniform in 0 ≤ α ≤ 1 with error F(α) = T^(−2α)(log T + O(1)) + α + O(1/√log T).

**The real configuration's constants vs the law's τ = 3·10⁻⁴⁰ (the honest re-derivation):**

| quantity | 256-law (this round's data) | real ζ-zeros (paper's Theorem B inputs) |
|---|---|---|
| certified simple fraction p₁ | p₀ = 0.681828687463831474… (exact rational, the law's own) | ≥ 2/3 (Thm B), ≥ 0.6725007… (Thm D) — **not** 0.6818 |
| near-CUE deviation | \|256·S(j) − j\| ≤ 2⁻¹³² = 1.837·10⁻⁴⁰ ≤ τ = 3·10⁻⁴⁰ (exact, over the whole box) | F(α) = α + O(1/√log T); no quantified uniform row bound at fixed N; error ~0.1 at T = 10¹⁰ — ~10³⁹ × the law's τ |
| error term | τ/512 = 5.86·10⁻⁴³ (negligible) | E′_T = O(log log T/log T) (λ=1) or O(1/log T) (λ<1), a quantified o(1) |
| E(1), D(1) | E(1) = −1/(6·256²) exactly; D(1) = +0.8239531607128352 (both from the grid law) | not certified at fixed N; only the mean-square two-moment control |
| certificate value | v\* = p₀ + \|E(1)\| = 0.68183123 | 0.6725007… (Thm D) is the best certified value; class ceiling 0.68183 is an upper bound |

**Bottom line for §1:** the two-moment bound certifies the *real* zeros only in L² on |α| ≤ 1 with error O(1/√log T);
the 256-law's τ = 3·10⁻⁴⁰ and p₀ = 0.68183 are *law* properties (the law is a synthetic extremal configuration), NOT
real-zero facts.  The ceiling theorem's validity hypothesis c₀ + Σ sⱼr(j/N) ≤ p₁ cannot be instantiated for the real zeros
with p₁ ≥ 0.6818 or with the law's masses — those are the beyond-bandwidth-1 inputs that are CONJECTURED (see
`attack-ceiling.md` §3).

---

## 2. The exact certificate (extracted from the LP, made rational)

**The LP-optimal certificate** (`tools/lpdual/lpdual_final.py`, results.json, boxed class, B = 1, C = 1): r(0) = 1.000,
r(1/2) = 0.3076, r(1) = 0, r′(1) = −0.6152, ∫|r″| = 1.0, gain = ∫rx − Σsⱼr = +2.543132·10⁻⁶ = |E(1)|.  **A cleaner optimum
with the same value is r(x) = 1 − x** (r(0) = 1, r′(1) = −1, ∫|r″| = 0), and this one is **exact with rational coefficients**
at every knot: r(j/256) = (256 − j)/256.

**Exact certificate (this round, PROVEN by `tools/lpdual/verify_exact_cert.py`):**

```
r(x) = 1 − x,  g(x) = r′(x) = −1,  h(x) = r″(x) = 0
c₀ = p₀ − Σ_{j=1}^{255} (S_max(j)/256)·(1 − j/256),   S_max(j) := hi_j/K  (top of the enclosure box)
   = p₀ − 21845/131072 − δ′ ,   δ′ = Σ_{j: hi_j = j·2^132 + 1} (2^-140/256)·(1 − j/256) = 1.9046711470564975·10⁻⁴³
value  v = c₀ + ∫₀¹ (1−x)x dx = c₀ + 1/6 = p₀ + 1/(6·256²) − δ′
        = 32727899068576410764285690587448163224591/48000000000000000000000000000000000000000 − δ′   (δ′ = 0 on the midpoint data)
        = 0.681831230595341890922618553905170067178979166…
```

Key facts verified exactly (fractions, no floats; data parsed from `LawN256.lean`):
- 124 of the 255 rows have hi_j = j·2¹³² (S(j) ≤ j/256), 131 rows have hi_j = j·2¹³² + 1 (S(j) ≤ j/256 + 2⁻¹⁴⁰);
  max |256·S(j) − j| over the whole box = 2⁻¹³² = 1.837·10⁻⁴⁰ ≤ τ = 3·10⁻⁴⁰ (margin 1.633).
- Σ_{j=1}^{255} (j/65536)·(1 − j/256) = 21845/131072 = 0.16666412353515625 (closed form: Σj, Σj²).
- E(1) = −1/(6·256²) = −1/393216 exactly for the midpoint model; D(1) = 0.8239531607128352 exactly.
- p₀ (Lean rational) = 0.6818286874638314742559518872385034005123125 (law_data.json's float p₀ differs by 2.57·10⁻¹⁷ — a
  float artifact; the Lean rational is authoritative).

**Validity is against the whole enclosure class** (PROVEN): since r(j/256) = 1 − j/256 ≥ 0 and EnclOK gives
K·S(j) ≤ hi_j (i.e. S(j) ≤ S_max(j)), c₀ + Σ (S(j)/256)r(j/256) ≤ c₀ + Σ (S_max(j)/256)r(j/256) = p₀ for **every** S with
EnclOK — hence in particular for the law's true S.  (A certificate valid against all S in the box is exactly what the
theorem's `hvalid` hypothesis needs, since the theorem is stated for an arbitrary S with EnclOK.)

**Stability identity (PROVEN, exact):** with r(1) = 0, g(1) = −1, h = 0,
Σ sⱼr(j/N) − ∫₀¹rx dx = r(1)D(1) − g(1)E(1) + ∫₀¹hE = 0·D(1) − (−1)(−1/393216) + 0 = −1/393216 = E(1),
i.e. the signed gain is exactly |E(1)| = 1/(6·256²).

**The precise obstruction to exactness** (what is not yet proven): the *upper* in-class bound v ≤ p₀ + |E(1)| for the
**boxed** class.  The Lean ceiling gives v ≤ p₀ + M(|g(1)| + ∫|h|), M = 1/(6·256²) + τ/512, which with |g(1)| ≤ 1, ∫|h| ≤ 0
is p₀ + M — a sliver 5.86·10⁻⁴³ above the attained p₀ + |E(1)| (decimal-Lear version: slack 8.958·10⁻¹⁴).  A proof that no
box-valid certificate beats p₀ + |E(1)| requires the "box lemma": for r with |r| ≤ 1 on [0,1], r(0) = 1, r(1) ≥ 0, the gain
Σsⱼr − ∫rx ≥ −|E(1)|.  Only the subcase r(0) = 1, r(1) = 0 is elementary (1 = |r(1)−r(0)| ≤ ∫|g| ≤ |g(1)| + ∫|g′|, so
v ≤ p₀ + M(|g(1)|+∫|h|) is attained within τ/512); the full box lemma (covering r(0) < 1, r(1) > 0, and the h-terms) is
argued but not written (LP says it holds: box-cap rows of results.json).  Since 5.86·10⁻⁴³ ≪ any significance threshold,
the correct formal target is the ceiling-level statement (below), not the box lemma.

---

## 3. The two claims, separated (CRITICAL HONESTY CHECK)

**(i) "The in-class optimum against the 256-law data is exactly 0.68183123"** — this is what the LP established, and it
is now rigorous up to τ-terms:

- **PROVEN (Lean + exact arithmetic):** every valid certificate with r(1) ≥ 0, |r′(1)| ≤ 1, ∫|r″| ≤ 0 has
  v ≤ p₀ + 2.5431316·10⁻⁶ (`ceiling_law256_signed`; exact constants: ≤ p₀ + 1/(6·256²) + τ/512); the certificate r = 1−x
  attains v = p₀ + 1/(6·256²) − δ′ ≥ p₀ + 1/(6·256²) − 3.58·10⁻⁴³.
  ⟹ **in-class optimum ∈ [p₀ + 1/393216 − δ′, p₀ + 1/393216 + 5.86·10⁻⁴³] = 0.6818312305953419 ± 10⁻⁴².**
- **CHECKED NUMERICALLY (LP):** the boxed class optimum equals p₀ + |E(1)| exactly (box-cap rows: B, C any → p₀ + |E(1)|);
  the no-box optimum is p₀ + M(B+C); row shadow prices and the p₁ shadow price (= 1.0) confirm no missing constraint
  inside bandwidth one.
- The headline "v\* = 0.68183123 = p₀ + |E(1)|" — **CHECKED NUMERICALLY** (LP, HiGHS; residual < 5·10⁻⁹), and its
  consistency with the Lean ceiling — **PROVEN** (ceiling attained numerically).

**(ii) "The corresponding constant for the REAL zero configuration"** — the paper's certificate, PROVEN, is
**0.6725007036794116…** (Theorem D; 2/3 flat-top, Theorem B).  The ceiling-class certificate r = 1−x does **not** transfer
to the real zeros:

- its validity needs c₀ + Σ sⱼr(j/N) ≤ p₁ with the *real* masses and the *real* simple fraction, and its value is
  p₁ − E(1)_real; the real data certify only p₁ ≥ 0.6725 and E(1)_real with no quantified uniform bound (O(1/√log T),
  sign unknown);
- the law's p₀ = 0.68183 is a law property; a proof that the real configuration cannot realize the law's shape (or a
  beyond-bandwidth-1 F(α) bound, or a multiplicity bound) is **CONJECTURED / unavailable** (`attack-ceiling.md` §3);
- Remark 1.1's ceiling bounds the *whole* method: no configuration-by-configuration certificate reading only
  bandwidth-one data can certify more than 0.68185 for ANY configuration, real zeros included
  (**PROVEN** in Lean modulo EnclOK; exact value 0.68183123).

**Real-data-valid value with the optimal r:** with the paper's Theorem B inputs alone the best certifiable value is
**0.6725** (Theorem D).  If the real zeros satisfied the near-CUE hypotheses with a quantified τ_real ≪ 1, the value would
be p₁_real + |E(1)_real| ≤ p₁_real + 1/(6·256²) + τ_real/512 — with p₁_real ≥ 0.6725 and τ_real = O(1/√log T) ≫ 1 the gain
term is ~10⁻⁶·τ_real, dwarfed by the 9·10⁻³ gap to 0.6818.  The 0.6725 → 0.6818 gap is **closed in-class, not for the
real zeros.**

---

## 4. The verification script (saved under tools/)

`tools/lpdual/verify_exact_cert.py` — exact-rational verification, re-deriving the law data from the canonical
`LawN256.lean` (enclosures, K = 2¹⁴⁰, p₀, τ); no floats.  Verifies:
1. enclosure structure (124 rows hi = j·2¹³², 131 rows hi = j·2¹³² + 1; S(j) ≤ j/256 + 2⁻¹⁴⁰; near-CUE over the box,
   max |256·S(j) − j| = 2⁻¹³² ≤ τ);
2. certificate validity vs the whole enclosure class (c₀ + Σ sⱼr(j/256) ≤ p₀);
3. exact value v = c₀ + 1/6 = p₀ + 1/393216 − δ′, δ′ = 1.9046711470564975·10⁻⁴³;
4. the stability identity exactly (Σsⱼr − ∫rx = E(1) = −1/393216);
5. consistency with `ceiling_law256_signed` (slack 8.958·10⁻¹⁴ decimal / 5.86·10⁻⁴³ exact — ceiling tight);
6. the two headline constants (law v\* = 0.6818312305953419 vs Thm-D 0.6725007036794116, gap 0.009330526915930282).

Run: `uv run --quiet python tools/lpdual/verify_exact_cert.py` (outputs in the transcript of this round).

---

## 5. Bottom line and the exact Lean-ization task

**What is now rigorously proven:**
1. The exact certificate r = 1−x (rational c₀) is valid against every S in the law's enclosure and attains
   v = p₀ + 1/(6·256²) − δ′ = **0.6818312305953419** (exact rational arithmetic).
2. The Lean ceiling `ceiling_law256_signed` bounds every valid certificate by p₀ + M(|r′(1)| + ∫|r″|), M = 1/(6·256²) + τ/512;
   hence the in-class optimum (B = 1, C = 0) lies in [p₀ + 1/(6·256²) − δ′, p₀ + 1/(6·256²) + τ/512], an interval of width
   τ/512 + δ′ ≈ 7.8·10⁻⁴³ — **the ceiling is tight** (the LP's "tight to 5·10⁻⁹" is now PROVEN to 7.8·10⁻⁴³ and exactly
   attained on the lower side by the rational certificate).
3. The real-data certificate remains 0.6725 (Theorem D, PROVEN); 0.68183 is the method's cap (PROVEN modulo EnclOK).

**What still needs the analytic constants (for the real zeros):** p₁ ≥ 0.6818 (beyond-bandwidth-1 / multiplicity —
CONJECTURED), and a quantified uniform near-CUE row bound for the real zeros (O(1/√log T) mean-square is all that exists).

**The exact Lean-ization task** (statement to formalize in `Zeta23/PairCeiling/`):

```lean
-- TARGET: the ceiling is attained; in-class optimum = p0 + 1/(6*256^2) (up to tau-terms).
theorem inclass_attainment (S : ℕ → ℝ) (hS : EnclOK LawN256.K S 0 LawN256.encl) :
    let r : ℝ → ℝ := fun x => 1 - x
    let c0 : ℝ := LawN256_p0 - ∑ j ∈ Finset.Icc 1 255, (LawN256.hi j / (LawN256.K * 256)) * (1 - (j:ℝ)/256)
    c0 + ∑ j ∈ Finset.Icc 1 255, massOf S 256 j * r ((j:ℝ)/256) ≤ LawN256_p0      -- validity vs the whole enclosure
    ∧ c0 + ∫ x in (0:ℝ)..1, r x * x = LawN256_p0 + 1 / (6 * (256:ℝ)^2) - δ        -- exact value, δ := the 131-row correction
```
plus the companion upper bound by instantiating `ceiling_law256_signed` with g = −1, h = 0, T = ∅:
`c0 + ∫₀¹ (1−x)x ≤ p₀ + 2.5431316e-6` (existing theorem, one `norm_num` + `simp` instance).

**Reused lemmas (already PROVEN, no new analysis):** `ceiling_law256_signed` (upper bound), `lawN256_rows`,
`LawN256_edge` / `D1_nonneg_of_edgeNonneg` (D(1) ≥ 0), `EnclOK` row bounds (S(j) ≤ hi_j/K), `massOf`, `Csum_massOf`,
`abel_ibp_second` (identity; not even needed if the value is computed directly via the closed forms Σj = 255·256/2,
Σj² = 255·256·511/6 and ∫₀¹(1−x)x = 1/6).

**New content required (mechanical, no new math):**
1. `LawN256_p0` as a named constant (currently inline in the comment; the p₀ rational lives in `LawN256.lean`'s header —
   add a `def LawN256_p0 : ℝ := 10909258999421303588095230195816054408197 / 16e39` or reuse the row-cert data);
2. the exact sum Σ_{j=1}^{255} (hi_j/K/256)(1 − j/256) = 21845/131072 + δ′ — by sum-formula lemmas (Σj, Σj²) plus a
   `decide`/`norm_num` computation of the 131-row correction (or simply keep δ′ symbolic and prove 0 ≤ δ′ ≤ 3.6·10⁻⁴³);
3. the polynomial interval integral ∫₀¹(1−x)x = 1/6 (mathlib has `intervalIntegral` of polynomials);
4. `r` is C¹ with g = −1 continuous, h = 0 integrable (trivial).

Estimated size: ~1 new theorem + ~4 small lemmas; reuses `Stability`, `Signed`, `NearCUE`, `CeilingLaw256`,
`RowCert`/`LawN256` verbatim.  The only non-Lean input remains EnclOK (INCONCLUSIVE — `validation-enclok.md`).

**What would change what we believe:** (a) the box lemma, written as a Lean theorem — removes the last 5.86·10⁻⁴³ sliver
and proves the *boxed*-class optimum is exactly p₀ + |E(1)|; (b) EnclOK resolved independently (regenerate the 256-law,
`research/notes/regenerate-256law.md`); (c) any beyond-bandwidth-1 datum (CONJECTURED) — each unit of certified real simple
fraction transfers 1:1 into the real constant (shadow price 1, LP-probed).

**Label for the headline claim:** in-class optimum against the 256-law = p₀ + 1/(6·256²) − δ′ =
**0.6818312305953419** — PROVEN (exact rational certificate + Lean ceiling, modulo the τ/512 + δ′ sliver ≈ 7.8·10⁻⁴³ and
EnclOK); real-zero constant = **0.6725** (Theorem D) — PROVEN; the gap 0.6725 → 0.6818 — closed in-class, CONJECTURED for
real zeros.
