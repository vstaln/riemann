# Graph Engineering for the Riemann Swarm

**Status:** DESIGN (to be implemented). **Date:** 2026-08-12.
**Labels:** the design itself is CONJECTURED (best practice, not proven optimal);
the tooling facts (pi subagents, SSH cloud agents, git exchange) are CHECKED NUMERICALLY (verified live).

## Why graph engineering for this swarm?

A swarm of ~30 LLM agents is a *network*. How agents are wired determines:

- **Idea diversity** — a fully-connected mesh converges too fast (groupthink, everyone copies the best idea); a pure star (all ideas to one oracle) bottlenecks and loses parallelism. The literature on collective intelligence (e.g. swarm intelligence, ensemble diversity) says you want *moderate* connectivity: independent parallel generators + sparse cross-links, so the search space is explored broadly before any convergence step.
- **Verification quality** — a judge who reads the proposer's own writeup inherits its blind spots. Independent verifiers (fresh context, different agent) catch errors a self-check never will. This is the repo's existing "adversarial validators" rule, made structural.
- **Convergence** — without a synthesis step, 30 agents produce 30 divergent notes and no progress. The graph must have explicit merge/synthesize nodes that consume many leaf results and emit one consolidated artifact.

LangGraph-style orchestration is the reference model: a graph of nodes (agents/functions) with edges (state transitions), checkpointing, and explicit control flow (conditional edges = "if verified, merge; else, back to generator"). We do not need the LangGraph library — we can implement the *graph semantics* with our existing tools (subagents, SSH, git, files).

## Node types (roles)

| Node | Count | Tool | Output |
|---|---|---|---|
| `PLANNER` | 1 | local subagent (architect/planner) | decomposes current frontier into attackable problems; emits task specs |
| `IDEA-GEN` | 10–20 | local + cloud `pi -p` agents | 10–15 diverse CONJECTURED ideas each → `research/notes/idea-wave-N.md` |
| `EXECUTOR` | 5–10 | local subagents (builder/general) | picks a promising idea, implements + runs the verification script, writes note with script+output |
| `VERIFIER` | 3–5 | *independent* subagents (reviewer/diagnose) | adversarial: tries to break the executor's claim with its own code; writes verdict note |
| `JUDGE` | 2–3 | local subagents | scores surviving claims (impact × feasibility × verification strength); ranks |
| `SYNTHESIZER` | 1–2 | writer/general | merges accepted claims into consolidated artifacts (ladder, mechanism note, paper sections) |
| `CRITIQUE` | 1 | general-purpose | reviews the synthesis for holes; emits `{accept, reject-with-reason}` → loop back |

## Graph topology (edges)

```
                    ┌────────────────────────────┐
                    │         PLANNER            │
                    └─────────────┬──────────────┘
                                  │ task specs
        ┌────────────┬────────────┼────────────┬────────────┐
        ▼            ▼            ▼            ▼            ▼
   IDEA-GEN-1    IDEA-GEN-2  IDEA-GEN-3 ...  CLOUD-GEN-A  CLOUD-GEN-B
   (local)       (local)      (local)         (kanaka2)    (oracle-old)
        └────────────┬────────────┴────────────┴────────────┘
                     │  idea notes (files)
                     ▼
               (gate: novelty check — drop duplicates of tried ideas)
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   EXECUTOR-1   EXECUTOR-2   EXECUTOR-3        (each executor → 1 idea, isolated)
        │            │            │
        ▼            ▼            ▼
   VERIFIER-1   VERIFIER-2   VERIFIER-3        (independent adversarial check)
        │            │            │
        ▼            ▼            ▼
              JUDGE (ranks) ──► SYNTHESIZER ──► CRITIQUE ──► {accept → ladder/paper}
                                             │        │
                                             │        └── reject → back to PLANNER (reason attached)
                                             └── accept → commit + broadcast to all agents
```

Key structural choices (each is a deliberate anti-failure mechanism):

1. **Generators are independent and parallel.** Each IDEA-GEN gets *only* the state-of-the-art note + the idea catalog (not each other's drafts). This maximizes diversity (the "thousands of ideas" requirement) and prevents one agent's framing from biasing the rest.
2. **Executor ↔ Verifier are different agents, never the same.** The verifier gets the executor's claim + its script, but must re-derive in *its own* scratch code. This is the repo's "never weaken a validator" rule, made structural. A claim that survives an independent adversarial verifier is worth keeping.
3. **Isolation by directory.** Each agent works in its own scratch dir; the only shared surface is `research/notes/` (append-only, one note per deliverable) and git commits by the orchestrator. No agent edits another's files mid-flight (prevents corruption).
4. **Convergence is a separate, explicit phase.** Synthesis only happens after a wave of verification completes. The SYNTHESIZER consumes all verdict notes and emits a consolidated `ladder.md` + `mechanism.md`. Critique loop: if a synthesis has a hole, it returns to PLANNER with the reason, not to the trash (per hooks).
5. **Cloud agents are generators + independent verifiers.** The three SSH hosts (kanaka2, oracle-old, oracle-new) each run `pi -p` with a prompt = the task spec. They are *cheap parallelism* for idea generation and a *second-opinion* verification lane (different hardware/context = genuinely independent re-derivation). Their notes are pulled back via git/scp.

## Message protocol (file-based, append-only)

1. Orchestrator writes `research/waves/wave-N/tasks.md` = list of task specs (one per agent).
2. Each agent reads its spec, works in `research/waves/wave-N/<agent-name>/`, writes:
   - `ideas.md` (IDEA-GEN) — 10–15 ideas, each labeled CONJECTURED
   - `result.md` (EXECUTOR) — claim + script path + exact command + output, honesty labels
   - `verdict.md` (VERIFIER) — `VERIFIED / REFUTED / INCONCLUSIVE` + evidence
   - `score.md` (JUDGE) — rank
3. Orchestrator merges via git; SYNTHESIZER consumes the merged wave dir.
4. Headline changes commit to `research/notes/` (the durable knowledge base).

## Implementation plan (priority order)

1. **`tools/swarm/wave.py`** — a dispatcher: takes a task list, fans out to local subagents (via pi subagent tool) + cloud agents (via `ssh host "cd repo && echo '<spec>' | pi -p ..."`), collects notes into `research/waves/wave-N/`, prints a status table. This is the spine.
2. **`tools/swarm/spec-template.md`** — the task-spec template with honesty labels and the exact verification protocol (script + command required).
3. **Wave 1 (immediate):** 6 IDEA-GEN local + 3 cloud IDEA-GEN (kanaka2, oracle-old, oracle-new) → ~120 ideas in `research/waves/wave-1/`.
4. **Wave 1 gate:** novelty check vs. `attack-vector-catalog*.md` (dedupe), then EXECUTORs on top 8–12.
5. **Wave 1 verification:** independent VERIFIERs (local + 1 cloud) on each surviving claim.
6. **Wave 1 synthesis:** SYNTHESIZER merges survivors into `ladder.md`; CRITIQUE reviews; accepted → commit + broadcast.

## What is PROVEN vs CONJECTURED here

- PROVEN (verified live today): cloud agents run `pi -p --provider commandcode --model deepseek/deepseek-v4-flash` on kanaka2, oracle-old, oracle-new; all return LLM output; all share the repo via ssh+git.
- CONJECTURED (best practice from the agent-orchestration literature — LangGraph graph-API semantics, ensemble-diversity results, tournament selection): that independent parallel generators + isolated executors + independent adversarial verifiers + explicit synthesis converges faster and with fewer false positives than a flat "everyone works on everything" mesh. This is exactly the repo's own multi-agent protocol made graph-formal.

## References (partially fetched; web access flaky)

- LangGraph / LangChain Graph API docs: https://docs.langchain.com/oss/python/langgraph/graph-api (concepts: nodes, edges, conditional edges, checkpointing, subgraphs)
- Anthropic multi-agent research system (Gan-style harness): https://www.anthropic.com/research/multi-agent-research-system (generator/evaluator/verifier loop)
- Agent topologies (supervisor, hierarchical, decentralized/peer-to-peer): https://docs.langchain.com/oss/python/langgraph/multi-agent/architecture
- Collective intelligence / ensemble diversity: standard swarms + diversity-vs-accuracy literature (e.g. "The Wisdom of Crowds" independence condition; ensemble learning diversity–accuracy tradeoff)
- Repo's own protocol (the strongest grounding): /home/vstaln/riemann/hooks/agents.md

**Next action:** implement `tools/swarm/wave.py` and dispatch Wave 1.
