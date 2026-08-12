# TASK: Complete the finite-T orchestrator graph — SYNTHESIZER role

## Mission
The finite-T orchestrator (wave-orch-phone, task-orch-finitet) ran a 5-role sub-swarm and its agent died on a phone crash BEFORE writing the synthesis. The graph is one step from complete. Your job: read the 5 completed role files, run the orchestration's SYNTHESIZER step, and write the one coherent answer to P6 (is the record finite-T robust?).

## Context — the role files are DONE, do NOT recompute them
Read in `research/waves/wave-orch-phone/results/`:
1. `reader-finitet.md` — the certificate formula contains NO T-dependent dropped term → record is finite-T-robust by construction
2. `idea-gen-finitet.md` — ideator's finite-T angles
3. `executor-finitet.md` + `executor-finitet-probe.py` + `executor-probe.out` — what the executor actually computed
4. `verifier-finitet.md` + `verifier-finitet-flip.py` — adversarial check (the flip test)
5. `theorist-finitet.md` — the theorist's structural read
Also: `research/waves/wave-orch-phone/probe/` contains `tower_probe.py` — a SIBLING probe with a KNOWN BUG (line 87: mpc-vs-int comparison in find_roots). The bug is documented in the wave notes; do NOT trust its output; say so in the synthesis and mark any numbers it produced INCONCLUSIVE.

## The work
1. Read all 5 role files + the probe outputs. Extract each role's verdict (with labels) into one table.
2. Write the SYNTHESIS: does the record's certificate hold for all finite T? What is the single best answer to P6 the swarm produced? What did the verifier's flip test conclude?
3. ONE cheap adjudication only if the files DISAGREE on a number (ponytail rung 1: otherwise cite, don't recompute): re-run the disagreeing script on the phone (`proot-distro login ubuntu -- python3 file.py`) and report which side was right.
4. Note the tower_probe.py bug's impact: which claimed numbers (if any) depend on it.

## Deliverable
`research/waves/wave-orch-phone/results/synthesis-finitet.md` — the finite-T verdict with labels, the role-verdict table, the bug-impact note.

## Ponytail (hooks/agents.md §PONYTAIL)
This is a read-and-synthesize task — the cheapest "computation" is reading the files that exist. No new probes unless the files disagree.
