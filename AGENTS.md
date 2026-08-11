# Riemann program

Read hooks/agents.md — the persistent research charter: never-give-up search for a proof of RH, honesty guardrails (no fabricated proofs; every claim labeled and numerically checked; adversarial validators), multi-agent research protocol, s4h methods. Follow PLAN.md for the plan and workspace layout. These bind before any work in this directory.

## Mandatory: code-backed verification + documentation (binds on every agent, every round)

1. **Confirm/deny only with code.** Every quantitative claim (constant, moment, eigenvalue, correlation, comparison, empirical trend) must be produced by a script you wrote and ran — never report a number no script produced. CPU-bound work in Rust (musl+rust-lld, `cargo build --release --target x86_64-unknown-linux-musl`); high-precision/exploratory via `uv run --quiet python` (mpmath/numpy/scipy; pip disabled). Don't edit canonical `tools/` if another agent owns it — use a scratch dir and say where.
2. **Save code with the note.** Every deliverable in `research/notes/` cites the exact script + command behind every number. Copy final scripts into `tools/` (or alongside the note) before finishing, unless the path is owned by another agent.
3. **Document every finding.** Every task ends with a note in `research/notes/` — including negatives, refuted inputs, dead ends, blockers. A negative with a script is a result; without one it's a rumor. Label: PROVEN / CHECKED NUMERICALLY (script+command) / CONJECTURED / ABANDONED (reason) / INCONCLUSIVE (blocker).
4. **Adjudicate disagreements with code.** When two agents' numbers disagree, both re-derive side by side in code; the resolution (which side was wrong and why) is written into both notes. No ambiguity left standing.
5. **Verification scripts are first-class artifacts** — self-contained, parse sources directly, print verdicts (model: `tools/verify_enclok.py`, `tools/qi_sweep.py`, `tools/nevanlinna_check.py`, `tools/lpdual/verify_exact_cert.py`).
