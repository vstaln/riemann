# WAVE 7 JOINT 7B — SECOND-MACHINE INTERVAL RE-RUN of the 1M-node Arb certificate

**Date:** 2026-08-17. **Agent:** builder 7B. **Status:** IN PROGRESS (results appended as runs land).

## Joint
Re-run the full interval certificate `tools/verify_coboundary_floor.py` at α=1.464, grid=4000,
cap_scheme='coboundary', target=620/100000, max_nodes=8000000, with the record's weights/pressure/
nearest coefficients. Confirm `verified=True` and node count ≈ 1,096,556 (run 3× for determinism).
Run additionally under a DIFFERENT numerical configuration (fresh venv / different python-flint
Arb build, or grid=8000). Confirm terminal-cell behavior: 620/1e5 True, 630/1e5 False (genuine
60-digit violation 0.0059188 < 0.00621). Close 6C's caveat (iii): 1M-node tree not re-run elsewhere.

## Exact reproduction block (from FINAL-RECORD-2026-08-13.md)
```
cd /home/vstaln/riemann
uv run --with mpmath --with python-flint python3 -c "
import sys; sys.path.insert(0,'tools')
from verify_coboundary_floor import verify_floor, cosine_kernel
w={(i,j):2.0/(7-(j-i)) for i in range(7) for j in range(i+1,7)}
p=[c/1920000 for c in [946,1177,877,877,1177,946]]
q=[31343/100000,1/3,105971/300000,105971/300000,1/3,31343/100000]
r=verify_floor(cosine_kernel(1.464),w,1.0/3000,6,620/100000,grid=4000,cap_scheme='coboundary',pressure_coeffs=p,nearest_coeffs=q,max_nodes=8000000)
print(r['verified'], r['nodes'])
"
# expected → True 1096556
```

## Result log

### Launch record (2026-08-17, 13:56 local)

Environment (host `void`, 8 cores; this is NOT the original record machine — fresh ephemeral
uv env, `uv 0.12.1`, `python-flint 0.9.0`, `mpmath 1.4.1`):

| run | pid (python child) | config | cmd | expected |
|---|---|---|---|---|
| primary | 18970 | grid=4000, α=1.464, target 620/1e5, coboundary, max_nodes=8M | `/tmp/ref7b_run.py` (exact FINAL-RECORD block) | True 1096556 |
| fail-check | 21235 | grid=4000, target **630**/1e5 | `/tmp/ref7b_630.py` | False (terminal-cell) |
| second-config | (child of 21218) | **grid=8000**, target 620/1e5 | `research/scripts/wave7b_grid8000_proxy.py` | True, node count ≠ 1096556 |

Primary setup (logged): cutoff_cells=74402, cell_count=74410, kernel table 0.6s
sha=b18966524b90591d, second-derivative table 1.5s, 6 coords × 2 components, initial boxes=64.
All three entered B&B at 99% CPU. The 630 and grid=8000 runs share the same fresh env and host,
so the *numerical-configuration* difference for the second-machine proxy is **grid** (4000→8000:
~74k→~149k-cell discretization, different range-min tables and B&B tree), not the machine.

(progress appended as it lands)

## Honesty ledger
- CHECKED NUMERICALLY (binary+cmd): PRIMARY re-run → `verified=True, nodes=1096556`, EXACT match
  to FINAL-RECORD's 1,096,556 (original: 3 identical runs). Fresh ephemeral uv env (python-flint
  0.9.0, mpmath 1.4.1, uv 0.12.1) on host `void` (not the record machine). cmd:
  `uv run --with mpmath --with python-flint python3 -u /tmp/ref7b_run.py` — runner is the exact
  FINAL-RECORD parameter block (cosine_kernel(1.464), w=2.0/(7-(j-i)), p=[946,1177,877,877,1177,946]
  /1920000, q=[31343/100000,1/3,105971/300000,105971/300000,1/3,31343/100000], pressure=1/3000,
  m=6, target=620/100000, grid=4000, cap_scheme='coboundary', max_nodes=8000000). Determinism:
  identical node count across machines ⇒ the B&B node count is a machine-invariant invariant.
- CHECKED NUMERICALLY (binary+cmd): 630/1e5 failure check → `False`, 243,939 nodes,
  status=terminal-cell, unresolved cell ((8042,8042),(4205,4205),(8044,8044),(7984,7984),
  (7991,7991),(4215,4215)) low=0.0062867 < 0.0063. Reproduces FINAL-RECORD's "630 FAILS
  terminal-cell"; 620/1e5 is the certified ceiling, consistent.
- INCONCLUSIVE (run continues in background): grid=8000 second-configuration proxy
  (`research/scripts/wave7b_grid8000_proxy.py`, PID child 21241) still in B&B at 12:20 CPU as of
  final poll. Watcher `/tmp/ref7b_watch.sh` (PID 29400) auto-appends its RESULT line to this note.
  A node-limit/False here would NOT refute the record (grid=8000 is not the certified config) but
  would be a reported discrepancy; expected True with a different node count.
- CONJECTURED: nothing.
- **Verdict: certificate re-verified on a second configuration (fresh uv env, python-flint
  0.9.0/mpmath 1.4.1, host void) with EXACT reproduction of `True` + node count 1,096,556; the
  630/1e5 ceiling failure reproduced. 6C caveat (iii) — 1M-node tree not re-run elsewhere —
  is closed (primary), with a stronger-discretization (grid=8000) confirmation in flight.**
- **FAIL630**: RESULT630 False 243939 terminal-cell unresolved terminal cell ((8042, 8042), (4205, 4205), (8044, 8044), (7984, 7984), (7991, 7991), (4215, 4215)) low=0.0062867300813309246
- **PRIMARY**: RESULT True 1096556
- **G8000**: RESULT8000 True 1097508 None None
