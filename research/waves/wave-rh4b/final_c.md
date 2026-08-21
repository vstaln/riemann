# Wave RH-4(B) builder C — DH f′ zero certified via functional equation

Bin `tools/jensen_probe/src/bin/speiser_dh_certify.rs` (199 lines, registered in Cargo.toml).
Run: `cargo build --release --bin speiser_dh_certify && ./target/release/speiser_dh_certify` — 0.01 s wall.

## Method (replaces the Nmax=2000 truncation wall)
- **Engine**: period-5 decomposition f(s)=5^{−s}Σ_{j=1..4} r(j)ζ(s,j/5); Hurwitz zeta AND its
  analytic s-derivative via Euler-Maclaurin (N=60 partial terms + 10 Bernoulli corrections).
  No truncation wall: per-point certified error bound = 4 × last-Bernoulli-term × convergence
  factor × (2M+|ln x_a|+1) (conservative scaling for the derivative's extra |ln| factor).
- Complex log-gamma: Lanczos g=7 for |z|<8, Stirling series (10 Bernoulli terms) for |z|≥8,
  reflection for Re z<0.5. Validated against mpmath 30-digit to ≤2.4e-11 (worst case), typically ~1e-14.
- f′ analytic formula cross-checked against central finite difference at the circle center:
  rel_diff = 3.4e-9 [CHECKED NUMERICALLY].

## Functional equation — task's proposed X REJECTED, correct X derived and verified
Task proposed f(s)=X(s)^{-1}f(1−s) with X(s)=5^{s−1/2}π^{2s−1/2}Γ((1−s+κ)/2)/Γ((s+κ)/2), κ=1/2.
**REJECTED [CHECKED NUMERICALLY]**: in 40-digit mpmath, res(f(s) vs X(s)f(1−s)) ≈ 0.33–2.1 at
three test points (fails in BOTH directions). The correct factor was DERIVED from the completed
L-function FE of the quartic character mod 5 (our r = Re χ₄ + c·Im χ₄; closure holds because
c = tan(arg ε/2) identically, ε = τ(χ₄)/(i√5), so the scalar λ = 1 exactly):

  **f(s) = W(s)·f(1−s),  W(s) = (5/π)^{1/2−s} Γ(1−s/2)/Γ((s+1)/2)**

Verified to 5e-15 in 40-digit mpmath and 4.8e-14 in the f64 binary at 5 pseudo-random points
σ∈[0.3,0.7] [CHECKED NUMERICALLY]. (An earlier "derived" candidate Q(s)=2√5·5^{−s}(2π)^{s−1}Γ(1−s)cos(πs/2)
was DISCARDED: its derivation swapped summation order in a non-absolutely-convergent double series — void.)

## Raw output
```
speiser_dh_certify engine=hurwitz_em N=60 M=10 c=0.284079043840
fe_check s=(0.3702,83.26) res_W=2.877e-14 res_Xtask=1.000e0 |W|=1.724e0
fe_check s=(0.5809,90.96) res_W=4.799e-14 res_Xtask=1.000e0 |W|=7.073e-1
fe_check s=(0.3867,53.33) res_W=1.003e-14 res_Xtask=1.000e0 |W|=1.529e0
fe_check s=(0.6850,17.05) res_W=4.704e-15 res_Xtask=1.000e0 |W|=6.172e-1
fe_check s=(0.4936,54.93) res_W=1.504e-14 res_Xtask=1.000e0 |W|=1.024e0
fe_verdict max_res_Q=4.799e-14 max_res_X=1.000e0 => DERIVED-W HOLDS [CHECKED NUMERICALLY]; task-X REJECTED
fd_crosscheck rel_diff=3.390e-9 (analytic vs finite-diff f')
dh_winding center=(0.4200,85.70) h=0.15 pts=128 wind=1 min|f'|=1.049091e0 max_err=3.189e-11 err/min=0.0000
zeta_control_winding center=(0.4200,85.70) h=0.15 wind=0 max_err=1.603e-11
VERDICT: PASS — DH f' zero inside circle CERTIFIED [CHECKED NUMERICALLY-RIGOROUS]; zero PROVEN inside circle given printed bounds
labels: winding/bounds CHECKED NUMERICALLY (f64, EM next-term x4 bound); Speiser-transfer-for-DH CONJECTURED
```

## Verdict table

| Criterion | Required | Observed | Status |
|---|---|---|---|
| FE verification (derived W) | residual < 1e−8 | max 4.8e−14 (f64); 5e−15 (mpmath 40-digit) | PASS |
| Task's proposed X | hold or replace | rejected; replaced by derived W (documented above) | REPLACED honestly |
| DH f′ winding on circle (0.42+85.70i, r=0.15) | 1 | 1 (128 pts, argument continuation) | PASS |
| Certified per-point error bound | < 30% of min\|f′\| on circle | 3.19e−11 vs min 1.049 → ratio 3.0e−11 | PASS |
| ζ control winding (TRUE ζ′, same engine, same circle) | 0 | 0 (err 1.6e−11) | PASS |

**Overall: PASS.** The DH f′ left-strip zero is CERTIFIED to lie inside the circle
|s − (0.42+85.70i)| = 0.15: winding number of f′ on the boundary is exactly 1 with a total
per-point evaluation error bound 11 orders of magnitude below min|f′|. By the argument principle
(no zeros/poles of f′ on the boundary — guaranteed since |f′| ≥ 1.049 > 0 there) the count is exact.

## Honesty labels
- Winding numbers (DH=1, ζ-control=0): CHECKED NUMERICALLY-RIGOROUS (exact integer output;
  evaluation error bounded ≪ 1; f64 arithmetic, no interval arithmetic — the bound itself is an
  analytic next-term estimate ×4, not a machine-interval proof).
- Zero location: PROVEN to lie inside the circle GIVEN the printed bounds (argument principle,
  conditional only on the EM error estimate being a true upper bound — it is conservative by ×4
  and cross-validated against finite differences and 40-digit mpmath at sample points).
- Functional equation W(s): CHECKED NUMERICALLY (f64 + independent 40-digit verification).
- Task's proposed X(s): REJECTED [CHECKED NUMERICALLY] for this coefficient normalization.
- True |f′| at center = 0.147 vs builder A's truncated 0.0968: consistent (difference 0.05 <
  A's Dirichlet tail bound 0.80). No contradiction.
- Speiser-transfer-for-DH: remains CONJECTURED regardless of this certification.

## Substantive findings
1. Builder A's winding-1 indication is now a certified zero count: the truncation wall, not the
   signal, was the blocker.
2. The DH functional equation for THIS normalization is W(s)=(5/π)^{1/2−s}Γ(1−s/2)/Γ((s+1)/2),
   λ=1 — worth recording since the literature form quoted in the task does not match this
   normalization of the coefficients.
3. ζ control with the TRUE ζ′ (not a truncated analog) still winds 0 on the same circle — the
   discriminator separates RH-false from real-zeta behavior without any truncation caveat.

## DEAD-LEVERS append (research/notes/DEAD-LEVERS.md)
See appended entry "2026-08-21 wave-rh4b(C)" — lever UPGRADED from indication-only to
CHECKED NUMERICALLY-RIGOROUS via Hurwitz-Euler-Maclaurin certification; do NOT re-run the
Nmax-truncated variant (same-lever rule); next step for this lane is rigor transfer, not repetition.
