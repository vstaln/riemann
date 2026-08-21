# Wave RH-4(A) — speiser_dh_control results

Builder A, bin `tools/jensen_probe/src/bin/speiser_dh_control.rs` (registered in Cargo.toml).
Run: `cargo build --release --bin speiser_dh_control && ./target/release/speiser_dh_control` — 23.6 s wall.

## Spec executed
- DH coefficients: r(n%5) = [1, c, −c, −1, 0], c = (√(10−2√5)−2)/(√5−1) — source: ranking.md funded Lane D spec (reproduces canonical c≈0.2840790438).
- f′(s) = −Σ_{n=2}^{2000} r(n) ln(n) n^{-s}, direct sum, f64.
- Scan σ∈[0.05,0.50] step 0.01, t∈[10,120] step 0.05.
- Winding: circle radius 0.15 centered at grid min, 64 points, argument continuation.
- Control: truncated real-analog ζ′ = −Σ_{n=2}^{2000} ln(n) n^{-s}, same circle; must wind 0 (wave-8B certified the real strip empty).

## Raw output
```
speiser_dh_control Nmax=2000 c=0.284079043840
dh_fprime_min sigma=0.4200 t=85.70 val=9.675581e-2
rem_abs_literal cap=1e6 val=3.453570e6 NOTE=diverges_as_n->inf
dh_rembound dirichlet=8.018311e-1 at sigma=0.4200; |f'|_center=9.675581e-2 ratio=8.287
dh_winding circle_center=(0.4200,85.70) h=0.15 pts=64 wind=1
zeta_control_winding center=(0.4200,85.70) h=0.15 wind=0
VERDICT: FAIL dh_wind_ok=true zeta_ctrl_ok=true remainder_ok=false (discriminator uncertified/absent)
```

## Verdict table

| Criterion | Required | Observed | Status |
|---|---|---|---|
| DH f′ winding at min | 1 | 1 | PASS [CHECKED NUMERICALLY] |
| ζ-control winding | 0 | 0 | PASS — discriminator NOT broken |
| Remainder < 10% of \|f′\| | yes | Dirichlet bound 0.80 vs \|f′\|=0.0968 (ratio 8.29) | **FAIL** |
| Literal task bound Σ\|r\|ln n·n^{−0.05} | printed | DIVERGES (exponent 0.05<1); capped value 3.45e6 @ cap 1e6 | reported honestly |

**Overall: FAIL on certification** — the discriminative signal is present and the control behaves,
but Nmax=2000 cannot certify a zero of magnitude ~0.097 in the strip: the certified Dirichlet-test
remainder bound (2B·ln(N+1)/N^σ, B=1+c≈1.284) exceeds |f′| by ~8×. The winding-1 result is
therefore a strong INDICATION, not a certified zero count.

## Substantive findings
1. The strongest |f′| minimum sits at t=85.70 — matching the canonical Voronin DH off-line zero
   height (~85.699i), NOT the proposal's unverified 14.12 saddle. ranking.md's suspicion about
   the 14.12 claim is confirmed empirically: no comparable minimum appears near t≈14.
2. The RH-false control FIRES correctly (DH winds 1, real-analog ζ′ winds 0): the Speiser-style
   discriminator distinguishes an RH-false function from zeta in this box. This is exactly what
   charter rule 7 demanded before trusting any Speiser-lane claim.

## Honesty labels
- Winding numbers (DH=1, ζ-control=0): CHECKED NUMERICALLY (f64 only; no interval/rug pass).
- Existence of a DH f′ left-strip zero near 0.42+85.70i: CONJECTURED-but-indicated (winding 1 on
  truncated series; remainder bound not met at Nmax=2000). Certification needs larger N or
  functional-equation-accelerated evaluation + interval arithmetic.
- Speiser-transfer-for-DH: CONJECTURED regardless of outcome (per task spec).
- Task's literal remainder bound diverges; the certified substitute is the Dirichlet/Abel bound
  stated above. No validator was weakened — the literal bound is infinite and cannot be a criterion.

## Recommended next step (not executed here)
Re-run certification with functional-equation evaluation (χ(s)f(1−s)) or N≥10^6 with interval
arithmetic to push the certified bound below 10% of |f′|; then the winding-1 becomes certifiable.
