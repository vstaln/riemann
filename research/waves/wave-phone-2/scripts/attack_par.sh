#!/bin/bash
cd /tmp/combine
UV=/home/vstaln/.local/bin/uv
run() {
  local tag=$1; shift
  echo "[$(date +%H:%M:%S)] RUN $tag: $*" >> /tmp/combine/attack_results2.txt
  timeout 1500 $UV run --quiet --with python-flint python3 verify_cos7.py "$@" >> /tmp/combine/attack_results2.txt 2>&1
  echo "[$(date +%H:%M:%S)] DONE $tag rc=$?" >> /tmp/combine/attack_results2.txt
}
echo "=== attack run2 (parallel) start $(date) ===" > /tmp/combine/attack_results2.txt
run eps8065_g4000 149 100 1 1320 8065 1000000 - 4000 &
P1=$!
run eps8066_g6000 149 100 1 1320 8066 1000000 - 6000 &
P2=$!
run eps8068_g6000 149 100 1 1320 8068 1000000 - 6000 &
P3=$!
run eps8070_g6000 149 100 1 1320 8070 1000000 - 6000 &
P4=$!
run eps8065_g6000 149 100 1 1320 8065 1000000 - 6000 &
P5=$!
run eps8066_g8000 149 100 1 1320 8066 1000000 - 8000 &
P6=$!
wait $P1 $P2 $P3 $P4 $P5 $P6
echo "=== attack run2 (parallel) done $(date) ===" >> /tmp/combine/attack_results2.txt
