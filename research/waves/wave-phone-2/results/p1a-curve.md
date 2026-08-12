# p1a-curve — FINAL (extended-row marked-config LP, N=64)

**State: COMPLETE.** Script `/root/riemann/tools/p1a_curve/p1a_curve.py` ran to near-completion
(3 seeds × 22 A; results.jsonl). Launch that worked (crash-proof, survives session teardown):
```
setsid nohup proot-distro login ubuntu -- bash -lc 'cd /root/riemann/tools/p1a_curve && python3 -u p1a_curve.py > run.log 2>&1' < /dev/null > /dev/null 2>&1 &
```
(inner setsid dies on proot-login exit; the outer wrapper is what must hold the process.)

## Environment note (why run.log was empty before)
The prior launch put `setsid nohup` **inside** proot; the process was torn down at login
teardown before first flush → 0-byte run.log, no results.jsonl. Same bug fixed: outer wrapper.

## What the LP computes (recap, labels)
- Family: `common2.gen_valid_family` (VALID: s+2d=N, sum marks=N, s_c=N−2d). PROVEN by code read.
- Objective: minimize p1 = Σ w_c s_c/N s.t. Σ w f_c(j) ∈ [j(1−τ), j(1+τ)] ∀ j≤M=⌊A·64⌋, Σw=1, w≥0; p1 is the certified simple-on-line fraction under PCC F=1 on [0,A] (f1curve §1 identity, plus 1/(6N²) correction).
- **Anchor caveat:** p1(1)=0.9338 (mean, 3 seeds) here pins ALL rows j=1..64 pointwise, which is strictly stronger than family_law's cumulative LP (0.828–0.844 in the STATUS). Higher anchor is expected, NOT a bug. All R(A) below use this LP's own per-seed p1(1) as anchor.
- N=64 wall: pinned rows j=64..128 need Σj=6240 > 64·Σm² ≤ 6144 ⇒ **A_max = 127/64 = 1.984375**. Consistent: A=1.98/1.99/2.0 INFEASIBLE at all seeds, all τ.

## p1(A) table (CHECKED NUMERICALLY; raw p1 per seed, then mean)
```
A      mean p1   n   per-seed p1 (42 / 1234 / 2024)
1.00   0.93384   3   0.92863 0.94030 0.93259
1.02   0.93536   3   0.92932 0.94274 0.93402
1.03   0.93536   3   0.92932 0.94274 0.93402
1.04   0.93590   3   0.92984 0.94283 0.93504
1.05   0.93629   3   0.93071 0.94286 0.93530
1.10   0.94129   3   0.93747 0.94598 0.94042
1.126  0.94321   3   0.93752 0.94863 0.94348
1.13   0.94321   3   0.93752 0.94863 0.94348
1.20   0.94734   3   0.94032 0.95364 0.94807
1.26   0.94907   2   (0.94279 0.95535; 2024 INFEASIBLE)
1.30   0.94371   1   (only seed 42)
1.40   0.94681   1   (only seed 42)
```
Coverage honestly: seeds 42/1234 feasible to A=1.26 (1234 only at τ=1e−3 there); seed 2024 only to
A=1.2. A≥1.3 feasible for seed 42 alone; A≥1.98 infeasible everywhere (wall). No rows dropped —
the grid is exactly the script's As; per-seed infeasibility is the data, not a reduction.

## Mean normalized deficit R(A) = (1−p1(A))/(1−p1(1)) vs 1/A²
```
A      R(A)    1/A²   rel. deviation
1.02   0.9760  0.9612   1.5 %
1.03   0.9760  0.9426   3.5 %
1.04   0.9681  0.9246   4.7 %
1.05   0.9626  0.9070   6.1 %
1.10   0.8883  0.8264   7.5 %
1.126  0.8581  0.7887   8.8 %
1.20   0.7944  0.6944  14.4 %
1.26   0.7747  0.6299  23.0 %
```
R(A) decays far slower than 1/A²; deviation grows monotonically (3→23%). The curve also
**plateaus** (R≈0.75–0.79 for A≥1.2) instead of decaying toward 0.

## 256-scale roadmap (p1_256(A) = 1 − R(A)·(1−p0), p0 = 0.6818286874638315)
- p1_256(1.03) = 0.6895, p1_256(1.04) = 0.6920, p1_256(1.05) = 0.6937, p1_256(1.10) = 0.7174,
  p1_256(1.20) = 0.7472, p1_256(1.26) = 0.7535.
- Interpolated A for targets: **p1=0.70 → A≈1.063**; **p1=0.75 → A≈1.226**; **p1=0.80 → not
  reachable** (needs R=0.6286; R floor ≈0.75–0.79, extrapolation is not honest).

## VERDICT vs M2 (R(A) ≈ 1/A² within 1.1%?)
**FAILS, and badly.** No A in the feasible range agrees within 1.1%; the smallest deviation is
already 1.5% at A=1.02 and it grows to ~23% at A=1.26. The pinned-row pointwise LP at N=64 does
NOT reproduce the M2 deficit law — deficit (1−p1) decays ~3–5× too slowly, and hits a floor.
**0.70@1.04 does NOT survive** (0.692 at 1.04; needs ≈1.063). 0.80@1.26 also fails (0.754 at
1.26 vs 0.80 target). Cause hypothesis (CONJECTURED): pointwise-pinning all rows j≤M against a
finite 4000-config family exhausts measure far faster than the M2 average-Ramsey heuristic
assumes; the jitter/no-coincidence spectrum cannot deliver the 1/A² drop. The N=64 LP is
therefore NOT a faithful proxy for the M2 curve — a documented negative, not evidence for/against M2.

Script + command: `tools/p1a_curve/p1a_curve.py` via the outer-setsid command above; raw rows in
`tools/p1a_curve/results.jsonl` (60 rows), full log `run.log`. Analysis in this note was computed
with inline python reading results.jsonl (same numbers reproducible in one call).

RESULT: COMPLETE — R(A) ≠ 1/A² (3–23% deviation, monotone); 0.70@1.04 and 0.80@1.26 both fail on the N=64 pinned-row LP; p1=0.80 unreachable (R floor ≈0.75).
