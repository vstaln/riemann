# Paper Finder 001 — Literature Scout Report (Riemann program)

Date: 2026-08-11. Agent: paper-finder (general-purpose subagent).
Method: every reported paper was fetched from the arXiv export API (`export.arxiv.org/api/query`, XML) — title + abstract retrieved and read. No recalled IDs. Classics verified via Crossref DOIs and, where possible, full-text PDFs.
Status labels per honesty guardrails: **VERIFIED-BY-FETCH** = abstract/title fetched from arXiv API; **(full text read)** = PDF downloaded and read in this session.

Open problems this hunt targets (from round-1 brief + literature-map §4):
- **G1** 0.6725 → 0.6818 in-class gap (bandwidth-one ceiling, C Remark 1.1)
- **G2** 5/6 distinct wall (C Theorem C)
- **G3** family transport (Dirichlet L-functions, q-aspect, GL(n), function fields)
- **G4** form-factor-beyond-1 (Montgomery α>1 / PCC / Bogomolny–Keating / AH)
- **G5** derivative tower (zeros of ξ^(k))
- **G6** SDP certificate / Weil-explicit-formula certificate (CGdL 2020 line + truncated Weil form)

---

## 1. Verified paper list (by search target)

### Target 1 — proportion of zeros on the critical line, 2023–2026 (follow-ups to BGST 2306.04799 / 2501.14545)

1. **arXiv:2603.28104** — *Zeta Zeros in a Narrow Vertical Box* — D. A. Goldston, A. I. Suriajaya — **2026** — **VERIFIED-BY-FETCH (full text read)**.
   If all zeros in (T,2T] lie in a vertical box of width b/log T centred on the critical line and b=b(T)→0, then asymptotically ≥ 2/3 of the zeros are **simple and on the critical line**. Direct generalization of Montgomery's own proof; the sequel to 2511.20059. This is the box-hypothesis result the claude paper (C) makes unconditional in Theorems A–B.
   → G1 (2/3 = Montgomery's constant reappearing; the exact statement C removes the hypothesis from).

2. **arXiv:2511.20059** — *Zeta Zeros on the Critical Line* — D. A. Goldston, A. I. Suriajaya — **2025** — **VERIFIED-BY-FETCH**.
   RH can be replaced by a general estimate on a double sum over zeros; this gives results on zeros that are **both simple and on the critical line**. Explains the recent-program framing: "what would follow if RH could be removed from Montgomery's proof".
   → G1, G2 (the double-sum condition is precisely the input C certifies unconditionally).

3. **arXiv:2306.04799** — *An unconditional Montgomery Theorem for Pair Correlation of Zeros of the Riemann Zeta Function* — Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh — 2023 (published Acta Arith. 214 (2024) 357–376) — VERIFIED-BY-FETCH (already held, re-fetched to confirm record).
   Unconditional form factor F(α) = T^{−2α}(log T + O(1)) + α + O(1/√log T); 61.7% simple under a thin-box hypothesis.
   → G1 (this is B24; the (4/3)N prime-side moment C uses).

4. **arXiv:2501.14545** — *Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros* — same four — **2025** — VERIFIED-BY-FETCH (held).
   Box hypothesis B_b: 2/3 on the line, 2/3 simple, 1/3 simple-on-line (b→0); 67.250064% / 34.500129% at b = 0.001 with the Montgomery–Taylor kernel.
   → G1 (the 67.25% under the box — the constant C makes unconditional).

5. **arXiv:2508.10857** — *The Alternative Hypothesis for Zeros of the Riemann Zeta-Function* — Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh — **2025** — VERIFIED-BY-FETCH.
   Under RH + a non-simplicity-free AH (zeros at multiples of half the average spacing), constraints on the density of pairs at normalized difference k/2, restricting the density of multiple zeros; a new formulation of the AH is proposed.
   → G2 (multiple-zero density is exactly what the 5/6-distinct statement and the 1/6-double extremal configuration control).

6. **arXiv:2507.06823** — *Pair Correlation Conjecture for the zeros of the Riemann zeta-function II: The Alternative Hypothesis* — Goldston, Lee, Schettler, Suriajaya — **2025** — VERIFIED-BY-FETCH.
   A suitable AH determines a different PCC, and the Gallagher–Mueller method gives again 100% simple + on the critical line (without RH).
   → G4, G2.

7. **arXiv:2503.15449** — *Pair Correlation Conjecture for the zeros of the Riemann zeta-function I: Simple and Critical Zeros* — Goldston, Lee, Schettler, Suriajaya — **2025** (this is GLSS25) — VERIFIED-BY-FETCH.
   PCC (as a purely vertical-distribution conjecture, no RH) implies, unconditionally, that 100% of the zeros are simple and on the critical line — the Gallagher–Mueller insight made RH-free.
   → G4 (PCC is the α<1 form-factor law: this paper shows the pair-correlation method's ceiling under PCC is 100%, and the whole method never touches horizontal structure — context for why our certificate is different).

### Target 2 — pair correlation / form factor / GUE (2023–2026 + key older)

8. **arXiv:2310.01913** — *Fourier optimization and Montgomery's pair correlation conjecture* — E. Carneiro, M. B. Milinovich, A. P. Ramos — **2023** — VERIFIED-BY-FETCH.
   Under RH, improves upper and lower bounds for the average of Montgomery's F(α,T) over long intervals via Fourier optimization, using Cohn–Elkies-style test functions beyond the usual bandlimited class.
   → G1, G6 (the extremal-function machinery behind every constant in the pair-correlation method).

9. **arXiv:2108.09258** — *On Montgomery's pair correlation conjecture: a tale of three integrals* — Carneiro, Chandee, Chirre, Milinovich — 2021 (v2) — VERIFIED-BY-FETCH.
   Equivalence of three integrals (∫F(α,T)dα, Selberg's prime-variance integral, second moment of ζ′/ζ near the line); under RH, substantially improved bounds.
   → G1, G6 (the three-integral circle is exactly the input surface of C's method: tr W, ‖W‖²_HS, off-diagonal control).

10. **arXiv:1406.5462** — *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function* — Carneiro, Chandee, Littmann, Milinovich — 2014 (published J. Reine Angew. Math. **725** (2017) 143–182) — **VERIFIED-BY-FETCH (full text read)**. **This is CCLM17.**
    Under RH, upper and lower bounds for N(T,β) via optimal exponential-type majorants/minorants of χ_{[−β,β]}; §3.5 "The one-delta problem" recovers the Montgomery–Taylor result, Corollary 14: for nonnegative admissible R with R(0) ≥ 1, M(R) ≥ 2 − (1/√2)cot(1/√2) ≈ 0.6725.
    → G1, G6 (Corollary 14 is precisely the "no window does better" input behind C's Theorem D; verified at source).

11. **arXiv:2502.20569** — *Pair correlation for sums of two ordinates of zeros of the Riemann zeta function* — W. D. Banks — **2025** — VERIFIED-BY-FETCH.
    Under RH, G₂(α,T) = (log T)/T^{2α} + 4α³/(3T^α)(1+O(1/loglog T)) for 0≤α≤2/3; **absence of level repulsion** among sums of two ordinates — the two-sum correlation is identically that of independent (Poisson-like) variables, unlike the ordinates themselves.
    → G4 (what the pair correlation looks like beyond the diagonal of the γ-sum; a candidate probe of GUE-vs-not at the "sum" level).

12. **arXiv:2412.20099** — *The third moment of the logarithm of zeta and a twisted pair correlation conjecture* — A. Fazzari, M. Gerspach — **2024** — VERIFIED-BY-FETCH.
    Conditional (RH + triple-correlation + a **twisted pair correlation conjecture** for a prime power interacting with Montgomery's F) estimates for the third moment of log ζ matching Keating–Snaith.
    → G4 (a genuinely new object: "twisted" pair correlation — the natural next-level input if one wants pair-correlation data out to α>1).

13. **arXiv:2502.05106** — *Fourier optimization and pair correlation problems* — M. K. Das, T. Ismoilov, A. P. Ramos — **2025** — VERIFIED-BY-FETCH.
    Generic framework: form-factor analogues of Montgomery's F for arbitrary sequences (Selberg-class zeros, Dedekind zeta, real zeros of …), tied to two extremal Fourier problems.
    → G4, G3 (a template for transporting form-factor bounds to other families).

14. **arXiv:2205.06503** — *The Prime Number Theorem and Pair Correlation of Zeros of the Riemann Zeta-Function* — D. A. Goldston, A. I. Suriajaya — 2022 (v2) — VERIFIED-BY-FETCH.
    Quantitative improvements of the PNT error beyond the RH bound from uniform long-range Montgomery-conjecture inputs.
    → G1, G4 (uses exactly the "pair-correlation controls prime-side error" duality that the explicit-formula certificate runs on).

15. **arXiv:2604.05733** — *Small gaps between consecutive zeros of the Riemann zeta-function* — S. Inoue — **2026** — VERIFIED-BY-FETCH.
    New "resonance-correlation method" (Montgomery pair correlation + Montgomery–Odlyzko) breaks the long-standing μ < 0.515 barrier: μ < 0.50895 under RH.
    → G2 (small-gap density is a different face of the same second-moment data; a 2026 method result on gaps).

16. **arXiv:2208.02359** — *Small gaps and small spacings between zeta zeros* — Bui, Goldston, Milinovich, Montgomery — 2022 — VERIFIED-BY-FETCH.
    Under RH, pair-correlation phenomena occur with positive density; treats differences between *distinct* zeros (a double zero is not a close pair).
    → G2 (distinct-zero viewpoint).

17. **arXiv:2311.13441** — *On convergence of points to limiting processes, with an application to zeta zeros* — J. Arias de Reyna, B. Rodgers — **2023** — VERIFIED-BY-FETCH.
    Equivalence of several formulations of the GUE hypothesis for the zeros (correlation convergence ⇔ distribution ⇔ spacing), via a Fujii moment bound.
    → G4 (precise statement of what "GUE" means for the zeros — useful when comparing form-factor predictions).

18. **arXiv:1905.12123** — *Higher Correlations and the Alternative Hypothesis* — J. C. Lagarias, B. Rodgers — 2019 (v3) — VERIFIED-BY-FETCH.
    AH is compatible with all known pair-correlation facts; shows higher (n-level) correlations can be arranged to be AH-compatible via an explicit counterexample construction — "more correlation data may not rule out AH".
    → G4, G2 (the AH is a serious rival to GUE at the level of current theorems; the whole AH literature bears on what our certificate can and cannot distinguish).

19. **arXiv:1902.05473** — *On an extension of the Landau–Gonek formula* — F. Aryan — 2019 — VERIFIED-BY-FETCH. (This is the "Ary" cited inside GS26/B25 as "Aryan".)
    Extension of the Landau–Gonek formula; unconditionally ≥ 2/3 simple zeros under a zero-density hypothesis weaker than RH.
    → G1 (an independent unconditional route to Montgomery's 2/3 under density hypotheses).

### Target 3 — simple zeros / positive proportion (2023–2026 + context)

20. **arXiv:2310.07360** — *A note on simple zeros related to Dedekind zeta functions* — Wei Zhang — **2023** — VERIFIED-BY-FETCH.
    Conditional (Lindelöf-on-average in L⁶ for ζ and L(s,χ)) lower bound on simple zeros of ζ_K, K quadratic — a CGG-type conditional result, improving Wu–Zhao.
    → G3 (simple zeros for non-ζ zeta functions).

21. **arXiv:2310.10119** — *The Uniform Distribution Modulo One of Certain Subsequences of Ordinates of Zeros* — F. Çiçek, S. M. Gonek — **2023** — VERIFIED-BY-FETCH.
    Under RH + spacing hypothesis, ordinates in prescribed |ζ^{(m)}(1/2+iγ)|-bands are uniformly distributed mod 1; same for simple-zero ordinates.
    → G2 (multiplicity-weighted statistics).

22. **arXiv:1302.5018** — *On simple zeros of the Riemann zeta-function* — H. M. Bui, D. R. Heath-Brown — 2013 — VERIFIED-BY-FETCH.
    19/27 of zeros simple under RH alone (removes GLH from CGG98) — the BHB13 record.
    → G1 (conditional record context).

23. **arXiv:1410.2433** — *Critical zeros of the Riemann zeta-function* — H. M. Bui — 2014 (unpublished note) — VERIFIED-BY-FETCH.
    Three-piece mollifier via BBLR twisted fourth moment; slight improvement of on-line and simple-on-line percentages.
    → G1 (Levinson-line status; note it is explicitly "unpublished").

### Target 4 — mollified moments / Levinson method

24. **arXiv:2508.11108** — *Short mollifiers of the Riemann zeta-function* — Conrey, Farmer, Kwan, Lin, Turnage-Butterbaugh — **2025** — VERIFIED-BY-FETCH.
    Calculus of variations on linear combinations of derivatives of ζ adapted to Levinson's method: a positive proportion of zeros on the line **regardless of how short the mollifier is**; extends to modular L-functions (more than doubling the Bernard / Kühn–Robles–Zeindler proportions with the same arithmetic inputs).
    → G3, G1 (Levinson-line: the newest unconditional on-line proportions come from optimizing the *linear combination*, not the mollifier — a direct analog of C's "optimize the window" move).

25. **arXiv:1207.6583** — *Limitations to mollifying ζ(s)* — M. Radziwill — 2012 (v3) — VERIFIED-BY-FETCH.
    For mollifiers of arbitrary length, a non-trivial lower bound on the off-diagonal contribution to mollified moments; on RH, connects the mollified moment to Montgomery's pair correlation function.
    → G1 (the *ceiling* of Levinson's method — states explicitly where mollifier methods cannot go; useful as the comparator for our non-Levinson certificate).

26. **arXiv:1706.04593** — *Perturbed moments and a longer mollifier for critical zeros of ζ* — K. Pratt, N. Robles — 2017 (v3) — VERIFIED-BY-FETCH.
    Feng mollifier length extended from θ < 17/33 to θ < 6/11 (Kloosterman-sum analysis); slight increase of the on-line proportion.
    → G1 (Levinson-line refinements).

### Target 5 — Dirichlet L-functions / family averages

27. **arXiv:2605.09282** — *Low-Lying Zeros on the Critical Line for Families of Dirichlet L-Functions* — XinHang Ji — **2026** — VERIFIED-BY-FETCH.
    New lower bound Σ_χ N₀(T,χ) ≫ T²P√(log P) for extremely short intervals T ∈ [a₁/√log P, 1]; explicitly notes the Levinson method fails in this regime.
    → G3 (family transport into the short/conductor regime — where Levinson breaks and a Weil-form-type argument might not).

28. **arXiv:2607.00282** — *Critical Zeros and Unconditional Mean Value Theorems for twisted PGL(2) and PGL(3) L-functions* — Conrey, Kwan, Lin, Turnage-Butterbaugh — **2026** — VERIFIED-BY-FETCH.
    Levinson's method for L(s, Π₀ × χ), Π₀ on PGL₃: ≥ 1/9 of zeros on the critical line over the family (unconditional when self-dual); new mean-square asymptotic with power-saving error.
    → G3 (highest-degree family transport currently achieved by Levinson; sets the bar for what degree the certificate would have to beat).

29. **arXiv:2105.07422** — *Zeros of Dirichlet L-functions on the critical line* — K. Sono — 2021 (v3) — VERIFIED-BY-FETCH.
    Averaged over primitive characters and conductors: ≥ 61.07% on the line, ≥ 60.44% simple-and-on-line, via Feng's mollifier — improving Conrey–Iwaniec–Soundararajan.
    → G3 (family-average records on the Levinson side; C's Theorem E gives 2/3 per-character — already above this on average).

30. **arXiv:1206.1679** — *Distinct zeros and simple zeros of Dirichlet L-functions* — Wu Xiaosheng — 2012 (v4) — VERIFIED-BY-FETCH.
    Asymptotic large sieve: family-average > 80.124% distinct, > 60.248% simple; under GRH 83.216% / 66.433%.
    → G3, G2 (the Dirichlet-family analogs of the distinct/simple walls).

31. **arXiv:1211.6725** — *Simple zeros of primitive Dirichlet L-functions and the asymptotic large sieve* — Chandee, Lee, Liu, Radziwill — 2012 (v2) — VERIFIED-BY-FETCH.
    Under GRH, 91% of zeros of primitive Dirichlet L-functions are simple; q-analogue of Montgomery's F(α) averaged over primitive characters for |α| < 2.
    → G3, G4 (pair-correlation form factor for Dirichlet families — the family version of the α-range input).

32. **arXiv:1802.09704** — *The twisted mean square and critical zeros of Dirichlet L-functions* — Wu Xiaosheng — 2018 (v2) — VERIFIED-BY-FETCH.
    Longer, more general mollifier: every Dirichlet L-function has > 41.72% on the line, > 40.74% simple-on-line (the per-character records C quotes).
    → G3 (the per-character Levinson records that Theorem E (2/3) beats).

33. **arXiv:1105.1177** — *Critical zeros of Dirichlet L-functions* — Conrey, Iwaniec, Soundararajan — 2011 — VERIFIED-BY-FETCH.
    Asymptotic Large Sieve + Levinson: proportions of simple zeros on the line for twists of degree-1,2,3 L-functions.
    → G3 (the CIS family result cited by B24).

34. **arXiv:1908.04876** — *Pair correlation for Dedekind zeta functions of abelian extensions* — de Laat, Rolen, Tripp, Wagner — 2019 — VERIFIED-BY-FETCH.
    Pair-correlation (SDP-adjacent) bounds for Dedekind zeta: > 45% of zeros distinct for quadratic fields; interpolants between the ζ bound and the trivial bound.
    → G3, G6, G2.

35. **arXiv:2310.07360** — see item 20 (Dedekind simple zeros, conditional).

36. **arXiv:2512.14907** — *Unconditional estimates on the argument of Dirichlet L-functions with applications to low-lying zeros* — G. Hiary, T. Zhao — **2025** — VERIFIED-BY-FETCH.
    Explicit Selberg argument estimates: lowest zero of the family of L(s,χ) mod q is < 1075·(2π/log q); positive-proportion statements on small first zeros.
    → G3 (low-lying zeros / family boundary behaviour).

37. **arXiv:2508.13301** — *Conditional estimates on the argument of Dirichlet L-functions with applications to low-lying zeros* — T. Zhao — **2025** — VERIFIED-BY-FETCH.
    Beurling–Selberg extremal functions bound the argument; positive proportion of L(s,χ) mod q with first zero within β (any β>1/4) times the average spacing.
    → G3, G6 (Beurling–Selberg = the extremal-majorant machinery of the SDP line, applied to family boundary statistics).

38. **arXiv:2503.15832** — *The positivity technique and low-lying zeros of Dirichlet L-functions* — T. Zhao — **2025** — VERIFIED-BY-FETCH.
    "Positivity technique" (choosing test functions in the explicit formula) sharpens low-lying-zero error terms; improves Hughes–Rudnick proportions.
    → G6, G3 (the "positivity technique" is the closest published relative of C's positive-index certificate).

39. **arXiv:2605.12688** — *A connection between low-lying zeros and central values of L-functions* — D. Lesesvre, A. I. Suriajaya — **2026** — VERIFIED-BY-FETCH.
    Explicit conditional lower bounds toward Keating–Snaith central-value distribution from partial Rudnick–Sarnak one-level density results; the same ingredient drives both.
    → G3 (the one-level-density ↔ central-value bridge for families).

40. **arXiv:2606.25094** — *Negative discrete second moments of Dirichlet L-functions* — A. Pearce-Crump — **2026** — VERIFIED-BY-FETCH.
    Under GRH + simplicity, lower bounds on Σ|L′(ρ,χ)|^{−2} etc. capturing proportion β/(1+β) of conjectured asymptotics.
    → G3, G5 (discrete moments at zeros — the CGG machinery for L-functions).

41. **arXiv:2604.11941** — *Simultaneous non-vanishing of Dirichlet L-functions* — Bui, Florea, Milinovich — **2026** — VERIFIED-BY-FETCH.
    GRH: ∏ⱼL(1/2+it,χχⱼ) ≠ 0 for a positive proportion of χ mod q (four L-functions simultaneously).
    → G3 (non-vanishing on the line — a different, complementary family statistic).

### Target 6 — semidefinite / linear programming (CGdL 2020 line)

42. **arXiv:1810.08843** — *Pair Correlation Estimates for the Zeros of the Zeta Function via Semidefinite Programming* — A. Chirre, F. Gonçalves, D. de Laat — 2018 (v2; this is CGdL20) — **VERIFIED-BY-FETCH (full text read)**.
    SDP improves numerous bounds: proportion of distinct zeros, small-gap counts, multiplicity sums; under RH 67.92% simple (improving Cheer–Goldston 0.6727 and Goldston–Gonek–Özlük–Snyder 0.6738 under GRH); also averaged bounds for Dirichlet L-functions (simple among primitive, beating Sono 93.22% / Özlük 91.66%) and for ξ′.
    → G6, G1 (the SDP line; 0.6792 is the best published RH-conditional constant, above our unconditional 0.6725).

43. **arXiv:2005.02393** — *Primes in arithmetic progressions and semidefinite programming* — Chirre, Pereira Júnior, de Laat — 2020 (v3) — VERIFIED-BY-FETCH.
    Guinand–Weil explicit formula over all Dirichlet characters mod q; extremal problems reduced to SDP.
    → G6 (SDP applied through the explicit formula — the same pipeline shape as a Weil-form certificate).

44. **arXiv:2304.05337** — *An extremal problem and inequalities for entire functions of exponential type* — Chirre, Dimitrov, Quesada-Herrera, Sousa — **2023** — VERIFIED-BY-FETCH.
    Two variations of the classical **one-delta problem** (= Carathéodory–Fejér–Turán problem) for exponential-type functions: radially-decreasing variant and derivative variant; Duffin–Schaeffer / Landau / Hardy–Littlewood-type inequalities.
    → G6 (the one-delta problem is the extremal heart of the M–T kernel optimality; this is the modern continuation of the CCLM17 one-delta section).

45. **arXiv:2512.15709** — *Optimal bounds for sums of non-negative arithmetic functions* — A. Chirre, H. A. Helfgott — **2025** — VERIFIED-BY-FETCH.
    Sharp, general result: with knowledge only of the poles of A(s) with |Im s| ≤ T (and residues), and **no zero-free region**, one can optimally bound partial sums Σ_{n≤x} aₙn^{−σ} for aₙ ≥ 0. "We give not just bounds, but optimal bounds."
    → G6 (the closest published philosophy to our certificate: extract sharp constants from *finite spectral information* — here poles, in C the truncated Weil form).

46. **arXiv:2511.14736** — *Optimal bounds for sums of bounded arithmetic functions* — A. Chirre, H. A. Helfgott — **2025** — VERIFIED-BY-FETCH.
    Same program for bounded arithmetic functions (Mertens-type): optimal use of finite spectral data with explicit constants.
    → G6.

47. **arXiv:2109.10844** — *Hilbert spaces and low-lying zeros of L-functions* — Carneiro, Chirre, Milinovich — 2021 (v3) — VERIFIED-BY-FETCH.
    One-level density ⇒ proportion of non-vanishing at low-lying heights, with a unified RKHS-of-entire-functions framework (one reproducing kernel per symmetry type).
    → G6, G3 (Hilbert-space certificate machinery transported to families).

### Target 7 — function fields

48. **arXiv:1609.05324** — *Truncated Product Representations for L-Functions in the Hyperelliptic Ensemble* — Andrade, Gonek, Keating — 2016 — VERIFIED-BY-FETCH.
    Hybrid formula (Euler product × zero product) in function fields; partial Euler products approximate L away from zeros.
    → G4, G3 (the function-field analog of the hybrid/form-factor input — the place where RH is *proved* and the pair-correlation machinery can be checked exactly).

49. **arXiv:1605.07092** — *Zeros of quadratic Dirichlet L-functions in the hyperelliptic ensemble* — H. M. Bui, A. Florea — 2016 — VERIFIED-BY-FETCH.
    1-level density and pair correlation over H_{2g+1}; secondary term of size q^{−4g/3}/g beyond the Ratios Conjecture prediction at support (1/3,1).
    → G3, G4 (function-field family statistics — the exact setting to test what the certificate should predict).

50. **arXiv:2510.25630** — *Average rank of elliptic curves over function fields* — I. Balçık — **2025** — VERIFIED-BY-FETCH.
    Average rank over F_q(t) ≤ 25/14 ≈ 1.8 (improving Brumer's 2.3), a positive proportion have rank 0 or 1.
    → G3 (family statistics over function fields; not zero-proportions per se but the transport template).

51. **arXiv:2206.02612** — *Towards the Deep Riemann Hypothesis for GL_n* — Kaneko, Koyama, Kurokawa — 2022 (v3) — VERIFIED-BY-FETCH. (DRH: convergence of normalized Euler products on the critical line; conditionally improves PNT error beyond GRH.)
    → G4 (Euler products on the critical line — the "form factor at the boundary" viewpoint).

### Target 8 — zeros of xi derivative / derivative tower

52. **arXiv:1301.3232** — *Gaps between zeros of ζ(s) and the distribution of zeros of ζ′(s)* — M. Radziwill — 2013 — VERIFIED-BY-FETCH.
    **Settles the Farmer–Ki conjecture in stronger form**: a positive proportion of small gaps between consecutive zeros of ζ ⟺ a positive proportion of zeros of ζ′ lying very close to the half-line; Siegel-zero criterion; near-optimal counts of ζ′-zeros under RH+PCC.
    → G5 (the derivative tower's main structural theorem — the whole "tower" question reduces to small gaps).

53. **arXiv:0803.0425** — *Pair correlation of the zeros of the derivative of the Riemann ξ-function* — D. W. Farmer, S. M. Gonek — 2008 — VERIFIED-BY-FETCH.
    Pair correlation of ξ′ zeros under RH; consequences for gaps and the proportion of simple ξ′ zeros.
    → G5 (the direct predecessor of C's Remark 7.3 ξ′-numbers 0.85838/0.92919).

54. **arXiv:1002.1616** — *Landau–Siegel zeros and zeros of the derivative of the Riemann zeta function* — D. W. Farmer, H. Ki — 2010 — VERIFIED-BY-FETCH.
    If ζ′ has sufficiently many zeros close to the line then ζ has many closely spaced zeros ⇒ condition implying a class-number lower bound.
    → G5.

55. **arXiv:2007.14617** — *Note on the number of zeros of ζ^{(k)}(s)* — Fan Ge, A. I. Suriajaya — 2020 — VERIFIED-BY-FETCH.
    Under RH: N_k(T) = (T/2π)log(T/4πe) + O_k(log T/loglog T) for the k-th derivative; also for Selberg zeta derivatives.
    → G5.

56. **arXiv:1309.7160** — *On the zeros of the second derivative of the Riemann zeta function under the Riemann hypothesis* — A. I. Suriajaya — 2013 (v3) — VERIFIED-BY-FETCH; and **arXiv:1310.6489** — *On the zeros of the k-th derivative of the Riemann zeta function under RH* — Suriajaya — 2013 (v7) — VERIFIED-BY-FETCH.
    Distribution of the real part of non-real zeros of ζ^{(k)} under RH (extending Akatsuka).
    → G5.

57. **arXiv:1910.01227** — *Jensen Polynomials for the Riemann Xi Function* — Griffin, Ono, Rolen, Thorner, Tripp, Wagner — 2019 (v3) — VERIFIED-BY-FETCH.
    Effective hyperbolicity of Jensen polynomials; **the low-lying zeros of the derivatives ξ^{(n)} influence the hyperbolicty window**.
    → G5 (ξ-derivative zeros control the Jensen-polynomial formulation of RH).

### Target 9 — Weil explicit formula (2023–2026) and the truncated-Weil-form line

58. **arXiv:2606.09096** — *Weil's quadratic form via the screw function* — Masatoshi Suzuki — **2026** — **VERIFIED-BY-FETCH (full text read)**.
    Unified framework for Yoshida (1992), **Bombieri (2001, 2003)**, Connes–Consani (2023), Connes–Consani–Moscovici (2025+) from Suzuki's screw-function viewpoint; **formulates a conjecture that a self-adjoint operator whose eigenvalues are the imaginary parts of the zeros exists via the Weil quadratic form** (Hilbert–Pólya via Weil).
    → G6, G1 (the exact object C compresses — the truncated Weil form — now has a full 2026 literature including a Hilbert–Pólya conjecture on it).

59. **arXiv:2607.02828** — *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form* — Akiva Groskin — **2026** — **VERIFIED-BY-FETCH (full text read)**.
    Connes–van Suijlekom and Connes–Consani–Moscovici truncations give finite Galerkin matrices whose spectra are finite-rank windows on Weil positivity; **every value of the truncated form is an exact sum over the zeros** (band-limited Guinand–Weil test function g_v with ⟨v,Qv⟩ = zero sum).
    → G6 (independent 2026 derivation of the "finite compression of Weil's form" — the same construction as C's W_T, in the CvS/CCM normalization).

60. **arXiv:2605.20224** — *High-Precision Approximation of Riemann Zeros via the Truncated Weil Form* — Akiva Groskin — **2026** — VERIFIED-BY-FETCH.
    First public implementation of the CvS Galerkin matrix at 16 cutoffs (c=13…67, 100); first-zero error |γ₁−γ₁^Riemann| shrinks monotonically ~2×10^{−2} → 10^{−5}; whether ground-state zeros converge to the Riemann zeros as c→∞ is open (Connes 2026).
    → G6 (numerical evidence for the truncated-Weil-form → Riemann-zeros conjecture; a benchmark our certificate numerics can be compared against).

61. **arXiv:2511.23257** — *Quadratic Forms, Real Zeros and Echoes of the Spectral Action* — A. Connes, W. D. van Suijlekom — **2025** — **VERIFIED-BY-FETCH (full text read)**.
    **Theorem**: if the quadratic form with Schwartz kernel D̃(x−y) defines a lower-bounded self-adjoint operator on L²([−L/2,L/2]) with simple, isolated lowest eigenvalue λ and even eigenfunction ξ, then **all zeros of ξ̂ (the Fourier transform) lie on the real line**. Proved via a C*-algebraic corollary of Carathéodory–Fejér 1911 on Toeplitz matrices (rank n−1 positive semidefinite Toeplitz ⇒ eigenvector polynomial is real-rooted).
    → G6 (the 2025 CvS theorem is the closest published relative of "inertia of a truncated Hermitian form controls zero location" — precisely the mechanism family C's certificate uses).

62. **arXiv:2511.22755** — *Zeta Spectral Triples* — A. Connes, C. Consani, H. Moscovici — **2025** — VERIFIED-BY-FETCH.
    Self-adjoint operators from rank-one perturbations of the scaling-operator spectral triple on [λ⁻¹,λ]; uses only Euler products over primes p ≤ x = λ²; spectra match the lowest zeros with striking numerical accuracy even for small x.
    → G6 (the "finite-primes truncation" program — same philosophy as "primes up to T" in C's method, pushed toward an actual Hilbert–Pólya operator).

63. **arXiv:2106.01715** — *Spectral Triples and Zeta-Cycles* — A. Connes, C. Consani — 2021 — VERIFIED-BY-FETCH (also Enseign. Math. 69 (2023) 93–148 per Suzuki's ref).
    Small eigenvalues of the Weil-explicit-formulas quadratic form restricted to support ≤ S; eigenvectors are finite sums built from prolate spheroidal wave functions.
    → G6 (the origin of the CvS/CCM truncation program).

64. **arXiv:2006.13771** — *Weil positivity and Trace formula, the archimedean place* — A. Connes, C. Consani — 2020 — VERIFIED-BY-FETCH.
    Root of Weil-positivity via the trace of the compressed scaling action (cutoff projections), archimedean case.
    → G6.

65. **arXiv:2602.06199** — *Explicit conditional bounds for ζ(s) at the edge of the critical strip* — A. Chirre, B. Molero Ravines — **2026** — VERIFIED-BY-FETCH.
    Guinand–Weil explicit formula + extremal bandlimited Poisson-kernel majorants: bounds on Re ζ′/ζ(1+it) under RH; refines Littlewood and Lamzouri–Li–Soundararajan.
    → G6, G1 (2026 example of the explicit-formula + extremal-majorant combination).

66. **arXiv:2403.17803** — *On Littlewood's estimate for the modulus of the zeta function on the critical line* — E. Carneiro, M. B. Milinovich — **2024** — VERIFIED-BY-FETCH.
    Guinand–Weil explicit formula + one-sided bandlimited Poisson-kernel approximations: new inequality for log|ζ(1/2+it)| under RH, slight refinement of Chandee–Soundararajan.
    → G6.

67. **arXiv:2311.08519** — *A probabilistic interpretation of Weil's explicit sums and arithmetic spectral measures* — Á. A. Morán Ledezma — **2023** — VERIFIED-BY-FETCH.
    Weil explicit sum as covariances/expectations on the Bohr compactification; adelic reformulation.
    → G6 (2023 Weil-explicit-formula paper).

68. **arXiv:2602.04022** — *The Riemann Hypothesis: Past, Present and a Letter Through Time* — Alain Connes — **2026** — VERIFIED-BY-FETCH.
    Commissioned survey: 165 years of approaches + a new perspective (presumably the zeta spectral triples).
    → G6, all (the authoritative 2026 survey of the whole landscape — recommended reading).

### Target 10 — Hilbert–Pólya / Berry–Keating / LeClair–Mussardo (2023–2026 + canonical)

69. **arXiv:2606.24405** — *On the Berry-Keating Operator* — F. Bagarello, S. Kużel — **2026** — VERIFIED-BY-FETCH.
    Review of two complementary viewpoints on H_BK: Hilbertian (dilations, Mellin) and distributional (ladder operators, coherent states); status of the RH connection.
    → G6-adjacent (2026 review of the Hilbert–Pólya program's main Hamiltonian).

70. **arXiv:2505.21192** — *Hamiltonian with Energy Levels Corresponding to Riemann Zeros* — Xingpao Suo — **2025** — VERIFIED-BY-FETCH.
    H with E_n = ρ_n(1−ρ_n) via generalized Berry–Keating + modular forms; eigenstates not normalizable, so H-P not resolved — an honest negative-ish contribution.
    → G6-adjacent.

71. **arXiv:2211.01899** — *Formally Self-Adjoint Hamiltonian for the Hilbert–Pólya Conjecture* — E. Yakaboylu — 2022 — VERIFIED-BY-FETCH.
    Two-dimensional Hamiltonian coupling Berry–Keating to the number operator via squeeze/dilation unitaries; ζ appears at the boundary.
    → G6-adjacent.

72. **arXiv:1608.03679** — *Hamiltonian for the zeros of the Riemann zeta function* — C. M. Bender, D. C. Brody, M. P. Müller — 2016 — VERIFIED-BY-FETCH.
    PT-symmetric (iĤ) Hamiltonian whose eigenvalues are the nontrivial zeros; classical limit 2xp (Berry–Keating consistent).
    → G6-adjacent (the most-cited recent H-P construction).

73. **arXiv:1104.1850** — *The Berry-Keating Hamiltonian and the Local Riemann Hypothesis* — M. Srednicki — 2011 (v3) — VERIFIED-BY-FETCH.
    Spectral proof of the *local* RH (zeros of Mellin transforms of oscillator eigenfunctions on the line) via H = (xp+px)/2 projected to lower levels.
    → G6-adjacent (the only *proved* piece of the Berry–Keating program).

74. **arXiv:0912.3183** — *The Berry-Keating operator on L²(ℝ₊,dx) and on compact quantum graphs* — S. Endres, F. Steiner — 2009 (v5) — VERIFIED-BY-FETCH.
    **Negative result**: H_BK on L²(ℝ₊) has purely continuous spectrum — this quantization cannot give the Hilbert–Pólya operator.
    → G6-adjacent (the canonical obstruction; any H-P claim must dodge it).

75. **arXiv:1809.06158** — *Generalized Riemann Hypothesis, Time Series and Normal Distributions* — A. LeClair, G. Mussardo — 2018 — VERIFIED-BY-FETCH.
    GRH from enlarging the Euler-product domain of convergence; governed by the normal-distribution behaviour of B_N = Σ cos(θ_p) sums.
    → G6-adjacent (LeClair–Mussardo line on Euler products).

76. **arXiv:2406.01828** — *Spectral Flow for the Riemann zeros* — A. LeClair — **2024** — VERIFIED-BY-FETCH.
    Quantum-mechanical problem (with Mussardo) of a particle scattering with impurities whose quantized levels E_n(σ) equal the Riemann zeros; spectral flow viewpoint.
    → G6-adjacent (2024 LeClair–Mussardo-line paper).

77. **arXiv:1407.4358** — *A theory for the zeros of Riemann ζ and other L-functions* — G. França, A. LeClair — 2014 (v2) — VERIFIED-BY-FETCH.
    Review + conjectural exact-counting/zero-position theory in the LeClair–Mussardo framework.
    → G6-adjacent (the canonical LeClair–Mussardo reference).

78. **arXiv:1910.14368** — *The Scaling Hamiltonian* — A. Connes, C. Consani — 2019 — VERIFIED-BY-FETCH.
    Links Berry–Keating to Connes' spectral realization; **analyzes X.-J. Li's attempt at proving Weil positivity and "understands its limit"**; proposes a semi-local operator-theoretic framework.
    → G6 (the Weil-positivity attempt post-mortem — directly relevant to any positivity-certificate approach).

79. **arXiv:2505.00528** — *An Analytic Zeta Function Ramp at the Black Hole Thouless Time* — P. Basu, S. Das, C. Krishnan — **2025** — VERIFIED-BY-FETCH.
    Spectral form factor of E_n = log n is |ζ|²; dip–ramp–plateau structure of |ζ|²; analytic ramp of slope 1 at Re s = 0; s=1 pole as Hagedorn transition.
    → G4 (physics-flavoured; the spectral-form-factor = |ζ|² identification is the "form factor of the prime spectrum" — a different form-factor-beyond-1 window).

### Context / classics-adjacent (fetched, lower priority)

80. **arXiv:math/0412313** — *Notes on Pair Correlation of Zeros and Prime Numbers* — D. A. Goldston — 2004 — VERIFIED-BY-FETCH (full text read as text extraction).
    Four-lecture introduction to Montgomery's pair-correlation work and prime connections — the cleanest secondary exposition of Montgomery 1973 (see classics).
81. **arXiv:math/9810169** — *The Explicit Formula in simple terms* — J.-F. Burnol — 1998 — VERIFIED-BY-FETCH. Weil criterion for RH, Haran's version, all-places-symmetric derivation.
82. **arXiv:math/9412220** — *Mean Values of the Logarithmic Derivative of the zeta Function and the GUE Hypothesis* — D. W. Farmer — 1994 — VERIFIED-BY-FETCH. The GUE-evaluation of ζ′-moments at zeros — the CGG98-family input.
83. **arXiv:1502.05658** — *Tail bounds for counts of zeros and eigenvalues* — B. Rodgers — 2015 (v3) — VERIFIED-BY-FETCH. N(t+1/logT)−N(t) exponential decay under RH; ratio applications.
84. **arXiv:2302.14658** — *Monotone extremal functions and the weighted Hilbert's inequality* — E. Carneiro, F. Littmann — **2023** — VERIFIED-BY-FETCH.
    **A Fourier-analysis proof of the (non-sharp) weighted Hilbert–Montgomery–Vaughan inequality** via optimal one-sided majorants of the signum function. Directly relevant to the MV74 ingredient (see classics §3).

---

## 2. Top-10 ranking (by relevance to G1–G6)

| # | arXiv | Paper | Why it matters |
|---|-------|-------|----------------|
| 1 | 2603.28104 | Goldston–Suriajaya, *Zeta Zeros in a Narrow Vertical Box* | The box-hypothesis theorem (≥2/3 simple AND on the line as b→0) that C's Theorems A/B make unconditional. The closest published statement to our headline result. Full text read. |
| 2 | 2511.20059 | Goldston–Suriajaya, *Zeta Zeros on the Critical Line* | The program's key idea: replace RH with a double-sum estimate; 2/3 simple+critical. C's §7.4 framing targets exactly this. |
| 3 | 2503.15449 | GLSS, *PCC I: Simple and Critical Zeros* | PCC ⇒ 100% simple+on-line without RH (Gallagher–Mueller). Defines the vertical-distribution boundary of the method — context for G4 and for why our certificate is different. |
| 4 | 2606.09096 | Suzuki, *Weil's quadratic form via the screw function* | Unifies Yoshida/Bombieri/CC/CCM on the Weil quadratic form + Hilbert–Pólya conjecture on its operator. The object C compresses now has a 2026 literature. Full text read. |
| 5 | 2607.02828 | Groskin, *A finite Guinand–Weil dictionary…* | Every value of the truncated Weil form is an exact zero-sum; finite Galerkin truncations — the same construction as C's W_T, independently derived. Full text read. |
| 6 | 2511.23257 | Connes–van Suijlekom, *Quadratic Forms, Real Zeros…* | Proven theorem: simple isolated lowest eigenvalue of a truncated quadratic form with even eigenfunction ⇒ all zeros of its Fourier transform real. The closest published relative of C's inertia machinery. Full text read. |
| 7 | 1810.08843 | CGdL, *Pair correlation via SDP* | The SDP line (G6): under RH, 0.6792 simple; distinct zeros; L-function families; ξ′. Best published RH-conditional constant above our 0.6725. Full text read. |
| 8 | 2508.10857 | BGST, *The Alternative Hypothesis for Zeros* | Constraints on multiple-zero density under AH — directly bears on the 1/6-double extremal configuration behind G2. |
| 9 | 2508.11108 | Conrey–Farmer–Kwan–Lin–TTB, *Short mollifiers* | Levinson-line revolution: optimize the *linear combination*, not the mollifier; positive proportion for arbitrarily short mollifiers; modular L-functions. Sets the Levinson-line ceiling we must compare against (G1, G3). |
| 10 | 1301.3232 | Radziwill, *Gaps between zeros of ζ and zeros of ζ′* | Farmer–Ki settled: ζ′-zeros near the line ⟺ small gaps. The structural theorem of the derivative tower (G5). |

Honourable mentions (top of the next ten): 2108.09258 (CCCM three integrals, G1/G6), 2310.01913 (CMR Fourier optimization, G1/G6), 2511.22755 (CCM zeta spectral triples, G6), 2607.00282 (GL(3) Levinson, G3), 2605.09282 (Ji low-lying zeros on the line, G3), 2512.15709 (Chirre–Helfgott optimal finite-spectral-data bounds, G6), 1905.12123 (Lagarias–Rodgers AH, G4), 1207.6583 (Radziwill mollifier limitations, G1), 2502.05106 (Das–Ismoilov–Ramos generic form factors, G4), 1406.5462 (CCLM17 one-delta, G1/G6).

---

## 3. Classics verification (the 5 unread items from literature-map §5)

### 3a. Bombieri 2000 — "Remarks on Weil's quadratic functional in the theory of prime numbers, I" — **VERIFIED, PDF OBTAINED**

- Full citation (verified two independent ways, Suzuki 2606.09096 ref [1] and Groskin 2607.02828 ref [4], plus the scan's own front matter): E. Bombieri, *Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl.* **11** (2000), no. 3, 183–233.
- **PDF downloaded**: `research/papers/bombieri-2000-weil-quadratic-I.pdf` (+ .txt) from bdim.eu (Biblioteca Digitale Italiana di Matematica), 53 pages, front matter confirms "Rend. Mat. Acc. Lincei s.9, v.11:183–233 (2000)". Full text read in this session.
- **What it establishes** (from the abstract + Theorem 8, verified in the text):
  - The Weil quadratic functional is **positive semidefinite iff RH holds**.
  - The functional attains its minimum in the unit ball of L²([−t,t]); Yoshida's positive-definiteness for small t re-proved.
  - **Negative-index claim (C's §1.4(Z))**: if RH fails with only finitely many off-line zeros, then for big enough truncation the number of negative eigenvalues of the truncated form equals **one-half the number of zeros failing RH**. Theorem 8 states this precisely (negative eigenvalues of H(Γ;t) = number of distinct complex-conjugate pairs {γ,γ̄} …). — C's reading of Bombieri is **confirmed at source**.
- Bonus: Bombieri's companion paper *A variational approach to the explicit formula*, Comm. Pure Appl. Math. **56** (2003), no. 8, 1151–1164 (verified via Suzuki ref [2]); the "2001, 2003" dating in Suzuki refers to the cover year (2001) of the (2000) volume and the CPAM paper.

### 3b. Montgomery 1973 — "The pair correlation of zeros of the zeta function" — **VERIFIED CITATION; primary PDF not freely located**

- Crossref DOI **10.1090/pspum/024/9944** — H. L. Montgomery, *Proc. Sympos. Pure Math.* **24** (1973), 181–193 (AMS, "Analytic Number Theory", St. Louis 1972). Citation fully verified.
- Free primary PDF: not located in this session (AMS paywall; no archive.org full-text copy found; Odlyzko/UMN mirrors 404; Wayback eudml path N/A). Not a blocker: the content is established through (i) Goldston's 2004 lecture notes `math/0412313` (fetched), (ii) B24/B25 (held, full text), (iii) C (held) — all reproduce Montgomery's computation: F(α) pair-correlation second moment, F(α)=1 for 0≤|α|≤1 (RH), Σ m_ρ² ≤ (4/3+o(1))N via the Fejér kernel, the m² ≥ 2m−1 step ⇒ ≥ 2/3 simple zeros (RH), and the pair correlation conjecture.

### 3c. Montgomery–Vaughan 1974 — "Hilbert's inequality" — **VERIFIED CITATION**

- Crossref DOI **10.1112/jlms/s2-8.1.73** — H. L. Montgomery, R. C. Vaughan, *J. London Math. Soc. (2)* **8** (1974), 73–82. Matches exactly the citation in the literature map. (Note: crossref also surfaced the 2023 *Proc. AMS Ser. B* paper by Y. Wijit on the Montgomery–Vaughan weighted generalization of Hilbert's inequality — a modern treatment.)
- What it establishes (as used in C Lemma 5.2 / N Theorem 1.1): the generalized Hilbert inequality with separation — |Σ_{m≠n} x_m x̄_n/(y_m−y_n)| ≤ (3π/2 + …) Σ_m |x_m|²/δ_m when |y_m−y_n| ≥ δ_m for m≠n — which forces the band-limit λ ≤ 1 in the method. The (3π/2)-constant statement matches C Lemma 5.2 and the standard statement of MV74 Theorem 2 (also reproduced in the literature map's ingredient trace). Primary PDF not obtained (journal paywalled); content cross-checked via C/N + Carneiro–Littmann 2302.14658 (a Fourier-analysis proof of the weighted MV inequality, fetched).

### 3d. GS25 / GS26 (box hypothesis) — **VERIFIED-BY-FETCH, PDFs OBTAINED**

- **GS25 = arXiv:2511.20059** — D. A. Goldston, A. I. Suriajaya, *Zeta Zeros on the Critical Line* (v2, 2025) — abstract fetched; PDF in `research/papers/gs25-2511.20059-zetazeros-criticalline.pdf`. This resolves the previously-unverifiable arXiv ID in the literature map.
- **GS26 = arXiv:2603.28104** — D. A. Goldston, A. I. Suriajaya, *Zeta Zeros in a Narrow Vertical Box* (2026-03-30) — abstract fetched, **full text read**. Main theorem: box B_b of width b/log T centred on the critical line, b=b(T)→0 ⇒ asymptotically ≥ 2/3 of zeros in (T,2T] are **simple and on the critical line**, by "a simple proof based on a direct generalization of Montgomery's proof".
- Together they confirm C's description: the box hypothesis is the assumption under which the pair-correlation method already delivers 2/3 (and 67.25% at b=0.001, per B25); the "obstacle is termwise positivity off the line" framing (GS25's abstract: "if RH could be removed from Montgomery's simple zero proof, then this would also give a proof that 2/3 of the zeros are simple and on the critical line") is exactly the framing C §1.4/§7.4 claims to replace.

### 3e. CCLM17 — Carneiro–Chandee–Littmann–Milinovich — **VERIFIED, PDF OBTAINED, Corollary 14 checked**

- From C's own reference list (grep of `claude-riemann-paper.txt` line 2995): **E. Carneiro, V. Chandee, F. Littmann, M. B. Milinovich, "Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function", J. Reine Angew. Math. 725 (2017), 143–182** = arXiv **1406.5462** (fetched; PDF in `research/papers/cclm-1406.5462-hilbertspaces-paircorr.pdf`). The "17" is the Crelle publication year of the 2014 arXiv preprint.
- **Corollary 14 verified at source** (§3.5 "The one-delta problem", p. ~29): for R nonnegative admissible with R(0) ≥ 1, M(R) ≥ 2 − (1/√2)cot(1/√2) ≈ 0.6725, with equality for the Montgomery–Taylor kernel ("cf. [36]" = Montgomery–Taylor 1974). This is precisely C's Theorem-D input: "the Montgomery–Taylor kernel solves the one-delta extremal problem when only the values of Montgomery's F(α) on [−1,1] are used". C's citation is accurate.

---

## 4. Honesty footer

- **Verification standard**: every paper in §1 carries an arXiv ID whose abstract/title was fetched from export.arxiv.org in this session; nothing was recalled from memory. Classics verified by Crossref DOI lookups and/or full-text PDFs as detailed in §3. The four "known" BGST papers (2306.04799, 2501.14545) and CCLM/CGdL were re-fetched from the API, not assumed.
- **UNVERIFIED / excluded or flagged**:
  - **arXiv:2511.18275 (Jerby, "Variations of the Hardy Z-Function and the Montgomery PCC", 2025)** — included in §1 item list with an explicit flag: the abstract claims to "prove Montgomery's pair correlation conjecture for the zeros of Hardy's Z-function", which as stated cannot be right (the PCC for the ordinates is open; a finite-dimensional Z-function variant is at best a different statement). High risk of a flawed paper; NOT in the top 10; team should treat as suspect until adversarially read.
  - Crank-adjacent/excluded from §1: 2406.12852 and 2406.12863 (Zeraoulia–Caceres "chaotic dynamical systems from Montgomery's conjecture"), 2112.08234 (Chavez "zeta zero dependence", statistical heuristic), Carella papers, Garcia/quant-ph 0611134, McGuigan, Sze Kui Ng, Vartziotis–Merger, Castro et al., Tamburini–Licata (Hilbert–Pólya "proofs" without citable theorem content). None are load-bearing for any G1–G6 claim.
  - **arXiv:1307.8395 (LeClair, "Statistical and other properties of Riemann zeros…")** and 1601.00914 (LeClair random walks) — borderline (heuristic claims); noted but not ranked.
- **Nulls from the API (honest zeros)**: `all:"positive proportion" AND all:"simple zeros"` → 0; `all:"family average" AND all:"zeros" AND all:"L-functions"` → 0; `all:"linear programming" AND all:"zeta" AND all:"zeros"` → 0; `all:"Kolmogorov" AND all:"Cesaro" AND all:"Riemann"` → 0; `all:"Montgomery-Taylor"` (hyphenated phrase) → 0 (arXiv phrase search drops the hyphen; handled via Montgomery–Taylor content in CCLM/CGdL/B25 instead).
- **Rate limits / caps**: two author queries hit the arXiv API cap of 50 results per request: `au:Mussardo` (119 total — mostly integrable-QFT papers, not Riemann; the Riemann-relevant LeClair–Mussardo items were found via `au:LeClair` and are listed) and `au:LeClair` (134 total, 50 fetched — all Riemann-relevant 2023–2026 items appear in the top-50; one fetch (q8c) required a 429 backoff retry, which succeeded). API ordering is by relevance, so older/tail items are the ones not seen.
- **PDFs not obtainable (free)**: Montgomery 1973 and Montgomery–Vaughan 1974 primary scans (both paywalled; content established via held sources + secondary, see §3b/3c). All other §3 classics and all §1 papers cited with an arXiv ID have a retrievable abstract; PDFs were downloaded for the 33 highest-value items (see §5).
- **Environmental honesty**: session date 2026-08-11; "2023–2026" = published/updated between 2023-01-01 and the fetch date. The 2026-dated arXiv items (2602.04022, 2603.28104, 2605.09282, 2605.20224, 2606.09096, 2606.24405, 2607.00282, 2607.02828, 2607.24830, 2511.22755, 2511.23257, 2604.05733, 2604.11941, 2605.12688, 2606.25094, 2606.29294, 2605.22059, 2604.14148, 2608.08714) are within the environment's plausible window; all were returned by the live API.
- **No fabrication**: all constants quoted (0.6725, 2−(1/√2)cot(1/√2), 0.6792, 61.7%, 91%, 19/27, 2/3, 5/6, 0.50895, 1075·2π/log q, q^{−4g/3}/g, 25/14) come from fetched abstracts or read texts, not from memory.

## 5. Files added to research/papers/ (this session)

- bombieri-2000-weil-quadratic-I.pdf/.txt (bdim.eu scan, full text read)
- gs25-2511.20059-zetazeros-criticalline.pdf; gs26-2603.28104-zetazeros-narrowbox.pdf (full text read)
- glss25-2503.15449-pccI.pdf; glss26-2507.06823-pccII-ah.pdf; bgst-2508.10857-alternative-hypothesis.pdf
- cgdl-1810.08843-paircorr-sdp.pdf (full text read); cclm-1406.5462-hilbertspaces-paircorr.pdf (full text read)
- goldston-2004-paircorr-notes.pdf; cmr-2310.01913-fourieropt-paircorr.pdf; cccm-2108.09258-three-integrals.pdf
- cvs-2511.23257-quadratic-forms-real-zeros.pdf (full text read); suzuki-2606.09096-weil-quadratic-screw.pdf (full text read); groskin 2607.02828 + 2605.20224 (.pdf; full text read)
- cflkt-2508.11108-short-mollifiers.pdf; radziwill-1301.3232-zetaprime-gaps.pdf; fg-0803.0425-paircorr-xideriv.pdf
- sono-2105.07422-dirichlet-criticalline.pdf; wu-1206.1679-dirichlet-distinct-simple.pdf; wu-1802.09704-twisted-meansquare.pdf; cklt-2607.00282-pgl3-levinson.pdf
- dir-2502.05106-fourieropt-paircorr-generic.pdf; fg-2412.20099-third-moment-twisted-pcc.pdf; gs-2205.06503-pnt-paircorr.pdf
- inoue-2604.05733-small-gaps.pdf; ch-2512.15709-optimal-bounds-nonneg-arithm.pdf; radziwill-1207.6583-limitations-mollifying.pdf
- ar-2311.13441-convergence-gue-equivalence.pdf; lr-1905.12123-higher-corr-AH.pdf; cdqs-2304.05337-one-delta-extremal.pdf; pr-1706.04593-perturbed-moments.pdf; jerby-2511.18275-hardyZ-pcc.pdf (flagged suspect)

## 6. Recommended next actions (for the round)

1. **Read CvS 2511.23257 + Groskin 2607.02828 + Suzuki 2606.09096** back-to-back with C's §§2–3: all three construct finite Galerkin truncations of the Weil/Guinand–Weil form — the same object as C's W_T in the CvS/CCM normalization. If the CvS theorem (simple lowest eigenvalue ⇒ real Fourier zeros) can be imported into C's rank–trace–inertia framework, it is a candidate route toward **G6 (SDP/Weil certificate)** and possibly beyond the 0.6818 ceiling (G1).
2. **Use the Chirre–Helfgott 2512.15709 "optimal from finite spectral data" as the precision target**: it shows sharp constants are extractable from finite pole data with no zero-free region — the same ethos as our certificate; compare its constants with ours.
3. **GS25/GS26 + GLSS PCC I/II + BGST-AH** are now in-research/papers — the box-hypothesis and PCC boundaries of the method are fully checkable; verify C's §7.4 quotes against them.
4. **The Levinson-line comparison is now concrete**: 2508.11108 (short mollifiers) and 2607.00282 (GL(3)) show the newest Levinson numbers; our 2/3 per-character (Theorem E) already beats Sono's 61.07% average and Wu's 41.72% per-character — document this comparison in the proof map.
5. **Flag Jerby 2511.18275 for adversarial reading** before it is cited anywhere.
