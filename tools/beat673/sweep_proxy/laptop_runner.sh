#!/usr/bin/env bash
# ============================================================================
# LAPTOP RUNNER — weight-profile sweep (candidate C1), grid-4000 confirmation
# ============================================================================
# Runs verify_cos7.py on a given weights JSON at a given target eps and grid.
# The phone's proot python has python-flint, so this same script also works
# on the phone; it is written so the orchestrator can execute it on the
# laptop (void, 192.168.1.50) at full grid 4000 without needing ssh here.
#
# Usage:
#   ./laptop_runner.sh <weights.json> <target_num> <target_den> <grid> [shard shard_count]
#   ./laptop_runner.sh weights/span3_ends2.json 8095 1000000 4000
#
# Exit code 0 => verified=True (certified); 1 => verified=False; 2 => error.
# ============================================================================
set -u
WEIGHTS="${1:?weights json}"
TARGET_NUM="${2:?target num}"
TARGET_DEN="${3:?target den}"
GRID="${4:-4000}"
SHARD="${5:-0}"
SHARD_COUNT="${6:-1}"
ALPHA_NUM=149; ALPHA_DEN=100; P_NUM=1; P_DEN=1320
DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$DIR/.." && pwd)"
cd "$DIR"

OUT=$(timeout 10800 python3 "$ROOT/verify_cos7.py" \
  "$ALPHA_NUM" "$ALPHA_DEN" "$P_NUM" "$P_DEN" \
  "$TARGET_NUM" "$TARGET_DEN" "$WEIGHTS" "$GRID" \
  "$SHARD" "$SHARD_COUNT" 2>&1)
rc=$?
echo "$OUT"
if [ $rc -ne 0 ]; then echo "RUNNER: verifier exit $rc"; exit 2; fi
if echo "$OUT" | grep -q "verified=True"; then
  echo "RUNNER: CERTIFIED target $TARGET_NUM/$TARGET_DEN grid $GRID"
  exit 0
else
  echo "RUNNER: FAILED target $TARGET_NUM/$TARGET_DEN grid $GRID"
  exit 1
fi
