# verifier-rs fix attempt — 2026-08-18

**Overall verdict: INCONCLUSIVE — root cause identified and PROVEN; fix (port of the
convex-tangent prune) NOT completed within budget.** The Rust port is marked
NOT-FOR-CERTIFICATION in its header. The Python verifier remains ground truth.

## Root cause (PROVEN)

The Rust port `tools/verifier-rs/src/main.rs` hardcodes `use_tangent=false` and never
implements `tangent_lower` (the code literally says "second-derivative table: skip for
now (tangent bound needs it)"). Python's `verify_coboundary_floor.py` defaults to
`use_tangent=True` and its certified verdicts **depend on the convex-tangent prune**:

| config | Python (tangent on, this env) | tangent prunes |
|--------|------------------------------|----------------|
| ainta (MT, uniform, 19/5000) | True, 707,901 nodes (= certified count exactly) | 93,735 |
| tawan baseline (cos 1.47, 577/1e5) | True, 209,236 nodes (= certified count exactly) | 18,182 |

Control probes (Python, same unmodified file):
- `verify_floor(..., use_tangent=False)` on 0.00620 → **False**, terminal cell low=0.00619981 < 0.0062.
- `verify_floor(..., use_tangent=False)` on ainta → node-limit (fails).
- So without the tangent prune Python fails on the same configs the Rust port fails on.
  The Rust port's enclosure is NOT the problem; the missing prune mechanism is.

## Enclosure: NOT the bug (verified)

- DIAG of Rust's terminal cell (8066,8125,8042,8054,8125,4257) at 0.00620: term breakdown
  sums exactly to the reported low (Σp=0.00584964, q≈5.7e-5, pairs≈3.0e-4, total 0.0061999837).
- Probe of `sinc_iv`/`sinc_point`: `sinc_point(4.0754) = -0.19725` is CORRECT (4.0754 rad is
  in the third quadrant, sin=−0.8039); my initial hand-check had a sign error. `table[4257]`
  = 3.94e-6 matches true w(1.06425) = (K/K0)² with K=−0.00185; `table[8066]`=4.43e-5 matches
  true w(2.0165). Rust's `sinc_iv` (exact extrema at roots of x=tan x), box_lower, RangeMinimum
  all agree with Python's Arb-ball versions. The old header claim "TIGHTER than python-flint"
  is retracted (corrected in header).

## Second finding: current Python does NOT certify 0.00620 (contradicts cert note)

The 2026-08-13 note `research/notes/eps-boundary-exact.md` records 0.00620 True @ 1,096,556
nodes (3 identical runs) with max_nodes=25M. The **current** file + current python-flint env
reproduces ainta/tawan node counts exactly but fails 0.00620:
- 0.00620, tangent on, precision 128/256/512 → **False** at 5,192 nodes, terminal cell
  (8060,8125,8042,8048,8125,4254), low=0.006195950882593026 (4.05e-6 below target).
- A terminal cell is a definitive False (not node-exhaustion; the cap was never hit).
- Likely cause: python-flint/Arb version difference affecting the second-derivative table
  and/or tangent LDL — the certified run's env is not reproducible here. NOT resolved.

For 0.00621 all agree **False** (real violation: certified note proves true F=0.0059188 at
the Python terminal cell; Rust terminal low=0.00620986 < 0.00621).

## Before/after table (4 acceptance configs, grid=4000, max_nodes=5e6, no tangent)

| config | Python certified | Rust before (this run) | Rust after | 
|--------|------------------|------------------------|------------|
| 0.00620 @ α=1.464 coboundary | True (cert note; current env: False) | False, terminal low=0.0061999837 | NOT FIXED — see below |
| 0.00621 @ α=1.464 coboundary | False (real violation) | False, terminal low=0.00620986 | False (matches; likely stays) |
| ainta (MT, uniform, 19/5000) | True, 707,901 nodes | False, node-limit @5e6 | NOT FIXED — needs tangent |
| tawan baseline (cos 1.47, 577/1e5) | True, 209,236 nodes | False, terminal low=0.00576989 | NOT FIXED — needs tangent |

## Fix (documented, not completed — out of budget)

Port `tangent_lower` to Rust:
1. Second-derivative table: interval enclosure of w'' = 2(k1² + k·k2)/k0² per cell via
   rug enclosures of sinc/sinc'/sinc'' over the cell (need sin_iv/cos_iv with extrema at
   kπ/2; K' = π(sinc'(b) − sinc'(a))/2, K'' = π²(sinc''(a)+sinc''(b))/2).
2. LDL positive-definite check (f64 with a relative pivot margin ≥1e-9 is SOUND — never
   prunes wrongly; weaker than arb's exact LDL).
3. Tangent plane: value = Σp_i·mid_i + Σa_ij·w(mid_span) + Σq_i·w(mid_i), gradient terms
   with w'(·) enclosures at the midpoint (1-ulp interval), tl = value − Σ|grad_i|·radius_i,
   radius_i = (hi−lo+1)/(2·grid). Prune when tl ≥ target.
4. Also make `k0` a directed-rounding enclosure (currently midpoint f64 — minor rigor gap,
   numerically negligible at PREC=300).
Then re-run the 4 acceptance configs. ainta/tawan should pass; 0.00620 is expected to stay
False unless the environment reproduces the certified True (open question above).

## Files
- `tools/verifier-rs/src/main.rs` — cleaned (debug blocks removed), header corrected to
  NOT-FOR-CERTIFICATION, main() now runs all 4 acceptance configs.
- `tools/probe_no_tangent.py`, `tools/probe_precision.py` — Python control probes (kept).
- Runs: `/tmp/verifier-rs-run1.txt`, `/tmp/verifier-rs-all4.txt`, `/tmp/verifier-rs-diag.txt`.

## COORDINATOR CORRECTION (2026-08-18, after agent completion) — the "current env fails 0.00620" finding is a PROBE ARTIFACT, record fully reproduces

The agent's Second finding ("current Python does NOT certify 0.00620... env drift") is **WRONG —
caused by a bug in its own control probe** (`tools/probe_no_tangent.py` / `probe_precision.py`):
the probe builds the weight dict with `range(6)` instead of the certified `range(7)`:
`w = {(i,j): 2.0/(7-(j-i)) for i in range(6) for j in range(i+1,6)}` — dropping ALL pairs
involving point index 6, i.e. a DIFFERENT F_B function. Suspect-the-check-first rule applied.

Coordinator's own re-runs with the CORRECT `range(7)` weights, current file, current python-flint:
- eps=0.00620 @ α=1.464 coboundary: **verified: True, nodes=1,096,556, pruned_tangent=222,047
  (pruned_interval=326,263)** — EXACT match to the 2026-08-13 certified count (1,096,556) and the
  FINAL-RECORD claim. Record baseline CONFIRMED in current env.
- eps=0.00621: **False, nodes=519,206, terminal low=0.006198271** — EXACT match to certified 519,206.
- So the certified boundary (0.00620 True / 0.00621 False) is reproducible to the NODE in the
  current environment. The record certification is NOT environment-fragile.

REVISED standing of the Rust port fix: the root cause analysis (Rust hardcodes use_tangent=false,
never implements tangent_lower → Rust's enclosure matches Python's but it lacks the load-bearing
convex-tangent prune) STANDS and is correct. But the acceptance evidence is now:
- Rust (no tangent): 0.00620 False @ terminal low 0.0061999837 — expected, since Python WITHOUT
  tangent also fails 0.00620 (low 0.00619981).
- Fix path (port tangent_lower: 2nd-deriv table via rug, LDL pivot margin ≥1e-9, tangent plane
  value − Σ|grad_i|·radius_i, prune when tl ≥ target) is documented and remains the way to make
  the Rust verifier certify like Python. NOT completed (out of budget).
- k0 midpoint → directed-rounding enclosure: minor rigor gap, numerically negligible.
