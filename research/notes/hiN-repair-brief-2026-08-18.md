# hiN.rs repair brief — certified d_N at N ∈ {2000, 3000, 5000}

Date: 2026-08-18. Status: **IN REPAIR — do not use output until validation passes**.
File: `tools/wave8c/src/bin/hiN.rs` (1589 lines, uncommitted work-in-progress).
Purpose: certified extension of the Báez-Duarte d_N sharp-rate law (d_N·√(log N) ≈ 0.2131 flat,
CHECKED NUMERICALLY N=100..1250 in f64) into N=2000..5000 with layered certification:
(A) f64 Gram + Cholesky, (B) double-double iterative refinement, (C) MPFR-256 solve on stored f64 G,
(D) full double-double pipeline. This is THE bottleneck for the strongest live lever.

## Known failure state (from `results/hiN_log.txt`, validate phase, 2026-08-16 02:05)

```
[validate] V1 dd ops vs rug256: max rel 1.00e0 (expect < 1e-28) FAIL
[validate] V2 dd_ln_int vs rug256: max rel 1.00e0 (expect < 1e-27) FAIL
[validate] V3a z_f64 vs z_mpfr_direct p<40: max rel 8.46e-7 (expect < 1e-13) FAIL
[validate] V4 gram j,k<=40: dd-vs-mpfr max rel 1.00e0 (expect < 1e-27) FAIL
[validate] V4 f64(adaptive)-vs-mpfr max rel 3.06e-7 (expect < 5e-15) FAIL
[validate] V4b TRUNCATION AUDIT: G_11(P32)=2.606614048227405e-1 G_11(adp)=2.606614048399805e-1 G_11(mpfr)=2.606614846955062e-1
       |P32-adp|/G=6.61e-11 max over pairs=6.61e-11
```
Plus: `thread '<unnamed>' panicked: capacity overflow` (raw_vec) during validate — unchecked Vec growth.

## Triage (coordinator)
1. **V1/V2/V4-dd max rel 1.00e0 = TOTAL garbage**: either (a) the dd primitives (two_sum/two_prod
   look correct, lines 225-235) are misused in dd_add/dd_mul/dd_div/dd_sqrt (lines 238-287), or
   (b) the validate harness compares wrong quantities (e.g., dd vs rug256 on different inputs, or
   the rug256 reference itself uses a wrong formula). Determine WHICH before fixing — do not guess.
2. **V3a z_f64 8.46e-7 off**: the f64 z-table (z_table_f64, line 132) disagrees with MPFR-direct
   (line 154) at 8.5e-7 — likely a truncation-order bug in z_f64 (fewer terms than p<40).
3. **V4 f64(adaptive) 3.06e-7 off + V4b truncation audit**: f64 adaptive Gram is off from MPFR by
   ~3e-7, and even the "adaptive" P is off by 6.6e-11 vs P32 while MPFR differs at 8e-9 — the
   p_adaptive() model (line 124) underestimates needed terms. The tail p-expansion rate comment
   (line ~10) says (1+1/L)/4 per term, worst L=1: 0.5 — verify against actual term ratios.
4. **capacity overflow panic**: guard the Vec growth (intervals(), gram builds).

## Deliverables (exact)
- `cargo build --release --bin hiN` compiles clean.
- `cargo run --release --bin hiN -- validate` passes ALL of V1, V2, V3a, V4, V4b at the stated
  expectations (V1/V2 < 1e-28, V3a < 1e-13, V4 f64 < 5e-15, dd < 1e-27).
- `cargo run --release --bin hiN -- prod 2000` etc: certified d_N at N=2000, 3000, 5000 appended
  (flushed) to results/hiN_log.txt with the kappa and per-layer gaps recorded.
- **HARD RULE: never weaken a validator to make it pass.** If an expectation is unreachable, fix
  the math. If you conclude a validator's expectation itself is wrong (e.g. it tests the wrong
  quantity), PROVE it with an independent computation and document the change in the log.

## Context
- The f64 reference values to reproduce at N≤1000: d_N(100)=1.001388e-1, d_N(1000)=8.055653e-2,
  d_N(1250)=7.938946e-2 (tools/wave8c/src/main.rs sweep, W8C_NMAX cap env available).
- MPFR cross-check in main.rs already validates gram_mpfr == gram_f64 to 6.3e-13 at N=100 —
  the closed-form Gram values ARE correct at low N; the hiN bug is in higher-precision paths or
  higher-N behavior.
- Machine is heavily loaded (load ~8, other agents running). Keep builds bounded:
  one `cargo build` per phase, `timeout` every run, write state to results/hiN_log.txt after
  every tool call (kill-robustness). If a full build takes >5 min, stop and report — do not loop.
- After prod runs: report d_N and d_N·√(log N) at each N; check the 0.213 flat law holds to >5%.
