# Paper extraction: Fazzari–Gerspach (arXiv:2412.20099) — third moment of log ζ and the twisted pair correlation

**Agent:** EXECUTIONER (paper extraction / range mapping; s4h applied: strategy-intelligence, epistemology, constraint-hardness-testing)
**Date:** Round 3
**Source:** `research/papers/fg-2412.20099-third-moment-twisted-pcc.pdf` (50 pp; text now at `research/papers/fg-2412.20099.txt`, extracted with `uv run --with pypdf --quiet python tools/pdf2txt.py <pdf> <txt>`; tool `tools/pdf2txt.py`).
**Task:** extract everything bearing on the P2 lane (third moment m₃(λ) / twisted correlations past the bandwidth-1 walls).

**Verdict up front (for the P2 orchestrator):**
- **NO — this paper does NOT provide an unconditional third-moment value at λ ∈ {1/2, 2/3}.** Its only unconditional third-moment content is the pure-prime-power piece at λ ≤ 1/3 (Prop 3.1), and its headline full third moment `M₃^ℜ = c_P + c_Z + O(1/log T)` is **conditional on RH + pair-correlation + triple-correlation + twisted-pair-correlation conjectures** (Thm 1.1).
- **The input P2 actually needs is already in hand:** `m₃(1/2) = 5`, `m₃(2/3) = 13/4` were proven in `attack-twobandwidth.md` (three independent verifications). This paper neither adds nor contradicts them.
- **PARTIAL for the "twisted quantity that could translate" (the M29 / beyond-bandwidth-1 lane):** the paper is the first rigorous treatment of the twisted pair correlation `F_n` — the exact additive-correlation object `attack-ceiling.md` §3/§4 names as the only documented route past the walls — and it proves it **under RH only** in-bandwidth (Prop 1.7) and **under RH + a uniform Hardy–Littlewood conjecture** beyond α = 1 (smoothed, Thm 1.9). Conditional, so it does **not** break the 0.6818 / 5/6 ceilings; but the *shape* of the conjectured beyond-1 twisted correlation is now precisely documented.
- **Recommended next step:** do **not** fund a translation agent for an unconditional input (nothing to translate — the needed λ = 1/2, 2/3 values already exist in-house). Instead (a) flag this paper to the running third-moment agent (Section 8), (b) record `F_n` + Conj 1.5 as the canonical conjectural target for the beyond-1 lane with its now-documented conditional proofs, and (c) optionally fund a **conditional-input certificate** line (a documented RH-conditional result is still a result per the hooks), using Prop 1.7/Thm 1.9 as the input source.

All claims about the paper's content are labeled **VERIFIED-FROM-PAPER** (read in the extracted text, page cited). All numbers are **CHECKED NUMERICALLY** with `tools/fg_cp_cz_verify.py` (`uv run --with mpmath --quiet python tools/fg_cp_cz_verify.py`).

---

## 1. The main theorems (verbatim, normalized for extraction artifacts)

### 1.1 Theorem 1.1 — the headline (VERIFIED-FROM-PAPER, p. 3)

> **Theorem 1.1.** Assume RH, the pair and triple correlation Conjectures 1.2 and 1.3, and the "twisted pair correlation" Conjecture 1.5. Then we have
> `M₃^ℜ(T) := (1/T)∫_T^{2T} (ℜ log ζ(1/2+it))³ dt = c_P + c_Z + O(1/log T)`   (1.4)
> and
> `M₃^ℑ(T) := (1/T)∫_T^{2T} (ℑ log ζ(1/2+it))³ dt = O(1/log T)`.   (1.5)

with (VERIFIED-FROM-PAPER, p. 3)
`c_Z := −π²/4`,  `c_P := (3/4) Σ_{p,m≥2} (1/(m p^m)) Σ_{k+ℓ=m} 1/(kℓ)`,
and the identifications `c_Z = (1/8)M'''_N(0)` (RMT factor), `c_P = (1/8)a'''(0)` (arithmetic factor), where `M_N(s) = E|Z(U,θ)|^{2s}` is the Keating–Snaith unitary-matrix moment and `a(s) = Π_p (1−1/p)^{s²} Σ_{m≥0} (Γ(s+m)/(m!Γ(s)))² p^{−m}`.

**CHECKED NUMERICALLY** (`tools/fg_cp_cz_verify.py`):
- `c_P = 0.233631072236959` (Pmax=2000, Mmax=60; the identity `Σ_{k+ℓ=m}1/(kℓ) = 2H_{m−1}/m` verified for m=2..12);
- `c_Z = −π²/4 = −2.467401100272340`;
- `c_P = (1/8)a'''(0)` **to 60 digits** (|c_P − (1/8)a'''(0)| = 2.2e-60 at matched truncation) — the paper's internal identification is CORRECT;
- `M'''_N(0) → −2π²` (numerically `−2π² + 6/N + O(1/N²)`: −19.140, −19.619, −19.709, −19.732 at N = 10, 50, 200, 800; limit −19.7392), confirming `c_Z = (1/8)M'''_N(0)`;
- the conditional full third moment `c_P + c_Z = −2.233770028035381`;
- Prop 3.1's finite-x diagonal `S(x) = Σ_{p^γ≤x, γ≥2} (1/(γp^γ)) Σ_{α+β=γ} 1/(αβ) → (4/3)c_P = 0.311508` (S(10⁶) = 0.311469, converging);
- second-moment constant of (1.3): `γ + 1/2 + (1/2)Σ_{p,m≥2}(1−m)/(m²p^m) = 0.989099049639`.

> **Epistemology note (adjudicated with code):** my first hand-check suggested `c_P = (1/8)a'''(0)` was off by a factor 6 (third-derivative vs third-coefficient slip: the s³ coefficient of `binom(s+m−1,m)²` is `2H_{m−1}/m²`, so `a'''(0) = 6·Σ_p Σ_m 2H_{m−1}/(m²p^m)`). The code shows the paper's identification is exactly right. Per the hooks: the suspect was my check, not the source. **Label: paper claim VERIFIED-FROM-PAPER + CHECKED NUMERICALLY; my initial check REFUTED-by-code.**

### 1.2 The correlation conjectures the theorem consumes (VERIFIED-FROM-PAPER, pp. 4–6)

- **Conjecture 1.2 (Pair Correlation, Montgomery):** `((T log T)/2π)^{-1} Σ_{T≤γ,γ'≤2T} r(γ̃−γ̃') = ∫ r̂(a)(δ(a) + min{|a|,1}) da + O(1/log T)` for r with ĥ... `r̂` Lipschitz + integrable. (Full-range: conjectural beyond |α| = 1.)
- **Conjecture 1.3 (Triple Correlation, Hejhal):** kernel `H(a,b) = H_δ(a,b) + H*(a,b)` with
  `H_δ = δ(a)δ(b) + δ(a)min{|b|,1} + δ(b)min{|a|,1} + δ(a+b)min{|a|,1}`,
  `H*(a,b) = 2G(a,b) + min{|a|,1} + min{|b|,1} + min{|a+b|,1} − 2`,
  `G(a,b) = max{(1/2)(2 − |a| − |b| − |a+b|), 0}`.
  The paper states this is the Fourier transform of the 3-dimensional sine-kernel determinant, computed explicitly by Hejhal (p. 4, citing [RS96, Thm 4.1] and [Hej94, (11)]).
- **The twisted pair correlation** (pp. 5–6): for n a prime power,
  `F_n(α) := −((T/2π)Λ(n)√n)^{-1} Σ_{T≤γ,γ'≤2T} n^{iγ} T^{iα(γ−γ')} ω(γ−γ')`,  ω(x) = 4/(4+x²).
  **Conjecture 1.4 (Strong):** for n ≤ T^{1−ε},
  `F_n(α) = T^{−2α}(logT + logT/n² + O(1)) − r_1(α,n) + O(1/logT)` on (0, 1−logn/logT);
  `= T^{2α}(logT+O(1)) + (logT+O(1))/(nT^α)² − r_2(α,n) + O(1/logT)` on [−logn/logT, 0];
  `= min{1, (logT/Λ(n))(α − 1 + logn/logT)} + O(1/logT)` on [1−logn/logT, ∞);
  with explicit `r_1, r_2` (small "spikes" near integer multiples of Λ(n)/logT).
  **Conjecture 1.5 (integrated form):** for r ∈ C(ℝ) (r̂ Lipschitz, r̂′ ≪ |a|⁻³),
  `−((T/2π)Λ(n)√n)^{-1} Σ_{T≤γ,γ'≤2T} n^{iγ} r(γ̃−γ̃') = ∫ (r̂(α) + r̂(−α−logn/logT))/2 · (δ(α) + m_n(α)) dα + O(E_n)`,
  with `m_n(α)` the explicit piecewise function (1 on (−∞, −1−Λ(n)/logT]; linear ramp on [−1−Λ(n)/logT, −1]; 0 on [−1, 1−logn/logT]; linear ramp on [1−logn/logT, 1−logn−Λ(n)/logT]; 1 on [1−logn−Λ(n)/logT, ∞)). **Note the plateau m_n = 1 for α ≥ 1 − logn−Λ(n)/logT — the twisted analogue of min{|α|,1} beyond 1.** For n prime, `(Λ(n)/logT)·m_n(α) = H*(α, Λ(n)/logT)` — the exact cancellation mechanism with the triple correlation ("we believe this to be of independent interest").
- **Conjecture 1.8 (uniform Hardy–Littlewood):** `Σ_{m≤x} Λ(m/n)Λ(m±h) = (S_n(h)/n)x + O_ε(x^{1/2+ε})` uniformly for 1 ≤ h, n ≤ x^{1−ε}, with the singular series S_n(h) = δ((n,h)=1)·S(nh).

### 1.3 The supporting results (VERIFIED-FROM-PAPER)

- **Prop 1.6:** Conj 1.4 ⇒ Conj 1.5 (convolve F_n against a kernel, split the α-range into the five pieces of Conj 1.4). Proven in §7.
- **Prop 1.7 (RH only — no correlation conjecture):** for n = q^a ≤ T^{1−ε}, 0 < α < 1 − logn/logT − δ_T (δ_T = 10 loglogT/logT):
  `F_n(α) = T^{−2α}(logT + logT/n² + O(1)) − r_1(α,n) + O(1/logT)`;
  and for −logn/logT ≤ α ≤ 0: `F_n(α) = T^{2α}(logT+O(1)) + (logT+O(1))/(nT^α)² − r_2(α,n) + O(1/logT)`.
  Symmetry F_n(α) = F_n(−α − logn/logT) gives the full range **−1 + δ_T < α < 1 − logn/logT − δ_T**. Proof (§8) uses Montgomery's explicit formula (Lemma 8.1, "Assume RH") + Landau–Gonek (Lemma 2.2, "Assume RH"). **So "unconditional" in the abstract = "assuming only RH, free of the correlation conjectures" — NOT unconditional in the program's sense. Flag this reading (abstract p. 1 vs Prop 1.7 p. 7).**
- **Theorem 1.9 (RH + Conj 1.8):** for the smoothed `F_n(α;ψ_U)` (U = (logT)² smoothing, §1 (1.10)) and uniformly in n, α:
  `F_n(α;ψ_U) = min{1, (logT/Λ(n))(α − 1 + logn/logT)} + O(loglogT/Λ(n))` on **1 − logn/logT ≤ α ≤ 2 − 48 logn/logT**.
  **Remark 9.5:** the 48 is technical (worst error term from [GG98, Cor 2]); with better shift-uniformity in Conj 1.8 (η > 1/2 in GG98's notation) one may get α up to ≈ 2 − 3 logn/logT on n ≤ T^β. So the beyond-1 twisted correlation is captured in the smoothed form under RH + uniform HL.

### 1.4 How Theorem 1.1 is assembled — the (P+Z)³ decomposition (VERIFIED-FROM-PAPER, §2–§6)

Under RH, for 2 ≤ x ≤ T: `ℜ log ζ(1/2+it) = P(t) + Z(t) + O(√x/(t log²x))` (Prop 2.4), where
`P(t) = Σ_{n≤x} Λ(n)cos(t logn)/(√n logn) · f(logn/logx)` (length-x prime-power polynomial; f from [LMQH23]) and
`Z(t) = −Σ_γ h((γ−t)logx) + ĥ(0)log(t/2π)/(2π logx)` (zero sum; f,g,h defined in (2.8)). Then `M₃^ℜ = (1/T)∫(P+Z)³ dt` + error (Selberg CLT bounds the error). The four pieces (x = T^β, β = log x/log T = **the λ-scale**):

| Piece | Object | Hypothesis | x-range (= λ-range) | Value |
|---|---|---|---|---|
| Prop 3.1 | P³ (three prime powers) | **none** | x ≤ T^{1/3} (**λ ≤ 1/3**) | c_P + O(1/log x) |
| Prop 3.2 | P³ (imag. part) | none | x ≤ T^{1/3} | O(1/log x) (odd cancel) |
| Prop 4.1/4.2 | P²Z (two primes + one zero) | RH | x ≤ T^{1/4} (**λ ≤ 1/4**) | O(1/log x) |
| Prop 5.1 | PZ² (one prime + two zeros) | RH + **Conj 1.5** (twisted PCC) | x ≤ T^{1/3} | (1/2)∫₀^β (g(b/β)/β − 1/b)L(b) db + O(1/log x) |
| Prop 5.2 | PZ² (imag. part) | RH + Conj 1.5 | x ≤ T^{1/3} | ≪ 1/log x |
| Prop 6.1 | Z³ (three zeros) | RH + Conj 1.2 + Conj 1.3 | x ≤ T | −π²/4 − (3/2)∫₀^β (g(b/β)/β − 1/b)L(b) db + O(1/log x) |
| Prop 6.2 | Z³ (imag. part, odd h) | RH + Conj 1.3 | x ≤ T | ≪ 1/log x |

**The β-integral cancels** between 3·(Prop 5.1) [coeff 3/2] and (Prop 6.1) [coeff −3/2] — the paper's "twisted pair correlation cancels with the triple correlation contribution in the expected way" (p. 6). Sum at any β ≤ 1/4: `M₃^ℜ = c_P − π²/4 + O(1/log x)`, β-independent → Theorem 1.1.

---

## 2. Mapping to our setting (paper object ↔ our m₃/P2 object)

| Paper object | Our object (from `attack-twobandwidth.md`, `attack-ceiling.md`) | Relationship |
|---|---|---|
| β = logx/logT (truncation scale of the log's Dirichlet polynomial) | λ (window scale of the Gram matrix G(λ), G_ij = sinc(πλ(x_i−x_j))) | Same role: the length scale of the third-moment probe. **Normalizations differ** (paper: (1/T)∫ over t ∈ [T,2T]; ours: (1/N)E tr G³ over the sine process). |
| P³ piece at β (Prop 3.1): the pure prime-power diagonal `ab = c` | our m₃(λ) diagonal-method/DPP evaluation at scale λ | Sibling computations of "the third moment at scale λ". Paper's unconditional range **λ ≤ 1/3** (they state "we have not attempted to maximise the range of x", p. 19); ours reaches **λ = 1/2 (kλ=1.5<2) and the boundary λ = 2/3** (PROVEN in `attack-twobandwidth.md`). So the paper is *weaker* in range than our in-house diagonal method. |
| M₃^ℜ = c_P + c_Z (full third moment of ℜ log ζ, Thm 1.1, conditional) | — | The β-independent limit. NOT our m₃(λ) (ours is λ-dependent: 5, 13/4, 2 at λ = 1/2, 2/3, 1). Related as the full-log vs Gram-moment siblings; the paper's value −2.2338 is conditional and is *not* an input to our certificate. |
| c_P (arithmetic constant) | the arithmetic part of our m₃ | VERIFIED identical to (1/8)a'''(0); self-consistent with Prop 3.1. |
| c_Z = −π²/4 = (1/8)M'''_N(0) | the RMT part of the KS prediction | **CHECKED NUMERICALLY** (M'''_N(0) → −2π²). Independent confirmation of the KS normalization we use. |
| Conj 1.3's H(a,b) (Hejhal/RS96 triple correlation) | the ρ₃ = det[sinc]₃ triple-correlation kernel in our DPP m₃(λ) | The paper states H is the Fourier transform of the 3-dim sine-kernel determinant ([RS96, Thm 4.1], [Hej94]) — **the same RMT triple correlation our m₃(λ) assumes.** Consistency cross-check, VERIFIED-FROM-PAPER. |
| **F_n(α) twisted pair correlation** (n prime power) | the beyond-bandwidth-1 / M29-type additive-correlation input (`attack-ceiling.md` §3.6, §4 FUND: "a proven estimate for the additive correlation Σ_m (Λ∗Λ)(m)(Λ∗Λ)(m+h), h ≤ X²/T") | **The paper's genuinely new object.** F_n IS the arithmetic prime-power × zero interaction. Proven under RH in-bandwidth (Prop 1.7) and under RH + uniform HL beyond 1 (Thm 1.9, smoothed). Conditional — but the first rigorous documentation of the exact shape (Conj 1.4/1.5) of this object. |
| m_n(α) = 1 for α ≥ 1−logn−Λ(n)/logT (Conj 1.5) | beyond-1 F(α) data (the thing the ceiling says would fund a breakthrough) | The twisted analogue of `min{|α|,1}` beyond 1. Conditional (conjectured; partly proven under RH/HL). Does **not** provide unconditional beyond-1 data for Montgomery's F itself. |

---

## 3. Range check: does the paper cover λ = 1/2 or λ = 2/3?

**No — on both counts, unconditionally and conditionally.**

| λ needed by P2 | Paper's coverage at that λ | Verdict |
|---|---|---|
| λ = 1/2 (kλ = 1.5 < 2) | Paper's unconditional P³: λ ≤ 1/3 only. P²Z: λ ≤ 1/4 (RH). PZ²: λ ≤ 1/3 (RH + twisted PCC). No piece reaches λ = 1/2. | **NOT COVERED by the paper.** (Already proven in-house: m₃(1/2) = 5, `attack-twobandwidth.md` §2.) |
| λ = 2/3 (kλ = 2, RS boundary) | Same: no piece reaches λ = 2/3. | **NOT COVERED by the paper.** (Already proven in-house: m₃(2/3) = 13/4.) |
| any λ (full third moment) | Only via Thm 1.1, i.e., **conditional on RH + Conj 1.2 + Conj 1.3 + Conj 1.5**. | CONDITIONAL only. The value c_P + c_Z = −2.2338 is not an unconditional input. |

**Precise gap:** the paper provides no *unconditional* third-moment information at any λ > 1/3, and its full-moment statement is conjectural (RH + three correlation conjectures). For our purposes this gap is **vacuous** — the λ = 1/2 and λ = 2/3 values P2 needs are already PROVEN in-house with a *stronger* range than the paper's diagonal method, and the paper's conditional full moment is a different (β-independent) object.

---

## 4. Scan: form factor beyond α = 1, variance, simple zeros, derivative tower

- **Form factor beyond α = 1:** the paper's only beyond-1 content is for the **twisted** F_n, not Montgomery's F: the conjectured plateau m_n(α) = 1 for α ≥ 1 − logn−Λ(n)/logT (Conj 1.5) and the RH + uniform-HL evaluation of the smoothed F_n(α;ψ_U) = min{1, (logT/Λ(n))(α−1+logn/logT)} on 1−logn/logT ≤ α ≤ 2−48logn/logT (Thm 1.9). For F itself the paper only *cites* the classical conditional literature: Montgomery suggested F(α) ~ 1 for 1 ≤ α ≤ 2−δ under HL; Bolanz proved it for 1 ≤ α ≤ 3/2−δ; Goldston–Gonek in the full range (p. 7). **No unconditional beyond-1 F data.** VERIFIED-FROM-PAPER.
- **Variance (Goldston–Montgomery):** no new results. (1.3) cites Goldston 1987 (ℑ², RH + PCC) and LMQH23 (ℜ²); the second moment enters the proof only as an error bound via Selberg's CLT (Prop 2.4 proof). VERIFIED-FROM-PAPER.
- **Simple zeros:** none. The only "simple" occurrences are "simple poles" of a Mellin-transform factor A_q(s) in the twisted-correlation machinery (p. 12) — unrelated to simple zeros of ζ. VERIFIED-FROM-PAPER.
- **Derivative tower (ξ′, FGL-type):** none. "Derivative test" occurrences are oscillating-integral bounds. VERIFIED-FROM-PAPER.

---

## 5. Verdict

**Q: does the paper provide the unconditional third-moment input P2 needs (m₃ at λ ∈ {1/2, 2/3})?**
**NO.** The paper's unconditional content (Prop 3.1) stops at λ ≤ 1/3, weaker than the in-house diagonal method; its headline full third moment is conditional on RH + three correlation conjectures; and it covers no λ ∈ {1/2, 2/3} at all. **This creates no gap** — the needed values m₃(1/2) = 5, m₃(2/3) = 13/4 are already PROVEN in `attack-twobandwidth.md` (the paper neither confirms nor contradicts them, being a different object).

**Q: is there a twisted quantity that could translate?**
**PARTIAL.** The twisted pair correlation F_n is exactly the M29/beyond-bandwidth-1 additive-correlation object named in `attack-ceiling.md` as the only documented route past the walls, and this paper is the first rigorous treatment of it — but its proofs are **conditional**: RH only in-bandwidth (Prop 1.7), RH + uniform HL beyond 1 (smoothed, Thm 1.9). Conj 1.8 (uniform HL) is a Hardy–Littlewood-type conjecture — the same strength family as PCC beyond 1 (per `attack-ceiling.md` §3.6 and the paper's own Bolanz/GG98 citations) — so it does **not** satisfy the attack-ceiling FUND criterion ("unconditional, or conditional on a hypothesis strictly weaker than the pair-correlation conjecture"). **The 0.6818 and 5/6 ceilings stand; classification of the "no unconditional beyond-1 input" constraint remains HARD** (constraint-hardness re-test: source = technical impossibility in the proven literature, unchanged by this paper; the paper adds conditional data, not unconditional).

**Epistemic status of the paper's claims** (s4h-epistemology applied): all statements I quote are VERIFIED-FROM-PAPER; all constants I computed are CHECKED NUMERICALLY (script cited); the paper's abstract phrase "unconditionally" is CONFIRMED-by-reading to mean "conditional only on RH", which I flag explicitly (Section 1.3) — a plain reading would overstate it.

---

## 6. Recommended next step

1. **Flag to the third-moment agent (primary).** The running third-moment agent (`attack-thirdmoment.md` lane, m3_* tools) should know: (a) arXiv:2412.20099 exists and computes the *full* third moment of ℜ log ζ **conditionally** (RH + PCC + TCC + twisted PCC) = c_P + c_Z = −2.2338; it does NOT touch the λ-truncated Gram-moment m₃(λ) at λ = 1/2 or 2/3; (b) its Conj 1.3 triple-correlation kernel H is the sine-kernel-determinant Fourier transform — the same RMT object our DPP m₃ uses, i.e., a normalization cross-check; (c) the paper's c_P = (1/8)a'''(0) and c_Z = (1/8)M'''_N(0) identifications are **verified numerically to 60 digits** — the KS normalization we use is consistent; (d) no conflict with m₃(1/2) = 5, m₃(2/3) = 13/4.
2. **Record F_n + Conj 1.5 as the canonical conjectural beyond-1 target** in the literature map (it is the precise object behind `attack-ceiling.md`'s FUND criteria), with its conditional proofs (Prop 1.7: RH-only in-bandwidth; Thm 1.9: RH + uniform HL beyond 1, smoothed) as the strongest rigorous statements of this type in the local library.
3. **Optional fund:** a *conditional-input certificate* line — using Prop 1.7/Thm 1.9 as inputs to a certificate whose hypotheses (RH + uniform HL) are stated explicitly and which is documented as a conditional result (a legitimate, labeled result per the hooks). This is a NEW line, not the unconditional P2 line.
4. **Do NOT fund** a translation agent for an unconditional λ ∈ {1/2, 2/3} third-moment input — nothing to translate; the values exist in-house.

---

## Label summary

- VERIFIED-FROM-PAPER: all theorem/conjecture statements quoted (Thm 1.1; Conj 1.2–1.5, 1.8; Props 1.6, 1.7, 2.4–2.5, 3.1–3.2, 4.1–4.2, 5.1–5.2, 6.1–6.2; Thm 1.9; Remark 9.5); the (P+Z)³ decomposition and the β-cancellation; the range limits (λ ≤ 1/3 unconditional, λ ≤ 1/4 RH, λ ≤ 1/3 RH+twisted, λ ≤ 1 RH+PCC+TCC); "no piece reaches λ = 1/2 or 2/3"; the abstract's "unconditionally" = RH-only; no simple-zeros / derivative-tower / new-variance content.
- CHECKED NUMERICALLY (`uv run --with mpmath --quiet python tools/fg_cp_cz_verify.py`, mpmath @60 digits): c_P = 0.233631072236959; c_Z = −π²/4; c_P = (1/8)a'''(0) to 2.2e-60; M'''_N(0) → −2π² (with 6/N correction term); c_P + c_Z = −2.233770028035381; S(x) → (4/3)c_P; second-moment constant 0.989099049639.
- REFUTED (by code): my own initial hand-check that c_P ≠ (1/8)a'''(0) (factor-6 slip: coefficient vs third derivative). The paper's internal consistency holds.
- CONJECTURED (in the paper, inherited): Conj 1.2/1.3/1.4/1.5/1.8 — the correlation inputs; the paper's conditional theorems are PROVEN (as conditional statements) given these.
- INCONCLUSIVE: none for this extraction; the "does F_n give us an unconditional input" question is settled NO (with the precise gap above).
- VERDICT: **NO** (unconditional m₃ at λ ∈ {1/2,2/3} — not provided, not needed, already in-house) + **PARTIAL** (twisted beyond-1 route now rigorously documented, conditional only).
