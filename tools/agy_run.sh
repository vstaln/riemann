#!/usr/bin/env bash
# agy_run.sh — reliable wrapper for the agy CLI in the riemann campaign.
#
# Why this exists (issues fixed, 2026-08-19):
#   * `--print-timeout` is misparsed by agy's CLI (it became a user message).
#   * `--mode plan` is intercepted by the ponytail plugin (wrong "mode" doc).
#   * `--disable-slash-commands` is treated as a prompt ("I will refrain...").
#   * Agentic tool-search hangs (prompts referencing repo paths trigger searches).
# So: plain `agy --print "<self-contained prompt>"` with shell timeout is the ONLY
# reliable invocation. This wrapper enforces that and gives a clean exit/retry.
#
# Usage: agy_run.sh <prompt-file> [timeout-seconds]
#   writes stdout to $OUT (default /tmp/agy_run.out), stderr to $OUT.err
set -u
PROMPT_FILE="${1:?usage: agy_run.sh <prompt-file> [timeout-seconds]}"
TIMEOUT="${2:-480}"
OUT="${AGY_RUN_OUT:-/tmp/agy_run.out}"

if [ ! -s "$PROMPT_FILE" ]; then echo "ERROR: prompt file empty/missing: $PROMPT_FILE" >&2; exit 2; fi

# Pre-check auth cheaply (avoids wasting a long timeout on an auth prompt).
if ! timeout 60 agy --effort high -p "Say OK only." >/dev/null 2>&1; then
  echo "AGY_AUTH_FAIL: agy not authenticated (or endpoint down). User must re-auth." >&2
  exit 3
fi

echo "AGY_RUN: invoking agy --print (timeout ${TIMEOUT}s)..." >&2
timeout "$TIMEOUT" agy --effort high -p "$(cat "$PROMPT_FILE")" > "$OUT" 2> "$OUT.err"
rc=$?
if [ $rc -ne 0 ]; then
  echo "AGY_RUN_FAIL: rc=$rc. stderr tail:" >&2
  tail -3 "$OUT.err" >&2 || true
  exit 1
fi
echo "AGY_RUN_OK: $(wc -l < "$OUT") lines -> $OUT" >&2
exit 0
