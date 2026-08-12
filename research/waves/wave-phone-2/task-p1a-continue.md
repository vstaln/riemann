# Task: p1a-curve CONTINUATION — finish the p₁(A) table (setup is done, solver died)

**Agent:** EXECUTOR (phone, proot Ubuntu). **Charter:** ~/riemann/hooks/agents.md (honesty + PONYTAIL — numbers first, no essays, never lazy about rigor).
**Mission:** CONTINUE the p1a-curve line. The prior agent set up everything but its LP process died when it wrapped (run.log empty, no results.jsonl). Your job: rerun the solver robustly (nohup+setsid, poll within-session), assemble the p₁(A) table, and deliver the verdict. The whole context is in the status file + script — READ FIRST, then fix/run.

**READ, in order (STOP after):**
1. ~/riemann/research/waves/wave-phone-2/results/p1a-curve.md — the STATUS file (everything established: family = common2.gen_valid_family [VALID: s+2d=N, Σ marks=N — the prior agent already swapped away from lp_smallN's infeasible family]; N=64 wall A_max = 127/64 = 1.984375 derived via second-period ramp sum ≤ 64·Σm² ≤ 64·96 = 6144 ⇒ M ≤ 127; A ≥ 2 infeasible since Σ_{j=64}^{128} j = 6240 > 6144; A=1 anchor expected ≈ p₀(64) ∈ [0.828, 0.844]; the M2-agreement metric = normalized deficit R(A) = (1−p₁(A))/(1−p₁(1)) vs 1/A²; roadmap via R against the proven 256-anchor p₀ = 0.6818286874638315; TODO: seeds 42/1234/2024 × A ∈ {1.0…2.00}).
2. ~/riemann/tools/p1a_curve/p1a_curve.py — the solver script (6638 bytes). Diagnose why it produced nothing (run.log empty): read it, fix any bug, then RUN it robustly: `cd ~/riemann/tools/p1a_curve && setsid nohup python3 p1a_curve.py > run.log 2>&1 &` and POLL (sleep 30–90s loops, bash < 90 s per call) until results.jsonl has rows or the run errors (then fix and rerun).
3. If the solver cannot finish in-session (LP too slow at N=64 with extended rows), do the honest thing: reduce to a SMALLER effective problem that still answers the roadmap (e.g., fewer seeds × key A values {1.0, 1.03, 1.26, 1.70, 1.984}, or N=64 with a leaner formulation), and say exactly what you dropped.

**THE WORK:**
1. Get ≥ one full (seed, A) row per A in {1.0, 1.03, 1.26, 1.70, 1.984} (the roadmap A's + the wall).
2. Assemble the p₁(A) table (seeds 42/1234/2024 × those A), the mean curve, R(A) = (1−p₁(A))/(1−p₁(1)).
3. VERDICT vs M2: is R(A) ≈ 1/A² within 1.1% (f1curve §4's agreement level)? Interpolate A for p₁(A) = 0.70/0.75/0.80 on the 256-scale (via the normalized R against p₀ = 0.6818286874638315: p₁(A) = 1 − R(A)(1−p₀)). Does the roadmap 0.70@1.04 / 0.80@1.26 survive on public data?
4. State the honest status of every number (CHECKED NUMERICALLY / INCONCLUSIVE).

**HARD CAPS:** write ~/riemann/research/waves/wave-phone-2/results/p1a-curve.md (overwrite the STATUS file with the FINAL version) by your 12th tool use; finish by 18th; < 150K tokens. Crash-proof: append after every computation; bash < 90 s; the LP runs via setsid nohup so it survives your session. No subagents.

**Deliverable:** ~/riemann/research/waves/wave-phone-2/results/p1a-curve.md (FINAL, replaces STATUS).
**Report < 100 words:** the p₁(A) table, A for 0.70/0.75/0.80, M2-agreement verdict. End: RESULT: <status> — <one line>.
