# Experiment Log

## Contribution (one sentence)
On 2026-08-24 the project discovered that every prior coboundary-floor record had been certified against the wrong functional (F_V instead of F_T) or against a theorem-inadmissible q-mass normalization, retired them all honestly, and re-based on sound, mass-respecting foundations — a Rust certification pipeline now mirrors the corrected Python verifier, and the density-one model constants were proven exact in three independent ways.

## Experiments Run

### 1. Devine audit confirmation (3 lanes)
- **Claim tested:** The posted eps=0.0079 certificate (record 0.6735471309049393) bounds the WRONG functional; external one-page audit by Michael Devine (Circumjovial LLC). [RETIRED 2026-08-24]
- **Setup:** Three independent lanes: (1) read of the repo verifier code, (2) read of Tawan's theorem/source across proof markdown + paper TeX + the actual C++ verifier, (3) an mpmath dps=60 identity evaluation.
- **Key result:** All three lanes agree — [PROVEN].
  - Lane 1 CODE: `tools/verify_coboundary_floor.py` sums ALL 21 pairs (`w_uniform` line 498, no span filter) PLUS `q_i·w(g_i)` separately (lines 268-279) ⇒ implements F_V, not F_T. [PROVEN]
  - Lane 2 THEOREM: Tawan's local-to-global lemma requires F_T — q_i REPLACE the span-one layer; `kSpanRationals[1]=0` and the pair loop starts at span=2 (`for (span=2; span<=6; ++span)`); `kNearestRationals`(q) IS the span-one layer. `Σq=2` equals the 6·(1/3)=2 span-one mass, a replacement not an addition. [PROVEN]
  - Lane 3 IDENTITY: F_V − F_T = (1/3)·Σᵢ w(gᵢ) = 0.000362273873459031 exactly (both evaluations agree, mpmath dps=60) at witness g=(7993,4182,7967,8003,7971,4197)/4000. [CHECKED NUMERICALLY]
- **Files:** research/notes/ledger.md (2026-08-24 entry, lane 1); research/notes/dispute-vstalin-tawan-2026-08-24.md (lane 2 theorem, verbatim source quote).
- **Surprising finding:** A verifier certifying F_V as written DOUBLE-COUNTS the span-one mass (2+2=4, not 2) and does not match Tawan's theorem — the posted 72h/384-core Devine value 0.673399 (reported) is for F_T and thus not comparable to an F_V certificate.

### 2. Retirement of 0.6735471309049393 [RETIRED 2026-08-24]
- **Claim tested:** The 2026-08-23 sound record N₀(T)/N(T) ≥ 0.6735471309049393 (m=136, eps=0.0079 verified=true, 27,679,928 nodes). [RETIRED 2026-08-24]
- **Setup:** Because the certified functional is F_V and the theorem needs F_T, and F_V ≥ F_T strictly on the domain interior, no F_T bound follows from any F_V certificate.
- **Key result:** RETIRED. The 2026-08-23 record (m=136) and ALL coboundary-floor records certified via the same `verify_coboundary_floor.py` coboundary branch are withdrawn, including the 2026-08-21 sound re-certification eps=0.00689 → 0.6734729658195391 (same code path). [PROVEN logical consequence]
- **Files:** research/notes/ledger.md (2026-08-24 record-retired entry; 2026-08-21, 2026-08-23 entries for the retired values).
- **Surprising finding:** The C21 optimizer (`joint_c21.py`, `F_B` via PAIRS21 = 21 pairs incl. y₀ distances + q-terms) had ALSO optimized the wrong objective; round-1 theta is usable only as a starting point.

### 3. Mass-condition discovery + post-fix floor retirements
- **Claim tested:** Whether the coboundary local-to-global lemma requires Σq=2 exactly (fixed span weights), or only Σq = removed-span-one-mass under some normalization, or leaves q free.
- **Setup:** Direct read of BELLMAN_COBBOUNDARY_PROOF.md; then a hard-fail mass assertion was added to the verifier.
- **Key result:** The mass conditions are HARD [PROVEN from source]. F_B = F₀ + U(g₂..g₆) − U(g₁..g₅) is a coboundary; Σp / Σq=2 / span-mass=2 are what make U telescope on periodic sequences — they license the block assembly itself, not parameter choices. Consequently the "honest restart" numbers 0.67296645387858 (m=151) and 0.6730965989022086 are RETIRED as INADMISSIBLE (not merely suspected):
  - cert_F_T_700: Σq = 2.6987 ≠ 2
  - cert_FT_0.0072: Σq = 2.6987 (idem)
  - optimizer-r2 winner (best_c21_theta.npy, joint_c21_ft.unpack): Σq = 3.0903 ≠ 2
  - A renormalized set with Σq≈1.98 triggers `MASS-FAIL: |sum q - 2| = 2.000e-2 > 1e-9; refusing to run` (exit 2) — the guard works.
- **Files:** research/notes/ledger.md (2026-08-24 HOLD → final entries); research/notes/verifier-rs-build-2026-08-24.md (mass assertion).
- **Surprising finding:** Σq must equal 2 EXACTLY (tolerance 1e-9) with each present span keeping mass 2 and Σq=2 replacing the dropped span-one mass; the surviving floors are Tawan published 0.6731929114731422 [PROVEN] and Devine-reported 0.673399 (unaudited by us).

### 4. Adversarial self-audit (NUMBER_WRONG correction, conservative direction)
- **Claim tested:** The replaced-mode (F_T) headline N₀(T)/N(T) ≥ 0.6729663177639583 at m=151 (verified=true at eps=0.0070, 779,030 nodes, α=1.4263026187858052, λ=1.351623997475116).
- **Setup:** Read-only adversarial pass (diagnose agent) on the patch, the pruning, the headline recomputation, and H — the placed number vs. its own stated formula.
- **Key result:** The machinery is SOUND, but the headline is NUMBER_WRONG (internal inconsistency):
  - Patch removes exactly the six span-one pairs (filter j−i≥2 drops (0,1)..(5,6)); no silent F_V fallback (mode echoed); pruning cannot manufacture verified=true. [PROVEN]
  - Claim's own formula psum=λ·Σraw_p/1920000 yields 0.67296645387858; the published 0.6729663177639583 reproduces only under psum=λ/320 (sum raw_p rounded to 6000). The published value is a CONSERVATIVE (sound, safe) UNDERSTATEMENT, 1.36e-7 low — correction is upward, not a security break. [PROVEN, mpmath dps=40]
  - H(α)=0.6724988031484523793… matches claim (12 digits). m=151 is the global argmax over [40,5000]; no m>400 growth. [CHECKED NUMERICALLY]
  - Verification take-back: "verified=true at eps=0.0070" is the claimed F_T floor, NOT independently re-run (multi-hour class) — taken as claimed, unc contradicted by static read.
- **Files:** research/notes/fT-recert-adversarial-2026-08-24.md; research/notes/ledger.md (2026-08-24 cont. entries).
- **Surprising finding:** The number labs found "wrong" was wrong in the SAFE direction (a smaller, valid lower bound) — the true formula value is HIGHER; and this installed floor was later retired anyway by the mass-condition finding (block 3), independent of its arithmetic.

### 5. Rust pipeline build incl. latent unsound-LDL find
- **Claim tested:** The independent Rust certification pipeline `tools/verifier-rs/` could soundly certify the coboundary floor for both F_V (span1 "added") and F_T ("replaced").
- **Setup:** Port the corrected Python semantics (Gershgorin/Weyl PD certificate replacing LDL-on-entrywise-lower-bounds); add span1_mode, hard mass assertions, self-describing param echo, and a floor-pipeline subcommand.
- **Key result:** Build clean; sound.
  - **Latent unsound-LDL find (third instance of this defect class):** the COMMITTED Rust `block.rs` already gated the tangent prune via `ldl_positive`, which current Python (2026-08-21 soundness fix) explicitly documents as INVALID ("M from entrywise lower bounds of w″ can be PD while true Hessian indefinite"). REPLACED with a sound Gershgorin diagonal-dominance certificate (`hessian_pd_gershgorin`); `ldl_positive` retained only as `#[allow(dead_code)]`, marked NOT a sound PD certificate. The two prior instances of the class are the 2026-08-21 Python cert-bug and the F_V/F_T mismatch (block 1). (The literal ordinal label "#3" does not appear verbatim in the notes; this is my numbering as the third instance.)
  - F_V tawan baseline (α=1.47): verified=True, 660,298 nodes; CHAIN_BOUND=0.6731929114731422 (m=183) — reproduces Tawan's committed 0.6731929114731423 to ~2e-16. [PROVEN]
  - F_T round-4 winner (α=1.4882098313790653): verified=True, 4,601,264 nodes; CHAIN_BOUND=0.67306445176945029 (m=188). [PROVEN]
  - `floor-pipeline` tawan: `PIPELINE_VERDICT: PASS`, bound=0.67319291147314220. Mass assertion verified working.
  - Honest limitation: the old invalid-LDL 0.00620 reproduction (1,096,556 nodes) does NOT certify with the sound Gershgorin within 5,000,000 nodes (band cells w″_lo ∈ [−0.68, +2.13] genuinely cross zero); the mission validation targets (0.00577, 0.0056) certify soundly via the interval prune and do not depend on the tangent.
- **Files:** research/notes/verifier-rs-build-2026-08-24.md; tools/verifier-rs/ (block.rs, build).
- **Surprising finding:** The Python 2026-08-21 "soundness fix" had a silent latent twin already sitting in the committed Rust code — caught only because the port forced the semantics to match.

### 6. Density-one refereeing
- **Claim tested:** The sine-model/CUE model constants m_7, m_8, and the resolution of the reported "+62σ sim anomaly" against the m_7/m_8 values.
- **Setup:** Exact-rational probe on `zeta-density-one-reproduction`: fit the constant term of the degree-floor(b/2) 1/N²-polynomial from the archive's exact m_b(N) rationals; cross-check the engine; recompute honest between-sample standard errors from ev_400/800/1600.
- **Key result:** Constants PROVEN 3 independent exact routes:
  - m_7 = 3439/180 = 19.1055556 (holdout N=6 exact, DELTA=0; engine m_7(4)=34507/2048 == archived; new m_7(9)=29725531/1594323 == prediction). [PROVEN]
  - m_8 = 747361/20160 = 37.0714782 (holdout N=7 exact, DELTA=0; engine m_8(2),(4),(6) all DELTA=0). [PROVEN]
  - Archive candidates M8=519/14 and Σ_8=89/315 are 4.96e-5 LOW (their own `_comment` flags "dev 5.0e-5"); `sigma_exact[8]=633/2240` is correct; Σ_7=7/90 exact.
  - SE artifact RESOLVED: analysis.json standard errors underestimated ~290× (m6), ~780× (m7), ~2700× (m8); at honest SE the pool agrees with exact constants at ~2-3σ. The "+62σ/+32σ" do not exist — an error-bar arithmetic bug in the analysis layer, NOT a sampler bias (sampler reproduces m1..m6 exactly). [PROVEN]
  - Layer-(b) disjointness: representation theory (Schur-Weyl/Weingarten) fully explains and certifies the CUE-side constants (m7(8)=2427905/131072 rational; DELTA=0 fits), but the arithmetic side m_b(T) is PROVEN structurally disjoint from the CUE/symmetric-group sector — the off-diagonal is number theory, not a unitary integral, so no RMT identity can certify m_b(T)→m_b. The b=4/H₃ discriminator (m₄ 346/105 vs 10/3; det H₃ 58/945 vs 0) is the cheapest sharpening rung. [PROVEN structural / CONJECTURED for the arithmetic convergence]
- **Files:** research/notes/densityone-probe-executed-2026-08-24.md; research/notes/xdom-repthy-2026-08-24.md; repo at /home/vstaln/.cache/checkouts/github.com/JoshuaHKU/zeta-density-one-reproduction.
- **Surprising finding:** The apparent contradiction ("sim disagrees with analytic constants") inverts to the constants being MORE strongly supported (exact, cross-method) than static reading allowed; the two prettier archive candidates are 5th-decimal-wrong and the paper already knew.

### 7. Cross-domain fan-out tally
- **Claim tested:** Whether representation theory / symmetric functions (and cross-domain lenses) can decide or sharpen the layer-(b) weak link m_b(T)→m_b, and the broader fan-out status.
- **Setup:** Read-only structural analyses across dynamics, stochastic, funcfield, and representation-theory lenses.
- **Key result (n = 4 items: 2 closed, 1 opened, 1 sharpened):**
  - CLOSED — dynamics: Gauss-map transfer-operator route = repackaging (non-self-adjoint; real-axis probe blind to complex planted zeros), with control experiment documented. [PROVEN reading]
  - CLOSED — stochast: unconditional counting rigidity = provable no-op (probe executed, O(1) deviation); point-process rigidity needs a conjectural local law. [PROVEN / CONJECTURED-boundary]
  - OPENED — funcfield: rank-infinity is the transport obstruction (unifies wave-25 finite-cut non-separations); D1 adaptive-growing-basis separation probe (<20 min Rust, 4 RH-false controls) queued. [CONJECTURED claim, CHECKED-NUMERICALLY footprint]
  - SHARPENED — representation theory: the CUE constants are fully certified (Tier 1) and the arithmetic layer is proven disjoint; the layer-(b) rung is rehosted as one all-orders asymptotic-determinantal/Toeplitz-TP conjecture (Borodin–Okounkov / ASW), with the b=4/H₃ numeric discriminator handed to a <20-min probe. [PROVEN structural + CONJECTURED reduction]
- **Files:** research/notes/ledger.md (2026-08-24 cross-domain entry); research/notes/xdom-dynamics-2026-08-24.md; xdom-stochast-2026-08-24.md; xdom-funcfield-2026-08-24.md; xdom-repthy-2026-08-24.md; xdom-funcfield (D1 queued).
- **Surprising finding:** Representation theory can PROVE nothing falls on its side can decide the weak link — it certifies the right-hand (CUE) constants and rehosts the left-hand side as a number-theoretic conjecture; that is itself the advance (it tells any future attacker exactly where to attack).

## Failed/Honest Retirements (withdrawn today)
- **0.6735471309049393** (2026-08-23 record, m=136, eps=0.0079) — wrong functional (F_V vs F_T). [RETIRED, PROVEN reason]
- **0.6734729658195391** (2026-08-21 sound re-cert, eps=0.00689) — same F_V code path. [RETIRED]
- **0.67356334799462276907825507156842728993505158837078861022540884** (2026-08-18, recorded 08-21) — LDL convexity certificate unsound (counterexample F_B=0.00689927 < 0.00703). [RETIRED, PROVEN]
- **0.67296645387858** (F_T honest-restart headline, m=151) — theorem-inadmissible q-mass (Σq = 2.6987). [RETIRED, INADMISSIBLE]
- **0.6730965989022086** (F_T companion value) — idem, INADMISSIBLE. [RETIRED]
- **0.6729663177639583** (inline conservative understatement) — corrected to 0.67296645387858 (NUMBER_WRONG, +1.36e-7, upward/safe direction) before being separately retired on mass grounds. [CORRECTED then RETIRED]
- **0.6751272603** ("breakthrough" from joint max-min) — artifact of the same cert bug (recorded 08-21). [DEAD]

## Labels discipline — every claim carries a status tag
- PROVEN: code reads (lanes 1/2, patch, pruning, Gershgorin replacement, mass-condition source reading), exact-rational constants (m_7, m_8), F_V−F_T identity mechanism, m=151 argmax / m<400 non-growth, Σq round-trips, structural disjointness of the CUE vs arithmetic sectors.
- CHECKED NUMERICALLY: F_V−F_T = 0.000362273873459031 (dps=60), H(α)=0.6724988031484523 (dps=40), degree-1/N²-polynomial holdouts (DELTA=0 at N=6,7,9), honest SE recomputation at ev_400/800/1600, density-one engine holdouts (DELTA=0), ms distinctness where a finite sample is used.
- CONJECTURED: m_b(T)→m_b two-sided convergence for b≥7 (arithmetic side, untouched by the probes); the all-orders asymptotic-determinantal/Toeplitz-TP equivalence (Tier 3); rank-infinity obstruction and the funcfield D1 separation lever.
- NOT independently re-run / taken as claimed: "verified=true at eps=0.0070" F_T floor (multi-hour class).
- NOT-RH-EVIDENCE: the density-one probe settles which constants the CUE ensemble has; it says nothing about ζ(s) zeros.
