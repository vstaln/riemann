
# Riemann program
- Persistent project at /home/vstaln/riemann. Read hooks/agents.md before working there: research charter, never-give-up clause, honesty guardrails, multi-agent research protocol, s4h methods.

## Subagent operation (binding, config: ~/.pi/agent/agents/*.md)
- **Subagents run in BACKGROUND by default** — `run_in_background: true` is locked in every agent file (adventurer, architect, builder, diagnose, planner, reviewer, writer). Dispatch with `run_in_background: true` and monitor via get_subagent_result; do not block the main loop on them.
- **Context death is the #1 failure mode** — agents have died at 85–99% context before writing. Every agent file now carries a binding context-discipline block: write the deliverable AFTER ≤3 FILE READS or FIRST 5 TOOL CALLS, then refine with ≤3 more reads. A committed partial note beats a dead agent.
- **Compaction is normal** — subagent sessions auto-compact (event `subagents:compacted`); a compacted agent should keep working, not restart.
- **Write-capable agents only**: adventurer, architect, builder, writer have `write, edit`; diagnose/planner/reviewer are read-only (they return verdicts, not files). Explore (default) is read-only — use architect/builder/writer for any write task.
- **Never dispatch the same lever twice** — check `research/notes/` for an existing note before launching; duplicate agents waste rate-limit budget (deepseek 429s under concurrency).

