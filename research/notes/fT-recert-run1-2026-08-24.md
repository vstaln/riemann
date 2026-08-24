# F_T recertification — run 1 (2026-08-24)

## Context
Recovery step 1 after the retirement of the previous (F_V-based) record.
`tools/verify_coboundary_floor.py` certifies **F_V** over all 21 pair spans
(r = 1..6 plus the q_i·w(g_i) nearest term). Tawan's theorem needs **F_T**:
the pair sum restricted to **r >= 2** (span-one pairs are dropped), with the
q_i term replacing the span-one contribution.

## What was patched (minimal, backward-compatible)
`tools/verify_coboundary_floor.py`, env-var parameterized branch of `main()`:

- Added `mode = os.environ.get("VERIFY_SPAN1_MODE", "added")`
  ("added" = current behavior, default; "replaced" = Tawan F_T).
- In `"replaced"` mode, `w_uniform` excludes span-one pairs:
  `w_uniform = {(i,j): v for (i,j),v in w_uniform.items() if j-i >= 2}`
- One echo before the run: `print(f"span1_mode={mode}")` so logs are
  self-describing.

Diff summary: **1 file, 4 insertions, 0 deletions.** Nothing else touched,
no refactor. Verified `AST_OK`.

## Why target eps = 0.0070
The expected F_T range is *below* this value, so a fresh banked honest floor
of 0.0070 should hold and verify cleanly on this first run. Later ladder runs
can climb toward the true F_T ceiling.

## Run config (run 1)
```
VERIFY_ALPHA=1.4263026187858052 VERIFY_TARGET=0.0070 VERIFY_GRID=4000
VERIFY_MAX_NODES=28000000 VERIFY_LAMBDA=1.351623997475116
VERIFY_P1..P6 = 895.6 1151.7 952.6 952.6 1151.7 895.6
VERIFY_Q1..Q6 = 0.331829 0.323062 0.343351 0.343351 0.323062 0.331829
VERIFY_SPAN1_MODE=replaced
timeout 3000 (i.e. ~50 min hard cap)
```
Log: `tmplogs/cert_F_T_700.log`

## Expected wall-clock
~1–3 h at 4000 grid / 28M node cap. The run was launched with a 3000 s
`timeout`, so on this first attempt it may either **verify** well before the
cap or hit the timeout having pruned only part of the band.

## Claim discipline (IMPORTANT — read before reporting any number)
If `verified=true`, the honest interim floor claim is **only** that F_T >= 0.0070
under Tawan's theorem setup. The headline **N0/N bound must be RECOMPUTED via
the headline chain** before any public number is stated. We do **not** compute
the N bound here; this run backs only the raw F_T floor. Log the `VERIFY_RESULT`
line verbatim and treat the N0/N value as NOT derivable from this run alone.

## Round 3 (mass-2 exact) — 2026-08-24

Changed `unpack()` in `joint_c21_ft2.py`: q normalization switched from
`qq/qq.sum()*2*lam` (mass = 2*lam) to exact mass-2 `qq*(2.0/qq.sum())`, so
Sigma q = 2 exactly regardless of lam, per the ledger 2026-08-24 final entry —
coboundary telescoping requires the exact mass condition (mirror triples
u+v+w=1 in exact rationals ideally; float renormalization acceptable for
surrogate search since certification re-runs separately). p scaling is untouched
(lam/320 still taxed through tau). Ran `c21_ft_opt2.py` (warm-started from
best_c21_theta.npy, 30 iterations, import from joint_c21_ft2) -> log
`tools/direction2_sdp/c21_mass2_round3.log` (PID 29085). Label CONJECTURED-license:
surrogate only; Arb certification is the arbiter.
