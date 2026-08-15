"""Campaign orchestrator CLI.

Usage (run from tools/campaign_orchestrator/):
    uv run orchestrator init                 # create/reset the checkpoint store
    uv run orchestrator step                 # advance the state machine one super-step
    uv run orchestrator status               # print current state (wave, phase, levers)
    uv run orchestrator report <lever> <status> [note]   # record a lever outcome
    uv run orchestrator kill <reason>        # log a kill event (audit trail)
    uv run orchestrator resume               # after a kill: print where we were + continue

The pi coordinator loop drives this: step -> read pending_dispatch -> launch subagents
with the subagent tool -> report lever outcomes -> step again. The SQLite checkpointer
makes every super-step durable; a killed process resumes by re-opening the same store.
"""

import argparse
import os
import sys

from langgraph.checkpoint.sqlite import SqliteSaver

from .state import initial_state
from .graph import build_graph

DB = os.environ.get("CAMPAIGN_DB", "/home/vstaln/riemann/tools/campaign_orchestrator/campaign.sqlite")
THREAD = "campaign"


def _saver():
    import sqlite3
    conn = sqlite3.connect(DB, check_same_thread=False)
    return SqliteSaver(conn), conn


def _graph(saver):
    return build_graph().compile(checkpointer=saver)


def cmd_init():
    with SqliteSaver.from_conn_string(DB) as saver:
        g = build_graph().compile(checkpointer=saver)
        cfg = {"configurable": {"thread_id": THREAD}}
        st = g.get_state(cfg)
        if st.values:
            print(f"checkpoint exists (wave={st.values.get('wave')}, phase={st.values.get('phase')}) — not resetting")
            return
        g.invoke(initial_state(), cfg)
        print("initialized campaign state (wave 0, DEFINE)")


def cmd_step():
    with SqliteSaver.from_conn_string(DB) as saver:
        g = build_graph().compile(checkpointer=saver)
        cfg = {"configurable": {"thread_id": THREAD}}
        st = g.get_state(cfg)
        if not st.values:
            print("no state — run `uv run orchestrator init` first")
            return 1
        # pass the current state back in as input (with a tick) so the entry node re-runs
        vals = dict(st.values)
        vals["_step"] = vals.get("_step", 0) + 1
        out = g.invoke(vals, cfg)
        print(f"wave={out.get('wave')} phase={out.get('phase')}")
        print(f"event: {out.get('last_event')}")
        pending = out.get("pending_dispatch") or []
        if pending:
            print("DISPATCH these levers (pi loop -> subagent tool):")
            for lv in pending:
                print(f"  - {lv['id']} (from {lv['brief']})")
        for lv in out.get("levers", []):
            print(f"  lever {lv['id']}: {lv.get('status')}" + (f" note={lv.get('note')}" if lv.get('note') else ""))
    return 0


def cmd_status():
    with SqliteSaver.from_conn_string(DB) as saver:
        g = build_graph().compile(checkpointer=saver)
        st = g.get_state({"configurable": {"thread_id": THREAD}})
        if not st.values:
            print("no state — run `uv run orchestrator init` first")
            return 1
        v = st.values
        print(f"wave={v.get('wave')} phase={v.get('phase')}")
        print(f"last_event: {v.get('last_event')}")
        print("levers:")
        for lv in v.get("levers", []):
            print(f"  {lv.get('id')}: {lv.get('status')}" + (f" note={lv.get('note')}" if lv.get('note') else ""))
        print("kill_log:")
        for k in v.get("kill_log", [])[-5:]:
            print(f"  {k}")
    return 0


def cmd_report(lever: str, status: str, note: str = ""):
    with SqliteSaver.from_conn_string(DB) as saver:
        g = build_graph().compile(checkpointer=saver)
        cfg = {"configurable": {"thread_id": THREAD}}
        st = g.get_state(cfg)
        if not st.values:
            print("no state — run init first")
            return 1
        levers = list(st.values.get("levers", []))
        found = False
        for lv in levers:
            if lv.get("id") == lever:
                lv["status"] = status
                if note:
                    lv["note"] = note
                found = True
        if not found:
            levers.append({"id": lever, "status": status, "note": note or ""})
        g.update_state(cfg, {"levers": levers, "phase": "MONITOR",
                             "last_event": f"report: lever {lever} -> {status}"})
        print(f"recorded lever {lever} -> {status}")
    return 0


def cmd_kill(reason: str):
    with SqliteSaver.from_conn_string(DB) as saver:
        g = build_graph().compile(checkpointer=saver)
        cfg = {"configurable": {"thread_id": THREAD}}
        st = g.get_state(cfg)
        kills = list(st.values.get("kill_log", []))
        kills.append({"event": "KILL", "reason": reason})
        g.update_state(cfg, {"kill_log": kills,
                             "last_event": f"KILLED: {reason}"})
        print("kill logged; run `uv run orchestrator resume` after restart")
    return 0


def cmd_resume():
    with SqliteSaver.from_conn_string(DB) as saver:
        g = build_graph().compile(checkpointer=saver)
        st = g.get_state({"configurable": {"thread_id": THREAD}})
        if not st.values:
            print("no state — run init first")
            return 1
        v = st.values
        print(f"RESUME from wave={v.get('wave')} phase={v.get('phase')}")
        print(f"last_event: {v.get('last_event')}")
        print("continuing: run `uv run orchestrator step`")
    return 0


def main():
    ap = argparse.ArgumentParser(prog="orchestrator")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init")
    sub.add_parser("step")
    sub.add_parser("status")
    sub.add_parser("resume")
    p = sub.add_parser("report")
    p.add_argument("lever")
    p.add_argument("status", choices=["PENDING", "DISPATCHED", "DONE", "DEAD", "INCONCLUSIVE", "RUNNING"])
    p.add_argument("note", nargs="?", default="")
    p = sub.add_parser("kill")
    p.add_argument("reason")
    args = ap.parse_args()
    fns = {"init": cmd_init, "step": cmd_step, "status": cmd_status, "resume": cmd_resume,
           "report": cmd_report, "kill": cmd_kill}
    fn = fns[args.cmd]
    if args.cmd == "report":
        return fn(args.lever, args.status, args.note)
    if args.cmd == "kill":
        return fn(args.reason)
    return fn()


if __name__ == "__main__":
    sys.exit(main())
