# swarm_langgraph — LangGraph orchestrator for the riemann swarm

Implements the topology from `research/notes/graph-engineering-swarm.md` as a
real LangGraph `StateGraph`, replacing the file-based dispatcher idea:

```
PLANNER ──► IDEA-GEN-0..N ──► GATE ──► EXECUTOR-0..M ──► VERIFIER-0..K ──► JUDGE ──► SYNTHESIZER ──► CRITIQUE
              (parallel)      (novelty)   (parallel)        (adversarial)                            │
                                                                        ┌───────────────────────────┤
                                                          reject ──► PLANNER (round+1, capped)   accept ──► FINALIZE
```

## Binding conventions (riemann hooks)

- **Orchestration glue only.** Python never computes here. EXECUTOR nodes either
  shell out to a *prebuilt* Rust binary (`idea["rust_cmd"]`, via `_run_rust`)
  or emit a method note labeled `CONJECTURED` with a proposed `rug`/`arb` check
  and the belief it would change. No Python numeric loops — ever.
- **Honesty labels** on every claim: `PROVEN / CHECKED NUMERICALLY /
  CONJECTURED / ABANDONED`. VERIFIER nodes re-derive adversarially and never
  weaken a validator.
- **File protocol (append-only)** under `research/waves/wave-<N>/`:
  `tasks.md`, `ideas/idea-gen-<i>.md`, `results/executor-<i>.md`,
  `verdicts.md`, `score.md`, `synthesis.md`, `final.md`.
- **Endpoint is shared with the bot** (OpenCode Go / `deepseek-v4-flash`):
  `timeout=45`, `max_retries=1`, every node degrades gracefully on failure.

## Setup

```bash
cd tools/swarm_langgraph
uv python pin 3.13          # 3.12 is not available locally (uv would hang downloading it)
uv add langgraph langchain-openai langgraph-checkpoint-sqlite
```

## Run

```bash
.venv/bin/python swarm.py --dry-run                          # compile graph only
.venv/bin/python swarm.py --wave 7 --generators 2 --executors 1 --verifiers 1 --max-rounds 1
```

Flags: `--wave` (default: next free), `--generators/--executors/--verifiers`,
`--max-rounds` (critique-reject loop cap), `--rust-timeout`, `--frontier`
(custom standing context; default reads `PLAN.md`), `--model` (default
`deepseek-v4-flash`; anything else changes the model for every node), `--dry-run`.

### Resume

Waves are checkpointed to `research/waves/swarm.sqlite` (thread = `wave-<N>`).
Rerun the same `--wave` to resume from where it stopped — a wave interrupted
mid-verifier picks up at the verifier, it does not restart.

## Verified (2026-08-15)

Mini-wave 7 end-to-end: PLANNER emitted two real task specs (Weil-form test
function optimization; zero-repulsion lemma); two parallel IDEA-GEN nodes
produced 6 CONJECTURED method ideas (e.g. Fejér–Riesz SOS parametrization of
the test function, Möbius-rescaling averaging, Jacobi-polynomial extremal
constructions); GATE passed all; EXECUTOR wrote 6 method-note claims each with
a belief-change statement and proposed `rug`/`arb` check. Full wave incl.
verifier/judge/synthesis/critique stages completes under the shared endpoint;
per-call latency can reach 60–90s when the bot is active (see README caveat in
the graph-engineering project). Compute: none performed (method notes only).

## Extending

- **Rust compute wiring**: give an accepted idea a `rust_cmd` (prebuilt binary)
  and the EXECUTOR will run it and label the result `CHECKED NUMERICALLY` /
  `INCONCLUSIVE` by exit code. Build release binaries first (`cargo build
  --release --target x86_64-unknown-linux-musl`) — this orchestrator never
  builds.
- **Subagent dispatch**: nodes are Python functions and cannot call the pi
  subagent tool directly; to dispatch real subagents, shell out to
  `pi -p "<prompt>"` (non-interactive) from a node. Default is LLM-direct.
