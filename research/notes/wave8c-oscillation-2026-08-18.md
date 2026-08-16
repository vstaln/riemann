# 8C — d_N·√(log N) ≈ 0.213: oscillation structure & explicit-formula origin (FINAL)

Date: 2026-08-18. Lever: Nyman–Beurling–Báez-Duarte. Status: **CHECKED NUMERICALLY** (dense f64+dd-refined
table, 19 points, N=100..5000); interpretation labels CONJECTURED / INCONCLUSIVE.
Files: tools/wave8c/src/bin/oscfit.rs (new, std-only fit bin), /tmp/osc/prod_*.log (run logs),
tools/wave8c/results/hiN_log.txt (append-only source).

## Task
(A) characterize the oscillation of d_N·√(ln N) ≈ 0.213 in log N; (B) test whether the constant's wobble
has an explicit-formula (zero-sum) origin — specifically the CONJECTURED reading from the burnol-rate
note: "consistent with explicit-formula oscillations from low zeros γ₁=14.1347 (P=0.4446), γ₂=21.0220
(P=0.2989), γ₃=25.0109 (P=0.2512)".

## Dense table (19 points; all d_ref = dd-refined ≤1e-13 rel; f64 rel err ~1e-13 ≪ wobble)
16 points freshly run (`hiN prod N`, exit=0, it2 refinement rel_r ≤7.4e-29, kappa 1.6e3..1.4e5);
3 certified points folded in from the burnol-rate note (2000/3000/5000, dd ≤3.9e-27). N=1600/1800
SKIPPED: timed out >330s (machine loaded), per protocol.

| N   | d_ref            | d·√(ln N) | N   | d_ref            | d·√(ln N) |
|-----|------------------|-----------|-----|------------------|-----------|
| 100 | 1.001388367112e-1| 0.214895  | 600 | 8.371049967530e-2| 0.211722  |
| 150 | 9.617926404690e-2| 0.215292  | 700 | 8.171888410557e-2| **0.209160** |
| 200 | 9.379478563235e-2| 0.215898  | 800 | 8.150620050461e-2| 0.210731  |
| 250 | 9.020952168936e-2| 0.211972  | 900 | 8.117948325339e-2| 0.211727  |
| 300 | 8.886026446248e-2| 0.212221  | 1000| 8.055652546967e-2| 0.211724  |
| 350 | 8.807567230484e-2| 0.213171  | 1200| 7.949977086099e-2| 0.211686  |
| 400 | 8.726995849793e-2| 0.213615  | 1400| 7.904546495570e-2| 0.212752  |
| 450 | 8.593600672797e-2| 0.212407  | 2000| 7.782135587726e-2| 0.214551† |
| 500 | 8.564264087724e-2| 0.213500  | 3000| 7.459524862924e-2| 0.211066† |
|      |                 |           | 5000| 7.252577566170e-2| 0.211661† |
† certified in burnol-rate note (dd-refined 5.7e-28/1.3e-27/3.9e-27).

Range [0.209160, 0.215898] — band ±1.6% about mean 0.21262 (sd 0.00165, 0.78%). **Flat law holds at
every point; no point escapes [0.209, 0.216].** (CHECKED NUMERICALLY.)

## Fits (oscfit.rs: linear least squares per fixed period, exact normal-equation solve, period swept)
x = ln N ∈ [4.605, 8.517] (3.91 log-units).

**Full 19 pts:**
- M0 (c): c=0.21262, RMS=0.001649
- M1 (c + A·cos(2πx/P+φ)): best c=0.21244, A=0.00123, **P=0.3305**, RMS=0.001448 (0.878×M0) — only 12% of variance
- M1 @ fixed γ₁ (P=0.4445): A=0.00078, RMS=0.001573; @ γ₂ (0.2989): A=0.00059, RMS=0.001607; @ γ₃: A=0.00045, RMS=0.001622 — **no single zero period stands out; each is only marginally better than the constant**
- M3 (c + (B/√x)cos(2πx/P+φ), explicit-formula amplitude decay): best P=0.3306, B=0.00325, RMS=0.001419 (0.86×M0)
- M2 (two cosines): c=0.21219, A1=0.00157 P1=0.3305, A2=0.00130 **P2=0.2925** (γ₂=0.2989 adjacent), RMS=0.001196 (0.73×M0)

**γ₁-periodicity probes (direct, robust):**
- Sign-agreement of (y−mean) vs cos(γ₁·ln N + φ), φ maximized over [0,2π): **0.684 (13/19)** — with the
  φ-scan's ~4–6 effective independent phases, chance-level max is ≥13/19 with p ≈ 0.3–0.4. **Indistinguishable from chance.**
- γ₂: 0.632, γ₃: 0.579 — also chance-level.
- Fixed-γ₁ one-cosine explains ~9% of the wobble variance (RMS 0.00157 vs 0.00165 baseline).

**Sub-window robustness (drift check):**
- N≥150 (18 pts): best P=0.2829 (γ₃-adjacent), RMS 0.001235 (0.77×M0); fixed-γ₁ RMS 0.001537 — γ₁ still clearly worse.
- N≥300 (14 pts, early transient removed): best **P=1.5112** (slow!), A=0.00148, RMS=0.000729 (**0.572×M0**, 43% of variance); fixed-γ₁ RMS 0.001196 (0.94×M0) — **γ₁ is ~1.6× worse than the slow period**. M2: P1=1.5112 A1=0.00145, P2=0.695 A2=0.00067, RMS 0.00055.

## Verdicts
1. **Flat law (A, macro)**: CHECKED NUMERICALLY — d_N·√(ln N) = 0.2126 ± 0.0016 over N=100..5000 (19 pts,
   two decades of log N). The ±1% wobble is REAL numerical structure (every point dd-exact; N=700 dip
   −0.0035 is certified to 7.4e-29), but its shape is NOT a clean sinusoid at any single zero period.
2. **γ₁ (or any single-zero) explicit-formula cosine: NOT PRESENT as the dominant wobble.** Sign-agreement
   at best phase ≈ chance (0.68/0.63/0.58 for γ₁/γ₂/γ₃); fixed-γ₁ fits barely beat the constant. The
   burnol-rate note's conjecture that the wobble is "explicit-formula oscillations from low zeros"
   is **NOT SUPPORTED in its single-zero form** by the dense data. (INCONCLUSIVE for multi-zero sums —
   see 4.)
3. **The wobble is dominated by a SLOW structure**, not γ₁-fast: after removing the early transient
   (N≲250), the best single cosine has period ~1.5 log-units, amplitude ~0.0015 (43% variance). The
   dominant features: deep dip at N≈700 (−0.0035, the deepest), peak at N≈150–200 (+0.0027/+0.0033,
   early transient), secondary dips at 3000/5000. (CHECKED NUMERICALLY for the fit; period identification CONJECTURED.)
4. **Explicit-formula origin: INCONCLUSIVE, not disproven.** The data reject a single-γ₁ cosine, but a
   zero-sum with multiple comparable terms produces beats (γ₂−γ₃ beat period = 2π/3.989 = 1.575 — close
   to the fitted slow 1.51, but the window spans only ~1.9 slow cycles so the period is poorly constrained;
   M2's P2≈0.29 is γ₂-adjacent on the full set but not reproducible in the N≥300 window). A 2-cosine model
   still leaves the N=700 dip as the largest residual (pred −0.0017 → observed −0.0035): the dip is
   deeper than any smooth cosine pair, hinting at a localized/non-sinusoidal mechanism (e.g.,
   smallest-eigenvalue sensitivity at specific N). These are CONJECTURED readings, not established.

## Honest bottom line
- **Not RH evidence either way.** The NB theorem is a dichotomy at N→∞; a flat or wobbling constant in
  d_N·√(log N) constrains the sharp-rate conjecture, not RH.
- Flat law: **STRENGTHENED** (19 points, band ±1.6%, all certified).
- The "low-zero oscillation" conjecture from the burnol-rate note: **REVISED** — the wobble is real but
  slow-period-dominated and non-sinusoidal, not a γ₁ cosine. Single-γ₁: REFUTED as the wobble's shape
  (data, CHECKED NUMERICALLY); zero-sum origin in general: INCONCLUSIVE.
- Next levers (cheap): (a) extend the dense grid 700..900 and 2000..3000 to pin the dip's width and the
  slow period; (b) fit d_N² directly (square the y's, y² ~ c²/x) to test the (1+κcos/√x) form on the
  square, where the 1/√x decay is better resolved; (c) compare against a Burnol-style |μ̂(ρ)|²-weighted
  zero sum if the multi-zero model is ever implemented.

## Provenance & trust
- All 16 fresh runs: `hiN prod N`, exit=0, RESULT lines in /tmp/osc/prod_*.log (parsed by oscfit);
  refinement it2 rel_r ≤7.4e-29 at every N, kappa 1.6e3 (N=100) .. 1.4e5 (N=1400).
- 3 certified points from burnol-rate note (2000/3000/5000) injected as RESULT lines — labeled †.
- oscfit: exact normal-equation least squares per period (partial-pivoting solve), period grid
  0.20..1.60 step 0.0025 + 0.0001 local refine; no nonlinear optimizer, no local-min traps.
- Known: window 3.91 log-units limits slow-period resolution (~1.9 cycles of 1.51); small-N transient
  contaminates full-set fits (hence sub-window analysis).
