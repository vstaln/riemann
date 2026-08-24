# Resurrection sweep — 2026-08-24

Trigger: F_V-vs-F_T functional bug fixed (verifier now `span1_mode=replaced`) and the C21
optimizer corrected. Some ABANDONED/INCONCLUSIVE ledger entries may have died from the *bug or
its artifacts*, not from mathematics, and are resurrectable under the corrected objective.

## What today's fix actually changed (grounded, PROVEN)

Three independent lanes (ledger 2026-08-24, `dispute-*-2026-08-24.md`):
1. CODE [PROVEN]: `tools/verify_coboundary_floor.py` summed all 21 pairs (`w_uniform` line 498,
   no span filter) plus `q_i*w(g_i)` separately => implements **F_V**.
2. THEOREM [PROVEN]: Tawan local-to-global needs **F_T**: `q_i` REPLACE span-one, spans r=j-i>=2
   only (`kSpanRationals[1]=0`, loop span=2..6 in Tawan's `verify_coboundary.cpp`).
3. IDENTITY [CHECKED NUMERICALLY mpmath 60dps]: `F_V - F_T = (1/3)*sum_i w(g_i)`
   (`0.000362273873459031` both evals at witness). F_V >= F_T strictly on domain interior =>
   **no F_T bound follows from any F_V certificate.**

Consequences that matter for resurrection:
- Retired ALL coboundary-floor N0/N records certified through the F_V code path (last:
  N0/N >= 0.6735471309049393, 2026-08-23, m=136). Honest F_T restart base banked:
  **eps=0.0070 verified=true at only 779,030 nodes => N0/N >= 0.67296645387858 (m=151).**
- The C21 optimizer `joint_c21.py` also maximized the wrong objective (PAIRS21, all 21 pairs).
  Round-1 theta is now only a *starting point*; round-2 (`joint_c21_ft.py`/`c21_ft_opt.py`)
  optimizes F_T and was launched in flight.
- **Cost cliff**: F_T certifies ~100x cheaper (779,030 nodes vs 60M+400M for F_V eps=0.0070).
  Every compute-limited F_V certification path is now dramatically cheaper — this is the main
  reopen mechanism unlocked by the bug.

## Scope & honesty note

ledger.md holds 16 `ABANDONED` + 41 `INCONCLUSIVE` occurrences (~25 distinct top-level bullets).
The direct-RH attempt lane (LSE/prime-zeta/theta-semigroup/mellin/operator/transfer/lee-yang/k<1/
GS-diagonal) died on PROVEN mathematical or firewall obstacles **independent of the F_V/F_T
functional**; those are not reopened by today's fix. Only the *coboundary-floor / N0-N / verifier*
line is bug-touched. Entries below are the ones I could classify from grep + targeted reads; the
~56 figure includes sub-bullets not individually re-screened here.

## Classification table

| Entry (ledger loc) | One-line claim | Death cause class | What changed today | Reopen cost | Expected gain if reopened |
|---|---|---|---|---|---|
| prior record-point ladder: eps=0.00700 INCONCLUSIVE at 60M+400M nodes (L2121) | N0/N floor below 0.67354 could not be certified within node budget | **BUG-DEPENDENT** (+ COMPUTE-LIMITED-THEN) | Old objective F_V was wrong AND ~100x costlier; F_T cert laps it: eps=0.0070 verified at 779,030 nodes | FREE — already effectively resolved as the banked F_T restart base | Restore a SOUND N0/N floor under the correct objective (0.67296645) and climb the ladder |
| 2026-08-23 record on round-1 (wrong-objective) C21 theta (L2026-08-23 section) | N0/N >= 0.6735471 | **PRE-C21-OBJECTIVE** (optimizer maximized F_V) | Round-2 F_T optimizer now running; round-1 theta usable only as seed | Med: wait for round-2 theta, then ladder | True F_T ceiling likely ABOVE the F_T restart base; possibly re-approaches 0.6735 |
| verifier-rs INCONCLUSIVE, no convex-tangent prune, NOT-FOR-CERTIFICATION (L486) | Rust certifier can't reproduce speed / not independent | **COMPUTE-LIMITED-THEN** (missing tangent_lower prune; orthogonal to today's span fix) | F_T functional is far cheaper, so a correct Rust certifier targeting F_T is high-value | High: port `tangent_lower` (2nd-deriv table via rug, LDL pivot) AND add span1_mode=F_T | Independent fast certifier for the whole F_T ladder; de-risk single-Python-verifier |
| torus E[m₂]=2.480620 definition INCONCLUSIVE, cheap (L213) | marked-family m₂ convention unresolved | **COMPUTE-LIMITED-THEN** (never computed) | unrelated to F_V/F_T; still cheap | Low (minutes-scale compute) | Narrows the 0.6818 marked-ceiling interpretation (0.6818 itself UNAFFECTED by bug) |
| 256-law exact marked S₃ INCONCLUSIVE (config private) (L159/200) | exact S₃ at 256-law config | **UNCLEAR** (config not recovered) | none relevant | Med: recover private config | Second independent lever on the 0.6818 ceiling |
| direct-rh-nonclassical-domains INCONCLUSIVE (L18) | no candidate in screened domains | **UNCLEAR** | none relevant | Low (rescreen) | unlikely; screened family has no closure proof |
| lee-yang / theta-semigroup / fullcomplex / transfer / mellin / operator-polya / k<1 / GS-diagonal / wave-22/23/26 / wave-30 / N=700 / entire-growth / gaussian-perron | various direct-RH one-way conditions | **GENUINE-WALL** (PROVEN symmetry collapse / mechanism trichotomy / firewall / refuted) | nothing — obstacles independent of the coboundary floor | re-run forbidden by ledger ("do NOT re-run"/"closed") | None — mathematics, not bug |
| finitet P5 tower probe INCONCLUSIVE (crash) (L58) | tower probe | **COMPUTE-LIMITED-THEN** but *separate* bug (mpc-vs-int, not the span bug) | not today's fix; separate probe code bug | Low: fix mpc↔int, rerun | Finite-T λ_positivity data only; not the record line |

## Counts per class (classified entries)

- **BUG-DEPENDENT: 1** (eps=0.00700 ladder INCONCLUSIVE — the direct victim; plus the retired
  F_V N0/N records themselves, not ledger ABANDONED entries)
- **PRE-C21-OBJECTIVE: 1** (2026-08-23 record on the round-1 wrong-objective optimum)
- **COMPUTE-LIMITED-THEN: 3** (verifier-rs, torus E[m₂], finitet-P5 [separate bug])
- **GENUINE-WALL: ~15** (all direct-RH one-way-condition closures; not reopened)
- **UNCLEAR: 2** (256-law exact S₃, nonclassical-domains)

## Top-3 recommended resurrections

1. **Resurrect the N0/N coboundary-floor ladder under F_T** — the 2026-08-24 restart base
   (eps=0.0070, N0/N >= 0.67296645387858) is already banked; climb the eps ladder (0.0071, 0.0075,
   0.0079...) with `VERIFY_SPAN1_MODE=replaced` now that each rung costs ~100x less than the old
   F_V path (which never got past INCONCLUSIVE at 60M+400M nodes). First step: run the F_T ladder
   at 0.0075/0.0079 at the round-2 F_T theta once it lands; log `VERIFY_RESULT` verbatim and route
   through the headline chain before any public N0/N number.

2. **Resurrect the C21 round-1 result as a *seed*, and land round-2 (F_T) optimization to
   completion** — round-1's "record" was on the wrong objective and is retired; the corrected
   `joint_c21_ft.py`/`c21_ft_opt.py` run (in flight, ~50 min) yields the first genuinely F_T-optimal
   theta. First step: when the run exits, certify its eps/bound via the independent Arb verifier
   (NOT the optimizer — it certifies nothing), then feed the winner into the ladder above.

3. **Resurrect the Rust verifier (`verifier-rs`) as the F_T fast-certifier** — its INCONCLUSIVE
   status is orthogonal to the span bug (missing `tangent_lower` convex prune), but the F_T
   functional makes a correct Rust certifier both cheaper and more valuable: an independent,
   fast certifier for the whole ladder removes single-Python-cerifier risk. First step: port
   `tangent_lower` (w-table, LDL pivot >= 1e-9, `tl = value - sum|grad_i|*radius_i`) and add the
   span1_mode=F_T exclusion, then benchmark against Python's 779,030-node 0.0070 cert.

Reopen rationale shared by all three: they died on compute cost or a wrong objective, not on a
proven mathematical wall; the F_V->F_T correction removes the wrong objective and orders-of-magnitude
the cost of the correct one.
```
