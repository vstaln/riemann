# 8C — Báez-Duarte d_N sharp rate: d_N·√(log N) ≈ 0.213 flat (CHECKED NUMERICALLY)

Date: 2026-08-18. Lever: Nyman–Beurling–Báez-Duarte. Status: **CHECKED NUMERICALLY** (f64 Cholesky, kappa ≤ 1e5).

## Question
Báez-Duarte: RH ⟺ d_N → 0. Known sharp-rate conjecture: d_N ≍ (log N)^(−1/2).
The cheap Burnol analysis (2026-08-15) reported "d_N·√N·√(log N) does NOT stabilize (0.72→6.70)" and treated
that as a live discriminating question. **That product was the wrong normalization.** Under d_N ~ c/√(log N),
d_N·√N·√(log N) = c·√N → ∞ necessarily — non-stabilization was expected, not discriminating.
The correct test is d_N·√(log N) → c.

## Data (tools/wave8c, f64 Cholesky with pivoting; N=10..1250 print in <1s, sweep aborts at N≥1600 on timeout)

```
N       d_N           d_N·√N     d_N·√(log N)
10      1.510410e-1   0.47763    0.2292
20      1.268230e-1   0.56717    0.2195
30      1.191920e-1   0.65284    0.2198
50      1.079371e-1   0.76323    0.2135
75      1.042841e-1   0.90313    0.2167
100     1.001388e-1   1.00139    0.2149
150     9.617927e-2   1.17795    0.2153
200     9.379479e-2   1.32646    0.2159
300     8.886027e-2   1.53910    0.2122
400     8.726997e-2   1.74540    0.2136
600     8.371051e-2   2.05048    0.2117
800     8.150621e-2   2.30534    0.2107
1000    8.055653e-2   2.54742    0.2117
1250    7.938946e-2   2.80684    0.2120
```

## Result
- **d_N·√(log N) ≈ 0.2131 ± 0.0018 (0.85% band) over N=100..1250** — flat, consistent with
  d_N ~ 0.213/√(log N), i.e. the Báez-Duarte conjectured sharp rate (log N)^(−1/2).
- Slight early drift 0.2292 (N=10) → ~0.213 (N≥100); thereafter stable to <1%.
- Under this law: d_N·√N = c·√N/√(log N) → ∞ (matches observed rise 0.48→2.81), so the
  2026-08-15 "no saturation" observation is fully explained — NOT evidence against the conjecture.

## Consistency with rigorous bounds
- Burnol lower bound d_N ≫ (log log N)^{3/4}/(log N)^{3/4} is strictly weaker than (log N)^(−1/2) —
  no contradiction.
- d_N(1000)=0.0806 vs √(log 1000)/√1000 = 0.0831 (the earlier "3% match" was coincidence of the
  wrong normalization at one point; the flat product is the real evidence).

## Trust limits
- f64 Cholesky with kappa ~ 1e5 at N=1250: retains ~11 digits — far above the 0.85% band, fine.
- Certification (MPFR 256-bit) currently only to N=100 (d_N == f64 to 2.2e-13 there). The flatness at
  N≥100 rests on f64 only.

## CORRECTIONS (2026-08-18 session 2 — two numerical bugs found in the published pipeline)
The hi-N certification work (below) found two biases in the ORIGINAL pipeline. Both are now fixed in
`tools/wave8c/src/main.rs` and in the new `tools/wave8c/src/bin/hiN.rs`; all previously published 8C
numbers carry them. **Neither affects the flatness conclusion** (both are ≤1e-6 relative; the band is
0.85%):

1. **Euler–Maclaurin half-term sign (inherited from main.rs `z_table_f64`).** The tail model used
   `+0.5·x^{−s}`; the correct upper-tail EM has **minus**: Z_p = Σ + x^{1−s}/(s−1) − ½x^{−s} +
   (s/12)x^{−s−1} − … . Verified numerically (n=10, s=2: minus-sign 0.0951663 = true tail; plus-sign
   0.1051667 wrong). Effect: every Z_p biased by +10⁴^{−(p+2)} (+1e-8 at p=0), G_jk by ~1e-8,
   **d_N by ~7e-8 relative**. Corrected values (CHECKED NUMERICALLY, dd ≡ MPFR-256 ≡ f64):
   - d(50): published 1.0793711120e-1 → **1.0793710431e-1** (rel shift 6.4e-8)
   - d(100): published 1.0013884399e-1 → **1.0013883664e-1** (rel shift 7.3e-8)
   - The 2026-08-17 claim "MPFR == f64 to 2.2e-13/6.3e-13" was TRUE as an arithmetic-agreement
     statement but both paths shared this z-bias (and the P=32 truncation below), so the absolute
     accuracy of the published d_N was ~1e-7, not 1e-13. Documented honestly; certification below
     now closes this gap.
2. **Fixed P=32 tail truncation.** The m≥4 tail series converges at rate (1+1/L)/4 per term; for
   j=k=1 (L=1) that is 0.5, leaving |G_11 error| ≈ 6.6e-11 (MEASURED: G_11(P32)=0.2606614014905735 vs
   adaptive 0.2606614015078135 vs MPFR-256 0.2606614015078122). Again invisible to the old MPFR
   cross-check (same truncation both paths). hiN uses P(L) adaptive: P = ceil(digits·ln10/ln(4L/(L+1)))+3
   (digits=17 f64, 31 dd/MPFR), capping at 110.
3. (Independent python adjudication, well-conditioned log1p sum of period integrals: G_11 =
   0.2606614015162 ± ~1e-11 — consistent with the corrected value.)

## NEXT (the strongest live lever) — status: IN EXECUTION
**Certified MPFR d_N extension to N ∈ {2000, 3000, 5000}** — exact closed-form Gram in MPFR at these N
is infeasible (O(N³) interval-operations at MPFR cost ≈ months), so certification is layered
(tools/wave8c/src/bin/hiN.rs):
- (A) f64 Gram, adaptive P(L), symmetric threaded fill + f64 Cholesky → d_f64 (fixes the N≥1600
  timeout of the old full-square fill);
- (B) iterative refinement with double-double (~106-bit) residuals → exact solve of the stored matrix;
- (C) threaded MPFR-256 Cholesky on the same stored Gram → independent solve check at every N;
- (D) FULL double-double pipeline at N=2000 (dd Gram incl. exact dd integer-ln table of 4N²+2 entries,
  dd Cholesky) → end-to-end measured gap, covering Gram closed-form + storage error, not just the solve.
Validation ladder (all GREEN, 2026-08-18): dd ops vs rug-256 max rel 1.9e-32; dd-ln vs rug 1.7e-32;
dd-Gram vs MPFR-direct Gram 1.8e-29 (pairs ≤ 40); d(50): **dd pipeline == MPFR-direct pipeline to
rel 0.0**; pow2 control saturates 0.3187711. Driver: tools/wave8c/run_hiN_prod.sh (results append
kill-safe to tools/wave8c/results/hiN_log.txt).
- Confirm d_N·√(log N) ∈ [0.21, 0.22] at N=2000..5000 → rate conjecture strengthened.
- Any deviation >5% → the flat law breaks; investigate (still not RH evidence either way, but sharpens
  the N-B lever's empirical structure).

## Files
- tools/wave8c/ (Rust, f64 sweep + MPFR cross-check; `cargo run --release` prints sweep; N list at src/main.rs line ~504)
- research/notes/wave8c-nyman-beurling-2026-08-17.md (prior state: MPFR==f64 to 6.3e-13 @N=100, decay slope −0.0892)
