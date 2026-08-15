# Campaign Orchestrator — checkpointed LangGraph state machine

The Riemann campaign runs as a persistent, **kill-robust** state machine built on
LangGraph + SQLite checkpointing. Every super-step is durable: if the coordinator
process is killed (plugin install, crash, session end), the exact state survives in
`campaign.sqlite` and `resume` + `step` continues where the process died.

## Why LangGraph

- **Checkpointing is the point.** `SqliteSaver` persists state after every node run.
  A kill loses at most the in-flight node, never the campaign state.
- The graph is the durable **wave loop**: DEFINE → DISPATCH → MONITOR → CONSOLIDATE,
  driven by files on disk (briefs, deliverables, synthesis) + explicit reports.

## The pi ↔ orchestrator bridge

LangGraph is the *brain* (state + decisions). The pi coordinator is the *hands*
(launches actual subagents via the subagent tool, runs Rust, commits). The contract
per wave:

```
1. coordinator writes  research/notes/wave<N>-briefs-*.md
2. uv run orchestrator step          # queues levers -> prints DISPATCH list
3. pi loop launches each lever       # subagent tool, run_in_background=true
   uv run orchestrator report <L> DISPATCHED "agent_id"
4. agents land; coordinator updates:
   uv run orchestrator report <L> DONE "wave<N>-<L>-*.md"
   (or DEAD / INCONCLUSIVE)
5. uv run orchestrator step          # monitor auto-detects landed deliverables
6. when all levers resolved -> phase DONE; coordinator writes
   research/notes/wave<N>-synthesis-*.md
7. uv run orchestrator step          # advances to wave N+1
```

## Kill protocol

```
kill <reason>   # log the event (audit trail)
... process dies ...
resume          # prints where we were
step            # continues exactly there
```

The `kill_log` ring in state keeps the audit trail of every interruption, so the
campaign history is honest about restarts.

## Usage

```bash
cd tools/campaign_orchestrator
uv run orchestrator init      # (re)create the store
uv run orchestrator step      # advance one super-step
uv run orchestrator status    # current wave/phase/levers/kill_log
uv run orchestrator report <lever> <status> [note]
uv run orchestrator kill <reason>
uv run orchestrator resume
```

## Notes

- Python is used HERE ONLY because the user explicitly authorized LangGraph
  (`lang graph is python but is ok to use`) — this is the single sanctioned Python
  exception; all mathematical computation remains Rust (rug/arb-sys).
- State schema in `orchestrator/state.py`; graph in `orchestrator/graph.py`;
  CLI in `orchestrator/__main__.py`.
