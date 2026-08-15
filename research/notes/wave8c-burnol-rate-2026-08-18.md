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

## NEXT (the strongest live lever)
**Certified MPFR d_N extension to N ∈ {2000, 3000, 5000}** to pin the constant and test whether
d_N·√(log N) stays flat past the f64 regime (kappa there ~1.5e5–3e5; MPFR Cholesky cost scales steeply —
needs the bounded-run discipline: one N per run, wall-clock capped).
- Confirm d_N·√(log N) ∈ [0.21, 0.22] at N=2000 → rate conjecture strengthened.
- Any deviation >5% → the flat law breaks; investigate (still not RH evidence either way, but sharpens
  the N-B lever's empirical structure).

## Files
- tools/wave8c/ (Rust, f64 sweep + MPFR cross-check; `cargo run --release` prints sweep; N list at src/main.rs line ~504)
- research/notes/wave8c-nyman-beurling-2026-08-17.md (prior state: MPFR==f64 to 6.3e-13 @N=100, decay slope −0.0892)
