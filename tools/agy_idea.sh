#!/usr/bin/env bash
# agy_idea.sh — agy one-shot ideation WITH memory of dead levers.
# Prepends research/notes/DEAD-LEVERS.md to the task prompt so agy never
# re-proposes a closed lane without saying why its version escapes.
#
# Usage: agy_idea.sh <task-prompt-file> [timeout-sec] [out-file]
set -u
PROMPT_FILE="${1:?usage: agy_idea.sh <task-prompt-file> [timeout-sec] [out-file]}"
TIMEOUT="${2:-300}"
OUT="${3:-$(mktemp /tmp/agy_idea_XXXXXX.out)}"
DIGEST="/home/vstaln/riemann/research/notes/DEAD-LEVERS.md"
COMBINED="$(mktemp /tmp/agy_idea_XXXXXX.txt)"
{
  echo "=== STANDING CONTEXT: TRIED AND DEAD (you must not re-propose these; if your idea touches one, prove why it escapes) ==="
  cat "$DIGEST"
  echo
  echo "=== TASK ==="
  cat "$PROMPT_FILE"
} > "$COMBINED"
AGY_RUN_OUT="$OUT" bash /home/vstaln/riemann/tools/agy_run.sh "$COMBINED" "$TIMEOUT"
rc=$?
rm -f "$COMBINED"
exit $rc
