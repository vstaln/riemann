#!/bin/sh
cd /home/vstaln/riemann
B=./tools/wave8c/target/release/hiN
LOG=tools/wave8c/results/hiN_log.txt
n=0
while kill -0 8392 2>/dev/null; do
  n=$((n+1))
  if [ $((n % 10)) -eq 0 ]; then echo "heartbeat: still waiting for ddgram (8392), ${n}min $(date -Is)" >> tools/wave8c/results/followup.log; fi
  sleep 60
done
echo "== followup start $(date -Is) ==" >> $LOG
if ! grep -q '[prod 2000] d_mpfr' $LOG; then
  echo "== prod 2000 (followup) start $(date -Is) ==" >> $LOG
  $B prod 2000 >> $LOG 2>> tools/wave8c/results/prod_stderr.log
  echo "== prod 2000 exit=$? ==" >> $LOG
fi
echo "== prod 5000 (followup) start $(date -Is) ==" >> $LOG
$B prod 5000 >> $LOG 2>> tools/wave8c/results/prod_stderr.log
echo "== prod 5000 exit=$? ==" >> $LOG
timeout 900 $B sample 5000 >> $LOG 2>&1
echo "== sample 5000 done ==" >> $LOG
echo "== followup done $(date -Is) ==" >> tools/wave8c/results/followup.log
