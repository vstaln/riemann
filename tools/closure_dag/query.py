#!/usr/bin/env python3
"""closure_dag query tool.

Usage:
    status                     -> every lever verdict + trap class
    query <idea-text>          -> fuzzy check: does any closed lever/trap kill this idea?
    traps                      -> list the RH-equivalence trap classes
    frontier                   -> active frontier items
    deps <lever-id>            -> outgoing/incoming edges for a lever
    path <lever-a> <lever-b>   -> path between two levers (if any)
"""
import json, os, sys, difflib

DAG = os.path.join(os.path.dirname(__file__), "closure_dag.json")
d = json.load(open(DAG))
levers = d["levers"]; edges = d["edges"]; traps = d["_meta"]["trap_classes"]

def find(id_or_frag):
    for lv in levers:
        if lv["id"] == id_or_frag: return lv
    for lv in levers:
        if id_or_frag.lower() in lv["id"].lower(): return lv
    return None

def cmd_status():
    print(f"{'lever':<26}{'verdict':<32}{'trap'}")
    for lv in levers:
        print(f"{lv['id']:<26}{lv.get('verdict','')[:30]:<32}{lv.get('trap_class','')}")
    print("\nTrap classes (consistency-only / dead):", ", ".join(traps))

def cmd_query(text):
    tl = text.lower()
    hits = []
    # 1) trap-class keyword check
    for t in traps:
        if any(k in tl for k in t.replace("-"," ").split()):
            hits.append(("TRAP", t, "this idea belongs to an RH-equivalence / dead class"))
    # 2) closed-lever fuzzy match
    for lv in levers:
        if lv["verdict"].startswith("DEAD") or "REFUTED" in lv["verdict"] or lv["verdict"].startswith("INVALID"):
            score = difflib.SequenceMatcher(None, tl, lv["id"].lower()).ratio()
            if score > 0.5:
                hits.append(("CLOSED-LEVER", lv["id"], f"{lv['verdict']} — {lv['claim'][:120]}"))
    # 3) edge: reach any 'refutes' from a closed lever
    if not hits:
        for e in edges:
            if e["type"] in ("refutes","implies_trap"):
                if any(k in tl for k in e["to"].lower().replace("-"," ").split()):
                    hits.append(("EDGE", e["from"]+" -> "+e["to"], e.get("note","")[:120]))
    if not hits:
        print(f"No closure hit for: {text!r}\n(Mark as genuinely-open candidate OR check CAMPAIGN-STATE.md before dispatch.)")
    else:
        print(f"Closure hit(s) for {text!r}:")
        for kind, name, note in hits:
            print(f"  [{kind}] {name}\n      {note}")

def cmd_frontier():
    for f in d.get("active_frontier", []):
        print(f"{f['id']} [{f['status']}] agent={f.get('agent','')}\n   {f['question']}")

def cmd_deps(lid):
    lv = find(lid)
    if not lv: print("no lever", lid); return
    print(f"{lv['id']}: {lv['verdict']}\n  {lv['claim'][:200]}\n")
    for e in edges:
        if e["from"]==lv["id"]: print(f"  -> {e['to']}  ({e['type']})  {e.get('note','')}")
        if e["to"]==lv["id"]:   print(f"  <- {e['from']} ({e['type']})  {e.get('note','')}")

def cmd_path(a, b):
    la, lb = find(a), find(b)
    adj = {}
    for e in edges:
        adj.setdefault(e["from"], []).append(e["to"])
    seen=set(); q=[(la["id"],[la["id"]])]
    while q:
        n,p=q.pop(0)
        if n==lb["id"]: print(" -> ".join(p)); return
        if n in seen: continue
        seen.add(n)
        for nx in adj.get(n,[]): q.append((nx,p+[nx]))
    print(f"no path {la['id']} -> {lb['id']}")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args: cmd_status()
    elif args[0]=="status": cmd_status()
    elif args[0]=="query": cmd_query(" ".join(args[1:]))
    elif args[0]=="traps": print(", ".join(traps))
    elif args[0]=="frontier": cmd_frontier()
    elif args[0]=="deps" and len(args)>1: cmd_deps(args[1])
    elif args[0]=="path" and len(args)>2: cmd_path(args[1],args[2])
    else: print(__doc__)
