# B1-R — Beyond-1 Conditional Certificate Program (the only positive-priced input)

**Agent:** EXECUTIONER (B1-R; s4h applied: writing-report, epistemology, resource-allocation, investigation)
**Vector:** #7 of `attack-vector-catalog-3.md` (score 350): convert the pricing sheet's ONE positive price
(dv\*/dA = 0.6363/A³, F ≡ 1 on [1, 1+ε]) into a written CONDITIONAL certificate program.
**Date:** 2026-08-12. **Code:** `research/notes/beyond1-conditional-program.py` (this note's companion; every
number below is produced by it). Command: `cd /home/vstaln/riemann && uv run --quiet --with numpy --with
scipy --with mpmath python research/notes/beyond1-conditional-program.py`.
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED per hooks/agents.md; every numeric claim
carries its script-produced value.

---

## 0. Verdict up front (answer-first)

**Three labeled conditional results are now written, each with its hypothesis set and pricing attribution,
and every number in them is code-verified:**

1. **Conditional (a) — RH + HL\*(4, λ), all λ < 1 ⟹ ≥ 13/18 simple-on-line.** The arithmetic is now fully
   verified from the primary source (C = claude-riemann-paper.txt): 13/18 = 2·(31/36) − 1 = 26/36, where
   31/36 = 1 − Λ₂(0) and Λ₂(0) = **5/36 exactly** is the Christoffel function of the moment sequence
   (1, 1, 4/3, 2, 13/4) — computed here by the defining min-problem (exact fractions; CHECKED NUMERICALLY).
   **The value is 13/18 ONLY IF m₄ = 13/4.** The m₄-dependence is now quantified (this run): m₄ = 346/105
   ⟹ certified 0.6882; m₄ = 10/3 (extremal world) ⟹ exactly 2/3 (the extremal {2/3 simples, 1/6 doubles}
   saturates ALL moments (1, 4/3, 2, 10/3)); m₄ = 4.64 ⟹ 2/3 (the 4-moment route weakens to 0.5339, the
   2-moment bound wins); 28/9 is the Hankel extensibility boundary; empirical ≈ 3.07 is below it (not a
   valid moment sequence — finite-height deficit). **m₄ remains under adjudication (13/4 vs 346/105 vs
   10/3 vs 4.64); the roadmap's content is conditional on that adjudication.**

2. **Conditional (b) — RH + uniform HL on [1, A] (F ≡ 1) ⟹ the 0.70/0.80/0.90 roadmap at supports
   1.04/1.26/1.70.** The M2 curve p₁(A) = 1 − (1−p₀)/A² is reproduced (CHECKED NUMERICALLY): p₁(1.04) =
   0.705833, p₁(1.26) = 0.799590, p₁(1.70) = 0.889906 (vs the paper Remark's 0.70/0.80/0.90, rel err
   +0.83% / −0.05% / −1.12%, all ≤ 1.12%), and the shadow-price bookkeeping v\* = p₁(A) + |E(1)| is
   re-verified at every roadmap point (LP, residual 0.00e+00). Price per unit bandwidth: 0.636343/A³.

3. **Status of the FG twisted route (the strongest documented conditional statement in the library):** FG
   Thm 1.9 (RH + Conj 1.8 uniform Hardy–Littlewood) evaluates the smoothed twisted pair correlation
   F_n(α;ψ_U) = min{1, (logT/Λ(n))(α−1+logn/logT)} + O(loglogT/Λ(n)) beyond 1 — the exact conjectured
   shape of the additive-correlation object that C §7.5(f)'s HL\* names and that the pricing sheet prices
   positive. It is conditional all the way down (RH + a conjecture of HL strength), so it does not break
   the 0.6818/5/6 ceilings; it is the canonical conjectural beyond-1 target, now recorded in the literature
   map. **F_n + Conj 1.5 is the canonical conjectural beyond-1 target of this lane.**

**Why this is a result, not a stop:** every unconditional route past 0.6725 is PROVEN dead — the MV-Hilbert
bound fails the certificate's tolerance by 3.6·10³–3.7·10⁴× (M29, measured T = 10⁴–10⁶) — so the only
inputs with positive price are *values* (HL / Montgomery pair-correlation / HL\*), all conjectural
[pricing §5–§8, m29]. A documented conditional result is still a result (hooks/agents.md); this note makes
the conditional content precise, code-verified, and its m₄-dependence explicit.

---

## 1. The certificate at bandwidth A (assembly + shadow-price bookkeeping)

**Object (from `attack-lpdual.md` §1, PROVEN structure; exact certificates in Lean):** a certificate
(c₀, r), r ∈ C¹[0,1], value v = c₀ + ∫₀¹ r(x)x dx, valid against a marked configuration iff
c₀ + Σⱼ sⱼ r(j/N) ≤ p₁; the rank–trace method certifies "proportion of simple zeros ≥ v". The near-CUE
256-law (rows |256·S(j) − j| ≤ 3·10⁻⁴⁰, p₀ = 0.6818286874638315 — the exact rational is
10909258999421303588095230195816054408197/(16·10³⁹), decimal match to 0.00e+00; the task brief's trailing
…14 is a 1-ULP rounding, the code value …15 is authoritative) is the worst case; v\*(p₁) = p₁ + |E(1)|
with |E(1)| = 1/(6·256²) = 2.5431315104·10⁻⁶ and shadow price of p₁ exactly 1 (PROVEN attack-lpdual §3;
re-verified here at p₁ ∈ {0.70, 0.80, 0.90}, LP residual 0.00e+00, and the anchor v\*(p₀) =
0.681831230595342 matches attack-lpdual to 0.00e+00).

**At bandwidth A:** the certified worst-case simple fraction is p₁(A) and the certificate value is
**v\*(A) = p₁(A) + |E(1)|**, with the beyond-1 input's price **dv\*/dA = 2(1−p₀)/A³ = 0.636343/A³** per unit
bandwidth (M2 model, `attack-f1curve.md` §4; the only positive price on the pricing sheet [pricing §5–§6]).
The certificate side is insensitive to the beyond-1 row *values* (r's support is [0,1]; checked in the
pricing sheet for all tested δ); the entire price flows through p₁(A).

**M2 curve reproduced (all CHECKED NUMERICALLY, this run):**

| A | p₁(A) = 1 − (1−p₀)/A² | v\*(A) = p₁(A) + |E(1)| | Remark target | rel err vs Remark | dv\*/dA = 0.6363/A³ |
|---|---|---|---|---|---|
| 1.00 | 0.681829 | 0.681831231 | (baseline p₀) | — | 0.636343 |
| 1.04 | **0.705833** | **0.705835279** | 0.70 @ 1.04 | +0.83% | 0.565706 |
| 1.26 | **0.799590** | **0.799592293** | 0.80 @ 1.26 | −0.05% | 0.318112 |
| 1.70 | **0.889906** | **0.889908663** | 0.90 @ 1.70 | −1.12% | 0.129522 |

Bandwidth needed (M2) for exact 0.70/0.80/0.90: A = 1.0298 / 1.2613 / 1.7837 (Remark: 1.04/1.26/1.70;
bandwidth err −1.0% / +0.1% / +4.9%; the mid point exact, endpoints within 0.08 — reproduces the pricing
sheet §5 and f1curve §4). Cross-check with the rank–trace formula H(λ) = 2 − 1/λ − λ/3 (C (1.3)): H(1.04)
= 0.6918, H(1.26) = 0.7863, H(1.70) = 0.8451 — the two bandwidth models agree to within 2.0%/1.7%/5.0% of
the M2 value at these points (different certificate constructions; the M2 is the config-side worst case used
by the pricing sheet).

**Weakest link (honest):** the *exact* p₁(A) needs the authors' private configuration LP
(cert_N256_blk_b128m.json, not public — same blocker as f1curve/enclok); the M2 model is the documented
numerical instantiation (CHECKED NUMERICALLY, CONJECTURED-as-exact-curve).

---

## 2. Conditional statement (a): RH + HL\*(4, λ) ⟹ ≥ 13/18 — arithmetic verified, m₄-dependence quantified

### 2.1 The verified arithmetic (from C §7.5(d),(f) + Prop 4.5)

Chain (all steps verified in this run, exact fractions):
1. **Moments:** under HL\*(4, λ), the trace moments d⁻¹tr(G̃/ℓ₁)^k match the sine-kernel Gram-matrix
   moments m_k(1) = 1, 4/3, 2, **13/4** for k ≤ 4 (C §7.5(f); the raw-moment sequence is
   (μ₀,μ₁,μ₂,μ₃,μ₄) = (1, 1, 4/3, 2, 13/4)). Hankel determinants D₁ = 1, D₂ = 1/3, D₃ = 5/108 > 0 (a
   representing measure exists). **CHECKED NUMERICALLY.**
2. **Christoffel function:** Λ₂(0) := min{∫q²dσ : deg q ≤ 2, q(0) = 1}, σ = spectral measure. Solving the
   2×2 gradient system with exact fractions gives the minimizer q\*(x) = 1 − (7/4)x + (2/3)x² and
   **Λ₂(0) = 5/36 exactly** (the paper's value — CHECK OK). **m = 1 consistency check:** Λ₁(0) =
   1 − m₁²/m₂ = 1/4, so n₊/d ≥ 3/4 = (m₁)²/m₂ = F(1), reproducing Lemma 3.3's thresholded
   Cauchy–Schwarz value and §7.5(c)'s "2F(1) − 1 = 1/2 for simple zeros" via Prop 4.5's count. The
   framework is self-consistent.
3. **CMS bound (C §7.5(d)):** n₊(G̃)/d ≥ 1 − Λ₂(0) = 1 − 5/36 = **31/36**.
4. **Prop 4.5 count (C (4.8)):** N^s₀(T,2T) ≥ 2n₊(G̃) − N(T,2T) − o(N), so
   **N^s₀/N ≥ 2·(31/36) − 1 = 26/36 = 13/18 = 0.7222222222** (CHECK OK).

**Hypothesis set (explicit):** (i) RH; (ii) HL\*(4, λ) for all λ < 1 — the hypothesis that
d⁻¹tr(G̃/ℓ₁)^k = m_k(λ) + o(1) for k ≤ 4, where m_k(λ) is the k-th moment of the sine-kernel Gram-matrix
spectral distribution (for k = 4, λ > 1/2 this encodes a Hardy–Littlewood-type asymptotic for the additive
correlations Σ_m (Λ∗Λ)(m)(Λ∗Λ)(m+h), |h| ≤ X²/T — C §7.5(f)); (iii) the CMS-bound framework of C §7.5(d).
The statement is **PROVEN-as-stated in C** given these hypotheses; the arithmetic chain (1)–(4) is
**CHECKED NUMERICALLY** here. The hypotheses themselves are CONJECTURED about ζ (HL\* is a prime-pair
statement, unproven).

### 2.2 The m₄-dependence (the roadmap is conditional on the m₄ adjudication) — CHECKED NUMERICALLY, this run

The 13/18 flows through m₄ = 13/4. The catalog lists m₄ as under adjudication: **13/4 vs 346/105 vs 10/3
vs 4.64** (plus the hankel threshold 28/9 and the empirical ≈ 3.07). The certified value as a function of
the m₄ candidate (certified = max(2/3, 2(1−Λ₂(0; m₄))−1); 2/3 is the two-moment rank–trace bound, Prop
4.4(ii), unconditional in the certificate class):

| m₄ candidate | source | Λ₂(0; m₄) | n₊/d | 4-moment cert | certified (max with 2/3) |
|---|---|---|---|---|---|
| 13/4 = 3.25 | paper §7.5(f) | 0.138889 | 0.8611 | **0.722222 = 13/18** | **0.722222** |
| 346/105 ≈ 3.2952 | third-moment agent | 0.155914 | 0.8441 | 0.688172 | **0.688172** |
| 10/3 ≈ 3.3333 | extremal world (exact) | 0.166667 | 0.8333 | 0.666667 | **0.666667 = 2/3** |
| 4.64 | chem m4_check diagram | 0.233062 | 0.7669 | 0.533875 | **0.666667 = 2/3** |
| 28/9 ≈ 3.1111 | hankel extensibility threshold | 0 (D₃ = 0) | — | 1 (degenerate) | DEGENERATE (Hankel boundary) |
| ≈ 3.07 | empirical (finite height) | D₃ < 0 | — | — | **INVALID** — not a moment sequence |

Fine grid (f64): m₄ = 3.12 ⟹ 0.963; 3.20 ⟹ 0.778; 3.25 ⟹ 0.722 (=13/18); 3.30 ⟹ 0.685; 3.333 ⟹ 2/3;
3.50 ⟹ 2/3; 4.0 ⟹ 2/3; 4.64 ⟹ 2/3; 5.0 ⟹ 2/3. **The certified value drops steeply from ~1 to 2/3 as
m₄ runs from 28/9 to 10/3; only candidates with m₄ < 10/3 beat 2/3.**

**Reading (the m₄-dependence made concrete):** the extremal world {2/3 simples, 1/6 doubles} has trace
moments (1, 4/3, 2, 10/3) — its FOURTH moment 10/3 saturates all four Gram moments simultaneously, so at
m₄ = 10/3 the 4th-moment certificate cannot exclude it and the certified value is exactly 2/3 (the method's
sharpness, C §7.5(b)). The paper's 13/4 < 10/3 *excludes* the extremal world at the 4th moment — the
separation is a fourth-moment phenomenon (consistent with `attack-hankel-test.md` §0: "the separation shows
up at the FOURTH moment"). If the m₄ adjudication resolves to 346/105 the roadmap degrades to 0.6882 (still
> 2/3); to 10/3 or 4.64 it collapses to 2/3; to 13/4 it stands at 13/18. **The 13/18 claim must carry the
qualifier "conditional on m₄ = 13/4" until the adjudication closes.**

---

## 3. Conditional statement (b): RH + uniform HL on [1, A] ⟹ the 0.70/0.80/0.90 roadmap

**Hypothesis set (explicit):** (i) RH; (ii) uniform Hardy–Littlewood on [1, A]: the pair-correlation
second moment can be evaluated at bandwidth λ = A, equivalently F(α) = 1 for 1 ≤ α ≤ A (Montgomery's
conjecture / HL prime pairs; C §7.5(a) names this as the required input beyond λ = 1). This is the
value-territory input that M29's unconditional side cannot supply (MV bound 3.6·10³–3.7·10⁴× over
tolerance, PROVEN) [m29].

**Statement (M2 model, CHECKED NUMERICALLY):** the certificate at bandwidth A certifies N^s₀/N ≥ p₁(A) with
p₁(A) = 1 − (1−p₀)/A², in particular:

| A (F-support) | certified p₁(A) | roadmap target |
|---|---|---|
| 1.04 | 0.705833 | 0.70 (rel err +0.83%) |
| 1.26 | 0.799590 | 0.80 (−0.05%) |
| 1.70 | 0.889906 | 0.90 (−1.12%) |

**Pricing attribution:** this is the only positive-priced input on the pricing sheet: dv\*/dA = 0.636343/A³
(0.5657 at A = 1.04, 0.3181 at A = 1.26, 0.1295 at A = 1.70). A single-point *value* δ at 1+ε is priced at
only ~8.5·10⁻⁴ per unit δ (M3 model) — the wrong unit; the RANGE [1, A] is what pays. The Remark roadmap
(0.70/0.80/0.90 at 1.04/1.26/1.70) is PROVEN-as-stated in C (Remark 1.1); its numerical instantiation here
is the M2 model, whose exact curve needs the private config LP (CONJECTURED-as-exact).

**Honest label:** the implication "RH + F ≡ 1 on [1,A] ⟹ N^s₀/N ≥ p₁(A)" is a legitimate, labeled
conditional result: the mechanism (pair-correlation data at bandwidth A feeds the certificate's second
moment; v\* = p₁(A) + |E(1)|, shadow price 1) is PROVEN (lpdual, pricing); the input is CONJECTURED
(Montgomery/HL value territory); the exact p₁(A) curve is model-dependent (M2, CHECKED NUMERICALLY).

---

## 4. Literature-map update (task item 3)

Added to `research/notes/literature-map.md` §4(a) (new item 3): **"The beyond-1 input, precisely named
[B1-R]** — the canonical conjectural beyond-1 target is the FG twisted pair correlation F_n (Fazzari–
Gerspach, arXiv:2412.20099) + Conj 1.5: the additive-correlation object behind C §7.5(f)'s HL*. FG Prop 1.7
(RH only) proves F_n in-bandwidth; FG Thm 1.9 (RH + Conj 1.8 uniform HL) evaluates the smoothed
F_n(α;ψ_U) = min{1, (logT/Λ(n))(α−1+logn/logT)} + O(loglogT/Λ(n)) on 1−logn/logT ≤ α ≤ 2−48logn/logT — the
strongest documented conditional statement in the library. Label: CONJECTURED as input (RH + Conj 1.8 are
hypotheses); the conditional theorems are PROVEN-as-stated given their hypotheses."

---

## 5. Status paragraph: the FG twisted route (the strongest documented conditional statement in the library)

**What it is.** Fazzari–Gerspach (arXiv:2412.20099, held and read: `paper-thirdmoment-pcc.md` + the extracted
text) is the first rigorous treatment of the **twisted pair correlation** F_n — the exact additive-correlation
object (prime power × zero) that `attack-ceiling.md` §3/§4 names as the only documented route past the
bandwidth-one walls and that C §7.5(f)'s HL\* encodes. Two conditional theorems (both VERIFIED-FROM-PAPER):
- **Prop 1.7 (RH only — no correlation conjecture):** for n = qᵃ ≤ T^{1−ε}, F_n(α) = T^{−2α}(logT + logT/n² +
  O(1)) − r₁(α,n) + O(1/logT) on 0 < α < 1 − logn/logT − δ_T, and the conjugate range −logn/logT ≤ α ≤ 0;
  full range −1+δ_T < α < 1 − logn/logT − δ_T by symmetry. *In-bandwidth, RH-only.*
- **Thm 1.9 (RH + Conj 1.8, uniform Hardy–Littlewood):** for the smoothed F_n(α;ψ_U) (U = (logT)² smoothing),
  uniformly in n and in 1 − logn/logT ≤ α ≤ 2 − 48logn/logT:
  **F_n(α;ψ_U) = min{1, (logT/Λ(n))(α−1+logn/logT)} + O(loglogT/Λ(n))** — the exact beyond-1 shape: a ramp to
  the plateau 1, the twisted analogue of min{|α|,1} (Conj 1.5's m_n(α) = 1 for α ≥ 1−logn−Λ(n)/logT; the 48 is
  technical, Remark 9.5). The classical analogue: Montgomery suggested F(α) ~ 1 for 1 ≤ α ≤ 2−δ under HL;
  Bolanz proved 1 ≤ α ≤ 3/2−δ; Goldston–Gonek the full range (FG p. 7).

**Status.** The twisted route is **conditional all the way down**: Thm 1.9's hypothesis set is RH + Conj 1.8,
and Conj 1.8 is a Hardy–Littlewood-strength conjecture — the same strength family as PCC beyond 1 — so it does
NOT supply the unconditional input the certificate's pricing sheet demands (the FUND criterion of
`attack-ceiling.md` §3.6 is not met; the 0.6818 and 5/6 ceilings stand). Prop 1.7 is the strongest *RH-only*
statement of this type in the library; Thm 1.9 is the strongest *RH + one conjecture* statement. **Value:**
(i) it documents, for the first time, the exact conjectured shape of the beyond-1 additive-correlation object
(the plateau 1; the n-prime identity Λ(n)/logT·m_n(α) = H*(α, Λ(n)/logT) with the triple correlation — "we
believe this to be of independent interest"); (ii) it is the concrete realization of the hypothesis behind
conditional statement (a) (HL\*'s additive correlations) and (b) (F ≡ 1 on [1,A]) — the roadmap inputs now
have a named, readable, provable-conditional target; (iii) its β-integral cancellation with the triple
correlation (Thm 1.1's assembly) cross-validates the RMT normalization (c_P = (1/8)a'''(0) to 60 digits, c_Z =
−π²/4, verified in `paper-thirdmoment-pcc.md` §1.1).

**Bottom line:** the FG twisted route is the canonical conjectural beyond-1 target and the strongest
documented conditional statement in the library — a *shape*, proven conditional on RH + HL, that the
certificate program can price (positive: 0.6363/A³) but cannot yet buy. M29's unconditional negative stands
PROVEN. Any future unconditional input of this shape re-opens the roadmap at the stated price without
re-running this analysis [pricing §9].

---

## 6. Epistemic status (labels per claim)

| Claim | Label |
|---|---|
| p₀ = 0.6818286874638315 (= exact rational 10909258999421303588095230195816054408197/(16·10³⁹), diff 0.00e+00); |E(1)| = 2.5431315104·10⁻⁶ | **CHECKED NUMERICALLY** (json + exact rational agree) |
| v\*(p₁) = p₁ + |E(1)|, shadow price of p₁ = 1; anchor 0.681831230595342; re-verified at p₁ = 0.70/0.80/0.90 (residual 0.00e+00) | **PROVEN** (attack-lpdual) + **CHECKED NUMERICALLY** (LP, this run) |
| M2 curve p₁(A) = 1 − (1−p₀)/A² at A = 1.04/1.26/1.70 → 0.705833/0.799590/0.889906 (Remark rel err ≤ 1.12%); bandwidths 1.0298/1.2613/1.7837 for 0.70/0.80/0.90 | **CHECKED NUMERICALLY** (model eval; reproduces pricing §5, f1curve §4) |
| price dv\*/dA = 0.636343/A³ (0.5657/0.3181/0.1295 at 1.04/1.26/1.70) | **CHECKED NUMERICALLY** (M2 derivative) |
| moments m_k(1) = 1, 4/3, 2, 13/4 (k ≤ 4); Hankel D₁,D₂,D₃ > 0 | **CHECKED NUMERICALLY** (from C §7.5(f)'s values; positivity verified) |
| Λ₂(0) = 5/36 exactly from the Christoffel min-problem (minimizer 1 − 7x/4 + 2x²/3); Λ₁(0) = 1/4 consistency with Lemma 3.3 (n₊ ≥ 3/4 = F(1), 2F(1)−1 = 1/2) | **CHECKED NUMERICALLY** (exact fractions, this run; framework from C §7.5(d)) |
| 13/18 = 2·(31/36) − 1 = 26/36, 31/36 = 1 − 5/36 | **PROVEN arithmetic** (this run; the derivation chain from C §7.5(d),(f) + Prop 4.5) |
| "RH + HL\*(4,λ) ⟹ N^s₀/N ≥ 13/18" | **PROVEN-as-stated in C** (conditional; hypotheses CONJECTURED about ζ) |
| m₄-dependence curve: 13/4→13/18; 346/105→0.688172; 10/3→2/3 exactly; 4.64→2/3 (4-mom 0.533875); 28/9→degenerate boundary; 3.07→invalid (D₃ < 0) | **CHECKED NUMERICALLY** (this run; the candidate values from the catalog [tm §4.3, hankel §5, chem F4]) |
| "RH + F ≡ 1 on [1,A] ⟹ roadmap 0.70/0.80/0.90 at 1.04/1.26/1.70" | **conditional, labeled** (mechanism PROVEN; input CONJECTURED [M29]; exact p₁(A) curve model-dependent) |
| FG Prop 1.7, Thm 1.9, Conj 1.5, Conj 1.8 statements | **VERIFIED-FROM-PAPER** (`paper-thirdmoment-pcc.md`; re-verified against the extracted text in this session) |
| M29: every proven beyond-1 bound fails by 3.6·10³–3.7·10⁴× | **PROVEN negative** [m29] (cited, not re-derived here) |
| Which m₄ candidate is the true 4th Gram moment | **OPEN / under adjudication** (the deciding computation is the direct 3D-diagram integral; catalog §2) |

**Weakest links (justification chain, explicit):** (i) the exact p₁(A) curve needs the private config LP
(same blocker as f1curve/enclok; M2 is the documented model); (ii) the 13/18 value inherits the m₄ = 13/4
candidate — the m₄ adjudication is the single load-bearing number of conditional statement (a); (iii) the
CMS-bound framework (n₊/d ≥ 1 − Λ_m(0)) is taken from C §7.5(d) and validated here by the m=1/Lemma 3.3
consistency check — the general-m theorem itself is the paper's, not re-derived; (iv) both conditional
inputs (HL\*, uniform HL) are conjectural about ζ — this is the documented content of the conditional
program, not a hidden assumption.

---

## 7. Definition of done (per the catalog brief #7)

- [x] Written conditional-input certificate (≥ 13/18 under HL\*(4,λ), with the verified arithmetic and the
  m₄-dependence flagged); the 0.70/0.80/0.90 roadmap under F ≡ 1 on [1,A] with A = 1.04/1.26/1.70 — each
  with its hypothesis set and the pricing attribution (v\* = p₁(A) + |E(1)|, price 0.6363/A³).
- [x] F_n + Conj 1.5 recorded in the literature map as the canonical conjectural beyond-1 target
  (`literature-map.md` §4(a) item 3).
- [x] Status paragraph on the FG twisted route (the strongest documented conditional statement in the
  library) — §5 above.
- [x] Every number code-verified (script + command in §8; companion `beyond1-conditional-program.py` saved
  alongside this note).

---

## 8. Reproduction

- Code: `research/notes/beyond1-conditional-program.py` (self-contained; the certificate LP reuses the
  pricing-sheet class, `attack-pricing-sheet.py`, untouched — no canonical tool was edited; the exact-
  fraction Christoffel and LP sections are new).
- Run:
  ```
  cd /home/vstaln/riemann && uv run --quiet --with numpy --with scipy --with mpmath python \
      research/notes/beyond1-conditional-program.py
  ```
- Data: `tools/lpdual/law_data.json` (p₀, E₁, s_mid — cached, no network). Primary statements re-read in
  this session from `research/papers/claude-riemann-paper.txt` (§7.5(d),(f); Prop 4.4/4.5; Lemma 3.3) and
  `research/papers/fg-2412.20099.txt` (Prop 1.7, Thm 1.9, Conj 1.5, Conj 1.8).
- Sources: `attack-pricing-sheet.md` (prices), `attack-f1curve.md` (M2/M3 curves), `attack-m29.md`
  (unconditional negative), `attack-lpdual.md` (v\* = p₁ + |E(1)|), `paper-thirdmoment-pcc.md` (FG
  extraction), `attack-vector-catalog-3.md` #7 (brief, DoD), `attack-multiplicity.md` §4 + `attack-ceiling.md`
  §7.5(f)-note + `attack-hankel-test.md` (m₄ status, 28/9 threshold), `attack-twobandwidth.md` (extremal
  world (1, 4/3, 2, 10/3)), `literature-map.md` (updated §4(a) item 3).

*Persistence note:* this closes B1-R as a written, code-verified conditional program, not as a stop. The
roadmap's two inputs (HL\*, uniform HL) remain conjectural (M29); the m₄ adjudication is now demonstrated to
be load-bearing for the 13/18 value and should be closed by the direct 3D-diagram integral (catalog M4 lane);
the α ≈ 1.0–1.3 empirical feature (≥ 11σ, cause unidentified) is the live empirical hint near this boundary
[catalog #10]. The search persists (hooks/agents.md).
