#!/usr/bin/env bash
# blaster.sh — fan out EVERY task spec in a directory across ALL cloud hosts,
# many concurrent agents per host (they're API-bound so concurrency is free).
# Usage: blaster.sh <specs-dir> [wave-name]
set -euo pipefail

SPECS_DIR="$1"
WAVE="${2:-wave-blast}"
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO"
mkdir -p "research/waves/$WAVE/results"

HOSTS=(kanaka2 oracle-old oracle-new)
SPECS=("$SPECS_DIR"/task-*.md)
echo "[blaster] $WAVE: ${#SPECS[@]} specs -> hosts: ${HOSTS[*]}"

# Deploy specs to all hosts once
for h in "${HOSTS[@]}"; do
  timeout 30 ssh -o ConnectTimeout=15 -o BatchMode=yes "$h" "mkdir -p ~/riemann/research/waves/$WAVE" 2>/dev/null || true
  timeout 60 scp -q "$SPECS_DIR"/task-*.md "$h":~/riemann/research/waves/$WAVE/ 2>/dev/null || true
done

# Launch every spec on a round-robin host, CONCURRENTLY
i=0
PIDS=()
for spec in "${SPECS[@]}"; do
  h="${HOSTS[$((i % ${#HOSTS[@]}))]}"
  tname="$(basename "$spec")"
  (
    # Copy spec to host, then run pi pointing at it (stdin drops >500 bytes)
    timeout 60 scp -q "$spec" "$h":~/riemann/"$WAVE/$tname" 2>/dev/null || true
    timeout 1800 ssh -o ConnectTimeout=15 -o BatchMode=yes "$h" \
      "export PATH=\"\$HOME/.npm-global/bin:\$HOME/.cargo/bin:/usr/bin:\$PATH\"; cd \"\$HOME/riemann\" 2>/dev/null || cd /tmp; \
       command -v pi >/dev/null || { echo 'PI NOT FOUND on $h'; exit 1; }; \
       pi -p --provider commandcode --model deepseek/deepseek-v4-flash \"Read the task spec at $WAVE/$tname and execute it completely. Write your deliverable file as instructed. Print RESULT: <status> — <summary> at the end.\"" \
      > "research/waves/$WAVE/results/$h--$tname.out" 2>&1
    echo "[blaster] DONE $h: $tname ($(wc -c < "research/waves/$WAVE/results/$h--$tname.out") bytes)"
  ) &
  PIDS+=($!)
  i=$((i+1))
done

echo "[blaster] launched ${#PIDS[@]} concurrent agents (pids: ${PIDS[*]})"
wait "${PIDS[@]}"
echo "[blaster] wave complete. Results in research/waves/$WAVE/results/"
ls -la "research/waves/$WAVE/results/" | tail -8
