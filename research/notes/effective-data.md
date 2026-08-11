# Effective data: verified-zeros floor for the V20 hybrid bound

**Date:** 2026-08-11 (round 2.5). **Agent:** effective-data (42896a01), recovered post-guard by the orchestrator.
**Status:** the index.db analysis and floor extraction were completed by the agent before the late-night guard
paused it; this note records the established numbers and the honest caveats. The bridge fetches (exact counts
above each block floor) were interrupted by the guard + LMFDB rate limiting; the floors below are block-start
lower bounds (exact verified counts of zeros below each block start), with the true counts bracketed.

## Data availability

1. **`~/Downloads/index.db` (1.3 GB SQLite)** — a *sparse index* of the LMFDB riemann-zeta-zeros data:
   14,589,999 rows, one per 2100-height block, each `(t = block-start height, N = exact verified count of zeros
   below t)`. Covers all **103.8B LMFDB-verified zeros**; max row N = 103,800,780,903 at t = 30,610,043,900
   (LMFDB's documented total: 103,800,788,359 — the block-start count is below by the partial-block count).
   The `.dat` payload files (actual ordinates) are **not** local.
2. **`tools/data/zeros_lmfdb_large.txt`** — 11,000 exact 34-digit LMFDB zeros cached via the REST endpoint
   (index 1..11000, up to γ ≈ 2.8·10⁵). The REST endpoint is live but rate-limited to ~10 req/min (captcha
   after bursts).
3. **`tools/data/zeros_computed_10000.txt`** — our own 10k zeros (computed, γ₁₀₀₀₀ = 9879.04), precision
   ~2.9e-6 at i=1000.

## Verified floors from index.db (semantics verified against N(T): t=5000 → N=4520 ✓, t=7100 → N=6814 ✓)

| T (height) | N₀ ≥ (verified zeros below block start) | Exact count bracket |
|---|---|---|
| 10⁵ | **137,299** (block start 99,500) | ≈ 138,0xx (partial block above) |
| 10⁶ | **1,743,904** (block start 998,300) | ≈ 1,74x,xxx |
| 10⁷ | **21,133,625** (block start 9,998,900) | ≈ 21,1xx,xxx |
| max | **103,800,780,903** at t = 3.061×10¹⁰ | 103,800,788,359 documented total |

All LMFDB zeros are **numerically verified on the critical line** (the database only stores verified critical-line
ordinates) — so these are exact empirical floors for N₀(T), the number of zeros on the line below T.

## Bridge method (documented, for the V20 agent)

To make each floor exact with only ~10 REST requests: the db floor is the verified count below the block start;
fetch only the ~800 / ~2,700 / ~2,500 zeros in the partial block above each floor (the LMFDB REST endpoint
serves exact ordinates in chunks ≤ 1000 with ≥ 0.35s delay; observed sustainable rate ~10 req/min) and add the
count below T from the fetched chunk. This avoids a ~25-min contiguous fetch.

## Caveat (honest label)

These floors are **empirically verified on the line**, not PROVEN. They feed the *effective* statement
N₀(T) ≥ N₀_verified(T) + (certificate on (T, 2T)) — the V20 agent's hybrid bound — where the floor is clearly
labeled as an empirical floor used in an explicit finite-T statement, not as a theorem. The asymptotic liminf
constant is unaffected.

## Files

- `tools/data/zeros_lmfdb_large.txt` — 11,000 exact LMFDB zeros (cached)
- `~/Downloads/index.db` — the sparse index (1.3 GB, local)
- This note: `research/notes/effective-data.md`
