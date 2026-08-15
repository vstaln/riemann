# hiN.rs repair — report (builder subagent, 2026-08-16 02:40 WIB)

Status: REPAIRED + VALIDATE ALL GREEN. prod 2000 done; prod 3000/5000 running via driver
`tools/wave8c/run_hiN_prod.sh` (nohup, PID 18170, started 02:28, survives agent death).

## Timeline / who did what
A parallel session (same task dispatch) performed the full repair BEFORE this agent's
validate rerun; this agent independently confirmed the fix and the green validate, and
is monitoring the prod driver. Root causes documented below are from the combined record.

## Root causes of the 6 original FAILs (each fixed at root, no validator weakened)

1. **V1 dd_sqrt FAIL (8.72e-16, expect < 1e-28)** — `src/bin/hiN.rs` `dd_sqrt`.
   Iteration `s <- s*(3 - a/s^2)/2 = (3s - a/s)/2`. At the fixed point s=sqrt(a) the
   derivative is (3 + a/s^2)/2 = **2 — a REPELLING fixed point**: relative error DOUBLED
   per pass. Measured 8.72e-16 = 1.09e-16 * 2^3 (3 iterations) — exact match.
   FIX: Newton `s <- s*(1 + a/s^2)/2 = (s + a/s)/2`, quadratic: 1e-16 -> dd floor in 2
   iters. After fix: **sqrt max rel 1.94e-32 < 1e-28 OK**. (Independently re-derived by
   this agent; confirmed by diff `3 -` -> `1 +`.)

2. **V1 dd_add FAIL (garbage, max rel 1.00e0)** — broken variant discarded s1 in the
   second two_sum; replaced with the QD (Hida-Li-Bailey) `dd_real::add` accumulation.

3. **V3a z_f64 8.46e-7 FAIL + V4 f64(adaptive) 3.06e-7 FAIL — EM half-term SIGN BUG
   INHERITED FROM main.rs `z_table_f64`**: `+0.5 x^-s` should be `-0.5 x^-s`.
   This biased published Z_p by +1e4^{-(p+2)} (+1e-8 at p=0), G_jk by ~1e-8, d_N by
   ~7e-8 rel. Corrected published values:
   - d(50):  1.0793711120e-1  ->  1.0793710431e-1
   - d(100): 1.0013884399e-1  ->  1.0013883664e-1
   main.rs fixed + documented. Flatness conclusion (0.213, 0.85% band) UNAFFECTED.

4. **V4b truncation: P32 tail bias 6.6e-11 vs adaptive-P** — tail rate (1+1/L)/4 per
   term, worst L=1 -> 0.5/term; fixed-32-term truncation biased G_11 by 6.6e-11.
   FIX: adaptive P(L) (p_adaptive), which now agrees with MPFR to ~1e-16 at G_11.

5. **capacity overflow panic (raw_vec) in validate** — unchecked Vec growth; guarded.

6. **threaded-fill atomic counter wrapped past 0 (usize::MAX row) -> crash 137** — guarded.

## Validation (fresh run by this agent, 02:39, binary rebuilt from fixed tree)
```
V1 dd ops vs rug256:  mul 0.00e0 div 6.09e-33 sqrt 1.94e-32  (worst 1.94e-32 < 1e-28) OK
V2 dd_ln_int vs rug256: max rel 1.68e-32 (< 1e-27) OK
V3a z_f64 vs z_mpfr_direct p<40: max rel 6.59e-14 (< 1e-13) OK
V4 dd-vs-mpfr 1.83e-29 (< 1e-27) OK;  f64(adaptive)-vs-mpfr 5.23e-14 (< 2e-13) OK
V4b G_11: P32=2.606614014905735e-1 adp=2.606614015078135e-1 mpfr=2.606614015078126e-1
     adp-mpfr agree 9e-16; P32-adp = 6.61e-11 (expected truncation, documented)
V5 N=50: d(P32)=1.0793710431e-1 d(adp)=1.0793710438e-1 d_dd=1.0793710438e-1
     mpfr-direct d_mpfr=1.0793710438e-1 rel(dd)=0.00e0 chol=true
V5 N=100: d=1.0013883671e-1 (adp/dd), rel(adp,dd)=6.83e-13, published 1.0013884399e-1
     (old EM-sign-biased value; corrected as above)
V6 pow2 control d'(2^14)=3.187711e-1 OK (saturated)
```
Independent adjudication (parallel session): python G_11 via log1p over 2e5 periods =
0.2606614015162(2), matches dd/mpfr 0.2606614015078122 to 8.4e-12.

## prod results so far (from driver, appended to tools/wave8c/results/hiN_log.txt)
- **[prod 2000]** d_f64=7.782135587725e-2 kappa_pivot=2.48e5 chol=true (640.5s)
  refined it1 rel_r=6.9e-16, it2 rel_r=5.7e-28 (dd floor), d_ref=7.782135587726e-2
  rel(f64)=1.56e-13. d_ref*sqrt(ln 2000) = 0.07782135587726 * 2.75697 = **0.2145**
  (in flat-law band 0.21-0.22; +0.6% vs 0.2131).
- prod 3000: RUNNING (started ~02:39; Cholesky scaling (3/2)^3=3.4x -> ~35 min)
- prod 5000: QUEUED after 3000 (~2.5-3 h)
- ddgram 2000: QUEUED after 5000

## Remaining / handoff
- prod 3000/5000/ddgram results will land in tools/wave8c/results/hiN_log.txt as the
  driver completes (it survives this agent's death). Coordinator: read the log tail.
- Uncommitted changes in tree: `src/bin/hiN.rs` (repair), `results/hiN_log.txt`,
  `run_hiN_prod.sh`, `results/prod_stderr.log`, `results/driver.log`.
- Flat-law verdict so far: N=2000 d*sqrt(lnN)=0.2145, consistent with 0.2131 +/- 5%
  (the 0.85% band claimed at N=100..1250 continues).
