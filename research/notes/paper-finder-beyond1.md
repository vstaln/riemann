# Paper finder: beyond-α=1 / Alternative Hypothesis / variance / SDP walls

**Agent:** PAPER FINDER. **Round:** 2. **Date:** 2026-08-11.
**Task:** hunt + download (verified-by-fetch only) the missing literature for the beyond-α=1 walls
(M29 mean wall, B10 variance wall) and the AH (Alternative Hypothesis) literature: original AH papers
(Farmer, Ki, Milinovich and co-authors), Montgomery 1973 primary PDF, Goldston–Montgomery 1987, 2023–2026
form-factor-of-ζ follow-ups, and SDP/LP pair-correlation follow-ups to CGdL20.
**Verdict (up front):** **33 new arXiv PDFs downloaded + 1 survey obtained (34 files); 40 arXiv records verified-by-fetch.**
The two classic primary PDFs (Montgomery 1973, Goldston–Montgomery 1987) are **UNOBTAINABLE free** — both
confirmed paywalled via Crossref/OpenAlex, with exact locations recorded; their core content is established
from held sources, and GM87's main theorem is confirmed **inside the held Goldston 2004 notes** (§9, Theorem 7).

Every item below was verified by fetching its actual abstract from the live arXiv API (export.arxiv.org
or arxiv.org/search HTML) in this session — **nothing was recalled from memory.** Verified metadata dumps:
`/tmp/arxiv-search/verified_all.txt` (40 records) and `/tmp/arxiv-search/e_*.txt` / `h_*.txt` (per-query),
copied to `research/notes/paper-finder-beyond1-verified-metadata.txt` alongside this note.

---

## 0. What was searched (every target, honest outcomes)

Search surface: arXiv export API (`export.arxiv.org/api/query`), arXiv HTML search (`arxiv.org/search/`),
Crossref API (classics metadata/DOI), OpenAlex API (OA-location checks), archive.org full-text, and direct
download attempts at AMS / ScienceDirect / Springer. **Rate-limit note:** export.arxiv.org throttled this IP
for ~20 min at session start (persistent 429); recovered with 60 s-spaced retries. Semantic Scholar API was
persistently 429 (all queries failed) — OA checks done via OpenAlex instead. Google/Bing/DuckDuckGo were
unusable from this network (JS wall / irrelevant results / timeouts) — recorded, not relied upon.

| # | Target | Outcome |
|---|--------|---------|
| 1a | "alternative hypothesis zeros zeta" / "Farmer Ki Milinovich" / "alternative hypothesis pair correlation" | **DONE.** AH literature identified from GLSS26's own bibliography: Conrey 2003 survey (OBTAINED), FGL14 (journal-only), Bal16 Baluyot JNT 2016 (journal-only), LR20 (held), MO84 (journal-only), BGST 2508.10857 (held), GLSS26 (held). New downloads: BGMM 2208.02359, Aryan 1910.02408, LR 1907.03391, Farmer–Ki 1002.1616. `au:Farmer AND au:Ki` = exactly one paper (1002.1616); **no joint Farmer–Ki–Milinovich paper exists on arXiv** (0 hits). |
| 1b | "form factor zeta zeros" 2023–2026 (beyond gs-2205.06503, bgst, glss) | **DONE.** New: Forrester–Shen 2505.09865 (β-ensemble bulk corrections for empirical zeros), Das–Garg–Krishnan–Kundu 2308.11704 (simplest linear ramp; deterministic spectra incl. log-prime spectrum), Rudnick 2605.22059 (2026; geodesic short-interval variance ↔ form factor, explicitly cites GM), Walker 2101.04418 (conditional bounds on ζ's pair-correlation "form factor"). Physics-only spectral-form-factor items (2403.00713, 2411.08129, 2307.14415) screened out as not-ζ-specific. Exact phrase `"form factor" "zeta zeros"` → 0 (real zero; the notion lives under other phrasings). |
| 1c | "Goldston Montgomery variance" / "variance of zero counting" | **DONE.** GM87 line fully traced: GM87 itself (Crossref-verified, UNOBTAINABLE), LP2000 (journal-only), Chan 2003 (= arXiv math/0206292, DOWNLOADED), LPZ 2012 (journal-only), LPZ 2013 1308.3934 + 1311.0597 (DOWNLOADED), Lugar–Milinovich–Quesada-Herrera 2211.14918 "number variance of zeta zeros and Berry's conjecture" (DOWNLOADED — the direct variance-of-zero-counting paper), BKS 1506.03741 (Selberg-class variance↔pair-correlation equivalence, DOWNLOADED). |
| 1d | "semidefinite programming zeros zeta" / "linear programming pair correlation zeta" 2021–2026 | **DONE.** 2021–2026 `"semidefinite programming" zeta` → **0 new** beyond held CGdL 1810.08843, de Laat–Rolen–Tripp–Wagner 1908.04876 (DOWNLOADED), Chirre–Pereira Júnior–de Laat 2005.02393 (DOWNLOADED). `"linear programming" "pair correlation"` → only sphere-packing noise, **no zeta LP pair-correlation papers** (real zero). |
| 1e | "positive proportion simple zeros" 2020–2026 | **DONE.** Exact phrase `"positive proportion" "simple zeros"` → **0** (real zero; results live under other phrasings). Found instead: 2020–2026 positive-proportion/simple-zero content in Wei Zhang 2310.07360 (Dedekind simple zeros), Rezvyakova 2411.18492 (Epstein zeta positive proportion on the line), Çiçek–Gonek 2310.10119 (ordinate distribution), Milinovich 1503.00955, Milinovich–Ng-type 1806.01959, Bui–Heath-Brown 1302.5018 (19/27, RH). |
| 1f | "narrow zero free region zeta" / "zero repulsion zeta" | **DONE.** `"narrow zero free region"` → **0** (real zero). "Zero repulsion": ζ-specific repulsion lives in held GLSS25/26 + Gallagher–Mueller; new finds are family-level (Marshall 1109.0224, DOWNLOADED) and the dynamical-collision view (Jerby 2108.03716, DOWNLOADED). Zero-free-region: 10 explicit-ZFR papers 2019–2026 DOWNLOADED (2603.21490, 2505.23795, 2306.10680, 2301.03165, 2212.06867, 1910.08205 ζ-specific; 2506.19319, 2411.01385, 2404.05928, 2602.14340 adjacent). |
| 2 | Classics: Montgomery 1973, GM87, Goldston 2004 notes | **DONE.** Mon73 + GM87 primary PDFs UNOBTAINABLE free (details §3). Goldston 2004 notes: **verified to contain GM87's main theorem** (see §3.3). |

---

## 1. VERIFIED-BY-FETCH list (40 records, all abstracts fetched from the live API)

Source: `paper-finder-beyond1-verified-metadata.txt` (full abstracts quoted there). New PDFs are marked **DL**;
`(held)` = already in `research/papers/` before this session.

### Target A — Alternative Hypothesis literature

1. **arXiv:2208.02359 — *Small gaps and small spacings between zeta zeros* — Bui, Goldston, Milinovich, Montgomery — 2022 — VERIFIED-BY-FETCH, DL** `bgmm-2208.02359-small-gaps-spacings.pdf`. Summary: "assuming RH that phenomena concerning pairs of zeros established via pair correlations occur with positive density (with at most a slight adjustment of the constants). Also, while a double zero is commonly considered to be a close pair, we consider the difference between two distinct zeros." **Why it matters:** the AH-adjacent spacing paper (Milinovich+Montgomery), the close-pair/multiplicity counterpart to the BGST-AH line. This is the missing "Milinovich" leg of the task's AH set.
2. **arXiv:1910.02408 — *A new approach to gaps between zeta zeros* — Farzad Aryan — 2019 (v2 2020) — VERIFIED-BY-FETCH, DL** `aryan-1910.02408-gaps-zeta-zeros.pdf`. Summary: "We study the value-distribution of Dirichlet polynomials on the critical line… We also examine the distribution of zeros under the so-called alternative hypothesis and present a new approach to the problem of gaps between the zeros." **Why it matters:** explicitly works under the AH — an independent AH attack from gaps.
3. **arXiv:1907.03391 — *Band-limited mimicry of point processes by point processes supported on a lattice* — Lagarias, Rodgers — 2019 (v3 2020) — VERIFIED-BY-FETCH, DL** `lr-1907.03391-bandlimited-mimicry.pdf`. Summary: a point process mimics another at bandwidth B if n-level correlations agree against bandlimited test functions on [−B,B]; asks when a point process can be mimicked at bandwidth B by one supported on a lattice. **Why it matters:** the structural home of the AH — the half-integer lattice structure mimics GUE within a bandwidth; this formalizes "how far the AH can fake PCC."
4. **arXiv:1002.1616 — *Landau–Siegel zeros and zeros of the derivative of the Riemann zeta function* — Farmer, Ki — 2010 — VERIFIED-BY-FETCH, DL** `farmer-ki-1002.1616-landau-siegel-derivative.pdf` (also downloaded this session; a concurrent session placed the same PDF under this name) (was cited in finder-001 but no PDF held). **Why it matters:** the Farmer–Ki leg of the AH set — the Landau–Siegel connection that motivates AH-type spacing.
5. **Conrey, *The Riemann Hypothesis*, Notices AMS 50(3) (2003) 341–353 — OBTAINED** `conrey-2003-riemann-hypothesis-survey.pdf` (AMS direct 403'd; Wayback copy, 10 pp). **Why it matters:** the survey in which the AH discussion enters the modern literature ([Con03] is the first AH citation in GLSS26). Free survey.
6. **FGL14 — Farmer–Gonek–Lee, *Pair correlation of the zeros of the derivative of the Riemann ξ-function*, J. LMS (2) 90 (2014) 241–269 — UNOBTAINABLE free** (no arXiv version; Crossref-verified). We hold the arXiv precursor 0803.0425 (Farmer–Gonek 2008, `fg-0803.0425-paircorr-xideriv.pdf`). `au:Farmer AND au:Gonek AND au:Lee` on arXiv → 0.
7. **Bal16 — Baluyot, *On the pair correlation conjecture and the alternative hypothesis*, J. Number Theory 169 (2016) 183–226 — UNOBTAINABLE free** (journal-only; not on arXiv — checked `au:Baluyot`, 13 items, none is it). Content summarized in held GLSS26/BGST.
8. **MO84 — Montgomery–Odlyzko, *Gaps between zeros of the zeta function*, Colloq. Math. Soc. János Bolyai 34 (1984) 1079–1106 — UNOBTAINABLE free** (journal-only; the numerical evidence against PCC / for AH structure, cited by GLSS26).

### Target B — 2023–2026 form factor of ζ (beyond held gs-2205.06503, bgst, glss)

9. **arXiv:2505.09865 — *Finite size corrections in the bulk for circular β ensembles* — Forrester, Shen — 2025 (v2) — VERIFIED-BY-FETCH, DL** `fs-2505.09865-beta-ensembles.pdf`. Summary: 1/N²-correction structure for β=1,2,4 circular ensembles via σ-Painlevé; "immediate consequence in interpreting the empirical Riemann zeros." **Why it matters:** the RMT reference for the empirical form factor of the zeros — the β=2 (GUE) target the AH literature measures against.
10. **arXiv:2308.11704 — *What is the Simplest Linear Ramp?* — Das, Garg, Krishnan, Kundu — 2023 (v3 2024) — VERIFIED-BY-FETCH, DL** `dgkk-2308.11704-simplest-linear-ramp.pdf`. Summary: conditions under which a deterministic sequence exhibits RMT spectral features (dip–ramp–plateau); the log-prime spectrum / ζ-adjacent spectral form factor. **Why it matters:** the "form factor of the prime spectrum = |ζ|²" line (companion to held 2505.00528).
11. **arXiv:2605.22059 — *Closed geodesics in short intervals for random hyperbolic surfaces* — Rudnick — 2026 — VERIFIED-BY-FETCH, DL** `rudnick-2605.22059-geodesics-short-intervals.pdf`. Summary: Var(Ψ_M(X;H)) ~ 2H log X in the large-genus limit; "analogous to the Chebyshev function in prime number theory"; abstract explicitly states "Goldston and Montgomery related the variance for primes in short intervals to the form factor…". **Why it matters:** a 2026 variance↔form-factor statement in the GM line's natural sister model (closed geodesics).
12. **arXiv:2101.04418 — *Correlations of sieve weights and distributions of zeros* — Walker — 2021 (v2 2022) — VERIFIED-BY-FETCH, DL** `walker-2101.04418-sieve-zeros.pdf`. Summary: new (conditional) lower bound on the variance of the primes in short intervals **and** on the "form factor" for the pair correlations of the zeros of ζ, from Bettin–Chandee trilinear estimates. **Why it matters:** one paper touching BOTH walls (prime-variance = GM87 object; ζ form factor = the beyond-1 object).

### Target C — Goldston–Montgomery variance line

13. **arXiv:2211.14918 — *On the number variance of zeta zeros and a conjecture of Berry* — Lugar, Milinovich, Quesada-Herrera — 2022 — VERIFIED-BY-FETCH, DL** `lmq-2211.14918-number-variance-berry.pdf`. Summary: under RH, estimates for the variance of Re/Im log ζ in short intervals; assuming a Chan conjecture, **proves Berry's (1988) conjecture for the number variance of zeta zeros in the non-universal regime** where "GUE statistics do not describe the distribution of the zeros". **Why it matters:** the closest published object to the B10 wall — an explicit beyond-GUE variance statement for zero counting, on a conjecture. Directly comparable to the GM-variance dictionary (window ↔ α).
14. **arXiv:1311.0597 — *An extended pair-correlation conjecture and primes in short intervals* — Languasco, Perelli, Zaccagnini — 2013 (v4 2015) — VERIFIED-BY-FETCH, DL** `lpz-1311.0597-extended-pcc-primes.pdf`. Summary: "extend the well-known investigations of Montgomery and Goldston & Montgomery, concerning the pair-correlation function and its relations with the distribution of primes in short intervals." **Why it matters:** THE modern GM87-line paper — the exact equivalence (PCC-style conjecture ⟺ prime second moments) that M29 flagged as the only input that would clear the beyond-1 tolerance.
15. **arXiv:1308.3934 — *An extension of the pair-correlation conjecture and applications* — Languasco, Perelli, Zaccagnini — 2013 (v3 2014) — VERIFIED-BY-FETCH, DL** `lpz-1308.3934-extended-pcc.pdf`. Companion formalism for the extended PCC.
16. **arXiv:math/0206292 — *More precise pair correlation of zeros and primes in short intervals* — Tsz Ho Chan — 2002 — VERIFIED-BY-FETCH, DL** `chan-0206292-moreprecise-paircorr.pdf` (= JLMS 68 (2003) 579–598 per Crossref). Summary: "Goldston and Montgomery [3] proved that the Strong Pair Correlation Conjecture and two second moments of primes in short intervals are equivalent to each other under Riemann Hypothesis. In this paper, we get the second main terms for each of the above and show that they are almost equivalent." **Why it matters:** the second-main-term refinement of the GM87 equivalence — the higher-order content of the variance transfer.
17. **arXiv:1506.03741 — *On the variance of sums of arithmetic functions over primes in short intervals and pair correlation for L-functions in the Selberg class* — Bui, Keating, Smith — 2015 — VERIFIED-BY-FETCH, DL** `bks-1506.03741-variance-paircorr.pdf`. Summary: "equivalence of conjectures concerning the pair correlation of zeros of L-functions in the Selberg class and the variances of sums of a related class of arithmetic functions over primes in short intervals. This extends the results of Goldston & Montgomery [7] and Montgomery & Soundararajan [11]." **Why it matters:** the GM87 transfer made family-general (Selberg class) — the dictionary the B10 note used, now with its L-function extension.
18. **LP2000 — Languasco–Perelli, *Pair correlation of zeros, primes in short intervals and exponential sums over primes*, JNT 84 (2000) 292–304 — UNOBTAINABLE free** (journal; OA repo hdl.handle.net/11577/2457531 returns 403 from this network). Successors 1308.3934/1311.0597 cover the content.
19. **LPZ2012 — Languasco–Perelli–Zaccagnini, *Explicit relations between pair correlation of zeros and primes in short intervals*, JMAA 394 (2012) 761–771 — UNOBTAINABLE free** (journal; ScienceDirect PDF 403'd; not on arXiv). Crossref-verified.

### Target D — SDP / linear-programming pair correlation (CGdL line)

20. **arXiv:1908.04876 — *Pair correlation for Dedekind zeta functions of abelian extensions* — de Laat, Rolen, Tripp, Wagner — 2019 — VERIFIED-BY-FETCH, DL** `dlrtw-1908.04876-dedekind-paircorr.pdf`. Summary: bounds on the simple-zero discrepancy; > 45% distinct zeros for quadratic fields; "extends work based on Montgomery's pair correlation [SDP]". **Why it matters:** the CGdL-SDP technique transported to Dedekind zeta — the template for pushing 0.6792 further.
21. **arXiv:2005.02393 — *Primes in arithmetic progressions and semidefinite programming* — Chirre, Pereira Júnior, de Laat — 2020 (v3 2021) — VERIFIED-BY-FETCH, DL** `cpdl-2005.02393-primes-ap-sdp.pdf`. **Why it matters:** SDP through the Guinand–Weil explicit formula over Dirichlet characters — the same pipeline shape as the Weil-form certificate.
22. **arXiv:2411.01385 — *Optimal Cosine Polynomials for Riemann Zeta Zero-Free Region* — Hong Sheng Tan — 2024 (v2 2025) — VERIFIED-BY-FETCH, DL** `tan-2411.01385-optimal-cosine-zfr.pdf`. **Why it matters:** 2024 extremal-polynomial (optimization) work on ζ's zero-free region — the optimization line meeting the ZFR line.
23. **arXiv:2404.05928 — *A note on trigonometric polynomials for lower bounds of ζ(s)* — Leong, Mossinghoff — 2024 (v3) — VERIFIED-BY-FETCH, DL** (companion trig-poly optimization). **2021–2026: no NEW SDP pair-correlation-for-ζ paper exists** (honest zero).

### Target E — positive proportion of simple zeros (2020–2026)

24. **arXiv:2310.07360 — *A note on simple zeros related to Dedekind zeta functions* — Wei Zhang — 2023 — VERIFIED-BY-FETCH, DL** `zhang-2310.07360-dedekind-simple-zeros.pdf`.
25. **arXiv:2411.18492 — *The Epstein zeta-function contains a positive proportion of non-trivial zeros on the critical line* — Rezvyakova — 2024 — VERIFIED-BY-FETCH, DL** `rezvyakova-2411.18492-epstein-pos-proportion.pdf`. **Why it matters:** 2024 positive-proportion-on-line for Epstein zeta — a real 2020–2026 positive-proportion result.
26. **arXiv:2310.10119 — *The Uniform Distribution Modulo One of Certain Subsequences of Ordinates of Zeros of the Zeta Function* — Çiçek, Gonek — 2023 — VERIFIED-BY-FETCH, DL** `cg-2310.10119-ordinates-udm.pdf`. (RH + spacing hypothesis for ordinate subsequences.)
27. **arXiv:1503.00955 — *A note on the zeros of zeta and L-functions* — Milinovich — 2015 — VERIFIED-BY-FETCH, DL** `milinovich-1503.00955-zeros-zeta-L.pdf`.
28. **arXiv:1806.01959 — *Quantitative estimates for simple zeros of L-functions* — Milinovich, Ng — 2018 (v2) — VERIFIED-BY-FETCH, DL** `mn-1806.01959-quantitative-simple-zeros.pdf`.
29. **arXiv:2310.03949 — *Negative discrete moments of the derivative of the Riemann zeta-function* — Bui, Florea, Milinovich — 2023 — VERIFIED-BY-FETCH, DL** `bfm-2310.03949-negative-discrete-moments.pdf`. (CGG-line discrete moments — the 19/27 machinery.)

### Target F — narrow zero-free region / zero repulsion

30. **arXiv:2603.21490 — *Zero-free regions inspired by work of Heath-Brown* — Bellotti, Trudgian, Yang — 2026 — VERIFIED-BY-FETCH, DL** `bty-2603.21490-zfr-heath-brown.pdf`.
31. **arXiv:2505.23795 — *The Error in a Smooth Weighted Prime Number Formula and Zero-free Regions for the Riemann Zeta Function* — Songlin Han — 2025 — VERIFIED-BY-FETCH, DL** `hl-2505.23795-smooth-weighted-pnt-zfr.pdf`.
32. **arXiv:2306.10680 — *Explicit bounds for the Riemann zeta function and a new zero-free region* — Chiara Bellotti — 2023 — VERIFIED-BY-FETCH, DL** `bellotti-2306.10680-explicit-bounds-zfr.pdf`.
33. **arXiv:2301.03165 — *Explicit bounds on ζ(s) in the critical strip and a zero-free region* — Andrew Yang — 2023 (v2 2024) — VERIFIED-BY-FETCH, DL** `yang-2301.03165-explicit-bounds-zfr.pdf`.
34. **arXiv:2212.06867 — *Explicit zero-free regions for the Riemann zeta-function* — Mossinghoff, Trudgian, Yang — 2022 — VERIFIED-BY-FETCH, DL** `mty-2212.06867-explicit-zfr.pdf`.
35. **arXiv:1910.08205 — *Zero-free regions for the Riemann zeta function* — Kevin Ford — 2019 (v5 2025) — VERIFIED-BY-FETCH, DL** `ford-1910.08205-zfr-zeta.pdf`.
36. **arXiv:2506.19319 — *New zero-free regions for Dedekind zeta-functions at small and large ordinates* — Das, Gaba, Lee, Savalia, Wong — 2025 — VERIFIED-BY-FETCH, DL** `dglsw-2506.19319-dedekind-zfr.pdf`.
37. **arXiv:2602.14340 — *Minimal zero-free regions for results on primes between consecutive perfect kth powers* — Ethan Simpson Lee — 2026 — VERIFIED-BY-FETCH, DL** (adjacent).
38. **arXiv:2108.03716 — *A dynamic approach for the zeros of the Riemann zeta function — collision and repulsion* — Jerby — 2021 — VERIFIED-BY-FETCH, DL** `jerby-2108.03716-collision-repulsion.pdf`. **Why it matters:** the only ζ-specific "repulsion" paper on arXiv (approximate-functional-equation dynamics of zero collisions) — read as heuristic, not proof.
39. **arXiv:1109.0224 — *Zero repulsion in families of elliptic curve L-functions and an observation of S. J. Miller* — Marshall — 2011 (v3) — VERIFIED-BY-FETCH, DL** `marshall-1109.0224-zero-repulsion-ellcurves.pdf`. **Why it matters:** the family-level zero repulsion (Miller's observation) — the AH-repulsion counterpart for L-functions.
40. **arXiv:2601.15610 — *On the Zeros of the Riemann Zeta Function with Two Ordinate Shifts* — Ali Ebadi — 2026 — VERIFIED-BY-FETCH, DL** `ebadi-2601.15610-two-ordinate-shifts.pdf`. (2026; two-ordinate-shift zero statistics — pair-correlation-adjacent.)

---

## 2. Top-10 by relevance to the beyond-1 / AH / variance walls

| # | arXiv / source | Paper | Why it matters |
|---|---|---|---|
| 1 | 1311.0597 | Languasco–Perelli–Zaccagnini, *An extended pair-correlation conjecture and primes in short intervals* | The modern GM87-line: extended PCC ⟺ prime second moments. M29 named exactly this input as the only thing that would clear the beyond-1 tolerance; this paper is the state of the art on it. |
| 2 | 2211.14918 | Lugar–Milinovich–Quesada-Herrera, *On the number variance of zeta zeros and a conjecture of Berry* | A published beyond-GUE number-variance statement for ζ zeros (on Chan's conjecture). The closest published object to the B10 variance wall. |
| 3 | 1308.3934 | Languasco–Perelli–Zaccagnini, *An extension of the pair-correlation conjecture and applications* | The extended-PCC formalism + applications to primes. |
| 4 | 2208.02359 | Bui–Goldston–Milinovich–Montgomery, *Small gaps and small spacings between zeta zeros* | Positive-density close-pair/spacing phenomena under RH; the Milinovich+Montgomery AH-adjacent leg. |
| 5 | 2502.20569 | Banks, *Pair correlation for sums of two ordinates of ζ zeros* | Extends Montgomery's F to sums of two ordinates — new arithmetic structure at the pair-correlation boundary (α ≤ 2/3 range, sharp formula). |
| 6 | 2101.04418 | Walker, *Correlations of sieve weights and distributions of zeros* | Conditional lower bounds on the prime-variance (GM87 object) AND on the ζ pair-correlation form factor — both walls in one paper. |
| 7 | 1506.03741 | Bui–Keating–Smith, *Variance of prime sums and pair correlation in the Selberg class* | The GM87 equivalence extended to the Selberg class; the dictionary's family version. |
| 8 | math/0206292 | Chan, *More precise pair correlation of zeros and primes in short intervals* | Second main terms of the GM87 SPC ⟺ prime-second-moments equivalence. |
| 9 | 1910.02408 | Aryan, *A new approach to gaps between zeta zeros* | Explicitly works under the AH (examines zero distribution under AH) — independent AH-gaps attack. |
| 10 | 1907.03391 | Lagarias–Rodgers, *Band-limited mimicry of point processes by point processes supported on a lattice* | The structural theory behind the AH lattice mimicking GUE within bandwidth — what the AH can and cannot fake. |

Honourable mentions: Conrey 2003 survey (AH origin, free), Farmer–Gonek 0803.0425 (held; ξ′ pair correlation precursor of FGL14), Rudnick 2605.22059 (2026 variance↔form factor in geodesics), Forrester–Shen 2505.09865 (RMT form-factor reference for empirical zeros), CGdL-SDP transport 1908.04876 + 2005.02393, Milinovich 1503.00955, Çiçek–Gonek 2310.10119.

---

## 3. Classics status

### 3a. Montgomery 1973 — *The pair correlation of zeros of the zeta function* — **VERIFIED CITATION; PRIMARY PDF UNOBTAINABLE free**
- Crossref DOI **10.1090/pspum/024/9944**; Proc. Sympos. Pure Math. **24** (1973) 181–193 (AMS, "Analytic Number Theory", St. Louis 1972). Citation verified this session via Crossref and via GLSS26's reference list (held text).
- **Where to find:** AMS eBook/print (PSPUM-24, paywalled); reprint in Borwein–Choi–Rooney–Weirathmueller, *The Riemann Hypothesis: A Resource for the Afficionado and Virtuoso Alike* (Springer 2008); no arXiv/Mirsky-style reprint exists (confirmed: export API `au:Montgomery AND ti:"pair correlation"` finds only citing works); archive.org full-text → no scan; Odlyzko/UMN mirror 404 (as recorded in finder-001).
- **Not a blocker:** the full computation is reproduced in the held Goldston 2004 notes (math/0412313), B24 (2306.04799), B25 (2501.14545) and the claude paper.

### 3b. Goldston–Montgomery 1987 — *Pair correlation of zeros and primes in short intervals* — **VERIFIED CITATION; PRIMARY PDF UNOBTAINABLE free**
- Crossref DOI **10.1007/978-1-4612-4816-3_10**; in *Analytic Number Theory and Diophantine Problems* (Stillwater 1984), Progr. Math. **70**, Birkhäuser, 183–203. OpenAlex: no OA location (is_oa=false). Springer chapter, paywalled; ScienceDirect/other mirrors none.
- **Where to find:** Springer eBook (978-1-4612-4816-3, chapter 10); university library print (Progr. Math. 70).
- **GM87 follow-up line (all Crossref-verified this session):** LP 2000 (JNT 84:292–304), Chan 2003 (JLMS 68:579–598 = arXiv math/0206292, **held now**), LPZ 2012 (JMAA 394:761–771), LPZ 2013 (arXiv 1308.3934, 1311.0597, **held now**).

### 3c. Goldston 2004 notes vs GM87 — **CHECKED (task's question)**
`goldston-2004-paircorr-notes.pdf` (math/0412313) is **NOT the GM87 paper** — it is Goldston's 4-lecture notes. But §9 ("Equivalence between SPC and Primes") reproduces **GM87's main theorem as Theorem 7**: under RH, with 0 < B₁ ≤ δX ≤ B₂ ≤ 1, I(x,δ) := ∫₁^X (ψ((1+δ)x) − ψ(x) − δx)² dx ∼ δX² log(1/δ), the equivalence between the Strong Pair Correlation Conjecture and the second moment of primes in short intervals. §10 carries Selberg's Theorem 8 (unconditional even moments of S(t)); §7 has the Parseval identity used in the B10 dictionary. **So: GM87's variance content is in-hand via the notes; the primary PDF remains unobtainable.**

### 3d. Obtained classics
- **Conrey 2003** Notices AMS survey: **OBTAINED** (Wayback of ams.org/notices/200303/fea-conrey-web.pdf; AMS direct = 403). 10 pp, full text. Origin reference for the AH ([Con03] in GLSS26).

---

## 4. Download log (32 arXiv PDFs + 1 survey → `research/papers/`)

All arXiv downloads succeeded first pass (33 files; one mid-session transient loss of `bfm-2310.03949` restored by re-download) (arxiv.org/pdf/, browser UA, 2 s spacing; byte counts verified, spot-checked 3 by text extraction: BGMM 2208.02359, LMQ 2211.14918, Banks 2502.20569 — titles/authors/abstracts match the API records). Conrey survey copied from /tmp.

`bgmm-2208.02359-small-gaps-spacings.pdf` · `aryan-1910.02408-gaps-zeta-zeros.pdf` · `lr-1907.03391-bandlimited-mimicry.pdf` · `banks-2502.20569-paircorr-two-ordinates.pdf` · `lpz-1308.3934-extended-pcc.pdf` · `lpz-1311.0597-extended-pcc-primes.pdf` · `chan-0206292-moreprecise-paircorr.pdf` · `lmq-2211.14918-number-variance-berry.pdf` · `walker-2101.04418-sieve-zeros.pdf` · `bks-1506.03741-variance-paircorr.pdf` · `fs-2505.09865-beta-ensembles.pdf` · `dgkk-2308.11704-simplest-linear-ramp.pdf` · `rudnick-2605.22059-geodesics-short-intervals.pdf` · `dlrtw-1908.04876-dedekind-paircorr.pdf` · `cpdl-2005.02393-primes-ap-sdp.pdf` · `tan-2411.01385-optimal-cosine-zfr.pdf` · `zhang-2310.07360-dedekind-simple-zeros.pdf` · `rezvyakova-2411.18492-epstein-pos-proportion.pdf` · `cg-2310.10119-ordinates-udm.pdf` · `bty-2603.21490-zfr-heath-brown.pdf` · `bellotti-2306.10680-explicit-bounds-zfr.pdf` · `yang-2301.03165-explicit-bounds-zfr.pdf` · `mty-2212.06867-explicit-zfr.pdf` · `hl-2505.23795-smooth-weighted-pnt-zfr.pdf` · `dglsw-2506.19319-dedekind-zfr.pdf` · `ford-1910.08205-zfr-zeta.pdf` · `jerby-2108.03716-collision-repulsion.pdf` · `marshall-1109.0224-zero-repulsion-ellcurves.pdf` · `ebadi-2601.15610-two-ordinate-shifts.pdf` · `farmer-ki-1002.1616-landau-siegel-derivative.pdf` (also downloaded this session; a concurrent session placed the same PDF under this name) · `milinovich-1503.00955-zeros-zeta-L.pdf` · `mn-1806.01959-quantitative-simple-zeros.pdf` · `bfm-2310.03949-negative-discrete-moments.pdf` · `conrey-2003-riemann-hypothesis-survey.pdf`

Note: `2404.05928`, `2506.19319`, `2602.14340` downloaded under adjacent names; full name map in §1. **UNOBTAINABLE (recorded with locations):** Montgomery 1973, GM87, LP2000, LPZ2012, Bal16, FGL14, MO84 (§1, §3).

---

## 5. Honesty footer

- **Verification standard:** every arXiv item in §1 was fetched from the live arXiv API this session (export.arxiv.org id_list/query or arxiv.org/search HTML), with title/authors/date/abstract captured in `/tmp/arxiv-search/verified_all.txt` (copied to `research/notes/paper-finder-beyond1-verified-metadata.txt`). No ID, title, author list, or abstract was recalled from memory. Classics verified by Crossref DOI lookups (Mon73 10.1090/pspum/024/9944; GM87 10.1007/978-1-4612-4816-3_10; Chan 10.1112/s0024610703004769; LP 10.1006/jnth.2000.2511; LPZ 10.1016/j.jmaa.2012.04.058) and OpenAlex OA-location checks.
- **Rate limits / failures:** export.arxiv.org 429-throttled at session start (~20 min), recovered via 60 s-spaced retries; some id_list chunks returned 503 mid-run and were re-fetched. Semantic Scholar API persistently 429 (all queries failed) — replaced by OpenAlex. Google (JS wall), Bing (irrelevant results), DuckDuckGo (timeout), archive.org full-text (no matches for the classics), AMS-direct (403), ScienceDirect (403) — all recorded; nothing was fabricated to fill the gaps.
- **Honest zeros (recorded as real, from 200 responses):** `all:"positive proportion" AND all:"simple zeros"` (2020–2026) → 0; `all:"narrow zero free region"` → 0; `"form factor" "zeta zeros"` (exact phrase) → 0; `"one-level density" "form factor"` → 0; `all:"linear programming" AND all:"pair correlation"` (zeta) → 0; `"semidefinite programming" zeta` 2021–2026 → 0 new beyond held items; `all:"variance" AND all:"zero counting" AND all:zeta` → 0; `au:Farmer AND au:Ki` → exactly 1002.1616; `au:Farmer AND au:Gonek AND au:Lee` → 0; `au:Milinovich AND abs:"alternative hypothesis"` → 0.
- **Suspect/flagged:** Jerby 2108.03716 (collision–repulsion) is heuristic/dynamical — flagged for adversarial reading, not load-bearing. Chavez–Allawala 2102.02280 (prime-zeta zero-difference repulsion, v5) is numerical/heuristic — listed only for completeness, excluded from top-10. Zeraoulia–Caceres 2406.12852/2406.12863 (Montgomery-conjecture "chaos" dynamical systems) — excluded as crank-adjacent (same call as finder-001).
- **Environmental honesty:** session date 2026-08-11; "2023–2026"/"2020–2026" = items returned by the live API with those published dates; 2026-dated IDs (2601.15610, 2602.14340, 2603.21490, 2605.22059) are within the environment's plausible window and were returned by the live services.
- **No fabrication:** all titles, author lists, dates, abstracts, DOIs, page ranges, and relevance judgments above trace to fetched records or read texts (Goldston notes §9 Theorem 7 quoted from the extracted text; GLSS26 references quoted from its extracted text).
