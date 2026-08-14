# Moment-route map: which moment-type input certifies the box

**Agent:** architect (structural thread). **Date:** 2026-08-14.
**Status:** PROPOSED (architect deliverable, literature/structure only — no compute, per charter).
**Inputs:** `scale-gap-lemma-2026-08-14.md` (box = N(1/2 + 1/(2 log T), T) = o(T log T); C_T remark: the moment route must save a further 1/log T); `structural-thread-newinput-2026-08-14.md` (input taxonomy, arXiv IDs); `hooks/agents.md` charter. Skills: s4h-decision-option-mapping (expand the option set before narrowing), s4h-constraint-hardness-testing (which "walls" are real).

**One-line verdict:** The moment route collapses to a single clean target — the **second horizontal moment** Σ_{γ≤T}(β−1/2)². Its current unconditional bound is O(T) (trivial from Selberg's first moment Σ(β−1/2)=O(T)); the box is certified iff it is improved to **o(T/log T)** — a saving of exactly one log T, the precise "further 1/log T" the scale-gap note demands. Among the five candidate inputs, **Selberg's classical log|ζ| moment + the Littlewood–Selberg displacement identity (routes (a)/(c) fused)** is the single most promising, because it is the only route whose base is unconditionally PROVEN (Selberg 1946) and whose missing piece is a clean explicit scale rather than RH or a conjectured equivalence.

---

## 1. The decisive reduction (the whole map in one line)

Write L := log T, σ_b := 1/2 + 1/(2L). **Box:** B: N(σ_b, T) = o(T L).

**Markov (one line, PROVEN arithmetic).** Each zero with β > σ_b contributes (β−1/2)² ≥ 1/(4L²) to Σ(β−1/2)². Hence

> N(σ_b, T) · (1/(2L))² ≤ Σ_{β > σ_b, 0<γ≤T} (β−1/2)²,

so

> **Σ_{γ≤T}(β−1/2)² = o(T/L) ⟹ B.**  (PROVEN.)

**Sharpness.** The scale-gap counterexample C_T has Σ(β−1/2)² = T/(8π L) = Θ(T/L) (§5 there). So any moment bound *weaker* than o(T/L) — in particular the known O(T) — fails to exclude the box failure. **The moment route must save exactly one factor of L = log T on the second moment.** This is the "further 1/log T" remark, made precise.

**Localization (zero-density already does its part).** Ingham's zero-density gives N(1/2+δ, T) = o(T) for any fixed δ > 0, i.e. N(1/2+δ,T) = o(T L). So zeros at fixed positive distance are already dead; the box is entirely about the **thin strip** [σ_b, σ_b + δ₀] for any fixed δ₀. The moment route reduces to

> **Σ_{σ_b < β < 1/2+δ₀, γ≤T}(β−1/2)² = o(T/L).**  (PROVEN, by the split β ≤ σ_b + δ₀ vs β > σ_b + δ₀.)

This is exactly where zero-density is scale-blind (the scale-gap lemma) but moments are not.

**Known base and the gap.** Selberg (1946), unconditionally: ∫₀^T log|ζ(1/2+it)| dt = O(T), hence (Littlewood–Selberg identity, §2) Σ_{γ≤T}(β−1/2) = O(T). Pointwise (β−1/2)² ≤ (1/2)(β−1/2) then gives

> **Σ_{γ≤T}(β−1/2)² = O(T)** (PROVEN, trivial from Selberg). **Gap to the box: a factor L.**

No sub-T bound on the second moment is known. That is the entire frontier.

---

## 2. The spine: the Littlewood–Selberg displacement identity

The operative "explicit formula" for Σ(β−1/2) is **Littlewood's lemma** (Jensen in a strip; Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., §9.9), *not* the Fourier/Guinand–Weil explicit formula (which expresses Σ_ρ x^ρ in primes and does not directly see β). Littlewood's lemma gives, for σ₀ > 1/2:

> 2π Σ_{β > σ₀, 0<γ<T}(β − σ₀) = ∫₀^T log|ζ(σ₀+it)| dt − ∫₀^T log|ζ(2+it)| dt + O(log T)  (arg-terms ≪ log T by Littlewood S(T) = O(log T)).

At σ₀ = 1/2, ∫ log|ζ(2+it)| dt = O(T), so

> **Σ_{β > 1/2, γ≤T}(β−1/2) = (1/2π) ∫₀^T log|ζ(1/2+it)| dt + O(T).**  (first moment)

Integrating the lemma over σ₀ ∈ (1/2, 1] (Fubini: ∫_{1/2}^β (β−σ₀)dσ₀ = (β−1/2)²/2) gives the second-moment identity:

> **Σ_{β > 1/2, γ≤T}(β−1/2)² = (1/π) ∫_{1/2}^{1} ∫₀^T log|ζ(σ+it)| dt dσ + O(T).**  (second moment)

*Sign/boundary caveat `[inferred]`:* log|ζ| is signed (|ζ|<1 gives negative log); the identities hold with the positive part log⁺ dominating, and the σ₀→1/2 limit under RH is degenerate because zeros sit on the boundary — so the +O(T) boundary term is exactly where the box information lives, not a disposable error. This is consistent: under RH the double integral ∫∫ log|ζ| is Θ(T) while Σ(β−1/2)² = 0, the two balancing through the O(T) term. The rigorous statement to hand to a builder is the displacement sum itself, with the double integral as the tool.

**Hence the box ⟺ an o(T/L) bound on the second moment ⟺ (via §2) an o(T) bound on the strip-integrated double integral of log⁺|ζ|.** Both forms carry the same one-log-T gap over the known O(T).

---

## 3. The map (candidate moment inputs)

| Route | Literature status | What it gives for the box | Cheapest attackable first step |
|---|---|---|---|
| **(a) Selberg's classical moment ∫₀^T \|ζ(1/2+it)\|² dt and log\|ζ\| relatives** | ∫\|ζ\|² ~ T L and ∫\|ζ\|⁴ ~ (1/2π²)T L⁴: **PROVEN** (Hardy–Littlewood 1918; Ingham/Selberg). ∫ log\|ζ(1/2+it)\| dt = O(T): **PROVEN** (Selberg 1946). ∫(log\|ζ\|)² ≪ T log log T: PROVEN (Selberg, unconditional CLT input). | The \|ζ\|²⁽ᵏ⁾ moments are the **wrong lever**: they measure vertical density (via the Γ-factor/Hadamard product), not horizontal displacement — a Jensen gap separates \|ζ\| from log\|ζ\| near zeros. The **log\|ζ\| first moment** is the right lever and gives Σ(β−1/2)=O(T) — insufficient (off by L on the second moment). | State the exact Littlewood–Selberg first- and second-moment identities (§2) with correct positive-part and arg terms; locate every known unconditional bound on ∫∫ log⁺\|ζ(σ+it)\| dσ dt over [1/2,1]×[0,T] and confirm the best is O(T). |
| **(b) Vertical distribution: Littlewood S(T) = O(log T)** | S(T) = O(log T): **PROVEN** (Littlewood 1924), unconditional. Quantitative form: N(T) − (T/2π)log(T/2πe) − 7/8 = O(log T). | S(T) constrains the **vertical count**, not β. C_T satisfies S(T) = O(log T) (its N(T) matches von Mangoldt to O(1)) yet violates the box — so O(log T) is blind to the box. The upgrade S(T) = o(log T) (true under RH: S(T)=O(log T/log log T)) is the candidate input, but its link to the box is **CONJECTURED/OPEN** (flagged as open in scale-gap §9.2), not a theorem. | Determine whether S(T) = o(log T) ⟹ B (or ⟺ B) is provable — a structure question, not a bound; the known unconditional base O(log T) is INSUFFICIENT (C_T witness). |
| **(c) Landau/Gonek Σ_{γ≤T}(β−1/2) via (ζ′/ζ) identities** | Landau's explicit formula (1909) and Gonek's uniform version (Contemp. Math. 143 (1993)): **PROVEN** machinery expressing Σ_ρ f(ρ) via (ζ′/ζ). | Same object as (a) by a different tool. First moment Σ(β−1/2)=O(T) reproven via Landau; the second moment becomes a **double sum over zero pairs** Σ_{ρ,ρ′} f(ρ,ρ′), i.e. a pair-correlation-type estimate — which is exactly what BGSTB (2306.04799) already consumes. So (c) exposes that the second-moment route is secretly a **pair-correlation input**, and BGSTB's box result (61.7%) is the *consumer* of the box, not a supplier — potential circularity to flag. | Derive the Landau/Gonek form of Σ(β−1/2)² as an explicit double sum over zeros and check whether any unconditional estimate of it is known independently of the box. |
| **(d) log\|ζ\| large-sieve / Soundararajan resonance** | Soundararajan resonance + large sieve for log\|ζ\|: **PROVEN** unconditional machinery (Math. Ann. 342 (2008); Ann. of Math. 170 (2009)); gives sharp upper bounds on ∫(log\|ζ\|)^{2k}. | Controls log\|ζ\| **on the line** (σ=1/2), sharpening the **first** moment's constant — the wrong scale. The box needs the **second** moment (or the σ-integrated double integral), a genuinely different quantity that resonance does not reach. Not decisive on its own; value is as a sharper first-moment input feeding (a). | Check whether the resonance method extends to the σ-integrated double integral ∫∫ log⁺\|ζ\| or to a bound on the count of t where log\|ζ(1/2+it)\| stays large — and whether any such bound improves Σ(β−1/2)² below O(T). |
| **(e) 2024–2026 unconditional mean-square on the line implying a first moment of β−1/2** | **INCONCLUSIVE.** Surveyed in `structural-thread-newinput-2026-08-14.md`: nothing in 2024–2026 gives Σ(β−1/2) beyond Selberg's O(T), nor any mean-square implying it. Guth–Maynard zero-density (2024, survey arXiv:2607.04632) is **scale-blind** (the scale-gap lemma proves it cannot supply the box). Goldston–Suriajaya / BGSTB (arXiv:2511.20059, 2603.28104, 2306.04799) is the *pair-correlation / simple-zeros* route — a downstream consumer of a box-like input, not a supplier of the displacement moment. | No unconditional 2024–2026 input supplies the box; confirmed from the repo's own literature survey. | Keep as watch-list only; the live item is whether GS's "general estimate" (a double sum over zeros) can be proven unconditionally — which is route (c)'s double sum, i.e. the same object. |

---

## 4. Ranking (criteria: decisiveness, proven base, cleanliness of the missing piece)

| Rank | Route | Decisive if proven? | Unconditional PROVEN base? | Missing piece |
|---|---|---|---|---|
| **1** | **(a) fused with (c): horizontal-displacement second moment** | **Yes** — Σ(β−1/2)²=o(T/L) ⟹ B, one-line Markov (PROVEN) | **Yes** — Selberg Σ(β−1/2)=O(T) ⟹ Σ(β−1/2)²=O(T) | an explicit factor-L saving; no RH, no conjectured equivalence |
| 2 | (c) Landau/Gonek double-sum form | Yes (same object) | Yes (machinery) | a pair-correlation-type estimate — harder, and near-circular vs BGSTB |
| 3 | (d) Soundararajan resonance | No on its own (first-moment scale) | Yes (machinery) | extension to the σ-integrated/second-moment scale |
| 4 | (b) S(T) = o(log T) | Conjectured equivalence (OPEN) | Partial (base O(log T) insufficient) | the S(T)↔box implication itself |
| 5 | (e) 2024–2026 mean-squares | No supplier found | n/a | absent — proven scale-blind (zero-density) or downstream (pair correlation) |

**Winner: route 1 — the second horizontal moment Σ(β−1/2)² = o(T/log T), attacked through the Littlewood–Selberg identity (a) with Landau/Gonek (c) as the alternative tool.** Rationale: it is the *only* route whose base (Selberg 1946) is unconditionally proven, whose sufficiency (Markov) is a one-line proven implication, and whose missing piece is a clean explicit scale (one log T) rather than RH or a conjectured equivalence. The scale-gap lemma already isolated exactly this scale ("save a further 1/log T"), and §1–§2 turn that remark into a single sharp statement.

---

## 5. The pick and the builder task

**Pick:** route (a)/(c) — prove (or refute) the second horizontal moment bound Σ_{γ≤T}(β−1/2)² = o(T/log T), which certifies the box by one-line Markov.

**Builder task (one line):** Starting from Selberg's unconditional Σ_{γ≤T}(β−1/2) = O(T), prove or refute the strengthening Σ_{γ≤T}(β−1/2)² = o(T/log T) — equivalently (Littlewood–Selberg identity) that ∫_{1/2}^{1}∫₀^T log⁺|ζ(σ+it)| dt dσ = o(T) — the single bound that certifies N(1/2 + 1/(2 log T), T) = o(T log T); first step is to derive the exact second-moment identity with correct positive-part and arg terms and enumerate every known unconditional bound on it.

---

## 6. Labels

| Claim | Label |
|---|---|
| Σ(β−1/2)² = o(T/L) ⟹ B (Markov) | **PROVEN** (§1, one line) |
| C_T has Σ(β−1/2)² = Θ(T/L); O(T) fails to exclude the box | PROVEN (scale-gap §5 + arithmetic) |
| Box reduces to the thin strip [σ_b, 1/2+δ₀] (zero-density does the rest) | PROVEN (Ingham zero-density + split) |
| Littlewood–Selberg first-moment identity Σ(β−1/2) = (1/2π)∫log\|ζ\| + O(T) | PROVEN (Titchmarsh §9.9) |
| Second-moment identity Σ(β−1/2)² = (1/π)∫∫log\|ζ\| + O(T) | PROVEN (integrate §9.9); boundary-term caveat `[inferred]` |
| Σ(β−1/2) = O(T) unconditional | PROVEN (Selberg 1946) |
| Σ(β−1/2)² = O(T) unconditional | PROVEN (trivial from Selberg; (β−1/2)² ≤ (1/2)(β−1/2)) |
| No sub-T bound on Σ(β−1/2)² known; nothing 2024–2026 supplies it | `[inferred]` (repo survey `structural-thread-newinput` found none; no exhaustive new search this session) |
| S(T) = O(log T) unconditional | PROVEN (Littlewood 1924) |
| S(T)=O(log T) is blind to the box (C_T witness); S(T)=o(log T)↔box | PROVEN (witness) / **CONJECTURED–OPEN** (equivalence, scale-gap §9.2) |
| Guth–Maynard zero-density cannot supply the box | PROVEN (scale-gap lemma) |

---

## 7. Assumptions

- `[verified]` In-repo: box definition, C_T and its Σ(β−1/2)² = T/(8π log T), the "save a further 1/log T" remark, the arXiv IDs (2306.04799, 2511.20059, 2603.28104, 2501.14545, 2607.04632), the zero-density/scale-gap verdict.
- `[verified]` (literature-standard, from training): Hardy–Littlewood ∫|ζ|² ~ T log T; Selberg ∫ log|ζ(1/2+it)| dt = O(T) and Σ(β−1/2)=O(T); Littlewood S(T)=O(log T); Littlewood's lemma (Titchmarsh §9.9); Landau (1909) and Gonek (1993) explicit formulas; Soundararajan resonance (2008/2009). Section numbers are standard references, not re-opened this session.
- `[inferred]` the sign/positive-part and boundary (σ₀→1/2) handling of the second-moment identity — flagged explicitly in §2; the displacement-sum formulation is what is rigorous.
- `[inferred]` that no bound better than O(T) on the second moment exists in the literature — based on the repo's own 2024–2026 survey plus the fact that the route is structurally equivalent to the (open) box statement; not an exhaustive independent search.
- No computation performed (literature/structure only, per charter); every quantitative statement is hand algebra (Markov, the C_T arithmetic) already certified in `scale-gap-lemma-2026-08-14.md`.

---

## 8. Skills applied (mandatory)

- **s4h-decision-option-mapping.** Expanded the option set beyond the two "obvious" inputs (first-moment and S(T)) to all five, and identified the *reframe* that collapses the map: the box is a threshold statement, and its cheapest sufficient moment is p = 2 at scale o(T/L), not p = 1 (which is strictly stronger than needed and unproven) nor the |ζ|²⁽ᵏ⁾ moments (wrong scale, Jensen gap). Deferral and hybrid moves: (a)+(c) are hybridized (same object, two tools).
- **s4h-constraint-hardness-testing.** Tested the implicit constraint "the moment route must save 1/log T" (from scale-gap §5). Source: a theorem (the C_T counterexample forces o(T/L)); consequence if violated: the box is unexcluded. Classification: **HARD at first-moment scale** (C_T is a genuine witness), **SOFT at second-moment scale** (nothing known precludes Σ(β−1/2)² = o(T/L)) — which is exactly why the second moment is the live target. Also tested "zero-density is useless here": confirmed HARD (scale-gap lemma) but scoped to fixed-σ; the thin-strip localization (§1) shows zero-density *does* still eliminate the fixed-distance tail, shrinking the moment route to a finite strip.

---

## 9. Next step

Hand the pick (§5) to a **builder**: derive the exact second-moment identity and enumerate known bounds on it (literature first), then attempt the o(T/L) strengthening. This is the single lever the scale-gap lemma left alive, now reduced to one explicit sentence.
