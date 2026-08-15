"""Campaign orchestration graph.

The wave loop as a checkpointed state machine. Each `invoke` (one `step`) runs a
bounded pipeline that TERMINATES and returns control to the pi coordinator:

    define -> dispatch -> monitor -> consolidate -> END

State fields drive the transitions:
  phase: DEFINE | DISPATCH | MONITOR | CONSOLIDATE | DONE | WAIT
  wave:  current wave number

Coordinator contract per wave:
  1. write research/notes/wave<N>-briefs-*.md
  2. `step`  -> graph detects briefs, queues levers in pending_dispatch, phase=DISPATCH
  3. pi loop launches subagents from pending_dispatch (subagent tool, background)
  4. as agents land, `report <lever> DONE <note>` (or DEAD / INCONCLUSIVE)
  5. `step`  -> monitor marks landed levers DONE; when all done -> phase=CONSOLIDATE
  6. `step`  -> consolidate writes the synthesis pointer, phase=DONE (waits for
     coordinator to actually write wave<N>-synthesis-*.md)
  7. `step`  -> define sees synthesis exists -> advances wave (phase=DEFINE, next wave)

Kill-robustness by construction: the SqliteSaver checkpointer persists after every
super-step; `resume` + `step` continues exactly where the process died.
"""

import os
import re
from typing import Any, Dict

from langgraph.graph import StateGraph, END

from .state import CampaignState

log = logging = __import__("logging").getLogger("orchestrator")

NOTES_DIR = os.environ.get("RIEMANN_NOTES", "/home/vstaln/riemann/research/notes")


def _list_notes() -> list:
    try:
        return sorted(os.listdir(NOTES_DIR))
    except FileNotFoundError:
        return []


def _briefs_for(wave: int) -> list:
    return [f for f in _list_notes() if re.match(rf"wave{wave}-briefs", f)]


def _synthesis_for(wave: int) -> list:
    return [f for f in _list_notes() if re.match(rf"wave{wave}-synthesis", f)]


def _lever_docs_for(wave: int) -> list:
    """Deliverable notes for a wave: wave<N>-<anything> but NOT briefs/synthesis."""
    return [f for f in _list_notes()
            if re.match(rf"wave{wave}-", f)
            and "brief" not in f and "synthesis" not in f]


def _parse_lever_ids(wave: int) -> list:
    """Lever ids from the briefs file sections (## LEVER 8A / ## 8A / ## LEVER 8A — ...)."""
    ids = []
    for fn in _briefs_for(wave):
        path = os.path.join(NOTES_DIR, fn)
        try:
            with open(path) as f:
                txt = f.read()
        except OSError:
            continue
        for m in re.finditer(r"^#{2,4}\s*(?:LEVER|lever|JOINT|joint)?\s*([0-9A-Za-z]{1,3})\b", txt, re.M):
            ids.append(m.group(1))
    # dedupe, keep order
    seen = set()
    return [x for x in ids if not (x in seen or seen.add(x))]


def _max_briefs_wave() -> int:
    """Highest wave<N> with a briefs file on disk."""
    m = 0
    for f in _list_notes():
        mm = re.match(r"wave(\d+)-briefs", f)
        if mm:
            m = max(m, int(mm.group(1)))
    return m


def node_define(state: CampaignState) -> CampaignState:
    wave = state.get("wave", 0)
    phase = state.get("phase", "DEFINE")
    # fresh start: jump to the highest wave with briefs on disk
    if wave == 0 and _max_briefs_wave() > 0:
        wave = _max_briefs_wave()
        return {**state, "wave": wave, "phase": "DEFINE",
                "last_event": f"fresh start: jumping to wave {wave}"}
    if phase == "DONE" and _synthesis_for(wave):
        # advance to next wave
        wave += 1
        return {**state, "wave": wave, "phase": "DEFINE",
                "last_event": f"advancing to wave {wave}"}
    if not _briefs_for(wave) and not _synthesis_for(wave):
        return {**state, "phase": "WAIT",
                "last_event": f"wave {wave}: no briefs yet — coordinator writes wave{wave}-briefs-*.md"}
    if _briefs_for(wave) and not _lever_docs_for(wave):
        return {**state, "phase": "DISPATCH",
                "last_event": f"wave {wave}: briefs found, queuing levers"}
    # levers already dispatched/landing
    return {**state, "phase": "MONITOR",
            "last_event": f"wave {wave}: levers in flight"}


def node_dispatch(state: CampaignState) -> CampaignState:
    wave = state.get("wave", 0)
    known = {lv.get("id") for lv in state.get("levers", [])}
    ids = [i for i in _parse_lever_ids(wave) if i not in known]
    levers = list(state.get("levers", []))
    if ids:
        levers += [{"id": i, "brief": _briefs_for(wave)[0], "status": "PENDING"} for i in ids]
    # pending = levers not yet launched (pi loop reports DISPATCHED after launching)
    pending = [lv for lv in levers if lv.get("status") == "PENDING"]
    return {**state, "levers": levers, "pending_dispatch": pending, "phase": "MONITOR",
            "last_event": f"wave {wave}: {len(pending)} lever(s) queued for dispatch"}


def node_monitor(state: CampaignState) -> CampaignState:
    wave = state.get("wave", 0)
    levers = list(state.get("levers", []))
    docs = _lever_docs_for(wave)
    for lv in levers:
        if lv.get("status") not in ("DONE", "DEAD", "INCONCLUSIVE"):
            hit = [f for f in docs if lv.get("id", "") in f]
            if hit:
                lv["status"] = "DONE"
                lv["note"] = hit[0]
    statuses = {lv.get("status") for lv in levers if lv.get("wave", wave) == wave}
    active = [lv for lv in levers if lv.get("status") in ("PENDING", "DISPATCHED", "RUNNING")]
    if active:
        return {**state, "levers": levers, "phase": "MONITOR",
                "last_event": f"wave {wave}: {len(active)} lever(s) still in flight"}
    return {**state, "levers": levers, "phase": "CONSOLIDATE",
            "last_event": f"wave {wave}: all levers resolved"}


def node_consolidate(state: CampaignState) -> CampaignState:
    wave = state.get("wave", 0)
    return {**state, "phase": "DONE",
            "last_event": f"wave {wave} resolved — coordinator writes wave{wave}-synthesis-*.md, then step()"}


def _route_define(state: CampaignState) -> str:
    return END if state.get("phase") == "WAIT" else "dispatch"


def _route_monitor(state: CampaignState) -> str:
    return END if state.get("phase") == "MONITOR" else "consolidate"


def build_graph():
    g = StateGraph(CampaignState)
    g.add_node("define", node_define)
    g.add_node("dispatch", node_dispatch)
    g.add_node("monitor", node_monitor)
    g.add_node("consolidate", node_consolidate)
    g.add_conditional_edges("define", _route_define, {END: END, "dispatch": "dispatch"})
    g.add_edge("dispatch", "monitor")
    g.add_conditional_edges("monitor", _route_monitor, {END: END, "consolidate": "consolidate"})
    g.add_edge("consolidate", END)
    g.set_entry_point("define")
    return g
