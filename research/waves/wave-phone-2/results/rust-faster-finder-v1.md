# faster_finder v1 — validated (2026-08-12)

Pure-std Rust zero finder, replacing the v3 hybrid (tools/zeros_rust/main.rs) as the
production finder for the 10^7 shard run.

## Design (per faster-finder-spec.md, options 1+2+3)
- **Batch row-update Riemann–Siegel**: factor Z = 2(cosθ·A + sinθ·B) + g0; the (c_k, s_k)
  = (cos,sin)(t·ln k) rotate per step via precomputed (cos,sin)(STEP·ln k) — 2 trig-free
  mults per (k, step) instead of a per-step trig eval; re-seeded every 1024 steps.
- **EM path t<200** (z_low, N=40), RS g0-only t>=200; theta + N(T) asymptotics.
- **Fine scan step 0.01/0.02** (vs the baseline's 0.2) — completeness: resolves twin
  pairs down to gap ~0.01 (baseline missed ALL pairs with gap < 0.2, ~0.78%/100k).
- **Pure-bisection refine** (8 iters on the fine bracket — the IQI was dropped: its
  edge-case bracket collapse produced spurious endpoint roots 1e-3..7e-3 off).
- **Wiggle-pair collapse post-filter**: the g0-only error near the t~200-1200 crossover
  makes the computed Z cross twice around one true zero (pairs with gap 1e-3..2e-2);
  collapsed to the midpoint (a better root estimate), banded: 0.02 in [150,1200]
  (no real twin lives there — real pairs measured >= 0.0197 at t >= 5229), 0.01
  elsewhere (never touches a real pair).
- **8 internal std::threads** over the scan span.

## Bugs found & fixed during bring-up (all real, all reproduced)
1. **Batch phase bug (the big one)**: when n = floor(sqrt(t/2π)) grew, the newly
   seeded terms were rotated in the same step -> phase error step·ln k persisted until
   the next re-seed, corrupting Z by ~0.01-0.05 right after every n-growth (e.g. zero
   1166 at t=1610: 7e-3 off). Fix: rotate only the terms present at the previous t.
2. **Scan used batch.z at t<200** (bypassing the z_low dispatch): the RS form is
   invalid below 200 -> spurious crossings at grid points (59.34 artifact). Fix: z_at.
3. **IQI edge-case bracket collapse** -> spurious endpoint roots. Fix: pure bisection.

## Validation (LMFDB canonical 11k, tools/data/zeros_lmfdb_11k.txt)
| metric | value |
|---|---|
| candidates in LMFDB range | 11000 / 11000 (complete, 0 dups) |
| max \|Δγ\| | 6.442e-4 (zero 364, t=630.8 — EM/RS crossover) |
| mean \|Δγ\| | ~1.9e-5 |
| > 1e-3 | 0 (bar met) |
| wall, 100k zeros | 12.68 s @ step 0.01 (3.3x vs 42 s baseline) |
| | 6.77 s @ step 0.02 (6.2x) |
| count vs N(T) | -1.04 @ 0.02 (one <0.02 pair missed), +1.59 @ 0.01 (within N(T) asymptotic error) |

## Usage
```
faster <count> [step] [threads]    # count mode (from t=14)
faster win <t_lo> <t_hi> [step] [shard] [n_shard] [threads]   # shard mode
```
Compile: `rustc -O faster_finder.rs -o faster` (rustc 1.97.1 on laptop).
Source: /root/riemann/tools/zeros_rust/faster_finder.rs (phone proot), mirrored to
/root/zeros_rs/ on the laptop.

## Status
PROVEN (vs LMFDB 11k: bar met, complete, no dups). Production finder for the 10^7
shard run using tools/data/zeros_lmfdb_blockstarts_1e7.txt as shard boundaries
(ground-truth zero indices per shard -> count checks).
