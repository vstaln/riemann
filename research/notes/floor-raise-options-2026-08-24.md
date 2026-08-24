# Floor-raise options — ranked strategy (2026-08-24)

**Status of this note:** analysis / strategy ranking (CONJECTURED costs and gains; every
claim labeled). Author: architect subagent. Does NOT change the certified record.

## Ground truth (what I read)
- **Sound record [PROVEN]** (ledger line ~2118, 2026-08-23): N0(T)/N(T) >= 0.6735471309049393
  (m=136) from C21-corrected joint max-min candidate: alpha=1.4263026187858052,
  lam=1.351623997475116, raw_p=[895.6,1151.7,952.6,952.6,1151.7,895.6],
  raw_q=[0.331829,0.323062,0.343351,0.343351,0.323062,0.331829]; grid 4000; eps=0.0079
  verified=true, 27,679,928 nodes, pruned_interval 13.84M, tangent 203. In-class dual ceiling
  0.68182868746 (far above; mechanism cannot break it). Ledger: true inf of F at this point
  in [0.0079, 0.0080).
- **Ladder failures (current params):**
  - eps=0.00800: FAILED, 273,607,405 nodes, unresolved terminal cell
    ((4209,4209),(7995,7995),(7989,7989),(4187,4187),(7944,7944),(4204,4204)) low=0.007999803... < 0.008.
  - eps=0.00805: FAILED, 225,760,131 nodes, unresolved terminal cell low=0.00804994 < 0.00805.
  - eps=0.00820: FAILED, 13,963,426 nodes, low=0.00819944 < 0.00820.
  - cert_790 (0.00790) = the record success; cert_795 (0.00795) log is only 515 bytes (no
    VERIFY_RESULT line) -> inconclusive / in-flight, not banked (VERIFY before trusting).
- **Hardware: AMD Ryzen 5 3500U, 8 threads (laptop APU, slow).** No explicit wall-clock line in
  logs; from mtimes and node counts I estimate the verifier processes roughly ~1e4 nodes/s
  (273M nodes ~ many hours). A ~2h+ cert run for ~27M nodes, 4-8h+ for 200-270M-node deep runs.
  Calibrate this empirically before committing multi-day runs.
- **epsmax-tight.md [CHECKED NUMERICALLY]:** the single-cosine record config was PROVEN at a
  tight boundary (8065 verifies / 8067 fails, a ~2e-6 band). This is the best precedent for
  reading the 0.00800 failure as a genuine true-minimum wall, not interval looseness.

## Why the current ladder is (almost) dead on the current params
The 0.00800 failure dies at a SINGLE collapsed cell (all 6 coordinates equal -> essentially a
1/4000-wide box) whose interval lower bound low=0.0079998 < 0.008. With sound interval
arithmetic, that reads as: the true inf of F is <= 0.0079998. Refining / subdividing cannot
push a certification above the true minimum. Combined with the epsmax-tight precedent, I judge
CONJECTURED (high confidence) that eps>0.0080 is NOT certifiable with the current param set.
Therefore finishing the ladder ABOVE ~0.0079998 buys at most the tiny eps=0.0079 -> ~0.00799
tail (~+7e-6 bound, see rate below) at the cost of multi-hour/day deep runs that have already
failed 3+ times. Low ROI as a standalone move.

Empirical bound-per-eps rate (from ledger, two sound points):
eps 0.00689 -> 0.6734730 ; eps 0.0079 -> 0.6735471. => ~+7.3e-5 bound per +0.001 eps
(CHECKED NUMERICALLY, 2 points). Use for all gain estimates.

---

## Ranked move table

| # | Move | Expected gain (honest) | Compute cost / wall-clock (this 3500U) | What kills it | Dep on dispute verdict |
|---|------|------------------------|----------------------------------------|---------------|------------------------|
| 1 | **More C21-objective optimizer rounds, calibrated to the Rust verifier** (round 1 = first correct-objective run ever gave the record; run random-perturbation walk with new seeds/scales + certify top 1-2 winners) | +1e-5 .. +1e-4 bound (needs finding eps +0.0002..+0.0014 above 0.0079; plausible since correct-objective search is <1 round old) CONJECTURED | Python search ~1-4h per round (120 iters x min_FB: DE 180iter*20pop + multi-start Nelder-Mead); then 1-2 cert runs at ~27M nodes ~2-6h each. Total per round ~4-16h. | Surrogate-vs-verifier slack is small; search stuck in local max; dispute kills objective | **HIGH** — if functional is wrong, every optimized theta targets the wrong objective |
| 2 | **Exploit surrogate-vs-verifier discrepancy (cheap probe):** run the Rust verifier on ~5-10 optimizer candidates; if true arb-eps > surrogate eps for any, re-optimize targeting the verified eps directly | +1e-6 .. +5e-5 (free bound from systematic under-estimate) CONJECTURED; cheap to test | ~5-10 short verifier runs (only need resolution near candidate min, can cap nodes) ~30min-2h | Surrogate already faithful; candidates are near-degenerate | **HIGH** (same objective dependency) |
| 3 | **Bank the near-boundary tail cheaply:** certify eps=0.00798/0.00799 at the record params (true inf is in [0.0079,0.0079998); certifying the highest low-rung that does NOT dive to the boundary cell could be cheap) | +2e-6 .. +7e-6 bound (eps +0.00008..+0.00009) CONJECTURED | 1-3 short runs ~1-4h each; stop early if it hits the boundary wall. Cheapest direct certified gain available. | 0.00798 already hits the boundary and burns hours | **HIGH** (depends on record params being sound) |
| 4 | **Interval-arithmetic tightening for near-boundary terminal cells** (higher-precision Arb / directed rounding on tangent-lower-bound / tighter second-derivative tables) so cells like low=0.0079998 resolve at higher eps WITHOUT brute subdivision | +1e-6 .. +1e-5 CONJECTURED; pure verifier improvement, reusable | implementation 2-6h + re-cert of arm; cheap to test on one pathological cell | True min genuinely below target (likely) -> tightening only helps if current bound is loose | **MEDIUM** (reuse; but budget LOW until dispute resolved) |
| 5 | **Parameter-space: larger m / more pairs / psum & kernel-family sweeps** (historical: single-cosine EXHAUSTED after normalization fix; 6-window family is early-stage at ~0.0079; psum=1/220 was optimal for single-cosine) | +1e-5 .. +1e-4 but long-horizon; higher variance CONJECTURED | Each new family needs a re-cert pipeline; screens are many cheap Python certs + 1-2 Rust certs ~5-20h per family | Dimension blow-up; runtime scales badly on 8-thread APU | **HIGH** (any kernel/pressure change must match the correct functional) |
| 6 | **My own certification idea (structural, independent of params):** warm reusable "definite(pressure, interval, tangent)" resolution with **materialized prune statistics** so a failed deep ladder run can be RESUMED at its unresolved cell(s) instead of restarting from 0 nodes — every 4-8h failed run becomes a checkpointed frontier. Pairs with (4): attack only the boundary cell with higher precision. | saves 4-8h per failed rung; converts some failures to wins; enables (3) CONJECTURED | verifier checkpoint/resume: 3-8h to implement; no extra node cost | checkpoint serialization overhead; deep run still truly below target | LOW (verifier-internal) — safest to start now |

---

## Required coverage answers
1. **What blocks 0.00800/0.00805 and can finer grid/targeted subdivision crack it in <=30min?**
   Blocks: a single near-point cell with interval low just below target (0.0079998 vs 0.008).
   CONJECTURED: this is the true minimum wall (see epsmax-tight precedent), so subdivision
   will NOT crack it; 0.008+ is off the table for these params. 30 min is far too short anyway
   — these runs cost 4-8h at ~1e4 nodes/s even before reaching the wall. Do NOT spend a day
   re-running 0.008 with only "finer grid." Real fix is (1)/(2): find params with higher true inf.
2. **More C21-optimizer rounds, cost, script ready?** Yes: `tools/direction2_sdp/c21_opt.py`
   is a ready 120-iteration random-perturbation walk (objective + bound in
   `tools/direction2_sdp/joint_c21.py`). Round 1 gave the record. More rounds = tweak
   seeds/scales/iterations and certify top wins. Python-only cost 1-4h/round; cert cost 2-6h/win.
   This is the highest-leverage move because correct-objective search is <1 round old.
3. **Parameter-space eps/hour:** historical winner is NOT brute ladder but canonical-objective
   + param optimization (this record). Single-cosine exhausted; 6-window young. Larger m raises
   the bound formula but inflates nodes; psum=1/220 (single-cosine optimum) is the reference.
4. **Different certification idea:** (6) resume-from-checkpoint + (4) high-precision boundary
   resolution; the cheapest independent of the dispute verdict.

## Honesty / status labels
- Record number, ladder failures, params: PROVEN / read from logs & ledger.
- eps->bound rate ~7.3e-5 per 0.001: CHECKED NUMERICALLY (2 sound points).
- "0.008+ not certifiable on current params" (true-minimum wall): CONJECTURED (high) — would be
  PROVEN only by a tight epsmax experiment on the 6-window functional (cheap, recommended).
- Wall-clock estimates: CONJECTURED (no timing lines in logs; calibrate node/s first).
- Dispute verdict: UNRESOLVED. If external audit is right that span-one terms are ADDED not
  REPLACED vs Tawan's theorem, the record objective is wrong and moves 1,2,3,5 target a dead
  functional; moves 4,6 (verifier internals) remain reusable but must be re-validated.
