# PHONE-BRAIN CONTRACT — the phone orchestrates; laptop+boxes are workers

**Architecture (decided 2026-08-12):** this phone (pi agent + pi-subagents) is the **only brain** —
it decides what to fund, writes every spec, judges every wave, and does the synthesis. The laptop
and the 3 cloud boxes are **compute workers only**: they run exactly the jobs the phone dispatches
and nothing else. No autonomous swarms anywhere (the laptop swarm is off; it stays off).

## Roles
| node | role | runs |
|---|---|---|
| **phone** (this) | brain: fund/kill, specs, ledger, judge, synthesize | pi subagents, light python |
| **laptop** (`pc-jump`) | worker: Rust interval verifier, bound-sweep, big numerics | dispatched jobs only (su vstaln -c '...') |
| **boxes** kanaka2 / oracle-old / oracle-new | workers: pi agents + heavy compute | phone-dispatch.sh only |

## Rules (all agents and dispatches bind to these)
1. **No work without a funded line.** The ledger (`research/notes/ledger.md`) is the gate. A line is
   funded only when it has a CERTIFIED-payoff path or a documented kill/learn outcome. Idea catalogs
   are not results — UNFUNDED by default.
2. **Ledger protocol:** every completed agent appends a ≤5-line verdict (result, labels, file, next
   move). New agents read ONLY the ledger + their task slice — never the full wave archive.
3. **Waves:** ≤3 agents per wave. One JUDGE after each wave (cheap agent or the brain itself) reads
   the ledger, prunes, funds the next ≤2 lines.
4. **Dispatch contract:** box agents run only via `tools/swarm/phone-dispatch.sh` (timeout always,
   spec via stdin, output tee'd to the wave's results/, results pulled back to the phone repo). Boxes
   never launch anything on their own.
5. **Laptop:** compute jobs only (`ssh pc-jump "su vstaln -c '...'"`). The laptop's interactive agent
   session (the user's) is off-limits — the phone does not touch it.
6. **Ponytail + honesty charter bind everywhere** (`hooks/agents.md`): smallest probe that decides;
   reuse-before-write; labels PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE.
7. **Token budget per wave:** logged in the ledger; target < 2M tokens per wave (was ~100M+ per wave).

## How to dispatch (phone side)
```sh
# agent job on a box: spec in research/waves/<wave>/, results come back to research/waves/<wave>/results/
tools/swarm/phone-dispatch.sh launch <wave> <spec-file> <host> [timeout]
# pull results back from a box (routes via the laptop)
tools/swarm/phone-dispatch.sh pull <wave> <host>
```
Laptop compute job:
```sh
proot-distro login ubuntu -- bash -lc 'ssh pc-jump "su vstaln -c '\''cd /home/vstaln/riemann && <command>'\''"'
```
