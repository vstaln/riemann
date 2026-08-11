# tools/regen_law — 256-law regeneration (EXECUTIONER, round 3+)

Attempt to independently regenerate the N=256 near-CUE law of marked configurations by re-solving its
defining LP (the ONE non-Lean link, EnclOK, in the 0.68185 bandwidth-one ceiling). Result: BLOCKED at
N=256 — the candidate configuration family is private (cert_N256_blk_b128m.json). See
`research/notes/regenerate-256law.md` for the full report and adjudication.

## Run
```
uv run --with scipy --with mpmath python3 <script>   # HiGHS via scipy.optimize.linprog; no pip
```

## Scripts
- `common.py` — **BROKEN** family generator (configs with Σ marks = N+d, NOT N; used by lp_smallN.py —
  produced the invalid small-N values later flagged). Do not reuse.
- `common2.py` — CORRECT generator (valid configs: s simples + d doubles, s+2d = N, s+d distinct positions).
- `final_numbers.py`, `adjudicate.py`..`adjudicate4.py`, `colgen8.py`, `check_cum8.py` — small-N
  adjudication (pointwise rows vs cumulative-only budget), bug fix verification, N=8 pool + column gen.
- `lp_*.py` — N=256 pointwise LP on structured families (all infeasible; Chebyshev diagnostics at the end).
- `search_defects.py`, `ramp_search.py`, `kernel_probe.py`, `gkernel.py` — structure probes.
- `cert_allconfigs.py`, `cert_allconfigs2.py` — certificate LP valid against sampled configs.

## Key numbers (see the report)
- Pointwise rows, valid configs: min p₁ = 0.705/0.753/0.844/0.915 at N = 8/16/32/64 (upper bounds).
- Cumulative-only budget: min p₁ = 0.669–0.687 at N=8 (below Theorem B's 0.6725 — MB2.4 nuance, not a
  refutation), rising to 0.914 at N=256.
- N=256 pointwise LP: infeasible for every family tested (the exact-CUE ramp is not in any convex hull
  I could construct).
