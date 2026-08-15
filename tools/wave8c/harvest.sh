#!/bin/sh
# waits for the full chain (ddgram -> followup), then digests results for review
cd /home/vstaln/riemann
while pgrep -f run_hiN_followup > /dev/null 2>&1; do sleep 120; done
sleep 5
{
  echo "=== wave8c hiN harvest $(date -Is) ==="
  grep -E '^\[prod (2000|3000|5000)\] (d_f64|d_ref|gram sampling|d_mpfr|RESULT)' tools/wave8c/results/hiN_log.txt | sort -u
  echo "--- ddgram ---"
  grep -E '^\[ddgram 2000\]' tools/wave8c/results/hiN_log.txt | sort -u
  echo "--- samples ---"
  grep -E '^\[sample' tools/wave8c/results/hiN_log.txt | sort -u
} > tools/wave8c/results/HARVEST.txt
echo done >> tools/wave8c/results/HARVEST.txt
