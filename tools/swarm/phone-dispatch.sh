#!/bin/bash
# phone-dispatch.sh — phone (brain) dispatches ONE funded agent job to a cloud worker.
# Usage:
#   phone-dispatch.sh launch <wave> <spec-file> <host> [timeout]
#   phone-dispatch.sh pull   <wave> <host>
#
# launch: scp the spec to the box, run pi -p feeding the spec via stdin, tee output to
#   research/waves/<wave>/results/<host>--<spec>.out  (box-local results dir: ~/riemann/research/waves/<wave>/results/)
# pull:   copy the box's results dir back to the phone repo, routing through the laptop (pc-jump),
#   because phone->box direct scp is flaky.
#
# Contract: ONLY run for ledger-funded lines (see research/notes/ledger.md + tools/swarm/phone-brain.md).
# Always set a timeout. Boxes never spawn on their own.
set -euo pipefail
cd /root/riemann

cmd="${1:-}"; WAVE="${2:-}"; SPEC="${3:-}"; HOST="${4:-}"; TIMEOUT="${5:-1800}"

case "$cmd" in
  launch)
    [ -n "$WAVE" ] && [ -n "$SPEC" ] && [ -n "$HOST" ] || { echo "usage: launch <wave> <spec> <host> [timeout]"; exit 1; }
    mkdir -p "research/waves/$WAVE/results"
    timeout 40 ssh -o ConnectTimeout=15 -o BatchMode=yes "$HOST" "mkdir -p ~/riemann/research/waves/$WAVE/results" 2>/dev/null || true
    timeout 60 scp -q -o ConnectTimeout=15 "research/waves/$WAVE/$SPEC" "$HOST":~/riemann/research/waves/$WAVE/ 2>/dev/null || { echo "scp spec failed"; exit 1; }
    timeout "$TIMEOUT" ssh -o ConnectTimeout=15 -o BatchMode=yes "$HOST" \
      "export PATH=\"\$HOME/.npm-global/bin:\$HOME/.cargo/bin:/usr/bin:\$PATH\"; cd \"\$HOME/riemann\" 2>/dev/null || cd /tmp; \
       command -v pi >/dev/null || { echo 'PI NOT FOUND on $HOST'; exit 1; }; \
       pi -p --provider commandcode --model deepseek/deepseek-v4-flash" < "research/waves/$WAVE/$SPEC" \
      > "research/waves/$WAVE/results/$HOST--$SPEC.out" 2>&1
    echo "launched $SPEC -> $HOST (timeout $TIMEOUT). Log: research/waves/$WAVE/results/$HOST--$SPEC.out"
    ;;
  pull)
    [ -n "$WAVE" ] && [ -n "$HOST" ] || { echo "usage: pull <wave> <host>"; exit 1; }
    mkdir -p "research/waves/$WAVE/results"
    # via laptop: box -> laptop /tmp, laptop -> phone repo
    timeout 60 ssh -o ConnectTimeout=15 -o BatchMode=yes pc-jump \
      "su vstaln -c 'scp -q -r $HOST:~/riemann/research/waves/$WAVE/results/. /tmp/wave-pull/ 2>/dev/null || true; mkdir -p /tmp/wave-pull'" 2>/dev/null || true
    timeout 60 rsync -e "ssh -o ConnectTimeout=15 -o BatchMode=yes" -az pc-jump:/tmp/wave-pull/ "research/waves/$WAVE/results/" 2>/dev/null || true
    echo "pulled $HOST results for $WAVE:"
    ls -la "research/waves/$WAVE/results/" | tail -5
    ;;
  *)
    echo "usage: phone-dispatch.sh {launch|pull} ..."; exit 1;;
esac
