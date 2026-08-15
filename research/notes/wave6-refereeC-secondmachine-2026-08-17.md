# WAVE 6 REFEREE 6C — SECOND-MACHINE INDEPENDENT RE-DERIVATION of 0.6734808616745137

**Date:** 2026-08-17. **Referee:** 6C (blind, joint C). **Status:** COMPLETE.
**Verdict: REPRODUCES — the certified record 0.6734808616745137 is reproduced
independently to machine precision (1.1e-16) with a separate implementation and a
different numerical strategy.**

## Joint
Reimplement the certificate VALUE computation from scratch: (1) H(1.464); (2) the bound chain
`(H−τ)/(1−B/m)` and the meaning of B; (3) eps=0.0062 floor consistency; (4) verdict.

**Method (separate implementation, different numerical strategy):** Rust, f64,
fixed 256-point Gauss–Legendre quadrature (nodes/weights by Newton–Raphson on Legendre
polynomials, self-contained, no external crates; error estimate by 128→256 node doubling),
musl release build. mpmath was NOT needed: the integrand is analytic on [0,1] (smooth cosine
window, no singularities), so f64 GL-256 reaches ~2e-16, matching the 16-digit reference floor.
Script: `research/notes/wave6-referee6c-H-and-bound.rs` (also
`scratch/referee6c/` with Cargo.toml). Run: `cargo build --release` then run the binary.
No file from `tools/` was read — all formulas below are from the notes' math only.

## Part 1 — H(α) at α=1.464: REPRODUCED to 2e-16

Formula (pinned from `better-test-family-H.md`; the brief's `w((1−w)/2·…)` is the integration
variable **times** the bracket, i.e. the linear window u ↦ u — this was the one ambiguity,
resolved from the notes):
```
H(a) = 2 − (Iv2 + J)/Iv²
Iv   = 2 sin(a/2)/a          = ∫₀¹ cos(a(t−1/2))dt        (L¹ moment of cosine kernel)
Iv2  = (1 + sin(a)/a)/2      = ∫₀¹ cos²(a(t−1/2))dt        (L² moment)
J    = 2 ∫₀¹ u·[ (1−u)/2·cos(au) + sin(a(1−u))/(2a) ] du
```

| a | mine (GL-256, f64) | reference (notes/mpmath) | agreement |
|---|---|---|---|
| √2 | 0.6725007036794117 | 0.6725007036794116 | 1 ulp |
| **1.464** | **0.6724674255777883** | **0.6724674255777881** | **1 ulp (2.2e-16)** |
| 1.49 | 0.6724218860964475 | 0.6724218860964475 | exact |
| 1.47 | 0.6724587094007293 | 0.6724587 (record table) | ✓ |

Quadrature error estimate 128→256: 2.2e-16 for a=1.464. Quadrature sanity: ∫₀¹x² = 0.3333333333333332 (exact to f64).
CHECKED NUMERICALLY (binary: `scratch/referee6c/target/release/referee6c`). Also consistent with the
closed-form `H(√2) = 2 − [1/2 + (1/√2)cot(1/√2)] = 2 − 1.3274992963 = 0.6725007` (PROVEN in notes; c = Iv²/(Iv2+J) is the reciprocal Rayleigh quotient — `H = 2 − 1/c` is the same number).

## Part 2 — the bound chain and B: REPRODUCED to 1.1e-16

Closed form (from `discovery-6732629.md`, reverse-engineered tawan machinery):
```
τ = psum·(m−6)/m                 psum = 1/320, m = 171   → τ = 0.0030153508771930
A = ε·(m−6)                      ε = 0.0062              → A = 1.0230000000
B = Φ_m(A) = 2√((m−1)A/m) − 1 + A/m                      → B = 1.022928210354
bound = (H − τ)/(1 − B/m)                                 → 0.6734808616745138
```
target = 0.6734808616745137. **abs diff = 1.11e-16** (f64 machine epsilon). REPRODUCED.

**What B is:** in FINAL-RECORD context, B = Φ_m(ε(m−6)) — the coboundary cap function evaluated at
the pressure-scaled floor argument A = ε(m−6) (ε = certified floor 0.0062; m−6 = block length minus
the 6 pressure cells). Numerically B = 1.022928210354, B/m = 0.0059820363 ≈ 0.6%. The denominator
(1 − B/m) = 0.994018 is the mass fraction surviving the redistribution boundary cap; dividing by it
repairs exactly the boundary loss, lifting H−τ = 0.6694520747 to 0.6734808617. Consistency check:
backing B out of the target gives B_backout = m(1 − (H−τ)/target) = 1.022928210354, which EQUALS
Φ_m(ε(m−6)) to 3e-14. So the B that makes the chain hit the target is exactly the machinery's
closed-form B — no missing term, no wrong τ, no wrong B. (The ε-dependence of B through A is what
makes the eps story coherent, see Part 3.)

**Cross-checks on the leaderboard (same closed form, all reproduce):**
- α=1.49, m=171, eps=0.0062 → 0.6734350481 (record: 0.673435) ✓
- α=1.47, m=183, eps=0.00577, psum=1/320 → 0.6731929115 (tawan record: 0.673193) ✓

Gain decomposition: bound − H = [H·B/m − τ]/(1−B/m) = 0.0010134; fully accounted, small, no
order-unity distortion. 256-law ceiling 0.6818 ≫ 0.673481 — no ceiling violation. (Breaking 0.6818
would need ε ≈ 0.026, far above the certified 0.0062 — INCONCLUSIVE beyond "not this certificate".)

## Part 3 — eps=0.0062 floor: structurally consistent

What would certify eps (terminal-cell / crystal-floor argument, from `eps-boundary-exact.md`):
- The coboundary scheme certifies a local floor: the capped functional F_B(ε) ≥ ε on every cell of
  the 6D point-box lattice, with the cap itself depending on ε through A = ε(m−6) and B = Φ_m(A).
- Branch-and-bound with interval enclosures (grid 4000, max_nodes 25M) checks the inequality;
  the binding cells are the TERMINAL cells (all coordinates equal) where F_B has the least room.
- eps=0.00620 → True (1,096,556 nodes, full stack exhausted, no violation). eps=0.00621/2/3 → False
  (terminal-cell), and the 0.00621 terminal cell was re-evaluated at 60-digit mpmath: true value
  0.00591883580089175 < 0.00621 — a REAL inequality violation, not an enclosure artifact.
- Hence certified eps = 0.0062 is the exact optimum of the coboundary class at α=1.464 with tawan's
  coefficients; α=1.464 is simultaneously the lowest α certifying 0.0062 (1.463 fails, 503,074
  nodes). All consistent with the record's claims.

Consistency of eps with the H-vs-bound gap (the check I can actually run): with my independently
computed H(1.464) and the closed-form τ, B from ε=0.0062:
`(H(1.464) − τ)/(1 − B/m) = 0.6734808616745138 = 0.6734808616745137` to 1.1e-16. The exact-boundary
claim "0.0062 is the certified optimum" is CHECKED NUMERICALLY in the notes (verifier + mpmath
terminal-cell evaluation — not re-run by me; I could not run the 1M-node verifier). The ε-sharpness
(margin 0.0062 − 0.0059188 ≈ 2.8e-4 at the ε=0.00621 cap) is covered by the cap shift dΦ_m =
Φ'_m·dA ≈ 0.99·0.00165 = 1.6e-3 between ε=0.0062 and 0.00621 — CONJECTURED quantitative reading
of the notes' numbers, consistent with both verifier verdicts.

## Part 4 — VERDICT

**The record value 0.6734808616745137 REPRODUCES independently.**
1. H(1.464) = 0.6724674255777881 reproduced to 2.2e-16 by independent f64 Gauss–Legendre (different
   library, different quadrature, different precision strategy than the notes' mpmath `mp.quad`).
2. The bound chain `(H−τ)/(1−B/m)` with τ = (1/320)(m−6)/m and B = Φ_m(ε(m−6)) =
   2√((m−1)·ε(m−6)/m) − 1 + ε(m−6)/m reproduces 0.6734808616745137 to 1.1e-16. B is exactly the
   machinery's closed-form coboundary cap (backout matches Φ_m to 3e-14). No missing term, no wrong
   τ, no wrong B found.
3. eps = 0.0062 is arithmetically consistent with the chain; the 620/1e5-pass / 630/1e5-fail
   boundary is documented as a genuine terminal-cell inequality violation in the notes.
4. The redistribution gain (bound − H = +0.0010134) is real, small, and fully accounted — it does
   NOT exceed the 256-law ceiling, and the H-vs-bound arithmetic is exact.

Caveats (honest, do not change the verdict): (a) my re-derivation covers the VALUE chain; the
certificate's soundness — that the verified F_B ≥ ε inequality implies the proportion bound —
is the redistribution algebra (joint 6A) and the transfer to ζ (joint 6B), not re-derived here.
(b) The 0.0062-certification itself (1M-node interval run) was not re-run on a second machine;
the notes' three identical runs + the 60-digit terminal-cell violation check stand as the evidence.
(c) The ε→F_B functional dependence (cap shifts with ε) is read from the notes' numbers, not
re-derived — the terminal-cell value 0.0059188 < 0.0062 while 0.0062 certifies is only coherent if
F_B depends on ε through the cap; the notes' framing ("real counterexamples to the inequality at
those eps values") supports this, but this specific point is CONJECTURED, not machine-checked by me.

## Honesty ledger
- CHECKED NUMERICALLY (mine, independent implementation): H at {√2, 1.464, 1.47, 1.49}; τ; A; B=Φ_m;
  bound chain = target to 1.1e-16; B backout = Φ_m to 3e-14; leaderboard cross-checks α=1.49 and
  α=1.47/tawan. Binary: `scratch/referee6c/target/release/referee6c`; source:
  `research/notes/wave6-referee6c-H-and-bound.rs`.
- CONJECTURED: cap-shift reading of the eps boundary margin (Part 3).
- INCONCLUSIVE: (i) soundness of the F_B≥ε ⇒ proportion implication (joint 6A); (ii) the transfer
  to ζ (joint 6B); (iii) second-machine re-run of the 1M-node interval certificate itself.
- NO tool code read; no fabrication; nothing weakened. Discrepancy found vs record: none (1.1e-16
  = f64 rounding in the printed last digit of H).
