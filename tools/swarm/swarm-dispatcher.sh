#!/usr/bin/env bash
# swarm-dispatcher.sh — run a swarm task spec on a cloud pi agent.
# Usage: swarm-dispatcher.sh <host> <task-spec-file> [workdir]
#
# FIX (2026-08-12): pi -p via stdin drops input >~500 bytes. Instead we
# (1) scp the spec to the remote as ~/riemann/<spec-name>, then
# (2) call pi with a short instruction pointing at the file.
set -euo pipefail

HOST="$1"
SPEC="$2"
WORKDIR="${3:-riemann}"          # relative to $HOME on the remote

SPEC_NAME="$(basename "$SPEC")"
RESULT_DIR="$(dirname "$SPEC")/results"
mkdir -p "$RESULT_DIR"
OUT="$RESULT_DIR/${HOST}--${SPEC_NAME%.md}.out"
PI_OPTS="${PI_OPTS:---provider commandcode --model deepseek/deepseek-v4-flash}"

echo "[swarm] $HOST <- $SPEC_NAME (workdir: ~/$WORKDIR)"
# 1. Copy the spec to the remote repo
timeout 60 scp -q "$SPEC" "$HOST":~/"$WORKDIR/$SPEC_NAME" 2>&1 | grep -vE "WARNING|may be|server may|openssh|bind|channel_setup|Could not request|store now|post-quantum|vulnerable" | head -1 || true
# 2. Run pi pointing at the spec file
timeout "${SWARM_TIMEOUT:-1800}" ssh -o ConnectTimeout=15 -o BatchMode=yes "$HOST" \
  "export PATH=\"\$HOME/.npm-global/bin:\$HOME/.cargo/bin:/usr/bin:\$PATH\"; cd \"\$HOME/$WORKDIR\" 2>/dev/null || cd /tmp; \
   command -v pi >/dev/null || { echo 'PI NOT FOUND on $HOST'; exit 1; }; \
   pi -p $PI_OPTS \"Read the task spec at $WORKDIR/$SPEC_NAME and execute it completely. Write your deliverable file as instructed in the spec. Print RESULT: <status> — <summary> at the end.\"" \
  > "$OUT" 2>&1 || { echo "[swarm] $HOST FAILED (see $OUT)"; tail -5 "$OUT"; exit 1; }

echo "[swarm] $HOST done -> $OUT ($(wc -c < "$OUT") bytes)"
