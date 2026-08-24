# verifier-rs completion — 2026-08-24

Goal: finish the independent Rust certification pipeline `tools/verifier-rs/` so it can
soundly certify the coboundary floor for both F_V (span1 "added") and F_T ("replaced").

## Grounded findings (read before changing anything)

- Tangent prune was ALREADY present in committed code (`block.rs`), but via `ldl_positive`,
  which current Python (2026-08-21 soundness fix in `tools/verify_coboundary_floor.py`
  `tangent_lower`, Gershgorin comment) explicitly documents as INVALID
  ("M from entrywise lower bounds of w'' can be PD while true Hessian indefinite").
  -> REPLACED with the sound Gershgorin/Weyl certificate to mirror Python semantics.
- F_T vs F_V: F_V = all 21 pair spans + q_i·w(g_i); F_T drops span-one pairs (j-i==1),
  q_i replaces that span-one mass. Python env var VERIFY_SPAN1_MODE.
- Mass conditions are HARD (ledger 2026-08-24 final): |Σq − 2| < 1e-9 and span masses
  preserved (each present span has weight mass 2; Σq=2 replaces dropped span-one mass).

## Changes (verifier-rs/src)

Stage 1 (soundness):
- `CellBounds` + `cell_bounds`: added w'' UPPER bound (`second_upper`, outward-rounded).
- `build_derivative_tables_parallel` now also emits `second_upper_table`; new
  `second_upper_ranges` (RangeMaximum) stored in SearchCtx.
- Added `hessian_pd_gershgorin(ctx, box_)` — sound diagonal-dominance PD certificate:
  `min_i(H_ii^lo - sum_{j!=i}|H_ij|^up) > 0`, mirroring current Python `tangent_lower`.
- Replaced the invalid `ldl_positive`-gated matrix block in `tangent_lower_cell` and
  `tangent_lower_point` with the Gershgorin gate. `ldl_positive` retained only as
  #[allow(dead_code)] reference, explicitly marked NOT a sound PD certificate.

Stage 2 (span1 + mass): `build_weights(span1_mode)`, `assert_mass_conditions(q_coeff, mode)`
refuses to run unless |Σq−2|<1e-9 AND every present span keeps mass 2 (span1 dropped in
"replaced" mode is covered by Σq=2). `verify_one(...)` runs mass assert + echo + verify.

Stage 3 (self-describing): `print_params(...)` prints alpha, target, grid, max_nodes,
span1_mode, lambda, p_raw/q_raw and p_coeff/q_coeff verbatim, plus sum p / sum q, before
every candidate run. Env-driven mode (VERIFY_ALPHA/VERIFY_TARGET/VERIFY_LAMBDA/VERIFY_GRID/
VERIFY_MAX_NODES/VERIFY_SPAN1_MODE/VERIFY_P1..6/VERIFY_Q1..6) added — python-verifier
compatible driver, kills the launcher black hole.

Stage 4 (floor-pipeline): `cargo run --release -- floor-pipeline <alpha> <target>
<p1..p6> <q1..q6> [--spans added|replaced] [--grid N] [--max-nodes N] [--chain-m0 N]
[--chain-m1 N]` -> mass assert -> certify -> record-chain bound
(port of cert-floor-rs::joint_bound/record_chain, q=6, argmax m over [m0,m1]) ->
`PIPELINE_VERDICT: PASS/FAIL` + bound + full parameter echo. Legacy VRS_CASE A/B/C/D kept.

## Validation results (grid=4000, added if F_V, replaced if F_T)

- F_V tawan baseline (alpha=1.47, P=[946,1177,877,877,1177,946]/1920000,
  Q=[31343/100000,1/3,105971/300000 mirrored], target=0.00577):
  **verified=True, 660,298 nodes** (Python 209,236 — different enclosure widths, expected
  per README). CHAIN_BOUND = **0.6731929114731422** (argmax m=183) — reproduces tawan's
  committed 0.6731929114731423 to ~2e-16. Pass.
- F_T round-4 winner (alpha=1.4882098313790653,
  P=[941.4583151442252,1166.5023445678612,876.8280966942434,mirrored],
  Q=[0.31170755083614082,0.33384461187125924,0.35444783729259993,mirrored], target=0.0056):
  **verified=True, 4,601,264 nodes** (fast). CHAIN_BOUND = 0.67306445176945029 (m=188). Pass.
- floor-pipeline tawan: `PIPELINE_VERDICT: PASS` bound=0.67319291147314220.
- Mass assertion: a Q vector with Σq≈1.98 -> `MASS-FAIL: |sum q - 2| = 2.000e-2 > 1e-9;
  refusing to run` (exit 2). Works.

## Honest limitation: record case 0.00620 (out of mission scope)

The committed (invalid-LDL) version's 0.00620 reproduction (claimed 1,096,556 nodes) used
the UNSOUND certificate; I do not reproduce it. With the SOUND Gershgorin, the tangent
correctly refuses certification in the genuinely non-convex stretches of the band (true
w'' crosses zero: band cells[4000..9000] w''_lo ∈ [−0.68, +2.13]; the per-cell enclosure
is tight, e.g. cell[3701] w''_lo=2.8125..2.8235, so enclosure width is not the issue).
0.00620 therefore needs deep subdivision into convex stretches and does NOT certify within
5,000,000 nodes here (node-limit; pruned_tangent=0 throughout). The mission validation
targets (tawan 0.00577, F_T 0.0056) certify soundly via the interval prune and do NOT
depend on the tangent (VRS_NO_TANGENT=1 gives the identical node count). This is a sound
limitation, not an overclaim.

## Build
`cargo build --release` clean (musl also available: RUSTFLAGS="-C linker=rust-lld -C
link-self-contained=yes" cargo build --release --target x86_64-unknown-linux-musl).
