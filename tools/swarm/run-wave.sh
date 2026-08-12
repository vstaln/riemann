#!/usr/bin/env bash
# run-wave.sh — fan out a wave of task specs to local + cloud agents in parallel.
# Usage:
#   run-wave.sh <wave-dir>
# Where <wave-dir> contains task-*.md files. Each task file's basename is passed
# to one agent: local subagents for 50% and cloud hosts (kanaka2, oracle-old, oracle-new)
# round-robin for the rest.
#
# Results land in <wave-dir>/results/<agent>--<task>.out
set -euo pipefail

WAVE="$1"
[ -d "$WAVE" ] || { echo "wave dir $WAVE missing"; exit 1; }
mkdir -p "$WAVE/results"

CLOUD_HOSTS=(kanaka2 oracle-old oracle-new)
TASKS=("$WAVE"/task-*.md)
echo "[wave] $WAVE: ${#TASKS[@]} tasks, hosts: ${CLOUD_HOSTS[*]}"

# Copy task specs to each host so they can read them
for h in "${CLOUD_HOSTS[@]}"; do
  timeout 30 ssh -o ConnectTimeout=15 -o BatchMode=yes "$h" "mkdir -p ~/riemann/research/waves/$(basename "$WAVE")" 2>/dev/null || true
  scp -q "$WAVE"/task-*.md "$h":~/riemann/research/waves/$(basename "$WAVE")/ 2>/dev/null || true
done

# Launch each task on a cloud host (round-robin) in background
i=0
declare -A PIDS
for t in "${TASKS[@]}"; do
  h="${CLOUD_HOSTS[$((i % ${#CLOUD_HOSTS[@]}))]}"
  tname="$(basename "$t")"
  (
    timeout "${SWARM_TIMEOUT:-900}" ssh -o ConnectTimeout=15 -o BatchMode=yes "$h" \
      "export PATH=\"\$HOME/.npm-global/bin:\$HOME/.local/bin:\$PATH\"; \
       cd \"\$HOME/riemann\"; \
       cat \"research/waves/$(basename "$WAVE")/$tname\" | \
       pi -p --provider commandcode --model deepseek/deepseek-v4-flash" \
      > "$WAVE/results/$h--$tname.out" 2>&1
    echo "[wave] $h done: $tname"
  ) &
  PIDS["$h--$tname"]=$!
  i=$((i+1))
done

# Wait for all
for k in "${!PIDS[@]}"; do wait "${PIDS[$k]}"; done
echo "[wave] all done. Results in $WAVE/results/"
ls -la "$WAVE/results/" | tail -5
