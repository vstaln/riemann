# Idea Generator — Literature-Grounded Attack Vectors on RH / Proportion-of-Zeros Constants

> Produced by the IDEA-GENERATOR agent (investigation-source-trace + epistemology), Round 1.
> Every vector below traces to a real paper. Labels: **HELD-FILE** = read in full from
> research/papers/; **ABSTRACT-FETCHED** = arXiv abstract retrieved via export.arxiv.org (network
> fetch, Aug 2026); **CITED-IN-OUR-PAPERS** = appears in the bibliography of
> claude-riemann-paper.txt / anthropic-informal-note.txt / bgst papers but NOT fetched.
> Companion doc: literature-map.md (parallel agent; ingredient-level trace). This file is the
> vector-mining complement — it maps each source to a *concrete thing to try*.

---

## (a) Bibliography as extracted from the held claude paper — checked against arXiv where possible

Primary sources held and read in full (HELD-FILE):
- **C** = claude-riemann-paper.txt, "More Than Two Thirds of the Zeta Zeros Lie on the Critical Line" (Anthropic research model, 2026). The 67.25% = 3/2 − (1/√2)cot(1/√2) argument: Weil/Guinand explicit formula → finite-dimensional restriction via v_ρ[k] = φ̂_T(γ_ρ − T − (T/N)k), φ_T ≈ ψ(x·T/N), ψ(u)=cos(√2u)1_{|u|≤1/2} → W_T real symmetric, on-line zeros give (1,0)-planes, off-line pairs give hyperbolic (1,1)-planes → Sylvester inertia + rank–trace inequality (Lemma 3.4) → tr and ‖·‖²_HS via Montgomery–Vaughan off-diagonal control + variational identity.
- **N** = anthropic-informal-note.txt, terse proof skeleton; key named inputs: Guinand–Weil explicit formula; Montgomery–Vaughan(-Hilbert) inequality; Lemma 3.4 rank bound.
- **B24** = baluyot-etal-2306.04799.txt, "An unconditional Montgomery theorem for pair correlation…" (Acta Arith. 214 (2024) 357–376).
- **B25** = bgst-2501.14545.txt, "Pair correlation of zeros of the Riemann zeta function I: proportions of simple zeros and critical zeros" (arXiv:2501.14545v2, 21 Nov 2025). Theorem 2: under box B_b (width b/log T around the line, T<γ≤2T), with Montgomery–Taylor kernel j_M: N_s, N_0 ≥ (0.67250064+o(1))·(T/2π)log T at b=0.001; fails for b ≥ 4.187 (simple/critical) — the kernel-positivity ceiling. **This is the exact constant 0.67250064 = 3/2 − (1/√2)cot(1/√2) our program re-derives via the Weil form.**

Full reference list of C (each labeled; arXiv IDs checked where fetched):

| Ref | Who/when | What | Label |
|---|---|---|---|
| [Rie59] | Riemann 1859 | primes memoir | CITED-IN-OUR-PAPERS |
| [Wei52] | Weil 1952 | explicit formulas | CITED-IN-OUR-PAPERS |
| [Sel42] | Selberg 1942 | positive proportion on line (unpublished constant) | CITED-IN-OUR-PAPERS |
| [Har14],[HL21] | Hardy 1914; Hardy–Littlewood 1921 | ∞ many / ≫T on line | CITED-IN-OUR-PAPERS |
| [Lev74],[Lev75] | Levinson 1974, 1975 | ≥1/3; mollifier | CITED-IN-OUR-PAPERS |
| [Mon73] | Montgomery 1973 | pair correlation; 2/3 simple on RH | CITED-IN-OUR-PAPERS |
| [Mon75] | Montgomery–Taylor (ICM 1974) | 0.6725 simple on RH — *origin of the constant* | CITED-IN-OUR-PAPERS |
| [HB79] | Heath-Brown 1979 | Levinson zeros simple; 34.74% simple&on-line | CITED-IN-OUR-PAPERS |
| [Con89] | Conrey 1989 | >2/5 on line | CITED-IN-OUR-PAPERS |
| [Bom00] | Bombieri 2000 | Weil quadratic form; negative-index observation | CITED-IN-OUR-PAPERS |
| [CGG98] | Conrey–Ghosh–Gonek 1998 | mollified discrete moments of ζ′(ρ); 19/27 simple (RH+GLH) | CITED-IN-OUR-PAPERS |
| [CG93] | Cheer–Goldston 1993 | 0.6727 simple on RH | CITED-IN-OUR-PAPERS |
| [MV74] | Montgomery–Vaughan 1974 | Hilbert's inequality — *our off-diagonal control* | CITED-IN-OUR-PAPERS |
| [GM87] | Goldston–Montgomery 1987 | F(α) to α=1 | CITED-IN-OUR-PAPERS |
| [Mon94] | Montgomery 1994 | ten lectures | CITED-IN-OUR-PAPERS |
| [MO84] | Montgomery–Odlyzko 1984 | gaps between zeros | CITED-IN-OUR-PAPERS |
| [GG07] | Goldston–Gonek 2007 | S(t) and zeros | CITED-IN-OUR-PAPERS |
| [Far95] | Farmer 1995 | distinct zeros via simple zeros of ξ^(j); 63.95% | CITED-IN-OUR-PAPERS |
| [Hej94] | Hejhal 1994 | triple correlation of zeros | CITED-IN-OUR-PAPERS |
| [RS96] | Rudnick–Sarnak 1996 | zeros of L-functions, RMT | CITED-IN-OUR-PAPERS |
| [Yos92] | Yoshida 1992 | Hermitian forms attached to zeta | CITED-IN-OUR-PAPERS |
| [Tsa93] | Tsang 1993 | Tsang kernel (positivity machinery) | CITED-IN-OUR-PAPERS |
| [Ary22] | Aryan 2022 | Landau–Gonek extension | CITED-IN-OUR-PAPERS |
| [BCY11] | Bui–Conrey–Young 2011 | >41% on line | ABSTRACT-FETCHED (arXiv:1002.4127) |
| [Fen12] | Feng 2012 | 41.28% on line | ABSTRACT-FETCHED (arXiv:1003.0059) |
| [BHB13] | Bui–Heath-Brown 2013 | 19/27 simple on RH alone | ABSTRACT-FETCHED (arXiv:1302.5018) |
| [PRZZ20] | Pratt–Robles–Zaharescu–Zeindler 2020 | >41.72% on line; ratios method | ABSTRACT-FETCHED (arXiv:1802.10521) |
| [CGdL20] | Chirre–Gonçalves–de Laat 2020 | SDP pair-correlation kernels; 67.9% simple (RH) | ABSTRACT-FETCHED (arXiv:1810.08843) |
| [FGL14] | Farmer–Gonek–Lee 2014 | pair correlation of zeros of ξ′ | ABSTRACT-FETCHED (arXiv:0803.0425, Farmer–Gonek v1) |
| [CCLM17] | Carneiro–Chandee–Littmann–Milinovich 2017 | Hilbert spaces & pair correlation | CITED-IN-OUR-PAPERS |
| [CIS13] | Conrey–Iwaniec–Soundararajan 2013 | 14/25 simple&on-line for Dirichlet L | CITED-IN-OUR-PAPERS |
| [BGSTB24] | Baluyot et al. 2024 | unconditional Montgomery theorem | HELD-FILE (2306.04799) |
| [BGSTB25] | Baluyot et al. 2025 | pair correlation ⇒ critical zeros (67.25% at b=0.001) | HELD-FILE (2501.14545) |
| [GS25],[GS26] | Goldston–Suriajaya 2025, 2026 | box hypothesis; 2/3 critical | ABSTRACT-FETCHED (2511.20059, 2603.28104) |
| [GLSS25] | Goldston–Lee–Schettler–Suriajaya 2025 | PCC ⇒ 100% simple (Gallagher–Mueller 1978, unconditional) | ABSTRACT-FETCHED (2503.15449) |
| [Wu15],[Wu19] | Wu 2015, 2019 | distinct zeros 66.03%; twisted mean square, Dirichlet critical zeros | CITED-IN-OUR-PAPERS |
| [MV07],[IK04],[Tit86] | books (Montgomery–Vaughan; Iwaniec–Kowalski; Titchmarsh) | standard tools | CITED-IN-OUR-PAPERS |
| [PNT+] | PrimeNumberTheoremAnd (Lean) 2024– | Lean formalisation | CITED-IN-OUR-PAPERS |

Fetched beyond the C bibliography (new survey, 2022–2026; all ABSTRACT-FETCHED):
- **2508.11108** Conrey–Farmer–Kwan–Lin–Turnage-Butterbaugh, "Short mollifiers of the Riemann zeta-function" (2025) — calculus of variations on linear combinations of derivatives of ζ; positive proportion regardless of mollifier length; extends to modular L-functions.
- **1207.6583** Radziwill, "Limitations to mollifying ζ(s)" (2012) — off-diagonal lower bound for mollified moments; on RH connects mollified moments to Montgomery's pair correlation.
- **2511.14415** Bui–Hall–Subira Jorge, "Amplified Fourth Moment of the Riemann Zeta-Function and Applications" (2025).
- **1410.2433** Bui, "Critical zeros of the Riemann zeta-function" (2014, unpublished note) — three-piece mollifier via Bettin–Bui–Li–Radziwill twisted fourth moment.
- **1403.5786** Preobrazhenskii–Preobrazhenskaya, "On a choice of the mollified function in the Levinson–Conrey method" (2014) — 41.2948%.
- **1805.07741** Preobrazhenskaya–Preobrazhenskii, "Almost all of the zeros of the Riemann zeta-function are on the critical line" (2018, v7) — ⚠ extraordinary claim, unverified by us (see vectors).
- **2511.06109** Ray, "Levinson's theorem and its generalization for Dirichlet L-functions" (2025) — exposition of Young (2010) presentation + Wu (2018) Dirichlet result.
- **2606.09096** Suzuki, "Weil's quadratic form via the screw function" (2026) — unifies Yoshida (1992), Bombieri (2001, 2003), Connes–Consani (2023), Connes–Consani–Moscovici (2025+) via screw functions.
- **2308.11860** Suzuki, "Analytic theories around the simplest screw" (2023, survey).
- **2206.03682**, **2209.04658** Suzuki (2022) — screw function for ζ; RH-equivalents in the shape of Weil positivity / Li's criterion, with partial unconditional results.
- **2301.00421** Suzuki, "On the Hilbert space derived from the Weil distribution" (2023) — completion w.r.t. Weil form is **isomorphic to a de Branges space** (Fourier + map); new RH-equivalence.
- **2301.05779** Suzuki, "Li coefficients as norms of functions in a model space" (2023).
- **2607.02828** Groskin, "A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form" (2026) — every real even Galerkin coefficient vector v ↔ band-limited Guinand–Weil test function g_v with exact equality of quadratic values.
- **2605.20224** Groskin, "High-Precision Approximation of Riemann Zeros via the Truncated Weil Form" (2026) — Connes–van Suijlekom truncated Weil form (prime cutoff c, band N); ground-state Fourier–Mellin zeros provably on the line; convergence to Riemann zeros as c→∞ open (Connes 2026; Connes–Consani–Moscovici 2025).
- **2607.24830** Kim–Hong–Kim–Choi–Jang–Kim, "A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator" (2026) — first numerical realization of Suzuki's 2026 Weil-form operator (P1 FEM, Richardson extrapolation); Archimedean spectral law.
- **2602.04022** Connes, "The Riemann Hypothesis: Past, Present and a Letter Through Time" (2026) — comprehensive survey + new perspective (truncated Weil form).

---

## (b) Paper-by-paper vector list

Each entry: paper → method (from abstract/text) → concrete attack vector for our program.

1. **B24/B25 (HELD-FILE)** — unconditional Montgomery theorem F(α) on complex zeros; box hypothesis B_b; Tsang kernel K_b with positivity from cosh-splitting; Montgomery–Taylor kernel j_M. **Vector:** the b-parameter (box width) is a *knob* our Weil-form argument inherited implicitly (ψ has support ±1/2). B25's Table 2 shows the constant decays from 0.6725 to 0 as b grows 0→4.187. Try: replace ψ(u)=cos(√2u) by the j_M-derived kernel with a cosh(bα) factor — the optimal b at fixed N(T) may push the trace/HS-norm ratio (0.6725 → ?) without new ideas. (CHECKED: the 0.67250064 constant matches C; kernel replacement is the extension.)

2. **2606.09096 Suzuki (ABSTRACT-FETCHED)** — Weil quadratic form via the **screw function**: study Q(f) through a continuous function instead of distributions. **Vector:** our W_T's entries v_ρ[k]·v_ρ[l] with v from φ̂_T are evaluations of the autocorrelation of φ̂_T — which is *exactly a screw function* (Suzuki 2206.03682: screw function of ζ is the norm kernel of the Weil form). Expressing tr W_T and ‖W_T‖²_HS as integrals of the screw function of ζ may yield the Montgomery–Vaughan off-diagonal control *as a theorem about the screw function's regularity*, giving an independent derivation of the constant and possibly a cleaner error term.

3. **2301.00421 Suzuki (ABSTRACT-FETCHED)** — Weil-form completion ≅ **de Branges space**. **Vector:** de Branges' theory has ordering/structure theorems for Hilbert spaces of entire functions with a "RH-type" condition. Our finite-rank restriction W_T is a Galerkin section of that de Branges space. De Branges-type embedding theorems could bound the *rank of the negative part* of W_T (the off-line hyperbolic planes) spectrally — a new path to the rank–trace inequality's n₊(W^off_T) term, possibly relaxing the box hypothesis.

4. **2607.02828 Groskin (ABSTRACT-FETCHED)** — finite Guinand–Weil dictionary: v ↔ g_v with <v,Qv> = Σ_ρ ĝ_v(ρ) exactly. **Vector:** our v_ρ[k] vectors are exactly Galerkin coefficient vectors. The dictionary gives a **second, independent trace identity**: tr W_T and ‖W_T‖²_HS recomputed as prime-side explicit-formula sums (no Montgomery–Vaughan), yielding a numerical cross-check and possibly a new constraint (the "archimedean tail order" term). This is a concrete, immediately executable validation target.

5. **2605.20224 / 2607.24830 (ABSTRACT-FETCHED)** — Connes–van Suijlekom truncation of the Weil form at prime cutoff c; Galerkin spectra computed numerically (c=13…100). **Vector:** their finite windows are a *different* restriction than our φ̂_T-shift window. Compare: (i) does the CvS window satisfy the same rank–trace inequality with a better constant? (ii) their ground-state Fourier–Mellin zeros provably lie on the line — the *positivity* is built in; our Sylvester-inertia counting may apply to their matrix directly, giving rank bounds on "on-line part" with *provable* convergence data. Numerical cross-pollination is cheap (Rust; their matrices are public-able).

6. **2508.11108 Conrey–Farmer–Kwan–Lin–Turnage-Butterbaugh (ABSTRACT-FETCHED)** — variational choice of linear combinations of derivatives of ζ for Levinson's method; positive proportion regardless of mollifier length. **Vector:** this is the *mollifier-side mirror* of our variational ψ. Two concrete imports: (i) their extremal functions likely encode the same "bandwidth vs. gain" trade-off — read their variational ODE and compare to our H(λ) = 2 − 1/λ − λ/3 type optimization; (ii) "positive proportion regardless of mollifier length" suggests our method's box hypothesis (width o(1/log T)) is *not* needed for a positive proportion — try width ≍ c/log T with c ≤ 4.187 (B25 ceiling) in the Weil-form counting.

7. **1207.6583 Radziwill (ABSTRACT-FETCHED)** — off-diagonal contributions to mollified moments are bounded below; on RH mollified moments ↔ Montgomery's pair correlation. **Vector:** this is the *ceiling of the Levinson line* — and our method is NOT a mollifier method, so it structurally bypasses it. Say it explicitly in the paper. Second import: Radziwill's off-diagonal lower bound is the mirror of our Montgomery–Vaughan off-diagonal *upper* control; the pair (lower/upper) suggests a duality between mollifier moments and our W_T moments — possibly a statement that our constant 0.6725 is *optimal* for the pair-correlation-style counting (relevant to the "bandwidth-one ceiling" question in the round brief).

8. **2503.15449 GLSS (ABSTRACT-FETCHED)** — PCC (pair correlation conjecture, vertical-distribution only) unconditionally implies 100% simple (Gallagher–Mueller 1978 re-read). **Vector:** PCC is a *conjecture about all α*; Montgomery's theorem (and BGST's unconditional version) covers α ∈ [0,1] only. Our F(α) bounds on [0,1] + GLSS's unconditional logic ⇒ if one could push F(α) to α ∈ [0,1+ε] (or prove PCC "on average"), 100% simple and 100% on-line follow *without RH*. Target: extend the box-hypothesis pair-correlation to α slightly past 1 using the Weil-form window (the Montgomery/BGST/GM87 evaluation range is 0 ≤ α ≤ 1; the natural next step is α > 1 with our φ̂_T-smoothing absorbing the new error terms).

9. **1810.08843 CGdL20 (ABSTRACT-FETCHED)** — SDP-optimized pair-correlation kernels; 67.9% simple under RH (beats 67.25% via better kernels, exploiting F beyond [−1,1]). **Vector:** our paper's Theorem D optimality is scoped to F on [−1,1]; CGdL operate beyond. Their SDP majorants can be dropped into the *box-hypothesis* framework (B25): for fixed b, choose the SDP-optimal j(α) instead of j_F/j_M — expected improvement of the 0.6725 constant at b=0.001 and extension of the b-ceiling 4.187. Concrete: reproduce their SDP (semidefinite program is small) and evaluate our C_b(j) functional on their kernels.

10. **1302.5018 BHB (ABSTRACT-FETCHED)** — 19/27 = 70.37% simple on RH alone (CGG method + generalized Vaughan). **Vector:** BHB get *more* simple zeros on RH than our box-hypothesis 67.25% (on-line, and simple&on-line 34.5%). Two directions: (i) our on-line result (67.25% on the line) has no RH-cost; BHB's simple result assumes RH — a hybrid "RH ⇒ 70.37% simple" already exists; the *open* statement is simple zeros off RH — our box argument gives 67.25% simple under a box; relaxing box→RH would meet BHB. (ii) The CGG discrete-moment machinery (ζ′(ρ) moments) has never been combined with a Weil-form/inertia count — the ζ′(ρ) mollified moments are a *different* quadratic form on the same zero set; a two-form argument (mollifier form + Weil form) is unexplored.

11. **1802.10521 PRZZ (ABSTRACT-FETCHED)** — ratios/CFKRS autocorrelation computes mollified second moments with coefficients μ⋆Λ_1^{*k_1}⋆…⋆Λ_d^{*k_d}. **Vector:** their machinery evaluates the *full* off-diagonal expansion that our Montgomery–Vaughan step only upper-bounds. If the CFKRS-style evaluation can be made unconditional for our specific ψ (the cos(√2u) kernel is a Fourier-side weight), ‖W_T‖²_HS becomes an *asymptotic identity* instead of an upper bound — tightening Lemma 3.4. Risk label: CFKRS/ratios are conditional/heuristic; an unconditional version for this narrow kernel may be provable (B24's M₂ evaluation is already unconditional — the missing piece is the cross terms).

12. **1003.0059 Feng / 1403.5786 P&P / 1410.2433 Bui (ABSTRACT-FETCHED)** — 41.28% → 41.2948% → three-piece mollifier (BBLR twisted 4th moment). **Vector:** the Levinson line is *still creeping* — but Radziwill's ceiling is real. The structural lesson for us: each improvement came from a *wider mollifier family* (more derivative terms / more pieces). The analog in our program: the *test-function family* for φ_T (more frequency bands, tensor products, ψ with more lobes). Feng's "length condition" optimization is the mirror of our λ-window optimization — worth mining Feng's length-condition analysis for a sharper statement of when the box hypothesis can be widened.

13. **0803.0425 FGL (ABSTRACT-FETCHED)** — pair correlation of zeros of ξ′ under RH; consequences for gaps and simplicity. **Vector:** Farmer's distinct-zeros argument chains simple-zero proportions of ξ, ξ′, ξ″…; our paper claims ≥5/6 distinct. Transport: apply the Weil-form/box argument to ξ′ (whose zeros interlace with those of ξ) — a box hypothesis for ξ′ zeros would give *simple* ξ′-zeros, feeding Farmer's chain. Note: FGL's kernel on ξ′ zeros is the same Montgomery machinery — the transport is structurally clean.

14. **2602.04022 Connes (ABSTRACT-FETCHED)** — 2026 survey; truncated Weil form as "new perspective". **Vector:** source document for the Hilbert–Pólya/Weil-form state of the art; check whether Connes' "letter" contains the CvS truncation heuristics that Groskin implements — anything about the *finite* window spectra feeding back into positivity criteria is directly our setting.

15. **1805.07741 P&P "almost all zeros" (ABSTRACT-FETCHED, ⚠)** — claims (v7) that a Levinson-type variant yields (almost) all zeros on the line, depending on the exponent in a zero-density estimate near the line; method: apply second-moment asymptotics on a *subset* of [1/2−a/logT, 1/2−a/logT+i2T] and the *integral of log of the mollified function* on the complement. **Honesty label:** extraordinary claim; we have NOT verified it and it has not (to our knowledge) displaced the 41.7% record — treat as CONJECTURED/possibly flawed. **Method vector (independent of correctness):** the "subset + log-moment on the complement" decomposition has *no analog* in our Weil-form argument. Import: split the T-interval into a part where the quadratic-form identity is sharp and a part controlled by a Jensen/log-type bound. Fresh structural move; cheap to prototype numerically.

16. **Hej94 / MO84 / GG07 / RS96 (CITED-IN-OUR-PAPERS)** — triple correlation; gaps; S(t); RMT. **Vector:** the rank–trace inequality uses only tr and ‖·‖²_HS — second-order data. Hejhal's triple correlation is the literature grounding for computing **third-order data (tr W³ / spectrum kurtosis of W_T)** — a "third trace identity" that would constrain the count of hyperbolic planes beyond n₊-counting. RMT (RS96) predicts the eigenvalue statistics of W_T's underlying operator — a numerical benchmark for the off-line part. (Extension is CONJECTURED; Hejhal's theorem itself is real.)

---

## (c) Top 10 literature-grounded attack vectors (ranked by expected value × feasibility)

1. **Finite Guinand–Weil dictionary ⇒ second trace identity** (Groskin 2607.02828, ABSTRACT-FETCHED). Recompute tr W_T and ‖W_T‖²_HS from prime-side sums via the v↔g_v dictionary; cross-check Montgomery–Vaughan step numerically; hunt for the "archimedean tail order" term as a new constraint. *Immediate, cheap, adversarial-validatable.*
2. **Screw-function formulation of the Weil form** (Suzuki 2606.09096, 2206.03682; ABSTRACT-FETCHED). Replace distribution-valued Q by the continuous screw function; derive the constant 3/2 − (1/√2)cot(1/√2) from screw-function regularity; independent derivation of the off-diagonal control.
3. **de Branges-space structure of the Weil completion** (Suzuki 2301.00421, ABSTRACT-FETCHED). Spectral/embedding theorems on the completion to bound the rank of the negative (off-line) part of W_T — relax the box hypothesis.
4. **Truncated Weil form (CvS/CCM) + our inertia inequality** (Groskin 2605.20224; Connes 2602.04022; ABSTRACT-FETCHED). Run Sylvester-inertia rank counting on the CvS Galerkin matrices (c=13…100, bands N); compare constants with φ̂_T-window; ground-state-on-line property may make the on-line part provably full-rank.
5. **SDP-optimal kernels in the box framework** (CGdL20 1810.08843, ABSTRACT-FETCHED). Drop CGdL's SDP majorants into B25's C_b(j) functional; improve 0.6725 at b=0.001 and extend the b=4.187 ceiling.
6. **Push F(α) past α=1** (GLSS25 2503.15449; GM87; ABSTRACT-FETCHED). If the box-hypothesis pair correlation extends beyond the [0,1] window, GLSS's unconditional Gallagher–Mueller logic upgrades simple/critical proportions toward 100% — no RH needed.
7. **Variational kernel from the short-mollifiers calculus** (Conrey–Farmer–Kwan–Lin–Turnage-Butterbaugh 2508.11108, ABSTRACT-FETCHED). Import their variational extremal functions as φ_T candidates; test the claim "positive proportion regardless of box width" in our counting.
8. **Two-form argument: CGG ζ′(ρ)-moment form + Weil form** (BHB 1302.5018, ABSTRACT-FETCHED). No one has combined the discrete ζ′(ρ) mollified moments with the Weil quadratic form; a joint constraint on the same zero set.
9. **"Subset + log-moment" decomposition** (P&P 1805.07741, ABSTRACT-FETCHED — method only, claim flagged CONJECTURED). Split the height interval; second-moment identity on one part, Jensen/log control on the complement; prototype numerically.
10. **Third trace identity via triple correlation** (Hejhal 1994, CITED-IN-OUR-PAPERS — extension CONJECTURED). tr W³ from 3-correlations of zeros; constrains hyperbolic-plane count beyond n₊.

---

## (d) What NOBODY seems to have tried (CONJECTURED — my read of the field, not a fact)

Based on the survey above (all papers fetched or held, 1973–2026):

1. **No one has combined SDP kernel optimization with the Weil-form/inertia machinery.** CGdL20 optimized pair-correlation kernels (simple-zero counting, RH); our program optimizes the test function inside a Weil-form rank–trace inequality. The SDP-over-test-functions problem for the *rank* functional appears untouched.
2. **No one has run an inertia/rank-counting inequality on the Connes–van Suijlekom / CCM truncated Weil form.** Groskin computes spectra and uses eigenvalue nonnegativity; the *counting* (Sylvester inertia on the finite window: rank ≥ 2tr + 4tr − 4n₊ − ‖·‖²_HS) is our program's novel ingredient and has no counterpart in the CvS literature.
3. **No one has used the finite Guinand–Weil dictionary for a double-trace (two independent computations of the same trace) cross-validation.** Groskin proves the dictionary exists and gives closed forms; an application to *identically recompute* a trace from prime side is not in the abstracts.
4. **No one has fed higher correlations (Hejhal triple, RMT-predicted kurtosis) into a zero-counting inequality.** Every zero-counting method uses first or second moments (Levinson: moments of mollified ζ; Montgomery: pair correlation). A "third-moment zero-counting method" does not exist in the surveyed literature.
5. **The de Branges-space isomorphism (Suzuki) has not been used for quantitative zero-counting** — only for RH-equivalence statements. de Branges' ordering/embedding theorems as a tool to bound the rank of the indefinite part of the finite-window form: unexplored.
6. **The "subset + log-moment" split (P&P) has not been imported into the pair-correlation/Weil-form framework** — it is a mollifier-side trick with no analog in any Montgomery-line paper.
7. **Box-hypothesis results have not been transported to Dirichlet L-functions with varying modulus** — CIS13 (56% simple&on-line, all L(s,χ)) uses different methods; the unconditional-pair-correlation-with-box technique (B24/B25) for L-functions in the q-aspect appears open (our paper's Dirichlet analogues are for the Weil-form constant, not the box-relaxation).

---

## Honesty footer

- All ABSTRACT-FETCHED entries were retrieved via export.arxiv.org on this session (id_list or search_query); abstracts quoted at summary level only. No paper was cited that was neither fetched nor present in the held files' bibliographies.
- 1805.07741 is flagged: extraordinary claim, unverified by us; only its *method* is recommended, never its conclusion.
- Vector claims about what "nobody has tried" (section d) are labeled CONJECTURED and reflect the fetched corpus (arXiv coverage is not complete; journal-only work may overlap).
- The 67.25% constant and the 2/3 result are PROVEN in held files (C/N/B25); everything downstream of them in this memo is CONJECTURED attack direction.
