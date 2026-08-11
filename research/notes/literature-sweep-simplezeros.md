# Literature Sweep — simple zeros / critical-line proportions / related techniques

**Date:** 2026-08-12 · **Agent:** LIT scout (phone) · **Status:** CHECKED NUMERICALLY (API
responses saved; counts reproducible)
**Reproducibility:** all numbers below come from raw arXiv API responses saved in
`scratch/lit-sweep/*.xml` (11 files, one per query), fetched by
`tools/lit_sweep.py` (main targets) and `tools/lit_sweep_supp.py` (two supplementary
phrase queries + author extraction). Commands:
```
python3 tools/lit_sweep.py
python3 tools/lit_sweep_supp.py
```
API: `http://export.arxiv.org/api/query` with `sortBy=submittedDate&sortOrder=descending&max_results=20`,
polite UA, retry/backoff. All arXiv dates below are submission dates.

**Scope guard:** per task brief, the query "sixth moment + Riemann zeta" was NOT run
(another agent owns it). Queries hit targets 1–5 plus `all:"67.25"` and
`all:"two thirds of the zeros"`.

---

## Relevant items (tight table)

| arXiv id | Date | Title (authors) | Relevance to THIS program | Deep read? |
|---|---|---|---|---|
| 2511.20059 | 2025-11-25 | Zeta Zeros on the Critical Line (Goldston, Suriajaya) | Removes RH from Montgomery's simple-zero proof via a general double-sum estimate; shows RH-free proof would give 2/3 simple **and** on the line. Direct upgrade path for the analytic-input layer (BGSTB24/25 inputs). | **YES** |
| 2603.28104 | 2026-03-30 | Zeta Zeros in a Narrow Vertical Box (Goldston, Suriajaya) | Narrow-box width b/log T ⇒ ≥ 2/3 of zeros simple **and on the critical line**; simple proof generalizing Montgomery. Feeds Q1 (on-line proportion) and the simple-zeros constant. | **YES** |
| 2306.04799 | 2023-06-07 | An unconditional Montgomery Theorem… (Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh) | Known input (BGSTB24): unconditional Montgomery; 61.7% simple under thin-box. Already in program. | — (known) |
| 2501.14545 | 2025-01-24 | Pair Correlation of Zeros I: Simple & Critical (BGSTB) | Known input (BGSTB25): 2/3 simple, 2/3 on-line, 1/3 both under narrow box. Already in program. | — (known) |
| 1302.5018 | 2013-02-20 | On simple zeros of ζ (Bui, Heath-Brown) | 19/27 simple under RH (Conrey–Ghosh–Gonek constant without GLH). Historical context for simple-zeros line. | no |
| 1410.2433 | 2014-10-09 | Critical zeros of ζ (Bui, unpublished note) | Three-piece mollifier sketch to nudge on-line + simple percentages (Feng route). Different technique (mollifier vs Weil form); context only. | no |
| 2310.10119 | 2023-10-16 | Uniform distribution modulo one of ordinates (Çiçek, Gonek) | Ordinate-spacing hypothesis machinery under RH; marginal for our certificate class. | no |
| 1902.05473 | 2019-02-14 | Extension of the Landau–Gonek formula (Aryan) | 2/3 simple under a **zero-density hypothesis** (weaker than RH); "pair correlation independent of RH". Same theme as GS25/26 — unconditional-input stack. | maybe |
| 2508.11108 | 2025-08-14 | Short mollifiers of ζ (Conrey, Farmer, Kwan, Lin, Turnage-Butterbaugh) | CoV-optimized linear combinations in Levinson's method; positive proportion for arbitrarily short mollifiers; doubles modular L proportions. Mollifier route, not Weil form; but "optimizing the linear combination" echoes our LP/certificate class. | maybe |
| 2509.18963 | 2025-09-23 | Positivity of Re(ξ′/ξ) near the critical line (Grigutis, Turčinskas) | Explicit lower bound for Re Σρ 1/(s−ρ) in 1/2+1/√log t < σ < 1. Feeds derivative tower (P5) and off-line repulsion inputs. | maybe |
| 2511.06109 | 2025-11-08 | Levinson's theorem and its generalization (Ray) | Expository proof of Levinson's theorem (Young 2010 route). No new constant. | no |
| 2411.18492 | 2024-11-27 | Epstein zeta: positive proportion on the line (Rezvyakova) | Family-transport context (P4) — positive proportion for Epstein zeta. | no |
| 2105.07422 | 2021-05-16 | Zeros of Dirichlet L-functions on the line (Sono) | 61.07% for Dirichlet L over primitive chars (mollifier). P4 context. | no |
| 2606.09096 | 2026-06-08 | Weil's quadratic form via the screw function (Suzuki) | Unified framework (screw function) for Yoshida 1992 / Bombieri 2001,2003 / Connes–Consani 2023 / Connes–Consani–Moscovici 2025+; conjecture: self-adjoint operator with eigenvalues = Im ρ as limit of nonlocal realizations on [−a,a]. **This is the Weil-form family our method uses.** | **YES** |
| 2607.02828 | 2026-07-02 | Finite Guinand–Weil dictionary, archimedean tail order for the truncated Weil form (Groskin) | Finite Galerkin truncations of the Weil form (prime cutoff c, band N): every truncated-form value is an **exact zero sum** of a band-limited g; two-sided certification rule with explicit budget B_T ~ (2N+1)ρ log T/(π²T); spectral scale 10⁻⁵⁹ at c=100; verified over first 512 zeros, scripts ship. **Directly the compressed-Weil-form machinery; interacts with Q2 (in-class ceiling) and our numerical verification.** | **YES (top)** |
| 2602.04022 | 2026-02-03 | RH: Past, Present and a Letter Through Time (Connes) | Survey + new result: extremizing (a restriction of) the Weil form with primes < 13 approximates the first 50 zeros to 10⁻⁵⁵…10⁻³, **provably on the critical line**; trace-formula convergence strategy (finite→infinite Euler products). Connes's own take on the Weil-form route. | **YES** |
| 2508.10857 | 2025-08-14 | The Alternative Hypothesis for Zeros of ζ (Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh) | AH (consecutive zeros at multiples of half average spacing): constraints on density of pairs at k/2 spacing, restricts multiple-zero density; strong AH ⇒ Essential Simplicity. **Consecutive-gap structure = the exact input to the Gram-stability refinement (discovery note) and Q3 ladder.** | **YES** |
| 1810.08843 | 2018-10-20 | Pair correlation estimates via semidefinite programming (Chirre, Gonçalves, de Laat) | SDP optimizes Montgomery-pair-correlation bounds: improves **proportion of distinct zeros**, counts of small gaps, multiplicity sums. Same optimization/certificate family as our LP-dual in-class ceiling; direct input for P2 (distinct) and small-gap structure. | **YES** |
| 1206.3737 | 2012-06-17 | Distinct zeros of ζ (Wu Xiaosheng) | > 66.036% distinct. Pre-5/6 record context for P2. | no |
| 1908.04876 | 2019-08-13 | Pair correlation for Dedekind zeta, abelian extensions | Simple/distinct zeros for Dedekind zeta. P4 family-transport context. | no |
| 2010.10675 | 2020-10-20 | Explicit unconditional results on gaps between zeros (Simonič, Trudgian, Turnage-Butterbaugh) | First unconditional explicit large/small gaps with positive proportion (explicit Landau–Gonek). Consecutive-gap structure tools; possibly reusable explicitly in the ladder (Q3). | maybe |
| 2307.13498 | 2023-07-25 | Gap distributions of Fourier quasicrystals via Lee–Yang polynomials (Alon, Vinzant) | FQ / Kurasov–Sarnak connection; NOT zeta zeros. Tangential. | no |
| 2205.00811 | 2022-05-02 | 100% of the zeros of ζ(s) are on the critical line (Suman) | **Crank flag** — sole author, v11, claims RH unconditionally. Ignore. | NO — flagged |

## Per-target verdicts

1. **Simple zeros.** No arXiv paper improves the Anthropic 67.25% simple-zeros constant (and the
   external 67.30/67.31/67.32% Gram-stability extensions are repos, not arXiv — see discovery note).
   The live *published* frontier is the RH-removal line: GS25 (2511.20059) and GS26 (2603.28104)
   give ≥ 2/3 simple **and on the line** under hypotheses weaker than RH (zero-density / narrow-box).
   These are the correct inputs to compare against BGSTB's unconditional Montgomery.
2. **On-line proportion records.** **No post-2025 improvement of Bui–Conrey–Young 41.05%/41.28%/
   41.6% found in the arXiv index.** The 2/3-on-line (Anthropic Theorem A) is not on arXiv. Closest
   published relatives: GS25/26 (2/3 on-line under weaker hypotheses) and the mollifier line
   (2508.11108, 2105.07422). `all:"67.25"` returns only ML/physics false positives — the Anthropic
   result is simply not in the index.
3. **Weil quadratic form / rank–trace.** **The rank–trace technique is NOT published elsewhere**
   under "rank-trace inequality" or "von Neumann trace inequality + zeta" (0 results each). But the
   Weil-form *family* is active: Suzuki 2606.09096 (screw-function unification), Groskin 2607.02828
   (finite Galerkin truncations + exact dictionary + certification budget), Connes 2602.04022
   (extremization → zeros on the line). Groskin's paper is the closest published analogue of our
   compressed-Weil-form finite matrix.
4. **Baluyot.** No follow-ups to 2306.04799 / 2501.14545 beyond the group's own 2508.10857
   (Alternative Hypothesis, deep-read candidate) and Baluyot–Chandee–Li 2408.09050 (low-lying zeros,
   P4 context only).
5. **Gram matrix / gap distribution.** `all:"Gram matrix" AND all:"Riemann zeta"` → **0 results**
   (arXiv API searches title/abstract; a full-text web search could differ — flagged, not run).
   `all:"gap distribution" AND all:"zeros"` → nothing on ζ-zero consecutive gaps (only FQ/ML
   papers). The real consecutive-gap content is the Alternative-Hypothesis paper (2508.10857) and
   the SDP small-gap bounds (1810.08843).

## Warm leads (the main program should chase these)

1. **2607.02828 (Groskin) — finite truncated Weil form, exact dictionary, two-sided certification.**
   Reason: this is the same object our method compresses (finite Galerkin matrices from the Weil
   form), and its certification rule ("finite-cutoff positivity certifies cutoff-free positivity",
   explicit budget B_T) speaks directly to Q2 — whether the stability refinement tr Ψ(M) can beat
   the in-class ceiling, and to our finite-T error-term problem (P6). Ships scripts + artifacts
   (verified over first 512 zeros) → reproducible cross-check against our zero data.
2. **2511.20059 + 2603.28104 (Goldston–Suriajaya) — RH-free pair correlation, 2/3 simple & on-line.**
   Reason: the Anthropic argument's analytic inputs are BGSTB24/25; GS25/26 push the same inputs
   past them under hypotheses weaker than RH, and 2603.28104 proves 2/3 **simple and on the line**
   together — precisely the combination our simple-zeros constant and Q1 (on-line transfer) care
   about.
3. **2508.10857 (BGSTB Alternative Hypothesis).** Reason: consecutive zeros at half-average-spacing
   multiples is exactly the consecutive-gap structure the Gram-stability refinement (discovery note)
   exploits (kernel cannot vanish at all three pairwise differences). Their density constraints on
   k/2-spaced pairs and the Essential-Simplicity implication are direct cross-checks for the
   stability mechanism and the Q3 ladder.
4. **1810.08843 (Chirre–Gonçalves–de Laat, SDP for pair correlation).** Reason: the same
   optimization/certificate methodology as our LP-dual in-class ceiling, applied to Montgomery
   pair-correlation bounds — improved distinct-zeros proportion, small gaps, multiplicity sums.
   Direct input to P2 (distinct 5/6 wall) and to the certificate class of the ceiling law.
5. **2606.09096 (Suzuki) + 2602.04022 (Connes) — Weil-form spectral route.** Reason: both work on
   the exact quadratic form family our method is built on, with Connes explicitly getting
   **provably-on-the-line** extremizers (primes < 13 → first 50 zeros accurate to 10⁻⁵⁵). If their
   limit-operator conjecture or extremization structure transfers, it could touch the on-line
   proportion (Q1) beyond what the rank–trace inequality alone does.

## Honest negatives (results, not padding)

- No arXiv item improves 41.6% (on-line, unconditional) or the Anthropic 67.25% (simple) — the
  external 67.3x% extensions live in repos, not the index.
- `rank-trace inequality` and `von Neumann trace inequality AND zeta`: 0 results — the rank–trace
  method is not visible in published literature under those names.
- `Gram matrix AND Riemann zeta`: 0 results; `67.25`: 0 relevant results (Anthropic result not
  indexed); `two thirds of the zeros`: only Aryan 1902.05473 (already in table).
- 2205.00811 ("100% of the zeros…") flagged as crank; excluded from leads.

## Notes on method

- arXiv export API phrase search covers title/abstract metadata; full-text gaps are possible
  (stated explicitly for the Gram-matrix query). Queries were run exactly as specified in the task
  brief plus two narrow supplements (`proportion of simple zeros`, `distinct zeros AND Riemann
  zeta`) and author extraction. Total items scanned ≈ 93; table above keeps only items with a
  genuine bearing on the program's constants (simple-zeros, on-line proportion, distinct zeros,
  Gram/stability, Weil-form method, gap structure).
