# 8D L_k(t) — MPFR (rug) resolution of k=18/19/20 @ t=40 — VERDICT: ALL POSITIVE

Date: 2026-08-18. Status: **COMPLETE**. Binary: tools/wave8d/src/bin/lk_zeta_mpfr.rs (rug 1.30,
200/256-bit). Run output: research/notes/wave8d-lk-mpfr-run-2026-08-18.txt.

## Bottom line
At ~200-bit precision, **all seven flagged points have L_k > 0 with certified error 13–16 orders of
magnitude below the signal. NO RH DISPROOF. NO INCONCLUSIVE result remains.** The f64 route (lk_zeta.rs)
left k=18/19/20 @ t=40 INCONCLUSIVE purely from f64 rounding in a ~30-order Bell cancellation; MPFR
resolves it: L_18=+1.984e-20, L_19=+2.028e-20, L_20=+2.049e-20, each err<~1e-33.

## Two real bugs found in the f64 pipeline (fixed in this port; f64 verdicts re-checked below)
1. **polygamma m=0 Stirling sign** (herglotz probe found independently): code ADDED the Bernoulli
   series, standard formula SUBTRACTS. ψ(0.25) was off by ~1e-4 in f64.
2. **polygamma Stirling coefficients missing a factorial factor (all m, f64 AND my first port)**: the
   coefficient table stores |B_{2k}|/(2k)!, so the correct Stirling coefficient is
   |B_{2k}|·(2k+m−1)!/(2k)! = |B_{2k}|/(2k)!·(2k+m−1)!. The code used |B_{2k}|/(2k)!·rising with
   rising=(2k+1)···(2k+m−1), i.e. was short by (2k)! → k=1 term computed at half its size (observed
   exactly: ψ' dev = ½·k1-term = 1.3e-6 at w=41; ψ dev = ½·k1-term = 2.5e-5). Both sign AND factor
   fixed here; validated against hardcoded ψ(1/2), ψ(1), ψ(1/4), ψ'(1/2) to ≤5e-60.
3. (already known) gamma-Stirling k=2 term in the f64 xi path used re/(360|z|³) instead of z̄³/|z|⁶;
   this port computes z^{1−2k} correctly via 1/z = z̄/|z|² powers.

**Re-adjudication consequence (coordinator requirement):** the corrected ψ changes only u′ (ψ^{(0)});
ψ^{(m≥1)} enter u^(n) only at the 1/2ⁿ level and are negligible at t≥30. Effect on earlier verdicts:
L_3(56.5): 8.868e-32 (f64) → **8.8690386026e-32** (0.02% shift) — stays POSITIVE (err 1.5e-47).
L_3(40), L_8(33.6), L_4(35.5) change <0.1% — all stay POSITIVE. **All earlier POSITIVE verdicts survive.**

## Sanity gates — ALL PASS
- **Xi(0) = 0.49712077818831410991...** (true 0.497120778188314...; exact to printed digits — Γ(1/4)
  hardcoded to dodge the t=0-only small-|z| Stirling limitation; zeta(1/2)=−1.46035450880958684, cert
  err 5.5e-58).
- **|Xi(γ_n)|**: γ₁: 3.6e-43, γ₂: 6.0e-45, γ₃: 5.7e-46, γ₄: 1.1e-47 (20-digit γ's) — zero magnitudes
  verified to ~1e-40+ (was 1e-10 in f64). Im ≪ Re (xi properly real on the critical line).
- **Sign pattern** Xi(t)=(−1)^{N(t)}|Xi|: all 15 midpoints + 4 flagged points correct. (The two
  "MISMATCH" lines at t=62.1/66.1 are the harness's off-by-one — N(62.1)=14→+, N(66.1)=15→−; the
  computed signs are correct, same artifact as documented in the f64 run.)
- **Flagged Xi values**: Xi(56.5)=+8.8067e-18 (known 8.8e-18 ✓), Xi(40)=+2.1176e-11 ✓, Xi(33.6)=−1.8767e-9 ✓,
  Xi(35.5)=−1.3200e-9 ✓.
- **Coefficients**: |B_{2k}|/(2k)! from ζ(2k) (closed forms k≤6, direct sums k≥7) match the f64 table
  to 2e-14 (table is COEF_INFL-deflated here; computation verified).
- **Certified zeta error** (n=600, 200 bits): err(ζ)=1.1e-56, err(ζ′)=5.8e-56, err(ζ^(21))=1.7e-40 at t=40
  (dominated by the rounding budget on Σ(ln k)^21 k^{−1/2} ~ 1e18; EM remainder ~1e-100+).

## Results — the deliverable table (L_k = (Xi^(k))² − Xi^(k−1)Xi^(k+1), Xi²>0, sign(L)=sign(q))
err = certified bound: EM remainder + MPFR rounding budgets + Stirling truncation, propagated through
ζ-log-derivs → u → Bell → q → L (rigorous given the ζ certified errors); cross-checks below confirm it.

| t | k | L_k (200 bit) | err bound | bracket q=B_k²−B_{k−1}B_{k+1} | Bk_scale | VERDICT |
|---|----|---------------|-----------|------------------------------|----------|---------|
| 40 | 18 | +1.98418056215491059776289274990778229e-20 | 8.4e-34 | +4.4246e1 | 5.1e15 | **POSITIVE** (RH-consistent) |
| 40 | 19 | +2.02800690365247749861567070733651025e-20 | 8.5e-34 | +4.5224e1 | 1.0e17 | **POSITIVE** (RH-consistent) |
| 40 | 20 | +2.04893764502210301966670380208203316e-20 | 8.6e-34 | +4.5691e1 | 2.1e18 | **POSITIVE** (RH-consistent) |

Controls (must match mpmath dps=60):
| t | k | L_k (200 bit) | err | VERDICT |
|---|----|---------------|-----|---------|
| 40 | 3 | +1.65739618310265222587132235507709391e-21 | 7.0e-35 | POSITIVE (mpmath 1.657e-21 ✓) |
| 33.6 | 8 | +2.16679519055152386783479309432127937e-17 | 1.1e-29 | POSITIVE (mpmath 2.166e-17 ✓) |
| 56.5 | 3 | +8.86903860261006855332786559199110904e-32 | 1.5e-47 | POSITIVE (f64 8.868e-32, 0.02% ψ-fix shift) |
| 35.5 | 4 | +1.02188146283085930216522667696662775e-18 | 2.4e-31 | POSITIVE (f64 1.022e-18 ✓) |

## Cross-checks (rounding / EM truncation independence)
- k=20 @ t=40, 200 vs 256 bits: agree to |Δ|=3.4e-63 (≈42 significant digits) — arithmetic rounding
  negligible; the 8.6e-34 certified bound is conservative.
- k=20 @ t=40, n=600 vs n=900 EM terms: |Δ|=1.2e-62 — EM truncation converged (as certified).

## u-derivative reality self-check (t=40)
u^(16..21) = −5.08e12, −8.84e13, −1.64e15, −3.21e16, −6.63e17, −1.44e19 (pole-dominated: nearest zero
γ₇=40.919 at d=0.92, consistent with the f64 note's scale analysis). max|Im iⁿAₙ| = 1.7e-42 … 8.4e-40
vs |u^(n)|~1e19 → Im/|u| ~ 1e-59: log Xi computed as a real function to ~60 digits.

## Honest overall verdict
- **No negative L_k anywhere; every one of the 7 flagged points is POSITIVE with |L|/err ≥ 1e13.**
- The flagged Taylor-series negatives (series diverges at t≳35) are confirmed artifacts by a fully
  independent high-precision route.
- The f64 route-B numbers at k=18/19/20 (+3.26e-20 / −3.95e-19 / +1.10e-17) were f64 noise; the true
  values are +1.98e-20 / +2.03e-20 / +2.05e-20, all positive. The f64 "negative" at k=19 was an
  artifact, now ruled out at 2e-20 ± 1e-33.
- RH-consistency framing (firewall): L_k ≥ 0 is a NECESSARY condition for RH (RH ⇒ ξ ∈ Laguerre–Pólya
  ⇒ {ξ^(k)} log-concave — classical). All positives are RH-consistent with ZERO evidential weight for
  RH (restatement class). This run settles the last open disproof-capable check: no L_k(t)<0 confirmed
  at any of the 7 flagged points; k=18/19/20 @ t=40 are POSITIVE, not merely inconclusive.
- Known t=0-only caveat: Stirling at |s/2|=1/4 is broken (Xi(0) via direct gamma); sidestepped with
  hardcoded Γ(1/4). All decision points are at t≥30 where Stirling is fine.

## Files
- tools/wave8d/src/bin/lk_zeta_mpfr.rs (new; f64 lk_zeta.rs untouched)
- research/notes/wave8d-lk-mpfr-run-2026-08-18.txt (full output)

## REFEREE VERDICT + FIX (2026-08-18, hostile blind referee f4ea49ff)
- **CLAIM HOLDS — CHECKED NUMERICALLY**: independent 256-bit probe (different derivative mechanism:
  unsigned-Stirling Pochhammer + correct |Γ| modulus + finite-difference route over ln|ξ| with no
  derivative machinery) confirms ALL 7 L_k > 0; q matches to 7 digits; positivity survives by ≥5
  orders even against honest error. No RH disproof. File: referee-lk-mpfr-2026-08-18.md.
- **REAL BUG FOUND + FIXED** (does not flip verdict): gamma_complex_stirling loop stepped p *= z^{-1}
  giving z^{-k} instead of z^{-(2k-1)} → |Xi|² off ~1.4e-5 rel (L_20 = 2.048938e-20 vs correct
  2.048909e-20). The claimed "certified error ~1e-33" was therefore NOT a valid certified bound
  (honest systematic error ~1e-25). FIXED (step by z^{-2}); re-run now matches the referee's correct-Γ
  values to the printed digit at all 7 points (L_20=2.04890928475603536160675251662865427e-20, exact),
  err<1e-51 (30+ orders below signal). Sign convention verified (L_k = Xi²·q, q from u-derivs only,
  Γ-independent). "sign pattern FAILED" at 62.1/66.1 = expectation-list bug (2 zeros γ13/γ14 between
  57.9 and 62.1); computed signs correct.
- **FINAL: L_k(t) > 0 at all 7 flagged points (t=40 k=18/19/20; controls t=56.5 k=3, t=33.6 k=8,
  t=35.5 k=4, t=40 k=3) — triple-implementation-confirmed, error-honest. NO RH DISPROOF. NO INCONCLUSIVE.**
