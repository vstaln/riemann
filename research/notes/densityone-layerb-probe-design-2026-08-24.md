# density-one — layer-(b) input t:schema: what m_b(T)/m_b are, and a decisive probe design
Date: 2026-08-24. Agent: adventurer (recon + probe design; analysis only, no compute).
Target repo: /home/vstaln/.cache/checkouts/github.com/JoshuaHKU/zeta-density-one-reproduction
Referee being served: research/notes/densityone-math-referee-2026-08-24.md (weakest link = t:schema).

============================================================================
STATUS LABELS (honesty guardrails)
============================================================================
- All numeric claims below are transcribed from THEIR files (paper.tex, repro/data/analysis.json,
  repro/constants/model_constants.json), or are arithmetic I ran off those, NOT new physics.
- No zeta-zero arithmetic simulation was run. No independent moment computation was run. The
  probe in TASK 3 is DESIGNED, not executed (per mission: analysis only, no compute).
- Anything I computed is marked [CMP].

============================================================================
TASK 1 — Pin down m_b(T) and m_b
============================================================================
VERDICT: m_b(T) = the arithmetic trace moment of the Gabor-compressed Weil matrix,
T-averaged over zeros in [T,2T]; m_b = the sine-model (CUE) limiting moment, defined by the
overlap-weighted F-CYC cluster calculus. Both confirmed verbatim below. [PROVEN from text]

m_b(T) — arithmetic side (paper.tex):
- Prop p:mu12 (~L549-566): tr G̃ = aL·N(T,2T)+O(L√X); tr G̃² = 2πbL ∫_T^{2T} μ²
  + (T/π) Σ_{n≤X} Λ(n)²/n · g(log n) + O(...). So the trace is an average over the
  zeta zeros whose height is ~T (counted by N(T,2T), normalized by spectral dimension d),
  and the surviving arithmetic content is higher-order autocorrelation sums of Λ over the
  b-tuple (the explicit-formula terms). This is the "T-average". [PROVEN]
- Normalization: the raw trace moment m_k = 𝔼 tr G̃^k / d (d = spectral dimension = zero count);
  after the recentring identity (e:recentre, §s:recentre) P := G̃/(Lℓ₁) − I, m_k = Σ_j binom(k,j) Σ_j,
  where Σ_j are the fully-joint (singleton-free) Bell-ledger class sums. [PROVEN]
- Endpoint regime (r:endpoint ~L585): λ→1⁻ (taper), w/L→0; the Gabor grid collapses to Nyquist rate,
  the frame kernel collapses on the diagonal, P is exactly scalar-recentred. t:schema lives here. [PROVEN]
- t:schema itself (~L3150): "For every b≥2, in the endpoint regime, the arithmetic trace moment
  converges two-sidedly to the model constant, m_b(T)→m_b, at the grade of §s:verif layer (b)." [PROVEN]

m_b — model side:
- Lemma l:transfer (~L2529): "For every b, lim_{N→∞}m_b(N) exists and equals the sine-model moment
  m_b defined by the overlap-weighted cluster calculus." m_b(N) = 𝔼∫x^b dν_N = normalized CUE trace
  moment of the frame eigenvalues (Diaconis–Shahshahani exact values, §s:tt). [PROVEN]
- Values (paper + repro/constants/model_constants.json):
  m0=1, m1=1, m2=4/3, m3=2, m4=13/4, m6=640/63=10.1587302, and at b=7,8 the archive holds
  PRE-REGISTERED RATIONAL CANDIDATES, not proved values:
    m7 = 3439/180 = 19.10555556  (via Σ_7=7/90, m7 = 685/36 + Σ_7)
    m8 = 519/14  = 37.07142857  (via Σ_8=89/315, m8 = 217/6 + 8Σ_7 + Σ_8)
  model_constants.json, top comment: "M7/M8 below are the PRE-REGISTERED RATIONAL CANDIDATES
  from the model measurement, not proved values." [PROVEN]
  (Footnote: the paper's tower also writes m8=747361/20160=37.0714782 [CMP: ≠519/14=37.0714286,
  differ by 1/20160≈5e-5]. Two in-repo representations of m8 with a 5e-5 mismatch — minor, not decisive.)

============================================================================
TASK 2 — Does repro contain computed m_b(T) vs model constants?
============================================================================
VERDICT: NO arithmetic (zeta-zero) m_b(T) tables exist — the capstone consumes none (referee noted;
paper says the archived tables "play no role in the proof of Theorem t:dens1"). But repro DOES hold
MODEL-side determinations of m_b, and the b=7,8 rung is internally CONFLICTED: two of the paper's own
determinations of the same model constants disagree at tens of sigma. [PROVEN from their files]

Model-side data present in repro/:
  1. Exact rational finite-N CUE moments m_b(N) for small N: constants/tt/m_tables.json
     (e.g. m4(2)=21/8, m4(12)=201061/62208 → 13/4; data up to b~14) + m_tables_ext.json
     (holdout b=9,11,13 at N=8,9,10, "bitwise HIT"). These are exact CUE/sine-model values, NOT arithmetic.
  2. Direct large-N simulation of the frame/CUE ensemble: data/ev_{400,800,1600}.npy with
     reps 2000/500/120; validated by gate g_logdet.py against the exact Morris integral
     (H_N − 1 − log N, ψ'(N+1)−ψ'(2)/N) — so these pools are the MODEL ensemble, and the
     validation confirms the ensemble is sound. analysis.json stores the measured moments.

The conflict (from analysis.json, their numbers):
  - m6 validated: val6 ≈ 10.15880/10.15863/10.15871 vs model 640/63=10.1587302 → ~1σ. [PROVEN]
  - m7 measured (e1["7"], flat across N=400/800/1600: 19.17156/19.17116/19.17223; N→∞ extrapolation
    m7_inf=19.171742, SE 1.07e-3). Model candidate 3439/180=19.1055556.
        deviation [CMP] = +0.06619 ≈ 61.9 σ, rel +0.35%. Not drifting toward candidate as N grows.
  - m8 measured (e1["8"]: 37.44485/37.44055/37.45226; m8_inf=37.446234, SE 1.17e-2). Model candidate
    519/14=37.0714286.
        deviation [CMP] = +0.37481 ≈ 32.0 σ, rel +1.01%. Flat in N, not converging to candidate.
  - Higher b: m9_inf=75.535, m10_inf=157.136; and RECEIPT_R146 §4/§6 documents that the front gate
    "known moments ≤0.5 sd reproduction" FAILED (all Σ_2..Σ_8 deviations NEGATIVE at N=128), the 3-point
    1/N² scaling test was INDETERMINATE, and Σ_11..Σ_14 were explicitly NOT certified for k=14 pricing.

Interpretation (honest, non-over-claim):
  The simulation that reproduces m1..m6 (incl. exact m6) to ~1σ does NOT reproduce the archived
  pre-registered candidates m7, m8 — off by ~0.35%/1.0%, at ~62σ/~32σ, stable from N=400 to 1600.
  Barring an undisclosed systematic in the b≥7 measurement (which the same engine demonstrably does not
  have at b≤6), this is an internal contradiction in the paper's own model-side determination of m7, m8.
  It sits EXACTLY on the frontier the certified rungs consume: rung k=4 uses moments through b=8; the
  headline rung k=7 (t:k14, λ_7(0)=0.04477, liminf N_0^s/N≥0.91046) uses moments through b=14.

============================================================================
TASK 3 — Cheapest decisive probe (<20 min laptop)
============================================================================
GOAL: decide whether the sine-model constants m_7≈19.1056, m_8≈37.0714 (equivalently the F-CYC
cluster constants Σ_7=7/90, Σ_8=89/315) are actually right, independently of (a) the paper's analytic
F-CYC calculus and (b) its own simulation (which claim 19.11/37.07 vs 19.17/37.45 respectively).

PROBE (PROTOTYPE, ~10 lines of mpmath; design only, not run):
  1. Constants to check (from model_constants.json): m7 = 685/36 + Σ_7, Σ_7 = 7/90 = 1/8 − C7
     with C7 = −17/360; m8 = 217/6 + 8Σ_7 + Σ_8, Σ_8 = 89/315. The building blocks are explicit
     orbit/cluster integrals: {5,2}_total=1/8 via Q0=5/504, Q1=1/360, Q2=13/2520; and the enumerated
     F-CYC orbits for the Σ_8 classes ({2^4}={105/17 orbits}, {2,2,4}, {4,4}, {6,2}, C_8).
  2. Independent cross-check that needs NO orbit enumeration (fastest decisive route): compute the
     CUE/sine-model moments directly to high precision from the known small-N exact values in
     m_tables.json, because m_b(N) is a polynomial in 1/N² of degree floor(b/2) (Theorem t:poly),
     whose constant term = m_b. Fit m7(N) and m8(N) from the exact rationals m7(2..6), m8(2..4)
     (all in m_tables.json) and read off the constant term to 1e-9. If it gives 19.10556/37.0714 →
     the analytic constants are right and the sim has a b≥7 bias. If it gives ≈19.17/≈37.45 →
     the analytic candidates 3439/180, 519/14 are wrong. This is pure exact-rational/interpolation
     arithmetic: <10 sec, no numerical integration at all.
  3. (Optional gold standard, ~10 min) mpmath numerical quadrature of the F-CYC box-convolution
     cluster integrals for b=7 and b=8 orbits at 1e-12: confirms Σ_7=7/90, Σ_8=89/315 directly from
     the definition in §s:conv (overlap-weighted box convolutions = same Fourier box convolutions as
     the sine kernel). Directly settles whether the archived analytic constants are the true sine-model
     moments.

WHAT EACH OUTCOME IMPLIES:
  - Fit/quadrature CONFIRM m7=3439/180, m8=519/14 → the analytic layer-(b) constants are correct;
    their own large-N simulation carries an undisclosed systematic at b≥7 (troubling but does NOT refute
    the input; the input only needs the TRUE m_b, and the probe would have pinned it).
  - Fit/quadrature give ≈19.17 / ≈37.45 (i.e. the simulation, not the candidates) → the archived
    pre-registered candidates 3439/180 and 519/14 are WRONG. Consequences: (i) the layer-(b) exact-constant
    machinery fails at b=7,8; (ii) every instantiated rung consuming b≥7 moments (k≥4, incl. the headline
    k=7 rung through b=14) is unsupported at face value; (iii) the pure qualitative capstone t:dens1
    survives structurally (it needs only determinacy ⇒ existence of some m_b, and the two-sided limit to
    WHATEVER the true sine-model m_b is), but its credibility — and per honest-science grading its
    "certified candidate" status — is materially weakened.
  - Fit/quadrature AGREE with NEITHER (unlikely) → both the analytic constants and the sim are wrong;
    highest-priority anomaly, warrants re-deriving the sine-model m_b from first principles (Monte Carlo
    CUE to 1e-4 won't settle a 1e-3 difference — quadrature or exact-fit is the only decisive tool).

============================================================================
TASK 4 — Verdict
============================================================================
INPUT AS STATED (t:schema: unconditional two-sided m_b(T)→m_b at every b, layer (b)
"pre-Lean, pre-review"):
  - Category: CONJECTURED-grade, exactly as the referee recorded. The paper itself labels layer (b)
    unformalized and M7/M8 "pre-registered candidates, not proved values". [PROVEN]
  - But NOT cleanly "plausible-as-stated": the paper's OWN two model-side determinations of the same
    constants m7, m8 conflict at ~62σ/~32σ (analytic 19.1056/37.0714 vs its simulation 19.1717/37.4462,
    stable in N), while m1..m6 are clean (~1σ). The paper's own audit (RECEIPT_R146 §4/§6) independently
    refuses to certify Σ_11..Σ_14 and reports induction-failed for the known-moment gate.
  - Therefore their own data STRAINS the input at the b=7,8 frontier — precisely the orders the
    certified rungs (k≥4; headline k=7 through b=14) consume. This does not refute the qualitative
    capstone, but it means "the model constant m_b is well-defined and the arithmetic moments converge
    to it two-sidedly at every b" cannot be taken as internally corroborated at b≥7; it is an open
    consistency question even inside the repo, resolvable by the 10-second exact-fit probe.

ONE-LINE: Plausible-as-CONJECTURED but internally strained — their own simulation of the sine-model
ensemble nails m1..m6 to ~1σ yet misses the archived m7=3439/180, m8=519/14 by ~62σ/~32σ (flat in N);
run the 10-second probe (exact 1/N² polynomial fit of m_tables.json m7(N),m8(N), or mpmath 1e-12
quadrature of the F-CYC Σ_7,Σ_8 cluster integrals) to decide which of candidate-vs-simulation is the
true sine model.
