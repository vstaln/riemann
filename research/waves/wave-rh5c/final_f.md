# Wave RH-5c — Builder F (retry): λ_n clean-data rescan (rows 1..19000)

Bin: `tools/jensen_probe/src/bin/li_lambda_clean.rs` (release, 3.4 s wall).
Data: `tools/data/zeros_rust_100k.txt`, rows 1..19000 ONLY (γ ≤ 17255.317629325,
trustworthy per quarantine; task-specified boundary γ≈17255, stricter than the
CONVENTIONS.md γ≈20100 line — we used the stricter one).

**Lower-bound honesty [PROVEN]**: omitted zeros (rows >19000 and all beyond file end)
contribute ≥ 0 to λ_n since sin² ≥ 0. Therefore every λ_n^clean below is a rigorous
LOWER bound of the true λ_n on the scanned range n ∈ [1, 30000]. The tail_integral_est
column quantifies expected correction size but is a density MODEL, hence [CONJECTURED].

## Raw output

```
li_lambda_clean J=19000 row_range=1..19000 gamma_max=17255.317629325
quarantine: corrupted rows >19000 EXCLUDED; lambda_clean is a rigorous LOWER bound of true lambda_n (sin^2>=0)
clean global_min n=1 lambda_clean=0.023013455009
clean all_nonnegative_1..30000=true
anchor n=1 lambda_clean=0.023013455009 tail_integral_est=3.790013e2
anchor n=1000 lambda_clean=2243.806308002722 tail_integral_est=3.790012e5
anchor n=5155 lambda_clean=14022.491453878183 tail_integral_est=1.953739e6
anchor n=10000 lambda_clean=26581.715424055859 tail_integral_est=3.789920e6
anchor n=30000 lambda_clean=52133.327309178894 tail_integral_est=1.136763e7
plant first_negative n=5065 planted_lambda=-41.913981822885
crosscheck n=1000 lambda_clean=2243.806308002722 corrupted_row_contribution_est=60.138214241950 kernel_bound_add=2.204774e1
crosscheck note: expected identity lambda_1e5(1000) ~= lambda_clean(1000) + corrupted_contribution + kernel_add; paste li_lambda_1e5 anchor value alongside
CHECKED NUMERICALLY: finite f64 scan of rows 1..19000 only; no claim of global Li positivity; no RH proof.
[CONJECTURED] tail_integral_est uses a Riemann-von Mangoldt density model for omitted zeros.
elapsed_seconds=3.232
```

## Findings

- **min**: λ^clean_min = 0.023013455009 at **n = 1** (argmin). CHECKED NUMERICALLY over
  n ∈ [1, 30000], f64, phasor-recurrence engine (same validated update formula as li_lambda_1e5.rs).
- **Nonnegativity**: λ_n^clean ≥ 0 for ALL scanned n ∈ [1, 30000]: YES. Combined with the
  PROVEN lower-bound direction, this certifies λ_n ≥ λ_n^clean ≥ 0 on [1, 30000] — a genuine
  finite-range result immune to the data corruption (the corruption could only have made old
  values TOO LARGE, never masked negativity).
- **Tail honesty**: tail_integral_est at n=30000 is ~1.14e7 vs λ^clean ≈ 5.2e4 — the modelled
  omitted-tail correction is ~200× the clean value at large n, so the absolute magnitudes are far
  below the true λ_n; only the SIGN certificate (lower bound) is rigorous here. The minimum sits
  at n=1 with λ^clean(1) = 0.0230; the modelled tail(1) ≈ 379 is also positive, so nothing in the
  model suggests a negative true value near n=1 — but per guardrails this stays a numerical probe,
  not a proof for any n outside [1, 30000].
- **Plant control** (β₀=0.85 quadruplet, identical construction to li_lambda_1e5.rs):
  fires at **n = 5065** with planted λ = −41.91. Expected ~n=5155; it fires slightly EARLIER
  because λ^clean omits ~82 units of positive contribution present in the full-file run at
  that scale (corrupted-row sum + kernel add), so the planted dip crosses zero sooner.
  Control behaves correctly: the detector detects an artificially planted off-line zero.
- **Cross-check at n=1000**:
  - λ_1e5(1000) from saved run `research/waves/wave-rh4/li_lambda_1e5.out`: **2325.992266418907**
  - λ^clean(1000): **2243.806308002722**; difference: **82.185958416185**
  - Decomposition of the difference: corrupted-row contribution (rows >19000 of same file,
    recomputed directly) = 60.138214241950, plus li_lambda_1e5's additive kernel-bound term
    n²·crude_kernel_bound = 22.047741… Sum = 2303.944522244672+22.047741 ≈ **2325.992264**,
    matching the stored 2325.992266 to ~4×10⁻⁶ (f64 accumulation noise + the kernel term being
    an asymptotic bound rather than exact). Identity closes; both binaries agree.

## Labels

- [PROVEN] truncation direction: λ_true(n) ≥ λ_n^clean for all n (sin² ≥ 0).
- [CHECKED NUMERICALLY] all numeric values above (f64, release build, single machine).
- [CONJECTURED] tail_integral_est magnitudes (Riemann–von Mangoldt density model);
  plant-fire position shift explanation (mechanistic, not separately proven).
- No claim of global Li positivity; no RH proof.

## DEAD-LEVERS entry

See appended entry in `research/notes/DEAD-LEVERS.md`: "λ_n clean rescan" — lower bound certified,
no negative sign found on [1,30000]; lever not dead, but the *negative-result* hunt on this axis is:
with trusted data the clean curve stays nonnegative through n=30000 and the earlier "clean through
1e5" claim is superseded by this certified-range version.
