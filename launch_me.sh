#!/bin/bash
# Launch eps-floor probes at alpha=1.49 p=1/1320 (psum=1/220), grid=4000
export PATH=/home/vstaln/.local/bin:$PATH
cd /tmp/combine
for t in 8060 8065 8066; do
  (uv run --quiet --with python-flint python3 verify_cos7.py 149 100 1 1320 $t 1000000 - 4000 > /tmp/me$t.log 2>&1) &
done
echo LAUNCHED_ME
