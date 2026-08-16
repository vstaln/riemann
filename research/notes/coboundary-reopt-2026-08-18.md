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
