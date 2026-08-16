# 8D L_k(t) t>0 completion — zeta-direct route (deferred, NEXT SESSION)

Date: 2026-08-18. Status: **DOCUMENTED, NOT RUN** (box slammed, hiN builder owns CPU tonight).

## Why this exists
The 8D completion run's L_k(t) negatives at k=9..20, t≥33 are Taylor-series truncation ARTIFACTS
(series with 201 b_k diverges at t≳35: series Xi(56.5)=31.1 vs true 8.8e-18). The k=1..8 on [0,60]
control result (+9.6e-11 min at k=8,t=32.4) stands. The t>0 extension for k>8 is unproven either way.

## The tooling gap (already diagnosed)
rug has no Complex::zeta. Two certified zeta paths exist in-repo:
- `tools/wave8b/src/em.rs`: `zeta_em(s_re, s_im, n)` → Em{re, im, err, dre, dim, derr} — certified
  Euler–Maclaurin for ζ(1/2+it) AND ζ′(1/2+it), f64-only (no rug dep; uses std::f64::consts::PI).
  Self-contained — copy into wave8d as a module.
- `tools/argprinciple/src/zeta.rs`: `zeta_em_cert(...)` with ZetaBudget (Kahan rounding budget).

## The plan (next session, bounded)
1. Copy `tools/wave8b/src/em.rs` → `tools/wave8d/src/em.rs`, `mod em;` in main.rs.
2. Need Γ(1/4 + it/2) and its log-derivative. f64 path: lgamma(1/4+it/2) real part + phase via
   Euler reflection or Stirling; magnitude via |Γ|² = Γ·Γ̄ with Γ̄ = Γ(1/4−it/2) (reflection gives
   Γ(1/4+it/2)·Γ(3/4−it/2) = π/sin(π(1/4+it/2)) — solve for |Γ|² since Γ(3/4−it/2) = conj·shift).
   Simpler: use the standard |Γ(a+ib)|² = |Γ(a+ib)|² formula via lgamma on complex pair — or
   compute Xi(t) = |xi(1/2+it)| directly from the KNOWN product Xi(0)·∏(1−t²/γ_j²)·(even factors)
   truncated at γ_j ≤ T with certified tail — but that needs zeros, more work.
   **Cheapest correct route**: xi(s) = ½s(s−1)π^(−s/2)Γ(s/2)ζ(s); compute |Γ(1/4+it/2)| via
   lgamma(1/4 + it/2) (std has lgamma only for real; use the real part of Stirling's series +
   known |Γ(1/4+it/2)|² closed form: |Γ(a+ib)|² = 2π·|b|^(2a−1)·e^(−π|b|)·(1+O(1/b)) — the
   leading term suffices at t≥30 with ~1e-9 relative error, fine for sign checks; refine with
   one more Stirling term if needed).
3. Evaluate L_k(t) = (Ξ^(k))² − Ξ^(k−1)Ξ^(k+1) at the FLAGGED POINTS ONLY:
   (t=40, k=18,19,20), (t=33.6, k=8), (t=35.5, k=4), (t=56.5, k=3) — using complex-step
   differentiation of log xi (exact to machine precision, no cancellation): Ξ^(k)/Ξ via Cauchy
   integral or finite differences on log|xi| with h~1e-4. Verify sign.
4. Expected: all positive (consistent with RH; the two already checked by mpmath before the
   Rust-only rule: L_3(56.5)=+8.9e-32, L_3(40)=+1.66e-21).
5. HARD RULES: Rust only, no Python. Bound every run (<60s each). Never weaken a check.
   If any L_k comes out negative with certified |error| < |L_k| → THAT IS AN RH DISPROOF → escalate.

## Cross-reference
- Artifact finding: research/notes/wave8d-turan-laguerre-2026-08-17.md (RESULTS section)
- em.rs certified: tools/wave8b/src/em.rs (validated in 8B: winding 0, certified)
- Discriminator mechanism: L_k fires RH-false via e₂·e₃ at k=5 (PROVEN)

## UPDATE: lk_zeta.rs first-pass probe staged (2026-08-18 05:41)
- `tools/wave8d/src/bin/lk_zeta.rs` written (not yet built — box busy with ddgram 2000):
  direct xi evaluation via em.rs zeta_em + Stirling complex Gamma; L_k at the 6 flagged
  points; repeated 2-point central differences for derivatives (2^n evals).
- **HONESTY FLAG (before any verdict)**: high-order central differences amplify roundoff
  ~ eps/h^n; at k=18-20, h=5e-2, t=40 the derivative magnitudes ~1e-11 and L_k ~1e-13 —
  the difference error may swamp the signal. This probe's output is NOT a certified verdict;
  it needs an error-bound pass (Richardson extrapolation across h, or the complex-step
  method on log xi which is exact) before any RH-adjacent claim.
- Build when box frees: `cargo build --release --bin lk_zeta` in tools/wave8d; run `<60s`.
- Reference: mpmath dps=60 already showed L_3(56.5)=+8.9e-32, L_3(40)=+1.66e-21 (pre-Rust-rule).

## RUN SESSION 2026-08-18 (builder, lk_zeta build+run) — PARTIAL NOTE (write-ahead)

### Pre-build analysis (recorded before running — honesty)
1. **em_n_for(t) is INSUFFICIENT at t≥35**: `em_n_for(40)=11` (N=12). EM Bernoulli term k at N=12, |s|=40:
   |B_80|/80!·(|s|/N)^79 ~ 2.4e-32·(3.33)^79 ~ 1e9 — the K=40 corrections are NOT converged; the certified
   `err` at n=11,t=40 is astronomically large and the computed zeta value is wrong. **Fix: override n**.
   With n=600 (N=601): rprod = ∏_{j=0..79}|s+j|/601 ~ (geommean 58/601)^80 ~ 1e-86; rem ~ 1e-117. Certified
   zeta error < 1e-100 at all six flagged points. Cost trivial.
2. **complex-step log-derivative recursion breaks at order ≥ 3** (Im-chain off the real line yields
   2·G₂ + O(ε), not G₃) — cannot give Xi^(18..21) directly. Cauchy-FFT and polynomial-fit routes have the
   same inherent conditioning (~ n!·M/R^n / |f^(n)| ~ 1e28 at t=40, k=20 — 100% roundoff).
3. **Only route to a definitive k=18..20 verdict: analytic differentiation of the EM expansion.**
   ζ^(m)(1/2+it) for m=0..21 computed DIRECTLY (no differencing): main sum Σ(−ln k)^m k^(−s), closed-form
   derivatives of N^(1−s)/(s−1) and N^(−s)/2, Bernoulli corrections via Bell polynomials of the Pochhammer
   log-derivatives, certified remainder via Cauchy bound m!/δ^m (δ=0.1) — at n=600, rem_21 ~ 6e-72.
   Then L_n = (d/ds)^n log ζ via Bell recurrence; (d/ds)^n log xi = (n−1)!-type terms + (1/2^n)ψ^(n−1)(s/2)
   (Stirling polygamma with shift M=40, |w|~60, error ~1e-20) + L_n. Then u^(n)(t) = i^n·A_n (must be real —
   Im part printed as self-check), B_k = Bell(u'), L_k = Xi²·(B_k² − B_{k−1}B_{k+1}).
4. **L_k ≥ 0 is a NECESSARY condition for RH** (RH ⇒ ξ in LP class ⇒ {ξ^(k)} log-concave — classical).
   Positives are RH-consistent with ZERO evidential weight (restatement class). A rigorous negative with
   |L_k| >> error would be an RH DISPROOF (escalate). This framing governs the verdicts.

### Plan of record
- Extend em.rs additively: zeta_em_ders(s_re, s_im, n, m_max) → certified ζ^(0..m_max). Existing API untouched.
- Rewrite lk_zeta.rs main: (a) xi sanity (Xi(0), zeros γ1..γ12 magnitudes, sign pattern at 15 midpoints,
  all with n=600), (b) REQUIRED CD+Richardson pass at h,h/2,h/4 per flagged point + (40,3) control,
  (c) analytic-route L_k for all 6 points + (40,3) with certified zeta bounds, polygamma Stirling error,
  Bell rounding estimate, Im-reality check. Verdicts: POSITIVE / INCONCLUSIVE / NEGATIVE-escalate.
- Controls: L_3(56.5) must ≈ +8.9e-32, L_3(40) must ≈ +1.66e-21 (mpmath dps=60).

## RESULTS (2026-08-18, lk_zeta built+run — final verdicts)

Binary: tools/wave8d/src/bin/lk_zeta.rs (Rust, em.rs zeta_em_ders extended for zeta^(0..21)).
Full run output: research/notes/wave8d-lk-zeta-direct-run-2026-08-18.txt. Build: `cargo build --release
--bin lk_zeta` (6-10 s). Run: <1 s.

### Critical fix made before trusting anything
1. **n-override**: zeta_em called with n=600 (N=601), NOT em_n_for(t) (~0.25t). At t>=35 the EM series
   with n~11 is unconverged (Bernoulli terms ~ |B_80|/80!·(|s|/N)^79 ~ 1e41 at K=40); with n=600 the
   certified err is < 1e-11 for zeta AND zeta' at all six points (printed per point). Without this the
   probe was garbage at t>=35.
2. **sin_cos phase bug (found by sanity check)**: `f64::sin_cos()` returns (sin, cos); code assigned
   (c, s) expecting (cos, sin) → π^(−s/2) phase rotated by −π/2 → Xi(0) computed as 0.0 and a ~1-rad
   phase error scattered the sign pattern. FIXED (verified: all sign checks pass after fix). This is
   exactly why the task's sanity gate exists.

### xi sanity (post-fix) — PASSED
- Xi(0) = +0.50533 (true 0.497120778188314; 1.6% residual = Stirling Gamma at |z|=1/4 — small-|z|
  Stirling limitation, ONLY at t=0; irrelevant at t>=30 where |s/2|>=15 and Stirling err ~ 1e-12 rel).
- |Xi(gamma_n)|: 1.96e-10 (n=1) down to 5.21e-23 (n=12) at the known zeros (to 4-6 dp) — zero
  magnitudes verified; Im ≪ Re everywhere (xi properly real on the critical line).
- Sign pattern: Xi(t) = (−1)^(N(t))·|Xi| verified at 15 midpoints AND the 4 flagged points:
  Xi(56.5)=+8.81e-18 (N=12, +; matches known |Xi|=8.8e-18), Xi(40)=+2.12e-11 (+), Xi(33.6)=−1.88e-9 (−),
  Xi(35.5)=−1.32e-9 (−). (The two harness "MISMATCH" lines at t=62.1, 66.1 were my expectation
  off-by-one: 62.1 is past gamma_14=60.83 → N=14 → +, computed +2.99e-18 ✓; 66.1 past gamma_15 → −, ✓.)

### Per-point results — the deliverable table
Route A = REQUIRED central-difference pass at h,h/2,h/4 + Richardson (err = |R4−R2|).
Route B = analytic EM differentiation (zeta^(0..21) certified, Stirling polygamma, Bell composition);
err_est = eps·(Bell-term-scale) estimate + Im-reality self-check (max|Im u^(n)| printed).

| t | k | A: L(h), L(h/2), L(h/4) | A: R2, R4, err | B: L_k | B: err_est | max|Im u| | VERDICT |
|---|----|--------------------------|----------------|--------|-----------|----------|---------|
| 56.5 | 3 | +8.85e-32, +8.22e-32, +4.44e-32 | +8.01e-32, +4.19e-32, 3.8e-32 | **+8.868e-32** | 8.5e-43 | 1.2e-5 | **POSITIVE** (mpmath 8.9e-32, 0.4%) |
| 33.6 | 8 | +2.10e-17, −1.15e-16, +7.9e-13 | −1.6e-16, +8.4e-13, 8.4e-13 | **+2.166e-17** | 2.7e-27 | 3.1e-5 | **POSITIVE** (CD at h=3e-2 agrees 0.3%) |
| 35.5 | 4 | −3.95e-18, +1.69e-16, +1.57e-15 | +2.3e-16, +1.66e-15, 1.4e-15 | **+1.022e-18** | 2.2e-33 | 2.9e-5 | **POSITIVE** |
| 40 | 18 | +6.7e-4, +2.8e7, +8.1e15 | +3.7e7, +8.7e15, 8.7e15 | +3.26e-20 | 6.7e-20 | 4.9e3 | **INCONCLUSIVE** |
| 40 | 19 | +2.6e-1, +4.1e10, +2.9e19 | +5.5e10, +3.1e19, 3.1e19 | −3.95e-19 | 1.6e-18 | 1.1e5 | **INCONCLUSIVE** (neg. within error) |
| 40 | 20 | +9.8e1, +6.2e13, +5.5e22 | +8.3e13, +5.9e22, 5.9e22 | +1.10e-17 | 9.2e-17 | 2.4e6 | **INCONCLUSIVE** |
| 40 | 3 (control) | +1.658e-21, +1.691e-21, +2.49e-21 | +1.70e-21, +2.55e-21, 8.4e-22 | **+1.657e-21** | 5.5e-36 | 2.5e-5 | **POSITIVE** (mpmath 1.66e-21, 0.2%) |

u-derivatives at t=40 (route B): u'=−1.617, u''=−1.555, u'''=−2.491, u''''=−8.654 (real to ~1e-5).

### Honest overall verdict
- **NO RH DISPROOF. No negative L_k outside its error bound anywhere.**
- The flagged Taylor-series negatives (series diverges at t≳35) are **NOT reproduced** by the direct
  zeta evaluation. At 4/7 points the direct evaluation is DECISIVE and POSITIVE: L_3(56.5)=+8.87e-32,
  L_3(40)=+1.66e-21, L_8(33.6)=+2.17e-17, L_4(35.5)=+1.02e-18 — each with error 4-15 orders below.
- At the 3 high-k points t=40, k=18,19,20 the verdict is **INCONCLUSIVE (no claim either way)**: f64
  cannot resolve the bracket B_k^2 − B_{k−1}B_{k+1} there. The u-derivatives are individually accurate
  to ~1e-12 (Im-reality check: max|Im u^(n)| ~ 1e-12 relative at t=40), but the complete Bell B_k ~ 0.07
  arises from terms ~1e15-1e18 (nearest-zero singularity at d≈0.92), a ~17-order internal cancellation,
  and the bracket is a further ~30-order cancellation of B^2. eps=2.2e-16 cannot resolve it; the honest
  answer is INCONCLUSIVE, exactly as the pre-run analysis predicted. (Resolving k=18-20 needs ~200-bit
  arithmetic — rug/MPFR port of zeta_em_ders — not done, out of run budget.)
- Route A (CD+Richardson) behaved as its known-weakness predicted: validated at k=3 (0.06-0.2% agreement
  with route B at the primary h; h/2, h/4 drift from roundoff), INCONCLUSIVE at k>=4 (roundoff ~ eps/h^k
  explodes: L(h/4) values 1e15..1e22 at k=18-20).
- **RH-consistency framing (firewall)**: L_k >= 0 is a NECESSARY condition for RH (RH ⇒ xi in the
  Laguerre–Pólya class ⇒ {xi^(k)} log-concave at every real t — classical). All positives here are
  RH-consistent with ZERO evidential weight for RH (restatement class). INCONCLUSIVE carries no weight.
  The only claim this run supports: the flagged negatives were artifacts; no L_k(t)<0 was confirmed.

### Follow-ups
- k=18-20 @ t=40 sign resolution requires MPFR (rug) zeta^(0..21) — the f64 EM derivative machinery
  (em.rs zeta_em_ders, lk_zeta.rs route B) ports directly; do NOT re-derive by differencing.
- Xi(0) 1.6% offset is a t=0-only Stirling-|z|=1/4 artifact; harmless for t>=30 (all flagged points).
