# 8C follow-up — slow ~1.5-log-unit wobble: γ₂−γ₃ beat hypothesis test (P=1.5752)

Date: 2026-08-18. Lever: Nyman–Beurling–Báez-Duarte (d_N·√(ln N) ≈ 0.213 wobble).
Status: **CONJECTURED — beat consistent with (but not uniquely identified by) the slow structure on
N≥300; the N=700 dip is NOT fully explained by the beat cosine** (localized extra feature).
This is structure characterization ONLY — **NOT RH evidence in either direction**.
Files: tools/wave8c/src/bin/slowfit.rs (new), tools/wave8c/results/hiN_log.txt (append-only source,
33 RESULT lines), /tmp/osc/prod_*.log (run logs), /tmp/osc/slowfit_{full2,ge300b}.txt (fit output).
Ledger ref: wave8c-oscillation-2026-08-18.md (19-pt table), burnol-rate note (certified 2000/3000/5000).

## Task
Staged follow-up from the 8C-oscillation note: pin the slow ~1.5-log-unit wobble, testing the
hypothesis that it is the γ₂−γ₃ BEAT: product cos(γ₂x)cos(γ₃x) = ½cos((γ₃−γ₂)x) + ½cos((γ₃+γ₂)x),
beat frequency (γ₃−γ₂) = 25.0109−21.0220 = 3.9889 → beat period P = 2π/3.9889 = **1.5752 log-units**
(the fast sum component, P=0.1365, is unresolvable/aliased in a 3.9-log-unit window and folds into c).

## New data: dense dip region (11 fresh runs, all `hiN prod`, exit=0, dd-refined rel_r ≤ 7.4e-29)
N=700/800/900 re-run and reproduce the certified values EXACTLY (0.209160 / 0.210731 / 0.211727 — same
d_ref digits), so the dense grid is self-consistent and the dip is a certified numerical feature.

| N   | d_ref             | d·√(ln N) | dev-from-mean* |
|-----|-------------------|-----------|----------------|
| 650 | 8.326529939628e-2 | 0.211909  | +0.0003        |
| 675 | 8.254233128241e-2 | 0.210681  | −0.0010        |
| 700 | 8.171888410557e-2 | **0.209160** | −0.0025     |
| 725 | 8.166425007983e-2 | 0.209579  | −0.0021        |
| 750 | 8.158556687962e-2 | 0.209916  | −0.0017        |
| 775 | 8.153759717694e-2 | 0.210311  | −0.0013        |
| 800 | 8.150620050461e-2 | 0.210731  | −0.0009        |
| 825 | 8.145259338891e-2 | 0.211077  | −0.0006        |
| 850 | 8.131126093320e-2 | 0.211178  | −0.0005        |
| 875 | 8.124005922402e-2 | 0.211446  | −0.0002        |
| 900 | 8.117948325339e-2 | 0.211727  | +0.0001        |
* dev-from-mean vs N≥300 window mean 0.211643.

**Dip shape:** deepest at N=700 (−0.0025 from window mean, −0.0035 from full mean), roughly
bell-shaped, ln-width at half-depth ≈ 0.12–0.23 (spans ~N 660..840); asymmetric tail to high N
(still −0.0006 at N=825). Localized feature, NOT a clean sinusoid.

## Fits (slowfit.rs, 27-pt full set and 23-pt N≥300 window; x = ln N)
| model | full (27 pts) RMS | N≥300 (23 pts) RMS |
|-------|-------------------|--------------------|
| M0 constant           | 0.001671 | 0.001289 |
| M1 free P  | P=1.3249, 0.001376 (0.82×M0) | **P=1.5219, 0.000716 (0.556×M0)** |
| M1 @ beat P=1.5752    | 0.001437 (0.86×M0) | 0.000722 (0.560×M0) |
| M1 @ ref P=1.5112     | 0.001421 | 0.000717 |
| M2 beat + P2          | P2=1.6846 (near-degenerate pair, amps blow up — discard) | **P2=0.4429 (γ₁-adjacent, 2π/γ₁=0.4446), A2=0.00075, 0.000526 (0.73×M1beat)** |
| Mprod explicit {2π/γ₂, 2π/γ₃} linear basis | 0.001596 (0.95×M0) | 0.001229 (0.95×M0, **1.70×M1beat**) |

**Beat vs free period (the core test):**
- N≥300: free-P optimum P=1.5219, only **3.4% from the beat 1.5752**; RMS(beat)=0.000722 vs
  RMS(free)=0.000716 — statistically indistinguishable (0.8% apart). The RMS(P) curve is flat within
  ±1% over P∈[1.51,1.58]; the beat sits squarely in the minimum.
- Full set: free P drifts to 1.3249 (early-transient contamination at N≤250; the period is unstable
  across windows, ~1.8–2.5 cycles only — as flagged in the 8C note). Beat 1.575 is 0.25 off the
  full-set optimum but still only 4% worse in RMS.
- Mprod (explicit zero-period linear basis) is 1.7× worse than the beat model — consistent with the
  wobble living at the SLOW beat frequency (a product/beat is not in the linear span of the two fast
  cosines), and re-confirms no fast zero-frequency content (γ₁ probe was chance-level in 8C note).

## Bootstrap null (honesty; 500 permutations of M0 constant-fit residuals, variance-preserving)
| statistic | full | N≥300 |
|-----------|------|-------|
| null RMS@beat ≤ observed RMS@beat (beat-amplitude p) | 2.8% | **0.0% (0/500)** |
| null free-P RMS ≤ observed free-P RMS (slow-structure p) | 24.8% | **0.2%** |
| null best-P lands within 10% of 1.5752 (beat emerges from noise) | 4.4% | 5.6% |
| null best-P median / p90 | 0.360 / 1.030 | 0.390 / 1.040 |

The N≥300 slow structure and its beat-period component are both real at p≲0.002. On the full set the
slow single-cosine is not significant (early transient breaks it; p=24.8%). Noise rarely produces a
best period near 1.575 at all (4–6%) — noise prefers SHORT periods (null median P≈0.36–0.39), so the
real data's long best-P (1.52, > null p90) is itself a slow-structure signature.

## Dip verdict: beat cosine does NOT explain the dip's full depth
Beat-model residual at N=700: **−0.00165 (N≥300) / −0.00223 (full)** — the largest residual, 2.3× the
window RMS. The beat cosine predicts ~0.2108 at N=700 (right REGION — phase consistent: the dip sits
where the slow cosine is at its trough) but the observed 0.2092 is 0.0017 deeper. The dip is a
localized extra feature on top of the slow wobble. M2 (beat + γ₁-adjacent second cosine) cuts the
residual to ~0.0005 RMS overall but the second component is not reproducible across windows (8C note)
and the dip remains the dominant residual.

## Verdicts
1. **γ₂−γ₃ beat as the slow-wobble driver: CONJECTURED (consistent, not proven).** On N≥300 the beat
   period 1.5752 is within 3.4% of the free-P optimum, statistically indistinguishable in RMS, and
   the beat-amplitude is real (p=0.0%). But with ~1.8 cycles in the window the period resolution is
   ±~0.15 — P=1.575, 1.52, and 1.51 are all equivalent fits. The beat is the only *a priori* candidate
   period in that band (it is not a fitted free parameter), which raises its prior, but the data alone
   cannot uniquely identify it.
2. **The N=700 dip: NOT explained by the beat (or any single cosine).** REFUTED as a pure cosine
   trough; the extra depth (−0.0017 vs cosine) is a localized/non-sinusoidal feature. CONJECTURED
   readings: higher-order zero-sum terms (γ₁-type, per M2's P2≈0.44) modulating the beat envelope, or
   a smallest-eigenvalue effect localized near specific N. Unresolved.
3. **Explicit two-zero-period (fast) structure: REFUTED as the wobble's shape** (Mprod 1.7× worse;
   γ₁ probe chance-level — consistent with 8C note).
4. **Flat law: STRENGTHENED** — 27 points now (100..5000), band [0.20916, 0.21590], all dd-exact;
   no point escapes [0.209, 0.216].
5. **NOT RH evidence either way** — this pins the structure of the sharp-rate constant's wobble; the
   NB dichotomy lives at N→∞.

## Cost
11 dense runs (~96–157s each, all exit=0) ≈ 20 min; slowfit (Rust, std-only) build+run seconds.
Budget OK.

## Provenance & trust
- 11 fresh runs: `hiN prod N`, exit=0, it2 refinement rel_r ≤7.4e-29; 700/800/900 reproduce certified
  d_ref digit-for-digit.
- slowfit.rs: exact normal-equation least squares (partial-pivoting solve), period grid 0.20..1.60
  (+0.0001 local refine), fixed-P models share the same linfit machinery; bootstrap = Fisher–Yates
  permutation of M0 residuals, xorshift64 seed 20260818, 500 draws.
- Known limits: slow-period resolution ±~0.15 (1.8 cycles in N≥300 window); full-set fits contaminated
  by the N≤250 transient; the sum-component (P=0.1365) of the product form is untestable (aliased).
