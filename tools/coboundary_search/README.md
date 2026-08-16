# coboundary_search

Rust port of the **coboundary-redistribution max-min LP + global float-floor
search** (Python originals: `../coboundary-reopt/coboundary_reopt_lp.py`,
`coboundary_symmetric_lp.py`). Pure Rust — no scipy, no numpy, no C deps.

> **SEARCH HEURISTIC ONLY.** This tool certifies nothing. Certification is the
> job of the interval verifier (`tools/verify_coboundary_floor.py`). The
> redistribution lever itself is PROVEN CLOSED (see
> `research/notes/ledger.md`); this crate preserves the methodology in fast
> form for future record-object hunts.

## What it does

Maximizes `v` over the coboundary redistribution `(l, c)` such that

```
F_B(g; l,c) = F0(g) + Σ_k l_k(g_{k+1}−g_k) + Σ_k c_k(w(g_{k+1})−w(g_k)) ≥ v
```

on a crystal-family + huge-gap + intermediate-grid constraint set, with the
exact huge-gap asymptotics `kappa_i = P0 + l_{i−1} − l_i ≥ 0`. Then it estimates
the *global* float floor of the winning `(l,c)` with a differential-evolution +
Nelder-Mead + huge-gap scan.

- `--mode sym`  — symmetric subspace LP (vars a1,a2,b1,b2,v), 578-config family
- `--mode full` — full LP (vars l1..l5,c1..c5,v), 1089-config family

## Build & run

```
cargo build --release
./target/release/coboundary_search --alpha 1.464 --mode sym
./target/release/coboundary_search --alpha 1.49 --mode full --c-bound 0.06
```

LP solves in ~15–100 ms; DE + huge-gap scan in ~0.5 s (vs ~50 min for the
scipy differential_evolution in wave-13).

## Architecture

- `src/main.rs` — `k_alpha`/`w_alpha`/`F0`/`F_B` math, bounded-variable
  two-phase simplex LP solver, DE (best/1/bin + bounded NM polish), huge-gap
  scan, CLI.
- `data/family_578.txt`, `data/family_1089.txt` — exact constraint families
  (byte-identical to the Python, incl. numpy `default_rng(12345)` samples;
  alpha-independent).
- `scripts/dump_cfgs.py` — regenerates the data files (numpy only).
- `scripts/ref_lp.py` — scipy/HiGHS reference LP values (validation only).

## Validation

LP `v*` matches scipy/HiGHS to all 9 printed digits at all tested
(α, mode, c_bound) combos; global float floors agree within ~5e-4 (DE is
stochastic). Full details + honest caveats:
`research/notes/coboundary-search-rs-2026-08-18.md`.

Gotcha recorded for future ports: `F_B` is unbounded below as all gaps → −∞
(the `P0·Σg` term), so any *unbounded* local optimizer (plain NM polish, and
DE mutants that are not clamped to bounds) escapes the verifier's active domain
[0.4, 21] and diverges. The Python was implicitly safe (scipy's DE polish is
bounded L-BFGS-B); the port must clamp both NM and DE trials explicitly.
