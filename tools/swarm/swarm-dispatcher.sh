#!/usr/bin/env bash
# swarm-dispatcher.sh — run a swarm task spec on one or more cloud pi agents.
# Usage:
#   swarm-dispatcher.sh <host> <task-spec-file> [workdir]
# Example:
#   swarm-dispatcher.sh kanaka2 /home/vstaln/riemann/research/waves/wave-1/task-idea-A.md
#
# Runs:  ssh <host> "cd <workdir> && cat <spec> | pi -p --provider commandcode --model deepseek/deepseek-v4-flash"
# and saves the output to a results file next to the spec.
set -euo pipefail

HOST="$1"
SPEC="$2"
WORKDIR="${3:-riemann}"          # relative to $HOME on the remote

SPEC_NAME="$(basename "$SPEC")"
RESULT_DIR="$(dirname "$SPEC")/results"
mkdir -p "$RESULT_DIR"
OUT="$RESULT_DIR/${HOST}--${SPEC_NAME%.md}.out"

# PI_OPTS: allow provider/model override via env
PI_OPTS="${PI_OPTS:---provider commandcode --model deepseek/deepseek-v4-flash}"

echo "[swarm] $HOST <- $SPEC_NAME  (workdir: ~/$WORKDIR)"
timeout "${SWARM_TIMEOUT:-600}" ssh -o ConnectTimeout=15 -o BatchMode=yes "$HOST" \
  "export PATH=\"\$HOME/.npm-global/bin:\$HOME/.local/bin:\$PATH\"; cd \"\$HOME/$WORKDIR\" 2>/dev/null || cd /tmp; \
   cat '$SPEC_NAME' 2>/dev/null | pi -p $PI_OPTS" \
  > "$OUT" 2>&1 || { echo "[swarm] $HOST FAILED (see $OUT)"; tail -5 "$OUT"; exit 1; }

echo "[swarm] $HOST done -> $OUT ($(wc -c < "$OUT") bytes)"
