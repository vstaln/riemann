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
# --- Provider routing (2026-08-20 revamp: commandcode muse-spark via headroom) ---
# Pi itself runs on commandcode/meta/muse-spark-1.2-contributor via headroom
# proxy at $OPENAI_BASE_URL (http://127.0.0.1:8787/v1). The swarm reuses that
# proxy so it inherits the session's auth automatically — no key duplication.
# Fallbacks: direct commandcode endpoint, then legacy opencode (for offline replay).
COMMANDCODE_URL = "https://api.commandcode.ai/provider/v1"
LEGACY_BASE_URL = "https://opencode.ai/zen/v1"  # legacy deepseek path, keep for fallback
BASE_URL = LEGACY_BASE_URL  # kept for greps; actual resolution is in make_llm
DEFAULT_MODEL = os.environ.get("PI_MODEL") or "meta/muse-spark-1.2-contributor"
SESSION_KEY = "sk-NmmWJsRyrj5zzHei7CHEzYr1a711Na9QO09LCcDQDhfnnvHqTxbrvcTmD0fJahat"  # legacy opencode fallback

# muse-spark is a thinking model — the old deepseek hardening ("Answer immediately
# with no internal deliberation") makes it worse: reasoning still runs (3–4k tok) but
# max_tokens=4k then truncates to 0. For muse-spark drop the hardening and give
# 8k+ budget; for deepseek keep the cheap 4k path.
PROMPT_HARDENING_DEEPSEEK = "Answer immediately with no internal deliberation. "
PROMPT_HARDENING = PROMPT_HARDENING_DEEPSEEK  # kept for external grep; actual choice is per-model


def _is_muse_spark(model: str | None) -> bool:
    m = (model or DEFAULT_MODEL or "").lower()
    return "muse-spark" in m or m.startswith("meta/")


def _prompt_hardening_for(model: str | None) -> str:
    # muse-spark / gpt-5 reason; hardening wastes the reasoning budget and flips
    # max_tokens=4k into finish=length with 0 content (measured 2026-08-20: 4k->0, 8k->10k).
    if _is_muse_spark(model):
        return ""
    return PROMPT_HARDENING_DEEPSEEK


def _resolve_base_url(model: str | None = None) -> str:
    # Muse-spark / meta/* lives on commandcode; deepseek lives on opencode.
    # Pi's session env carries OPENAI_BASE_URL=http://127.0.0.1:8787 but nothing
    # listens there (Connection refused), so don't blindly trust it.
    m = (model or DEFAULT_MODEL or "").lower()
    if "muse-spark" in m or m.startswith("meta/"):
        return COMMANDCODE_URL
    # Commandcode also hosts some GPT-family; keep opencode for deepseek-free etc.
    if "deepseek" in m or "mimo" in m or "nemotron" in m or "laguna" in m:
        return LEGACY_BASE_URL
    for k in ("OPENAI_BASE_URL", "OPENAI_API_BASE"):
        v = os.environ.get(k)
        if v:
            return v
    if os.environ.get("COMMANDCODE_API_KEY"):
        return COMMANDCODE_URL
    return LEGACY_BASE_URL


def _resolve_api_key(model: str | None = None) -> str:
    # Model-aware: muse-spark/meta/* -> commandcode key; deepseek-family -> opencode key.
    is_muse = _is_muse_spark(model)
    # For muse-spark prefer commandcode key
    if is_muse:
        v = os.environ.get("COMMANDCODE_API_KEY")
        if v:
            return v
        try:
            import json as _json
            mj = Path.home() / ".pi" / "agent" / "models.json"
            if mj.exists():
                j = _json.loads(mj.read_text())
                ck = j.get("providers", {}).get("commandcode", {}).get("apiKey")
                if ck:
                    return ck
        except Exception:
            pass
        # last resort legacy (won't auth commandcode, but better than empty)
        for k in ("OPENCODE_API_KEY", "OPENAI_API_KEY"):
            v = os.environ.get(k)
            if v:
                return v
        return SESSION_KEY
    # Non-muse (deepseek/mimo etc) -> opencode key
    for k in ("OPENCODE_API_KEY", "OPENAI_API_KEY"):
        v = os.environ.get(k)
        if v:
            return v
    v = os.environ.get("COMMANDCODE_API_KEY")
    if v:
        return v
    try:
        import json as _json
        mj = Path.home() / ".pi" / "agent" / "models.json"
        if mj.exists():
            j = _json.loads(mj.read_text())
            # opencode key lives in env SESSION_KEY, but also try commandcode as fallback
            ck = j.get("providers", {}).get("commandcode", {}).get("apiKey")
            if ck:
                return ck
    except Exception:
        pass
    return SESSION_KEY


def make_llm(model: str | None = None) -> ChatOpenAI:
    model = model or DEFAULT_MODEL
    base_url = _resolve_base_url(model)
    api_key = _resolve_api_key(model)
    is_muse = _is_muse_spark(model)
    # muse-spark burns ~3.8k reasoning + ~2–6k text on the 1580-char idea-gen prompt
    # (measured 2026-08-20: 4k max_tokens -> finish=length content=0, 8k -> content~10k).
    # Keep 8k for muse-spark, 4k for deepseek; keep low reasoning for muse (budget).
    max_tok = 8000 if is_muse else 4000
    # muse-spark timeout 120 (observed reasoning+text ~6–7.5k tok); deepseek 90 is fine.
    tm = 120 if is_muse else 90
    kwargs: dict = dict(
        base_url=base_url,
        api_key=api_key,
        model=model,
        temperature=0.4,
        timeout=tm,
        max_retries=0,
        max_tokens=max_tok,
    )
    if any(x in model for x in ("muse-spark", "deepseek", "gpt-5", "o1", "o3", "reasoning")):
        kwargs["reasoning_effort"] = "low"
    return ChatOpenAI(**kwargs)


def _safe_invoke(llm: ChatOpenAI, prompt: str) -> str:
    import time as _time

    # FIX tokens-out: if free-tier out, skip LLM entirely and go straight to agy (saves 560s of 429 retries)
    if os.environ.get("TOKENS_OUT") == "1" or os.environ.get("AGY_ONLY") == "1":
        print(f"[swarm] TOKENS_OUT/AGY_ONLY set — skipping LLM, agy direct len(prompt)={len(prompt)}", flush=True)
        fallback = _agy_invoke(prompt)
        if fallback:
            print(f"[swarm] agy direct produced {len(fallback)} chars", flush=True)
            return fallback
        return "[LLM skipped: tokens out, agy failed]"

    last: Exception | None = None
    _model_id = getattr(llm, "model_name", None) or getattr(llm, "model", None) or ""
    _hard = _prompt_hardening_for(_model_id)
    _tm = 120 if _is_muse_spark(_model_id) else 90
    for attempt in range(1):  # was 2, now 1 to save quota (fail fast to agy)
        pool = ThreadPoolExecutor(max_workers=1)
        try:
            fut = pool.submit(llm.invoke, _hard + prompt)
            r = fut.result(timeout=_tm)
            if r and r.content:
                return r.content
            print(f"[swarm] attempt {attempt}: empty content, len(prompt)={len(prompt)} model={getattr(llm,'model_name', getattr(llm,'model','?'))} finish={getattr(getattr(r,'response_metadata',{}),'get',lambda*k: '?')('finish_reason','?') if hasattr(r,'response_metadata') else '?'}", flush=True)
        except Exception as exc:  # shared endpoint; degrade, never hang
            last = exc
            msg = str(exc)
            print(f"[swarm] attempt {attempt}: {type(exc).__name__}: {msg[:100]}", flush=True)
            # fast path: on 429/503/FreeUsageLimit, don't retry LLM, go straight to agy
            if "429" in msg or "503" in msg or "FreeUsageLimit" in msg or "Upstream" in msg:
                print(f"[swarm] quota hit — fast-fail to agy", flush=True)
                break
        finally:
            pool.shutdown(wait=False)  # never block on a hung worker
        _time.sleep(1)
    # FALLBACK: if the shared LLM endpoint is capped/unavailable (wave-24 failure
    # mode: weekly GoUsageLimitError -> all nodes silently produced "(none)"),
    # degrade to the agy CLI when available, instead of emitting an unusable
    # sentinel that the callers then parse as empty.
    if os.environ.get("AGY_FALLBACK", "1") == "1":
        fallback = _agy_invoke(prompt)
        if fallback:
            print(f"[swarm] agy fallback produced {len(fallback)} chars", flush=True)
            return fallback
    return f"[LLM unavailable: {type(last).__name__ if last else 'empty'}]"


def _agy_invoke(prompt: str) -> str:
    """Best-effort agy CLI fallback for idea generation when the shared LLM is
    down. agy is the same co-author tool used for direct batches; here it is
    used as a degraded generator. Self-contained prompts only (no repo paths:
    agy hangs on agentic tool-search)."""
    import tempfile
    import subprocess as sp
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write(prompt)
            pf = f.name
        out_path = f"{pf}.out"
        r = sp.run(["bash", "/home/vstaln/riemann/tools/agy_run.sh", pf, "240"],
                   capture_output=True, text=True, timeout=280,
                   env={**os.environ, "AGY_RUN_OUT": out_path})
        if r.returncode != 0:
            print(f"[swarm] agy fallback rc={r.returncode}", flush=True)
            return ""
        if os.path.exists(out_path):
            return Path(out_path).read_text()
        return ""
    except Exception as exc:
        print(f"[swarm] agy fallback error: {type(exc).__name__}: {str(exc)[:80]}", flush=True)
        return ""


def _read_json(text: str) -> dict:
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end <= start:
        return {}
    # Repair common truncation: unbalanced brackets / dangling tail.
    candidate = text[start : end + 1]
    try:
        return json.loads(candidate)
    except Exception:
        pass
    # progressive fallback: drop trailing unbalanced structure one level at a time
    depth = 0
    cut = -1
    for i, ch in enumerate(candidate):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                cut = i + 1
    if cut > 0:
        try:
            return json.loads(candidate[:cut])
        except Exception:
            return {}
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
        "For EACH spec also state: (a) which classical RH-equivalence it attacks "
        "(Li / Speiser / Nyman-Beurling-Baez-Duarte / Turan-Polya / de Branges / "
        "Weil), (b) the RH-false control model that MUST fail if the lever works, "
        "(c) the hidden assumption that would silently kill it. "
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
        llm = cfg["llms"].get(cfg["gen_models"][idx % len(cfg["gen_models"])], cfg["llm"])
        task = state["tasks"][idx % len(state["tasks"])]
        # PER-GENERATOR DISTINCT ANGLE — each angle is now anchored to a real s4h skill
        # (project-local .pi/skills/; hooks demand ≥1 s4h skill per brief). The lens
        # description names the skill explicitly so the LLM's chain is s4h-disciplined,
        # not hand-rolled slang. Diversity is by construction, not by temperature.
        GEN_ANGLES = [
            ("HESSIAN/ARCHIMEDEAN", "s4h-creativity-assumption-excavator + s4h-aesthetic-pattern-detection on the gamma-factor background and TOTAL-POSITIVITY", "total-positivity, Polya-Laguerre, log-concavity"),
            ("TOPOLOGICAL-INDEX", "s4h-analogy-domain-transfer (2D fluid Poincare-Hopf) + s4h-systems-feedback-mapping", "Poincare-Hopf, winding, index, vortex"),
            ("GAP-STRUCTURE", "s4h-constraint-hardness-testing on the zero-gap barrier + s4h-information-signal-noise (gap-gap correlations)", "gap, spacing, midpoint, resolvent"),
            ("ARITHMETIC-DUALITY", "s4h-investigation-claim-decomposition + s4h-logic-consistency-check on Baez-Duarte / Mellin dual witnesses", "Baez-Duarte, Mellin, dual, Hardy"),
            ("CONTROL/BLASCHKE", "s4h-analogy-domain-transfer (control/Blaschke non-minimum-phase) + s4h-systems-leverage-analysis", "Blaschke, all-pass, Poisson-Bode, H-infinity"),
            ("FRAME/INFO-THEORY", "s4h-information-entropy + s4h-network-effects (frame/ tight-frame information geometry)", "frame, information, entropy, tight-frame"),
        ]
        angle, lens_desc, ban_words = GEN_ANGLES[idx % len(GEN_ANGLES)]
        # Extract the s4h skill tag for the mandatory header (first s4h-* token in lens_desc)
        import re as _re2
        _m = _re2.search(r"s4h-[a-z0-9-]+", lens_desc)
        s4h_tag = _m.group(0) if _m else "s4h-creativity-assumption-excavator"
        prompt = (
            f"You are generator {idx}. Your UNIQUE angle this wave: {angle} — {lens_desc}. "
            f"Applied s4h skill: {s4h_tag} (you MUST name it in your JSON under key 's4h_skill'). "
            f"Other generators are covering: {[a for a,_,_ in GEN_ANGLES if a != angle]}. "
            "You MUST produce ideas that ONLY your angle can see. Do NOT produce any idea "
            "that another generator's angle would produce. Produce 2 ideas, each: "
            "(1) a PROOF-SHAPED move (a lemma to prove, a structure to exhibit, a reduction "
            "to a named known theorem); (2) the EXACT computable statement (what to evaluate, "
            "at what N/T, in what precision); (3) the RH-false control (Davenport-Heilbronn, "
            "Epstein, or planted FE pair) and the EXACT predicted value there (derived, or "
            "say 'must be measured' honestly); (4) the label (PROVEN-able / CONJECTURED / "
            "measurement-probe); (5) the ONE cheap Rust/rug check (<1min) that would change "
            "belief and what each outcome means — also give its exact shell command as rust_cmd. ALLOWED BINS ONLY (whitelist — any other bin => INCONCLUSIVE, never VERIFIED): "
            "DIRECT-RH: jensen_probe, jensen_weil_hybrid, arch_hessian_detrend, li_jensen_laplace, turan_debranges_jensen, beurling_jensen_dist, nyman_jensen_hybrid, jensen_hessian_gamma, jensen_curvature_subtract, li_debranges_turan, li_feedback_gain, kolmogorov_prime, diffraction_logp, coulomb_energy, persistence_zero "
            "(jensen_* in tools/jensen_probe/Cargo.toml alias honest E(c,r); alien 4 in tools/alien_probes/Cargo.toml — N-body global discriminants). "
            "LOWER-BOUNDS (proportion improvement, firewall holds — not RH evidence): sinc_m3_cert (tools/sinc_m3_cert), finitet-cinf (tools/finitet), angle_kernel (tools/angle_kernel), coboundary_search (tools/coboundary_search), npoint-sweep (tools/npoint-sweep), cert-floor-rs, verifier-rs, logprofile. "
            "EXAMPLES (copy exactly, only change flags): "
            "\"cargo run --bin jensen_probe -- --c-re 0.75 --r 0.30 --planted-beta 0.80 --centers 14.1347,14.28,14.43,30,50\" "
            "or \"cargo run --bin sinc_m3_cert -- --help\" "
            "or \"cargo run --bin finitet-cinf -- --help\" "
            "or \"cargo run --bin npoint-sweep -- --help\". "
            "If you invent a bin not in the whitelist, your idea will be scored INCONCLUSIVE. If no bin fits, use \"\" but still describe the check. "
            f"NEVER use these (death list): {ban_words}, d_N floors, winding/argument-principle "
            "zero-counts, explicit-formula residue extraction, zero-search, Herglotz-family "
            "objects, midpoint resolvent floors, critical-point counts (all classical or "
            "closed). State which UNIQUE angle and s4h skill you're using and why your idea is not on the "
            "death list.\n"
            f"TASK: {task}\nDo not repeat: {state['tried_levers'][:10]}.\n"
            'Reply ONLY JSON: {"ideas": [{"text": "idea1 full text (include (1)-(5) and WHY NOT DEATH LIST)", "rust_cmd": "cargo run --bin ... or empty", "label": "CONJECTURED", "s4h_skill": "s4h-..."}, {"text": "idea2...", "rust_cmd": "...", "label": "...", "s4h_skill": "..."}], "s4h_skill": "..."}  '
            'Legacy string array {"ideas": ["idea1","idea2"]} also accepted but rust_cmd will be empty.'
        )
        raw = _safe_invoke(llm, prompt)
        parsed = _read_json(raw)
        ideas_raw = parsed.get("ideas", [])
        # agy (the idea co-author) returns markdown candidates, not the JSON
        # {"ideas": [...]} shape; parse "Candidate N" sections as ideas.
        if not ideas_raw and "Candidate" in raw:
            import re as _re
            ideas_raw = [_re.sub(r"^#{1,6}\s*", "", s).strip()
                         for s in _re.split(r"(?=^#{1,6}\s*Candidate)", raw, flags=_re.M)
                         if "Candidate" in s][:2]
        # Normalize: supports structured {"text","rust_cmd","label","s4h_skill"} (new),
        # legacy [{"label":...,"lemma":...}] (muse-spark), and ["string"].
        # Handle both dict and string shapes, preserving rust_cmd per idea.
        normalized: list[dict] = []  # {text, rust_cmd, label, s4h_skill}
        for it in ideas_raw:
            if isinstance(it, dict):
                text = it.get("text") or it.get("idea") or it.get("lemma") or it.get("move") or ""
                if not text:
                    # fallback: dump the dict as text so gate/verifier still see it
                    try:
                        text = json.dumps(it, ensure_ascii=False)
                    except Exception:
                        text = str(it)
                rust_cmd = it.get("rust_cmd") or it.get("rustCmd") or it.get("cmd") or it.get("rust") or ""
                label = it.get("label") or it.get("honesty_label") or "CONJECTURED"
                skill = it.get("s4h_skill") or it.get("s4h") or parsed.get("s4h_skill") or s4h_tag
                normalized.append({"text": str(text).strip(), "rust_cmd": str(rust_cmd).strip(), "label": str(label).strip() or "CONJECTURED", "s4h_skill": str(skill).strip() or s4h_tag})
            elif isinstance(it, str) and it.strip():
                normalized.append({"text": it.strip(), "rust_cmd": "", "label": "CONJECTURED", "s4h_skill": parsed.get("s4h_skill") or s4h_tag})
            elif it is not None:
                s = str(it).strip()
                if s:
                    normalized.append({"text": s, "rust_cmd": "", "label": "CONJECTURED", "s4h_skill": parsed.get("s4h_skill") or s4h_tag})
        normalized = normalized[:2]
        # agy Candidate fallback already string-normalized above; ensure rust_cmd empty there
        s4h_skill = parsed.get("s4h_skill") or s4h_tag
        out = [
            {"id": f"g{idx}-{j}", "generator": f"idea-gen-{idx}", "task": task,
             "idea": n["text"], "rust_cmd": n["rust_cmd"], "label": n["label"], "s4h_skill": n["s4h_skill"] or s4h_skill or s4h_tag}
            for j, n in enumerate(normalized)
        ]
        existing_ids = {x["id"] for x in state["ideas"]}
        out = [x for x in out if x["id"] not in existing_ids]
        # Write ONLY this generator's own ideas (not the accumulated state) —
        # otherwise later generators imitate earlier ones (serial-imitation
        # collapse: gens 2-5 added nothing in wave-45 because they echoed gen-1).
        _write(state, f"ideas/idea-gen-{idx}.md", _dump_list(f"IDEAS (generator {idx})", [i["idea"] for i in out]))
        # NOTE: `ideas` channel uses operator.add reducer, so return ONLY the new
        # items — returning state+out would double-count (3 -> 9 -> 21 -> 45 -> 93).
        return {"ideas": out}
    return node


# ---------------------------------------------------------------------------
# Node: GATE (novelty, deterministic + cheap)
# ---------------------------------------------------------------------------

def gate_node(state: SwarmState, config) -> dict:
    tried = " | ".join(state["tried_levers"]).lower()
    # Death-list classifier: reject ideas whose mechanism is a known-collapse class
    # (all PROVEN dead or classical-only in prior waves). Root-cause fix for the
    # swarm re-emitting dead classes.
    # Surgical hybrid-aware death list (2026-08-20 fix 2)
    # Bare classical lanes are dead, but Jensen-circle-mean *transfers* to
    # Weil/Li/Turan/Beurling/Nyman are the LIVE frontier (wave-77: 4 ideas all
    # killed by substring hits inside disclaimer/positive-control text — locat via
    # "zero location", explicit formula as error term, baez-duarte in corona hybrid).
    # Gate is cheap pre-filter, not an adversarial referee: be narrow. Only the
    # PROVEN-closed bare subfamilies stay here; hybrids that name both Jensen and a
    # transfer target (Weil, Li, Beurling, Turan, de Branges) are exempt. Verifier
    # does the real adversarial kill with full context.
    DEATH_PATTERNS = [
        "winding", "argument principle", "index theorem", "poincare-hopf",
        "residue extraction", "contour shift",
        "herglotz", "nevanlinna", "transverse curvature", "gap-resolvent",
        "critical point", "laguerre", "interleav",
        "dipole", "log-derivative curvature",
        # "hessian determinant" removed 2026-08-20 fix 4: killed legitimate
        # HESSIAN/ARCHIMEDEAN gamma-curvature ideas (wave-79 g0-1) via substring
        # "det Hess log|xi|" heat-map. Keep verifier-stage check for bare dipole-well.
        # "euler product" removed 2026-08-20 fix 4: killed Hessian splitting lemma
        # (wave-79 g0-0) which used "explicit Euler product majorant" only as a
        # bound for zeta'/zeta inside the Jensen-Hessian hybrid, not as bare lane.
        "prime martingale", "scale orthogonality",
        "gram spectral", "hankel radius", "prime-zeta",
        "hyperdeterminant", "tensor",
        "cosh invariant", "stieltjes hankel", "nodal",
        # NOTE: removed broad killers that fire inside legitimate hybrid positives:
        # "d_n"/"baez-duarte"/"beurling"/"blaschke"/"hardy space"/"all-pass"
        # "weil"/"jensen"/"li"/"turan" as single words, "explicit formula",
        # "locat"/"pole"/"root-find"/"zero search" (hit "zero location" of planted
        # control description), "midpoint". These are now verifier-stage checks
        # with surrounding-context required, not gate substrings. Keep "li_k" etc
        # out too — Li is live via Li-Jensen transfer.
    ]
    accepted = []
    seen = set()
    for idea in state["ideas"]:
        raw_hay = idea["idea"]
        # Strip the disclaimer sentence ("WHY NOT DEATH LIST: ...") before checking —
        # ideas disclaim death-list terms with "No X, No Y" and would be killed by
        # substring search if we keep that section. The disclaimer is not mechanism.
        # Also strip JSON fields why_not_death_list / why_not_other for same reason.
        hay_for_gate = raw_hay
        # remove WHY NOT DEATH LIST block (case-insensitive) up to next period or next field
        import re as _re_gate
        hay_for_gate = _re_gate.sub(r"WHY NOT DEATH LIST:[^\n]*", "", hay_for_gate, flags=_re_gate.I)
        hay_for_gate = _re_gate.sub(r"why_not_death[^\"]*\"[^\"]*\"", "", hay_for_gate, flags=_re_gate.I)
        # also if idea is JSON string, parse and keep only mechanism fields for gate
        try:
            j = json.loads(raw_hay) if isinstance(raw_hay, str) and raw_hay.strip().startswith("{") else None
            if isinstance(j, dict):
                # keep only positive mechanism fields, not disclaimer fields
                keep_keys = [k for k in j.keys() if k not in ("why_not_death_list", "why_not_other_angles", "why_not_other", "why_not_death")]
                hay_for_gate = " ".join(str(j[k]) for k in keep_keys if k in j)
                if not hay_for_gate.strip():
                    hay_for_gate = raw_hay
        except Exception:
            pass
        hay = hay_for_gate.lower()
        # death-list kill (on-positive content only)
        if any(p in hay for p in DEATH_PATTERNS):
            _write(state, f"gate-rejects.md", _dump_list("GATE REJECTS (death-list)", [idea["idea"][:200]]))
            continue
        # tried-lever duplicate kill
        if any(t in hay for t in tried.split(" | ") if len(t) > 8):
            continue
        # sibling-dedup (same idea text from collapsed generators)
        norm = " ".join(hay.split())[:400]
        if norm in seen:
            continue
        seen.add(norm)
        accepted.append(idea)
    return {"accepted": accepted}


# ---------------------------------------------------------------------------
# Nodes: EXECUTOR (parallel). Compute stays in Rust; Python never computes.
# ---------------------------------------------------------------------------

def make_executor(idx: int):
    def node(state: SwarmState, config) -> dict:
        cfg = config["configurable"]
        # llm kept only for optional method-note sidecar, not for claims
        slice_ = state["accepted"][idx::cfg["executors"]]
        new_claims = []
        side_notes: list[str] = []
        for idea in slice_:
            rust_cmd = (idea.get("rust_cmd") or "").strip()
            idea_text = idea.get("idea", "")
            task_text = idea.get("task", "")
            s4h = idea.get("s4h_skill", "")
            if rust_cmd and _binary_exists(rust_cmd):
                out = _run_rust(rust_cmd, timeout=cfg["rust_timeout"])
                # keep stderr too — rug/arb diagnostics are on stderr
                out_tail = (out.stdout[-700:] + ("\nSTDERR:" + out.stderr[-400:] if out.stderr.strip() else ""))[:1100]
                claim = f"Ran `{rust_cmd}`: exit {out.returncode}. Output: {out_tail}"
                label = "CHECKED NUMERICALLY" if out.returncode == 0 else "INCONCLUSIVE"
                # side note: what the check was for
                side_notes.append(f"{idea['id']} [{s4h}] CHECKED via `{rust_cmd}` — {idea_text[:350]}")
            else:
                # STRICT Rust gate (2026-08-20 fix 3): no binary => no CONJECTURED claim.
                # Previously this emitted a CONJECTURED LLM method-note that verifiers
                # inflated to VERIFIED (wave-78: 4 CONJECTURED -> 1 false VERIFIED).
                # Now this is INCONCLUSIVE and verifier kills CONJECTURED at step (0).
                reason = "empty rust_cmd" if not rust_cmd else f"binary not found for `{rust_cmd.split()[0] if rust_cmd else ''}`"
                claim = (
                    f"NO BINARY ({reason}) — no computation performed for {idea['id']} [{s4h}]. "
                    f"IDEA: {idea_text[:700]}. TASK: {task_text[:220]}. "
                    f"Proposed rust_cmd: `{rust_cmd or '(empty — idea did not supply rust_cmd)'}`. "
                    "Label INCONCLUSIVE — requires a real Rust/rug check before verification."
                )
                label = "INCONCLUSIVE"
                side_notes.append(f"{idea['id']} [{s4h}] INCONCLUSIVE — {reason} — {idea_text[:300]}")
            new_claims.append({
                "idea_id": idea["id"], "executor": f"executor-{idx}",
                "claim": claim, "script": rust_cmd or "missing-binary",
                "cmd": rust_cmd, "label": label,
            })
        existing = {c["idea_id"] for c in state["claims"]}
        new_claims = [c for c in new_claims if c["idea_id"] not in existing]
        _write(state, f"results/executor-{idx}.md", _dump_list(
            f"CLAIMS (executor {idx})", [c["claim"] for c in state["claims"] + new_claims]))
        # sidecar for synthesis context — does not become a claim
        if side_notes:
            _write(state, f"results/method-notes-{idx}.md", _dump_list(f"METHOD NOTES (executor {idx} sidecar)", side_notes))
        return {"claims": new_claims}
    return node

# ---------------------------------------------------------------------------
# Nodes: VERIFIER (parallel, adversarial, independent)
# ---------------------------------------------------------------------------

def make_verifier(idx: int):
    def node(state: SwarmState, config) -> dict:
        cfg = config["configurable"]
        llm = cfg["llms"].get(cfg["ver_models"][idx % len(cfg["ver_models"])], cfg["llm"])
        # Only verify claims not yet verified (idempotent across resumes/rounds)
        already = {v["claim_id"] for v in state["verdicts"]}
        slice_ = [c for c in state["claims"][idx::cfg["verifiers"]] if c["idea_id"] not in already]
        new_verdicts = []
        for c in slice_:
            # (0) CONJECTURED/INCONCLUSIVE kill — executor strict gate (fix 3): claims with no binary
            # are INCONCLUSIVE by construction and must not become VERIFIED. This was the wave-78
            # inflation: CONJECTURED method note -> verifier said VERIFIED with 0/10 strength.
            if c.get("label") == "CONJECTURED":
                new_verdicts.append({
                    "claim_id": c["idea_id"], "verifier": f"verifier-{idx}",
                    "verdict": "INCONCLUSIVE", "evidence": "CONJECTURED method note — no computation performed, cannot be VERIFIED",
                })
                continue
            if c.get("label") == "INCONCLUSIVE" and "NO BINARY" in c.get("claim", ""):
                new_verdicts.append({
                    "claim_id": c["idea_id"], "verifier": f"verifier-{idx}",
                    "verdict": "INCONCLUSIVE", "evidence": "No binary / empty rust_cmd — no computation to verify",
                })
                continue
            prompt = (
                "Adversarially re-derive this claim from scratch. Try to break it. "
                "MANDATORY checks in order: "
                "(0) HONESTY: if LABEL is CONJECTURED or INCONCLUSIVE, verdict is INCONCLUSIVE (no computation to verify) — do not promote to VERIFIED. "
                "(1) CONTROL: does the claim NAME its RH-false control (Davenport-"
                "Heilbronn, Epstein class-2, planted FE pair at beta0, or alien planted beta0) AND give the EXACT derived number? For Jensen hybrids: E=log(r/d) with r,d (e.g. 1.386=log4) ; for ALIEN probes (kolmogorov_prime/diffraction_logp/coulomb_energy/persistence_zero): the ALIEN derived prediction with formula counts — e.g. kolmogorov pred saving ~N^{beta0}/(beta0 log N), diffraction pred diffuse +20% from N^{2beta0-1}, Coulomb Delta_H/N, persistence hole_gain=d0 — any explicit formula or 'must be measured' with bin output is valid control. If NO control at all, "
                "verdict REFUTED (no discriminator). "
                "(2) Does the mechanism also 'prove' an RH-false model? If the move "
                "fires on a control world, it is wrong (REFUTED). "
                "(3) Is the predicted number DERIVED or 'must be measured'? A claimed "
                "gap with no derivation and no script is a fabrication (REFUTED). "
                "(4) Is the label honest (PROVEN-able vs CHECKED NUMERICALLY vs measurement)? "
                "(5) Is the mechanism a BARE classical lane without a Jensen-circle-mean transfer hybrid AND not an ALIEN global probe? "
                "Bare lanes (d_N floors alone, bare Herglotz family, bare Laguerre, bare zero-search, bare dipole/prime-Euler moments) with NO Jensen mean E(c,r) transfer and not an alien 4-probe (kolmogorov_prime/diffraction_logp/coulomb_energy/persistence_zero which are N-body global invariants, not bare lanes): REFUTED. But hybrids that use Jensen circle-mean E(c,r) as a BRIDGE to Weil/Li/Beurling/Turan/de Branges (e.g., Weil-Jensen-Gram, Li-Jensen convolution, Turan heat-flow barrier via E-islands, Beurling-Mellin via E-islands, Weil explicit formula as error term O((log T)/X^{0.25}) inside a Jensen transfer) are LIVE — do NOT kill them. Alien 4 probes are LIVE via derived predictions above — do NOT kill them at (5) if they carry an alien control at (1). "
                "Explicit formula, Gram, Weil positivity, Beurling approximants, and location language ('zero location', 'pole') are ALLOWED when they appear inside a Jensen-transfer hybrid — kill only when they are the SOLE mechanism with no Jensen bridge. "
                "Never weaken a validator. "
                "Reply "
                'ONLY JSON: {"verdict": "VERIFIED|REFUTED|INCONCLUSIVE", '
                '"evidence": "one sentence naming the control or the kill"}.\n'
                f"CLAIM: {c['claim'][:900]}\nLABEL: {c['label']}\nSCRIPT: {c['script']}"
            )
            raw = _read_json(_safe_invoke(llm, prompt))
            v = (raw.get("verdict") or "INCONCLUSIVE").strip().upper()
            if v not in ("VERIFIED", "REFUTED", "INCONCLUSIVE"):
                v = "INCONCLUSIVE"
            # Never promote INCONCLUSIVE-label claims to VERIFIED even if LLM says so
            if c.get("label") in ("INCONCLUSIVE", "CONJECTURED") and v == "VERIFIED":
                v = "INCONCLUSIVE"
            new_verdicts.append({
                "claim_id": c["idea_id"], "verifier": f"verifier-{idx}",
                "verdict": v, "evidence": raw.get("evidence", raw.get("reason", "")),
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
    # Only CHECKED NUMERICALLY with VERIFIED counts as survivor (fix 3)
    verified = [c for c in state["claims"]
                if c.get("label") == "CHECKED NUMERICALLY"
                and any(v["claim_id"] == c["idea_id"] and v["verdict"] == "VERIFIED" for v in state["verdicts"])]
    if not verified:
        _write(state, "score.md", _dump_list("SCORES", ["(no CHECKED NUMERICALLY + VERIFIED survivors — all claims INCONCLUSIVE/CONJECTURED this wave)"]))
        return {"scores": []}
    prompt = (
        "Score each verified claim on impact x feasibility x verification "
        "strength (0-10 each). Reply ONLY JSON: "
        '{"scores": [{"claim_id": "...", "score": 7, "rationale": "..."}]}.\n'
        + "\n".join(f"{c['idea_id']} [{c.get('label','')}]: {c['claim'][:600]} cmd={c.get('cmd','')[:120]}" for c in verified)
    )
    scores = _read_json(_safe_invoke(llm, prompt)).get("scores", [])
    _write(state, "score.md", _dump_list("SCORES", [f"{s.get('claim_id')}: {s.get('score')} — {s.get('rationale','')}" for s in scores]))
    return {"scores": scores}


# ---------------------------------------------------------------------------
# Node: SYNTHESIZER
# ---------------------------------------------------------------------------

def synthesizer_node(state: SwarmState, config) -> dict:
    cfg = config["configurable"]
    llm = cfg["llm"]
    if not state["claims"]:
        return {"synthesis": "No claims survived this wave."}
    # Include verdict linkage and full claim text (truncation was wave-78 bug)
    # Build per-claim line with verdict to avoid "[SOURCE TRUNCATED]" synthesis
    def _claim_line(c):
        v = next((x["verdict"] for x in state["verdicts"] if x["claim_id"] == c["idea_id"]), "?")
        return f"[{c['label']}|{v}] {c['idea_id']} cmd={c.get('cmd','')[:100]}: {c['claim'][:600]}"
    prompt = (
        "Merge the wave's claims into one consolidated research note: headline "
        "result, labels (CHECKED vs INCONCLUSIVE), verdicts, the single next move. "
        "Honesty labels mandatory. If no CHECKED NUMERICALLY + VERIFIED survivor, say so explicitly — do not inflate CONJECTURED/INCONCLUSIVE to a result.\n"
        + "\n".join(_claim_line(c) for c in state["claims"][:6])
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
        f"SYNTHESIS: {state['synthesis'][:4000]}"
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
    # Serialize idea-gen fan-out: parallel LLM calls 429 the shared deepseek
    # endpoint (documented failure). Chain them to keep at most 1 in flight.
    for i in range(cfg["generators"]):
        src = "planner" if i == 0 else f"idea_gen_{i - 1}"
        g.add_edge(src, f"idea_gen_{i}")
    g.add_edge(f"idea_gen_{cfg['generators'] - 1}", "gate")
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
    # cargo run --bin <name> is special: check that the bin's Cargo.toml actually exists,
    # not just that `cargo` is on PATH (wave-79 bug: every `cargo run --bin <imaginary>`
    # returned True via `command -v cargo`, then failed with exit 101 "could not find Cargo.toml").
    import re as _re_bin
    m = _re_bin.search(r"cargo\s+run\s+.*--bin\s+([A-Za-z0-9_\-]+)", cmd)
    if m:
        bin_name = m.group(1)
        # search tools/*/Cargo.toml for that bin (or package name == bin_name)
        import fnmatch
        for manifest in RIEMANN.glob("tools/**/Cargo.toml"):
            try:
                text = manifest.read_text()
                if f'name = "{bin_name}"' in text or f"name = '{bin_name}'" in text:
                    return True
                # also check [[bin]] name entries
                if _re_bin.search(r'\[\[bin\]\][^\[]*name\s*=\s*["\']' + re.escape(bin_name) + r'["\']', text, flags=re.S):
                    return True
            except Exception:
                continue
        # also allow explicit --manifest-path in cmd itself
        if "--manifest-path" in cmd:
            return bool(subprocess.run(["bash", "-lc", f"command -v cargo"], capture_output=True, text=True).stdout.strip())
        return False
    exe = cmd.split()[0]
    return bool(subprocess.run(["bash", "-lc", f"command -v {exe}"], capture_output=True, text=True).stdout.strip())


def _run_rust(cmd: str, timeout: int) -> subprocess.CompletedProcess:
    # Fix Cargo.toml discovery: `cargo run --bin X` without --manifest-path fails when
    # cwd is repo root (no root Cargo.toml). Rewrite to use the bin's manifest path
    # if not already specified. Also enforce cheap-first: any cmd running > timeout
    # is killed and reported as INCONCLUSIVE (timeout), not hung.
    import re as _re_run
    if "cargo run" in cmd and "--manifest-path" not in cmd:
        m = _re_run.search(r"--bin\s+([A-Za-z0-9_\-]+)", cmd)
        if m:
            bin_name = m.group(1)
            for manifest in RIEMANN.glob("tools/**/Cargo.toml"):
                try:
                    text = manifest.read_text()
                    if f'name = "{bin_name}"' in text or _re_run.search(r'\[\[bin\]\][^\[]*name\s*=\s*["\']' + re.escape(bin_name) + r'["\']', text, flags=re.S):
                        # inject --manifest-path right after `cargo run`
                        cmd = cmd.replace("cargo run", f"cargo run --manifest-path {manifest}", 1)
                        break
                except Exception:
                    continue
    try:
        return subprocess.run(["bash", "-lc", cmd], capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        # Return a CompletedProcess-like object with non-zero code and timeout marker
        return subprocess.CompletedProcess(
            args=exc.cmd, returncode=124,
            stdout=(exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")) + f"\n[TIMEOUT after {timeout}s — cheap-first kill]",
            stderr=(exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or "")) + f"\n[TIMEOUT after {timeout}s]",
        )


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
    ap.add_argument("--frontier-file", type=str, default=None,
                    help="path to a file whose contents are used as --frontier (avoids shell quoting of leading dashes)")
    ap.add_argument("--model", type=str, default=DEFAULT_MODEL)
    ap.add_argument("--models", type=str, default=None,
                    help="comma-separated model ids cycled across generators/executors/verifiers "
                         "(fix: per-node models prevent generator collapse under a shared client)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.frontier_file:
        args.frontier = Path(args.frontier_file).read_text()
    wave = args.wave or _next_wave()
    if args.models:
        models = [m.strip() for m in args.models.split(",") if m.strip()]
        # distinct client per model id: diversity is the root-cause fix for collapse
        llms = {m: make_llm(m) for m in dict.fromkeys(models)}
        gen_models = [models[i % len(models)] for i in range(args.generators)]
        exec_models = [models[(args.generators + i) % len(models)] for i in range(args.executors)]
        ver_models = [models[(args.generators + args.executors + i) % len(models)] for i in range(args.verifiers)]
        cfg = {
            "llm": make_llm(args.model),  # default/planner/synth
            "gen_models": gen_models,
            "exec_models": exec_models,
            "ver_models": ver_models,
            "llms": llms,
            "generators": args.generators,
            "executors": args.executors,
            "verifiers": args.verifiers,
            "rust_timeout": args.rust_timeout,
        }
    else:
        cfg = {
            "llm": make_llm(args.model),
            "gen_models": [args.model] * args.generators,
            "exec_models": [args.model] * args.executors,
            "ver_models": [args.model] * args.verifiers,
            "llms": {},
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
        thread = {"configurable": {"thread_id": f"wave-{wave}", "llm": cfg["llm"],
                                   "gen_models": cfg["gen_models"], "exec_models": cfg["exec_models"],
                                   "ver_models": cfg["ver_models"], "llms": cfg["llms"],
                                   "generators": cfg["generators"],
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
