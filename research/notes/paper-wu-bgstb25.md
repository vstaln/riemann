# Paper reading: Wu (Dirichlet distinct/simple) + BGSTB25 (pair correlation I) + GS25 (critical line)

**Agent:** EXECUTIONER (paper-read / source-verification lane, feeding the real-constants audit and the distinct-zeros program).
**Task:** read the two held primary sources that had never been read (`wu-1206.1679-dirichlet-distinct-simple.pdf`, `bgst-2501.14545.pdf`), plus `gs25-2511.20059-zetazeros-criticalline.pdf`; state their main theorems verbatim; map onto our program; verdict on whether either moves the real lower bound or the distinct bound.
**Compute:** `scratch/wu_bgst_verify/verify.py` (final copy `research/notes/paper-wu-bgstb25-verify.py`). Command: `cd /home/vstaln/riemann && uv run --quiet --with scipy python scratch/wu_bgst_verify/verify.py` — ALL CHECKS PASS. Every number below labeled CHECKED NUMERICALLY came from that run.
**Labeling:** every claim about the papers' content is **VERIFIED-FROM-PAPER** (I read the full `.txt` extractions of all three, converted with pypdf; `bgst-2501.14545.txt` was already present). Where a number is additionally re-derived, it is **CHECKED NUMERICALLY** (script above). One claim (`Wu15` published-version identity) is **VERIFIED-VIA-CROSSREF** (online bibliographic lookup) and is flagged as such.

---

## 0. Executive finding (the headline for the audit)

**There are TWO distinct Wu papers, and the held one is NOT the source of the "0.6603" line.**

- `wu-1206.1679` (held, arXiv v4 Nov 2013; published as Quart. J. Math. 66 (2016), DOI 10.1093/qmath/haw039) — "Distinct zeros and simple zeros of **Dirichlet L-functions**": family-averaged results **0.8013 distinct / 0.60261 simple** (unconditional) and **0.83216 / 0.66433** (GRH). It does **NOT** contain 0.6603.
- `Wu15` as cited in the claude paper ([Wu15] = X. Wu, "Distinct zeros of the **Riemann zeta-function**", Quart. J. Math. 66 (2015), 759–771, DOI 10.1093/qmath/hav014) is a **separate paper** whose arXiv version is **arXiv:1206.3737** — **fetched and read in this session** (added to `research/papers/wu-1206.3737-distinct-zeros-zeta.pdf/.txt`). Its Theorem 1 is **Nd(T) ≥ 0.66036·N(T)** — VERIFIED-FROM-PAPER, and its §3 gives **Nξ′,c(T) ≥ 0.86957·N(T)** — VERIFIED-FROM-PAPER. So the claude paper's "0.6603 [Wu15]" and "0.86957 [Wu15, §3]" citations are **now verified against primary sources** (0.66036 matches to 4 decimals; 0.86957 exact). The bibliographic identity Wu15 = hav014 = Quart. J. Math. 66:759–771 is **VERIFIED-VIA-CROSSREF** (title, author X. Wu, vol/pages, 2015).

**Verdict (preview): NO movement on either program target.** Neither Wu nor BGSTB25 supplies an unconditional constant above what the claude paper already achieves (2/3, 0.6725, 5/6, 0.83625; Theorems B/C/D/E). Details in §5.

---

## 1. Wu, arXiv:1206.1679v4 (2013) — "Distinct zeros and simple zeros of Dirichlet L-functions" (family results)

VERIFIED-FROM-PAPER (read in full, 15 pp). All statements below are as printed; constants CHECKED NUMERICALLY.

**Setup.** Primitive χ (mod q), N(T,χ) = (T/π)log(qT/2πe) + O(log qT). Nd(T,χ), Ns(T,χ) count distinct / simple zeros with −T < γ ≤ T. Family averages: N(T,Q) = Σ_{q≤Q} Ψ(q/Q)/φ(q) Σ*_{χ} N(T,χ) (and Nd, Ns likewise), where Ψ ≥ 0 smooth compactly supported, Q ≥ 3, T ≥ 3. The method does **not** track zeros across different L-functions (a numerical coincidence ρ₁ = ρ₂ for χ₁ ≠ χ₂ counts as two family zeros).

**Theorem 1 (verbatim, unconditional).** "For Q and T with (log Q)^6 ≤ T ≤ (log Q)^A we have
Nd(T,Q) ≥ 0.8013·N(T,Q),  Ns(T,Q) ≥ 0.60261·N(T,Q),
where A ≥ 6 is any constant, provided Q is sufficiently large in terms of A."

**Theorem 2 (verbatim, GRH).** "Assume the Generalized Riemann Hypothesis. For Q and T with (log Q)^6 ≤ T ≤ (log Q)^A we have
Nd(T,Q) ≥ 0.83216·N(T,Q),  Ns(T,Q) ≥ 0.66433·N(T,Q),
where A ≥ 6 is any constant, provided Q is sufficiently large in terms of A."

**Method (the "Farmer's derivative combination" in modern form — VERIFIED-FROM-PAPER §2–§6).** Partition the critical strip into left (Re s < 1/2) and right (Re s ≥ 1/2).
- Left: G(s,χ) = ξ′(s,χ), ξ = H·L, H(s,χ) = ½s(s−1)(q/π)^{s/2}Γ((s + (1−χ(−1))/2)/2). Functional equation gives N_{ξ′,l} + N_{ξ′,l̄} = N − N_{ξ′,c}; key identity (11): **Nd(T,χ) + Nd(T,χ̄) ≥ N(T,χ) + N_{ξ′,c}(T,χ) − NG(D,χ) − NG(D,χ̄)**, and (12): Ns + Ns̄ ≥ 2N_{ξ′,c} − 2NG(D) − 2NG(D̄).
- Right: G(s,χ) = L(s,χ)ψ₁(s,χ) + λL′(s,χ)ψ₂(s,χ), λ = 1/(r log q), ψᵢ mollifiers with X = q^θ (0 < θ < 1), P₁(0)=P₂(0)=0, P₁(1)=P₂(1)=1; D = rectangle 1/2 − iT to 3 + iT.
- Averaging via the **Asymptotic Large Sieve** (Conrey–Iwaniec–Soundararajan): the mean-square of |G| on the σ₀-line (σ₀ = 1/2 − R/log q) is evaluated by (24), an asymptotic large-sieve lemma with the h_{i₁,i₂} kernel (41), giving with θ = 1−ε, r = 1.154, R = 0.617, P₁(x) = x − 0.158x(1−x) + 0.25x²(1−x), P₂(x) = x − 0.492x(1−x) + 0.075x²(1−x): c(θ,r,R) = 1.230108…, hence **(33) NG(D,Q) ≤ (1/(2R)·log c + o(1))N = 0.167835·N(T,Q)** (CHECKED NUMERICALLY: (1/(2·0.617))ln 1.230108 = 0.167830 ≈ 0.167835).
- ξ′-zeros on the line via Levinson's method generalized by Conrey: **(48) N_{ξ′,c}(T,Q) ≥ (1 − (1/R)log c₁ + o(1))N(T,Q)**, with θ = 1−ε, R = 0.746, δ = 0.771, P(x) = x − 0.482x(1−x) − 0.392x²(1−x) − 0.262x³(1−x), Q(x) = 1 − 0.673x + 0.369(x²/2 − x³/3) − 4.635(x³/3 − x⁴/2 + x⁵/5): **N_{ξ′,c}(T,Q) ≥ 0.93828·N(T,Q)**.
- Completion: Nd ≥ ½ + ½·0.93828 − 0.167835 = 0.801305 > 0.8013; Ns ≥ 0.93828 − 0.33567 = 0.60261 (CHECKED NUMERICALLY). GRH case: Nd ≥ 1 − 0.167835 = 0.832165, Ns ≥ 1 − 0.33567 = 0.66433 (CHECKED NUMERICALLY).

**Context stated in the paper (VERIFIED-FROM-PAPER, useful for the audit):**
- Farmer 1995: at least **63.952%** of zeros of ζ are distinct (combination method from proportions of simple zeros of ξ^(n)(s,1)). (1206.1679 p.1.)
- Bui–Conrey–Young 2011: more than **40.58%** of zeros of ζ are simple (Levinson + general mollifier). (p.1.)
- Cheer–Goldston 1993, on RH: more than **67.275%** of zeros of ζ are simple. (p.2.)
- Conrey–Ghosh–Gonek 1998, on RH + GLH: more than **84.56%** distinct and **70.37%** simple for ζ. (p.2.)
- Conrey–Iwaniec–Soundararajan: at least **58.65%** of zeros of the family of Dirichlet L-functions are on the critical line and simple. (p.2.)
- Remark (p.14): "Using Levinson's method, we may estimate the proportions for simple zeros of the family of ξ^(n)(s,χ), n ≥ 0, and then use Farmer's combination method as in [10] to get a lower bound for the proportion of distinct zeros only. However, the result obtained by this way is **much worse than Theorem 1**." — i.e. Wu himself confirms the derivative-combination route is the weaker one.

---

## 2. Wu, arXiv:1206.3737v2 (2012) — "Distinct zeros of the Riemann zeta-function" (= [Wu15], the ζ paper)

VERIFIED-FROM-PAPER (read in full, 9 pp; fetched this session). **This is the paper the claude paper cites as [Wu15] for the 0.6603 line.**

**Theorem 1 (verbatim).** "For T sufficiently large, we have Nd(T) ≥ 0.66036·N(T)." (Abstract: "more than 66.036% of zeros of the Riemann zeta-function are distinct.")

**Method.** Same partition as §1 but for ζ alone: left side G(s) = ξ′(s) with the additional-zeros count ≤ ½(N − N_{ξ′,c}) + O(log T); right side G(s) = ζ(s)ψ₁(s) + ζ′(s)ψ₂(s) with mollifiers of length y = T^θ, **0 < θ < 4/7** (the Conrey mollifier length). Identity (5): **Nd(T) ≥ ½N(T) + ½N_{ξ′,c}(T) − NG(D)**. Numerics (CHECKED NUMERICALLY):
- NG(D) ≤ **0.27442·N(T)** with θ = 4/7−ε, R = 1.023, P₁(x) = x − 0.064x(1−x) + 0.112x²(1−x), P₂(x) = 1.305x − 0.276x² − 0.025x³;
- N_{ξ′,c}(T) ≥ **0.86957·N(T)** (§3, Levinson-generalized-by-Conrey; θ = 4/7−ε, R = 1.104, δ = 0.869, P(x) = x − 0.274x(1−x) − 0.334x²(1−x) + 0.005x³(1−x), Q(x) = 1 − 0.609x − 0.572(x²/2 − x³/3) − 4.895(x³/3 − x⁴/2 + x⁵/5));
- Nd ≥ ½ + 0.434785 − 0.27442 = 0.660365 > 0.66036 (CHECKED NUMERICALLY).
- Also states (p.1): Farmer's method gives "at least 63.9%"; Conrey 1983: ≥ 81.37% of ξ′(s,1) zeros on the line; with the θ = 4/7−ε mollifier in Conrey's method, ≥ 82.402%.

---

## 3. BGSTB25 — arXiv:2501.14545v2 (Nov 21 2025), "Pair correlation of zeros of the Riemann zeta function I: proportions of simple zeros and critical zeros"

VERIFIED-FROM-PAPER (read in full, 16 pp). Same authors as BGSTB24. This is the paper our notes connect to the claude paper's Theorem 5.8 (= BGSTB24 Thm 1).

### 3.1 The unconditional form-factor statement (the key analytic input)

**(2.2)–(2.3), "Montgomery Theorem (MT)", verbatim.** With zeros counted with multiplicity,
F(x,T) := Σ_{ρ,ρ′: T<γ,γ′≤2T} x^{ρ−ρ′}·W(ρ−ρ′),  W(u) = 4/(4−u²).
"For x ≥ 1 and T ≥ 3, we have F(x,T) ≥ 0, F(x,T) = F(1/x,T), and
F(x,T) = (T/2πx²)·log²T·(1 + O(1/√logT)) + (T/2π)·log x + O(T√logT),
uniformly for 1 ≤ x ≤ T."

**The sum runs over ALL complex zeros ρ = β+iγ (real parts retained)** — that is the unconditional content: Montgomery's original assumed RH to drop the β's. The zero-side evaluation is reduced to an L²-norm via Lemma 1 ((3.4)–(3.5), residue integral); the prime side is Montgomery's [Mon73] computation via the explicit formula with the Korobov–Vinogradov zero-free region controlling the cross term (bound E₁ ≪ x^{1−2η(2T)}log³T, η(t) = c/(log t)^{2/3}(log log t)^{1/3}).

**Error-term correction (VERIFIED-FROM-PAPER, §2 footnote + §3).** The statement "has been modified from its original formulation in [BGSTB24], with two changes": (i) the sum is over (T, 2T] instead of (0, T]; (ii) "the error terms appearing above have been corrected from those in the original statement of the theorem" — the original had F = [(T/2πx²)log²T + (T/2π)log x]·(1 + O(1/√logT)), and "if, for example, x = c·log T, then … the factor of c on the T term is incorrect." The corrected O(T√logT), uniform over 1 ≤ x ≤ T, absorbs the lower-order terms. This correction is due to Ramūnas Garunkštis and Julija Paliulionytė. **"All the applications of Theorem 1 in [BGSTB24], such as Lemma 5 and Lemma 7, remain correct."** (Montgomery–Vaughan, to appear, have an RH-conditional refinement.)

### 3.2 Box-hypothesis results (the GS25/GS26 connection)

Box B_b := {s = σ+it : 1/2 − b/(2 log T) < σ < 1/2 + b/(2 log T), T < t ≤ 2T}. N(B_b) counts zeros in B_b (with multiplicity), N^s simple, N⁰ on the line, N^s_0 simple-and-on-the-line.

**Theorem 1 (verbatim).** "Assume that, for all sufficiently large T, all the zeros ρ = β+iγ of ζ(s) with T < γ ≤ 2T are in B_b. Then we have, where b → 0 as T → ∞,
(1.2) N^s(B_b) ≥ (2/3 + o(1))·N(B_b),
(1.3) N⁰(B_b) ≥ (2/3 + o(1))·N(B_b),
(1.4) N^s_0(B_b) ≥ (1/3 + o(1))·N(B_b)."
Remark 1: (1.3) is "the new result that the pair correlation method yields at least 2/3 of the zeros on the critical line" (pair correlation > Levinson under the box; Levinson is unconditional, pair correlation is not). Remark 2: (1.4) "is known unconditionally and was first proved independently by Heath-Brown [HB79] and Selberg (unpublished)".

**Theorem 2 (verbatim, fixed b).** "Assume that, for all sufficiently large T, all the zeros … are in B_b. Then as T → ∞, we have
N^s(B_{0.3185}) ≥ (0.66666908 + o(1))·(T/2π)logT,  N⁰(B_{0.3185}) ≥ (0.66666908 + o(1))·(T/2π)logT,  N^s_0(B_{0.3185}) ≥ (0.33333816 + o(1))·(T/2π)logT,
N^s(B_{0.001}) ≥ (0.67250064 + o(1))·(T/2π)logT,  N⁰(B_{0.001}) ≥ (0.67250064 + o(1))·(T/2π)logT,  N^s_0(B_{0.001}) ≥ (0.34500129 + o(1))·(T/2π)logT."
(The b = 0.001 constant **0.67250064 is the Montgomery–Taylor constant** 2 − (1/2 + 2^{−1/2}cot(2^{−1/2})) = 0.67250070…, CHECKED NUMERICALLY.) Table 1 shows deterioration with b (b=1: 0.61748; b=2: 0.47485; b=4.187: 0.00007); "the method ultimately fails when b ≥ 4.2 for (1.2) and (1.3) and when b ≥ 2 in (1.4)". Table 2 compares j_F vs j_M.

**Method (VERIFIED-FROM-PAPER §4–§7).** Tsang kernel K_b with K̂_b(t) = j(2πt)/cosh(2πbt) ((4.5)–(4.6)); Lemma 3: **Re K_b(x+iy) > 0 for all x and |y| < b** ((5.3), via the positive Fourier pair (5.1) — Lemma 2), and K_b(z) ≪ e^{|Im z|}/(1+|z|²) ((5.4)). Lemma 4: under the box, Σ_{ρ,ρ′∈B_b} Re K_b(−i(ρ−ρ′)logT) = (1/2π)(j(0) + 2∫₀¹ αj(α)/cosh(bα) dα + O(1/√logT))·(T/2π)logT, every term positive ((5.10); the W-weight is removable with error ≪ e^b T). The diagonal (ρ=ρ′) and **symmetric-diagonal (ρ′ = 1−ρ, off-line)** terms give (6.1); with j_F and b→0 this is the fundamental inequality
**(6.2) Σ_{T<γ≤2T} m_ρ + Σ_{T<γ≤2T, β≠1/2} m_ρ ≤ (4/3 + o(1))·(T/2π)logT.**
Since Σm ≥ N, the off-line multiplicity sum ≤ (1/3+o(1))N — that is how the method counts critical zeros. For fixed b, C_b(j) := [j(0) + 2∫₀¹ αj(α)/cosh(bα)dα]/[2∫₀¹ j(α)/cosh(bα)dα] ((7.1)) replaces 4/3, and (7.2): **N^s, N⁰ ≥ (2 − C_b(j) + o(1))·(T/2π)logT; Σ_{β≠1/2}m ≤ (C_b(j) − 1 + o(1))·(T/2π)logT; N^s_0 ≥ (3 − 2C_b(j) + o(1))·(T/2π)logT.** All constants CHECKED NUMERICALLY: C₀(j_F) = 4/3 exactly ⇒ 2/3, 2/3, 1/3; the b = 0.3185 row is exact (0.33333816 = 2·0.66666908 − 1); the b = 0.001 row agrees to 1e-8 (paper's 0.34500129 vs 2·0.67250064 − 1 = 0.34500128 — rounding of independently computed C_b; CHECKED NUMERICALLY, tolerance 1e-7).

---

## 4. GS25 — arXiv:2511.20059v2 (Feb 5 2026), "Zeta zeros on the critical line"

VERIFIED-FROM-PAPER (read in full, 9 pp). Goldston–Suriajaya. This is the "critical line" paper the task asked about — the box-hypothesis ⇒ 2/3 prior state.

**Theorem 1 (Montgomery, RH, restated):** at least 2/3 of the zeros of ζ are simple. Proof: (4.1) Fejér-kernel sum Σ_{ρ,ρ′: γ=γ′} 1 ≤ Σ[sin(½(γ−γ′)logT)/(½(γ−γ′)logT)]² = (4/3+o(1))·(T/2π)logT; under RH γ=γ′ ⇔ ρ=ρ′, so Σ m_ρ ≤ (4/3+o(1))N, and (4.5) simple ≥ 2N − Σm ≥ 2/3·N.

**The RH-free decomposition (5.1) — the structural heart (verbatim):**
Σ_{ρ,ρ′∈Z(T), γ=γ′} 1 = Σ_ρ m_ρ + Σ_{ρ: β≠1/2} m_ρ + Σ_{ρ,ρ′: β+β′≠1, γ=γ′} 1,
(diagonal + symmetric diagonal + non-symmetric horizontal terms). Without RH, γ=γ′ no longer implies ρ=ρ′ because of the pairs (β+iγ, 1−β+iγ).

**Theorem 2 (verbatim).** "Suppose there exists a constant C where 1 ≤ C < 2 and that, as T → ∞, Σ_{ρ,ρ′∈Z(T), γ=γ′} 1 ≤ (C+o(1))·(T/2π)logT. Then asymptotically at least the proportion 2−C of the zeros of ζ(s) are simple, and at least the proportion 2−C of the zeros of ζ(s) are on the critical line." (C ≥ 1 is forced by Σm ≥ N; C < 2 for positivity.) **This is exactly the statement the claude paper cites** ("[GS25, Theorem 2] … would give proportions ≥ 2−C of simple zeros and ≥ 2−C of zeros on the line, and that C = 4/3 would follow if the terms γ ≠ γ′ of the Fejér sum could be discarded, which requires a positivity that fails for zeros far from the line").

**Theorem 3 (verbatim).** Under Σ m_ρ + Σ_{β≠1/2} m_ρ ≤ (C+o(1))N: (i) simple-and-on-line ≥ 2−C; (ii) average of (simple proportion, critical proportion) ≥ (3−C)/2; (iii) proportion simple-or-critical-or-both ≥ (4−C)/3. Remark 2: at C = 4/3, (ii) gives average ≥ **5/6**, (iii) gives ≥ **8/9** (equivalently: proportion of multiple zeros off the critical line ≤ 1/9).

**Theorem 4 (BGSTB25, restated).** Under the box B_b (8.1), for b = 0.3185, at least 2/3 of zeros with T < γ ≤ 2T are simple and on the critical line.

**Theorem 5 (GLSS).** The Pair Correlation Conjecture implies asymptotically 100% of the zeros of ζ are simple and on the critical line — via "Essential Simplicity" (ES): Σ_{|γ−γ′| ≤ 2πλ/logT} 1 = (1+o(1))N as λ → 0, which is the C = 1 case. (GLSS25b: a form of the Alternative Hypothesis also implies ES.)

CHECKED NUMERICALLY: 2 − 4/3 = 2/3; (3−4/3)/2 = 5/6; (4−4/3)/3 = 8/9.

---

## 5. Mapping onto our walls (the three audit questions + the verdict)

### 5a. Does Wu's derivative combination give anything the paper's 5/6 distinct doesn't already beat?

**NO.** Numerically (CHECKED NUMERICALLY):

| Distinct-zeros source | Constant | vs paper's 5/6 = 0.83333 |
|---|---|---|
| Farmer 1995 (ζ) | 0.63952 | beaten |
| **Wu15 = 1206.3737 (ζ, Theorem 1)** | **0.66036** | **beaten (0.83333 > 0.66036)** |
| Wu16 = 1206.1679 (Dirichlet family, uncond Thm 1) | 0.8013 | beaten |
| Wu16 (Dirichlet family, GRH Thm 2) | 0.83216 | beaten — 5/6 exceeds it **even though C's Theorem E is unconditional** |
| paper C Theorem C (ζ), Theorem E (fixed primitive χ) | **5/6 = 0.83333** | — |

Simple zeros: Wu16 family 0.60261 (uncond) and 0.66433 (GRH) are both below the paper's unconditional 2/3 (Theorem B, fixed χ). So on every one of the four counts (distinct/simple × unconditional/GRH) the paper strictly dominates Wu. Wu's own Remark (1206.1679 p.14) confirms the pure derivative-combination route is "much worse than Theorem 1". VERDICT: derivative combination adds nothing to the distinct bound; the 5/6 wall stands.

### 5b. Does BGSTB25 give a sharper real-data p₁ bound than H(λ) = 2−1/λ−λ/3 at any λ, or a sharper form-factor error than the paper uses?

**NO on both.**

- **p₁ (simple-fraction) bound.** H(λ) = 2 − 1/λ − λ/3, maximised on [1/2, 1] at λ = 1 with H(1) = 2/3 (CHECKED NUMERICALLY). The paper's Theorem B attains 2/3 **unconditionally**. BGSTB25's content is (i) the unconditional MT — which is a second-moment *evaluation*, not a p₁ bound — and (ii) the box-conditional Theorem 1 (2/3, 2/3, 1/3) and Theorem 2 (0.67250064 at b = 0.001), which are **conditional on all zeros lying in the box B_b** (width b/log T). There is no λ at which BGSTB25 gives an *unconditional* p₁ improvement over H(λ). The 67.25% and 34.5% constants at b = 0.001 are precisely the constants the paper's Theorem D makes unconditional by replacing the box hypothesis with the rank–trace inequality. (For *real data* the box is verified up to 3·10¹² — Platt–Trudgian, as GS25 notes — but that is a finite verification statement, of a different type than the asymptotic certificate, and is not what the pricing sheet prices.)
- **Form-factor error.** The corrected MT (2.3) has error **O(T√logT) uniform over 1 ≤ x ≤ T** — this is the *canonical* form of the input the paper calls Theorem 5.8 (= BGSTB24 Thm 1, corrected per B25 §2). It does not beat anything the paper uses; it is the same evaluation, and its correction (from the flawed multiplicative (1+O(1/√logT)) error of BGSTB24) leaves all main terms and all applications unchanged. No constant anywhere changes. VERDICT: no movement; the correction is a citation-hygiene note for the real-constants audit (see §6).

### 5c. Any unconditional statement the pricing sheet mispriced?

**NO repricing.** The pricing sheet (`attack-pricing-sheet.md`) prices three hypothetical inputs: beyond-1 form-factor range (positive, dv*/dA = 0.6363/A³), third moment m₃ ≥ 2 (negative: caps p₁ ≤ 2/3), min-gap (negative: caps p₁ at the Parseval floor). BGSTB25's unconditional MT supplies the second-moment evaluation on the **bandwidth-1 range only** (1 ≤ x ≤ T ⇔ |α| ≤ 1), i.e. exactly the data the certificate already reads — it contains **no unconditional statement beyond α = 1**, so the pricing sheet's "beyond-1 = CONJECTURED [M29]" row stands. The box-conditional 67.25% does not touch the *unconditional* certificate class; under the box it is a different (stronger-hypothesis) statement the paper already replicates unconditionally. m₃ and min-gap rows: nothing in either paper changes the marked-configuration identities (m₃ = 4 − 3p₁, Parseval floor). VERDICT: no mispriced row.

### 5d. Bottom-line verdict

**NO — neither paper moves the real lower bound (2/3, 0.6725, 5/6, 0.83625) nor the distinct bound (5/6).**
- Wu tops out at 0.66036 (ζ distinct) / 0.8013–0.83216 (family) — all < 5/6.
- BGSTB25's 2/3 and 67.25% are box-conditional; its unconditional content (corrected MT) is the bandwidth-1 input the paper already uses.
- GS25 (box ⇒ 2/3; C<2 ⇒ 2−C) is the exact prior state the paper replaces with the rank–trace argument.
- The one genuinely new deliverable of this session is **source verification**: the "0.6603 [Wu15]" and "0.86957 [Wu15,§3]" citations are now verified against a primary source (arXiv:1206.3737), and the real-constants audit now knows the held `wu-1206.1679` is the *family* paper, not the ζ paper.

---

## 6. What each unlocks (program value)

1. **Wu15 (1206.3737), now held.** (a) Closes the "0.6603" verification gap in `literature-map.md` §1a (label upgrades from "PROVEN (as stated in C)" to PROVEN against a primary source). (b) The derivative-combination identity Nd ≥ ½N + ½N_{ξ′,c} − NG(D) is a **genuinely different attack on the distinct count** (Levinson/ξ′-based, not pair-correlation-based) — a cross-check route: any improvement of N_{ξ′,c} or NG(D) feeds the distinct bound through a mechanism unrelated to the 5/6 wall; it caps at 0.66036 for ζ today, so it is not competitive, but it is the right control for "is 5/6 an artifact of the pair-correlation route?" (c) The 0.86957 ξ′-on-line proportion equals the claude paper's own ξ′-results context (C Remark 7.3: "Wu [Wu15,§3] has 0.86957 unconditionally, which neither our 0.85838 nor our 0.86864 exceeds") — VERIFIED-FROM-PAPER, so that Remark's honesty claim is now source-checked.
2. **Wu16 (1206.1679).** (a) The family-averaged template: Asymptotic Large Sieve + ξ′/G-partition is the state of the art for Dirichlet families; the paper's 0.93828 (ξ′ zeros on the line, family) vs the claude paper's 0.85838/0.86864 (single ζ, flat/quartic windows) shows family averaging is *stronger* for ξ′ — a comparison datum for the ξ′-program. (b) Theorem E comparison: the claude paper's fixed-χ 5/6 distinct dominates the family 0.83216 even under GRH — this is worth stating explicitly wherever Theorem E is advertised.
3. **BGSTB25.** (a) The corrected MT (2.3) is the canonical citation for the paper's Theorem 5.8 prime-side input — replacing any reference to the un-corrected BGSTB24 statement. (b) The Tsang-kernel positivity lemma (Re K_b > 0 for |y| < b) and the symmetric-diagonal decomposition (6.2)/(5.1) are the exact machinery the paper's rank–trace Lemma 3.2 replaces — the "obstacle is termwise positivity off the line" claim (C §7.4) is now directly documented from the primary source. (c) The b = 0.001 row (67.25%, 34.5%) confirms the Montgomery–Taylor constant is the pair-correlation method's box-limit answer — matching C's Theorem D; any future claim that "the box gives more than the paper" is refuted by Table 1 (deterioration with b).
4. **GS25.** (a) Theorem 2 is the precise statement of the prior state C replaces (C < 2 ⇒ 2−C simple AND 2−C critical). (b) Theorem 3's 5/6-average / 8/9-either-or are the strongest "prior" statements on the simple/critical Venn diagram under the C = 4/3 hypothesis — the natural comparanda for the paper's 5/6 distinct and 0.83625. (c) Theorem 5 (PCC ⇒ 100% simple+critical; ES ⇔ C = 1) marks the conjectural ceiling: the "if the horizontal-diagonal terms could be dropped" limit is exactly C = 1, i.e. 100%.

---

## 7. Honesty labels and epistemic status

| Claim | Label |
|---|---|
| Wu16 (1206.1679) Theorems 1–2 verbatim; constants 0.8013/0.60261/0.83216/0.66433; intermediate 0.167835, 0.93828, 1.230108; method (ξ′-left + G-right + ALS averaging; P₁,P₂,Q,R,θ,δ,λ values) | **VERIFIED-FROM-PAPER** (read in full); arithmetic recomputed **CHECKED NUMERICALLY** (0.801305, 0.602610, 0.832165, 0.664330, 0.167830 vs printed 0.167835) |
| Wu15 (1206.3737 = Quart. J. Math. 66 (2015) 759–771, DOI 10.1093/qmath/hav014) Theorem 1: Nd ≥ 0.66036N; N_{ξ′,c} ≥ 0.86957N; NG(D) ≤ 0.27442N | **VERIFIED-FROM-PAPER** (arXiv version fetched and read this session); Nd = 0.660365 **CHECKED NUMERICALLY**; bibliographic identity **VERIFIED-VIA-CROSSREF** |
| The held 1206.1679 does NOT contain 0.6603; it is the Dirichlet-family paper | **VERIFIED-FROM-PAPER** (the abstract/intro contain only family results + Farmer 63.952% for ζ) |
| BGSTB25 MT (2.3) verbatim (range 1 ≤ x ≤ T, error O(T√logT)); correction of BGSTB24 (factor-of-c error, Garunkštis–Paliulionytė); all applications remain correct | **VERIFIED-FROM-PAPER** |
| BGSTB25 Theorems 1–2 verbatim; Tsang-kernel positivity; C_b(j) formula; (6.2); tables | **VERIFIED-FROM-PAPER**; C₀(j_F) = 4/3 ⇒ 2/3, 2/3, 1/3 **CHECKED NUMERICALLY**; b = 0.3185 row exact, b = 0.001 row to 1e-8 (rounding) |
| BGSTB25 0.67250064 = Montgomery–Taylor constant 2 − (½ + 2^{−1/2}cot(2^{−1/2})) = 0.67250070 | **CHECKED NUMERICALLY** |
| GS25 Theorems 1–5 verbatim; (5.1) decomposition; 2−C/2−C/(3−C)/2/(4−C)/3; 5/6 and 8/9 at C = 4/3 | **VERIFIED-FROM-PAPER**; 5/6, 8/9, 2/3 **CHECKED NUMERICALLY** |
| Verdict: no unconditional constant from Wu or BGSTB25 exceeds the paper's 2/3, 0.6725, 5/6, 0.83625; beyond-1 stays conjectural; pricing sheet unrepriced | **PROVEN-BY-ARGUMENT** (from the verified statements above; comparisons CHECKED NUMERICALLY) |
| C's "0.6603 [Wu15]" and "0.86957 [Wu15,§3]" citations are accurate | **VERIFIED-FROM-PAPER** (0.66036, 0.86957) — closes the gap flagged in `literature-map.md` §5 |
| Platt–Trudgian verification to 3·10¹² (all zeros on line, simple) | **VERIFIED-FROM-PAPER** (as stated in GS25 §1; the underlying computation not re-run here) |

**Known limits of this reading.** (i) `.txt` extractions are pypdf/poppler text pulls; a few glyphs (√, superscripts, the j_M kernel formula (4.3)/(4.4)) are garbled — the j_M closed-form constant was therefore verified only via the Montgomery–Taylor formula, not via the printed kernel; the literature map flagged the same issue. (ii) Wu15 was read in its arXiv v2 (1206.3737v2, 18 Sep 2012); the published Quart. J. Math. version is identical in content per Crossref/abstract but was not itself read. (iii) No claim here asserts anything about the *truth* of the papers' theorems beyond what they state — VERIFIED-FROM-PAPER means the statement is accurately quoted, and every quoted constant is internally consistent (script).

**Blockers encountered (documented):** `pdftotext` unavailable on this machine → used pypdf (`uv run --with pypdf`). arXiv API (`export.arxiv.org`) initially rate-limited/redirecting → used https + Crossref + Semantic Scholar for the Wu15 bibliographic identity and the 1206.3737 fetch. None blocked the deliverable.

---

## 8. Files touched / created

- `research/papers/wu-1206.1679-dirichlet-distinct-simple.txt` (created from held PDF; conversion only).
- `research/papers/gs25-2511.20059-zetazeros-criticalline.txt` (created from held PDF; conversion only).
- `research/papers/wu-1206.3737-distinct-zeros-zeta.pdf` + `.txt` (**new primary source fetched**: the actual [Wu15] ζ paper).
- `scratch/wu_bgst_verify/verify.py` + final copy `research/notes/paper-wu-bgstb25-verify.py` (all numeric claims).
- This note: `research/notes/paper-wu-bgstb25.md`.

*Sources read in full: `wu-1206.1679-dirichlet-distinct-simple.txt`, `wu-1206.3737-distinct-zeros-zeta.txt`, `bgst-2501.14545.txt`, `gs25-2511.20059-zetazeros-criticalline.txt`, `claude-riemann-paper.txt` (Wu citations, §1.2/§7.3/refs), `literature-map.md`, `attack-pricing-sheet.md`.*
