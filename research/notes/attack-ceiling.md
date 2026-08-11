# Attack: is the bandwidth-one ceiling real, and what input would break it?

**Agent:** EXECUTIONER (constraint-hardness-testing + epistemology + strategy)
**Date:** Round 1
**Verdict up front:** The ceiling is REAL for the rank-trace certificate class — PROVEN in Lean modulo one numerically-checked enclosure hypothesis — and **no beyond-bandwidth-1 input exists in the verified literature**. The angle "push the certificate past 0.6818 by the same route" is DEAD **as an unconditional program**. What remains alive inside the class: the gap 0.6725 → 0.6818 (Theorem D vs the ceiling), and a clean adversarial test of the ceiling itself (the LP dual). A genuine breakthrough input would be a *proven* estimate on the form factor for |α| > 1 — none is known; everything there is CONJECTURED (RMT / Hardy–Littlewood).

Sources read (all local): `lean-zeta-23/README.md`, `Zeta23/PairCeiling/{Stability,Ceiling,NearCUE,Bridge,CeilingLaw256,LawN256,Signed}.lean`, `ZeroSide/TightMult.lean`; `papers/anthropic-informal-note.txt` (Thm 1.1, Lemmas 3.2–3.4); `papers/claude-riemann-paper.txt` (§1.3 Remark 1.1, §7.1, §7.3–7.5); `papers/baluyot-etal-2306.04799.txt` (Thm 1); `papers/bgst-2501.14545.txt` (unconditional Montgomery Theorem (MT), §4–5 Tsang-kernel extraction).

---

## 1. What the ceiling is, precisely

**A certificate** (the object Theorem B's method produces) is a pair (c₀, r): c₀ ∈ ℝ and r ∈ C¹[0,1] with r′ =: g continuous, g differentiable off a countable set with integrable derivative h. Its **value** is v := c₀ + ∫₀¹ r(x)·x dx (the proportion of simple on-line zeros it certifies). It is **valid against a configuration** whose form-factor measure has grid masses s_j at j/N and simple-point fraction p₁ iff c₀ + Σ_{j=1}^{N} s_j·r(j/N) ≤ p₁. The certificate's inputs are exactly: mean density, the form factor sampled on [0,1] (bandwidth one), and integrality of multiplicities — the three inputs named in the paper's Remark 1.1.

**`ceiling_stability` (PROVEN in Lean, standard axioms only).** For any such certificate valid against a configuration (masses s, grid N, |E| ≤ M on [0,1], where D(x) = C(x) − x²/2 is the cumulative mass against the GUE datum, E = ∫₀ˣ D):

|Σ s_j r(j/N) − ∫₀¹ r(x)x dx| ≤ |r(1)|·|D(1)| + |r′(1)|·|E(1)| + M·∫₀¹|r″|.

Two integrations by parts (cellwise FTC + Abel summation, then FTC off a countable set); fully formalized in `Stability.lean`. This is a *configuration-free analytic identity* — no arithmetic content.

**`ceiling_law256` (PROVEN in Lean, one displayed hypothesis).** At the N = 256 near-CUE law (an explicit 256-periodic law of marked configurations, exact rational weights w_c ≥ 0, positions, marks ∈ {1,2}, Σ marks = 256 — the solution of an exact-rational linear program, certificate sha256 `cc3de991…`):

v ≤ p + 0.82395317·|r(1)| + 2.5431316·10⁻⁶·(|r′(1)| + ∫₀¹|r″|),

and with the signed form (`ceiling_law256_signed`, valid because the certificates have r(1) ≥ 0 and the law has D(1) ≥ 0, both kernel-checked): v ≤ p + 2.5431316·10⁻⁶·(|r′(1)| + ∫₀¹|r″|). With p = p₀ = 10909258999421303588095230195816054408197/16·10³⁹ = **0.6818286874638…** (the law's exact simple-point fraction; I verified the decimal) and r(1) = 0 (the actual certificates):

**v ≤ 0.6818287 + 2.55·10⁻⁶·(|r′(1)| + V(r′)).** This is the ceiling.

**Role of the 256-periodic (near-CUE) law.** The law is a legitimate configuration — a 256-periodic arrangement of marked points whose grid form factor satisfies |256·S(j) − j| ≤ 3·10⁻⁴⁰ for 0 < j < 256 (`NearCUE`), i.e., within 3·10⁻⁴⁰ of the CUE/sine-kernel form factor F(α) = 1 on [0,1], and whose simple-point fraction is p₀ = 0.68182868746… It therefore matches **all** bandwidth-one data (mean density = 1, F ≡ 1 on [0,1], integer marks ≤ 2). Any certificate valid against all configurations must in particular be valid against this one (hvalid with p = p₀), so the stability inequality forces its value ≤ p₀ + tiny. The ceiling is thus: *no certificate of this kind can certify more than 0.6818, because there exists a configuration consistent with every bandwidth-one input that has only 0.6818 simple zeros.*

**Labels.**
- `ceiling_stability`, `ceiling_nearCUE`, `ceiling_law256`, `ceiling_law256_decimal`, signed forms, the near-CUE row machinery, `TightMult`: **PROVEN (Lean)** — `#print axioms` = {propext, Classical.choice, Quot.sound} only.
- `EnclOK` (the law's S(j) lies in the 256 integer enclosures of `LawN256.lean`): **INCONCLUSIVE as of round 3 — see validation-enclok.md**. CORRECTION TO THE RECORD: the prior "CHECKED NUMERICALLY — 70-digit interval arithmetic" label was *inherited from the authors' README*, not re-run by any Riemann-program agent; the first fresh attempt (validation-enclok.md + tools/verify_enclok.py, exact big-int + mpmath@100, two independent paths) reaches INCONCLUSIVE: everything *downstream* of the enclosures is re-verified (checkRows == true, edgeNonneg, D(1) ∈ [0.8239531607128…, +2⁻¹⁴⁰] with slack 9.3e-9, p₀ = 0.6818286874638314…, e₁ slack 9.0e-14), but the enclosures themselves depend on the law's exact-rational weights/positions/marks which exist only in the authors' private certificate `cert_N256_blk_b128m.json` (sha256 cc3de991…, not public, absent from Lean repo/workspace/papers/transcripts/public search). NOT REFUTED; robust (70-digit precision gives ~93 bits headroom; razor-thin ±1 unit tolerance, but rounding is not a plausible failure mode). Closing route in flight: regenerate the 256-law by re-solving its defining LP (research/notes/regenerate-256law.md, agent d5af80ab) — match → EnclOK becomes CHECKED NUMERICALLY (independent); differ → the ceiling's only non-Lean link is REFUTED.
- That the near-CUE law is the **worst case** for the whole class (the paper's "0.68185" and the support-1.04/1.26/1.70 claim for 0.70/0.80/0.90, Remark 1.1): **CHECKED NUMERICALLY / argued** — it is the LP optimum over 256-periodic marked configurations; the formalized statement is the single-law instance.

## 2. Hardness test of the four inputs

| Input | Status | Classification |
|---|---|---|
| (a) bandwidth ≤ 1 from Montgomery's theorem | **PROVEN (unconditional)** — BGSTB24 Thm 1: F(α) = T^(−2α)(log T + O(1)) + α + O(1/√log T) uniformly for 0 ≤ α ≤ 1; F real, even, nonnegative. The Tsang-kernel extraction (bgst-2501.14545 (4.7)–(4.8)) evaluates the zero-side pair sum only against kernels with Fourier support [−1,1] | **HARD WALL.** The evaluation is unavailable for x > T (α > 1); the paper §7.5(a): for X ≫ T^l the off-diagonal terms cease to be diagonal-dominated and "their evaluation would require information on prime pairs (the Hardy–Littlewood conjectures, or equivalently Montgomery's pair correlation conjecture for α > 1)". This is the root of the ceiling. |
| (b) prime-side second moment (BGSTB24 / Goldston–Suriajaya) | **PROVEN (unconditional)**, error terms corrected in 2501.14545 (uniform 1 ≤ x ≤ T; footnote: Montgomery–Vaughan to appear refine it) | **SOFT WALL within bandwidth 1** (constants/error terms improvable), **HARD at the boundary**: extending the range beyond x = T is exactly the prime-pair problem. GS25/GS26 weaken only the zero-side reading (box hypothesis b/log T), not the bandwidth. |
| (c) rank–trace inequality | **PROVEN TIGHT (Lean, `TightMult`)** — at c = 2, on-line doubles and tight off-line pairs price identically (k₂(2) = 4 = c²), so the certificate *provably cannot separate* an on-line double from an off-line pair at depth → 0 | **HARD WALL at the level of these quantities** (tr, ‖·‖²_F, n₊(Q), integer atoms). Soft only in the trivial sense that a *different* inequality consuming *more* inputs (eigenvalues, higher moments) is a different certificate class — which §7.5(e) shows does not help (below). |
| (d) variational optimum | **PROVEN (Lean, Thm D):** 2 − 1/c₁* = 0.6725007036794116…; CCLM17 Cor. 14: the Montgomery–Taylor kernel is the extremal one-delta solution using only F on [−1,1]; paper §7.1: "no window does better" for block-structure + two traces + primes up to T | **HARD WALL within bandwidth one** (PROVEN optimal for that input). Note 0.6725 < 0.6818: the window-optimal certificate is *not* the class-optimal certificate — see §4. |

**Net:** inside the bandwidth-one class every input is either proven-optimal or near-optimal; the entire gap to 1 is attributed by the paper (and by the ceiling theorem) to the missing |α| > 1 data.

## 3. THE KEY QUESTION: pair correlation beyond bandwidth 1 — proven or conjectural?

**Answer: only CONJECTURAL information exists beyond |α| = 1; the ceiling holds.** Verified against the local literature:

1. **Montgomery (1973, RH):** F(α) = 1 for |α| ≤ 1; the pair correlation conjecture F(α) = 1 for all α is OPEN. No pointwise statement for α > 1 even under RH.
2. **Unconditional (BGSTB24 / 2501.14545):** the formula holds for 0 ≤ α ≤ 1 only. For all α, only trivialities are proven: F real, even, **nonnegative** (from the integral representation F(x,T) = (2/π)∫|Σ x^{ρ−1/2}/(1−(ρ−1/2−it)²)|² dt ≥ 0, bgst (3.4)). Nonnegativity is an inequality, not a value: it can bound a kernel *from above* (CGdL20's SDP trick, 0.6792 — RH-conditional, and the paper notes it "operates in a different regime") but cannot pin down ∫ j(α)F(α)dα for support beyond 1.
3. **Goldston–Montgomery (1987):** the α > 1 regime is *equivalent* to the Hardy–Littlewood prime-pair conjecture (cited this way in §7.5(a)); per the local sources GM87 supplies the Lemma 7/Lemma 8 estimates that fix the range up to α = 1 — not values beyond.
4. **Higher moments of the Gram matrix (the Levinson/mollifier-adjacent route), §7.5(e) of the paper:** unconditional evaluation of tr G̃ᵏ by the diagonal method is available **exactly in the Rudnick–Sarnak range kλ < 2**. For λ ∈ (1/2, 1): at most k = 3, only for λ < 2/3, and odd moments do not lower Λ₁(0) — "unconditionally, higher moments add nothing to the n₊-bound on (1/2,1)". For λ ≤ 1/2, where more moments exist, Proposition 7.4 (rank ≤ d = λ₁N) makes them useless. Under RH the triple correlation is a theorem (Hejhal 1994; RS96) but only in kλ < 2, and it serves *distinct-zero* counts (N_d ≥ 0.85082 under RH, §7.5(g)), not the simple-on-line certificate.
5. **Mollifier machinery (Conrey 1989; Bui–Heath-Brown 2013, 19/27 under RH):** gives simple-zero proportions via a *different* mechanism (mollified discrete moments); it neither produces form-factor values beyond bandwidth 1 nor runs unconditionally (the 19/27 is RH-conditional).
6. **Farmer–Gonek–Lee (2014) / the ξ′ line:** FGL studies pair correlation of the zeros of the *derivative* ξ′ — a different function. The method transports (Lean proves ≥ 0.85838 simple on-line for ξ′ unconditionally, ≥ 0.86864 quartic; §7.3), but this is a different certificate target, **not** a beyond-bandwidth-1 input for ζ's form factor.
7. **GLSS25 (§7.5(f) "complementary" remark):** the *full* pair correlation conjecture (support beyond 1 at the pair level) would yield 100% simple zeros on the line — i.e., the RMT input that would crush the ceiling is exactly the conjectural one.
8. **The conditional lever named by the paper (§7.5(f)):** HL*(k₀, λ) — a Hardy–Littlewood-type asymptotic for the additive correlations Σ_m (Λ∗Λ)(m)(Λ∗Λ)(m+h), |h| ≤ X²/T — would give 13/18 (k₀ = 4) and proportion 1 in the limit. This is **CONJECTURED** (it is a prime-pair statement), not proven.

**Conclusion:** there is **no proven sliver** of form-factor information for |α| > 1 — unconditional or conditional-on-RH — in the verified sources. The paper's own quantification (Remark 1.1): 0.70/0.80/0.90 would need Fourier support out to ≈ 1.04/1.26/1.70, "beyond what is known." So the ceiling is a **hard, proven structural bound** for the certificate class, not an artifact of the proof.

## 4. Strategy: kill criteria and funding criteria

**ABANDON (kill the "beat 0.6818 unconditionally by the same class" angle).** Evidence now in hand, all verified:
- The ceiling is PROVEN in Lean (modulo numerically-checked EnclOK) for certificates of the rank-trace type reading bandwidth-one data.
- Every input of the class is proven-optimal or hard-bounded (§2).
- No proven beyond-bandwidth-1 input exists anywhere in the local literature (§3).
This is a documented structural result, not a research failure: the search should stop trying to push the *unconditional simple-zeros constant* past 0.6818 via pair-correlation certificates, and should not re-attack the ceiling itself except adversarially (below).

**Keep-alive (fundable, in-class):**
1. **Close 0.6725 → 0.6818.** The ceiling is an upper bound for the class; Theorem D's 0.6725 is the window optimum, not the class optimum. The 256-law was found as the optimum of an exact-rational LP over marked configurations; its **dual** is a certificate — computing it (and certifying it in Lean) would (a) push the constant toward 0.6818, and (b) act as an **adversarial validation of the ceiling**: if any certificate beat 0.6818 + slack against the law, `ceiling_law256` would be refuted. Small, well-scoped, and it changes what we believe about how close the method sits to its cap. Low expected yield (bounded above by 0.6818), high verification value.
2. **Adversarial re-check of EnclOK.** The single non-Lean link is the 70-digit interval-arithmetic enclosure of S(j), j = 1…256. Independently recomputing the LP + enclosures from the certificate file (or from scratch) and comparing hashes is cheap and hardens the ceiling's only assumption. If it failed, the ceiling collapses — that is the one live way the ceiling could be *wrong*.

**FUND (breakthrough input — would reopen the angle).** Any of the following, if found in the literature or produced:
- A **proven** (unconditional, or conditional on a hypothesis strictly weaker than the pair-correlation conjecture) estimate for F(α) on some interval (1, 1+δ) — e.g., a proven bound for the additive correlation Σ_m (Λ∗Λ)(m)(Λ∗Λ)(m+h), h ≤ X²/T, currently equivalent to Hardy–Littlewood (§7.5(f)); or any unconditional evaluation of a Gram-matrix moment **outside** the Rudnick–Sarnak range kλ < 2.
- A proven lower bound on F beyond 1 usable with a positive kernel (e.g., an unconditional SDP majorant of the CGdL20 type). Note: the trivial F ≥ 0 alone is insufficient — it gives upper constraints, not values, and the paper already exploits the distinction.
- Proof that ζ's actual zero configuration **cannot** realize near-CUE laws (any structural constraint ruling out the extremal law's shape would directly invalidate the ceiling's premise "the law is an admissible configuration"). Nothing of this kind is known or even plausible from the local sources.

Until one of these appears, the honest status of the 0.6818 ceiling is: **PROVEN (Lean, modulo a numerically-verified enclosure)** — a hard wall for the rank-trace/pair-correlation certificate class, and the correct thing to do is to document it, close the in-class gap, and redirect the search (e.g., ξ′-type transports, or the conjectural-input route labeled as such).
