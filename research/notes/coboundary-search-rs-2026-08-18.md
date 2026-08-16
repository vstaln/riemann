# coboundary_search — Rust port of the redistribution LP + DE global floor

Date: 2026-08-18. Agent: builder. Status: DONE (acceptance met).

**Context.** The coboundary-redistribution lever (l,c) is PROVEN CLOSED (see
ledger). This work preserves its methodology in fast, scipy-free form so future
record-object hunts can re-run the search in seconds. Nothing here re-opens the
lever and nothing here certifies anything — the tool is a search heuristic; the
interval verifier (tools/verify_coboundary_floor.py) is the ground truth.

## What was ported

`tools/coboundary_search/` (new crate, pure Rust, zero C deps):

- `k_alpha`, `w_alpha`, `F0`, `lin_coeffs`, `F_B(g; l,c)`, `kappa_i = P0 + l_{i-1} - l_i`
  — exact port of `tools/coboundary-reopt/coboundary_reopt_lp.py` (221 L) and
  `coboundary_symmetric_lp.py` (241 L). Python originals untouched.
- **LP solver**: self-contained bounded-variable two-phase simplex
  (`bounded_simplex`, ~90 lines). HiGHS-via-good_lp was the first choice but the
  build is blocked on this machine (no cmake, no libclang for bindgen, no sudo,
  pip disabled). The simplex is validated directly against scipy/HiGHS reference
  values (below) — v* matches to all 9 printed digits.
- **Constraint families**: byte-identical to the Python (incl. numpy
  `default_rng(12345)` intermediate samples). Dumped once by
  `scripts/dump_cfgs.py` into `data/family_578.txt` (sym LP) and
  `data/family_1089.txt` (full LP: crystal3(5)=125 + huge_gap 18 +
  intermediate(500) which is 500+250 mixed-range = 750). Families are
  alpha-independent.
- **Global float floor**: DE (best/1/bin, popsize 20·6=120, maxiter 400,
  dither F∈(0.5,1), CR=0.7, SplitMix64 seed 3) over [0.4,3.5]^6 + Nelder-Mead
  polish (bounded), plus the huge-gap scan (g_pos = H ∈ linspace(5,21,9), 6 NM
  restarts from base [1.05,1.98]×3 + all-1.1 background), matching
  `global_floor`/`refine_floor` in the Python.

## Acceptance table (Python vs Rust)

Reference Python values from `scripts/ref_lp.py` (scipy linprog 'highs', fast
LP only; DE global floors are the task-recorded wave values, scipy DE being
50-min-per-case).

| case | scipy v* | Rust v* | global floor recorded | Rust global floor | \|diff\| |
|---|---|---|---|---|---|
| sym, α=1.464 | 0.007612214 | **0.007612214** | 0.006037851 | 0.005519 | 5.2e-4 |
| sym, α=1.49 | 0.007797184 | **0.007797184** | — | 0.005635 | — |
| sym, α=√2 | 0.007322010 | **0.007322010** | — | 0.005305 | — |
| full, α=1.49, cb=0.06 | 0.008771241 | **0.008771241** | 0.005674 | 0.005576 | 1.0e-4 |
| full, α=1.49, cb=0.02 | 0.008629757 | **0.008629757** | 0.005392 | 0.005828 | 4.4e-4 |
| full, α=1.49, cb=0.15 | 0.009089580 | **0.009089580** | 0.005674 | 0.006011 | 3.4e-4 |

- **LP v*: exact match in all 6 cases (9 digits).** Full-LP (l,c) also match
  scipy exactly; kappa ≥ 0 and family floors = v* re-confirm feasibility/optimality.
- **Global float floor: within 5.2e-4 everywhere (tolerance ~1e-3).** Runtime
  ~0.5–0.7 s per case (LP ~15–100 ms) vs ~50 min for the Python DE (wave-13).

## Honest caveats (INCONCLUSIVE-grade items, by design)

1. **Symmetric LP is DEGENERATE at α=1.464.** My simplex lands on a different
   LP-optimal vertex than HiGHS: a2,b2 match scipy to 1e-12 but (a1,b1) differ
   (mine −4.8975e-4/−0.06, scipy +2.7037e-4/+0.06); v* identical, family floor
   identical. The global floor is therefore evaluated at my vertex, so the
   5.2e-4 gap vs the recorded 0.006037851 (scipy's vertex) mixes degenerate-vertex
   choice with DE stochasticity. Qualitatively both conclude symLP's global floor
   sits below tawan's (0.006222 recorded); conclusion unchanged.
2. **DE is stochastic.** On the full LP (where (l,c) match scipy exactly) the
   Rust DE still lands 1e-4–4.4e-4 away from the recorded scipy-DE values
   (0.005576/0.005828/0.006011 vs 0.005674/0.005392/0.005674). Different RNGs,
   different local minima found; well inside tolerance, honestly reported.
3. Two bugs were found and fixed during the port (worth recording for future
   Rust ports of scipy optimizers):
   - unconstrained NM polish escapes to the unphysical g→−∞ direction where
     F_B is unbounded below (P0·Σg term) → −1.86e304 garbage; fixed by bounding
     NM to the verifier's active domain [0.4,21] (scipy's DE polish uses bounded
     L-BFGS-B — the Python was implicitly safe, the naive port was not);
   - unclamped DE trial (my fallback instead of scipy's bounds-clamping) let
     pop/best escape the box and drift exponentially (±1e50); fixed by
     `m.clamp(lo,hi)` as scipy does.

## Usage

```
cargo run --release -- --alpha 1.464 --mode sym [--c-bound 0.06]
cargo run --release -- --alpha 1.49  --mode full --c-bound 0.06
```

Prints v*, (l,c), kappa, family floor, DE-box floor, huge-gap floor, global floor.
SEARCH HEURISTIC ONLY — no certification claim.

## Files

- `src/main.rs` — everything (F_B math, simplex, DE, NM, huge-gap scan, CLI)
- `data/family_578.txt`, `data/family_1089.txt` — exact constraint families
- `scripts/dump_cfgs.py` — regenerates the data files (numpy only)
- `scripts/ref_lp.py` — scipy reference LP values for validation (scipy only)
