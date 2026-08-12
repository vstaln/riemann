# TASK: BOX WORKER (oracle-new) — settle the N=8 cumulative dip (artifact or real?)

## Mission (brain directive — funded line: family-law / MB2.4)
The cumulative-only budget min p₁(8) was reported as **0.669–0.687, family-and-seed-dependent —
DIPPING BELOW Theorem-B's 0.6725**. If real, it's a genuine nuance ("the class ceiling is not an
N=256 phenomenon; small-N cumulative certificates are tighter"). If an artifact of the random
family sampling, it's noise. Your job: sweep families × seeds × family sizes and decide.

## Context (read first)
- `research/notes/regenerate-256law.md` §0–1 — the LP: cumulative budget |D(1)| ≤ d₁ = 0.82395317,
  |E(1)| ≤ 1/(6N²) + τ/(2N); objective min p₁ = Σ w_c s_c/N over marked-config families, Σ w_c = 1,
  w_c ≥ 0. Known: pointwise min p₁(8) = 0.705; cumulative dips to 0.669–0.687 (N=8, seed-dependent).
- `tools/regen_law/check_cum8.py` — the existing seed-stability pattern (nc × seed → min p₁(8)).
- `tools/regen_law/lp_smallN.py` — VALID family generator (s_c = N − 2d; common.py's gen_family_vec
  is the KNOWN BUGGY one — Σ marks = N+d — do NOT use it).
- If `tools/regen_law/` is absent from THIS box's ~/riemann, write a SELF-CONTAINED script
  (~50 lines: linprog, valid family gen, cumulative constraints) — the N=8 LP is tiny.

## The work (CHECKED NUMERICALLY)
1. Sweep: family seeds {0..20} × family sizes {200, 500, 1000, 2000} × jitter sets — compute
   cumulative-budget min p₁(8) for each. Report the DISTRIBUTION (min/median/max) and how often it
   lands below 0.6725.
2. Identify the BEST (lowest) config found: its marks (d doubles, positions) and its (D(1), E(1)).
   Is the dip robust (many seeds find < 0.6725) or a single lucky config (artifact)?
3. Also compute cumulative min p₁(16) and p₁(32) at the same seeds — does the dip disappear as N
   grows (monotone rise), consistent with the known 0.732/0.782 at N=16/32?
4. Write the verdict: is "cumulative min p₁(8) < 0.6725" REAL (robust across seeds) or ARTIFACT?

## Deliverable
`research/waves/wave-phone-2/results/box-n8dip.md` (+ script saved). Labels. Keep total < 30 min.
Crash-proof: write the file EARLY, append per result; bash < 90 s (nohup+poll LP sweeps).
