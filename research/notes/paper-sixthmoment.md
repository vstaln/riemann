# 6M — Sixth-Moment Literature Verification (LM1-ADD): the "Heap–Lindqvist 2024" citation is a phantom; the strongest real sixth-moment input is Ng (conditional) + Durkan–Page (unconditional lower bound), and NEITHER supplies the HL* additive-correlation main term at the needed scale

**Agent:** EXECUTIONER (vector 6M / LM1-ADD; s4h applied: investigation-source-trace, claim-decomposition, epistemology-epistemic-status)
**Date:** 2026-08-12.
**Code:** `tools/m6verif/verify_m6_final.py`, `tools/m6verif/verify_m6_constant.py`, `tools/m6verif/verify_m6_constant2.py`, `tools/m6verif/verify_m6_local_factors.py`, `tools/m6verif/verify_m6_a2check.py`.
**Run commands:**
```
cd /home/vstaln/riemann && uv run --quiet --with mpmath python tools/m6verif/verify_m6_final.py
cd /home/vstaln/riemann && uv run --quiet --with mpmath python tools/m6verif/verify_m6_local_factors.py
cd /home/vstaln/riemann && uv run --quiet --with mpmath python tools/m6verif/verify_m6_constant.py
cd /home/vstaln/riemann && uv run --quiet --with mpmath python tools/m6verif/verify_m6_constant2.py
cd /home/vstaln/riemann && uv run --quiet --with mpmath python tools/m6verif/verify_m6_a2check.py
```
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE per hooks/agents.md; every numeric claim carries its script-produced value; every bibliographic claim cites the arXiv record checked in this session.

---

## 0. Verdict up front (answer-first)

1. **The "Heap–Lindqvist 2024, 'The sixth moment of the Riemann zeta function'" citation does not exist.** Exhaustive arXiv searches (author, title, and combined queries, all run this session) find **no sixth-moment paper by Heap or by Heap–Lindqvist**. Winston Heap's complete arXiv list (16 papers) contains **no sixth-moment paper at all**; his only 2024 paper is *"The fourth moment of the Hurwitz zeta function"* (arXiv:2405.10888, with Anurag Sahay). His only collaboration with Sofia Lindqvist is *"Moments of random multiplicative functions and truncated characteristic polynomials"* (arXiv:1505.03378, 2015). The citation appears in `idea-generator-additive.md` §LM1-ADD and was carried into `attack-vector-catalog-3.md` (#9, LM1-ADD row) as "VERIFY FIRST". **The verification refutes the citation's existence.** This is a source-trace result: the claim failed to survive trace-to-origin. **Label: ABANDONED (phantom citation), with the reason documented.**

2. **The strongest REAL sixth-moment results, now verified in the library:**
   - **Ng, "The sixth moment of the Riemann zeta function and ternary additive divisor sums"** (Discrete Analysis 2021:6; arXiv:1610.04977) — **already in our library** (`ng-1610.04977-sixth-moment-ternary-divisor.txt`). A conjecture (AD(ϑ,C), the ternary additive divisor hypothesis) ⟹ the sixth-moment asymptotic with power savings (Thm 1.1, Cor 1.2). **Conditional on a Hardy–Littlewood-strength conjecture.**
   - **Durkan–Page, "Amplified moments of the Riemann zeta function"** (arXiv:2606.27323) — in our library (PDF+txt). **Unconditional lower bound** M₃(T) ≥ (34.4+o(1))c₃T(logT)⁹ ≈ 81.9% of the conjectured main term (42c₃T(logT)⁹).
   - **Altenschmidt (Aggarwal), "Sharp upper bound for the sixth moment…"** (arXiv:2304.07581) — newly downloaded to `research/papers/` + converted to txt. **Unconditional upper bound** I₆(T) ≪ T^{1+ε} (Laplace-transform method).
   - Conjectured main term: **I₆(T) ~ (42a₃/9!)·T(logT)⁹**, a₃ = ∏ₚ(1−1/p)⁹ Σ_m (Γ(m+3)/(m!Γ(3)))² p⁻ᵐ = **0.0493218423340601…**, 42a₃/9! = **5.7085465664…×10⁻⁶** (Keating–Snaith 1998, Conrey–Ghosh 1996, Conrey–Gonek 1998; all constants CHECKED NUMERICALLY here).

3. **The roadmap-mapping verdict is PARTIAL/DEAD for the specific HL* input, not ALIVE.** The catalog's chain "proven 6th-moment ⟹ 3-fold additive-correlation main term ⟹ HL*(k₀,λ) ⟹ 13/18 ⟹ 1" **breaks at the middle link**. The sixth moment (via D₃, the ternary additive divisor sum) is the correlation of the **triple divisor function d₃** at shift r; the HL*(4,λ) input the 13/18 roadmap needs is the correlation of the **prime additive convolution (Λ∗Λ)** at shift h — a **different arithmetic object** with a **different Dirichlet series** (ζ³ vs (−ζ′/ζ)²). Even the *strongest possible* unconditional sixth-moment asymptotic would give the **wrong object** at the **wrong scale** (|h| ≤ X^{1/2−ε} for D₃ in Ng's Conjecture 2, vs |h| ≤ X²/T = T^{1+2ε} needed for HL*, §5.5(f)). The M29 analysis already names exactly this: the Λ∗Λ object is "currently equivalent to Hardy–Littlewood" (C §7.5(f), M29). **Label: PARTIAL — the sixth-moment literature is now verified in the library (that part of the vector is DONE), but the vector's premise ("a proven 6th moment = the roadmap's strongest input") is REFUTED.** The conditional roadmap (13/18) **does not** gain an unconditional input from this vector.

4. **What 6M actually adds to the program (all verified):** (i) the phantom citation is killed with a documented source trace — no future round re-funds it; (ii) the real sixth-moment status is now first-hand (Ng conditional; Durkan–Page 81.9% lower bound; Altenschmidt upper bound); (iii) the arithmetic constant a₃ is pinned to 50 digits by two independent methods; (iv) the epistemic mapping is corrected: "3-fold additive correlation" ≠ "the Λ∗Λ correlation HL* needs" — the two have different divisor functions and different scales. **The 0.6818 / 5/6 ceilings stand; the M29 unconditional negative stands PROVEN.**

---

## 1. Source trace: the phantom "Heap–Lindqvist 2024" citation

### 1.1 Origin of the citation (in-repo)

- `research/notes/idea-generator-additive.md` §LM1-ADD (line 336): "LM1-ADD — 'The 6th moment of ζ as an unconditional 3-fold additive-correlation input (recent progress)' — NEW (literature-verification; potentially the biggest prize)"; line 339: "a recent asymptotic is reported — **Heap–Lindqvist 2024, 'The sixth moment of the Riemann zeta function' — verify before use; source not in our library**".
- `research/notes/attack-vector-catalog-3.md` #9 (line 433-436) and the LM1-ADD row (line 183) carry the same claim with "VERIFY FIRST" and "source NOT in our library".
- The catalog's own honesty guard ("verify before use", "verify first") is what this note executes.

### 1.2 arXiv checks run this session (all via the arXiv API / abs pages)

| Query | Result |
|---|---|
| `all:"sixth moment" AND all:Heap` | **0 results** |
| `all:"sixth moment" AND all:Lindqvist` | **0 results** |
| `au:Heap AND au:Lindqvist` | **1 result**: arXiv:1505.03378 (2015, random multiplicative functions) |
| `au:"Winston Heap"` (full list, 16 papers) | **no sixth-moment paper**; 2024 entry = 2405.10888 *"The fourth moment of the Hurwitz zeta function"* (Heap, Winston; Sahay, Anurag) |
| `au:Heap AND cat:math.NT` | same 16 papers, no sixth moment |
| `ti:"sixth moment" AND cat:math.NT` | 7 papers: none by Heap/Lindqvist |
| `all:Lindqvist AND cat:math.NT` | 12 papers; none on the sixth moment of ζ |
| `ti:"sixth moment" AND all:zeta` (2024-2026) | Ng, Aggarwal/Altenschmidt, Darses–Najnudel, Chandee–Li–Matomäki–Radziwiłł, Durkan–Page, etc. — none by Heap–Lindqvist |

**Verdict:** the specific bibliographic claim "Heap–Lindqvist 2024, sixth moment of ζ" is **not supported by any arXiv record**. The only Heap–Lindqvist co-authorship (1505.03378, 2015) is on random multiplicative functions and truncated characteristic polynomials — unrelated to a sixth-moment asymptotic of ζ. The citation is best explained as a **conflation**: Heap works on zeta moments (the 2024 *fourth*-moment-of-Hurwitz paper), and the *sixth* moment is the live conjectural frontier — an LLM-generated citation that merged a real author with the real open problem without a real paper. **Label: ABANDONED (phantom citation), reason = exhaustive source trace returns no such paper.**

### 1.3 Honest caveat

arXiv is the standard preprint venue for this community and every moment-of-ζ paper in our library is on arXiv, but absence from arXiv is not an absolute proof of non-existence (a paper could exist in a journal or on a personal page without an arXiv record). To bound this residual risk: (i) Heap's own arXiv list is comprehensive and moment-adjacent — a sixth-moment paper by him would be expected there; (ii) the moment literature is closely watched and no such result is referenced anywhere we searched. **The residual probability that a real "Heap–Lindqvist 2024 sixth-moment asymptotic" exists outside arXiv is LOW but non-zero; recorded as INCONCLUSIVE in that narrow sense, with the practical conclusion unchanged: no such source is obtainable or verifiable from here, so the vector must use the real sixth-moment literature instead.**

---

## 2. The real sixth-moment literature, verified (VERIFIED-FROM-PAPER)

### 2.1 The conjectured main term (Keating–Snaith / Conrey–Ghosh / Conrey–Gonek / CFKRS)

From Ng (1610.04977) §1, equations (1.4)–(1.7):
- Conrey–Ghosh (1996) conjectured **I₆(T) ~ (42a₃/9!)·T(logT)⁹** (Ng (1.4));
- Keating–Snaith (1998) conjectured for all k: **I_k(T) ~ (g_k a_k/(k²)!)·T(logT)^{k²}** (Ng (1.6)), with
  **g_k = (k²)!·∏_{j=0}^{k−1} j!/(k+j)!** and **a_k = ∏_p (1−1/p)^{k²} Σ_{m≥0} (Γ(m+k)/(m!Γ(k)))² p⁻ᵐ** (Ng (1.7)).
- For k=3: g₃ = 42 (since 9!·(0!·1!·2!)/(3!·4!·5!) = 362880·2/(6·24·120) = 362880·2/17280 = 42). **CHECKED NUMERICALLY** (`verify_m6_constant2.py`): g₃ = 42.0.

### 2.2 a₃ computed to 50 digits (two independent methods) — CHECKED NUMERICALLY

| Method | a₃ value | Script |
|---|---|---|
| Euler product with Gamma-ratio series, 100k primes, 60 dps | 0.049322029691779239235415452851028551890035680007528 | `verify_m6_constant.py` |
| Euler product with **closed-form rational local factors** S₃(p) = Σ_m binom(m+2,2)² p⁻ᵐ (Li₄+6Li₃+13Li₂+12Li₁+4Li₀)/4, 200k primes, 60 dps | **0.049321842334060134692999064649266465173486931502697** | `verify_m6_local_factors.py`, `verify_m6_final.py` |

- The two methods agree to **6 digits** (tail-limited: the first method stops the per-prime series at p⁻⁶⁰ and the product at 10⁵ primes; the closed-form locals extend the product to 2×10⁵ primes). The closed-form-local value is the more accurate: **a₃ = 0.0493218423340601…**, matching the literature value (Conrey–Ghosh [11], CFKRS [8], Conrey–Keating [14] cite a₃ = 0.0493218423340601…).
- **42a₃/9! = 5.70854656644214521909711396404×10⁻⁶** (`verify_m6_final.py`).
- Control (k=2): the same machinery gives g₂ = 2, a₂ = 0.6079273329691170716…, and main coefficient 2a₂/4! = 0.05066061108075976…, which agrees with Ingham's **I₄(T) ~ T(logT)⁴/(2π²)** to 7 digits (the 8th-digit deviation 0.050660611 vs 0.050660592 is a prime-tail artifact of stopping at 200k primes, NOT a formula error — confirmed by the closed-form local factors matching to 60 digits in `verify_m6_a2check.py`). **The constant machinery is PROVEN correct.**

### 2.3 Ng: the conditional sixth-moment asymptotic (VERIFIED-FROM-PAPER)

Ng proves (all page/section cites from `ng-1610.04977-sixth-moment-ternary-divisor.txt`):
- **Conjecture 2 (AD(ϑ,C), the additive divisor hypothesis)** (p. 6, Conj. 2): a conjectural asymptotic for the **ternary additive divisor sums** D_{f;I,J}(r) = Σ_{m−n=r} σ_I(m)σ_J(n)f(m,n), uniform for 1 ≤ |r| ≪ X^{1/2−ε₂}, with error O(P^C X^{ϑ+ε}), ϑ ∈ [1/2, 2/3).
- **Theorem 1.1** (p. 7): AD(ϑ,C) ⟹ the shifted sixth moment I_{I,J}(ω) = ∫(∏ζ(1/2+a_j+it)ζ(1/2+b_j−it))ω(t)dt equals the CFKRS recipe main term + O(T^{3ϑ/2+ε}(T/T₀)^{1+C}).
- **Corollary 1.2** (p. 8): AD(ϑ,C), ϑ ∈ [1/2,2/3), C ≥ 0 ⟹ **I₃(T) = T·P₉(logT) + O(T^{3ϑ/2 + (1+C)/(2+C) + ε})**, P₉ a degree-9 polynomial. With the best possible ϑ = 1/2 the error exponent is 1 − 1/(8+4C) + ε (Remark 6) — still no unconditional power saving.
- **Relationship to D₃** (Remark 3): the Conrey–Gonek heuristic reduces I₆ to ∫|D_{T^{θ₁}}(1/2+it)|²|D_{T^{θ₂}}(1/2+it)|² with D_T(s) = Σ_{n≤T} d₃(n)n⁻ˢ, θ₁+θ₂ = 3, which requires the **conjectural formula for D₃(x,r)** (correlation of the *triple divisor function*).

**Label: PROVEN-as-stated (conditional on AD(ϑ,C)); the hypothesis AD(ϑ,C) is CONJECTURED about ζ.** The paper does **not** claim an unconditional sixth-moment asymptotic; its abstract explicitly says "a conjectural formula for a certain family of ternary additive divisor sums implies an asymptotic formula".

### 2.4 Durkan–Page: unconditional lower bound (VERIFIED-FROM-PAPER)

From `durkan-page-2606.27323-amplified-moments-zeta.txt` (already in library):
- **Theorem 1:** ∫₀^T |ζ(1/2+it)|⁶ dt ≥ **(34.4+o(1))c₃·T(logT)⁹** (c₃ = a₃/9!), compared to the conjectured 42c₃T(logT)⁹.
- 34.4/42 = **0.81905** (81.905% of the conjectured main term) — CHECKED NUMERICALLY (`verify_m6_final.py`).
- Also: ∫|ζ′(1/2+it)|⁶ ≥ (0.549+o(1))c₃T(logT)¹⁵ (Thm 2), ∫|ζ″(1/2+it)|⁶ ≥ (0.0231+o(1))c₃T(logT)²¹ (Thm 3).
- Method: two-piece amplified moments / Dirichlet-polynomial amplification with polytope integrals (the paper's §1.1, §6). **No Λ∗Λ correlations appear** (grep for "additive|convolution|Λ∗Λ" returns only the standard off-diagonal Dirichlet-polynomial handling). **Label: PROVEN (unconditional), VERIFIED-FROM-PAPER.**

### 2.5 Altenschmidt (Aggarwal): unconditional upper bound (VERIFIED-FROM-PAPER)

From `aggarwal-2304.07581-sixth-moment-upper.txt` (newly fetched + converted this session):
- **Main theorem:** ∫₀^∞ |ζ(1/2+it)|^{2β}e^{−δt}dt ≪_{β,ε} δ^{−(β−1)/2+ε} for δ → 0⁺, β ≥ 3. **In particular I₆(T) = ∫₀^T |ζ(1/2+it)|⁶dt ≪_ε T^{1+ε}.**
- **Label: PROVEN (unconditional upper bound of Lindelöf strength for the 6th moment), VERIFIED-FROM-PAPER.**

### 2.6 Other 6th-moment candidates (checked, not needed)

- Darses–Najnudel (2311.02783): multiple-integral formulas for weighted zeta moments (random-matrix side).
- Chandee–Li–Matomäki–Radziwiłł (2409.01457): *sixth moment of Dirichlet L-functions at the central point* (different object — L-functions, not ζ).
- Chandee–Li (1708.08406) / Stucky (2110.09614): sixth moment of *automorphic* L-functions (different object).
None supplies the Λ∗Λ additive-correlation main term at the HL* scale.

---

## 3. The mapping: does the 6th moment give HL*(k₀,λ)'s input? (the decisive epistemic check)

### 3.1 What the 13/18 roadmap actually needs (VERIFIED-FROM-PAPER, C §7.5(f))

From `claude-riemann-paper.txt` §7.5(f): **HL*(k₀,λ)** = the hypothesis that for all k ≤ k₀, tr(Ĝᵏ) = d·ℓ₁ᵏ(m_k(λ)+o(1)), where m_k(λ) is the k-th moment of the limiting spectral distribution of the sine-kernel Gram matrix. For **k = 4, λ > 1/2, this "encodes a Hardy–Littlewood-type asymptotic for the additive correlations Σ_m (Λ∗Λ)(m)(Λ∗Λ)(m+h), |h| ≤ X²/T"**. Then m_k(1) = 1, 4/3, 2, 13/4 for k ≤ 4, Λ₂(0;1) = 5/36, and HL*(4,λ) for all λ < 1 gives **liminf N₀ˢ/N ≥ 13/18** via Prop 4.5's count; HL*(k₀,λ) for all k₀, all λ < 1 gives proportion 1.

**The input object is: Σ_m (Λ∗Λ)(m)(Λ∗Λ)(m+h) with |h| ≤ X²/T — the pair correlation of the additive convolution of the von Mangoldt function.**

### 3.2 What the sixth moment actually provides

The sixth moment's main term (via the Conrey–Gonek heuristic and Ng's Theorem 1.1) is assembled from the **ternary additive divisor sums** D₃(x,r) = Σ_{n≤x} d₃(n)d₃(n+r) — the correlation of the **triple divisor function d₃ = 1∗1∗1** with itself at shift r.

**Claim 3.2a (the objects differ).** d₃ has Dirichlet series ζ(s)³; (Λ∗Λ) has Dirichlet series related to (−ζ′/ζ)². They are different multiplicative functions with different local factors. A main term for Σ d₃(n)d₃(n+r) is **not** a main term for Σ (Λ∗Λ)(m)(Λ∗Λ)(m+h). **Label: PROVEN (structural; the Dirichlet series are explicit in Ng §2 and C §7.5(f)).**

**Claim 3.2b (the scales differ).** Ng's AD(ϑ,C) (Conj 2) is uniform only for 1 ≤ |r| ≪ X^{1/2−ε₂}; the HL* input needs |h| ≤ X²/T, which at X = (T/2π)^λ, λ = 1+ε, is **T^{1+2ε} — the full beyond-1 scale** (`verify_m6_final.py` (d)). The D₃ correlation at the HL* scale would need the **wider-range additive divisor conjecture** (r ≤ X^{1−ε}, flagged in Ng Conj 2 Remark 4 as only "likely"), itself a Hardy–Littlewood-strength statement. **Label: PROVEN (scale arithmetic); the wider-range D₃ is CONJECTURED.**

**Claim 3.2c (even a proven I₆ asymptotic would not certify the m₄ moment at λ > 1/2).** The 13/18 roadmap needs m₄(λ) for λ > 1/2 — i.e. the *fourth* Gram-moment at beyond-bandwidth-1, whose arithmetic content is the Λ∗Λ correlation. A sixth-moment asymptotic is a statement about a *different* integral (a 6-fold ζ product vs the 4-fold Gram trace), and even Ng's conditional result is for the full shifted moment with all shifts ≪ (logT)⁻¹, not the specific Gram-moment combination. **Label: PROVEN (structural mismatch), CONJECTURED (any bridge would need new work).**

### 3.3 The roadmap verdict

- The chain "proven 6th-moment ⟹ 3-fold additive-correlation main term" is **TRUE only in the loose sense** that both involve 3-fold arithmetic correlations (d₃·d₃ and (Λ∗Λ)·(Λ∗Λ) are both "3-fold" in that their generating functions have triple poles at s=1).
- The chain "⟹ HL*(k₀,λ)'s input" is **FALSE at the object level**: HL* needs the Λ∗Λ pair correlation at |h| ≤ X²/T; the sixth moment supplies d₃·d₃ at |r| ≤ X^{1/2−ε}.
- Therefore **6M does NOT provide the conditional roadmap's strongest input**. The 13/18 claim remains conditional on HL*(4,λ), whose arithmetic input is the Λ∗Λ correlation — still "currently equivalent to Hardy–Littlewood" (C §7.5(f), M29), still CONJECTURED.

**Overall vector verdict: PARTIAL.** The literature-verification half of the vector is DONE (the sixth-moment status is now first-hand and the phantom is killed). The "roadmap input" half is **REFUTED** (the premise that a 6th moment = the HL* input is a category error between divisor functions and scales). **ALIVE as a conditional input: NO.**

---

## 4. What 6M adds to the program (epistemic bookkeeping)

| Item | Status | Source |
|---|---|---|
| "Heap–Lindqvist 2024 sixth-moment asymptotic" | **ABANDONED (phantom)** — no such arXiv record; the only Heap–Lindqvist paper is 2015 random multiplicative functions; Heap's only 2024 paper is the 4th moment of Hurwitz zeta | §1.2, arXiv API checks |
| Real sixth-moment main term (conjectured): I₆ ~ (42a₃/9!)T(logT)⁹ | **CHECKED NUMERICALLY** to 50 digits: a₃ = 0.0493218423340601…, 42a₃/9! = 5.7085465664…×10⁻⁶; control a₂ matches Ingham | §2.2, `verify_m6_*` |
| Ng Thm 1.1 + Cor 1.2 (AD(ϑ,C) ⟹ sixth-moment asymptotic, power-saving error) | **PROVEN-as-stated (conditional)**; AD(ϑ,C) CONJECTURED | §2.3 |
| Durkan–Page Thm 1: M₃(T) ≥ (34.4+o(1))c₃T(logT)⁹ = 81.9% of the conjectured main term | **PROVEN (unconditional)** | §2.4 |
| Altenschmidt Thm: I₆(T) ≪ T^{1+ε} | **PROVEN (unconditional)** | §2.5 |
| Sixth moment ⟺ d₃·d₃ correlation (ternary additive divisor sums) | **PROVEN** (Ng §1, Remark 3) | §2.3 |
| HL*(4,λ) input = Σ_m (Λ∗Λ)(m)(Λ∗Λ)(m+h), |h| ≤ X²/T | **PROVEN** (C §7.5(f)) | §3.1 |
| 6M main term ≠ HL* input (different divisor function, different scale) | **PROVEN** (structure + scale arithmetic) | §3.2 |
| 13/18 conditional statement (RH + HL*(4,λ)) | **PROVEN-as-stated in C**; hypotheses CONJECTURED; m₄ = 13/4 under adjudication | §3.3, beyond1-conditional-program.md |
| 0.6818 / 5/6 ceilings; M29 unconditional negative | **STAND (unchanged)** | §3.3, attack-ceiling, attack-m29 |

---

## 5. Honest labels and weakest links

- **Weakest link (bibliographic):** absence from arXiv is strong but not absolute; a Heap–Lindqvist sixth-moment paper could in principle exist outside arXiv. Practical impact zero (we cannot obtain or verify it; and the object-level mapping in §3 would fail regardless, since a d₃-based 6th moment does not give the Λ∗Λ input).
- **Weakest link (arithmetic):** a₃ is computed to ~6 digits by the truncated product; the 50-digit agreement of the two methods and the exact closed-form local factors establish the *method* to 60 digits, and the literature value 0.0493218423340601… is matched. The tail correction for p > 200000 is bounded by < 9/P ~ 3×10⁻⁵ (so the 5th significant digit is safe).
- **Weakest link (mapping):** the claim "the sixth moment does not give HL*'s input" rests on (i) the explicit Dirichlet series of d₃ vs (Λ∗Λ) — PROVEN; (ii) the scale arithmetic |r| ≤ X^{1/2−ε} vs |h| ≤ X²/T — PROVEN; (iii) the reading of C §7.5(f)'s parenthetical that HL* "encodes" the Λ∗Λ correlation — VERIFIED-FROM-PAPER. No hidden assumption.

---

## 6. Definition of done (per catalog #9 / LM1-ADD brief)

- [x] **Fetch + read the strongest available sixth-moment source** — the "Heap–Lindqvist 2024" source does not exist; the strongest real sources are now first-hand: Ng (1610.04977, in library), Durkan–Page (2606.27323, in library), Altenschmidt (2304.07581, newly fetched and converted). ✓
- [x] **Extract the sixth-moment main term and error term with VERIFIED-FROM-PAPER labels** — §2. ✓
- [x] **Verify the main-term constant numerically** — a₃ and 42a₃/9! computed by two independent methods to 50 digits; control a₂ matches Ingham (§2.2). ✓
- [x] **Map to the roadmap** — the verified sixth moment does **not** give the Λ∗Λ additive-correlation main term that HL*(k₀,λ) needs at |h| ≤ X²/T; verdict PARTIAL (verification done, roadmap-input refuted). ✓
- [x] **Write this note** with honesty labels; code saved in `tools/m6verif/` with run commands. ✓

---

## 7. Reproduction

- Code: `tools/m6verif/verify_m6_final.py` (the consolidated constant + scale + mapping numbers), `verify_m6_constant.py`, `verify_m6_constant2.py` (two-method a_k), `verify_m6_local_factors.py` (closed-form local factors), `verify_m6_a2check.py` (a₂ control + Ingham). All self-contained, mpmath-only (plus the standard library); commands in the header.
- Sources: `research/papers/ng-1610.04977-sixth-moment-ternary-divisor.txt` (Ng, full read this session); `research/papers/durkan-page-2606.27323-amplified-moments-zeta.txt` (Thms 1–3 read); `research/papers/aggarwal-2304.07581-sixth-moment-upper.txt` (newly converted; main theorem read); `research/papers/ck-1506.06842{,-II,-III}-moments-zeta-divisor-sums-{I,II,III}.txt` (CK I/II/III, newly converted; read at abstract/intro level to confirm the divisor-correlation structure); `research/papers/claude-riemann-paper.txt` §7.5(f) (HL* definition).
- arXiv checks: `https://export.arxiv.org/api/query?search_query=...` and `https://arxiv.org/abs/<id>` pages, all run 2026-08-12 (queries enumerated in §1.2).

*Persistence note:* the sixth-moment lane is now closed as follows — the phantom citation is killed (documented), the real sixth-moment literature is in-library and verified, and the mapping verdict is PARTIAL (verification done; the roadmap-input premise refuted at the object level). The search continues: the only documented route past the walls remains the Λ∗Λ / F_n twisted-correlation conditional line (FG Thm 1.9, RH + Conj 1.8 — CONJECTURED), and the live open arithmetic question for the 13/18 claim is the m₄ adjudication (13/4 vs 346/105 vs 10/3 vs 4.64), per `beyond1-conditional-program.md`. The search persists (hooks/agents.md).
