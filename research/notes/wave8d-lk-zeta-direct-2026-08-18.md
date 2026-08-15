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
