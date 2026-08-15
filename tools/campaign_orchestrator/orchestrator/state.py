"""Campaign orchestrator state schema.

The campaign runs as a checkpointed LangGraph state machine. Every node reads and
writes this state; the SQLite checkpointer persists it after every super-step, so a
killed coordinator process resumes exactly where it left off (no state lost).

State fields:
  wave:            current wave number (int)
  phase:           DEFINE | DISPATCH | MONITOR | CONSOLIDATE | REFEREE | DONE
  levers:          list of lever dicts (the roster, append-only)
  kill_log:        ring buffer of kill/resume events (audit trail)
  last_event:      human-readable summary of the last step
  pending_dispatch: levers queued for dispatch in this wave (consumed by pi loop)
"""

from typing import TypedDict, List, Dict, Any


class CampaignState(TypedDict, total=False):
    wave: int
    phase: str
    levers: List[Dict[str, Any]]
    kill_log: List[Dict[str, Any]]
    last_event: str
    pending_dispatch: List[Dict[str, Any]]
    _step: int


def initial_state() -> CampaignState:
    return {
        "wave": 0,
        "phase": "DEFINE",
        "levers": [],
        "kill_log": [],
        "last_event": "initialized",
        "pending_dispatch": [],
    }
