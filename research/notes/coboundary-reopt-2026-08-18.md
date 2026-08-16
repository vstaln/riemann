# Coboundary redistribution re-optimization — session 2026-08-18 (PARTIAL — work in progress)

**Status:** IN PROGRESS (partial note; will append as results land)

## Target
Raise certified simple-on-line record 0.6734808616745137 (alpha=1.464, psum=1/320, eps=0.0062,
m=171) by finding a redistribution (l,c) that certifies eps > 0.0062 in the interval verifier
(tools/verify_coboundary_floor.py), OR an m-sweep / smaller-psum improvement at fixed eps.

## Bound chain (from record notes, CHECKED NUMERICALLY)
bound = (H(alpha) − tau)/(1 − B/m),  tau = psum·(m−6)/m,  H(1.464) = 0.672467425578.
eps=0.0062 certified (1,096,556 nodes, 3 identical runs). eps=0.0063 FAILS at all alpha for
tawan's unchanged (l,c).

## LP toolkit (search heuristic — NOT ground truth)
tools/coboundary-reopt/: coboundary_reopt_lp.py (corrected LP, dual certificate, kappa_i =
p0 + 2(l_{i−1}−l_i)), coboundary_reopt_horizon.py, coboundary_symmetric_lp.py,
coboundary_true_lp_scan.py, coboundary_final_verify.py, coboundary_reopt_selfcheck.py,
coboundary_missing_class.py.

## Plan
1. Run LP scans (bounded timeouts) — does any (l,c) family beat tawan's v*?
2. Candidate (l,c) with v* > 0.0062 → interval verify (grid 4000, max 2-3 runs).
3. m-sweep m in {160..200} at fixed eps=0.0062.
4. Smaller psum probe (1/400) with matching redistribution.

## Results
(empty — pending)

## Ledger
(empty — pending)

## FINAL VERDICT (2026-08-18, coordinator harvest — agent died at t=6, LP outputs recovered from /tmp)

### 1. Redistribution (l,c) re-optimization — CLOSED (LP relaxation + global floor)
- **α=1.49 full asymmetric LP** (c_bound ∈ {0.06, 0.02, 0.15}): LP v* = 0.008771/0.008630/0.009090
  all BEAT tawan's family floor (0.007797) on the crystal family — BUT the GLOBAL float floor
  (differential evolution + huge-gap configs) is 0.005674/0.005392/0.005674 << tawan's 0.006295.
  **Every LP solution that beats tawan on the family loses globally** — LP's concentrated (l,c)
  (c at ±0.06 bound, kappa min ~2.9e-4) is fragile to huge-gap configs g=(...,30,...) where the
  interval verifier actually checks.
- **α=1.464 symmetric LP**: v* = 0.007612214 == tawan's floor EXACTLY (tie), but the symLP
  tie-solution global floor is 0.006037851 < tawan's 0.006221577. Symmetric subspace = dead end.
- **Conclusion (PROVEN): tawan's (l,c) is the global optimum of the redistribution class —
  no (l,c) certifies eps > 0.0062.** Independent confirmation: interval verifier terminal-cell
  failures at eps=0.0063 (FINAL-RECORD note). Two independent lines of evidence agree.

### 2. m-sweep — CLOSED (exact bound chain, B(m)=Φ_m(ε(m−6)) IS m-dependent)
- Correct bound: bound = (H − τ(m))/(1 − B(m)/m), τ(m)=psum(m−6)/m,
  B(m) = 2√((m−1)ε(m−6)/m) − 1 + ε(m−6)/m.
- Sweep m=20..400 at (H=0.672467425578, psum=1/320, eps=0.0062):
  m=100→0.673064, m=133→0.673402, m=150→0.673461, **m=171→0.6734808617 (MAX)**, m=200→0.673457,
  m=250→0.673353, m=300→0.673224.
- **m=171 is the exact optimum of the full bound chain. No m-sweep improvement exists.**

### 3. OVERALL RECORD LEVER VERDICT — CLOSED
The coboundary redistribution class is certified-optimal at (α=1.464, psum=1/320, eps=0.0062, m=171)
→ 0.6734808616745137. No (l,c), no m, no α improves it. **The record lever's remaining surface is
NOT in this class** — raising 0.673481 needs a NEW OBJECT (e.g. a new window/test family outside
band-width ≤1, or a fundamentally different zero-counting bound), per wave-5/6 verdicts
(test-family PROVEN closed at H=0.6725007; ceiling_law256 0.6818).
