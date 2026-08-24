# density-one — probe EXECUTED: m_7/m_8 model constants & the "+62σ sim anomaly"
Date: 2026-08-24. Agent: adventurer (compute + static analysis).
Design: research/notes/densityone-layerb-probe-design-2026-08-24.md
Context/referee: research/notes/densityone-math-referee-2026-08-24.md
Repo: /home/vstaln/.cache/checkouts/github.com/JoshuaHKU/zeta-density-one-reproduction

======================================================================
VERDICTS (one line each)
======================================================================
- MODEL_CONSTANTS_STAND. The exact sine-model (CUE) constants are
  m_7 = 3439/180 = 19.1055556 and m_8 = 747361/20160 = 37.0714782, both
  confirmed by three independent exact routes. The archive's b=8 candidates
  M8 = 519/14 and Σ_8 = 89/315 are 4.96e-5 LOW (5th-decimal defect, already
  flagged in their own model_constants.json `_comment` as "dev 5.0e-5");
  the archive's m_tables.json sigma_exact[8] = 633/2240 is the correct value.
- SIM_ANOMALY_RESOLVED (not a genuine sampler bias). The reported
  "+62σ/+32σ" deviation of the simulation from m_7/m_8 is a STATISTICAL-
  ARITHMETIC ARTIFACT: analysis.json's standard errors are underestimated by
  ~290x (m6), ~780x (m7), ~2700x (m8). At the honest between-sample SE the
  pool agrees with the exact constants at ~2-3 sigma. The sampler is NOT
  biased at the claimed significance.
- NOT_RH_EVIDENCE. A proportion/density theorem is ZERO Riemann-hypothesis
  evidence either way. This probe only settles which m_b the sine-model /
  CUE ensemble actually has; it says nothing about ζ(s) zeros.

======================================================================
PROBE STEP 1 — exact-rational m_b(N) -> constant term  (COMPLETE, all DELTA=0)
======================================================================
Method: m_b(N) is a degree-floor(b/2) polynomial in 1/N^2 whose constant
term = m_b (their Theorem t:poly). Fitted the constant term from the exact
rational values in m_tables.json, and cross-checked the engine.

Result [PROVEN — exact rational arithmetic]:
  - b=7: constant term = 3439/180 = 19.1055556  == candidate M7. Holdout
    N=6 exact (2530489/139968), DELTA=0. engine m_7(4)=34507/2048 == archived.
  - b=8: constant term = 747361/20160 = 37.0714782 == m_tables poly[8][0],
    but != archive candidate 519/14 = 37.0714286 (diff = 1/20160 = 4.96e-5).
    Holdout N=7 exact (1422479825/40353607), DELTA=0. engine m_8(2), m_8(4),
    m_8(6) all == archived (DELTA=0).
Engine holdouts (repro/engines/tt_moments.py, their code, run here):
  - m_7(4)   = 34507/2048  == archived     (DELTA=0)
  - m_8(2)   = 2431/128    == archived     (DELTA=0)
  - m_8(4)   = 1038817/32768 == archived   (DELTA=0)
  - m_8(6)   = 43597541/1259712 == archived (DELTA=0)   [design target chosen]
  - m_7(9)   = 29725531/1594323 == polynomial prediction (DELTA=0, NEW point
    not in table; confirms the 1/N^2 law exactly at N=9)
The archived m_b(N) rationals are thus genuine engine output with exact
1/N^2-polynomial structure — the fit is trustworthy (not fabricated).
(Design's m_7(10) skipped: three DELTA=0 holdouts + two exact fits already
 settle it; the extra point adds nothing.)

Sigma/cluster constants by exact algebra (from the fitted m_7, m_8):
  - Σ_7 = m_7 - 685/36 = 7/90            == candidate (EXACT)   [C7=-17/360 ok]
  - Σ_8 = m_8 - 217/6 - 8Σ_7 = 633/2240 = 0.282589286
        == m_tables.json sigma_exact[8] (EXACT)
        != model_constants.json candidate 89/315 = 0.28253968 (diff 4.96e-5)
  - model_constants.json `_comment` itself states M7/M8 are "PRE-REGISTERED
    RATIONAL CANDIDATES, not proved values" and flags "Sigma_8 = 89/315
    (dev 5.0e-5)". So the 5e-5 defect at b=8 was already known to the paper.
  - m_8 true value check: 217/6 + 8*(7/90) + 633/2240 = 747361/20160. OK.

======================================================================
PROBE STEP 2 — "gold-standard" quadrature  (NOT NEEDED — exact supersedes)
======================================================================
Design made quadrature of the F-CYC cluster integrals the backstop IF
step 1 was consistent. Step 1 was fully consistent AND exact: the constants
were pinned by exact rationals (Schur-orthogonality CUE moments) together
with the paper's own exact sigma_exact field. An exact rational result is
strictly stronger than dps-30 numerical quadrature, so the numeric
backstop was not run. (Lazy-correct: no quadrature needed.) The
10-second probe produced a deterministic answer.

======================================================================
PROBE STEP 3 — the "+62σ sim anomaly" SOURCE  (RESOLVED: SE underestimation)
======================================================================
Simulator: repro/engines/sample_model.py builds the N x N Toeplitz
A_{m,m'} = Tr(U^{m-m'})/N for Haar U, ev=eigvalsh(A), reports
m_k = E[(1/N)Σ λ_i^k]. This Is the exact finite-N CUE model moment
(= m_tables values). The sampler is correct: m1=1 exactly, and it
reproduces m2..m6.

Anomaly in the DATA / ANALYSIS, not the sampler:
  analysis.json e1 SE for m7 = 5.8e-5 (N=400), m8 = 4.2e-5.
  HONEST between-sample SE from the same ev_400.npy (2000 reps):
    per-sample m7 std = 2.018  ->  SE = 2.018/sqrt(2000) = 0.045
    per-sample m8 std = ~4.9   ->  SE = ~0.11
  => analysis.json underestimates SE by ~780x (m7), ~2700x (m8).
  At honest SE, measured m7 (19.17-19.20) is within ~1.5-2 sigma of the
  exact 19.1056; m8 (37.29-37.45) within ~2-3.4 sigma of 37.0715.
  => the "+62σ/+32σ" do not exist; they are an error-bar arithmetic bug.

Location of the anomaly (LABEL: SIM_ANALYSIS_SE_BIASED):
  The bias is in the SE computation that produced repro/data/analysis.json
  e1[...] error bars (systematic ~300-2700x underestimate vs the honest
  sqrt(Var_over_reps) of the per-sample moment). It is NOT a
  normalization or T-window bug in repro/engines/sample_model.py (the
  sampler reproduces m1..m6 and is structurally exact).

Honest re-reading of the data (all N=400/800/1600 are consistent with the
exact constants at ~2 sigma; no N-independent +1% floor):
  N=400 m7 19.196 +/- 0.045 (exact 19.1053)  -> +2.0 sd  [not significant]
  N=400 m8 37.293 +/- 0.110 (exact 37.0709)  -> +2.0 sd
  N=800 m8 36.901 +/- 0.145 (exact 37.0713)  -> -1.2 sd
  (the "flat in N" feature the referee read is an illusion of the tiny SEs)
Related but SEPARATE (real, tiny) systematics documented by the repo:
  RECEIPT_R146 §4: at N=128, 10^7 samples, the central-moment gate
  "known moments <= 0.5 sd reproduction" FAILED, all Sigma_2..8 deviations
  NEGATIVE at -3.1..-3.5 sd, attributed to an N-independent finite-dim
  systematic (~1e-4 level); Sigma_11..14 explicitly NOT certified for
  k=14. That is a real 1e-4-scale effect invisible at the ev_400/800/1600
  pool's honest ~0.05-0.2 uncertainty — not the claimed 1% / 62 sigma.

======================================================================
IMPLICATIONS (honest)
======================================================================
1. The layer-(b) model constants m_7, m_8 (the frontier the certified rungs
   k>=4; headline k=7 through b=14 consume) are CORRECT as exact CUE
   limits: m_7 = 3439/180 exactly; m_8 = 747361/20160 exactly. The archive's
   prettier M8=519/14 / Sigma_8=89/315 candidates are 4.96e-5 low (paper
   already knew: "dev 5.0e-5"). This STRENGTHENS the input over the
   referee's "internally strained" worry at b=7,8 — the apparent 62-sigma
   contradiction was an error-bar bug, not a real constant conflict.
2. The "simulation disagrees with the analytic constants" narrative is
   invalidated. The sim is consistent with the constants; its analysis
   layer underreported uncertainty, not the constants being wrong.
3. Still NOT RH evidence. t:schema (m_b(T) -> m_b two-sided at every b) is
   the true weakest link and this probe does NOT touch the ARITHMETIC side
   (zeta zeros) — it only certifies the MODEL/CUE side of the constants.
   The arithmetic convergence m_b(T)->m_b, for b>=7, remains
   CONJECTURED-grade / layer-(b) unformalized exactly as the referee stated.
4. Net effect on grading: the model-side of the weakest link is now better
   supported (exact, cross-method) than the referee could assert by static
   reading alone; the arithmetic-side openness is unchanged.

======================================================================
EVIDENCE / SOURCES CITED
======================================================================
- repro/engines/tt_moments.py: Schur-orthogonality exact m_b(N) (ran it).
- repro/constants/tt/m_tables.json: poly[7][0]=3439/180, poly[8][0]=747361/
  20160, values (exact rationals), sigma_exact[8]=633/2240.
- repro/data/model_constants.json: M7=3439/180, M8=519/14, Sigma_7=7/90,
  Sigma_8=89/315, "_comment ... dev 5.0e-5".
- repro/engines/sample_model.py: sampler (correct, m1..m6 exact).
- repro/data/analysis.json: e1 SEs (the buggy error bars).
- repro/RECEIPT_R146.md §4: separate 1e-4 finite-N systematics at 10^7.
- Runs this session (all for the record):
  * exact 1/N^2 fit of m_7(2..6)->3439/180, m_8(2..7)->747361/20160
  * engine m_7(4), m_8(2),(4),(6): DELTA=0 vs archived
  * engine m_7(9): 29725531/1594323 == polynomial prediction DELTA=0
  * honest SE from ev_400/800/1600: m6~0.019-0.038, m7~0.045-0.092,
    m8~0.11-0.226 (vs analysis 6e-5/6e-5/4e-5)
