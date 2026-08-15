#!/bin/sh
# serial follow-up: wait for ddgram (driver) to finish, then complete the prod matrix
cd /home/vstaln/riemann
B=./tools/wave8c/target/release/hiN
LOG=tools/wave8c/results/hiN_log.txt
while kill -0 8392 2>/dev/null; do sleep 60; done
echo "== followup start $(date -Is) ==" >> $LOG
if ! grep -q 'mpfr-chol SKIPPED' $LOG || ! grep -q '\[prod 2000\] d_mpfr' $LOG; then
  echo "== prod 2000 (followup) start $(date -Is) ==" >> $LOG
  $B prod 2000 >> $LOG 2>> tools/wave8c/results/prod_stderr.log
  echo "== prod 2000 exit=$? ==" >> $LOG
fi
echo "== prod 5000 (followup) start $(date -Is) ==" >> $LOG
$B prod 5000 >> $LOG 2>> tools/wave8c/results/prod_stderr.log
echo "== prod 5000 exit=$? ==" >> $LOG
timeout 600 $B sample 5000 >> $LOG 2>&1
echo "== sample 5000 done ==" >> $LOG
