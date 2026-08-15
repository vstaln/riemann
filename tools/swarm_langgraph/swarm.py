"""LangGraph orchestrator for the riemann swarm.

Implements the topology from research/notes/graph-engineering-swarm.md as a
real LangGraph StateGraph: PLANNER -> IDEA-GEN* -> GATE -> EXECUTOR* ->
VERIFIER* -> JUDGE -> SYNTHESIZER -> CRITIQUE -> (accept | back to PLANNER).

Conventions (riemann hooks, binding):
  * This is ORCHESTRATION GLUE only. Python never does math here: compute nodes
    shell out to prebuilt Rust binaries (idea["rust_cmd"]), or emit a method
    note labeled CONJECTURED with a proposed Rust verification path.
  * Every claim carries a label: PROVEN / CHECKED NUMERICALLY / CONJECTURED /
    ABANDONED. Verifiers re-derive adversarially; never weaken a validator.
  * File protocol (append-only): research/waves/wave-<N>/tasks.md, ideas/,
    results/, verdicts.md, score.md, synthesis.md.
  * LLM endpoint is shared with the bot: short timeouts, max_retries=1, degrade.

Usage:
  .venv/bin/python swarm.py --dry-run                     # compile graph only
  .venv/bin/python swarm.py --wave 7 --generators 2 --executors 1 \
      --verifiers 1 --max-rounds 1                        # one mini-wave

Resume a wave: rerun with the same --wave (SQLite checkpointer by thread_id).
"""
from __future__ import annotations

import argparse
import json
import operator
import os
import subprocess
import sys
from pathlib import Path
from typing import Annotated

from concurrent.futures import ThreadPoolExecutor
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict

RIEMANN = Path("/home/vstaln/riemann")
WAVES = RIEMANN / "research" / "waves"
NOTES = RIEMANN / "research" / "notes"
BASE_URL = "https://opencode.ai/zen/go/v1"

PROMPT_HARDENING = "Answer immediately with no internal deliberation. "


def make_llm(model: str = "deepseek-v4-flash") -> ChatOpenAI:
    return ChatOpenAI(
        base_url=BASE_URL,
        api_key=os.environ["OPENCODE_API_KEY"],
        model=model,
        temperature=0.4,
        timeout=45,
        max_retries=1,
        max_tokens=1500,
    )


def _safe_invoke(llm: ChatOpenAI, prompt: str) -> str:
    pool = ThreadPoolExecutor(max_workers=1)
    try:
        fut = pool.submit(llm.invoke, PROMPT_HARDENING + prompt)
        return fut.result(timeout=60).content or ""
    except Exception as exc:  # shared endpoint; degrade, never hang
        return f"[LLM unavailable: {type(exc).__name__}]"
    finally:
        pool.shutdown(wait=False)  # never block on a hung worker


def _read_json(text: str) -> dict:
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end <= start:
        return {}
    try:
        return json.loads(text[start : end + 1])
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# State
# ---------------------------------------------------------------------------

class SwarmState(TypedDict):
    wave: int
    round: int
    frontier: str              # standing context (PLAN.md + key notes)
    tried_levers: list         # note titles, for the novelty gate
    tasks: list                # task specs from PLANNER
    ideas: Annotated[list, operator.add]      # parallel writers -> reducer
    accepted: list             # ideas that passed the gate
    claims: Annotated[list, operator.add]     # parallel writers -> reducer
    verdicts: Annotated[list, operator.add]   # parallel writers -> reducer
    scores: list               # {claim_id, score, rationale}
    synthesis: str
    critique: dict             # {accept, reason}
    status: str                # running | accepted | exhausted


# ---------------------------------------------------------------------------
# Node: PLANNER
# ---------------------------------------------------------------------------

def planner_node(state: SwarmState, config) -> dict:
    cfg = config["configurable"]
    llm = cfg["llm"]
    n = cfg["generators"]
    prompt = (
        f"Decompose the current riemann frontier into {n} attackable task specs. "
        "Each spec: one concrete problem, the objects involved, and what a "
        "successful result would look like (a lemma, a refutation, a structure). "
        f"Do NOT repeat tried levers: {state['tried_levers'][:20]}.\n"
        f"FRONTIER:\n{state['frontier'][:2500]}\n"
        'Reply ONLY JSON: {"tasks": ["spec1", "spec2", ...]}'
    )
    tasks = _read_json(_safe_invoke(llm, prompt)).get("tasks", [])
    tasks = [str(t) for t in tasks if str(t).strip()][:n]
    _write(state, "tasks.md", _dump_list("TASKS", tasks))
    return {"tasks": tasks or [f"Re-derive the standing frontier claim: {state['frontier'][:300]}"]}


# ---------------------------------------------------------------------------
# Nodes: IDEA-GEN (parallel fan-out)
# ---------------------------------------------------------------------------

def make_idea_gen(idx: int):
    def node(state: SwarmState, config) -> dict:
        cfg = config["configurable"]
        llm = cfg["llm"]
        task = state["tasks"][idx % len(state["tasks"])]
        prompt = (
            "Generate 3 diverse CONJECTURED research ideas for this task. Each "
            "must be a method move (a transformation, an inequality to try, a "
            "reduction, a structure), never a compute grind. Do not repeat: "
            f"{state['tried_levers'][:15]}.\nTASK: {task}\n"
            'Reply ONLY JSON: {"ideas": ["idea1", "idea2", "idea3"]}'
        )
        ideas = _read_json(_safe_invoke(llm, prompt)).get("ideas", [])
        ideas = [str(i) for i in ideas if str(i).strip()][:3]
        out = [
            {"id": f"g{idx}-{j}", "generator": f"idea-gen-{idx}", "task": task,
             "idea": i, "label": "CONJECTURED"}
            for j, i in enumerate(ideas)
        ]
        existing_ids = {x["id"] for x in state["ideas"]}
        out = [x for x in out if x["id"] not in existing_ids]
        _write(state, f"ideas/idea-gen-{idx}.md", _dump_list(f"IDEAS (generator {idx})", [i["idea"] for i in state["ideas"] + out]))
        return {"ideas": state["ideas"] + out}
    return node


# ---------------------------------------------------------------------------
# Node: GATE (novelty, deterministic + cheap)
# ---------------------------------------------------------------------------

def gate_node(state: SwarmState, config) -> dict:
    tried = " | ".join(state["tried_levers"]).lower()
    accepted = []
    for idea in state["ideas"]:
        hay = idea["idea"].lower()
        if any(t in hay for t in tried.split(" | ") if len(t) > 8):
            continue  # duplicate of a tried lever -> drop
        accepted.append(idea)
    return {"accepted": accepted}


# ---------------------------------------------------------------------------
# Nodes: EXECUTOR (parallel). Compute stays in Rust; Python never computes.
# ---------------------------------------------------------------------------

def make_executor(idx: int):
    def node(state: SwarmState, config) -> dict:
        cfg = config["configurable"]
        llm = cfg["llm"]
        slice_ = state["accepted"][idx::cfg["executors"]]
        new_claims = []
        for idea in slice_:
            rust_cmd = idea.get("rust_cmd", "")
            if rust_cmd and _binary_exists(rust_cmd):
                # Belief line (hooks: compute only when it changes beliefs).
                belief = "Re-checking the numeric claim behind this idea."
                out = _run_rust(rust_cmd, timeout=cfg["rust_timeout"])
                claim = f"Ran `{rust_cmd}`: exit {out.returncode}. Output: {out.stdout[-500:]}"
                label = "CHECKED NUMERICALLY" if out.returncode == 0 else "INCONCLUSIVE"
            else:
                prompt = (
                    "For this CONJECTURED idea, write a 3-6 sentence method note: "
                    "the precise move, what belief a cheap Rust check (rug/arb) would "
                    "change, and the label CONJECTURED. No computation performed.\n"
                    f"IDEA: {idea['idea']}\nTASK: {idea['task']}"
                )
                claim = _safe_invoke(llm, prompt)
                label = "CONJECTURED"
            new_claims.append({
                "idea_id": idea["id"], "executor": f"executor-{idx}",
                "claim": claim, "script": rust_cmd or "method-note",
                "cmd": rust_cmd, "label": label,
            })
        existing = {c["idea_id"] for c in state["claims"]}
        new_claims = [c for c in new_claims if c["idea_id"] not in existing]
        _write(state, f"results/executor-{idx}.md", _dump_list(
            f"CLAIMS (executor {idx})", [c["claim"] for c in state["claims"] + new_claims]))
        return {"claims": new_claims}
    return node

# ---------------------------------------------------------------------------
# Nodes: VERIFIER (parallel, adversarial, independent)
# ---------------------------------------------------------------------------

def make_verifier(idx: int):
    def node(state: SwarmState, config) -> dict:
        cfg = config["configurable"]
        llm = cfg["llm"]
        # Only verify claims not yet verified (idempotent across resumes/rounds)
        already = {v["claim_id"] for v in state["verdicts"]}
        slice_ = [c for c in state["claims"][idx::cfg["verifiers"]] if c["idea_id"] not in already]
        new_verdicts = []
        for c in slice_:
            prompt = (
                "Adversarially re-derive this claim from scratch. Try to break it: "
                "is the label honest? is there a script behind numbers? Reply "
                'ONLY JSON: {"verdict": "VERIFIED|REFUTED|INCONCLUSIVE", '
                '"evidence": "one sentence"}. Never weaken a validator.\n'
                f"CLAIM: {c['claim'][:800]}\nLABEL: {c['label']}\nSCRIPT: {c['script']}"
            )
            raw = _read_json(_safe_invoke(llm, prompt))
            new_verdicts.append({
                "claim_id": c["idea_id"], "verifier": f"verifier-{idx}",
                "verdict": raw.get("verdict", "INCONCLUSIVE"), "evidence": raw.get("evidence", ""),
            })
        _write(state, "verdicts.md", _dump_list("VERDICTS", [f"{v['claim_id']}: {v['verdict']} — {v['evidence']}" for v in state["verdicts"] + new_verdicts]))
        return {"verdicts": new_verdicts}
    return node


# ---------------------------------------------------------------------------
# Node: JUDGE
# ---------------------------------------------------------------------------

def judge_node(state: SwarmState, config) -> dict:
    cfg = config["configurable"]
    llm = cfg["llm"]
    verified = [c for c in state["claims"]
                if any(v["claim_id"] == c["idea_id"] and v["verdict"] == "VERIFIED" for v in state["verdicts"])]
    if not verified:
        return {"scores": []}
    prompt = (
        "Score each verified claim on impact x feasibility x verification "
        "strength (0-10 each). Reply ONLY JSON: "
        '{"scores": [{"claim_id": "...", "score": 7, "rationale": "..."}]}.\n'
        + "\n".join(f"{c['idea_id']}: {c['claim'][:300]}" for c in verified)
    )
    scores = _read_json(_safe_invoke(llm, prompt)).get("scores", [])
    _write(state, "score.md", _dump_list("SCORES", [f"{s.get('claim_id')}: {s.get('score')} — {s.get('rationale','')}" for s in state["scores"] + scores]))
    return {"scores": scores}


# ---------------------------------------------------------------------------
# Node: SYNTHESIZER
# ---------------------------------------------------------------------------

def synthesizer_node(state: SwarmState, config) -> dict:
    cfg = config["configurable"]
    llm = cfg["llm"]
    if not state["claims"]:
        return {"synthesis": "No claims survived this wave."}
    prompt = (
        "Merge the wave's claims into one consolidated research note: headline "
        "result, labels, the single next move. Honesty labels mandatory.\n"
        + "\n".join(f"[{c['label']}] {c['claim'][:400]}" for c in state["claims"][:6])
    )
    synthesis = _safe_invoke(llm, prompt)
    _write(state, "synthesis.md", f"# Wave {state['wave']} synthesis (round {state['round']})\n\n{synthesis}")
    return {"synthesis": synthesis}


# ---------------------------------------------------------------------------
# Node: CRITIQUE + routing
# ---------------------------------------------------------------------------

def critique_node(state: SwarmState, config) -> dict:
    cfg = config["configurable"]
    llm = cfg["llm"]
    prompt = (
        "Review this synthesis for holes: unlabeled claims, numbers without "
        "scripts, overclaims. Reply ONLY JSON: "
        '{"accept": true|false, "reason": "one sentence"}.\n'
        f"SYNTHESIS: {state['synthesis'][:1200]}"
    )
    raw = _read_json(_safe_invoke(llm, prompt))
    return {"critique": {"accept": bool(raw.get("accept")), "reason": str(raw.get("reason", ""))}}


def route_after_critique(state: SwarmState) -> str:
    if state["critique"].get("accept"):
        return "finalize"
    if state["round"] >= state.get("max_rounds", 2):
        return "finalize"
    return "planner"  # reject -> back to PLANNER with reason attached


def finalize_node(state: SwarmState, config) -> dict:
    reason = "" if state["critique"].get("accept") else f"\nRejected reason: {state['critique'].get('reason','')}"
    _write(state, "final.md", f"# Wave {state['wave']} final\nStatus: {state['status']}{reason}\n\n{state['synthesis']}")
    return {"status": "accepted" if state["critique"].get("accept") else "exhausted"}


# ---------------------------------------------------------------------------
# Graph assembly
# ---------------------------------------------------------------------------

def build_graph(cfg: dict):
    g = StateGraph(SwarmState)
    g.add_node("planner", planner_node)
    for i in range(cfg["generators"]):
        g.add_node(f"idea_gen_{i}", make_idea_gen(i))
    g.add_node("gate", gate_node)
    for i in range(cfg["executors"]):
        g.add_node(f"executor_{i}", make_executor(i))
    for i in range(cfg["verifiers"]):
        g.add_node(f"verifier_{i}", make_verifier(i))
    g.add_node("judge", judge_node)
    g.add_node("synthesizer", synthesizer_node)
    g.add_node("critique", critique_node)
    g.add_node("finalize", finalize_node)
    g.add_node("next_round", lambda state: {"round": state["round"] + 1})

    g.add_edge(START, "planner")
    for i in range(cfg["generators"]):
        g.add_edge("planner", f"idea_gen_{i}")
        g.add_edge(f"idea_gen_{i}", "gate")
    for i in range(cfg["executors"]):
        g.add_edge("gate", f"executor_{i}")
    for i in range(cfg["verifiers"]):
        for j in range(cfg["executors"]):
            g.add_edge(f"executor_{j}", f"verifier_{i}")  # all executors feed all verifiers
    for i in range(cfg["verifiers"]):
        g.add_edge(f"verifier_{i}", "judge")
    g.add_edge("judge", "synthesizer")
    g.add_edge("synthesizer", "critique")
    g.add_conditional_edges("critique", route_after_critique, {"planner": "next_round", "finalize": "finalize"})
    g.add_edge("next_round", "planner")
    g.add_edge("finalize", END)
    return g


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _write(state: SwarmState, name: str, content: str):
    d = WAVES / f"wave-{state['wave']}"
    d.mkdir(parents=True, exist_ok=True)
    (d / name).parent.mkdir(parents=True, exist_ok=True)
    (d / name).write_text(content)


def _dump_list(title: str, items: list) -> str:
    body = "\n".join(f"- {i}" for i in items) if items else "- (none)"
    return f"# {title}\n\n{body}\n"


def _binary_exists(cmd: str) -> bool:
    exe = cmd.split()[0]
    return bool(subprocess.run(["bash", "-lc", f"command -v {exe}"], capture_output=True, text=True).stdout.strip())


def _run_rust(cmd: str, timeout: int) -> subprocess.CompletedProcess:
    return subprocess.run(["bash", "-lc", cmd], capture_output=True, text=True, timeout=timeout)


def _tried_levers() -> list:
    if NOTES.is_dir():
        return sorted(p.stem for p in NOTES.glob("*.md"))[:60]
    return []


def _frontier() -> str:
    plan = RIEMANN / "PLAN.md"
    text = plan.read_text()[:2000] if plan.exists() else ""
    return text or "Standing target: unconditional simple-zero proportion beyond the in-class 0.673481 ceiling."


def _next_wave() -> int:
    existing = [int(p.name.split("-")[1]) for p in WAVES.glob("wave-*") if p.name[5:].isdigit()]
    return max(existing, default=0) + 1


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wave", type=int, default=None)
    ap.add_argument("--generators", type=int, default=3)
    ap.add_argument("--executors", type=int, default=2)
    ap.add_argument("--verifiers", type=int, default=2)
    ap.add_argument("--max-rounds", type=int, default=2)
    ap.add_argument("--rust-timeout", type=int, default=300)
    ap.add_argument("--frontier", type=str, default=None)
    ap.add_argument("--model", type=str, default="deepseek-v4-flash")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    wave = args.wave or _next_wave()
    cfg = {
        "llm": make_llm(args.model),
        "generators": args.generators,
        "executors": args.executors,
        "verifiers": args.verifiers,
        "rust_timeout": args.rust_timeout,
    }
    graph = build_graph(cfg)
    if args.dry_run:
        print("Graph compiles. Nodes:", [n for n in graph.compile().get_graph().nodes])
        return

    with SqliteSaver.from_conn_string(str(RIEMANN / "research" / "waves" / "swarm.sqlite")) as checkpointer:
        app = graph.compile(checkpointer=checkpointer)
        thread = {"configurable": {"thread_id": f"wave-{wave}", "llm": cfg["llm"], "generators": cfg["generators"],
                                   "executors": cfg["executors"], "verifiers": cfg["verifiers"],
                                   "rust_timeout": cfg["rust_timeout"]}}
        existing = checkpointer.get_tuple({"configurable": {"thread_id": f"wave-{wave}"}})
        if existing is not None:
            print(f"Resuming wave {wave} from checkpoint {existing.config['configurable']['checkpoint_id'][:8]}...")
            final = app.invoke(None, config=thread)
        else:
            state = {
                "wave": wave,
                "round": 0,
                "frontier": args.frontier or _frontier(),
                "tried_levers": _tried_levers(),
                "tasks": [], "ideas": [], "accepted": [], "claims": [],
                "verdicts": [], "scores": [], "synthesis": "", "critique": {"accept": False, "reason": ""},
                "status": "running", "max_rounds": args.max_rounds,
            }
            print(f"Wave {wave}: generators={args.generators} executors={args.executors} "
                  f"verifiers={args.verifiers} max_rounds={args.max_rounds}")
            final = app.invoke(state, config=thread)
        print(f"\nFinal status: {final.get('status')}")
        print(f"Ideas: {len(final.get('ideas', []))} | Accepted: {len(final.get('accepted', []))} "
              f"| Claims: {len(final.get('claims', []))} | Verdicts: {len(final.get('verdicts', []))}")
        wd = WAVES / f"wave-{wave}"
        print(f"Artifacts in {wd}: {sorted(p.name for p in wd.iterdir())}")


if __name__ == "__main__":
    main()
