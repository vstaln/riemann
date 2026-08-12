#!/usr/bin/env bash
# pull-discoveries.sh — pull cloud-agent discoveries back to local and commit.
# For each host, rsync/scp the agent's research notes + results into local
# research/waves/<host>/ and commit any new discoveries.
#
# Usage: pull-discoveries.sh [wave-dir]
set -euo pipefail

WAVE_DIR="${1:-research/waves}"
LOCAL_REPO="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$LOCAL_REPO"
mkdir -p "$WAVE_DIR"

CLOUD_HOSTS=(kanaka2 oracle-old oracle-new)

for h in "${CLOUD_HOSTS[@]}"; do
  echo "=== pulling from $h ==="
  DEST="$WAVE_DIR/$h"
  mkdir -p "$DEST"

  # Pull any wave results + notes the agent wrote
  for sub in research/notes research/waves; do
    timeout 60 ssh -o ConnectTimeout=15 -o BatchMode=yes "$h" \
      "ls ~/riemann/$sub 2>/dev/null | head -100" 2>/dev/null | grep -vE "WARNING|may be|server may|openssh|bind|channel_setup|Could not request|store now|post-quantum|vulnerable" \
      | while read -r f; do
        # Only pull files newer than our copy or absent locally
        if [ ! -f "$sub/$f" ] || timeout 30 ssh -o ConnectTimeout=15 "$h" "stat -c %Y ~/riemann/$sub/$f" 2>/dev/null | grep -qv "^$(stat -c %Y "$sub/$f" 2>/dev/null || echo 0)$"; then
          timeout 30 scp -q -r "$h":~/riemann/"$sub/$f" "$sub/" 2>/dev/null || true
        fi
      done
  done

  # Pull any discovery notes (marked with DISCOVERY or in notes/)
  echo "--- $h notes pulled to $sub/"
done

# Commit anything new
git add -A "$WAVE_DIR" research/notes 2>/dev/null || true
if ! git diff --cached --quiet; then
  git commit -q -m "swarm: pulled discoveries from cloud hosts" --allow-empty
  echo "[pull] committed new material"
else
  echo "[pull] nothing new"
fi
