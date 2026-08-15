#!/bin/sh
# sequential bounded runs; every phase appends kill-safe to results/hiN_log.txt
cd /home/vstaln/riemann
B=./tools/wave8c/target/release/hiN
for N in 2000 3000 5000; do
  echo "== prod $N start $(date -Is) ==" >> tools/wave8c/results/hiN_log.txt
  $B prod $N >> tools/wave8c/results/hiN_log.txt 2>> tools/wave8c/results/prod_stderr.log
  echo "== prod $N exit=$? $(date -Is) ==" >> tools/wave8c/results/hiN_log.txt
done
echo "== ddgram 2000 start $(date -Is) ==" >> tools/wave8c/results/hiN_log.txt
$B ddgram 2000 >> tools/wave8c/results/hiN_log.txt 2>> tools/wave8c/results/prod_stderr.log
echo "== ddgram 2000 exit=$? $(date -Is) ==" >> tools/wave8c/results/hiN_log.txt
