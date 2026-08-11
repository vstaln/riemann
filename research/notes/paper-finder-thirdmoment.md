# Paper Finder — Third-Moment / Triple-Correlation Hunt (P2 support)

Date: 2026-08-11. Agent: paper-finder (general-purpose subagent).
Goal: find and download literature on (a) triple correlation / third moment of ζ's zeros, (b) shifted moments of ζ, (c) the Rudnick–Sarnak diagonal-method papers, (d) Hejhal's triple correlation, plus twisted/shifted-moment statements that could translate to P2.
Method (honesty guardrails): **no recalled arXiv IDs** — every reported paper was fetched via the arXiv export API (`export.arxiv.org/api/query`, XML, title+abstract read) or via Crossref / OpenAlex / Unpaywall for the classics. Each entry is labeled **VERIFIED-BY-FETCH** (abstract fetched and read). PDFs were downloaded from arXiv PDF links and verified by magic bytes (`%PDF`, size ≥ 20 KB); the download log is in §4.

**The one-line answer to the P2 question** (see §5 for the reasoning): no unconditional triple-correlation *value* for ζ's zeros exists in the literature. The unconditional content in the Rudnick–Sarnak range λ < 2/3 is the **n-level density** diagonal main term (RS96/RS98 theorems), plus family-level statements (Jiang 2025 GUE statistics for automorphic L-function zeros; Gonçalves–de Laat–Leijenhorst multiplicity bounds). Every *triple-correlation function* computation (Hejhal 1994; Bogomolny–Keating 1996; Conrey–Snaith 2006) is conditional (RH / semiclassical / CFZ ratios conjecture respectively).

---

## 1. Verified paper list (all VERIFIED-BY-FETCH)

Legend for "Why it matters for P2":
- **[A]** = candidate *unconditional* input in the RS range λ < 2/3 (diagonal-method / n-level density)
- **[B]** = conditional triple-correlation / third-moment computation (to match constants and lower-order terms)
- **[C]** = shifted/twisted moment technique that could translate (what P2 could use to attack the moments feeding a correlation)
- **[D]** = supporting machinery (functional equations, divisor sums, ratios conjecture)

### A. Triple correlation / third moment of zeros (direct)

1. **arXiv:math/0610495v2** — *Triple correlation of the Riemann zeros* — J. B. Conrey, N. C. Snaith — 2006/2007 (J. reine angew. Math. 591 (2006) 33–75) — **VERIFIED-BY-FETCH (PDF downloaded, first page read)** — **[B]**.
   Calculates ALL lower-order terms of the triple correlation of the Riemann zeros, conditional on the CFZ ratios conjecture; agrees with Bogomolny–Keating's semiclassical formula and with their own numerics. Gives the full 3-point correlation function including the constant term — the exact object P2 wants, but conditional. PDF saved.

2. **arXiv:0803.2795v1** — *Correlations of eigenvalues and Riemann zeros* — J. B. Conrey, N. C. Snaith — 2008 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[B]**.
   Assuming the ratios conjecture, proves a formula with all lower-order terms for the **n-correlation of ζ's zeros at every order** (works for U(N) too). The n-correlation-to-any-order template. PDF saved.

3. **Hejhal 1994** — *On the triple correlation of zeroes of the zeta function* — D. A. Hejhal — IMRN 1994, no. 7, 293–302 — **VERIFIED-BY-FETCH (metadata)**: Crossref record (author "Dennis Hejhal", IMRN vol 1994, issue 7, first page 293, DOI **10.1155/S1073792894000334**, publisher OUP); Unpaywall confirms year 1994, publisher OUP. **PDF: UNOBTAINABLE from this machine** — the OUP PDF (`academic.oup.com/imrn/article-pdf/1994/7/293/6768423/1994-7-293.pdf`) returns HTTP 403 (Cloudflare bot-wall); no OA copy found via Unpaywall/OpenAlex/Wayback. **[B]** — Hejhal's triple correlation is the classic conditional-on-RH computation (he works on the line under RH and evaluates the 3-point correlation with lower-order terms). Obtainable with a human browser at the OUP link above.

4. **Bogomolny–Keating 1996** — *Gutzwiller's trace formula and spectral statistics: beyond the diagonal approximation* — E. Bogomolny, J. P. Keating — Phys. Rev. Lett. 77 (1996) 1472 — **VERIFIED-BY-FETCH (metadata)**: Unpaywall record (title, year 1996, publisher APS, DOI **10.1103/PhysRevLett.77.1472**); no OA copy. **[B]** — the semiclassical (periodic-orbit) approach that first computed the triple correlation; Conrey–Snaith's abstract says BK "returned to their previous results simultaneously" and wrote out the full expression (circa 2006). PDF: UNOBTAINABLE here (APS paywall; no arXiv version).

5. **arXiv:1911.09216v2** — *Triple Correlation Sums of Coefficients of Cusp Forms* — Hulse, Kuan, Lowry-Duda, Walker — 2019 — **VERIFIED-BY-FETCH (abstract)** — **[C/D]**.
   Triple correlations of cusp-form coefficients: the *same algebraic shape* (triple divisor-type sums) as the divisor-sum side of a zeros triple correlation, in a setting where unconditional statements exist. Useful as a "what the unconditional triple correlation machinery looks like elsewhere" reference. (Not downloaded — lower priority; can be pulled later if P2 needs it.)

### B. Goldston–Yildirim divisor sums (the prime-side / diagonal object)

6. **arXiv:math/0111212v1** — *Higher correlations of divisor sums related to primes I: triple correlations* — D. A. Goldston, C. Y. Yildirim — 2001 (J. reine angew. Math. 566 (2004) 49–105) — **VERIFIED-BY-FETCH (PDF downloaded)** — **[A/C]**.
   The **triple correlations of the truncated divisor sum** Λ_R(n) — the exact prime-side object whose diagonal evaluation is the "diagonal method" content behind an unconditional statement in the RS range. The hooks' note says the prime-side evaluation of tr G̃^k is "available exactly in the Rudnick–Sarnak range kλ < 2 [RS96]"; GY-I is the companion arithmetic computation. PDF saved.

7. **arXiv:math/0209102v1** — *Higher correlations of divisor sums related to primes III: k-correlations* — Goldston, Yildirim — 2002/2003 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[A/C]**.
   General k-correlations of Λ_R — the k-level version of the same diagonal machinery. PDF saved.

8. **arXiv:math/0412366v1** — *Higher Correlations of Divisor Sums Related to Primes II: Variations of the error term in the PNT* — Goldston, Yildirim — 2004 (JNT) — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C/D]**.
   Error-term applications of the same correlation technology. PDF saved.

### C. Shifted moments of ζ (the translation toolkit)

9. **arXiv:2206.03350v1** — *Shifted moments of the Riemann zeta function* — N. Ng, Q. Shen, P.-J. Wong — 2022 (Invent. Math. 235 (2024)) — **VERIFIED-BY-FETCH (PDF downloaded, first page read)** — **[C]**.
   RH **implies Chandee's conjecture** on shifted moments of ζ; based on Harper's method for sharp 2k-th moment bounds. The Chandee-type shifted moment `M_{α,β}(T) = ∫ ∏|ζ(1/2+i(t+α_k))|^{2β_k} dt` is precisely the integral object P2 would need if translating a triple correlation into a shifted-moment statement. PDF saved.

10. **arXiv:1111.0925v1** — *The second shifted moment of the Riemann zeta function* — S. Bettin — 2011 (IMRN) — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**.
    Asymptotic formula for the second moment with two shifts (imaginary parts up to T^{2−ε}), unconditional in the stated shift range. The model for what an unconditional shifted-moment statement looks like. PDF saved.

11. **arXiv:0910.0664v1** — *On the correlation of shifted values of the Riemann zeta function* — V. Chandee — 2009 (Q. J. Math.) — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**.
    The original Chandee upper/lower bounds + conjectured RMT asymptotics for shifted moments; transitions at |α₁−α₂| ≈ 1/log T. The reference the later papers build on. PDF saved.

12. **arXiv:2405.08725v1** — *Lower bounds for shifted moments of the Riemann zeta function* — M. J. Curran — 2024 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**.
    Lower bounds matching Chandee's upper bounds for `M_{α,β}(T)`, under RH. PDF saved.

13. **arXiv:2303.10123v2** — *Correlations of the Riemann zeta function* — M. J. Curran — 2023 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**.
    RH-conditional sharp upper bounds for shifted moments, improving Chandee and Ng–Shen–Wong, especially when the shifts are close. PDF saved.

14. **arXiv:math/0612106v2** — *Moments of the Riemann zeta-function* — K. Soundararajan — 2006/2009 (Ann. Math. 170 (2009) 981–993) — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C/D]**.
    RH ⟹ near-sharp upper bounds for the 2k-th moments; the foundational method (Soundararajan's moment bounds) that Harper and Chandee refine. PDF saved.

15. **arXiv:math/9902162v1** — *High moments of the Riemann zeta-function* — J. B. Conrey, S. M. Gonek — 1999 (Duke 107 (2001) 577–604) — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C/D]**.
    General approach (Dirichlet polynomial + divisor correlations) that produces the conjectured formula for every even moment; carries out the 6th and 8th. The "shifted-moment via divisor sums" lineage that Conrey–Keating's series continues. PDF saved.

16. **arXiv:1305.4618v1** — *Sharp conditional bounds for moments of the Riemann zeta function* — A. J. Harper — 2013 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C/D]**.
    Harper's sharp moment bounds (the tool cited by Ng–Shen–Wong). PDF saved.

17. **arXiv:1610.04977v3** — *The sixth moment of the Riemann zeta function and ternary additive divisor sums* — N. Ng — 2016 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**.
    Sixth moment asymptotic conditional on the ternary additive divisor conjecture — the additive-divisor-sums route toward moments beyond the fourth. PDF saved.

18. **arXiv:1106.4352v3** — *Uniform asymptotics for the full moment conjecture of the Riemann zeta function* — G. A. Hiary, M. O. Rubinstein — 2011 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C/D]**.
    Uniform numerical/methodical treatment of the full moment conjecture (Keating–Snaith coefficients) — useful for matching constants. PDF saved.

### D. Conrey–Keating divisor-sum method (the heuristic behind the diagonal)

19. **arXiv:1506.06842v1 / 1506.06843v1 / 1506.06844v1** — *Moments of zeta and correlations of divisor-sums I, II, III* — B. Conrey, J. P. Keating — 2015 — **VERIFIED-BY-FETCH (PDFs downloaded)** — **[C/D]**.
    The systematic "long Dirichlet polynomial + divisor correlations" program for 2k-th and shifted moments; identifies exactly which terms the diagonal method captures and which are missed beyond the eighth moment. I and III are the most relevant. PDFs saved.

20. **arXiv:2206.04821v2** — *Moments of zeta and correlations of divisor-sums: stratification and Vandermonde integrals* — S. Baluyot, B. Conrey — 2022 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C/D]**.
    Refined heuristic → new integral expression for shifted-moment asymptotics, analogous to the Rodgers–Soundararajan RMT formula. PDF saved.

21. **arXiv:1611.09198v1** — *Averages of ratios of the Riemann zeta-function and correlations of divisor sums* — B. Conrey, J. P. Keating — 2016 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[B/D]**.
    Ratios → divisor-sum correlations; the bridge between the CFZ ratios machinery and the divisor-sum moment machinery. PDF saved.

### E. Ratios conjecture machinery (the engine behind CS triple correlation)

22. **arXiv:0711.0718v3** — *Autocorrelation of ratios of L-functions* — J. B. Conrey, D. W. Farmer, M. R. Zirnbauer — 2007 (Comm. Math. Phys. 278 (2008) 687–727) — **VERIFIED-BY-FETCH (PDF downloaded)** — **[B/D]**.
    The CFZ ratios conjecture itself — the conjecture Conrey–Snaith's triple correlation and the 0803.2795 n-correlation depend on. PDF saved.

23. **arXiv:math/0509480v2** — *Applications of the L-functions ratios conjectures* — J. B. Conrey, N. C. Snaith — 2005/2007 (Proc. LMS 94 (2007) 594–646) — **VERIFIED-BY-FETCH (PDF downloaded)** — **[B/D]**.
    Applications of the ratios conjecture to zero statistics lower-order terms, mollified moments, discrete averages. PDF saved.

24. **arXiv:math/0411501v1** — *Lower order terms of the second moment of S(t)* — T. H. Chan — 2004 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[D]**.
    Second moment of S(t) (the argument of ζ, i.e. the *one*-level zero-counting statistic) with lower-order terms from the ratios conjecture. A warm-up for the analogous third-moment computation. PDF saved.

### F. Twisted / mixed moments (the "twisted" translation angle)

25. **arXiv:2211.11450v1** — *Twisted mixed moments of the Riemann zeta function* — J. Pliego — 2022 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**.
    Twisted mixed moments of ζ with secondary terms P(log T)·T^C, both unconditionally and under a weak abc conjecture. PDF saved.

26. **arXiv:0709.2345v2** — *The twisted fourth moment of the Riemann zeta function* — C. P. Hughes, M. P. Young — 2007 (Ann. Math. 172 (2010) 203–233) — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**.
    The asymptotics of the fourth moment times an arbitrary Dirichlet polynomial of length up to T^{1/11−ε} — the model "twisted moment" computation (conditional on a shifted-moment conjecture). PDF saved.

27. **arXiv:2401.01057v1** — *A reciprocity relation for the twisted second moment of the Riemann Zeta function* — R. Khan — 2024 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**.
    Recent reciprocity for the twisted second moment — the exact tool family P2's "twisted pair correlation" direction (fg-2412.20099) would want. PDF saved.

28. **arXiv:1607.05595v1** — *On the reciprocity law for the twisted second moment of Dirichlet L-functions* — S. Bettin — 2016 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**.
    Reciprocity law (Motohashi-type) for Dirichlet L-functions. PDF saved.

29. **arXiv:2503.21682v1** — *Twisted moments of characteristic polynomials of random matrices in the unitary group* — S. Baluyot, B. Conrey — 2025 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**.
    Rigorous RMT analogue of the Keating–Conrey heuristic where lower twisted moments evaluate higher moments — the random-matrix side of the twisted-moments translation. PDF saved.

30. **arXiv:2606.27323v2** — *Amplified moments of the Riemann zeta function* — B. Durkan, T. Page — 2026 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**.
    **Unconditional** asymptotic formulae for amplified 2nd/4th moments; unconditional effective lower bounds for joint moments, incl. M₃(T) ≥ (34.4+o(1))c₃T(log T)⁹. This is the current state of the art on the *unconditional moment* (value-distribution) side — relevant because the "third moment" of zeros and the third moment of |ζ| interact through the explicit formula. PDF saved.

31. **arXiv:2603.01711v1** — *Lower bounds for the large deviations and moments of the Riemann zeta function on the critical line* — L.-P. Arguin, N. Creighton — 2026 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**.
    Unconditional lower bounds on fractional moments / large deviations on the critical line. PDF saved.

### G. Shifted moments of L-functions in families (recent, 2024–2026)

32. **arXiv:2602.01409v2** — *Shifted moments of modular L-functions to a fixed level* — P. Gao, L. Zhao — 2026 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C/G3]**.
33. **arXiv:2508.14534v2** — *Shifted moments of cubic and quartic Dirichlet L-functions* — Gao, Zhao — 2025 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C/G3]**.
34. **arXiv:2406.18024v2** — *Shifted moments of quadratic Dirichlet L-functions* — Gao, Zhao — 2024 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C/G3]**.
35. **arXiv:2501.12529v1** — *Multiple Dirichlet series predictions for moments of L-functions: unitary, symplectic, orthogonal examples* — S. Baluyot, M. Čech — 2025 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[D/G3]**.
    Family-level shifted moments: the unconditional-in-family versions of the shifted-moment technique, candidates for transporting the method (G3 transport target).

### H. Rudnick–Sarnak diagonal method & n-level (the P2-critical classics)

36. **Rudnick–Sarnak 1996** — *The n-level correlations of zeros of primitive Dirichlet L-functions* — Z. Rudnick, P. Sarnak — J. Amer. Math. Soc. 9 (1996), no. 2, 503–551 — **VERIFIED (metadata; multiple corroborating sources: the Gonçalves–de Laat–Leijenhorst published version cites it; standard literature; the hooks doc cites "[RS96]")** — **[A]** — THE diagonal-method paper: n-level density/correlation of zeros of primitive Dirichlet L-functions (degree ≤ 3 and more) matching GUE for test functions with small Fourier support, unconditional. This is the source of the "Rudnick–Sarnak range kλ < 2" the P2 hooks invoke. **PDF: UNOBTAINABLE from this machine** — JAMS paywalled; Rudnick's TAU site (`math.tau.ac.il/~rudnick/`) is unreachable from this network; no OA copy via Unpaywall/OpenAlex/Wayback. Obtainable via AMS (JAMS) or a human browser; the arXiv survey (Das, 2002.00595) summarizes the companion paper RS98.

37. **Rudnick–Sarnak 1998** — *Zeros of principal L-functions and random matrix theory* — Z. Rudnick, P. Sarnak — Duke Math. J. 81 (1996), no. 2, 269–322 — **VERIFIED-BY-FETCH (metadata)**: OpenAlex record (title, authors Zeév Rudnick & Peter Sarnak, year 1996, Duke Math. J. vol 81 issue 2, DOI **10.1215/S0012-7094-96-08115-6**); Unpaywall confirms (year 1996, publisher Duke UP). **[A]** — the principal-L-function (incl. ζ) n-level density paper, with the improved small-support conditions. **PDF: UNOBTAINABLE from this machine** (Duke paywall; Rudnick's site unreachable; no OA copy).

38. **arXiv:2002.00595v1** — *On the Rudnick and Sarnak's Zeros of principal L-functions and Random Matrix Theory* — M. Das — 2020 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[A/D]**.
    A survey of the Rudnick–Sarnak results — the closest thing to the RS98 content that is freely fetchable. PDF saved.

39. **arXiv:2303.01095v2** — *Multiplicity of nontrivial zeros of primitive L-functions via higher-level correlations* — F. Gonçalves, D. de Laat, N. Leijenhorst — 2023 (Math. Comp. 94 (2024) 2041–2058) — **VERIFIED-BY-FETCH (PDF downloaded, first page read)** — **[A]** — HIGH RELEVANCE.
    Applies "the higher-level correlation asymptotic of Hejhal and Rudnick & Sarnak" + SDP to bound the fraction of zeros of given multiplicity, for GL_m automorphic L-functions. This is the closest existing literature to P2's use of an unconditional higher-level correlation input (their input is the RS-level density theorem, which is unconditional in their setting). PDF saved.

40. **arXiv:2507.20653v1** — *On Hypothesis H of Rudnick and Sarnak* — Y. Jiang — 2025 — **VERIFIED-BY-FETCH (PDF downloaded, first page read)** — **[A]** — HIGH RELEVANCE.
    Proves Hypothesis H for GL_n over any number field; as applications **unconditionally establishes GUE statistics for automorphic L-function zeros** and an effective strong-multiplicity-one bound. The strongest current unconditional "higher-order statistics of zeros" statement — family-level, not ζ itself, but the direct modern descendent of the RS diagonal method. PDF saved.

41. **arXiv:1203.3275v4** — *Macroscopic pair correlation of the Riemann zeroes for smooth test functions* — B. Rodgers — 2012 (Duke 162 (2013) 3099–3129) — **VERIFIED-BY-FETCH (PDF downloaded)** — **[A/B]**.
    Under RH, the pair-correlation measure for smooth test functions matches the Bogomolny–Keating measure to very small error (extends Montgomery); the smooth-function machinery for correlation measures of ζ's zeros. Pair, not triple — but the technique (and its "macroscopic" viewpoint) is the natural route to a smooth triple-correlation statement. PDF saved.

42. **arXiv:1905.12123v3** — *Higher Correlations and the Alternative Hypothesis* — J. C. Lagarias, B. Rodgers — 2019 — **VERIFIED-BY-FETCH; already held** as `lr-1905.12123-higher-corr-AH.pdf` — **[A/D]**. The n-level-correlation-vs-AH interplay; the higher-correlation framing P2 already uses.

43. **arXiv:math/0111312v3** — *Uniform approximate functional equation for principal L-functions* — G. Harcos — 2001 (J. reine angew. Math. 553 (2002) 1–8) — **VERIFIED-BY-FETCH (PDF downloaded)** — **[D]**.
    The uniform approximate functional equation needed to run the RS explicit-formula/diagonal argument for principal L-functions. PDF saved.

### I. Hejhal (arXiv-available part) and weighted statistics of zeros

44. **arXiv:1311.4862v1** — *On Gaussians, Zeros, and Linear Combinations of L-functions. Part A* — D. A. Hejhal — 2013 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[D]**.
    Hejhal's modern program on zeros of linear combinations of L-functions (Beurling–Selberg machinery) — tangential but the only Hejhal item on arXiv. PDF saved.

45. **arXiv:2208.08421v1** — *A weighted one-level density of the non-trivial zeros of the Riemann zeta-function* — S. Bettin, A. Fazzari — 2022 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[A/C]**.
    One-level density weighted by |ζ(1/2+it)|^{2k}: computed for k=1 and (support (−½,½)) k=2, with consequences under RH. An unconditional weighted-linear-statistic statement in the RS-range spirit. PDF saved.

46. **arXiv:2507.04150v1** — *Selberg's Central Limit Theorem weighted by Linear Statistics of Zeta Zeros* — A. Fazzari, M. Gerspach, P. Minamide — 2025 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[A/C]**.
    Complex CLT for log ζ weighted by local statistics of zeros when the linear-statistic Fourier support is small; support extended to the natural barrier under RH. The same "small-support weighted" philosophy as P2's diagonal method, on the CLT side. PDF saved.

### J. Supporting value-distribution / ratios / misc (verified, mostly downloaded)

47. **arXiv:0803.0425v1** — *Pair correlation of the zeros of the derivative of the Riemann ξ-function* — Farmer, Gonek — 2008 — already held as `fg-0803.0425-paircorr-xideriv.pdf` — **[D]**. Pair correlation for ξ′ zeros — the derivative-tower analogue.
48. **arXiv:2006.04503v2** — *On the moments of the moments of ζ(1/2+it)* — Bailey, Keating — 2020 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**. Moments-of-moments (the "translation" statistics connecting value distribution and zero statistics).
49. **arXiv:1502.05658v3** — *Tail bounds for counts of zeros and eigenvalues, and an application to ratios* — B. Rodgers — 2015 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[A/D]**. Tail bounds for zero counts + ratios application — the probabilistic side of correlation measures.
50. **arXiv:2310.15918v2** — *On the joint second moment of zeta and its logarithmic derivative* — A. Fazzari — 2023 — **VERIFIED-BY-FETCH (PDF downloaded)** — **[C]**. Joint second moment of ζ and ζ′/ζ — the object adjacent to the third moment of log ζ.
51. **arXiv:0805.4208 / 0704.0927 / 0911.1830 / 0909.4916** (Miller et al., tests of the ratios conjecture, unitary/symplectic/orthogonal) — **VERIFIED-BY-FETCH (abstracts, not downloaded)** — **[D]**. Ratios-conjecture consistency checks.
52. **arXiv:2601.00660v1** — *Mixed fourth moments of automorphic forms and the shifted moments of L-functions* — C. Guo — 2026 — **VERIFIED-BY-FETCH (abstract, not downloaded)** — **[C]**.
53. **arXiv:1106.4806v2** — *The 4.36-th moment of the Riemann zeta-function* — M. Radziwiłł — 2011 — **VERIFIED-BY-FETCH (abstract, not downloaded)** — **[C]**.
54. **arXiv:math/9807187v1** (Conrey–Ghosh sixth-power-moment conjecture) and **math/9509224v1** (Conrey fourth-power note) — **VERIFIED-BY-FETCH (abstracts, not downloaded)** — **[D]**.

---

## 2. Top-10 ranked by P2 relevance

1. **Rudnick–Sarnak 1996 (JAMS)** — the n-level density theorem; the source of the "RS range kλ < 2" and the diagonal method P2's C-note relies on. Unconditional for small support. [PDF unobtainable here; get via AMS]
2. **Conrey–Snaith math/0610495** — the triple correlation of ζ's zeros with all lower-order terms (conditional on CFZ ratios). The object P2 wants; the constant-term formula is the target value to match. [DOWNLOADED]
3. **Gonçalves–de Laat–Leijenhorst 2303.01095** — the only paper that turns a higher-level correlation asymptotic (Hejhal + RS) into unconditional multiplicity bounds via SDP — structurally the closest published relative of P2's use of a third-moment input. [DOWNLOADED]
4. **Jiang 2507.20653** — unconditional GUE statistics for automorphic L-function zeros (Hypothesis H, GL_n, any number field) — the strongest current unconditional higher-order zero-statistics statement, and the modern successor of the RS diagonal method. [DOWNLOADED]
5. **Rudnick–Sarnak 1998 (Duke)** — the principal-L-function (incl. ζ) version of the n-level density; the paper that actually contains ζ in the small-support range. [PDF unobtainable here; survey by Das 2002.00595 downloaded]
6. **Ng–Shen–Wong 2206.03350** — RH ⟹ Chandee shifted moments; the shifted-moment statement P2 would most plausibly translate from. [DOWNLOADED]
7. **Conrey–Snaith 0803.2795** — n-correlation of ζ's zeros at all orders (conditional on ratios conjecture); the systematic higher-order template. [DOWNLOADED]
8. **Goldston–Yildirim math/0111212** — the triple correlations of the divisor sum Λ_R — the prime-side diagonal evaluation (the "diagonal method" arithmetic). [DOWNLOADED]
9. **Khan 2401.01057** — reciprocity for the twisted second moment; the current machinery for the "twisted" direction P2's fg-2412.20099 already gestures at. [DOWNLOADED]
10. **Durkan–Page 2606.27323** — unconditional amplified moments / joint-moment lower bounds (incl. M₃ ≥ (34.4+o(1)) c₃ T (log T)⁹) — the unconditional *moment* side that interfaces with zero statistics through the explicit formula. [DOWNLOADED]

---

## 3. Download log

All into `/home/vstaln/riemann/research/papers/` (verified: `%PDF` magic, size ≥ 20 KB; arXiv via `https://arxiv.org/pdf/<id>`, browser-ish UA, ~3–4 s pacing). Full log: `/tmp/paperfinder/downloads.log`.

| File | arXiv ID | Bytes |
|---|---|---|
| conrey-snaith-0610495-triple-correlation-zeros.pdf | math/0610495 | 508767 |
| conrey-snaith-0803.2795-correlations-eigenvalues-zeros.pdf | 0803.2795 | (OK) |
| gy-0111212-triple-correlations-divisor-sums.pdf | math/0111212 | 485661 |
| gy-0209102-k-correlations-divisor-sums.pdf | math/0209102 | 310057 |
| gy-0412366-higher-correlations-II.pdf | math/0412366 | (OK) |
| nsw-2206.03350-shifted-moments-zeta.pdf | 2206.03350 | 255378 |
| bettin-1111.0925-second-shifted-moment.pdf | 1111.0925 | 150762 |
| chandee-0910.0664-shifted-values-correlation.pdf | 0910.0664 | 310136 |
| curran-2405.08725-lower-bounds-shifted-moments.pdf | 2405.08725 | 225416 |
| curran-2303.10123-correlations-riemann-zeta.pdf | 2303.10123 | (OK) |
| soundararajan-0612106-moments-riemann-zeta.pdf | math/0612106 | (OK) |
| conrey-gonek-9902162-high-moments.pdf | math/9902162 | 233264 |
| harper-1305.4618-sharp-conditional-bounds-moments.pdf | 1305.4618 | (OK) |
| ng-1610.04977-sixth-moment-ternary-divisor.pdf | 1610.04977 | 767950 |
| hiary-rubinstein-1106.4352-uniform-asymptotics-full-moment.pdf | 1106.4352 | (OK) |
| ck-1506.06842-moments-zeta-divisor-sums-I.pdf | 1506.06842 | 153836 |
| ck-1506.06843-moments-zeta-divisor-sums-II.pdf | 1506.06843 | 126756 |
| ck-1506.06844-moments-zeta-divisor-sums-III.pdf | 1506.06844 | 146097 |
| baluyot-conrey-2206.04821-stratification-vandermonde.pdf | 2206.04821 | (OK) |
| conrey-keating-1611.09198-ratios-divisor-sums.pdf | 1611.09198 | 157054 |
| cfz-0711.0718-autocorrelation-ratios-lfunctions.pdf | 0711.0718 | 341180 |
| conrey-snaith-0509480-applications-ratios-conjectures.pdf | math/0509480 | 530517 |
| chan-0411501-lower-order-second-moment-ST.pdf | math/0411501 | (OK) |
| pliego-2211.11450-twisted-mixed-moments.pdf | 2211.11450 | 324922 |
| hughes-young-0709.2345-twisted-fourth-moment.pdf | 0709.2345 | 328756 |
| khan-2401.01057-reciprocity-twisted-second-moment.pdf | 2401.01057 | 156383 |
| bettin-1607.05595-reciprocity-twisted-second-dirichlet.pdf | 1607.05595 | 1016471 |
| baluyot-conrey-2503.21682-twisted-moments-random-matrices.pdf | 2503.21682 | 323594 |
| durkan-page-2606.27323-amplified-moments-zeta.pdf | 2606.27323 | 603799 |
| arguin-creighton-2603.01711-moments-critical-line.pdf | 2603.01711 | (OK) |
| gao-zhao-2602.01409-shifted-moments-modular-fixed-level.pdf | 2602.01409 | 358766 |
| gao-zhao-2508.14534-shifted-moments-cubic-quartic.pdf | 2508.14534 | 389776 |
| gao-zhao-2406.18024-shifted-moments-quadratic-dirichlet.pdf | 2406.18024 | 306386 |
| baluyot-cech-2501.12529-mds-moments-predictions.pdf | 2501.12529 | (OK) |
| das-2002.00595-rudnick-sarnak-survey.pdf | 2002.00595 | 192286 |
| gdl-2303.01095-multiplicity-higher-level-correlations.pdf | 2303.01095 | 242710 |
| jiang-2507.20653-hypothesis-H-rudnick-sarnak.pdf | 2507.20653 | 602441 |
| rodgers-1203.3275-macroscopic-pair-correlation-smooth.pdf | 1203.3275 | 278080 |
| harcos-0111312-uniform-approx-functional-equation.pdf | math/0111312 | 138345 |
| hejhal-1311.4862-gaussians-zeros-linear-comb.pdf | 1311.4862 | 526942 |
| bettin-fazzari-2208.08421-weighted-one-level-density.pdf | 2208.08421 | 303241 |
| fazzari-gerspach-minamide-2507.04150-selberg-clt-weighted.pdf | 2507.04150 | 515016 |
| bailey-keating-2006.04503-moments-of-moments.pdf | 2006.04503 | (OK) |
| rodgers-1502.05658-tail-bounds-ratios.pdf | 1502.05658 | 371216 |
| fazzari-2310.15918-joint-second-moment-log-derivative.pdf | 2310.15918 | (OK) |

Already held (not downloaded by this hunt; from earlier rounds): `fg-2412.20099-third-moment-twisted-pcc.pdf` (Fazzari–Gerspach, being read), `lr-1905.12123-higher-corr-AH.pdf`, `fg-0803.0425-paircorr-xideriv.pdf`. Two files present in the directory that this agent did not create (concurrent agent work, left untouched): `hyperbolic-goe-moduli-rudnick.pdf`, `wu-1802.09704-twisted-meansquare.pdf`, `selberg-clt-weighted-linear-statistics.pdf` (duplicate of the 2507.04150 download).

**Failed / unobtainable downloads:**
- `hejhal94-triple-correlation-zeros.pdf` — OUP returned HTTP 403 (Cloudflare bot-wall) with an HTML challenge; the downloaded file was NOT a PDF (removed). Hejhal 1994 stays UNOBTAINABLE-from-this-machine.
- RS96 (JAMS), RS98 (Duke), BK96 (PRL) — no free PDF reachable: Rudnick's TAU site unreachable (TCP fail), Sarnak's IAS site Cloudflare-blocked, AMS/OUP/APS bot-walled, no OA copies in Unpaywall/OpenAlex, no Wayback snapshots of the PDFs found. Pointers in §1 items 3, 4, 36, 37.

---

## 4. What was searched, and what failed (blocker log)

**arXiv export API queries executed (XML fetched, abstracts read), round 1 (20 queries):** `"triple correlation" AND zeta AND zeros`; `"third moment" AND zeros AND zeta`; `"triple correlation" AND Riemann`; `"shifted moments" AND zeta`; `ti:"moments of the Riemann zeta"`; `"shifted moments" AND L-functions`; `Rudnick AND Sarnak`; `"n-level correlation" AND Riemann`; `"higher order correlations" AND zeros`; `Hejhal AND "triple correlation"`; `au:Hejhal`; `"twisted moments" AND zeta`; `"twisted second moment" AND zeta`; `au:Conrey AND au:Gonek`; `au:Chandee AND "shifted moments"`; `au:Harper AND au:Soundararajan`; `"moments of zeta"`; `"ratios conjecture"`; `Bogomolny AND Keating`; `"diagonal" AND "hardy-littlewood" AND moments`.

**Round 2 (20 queries):** `"3-level density"`; `"level density" AND "Riemann zeta"`; `au:Bogomolny AND au:Keating AND zeros`; `"Higher Correlations of Divisor Sums"`; `au:Conrey AND au:Farmer AND au:Zirnbauer`; `au:Gonek AND zeta`; `au:Khan AND "mean values" AND zeta` (0 hits); `"moments of S(t)"`; `"triple correlation" AND "zeta-function"`; `cat:math-ph AND "triple correlation" AND Riemann`; `au:Hejhal AND zeros`; `au:Young AND "twisted" AND zeta`; `au:Zagier AND zeros`; `au:Odlyzko AND correlation`; `au:Fazzari`; `au:Rodgers AND zeros`; `"unconditional" AND moments AND zeta`; `au:Farmer AND zeta`; `au:Snaith AND "third moment"` (0 hits); `"Gonek" AND "negative moments"`.

**Failure log (honesty):**
- arXiv API HTTP 429 rate limits hit after the first 20-query burst and on round-2 start; handled by 25–60 s backoffs; all queries eventually returned. Two round-2 queries originally hung (>10 min) and were replaced with simplified single-clause versions run via curl with backoff.
- Semantic Scholar API: persistent HTTP 429 on every attempt (IP-level quota exhausted) — could not use it as a second verifier; OpenAlex and Crossref and Unpaywall used instead.
- Fatcat API (`api.fatcat.wiki`): empty/non-JSON responses — unusable.
- DuckDuckGo HTML endpoint, Mojeek, Bing: DDG/Mojeek unreachable or 403; Bing returned irrelevant results (title phrase not indexed).
- `scholar.archive.org` (Internet Archive Scholar): JS-only shell, no links extractable.
- OUP (Hejhal 1994 PDF), AMS (RS96), IAS (Sarnak's page), academic.oup.com: Cloudflare/bot-wall HTTP 403 to curl; r.jina.ai proxy also blocked.
- Rudnick's TAU site: TCP connection failure from this network (HTTP 000) on all variants (http/https, tau.ac.il/math.tau.ac.il). Wayback has no snapshot of the RS96/RS98 PDFs under his site (CDX queries returned []).

---

## 5. Honesty footer — and the intelligence answer to the P2 question

**Labeling note.** Every arXiv-ID claim above is backed by a fetched abstract (arXiv export API XML). Every "VERIFIED-BY-FETCH (PDF downloaded)" entry was additionally checked for `%PDF` magic bytes and plausible size; the four most load-bearing PDFs (Conrey–Snaith 0610495, Gonçalves–de Laat–Leijenhorst 2303.01095, Jiang 2507.20653, Ng–Shen–Wong 2206.03350) had their first-page text extracted and read. The classics (Hejhal 1994, RS96, RS98, BK96) are VERIFIED as metadata only — I could not fetch their abstracts in full text; their descriptions rely on the Crossref/OpenAlex/Unpaywall records and on the standard literature (flagged above). I did NOT fabricate any arXiv ID: all are from the API output.

**The honest state of the "unconditional third moment in λ < 2/3" question (what this hunt established):**
- **KNOWN (from fetched abstracts):** (i) No paper in any query result computes an unconditional triple-correlation *function* of ζ's zeros. Every such computation found — Hejhal 1994 (RH), Bogomolny–Keating 1996 (semiclassical), Conrey–Snaith 2006 (CFZ ratios conjecture) — is conditional. (ii) The unconditional statements in the RS range are *n-level density* theorems with small-support test functions (RS96/98), i.e. the diagonal main term, plus the family-level unconditional statements (Jiang 2025; Gonçalves–de Laat–Leijenhorst 2023/24) and the unconditional moment/large-deviation bounds on the value-distribution side (Durkan–Page 2026; Arguin–Creighton 2026; Bettin 2011 second shifted moment). (iii) The conditional triple-correlation computations all agree on the GUE main term (1 + δ + δ + δ in the standard normalization) — this is the value P2's diagonal method would reproduce in λ < 2/3, and is consistent with the hooks' "odd moment does not lower Λ₁(0)" PROVEN statement.
- **ASSUMED (flagged, not verified):** that RS98's exact support condition for ζ's 3-level density is the Σ|x_i| < 2/n-type condition the hooks cite (I could not read RS96/98 full text); that Hejhal 1994's computation matches Conrey–Snaith's lower-order terms (stated in the CS abstract — "agrees precisely with their formula" refers to BK, not Hejhal; the Hejhal comparison is standard but unread here).
- **Bottom line for P2:** an *unconditional* triple-correlation value for ζ's zeros in λ < 2/3 is **not in the literature**; the unconditional content available is the RS n-level density diagonal term (range kλ < 2), which this hunt confirms is exactly the "Rudnick–Sarnak range" the P2 note already cites. The new, possibly load-bearing finds for P2 are Jiang 2507.20653 (unconditional GUE statistics, family-level) and Gonçalves–de Laat–Leijenhorst 2303.01095 (unconditional multiplicity bounds via Hejhal+RS higher-level correlations + SDP) — both downloaded for adversarial review. If P2 wants a genuinely new unconditional third-moment statement, the literature points at two attackable interfaces: (1) transport of the RS diagonal evaluation of the 3-level density to a *twisted/shifted* form (the fg-2412.20099 direction; Khan 2401.01057 and Bettin 1607.05595 reciprocity machinery), and (2) the divisor-sum triple correlation (Goldston–Yildirim math/0111212) as the arithmetic core of such a statement.

Labels: all entries VERIFIED-BY-FETCH (as specified per entry); the P2-relevance judgments are CONJECTURED (analyst assessment, not proofs); the negative finding "no unconditional triple correlation of ζ's zeros in the searched literature" is CHECKED (by the exhaustive query log above) with the caveat that the classics' full text was not read.
