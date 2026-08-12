#!/bin/bash
# phone-worker.sh — runs ON THE LAPTOP (as vstaln): ssh to a box and run pi -p there,
# feeding the spec via stdin (phone -> pc-jump -> laptop -> box). Stable route.
# usage: phone-worker.sh <box> [timeout]
BOX="$1"
TIMEOUT="${2:-2700}"
export PATH="$HOME/.npm-global/bin:$HOME/.cargo/bin:/usr/bin:$PATH"
command -v ssh >/dev/null || { echo "ssh missing"; exit 1; }
timeout "$TIMEOUT" ssh -o BatchMode=yes -o ConnectTimeout=15 "$BOX" \
  "export PATH=\"\$HOME/.npm-global/bin:/usr/bin:\$PATH\"; cd ~/riemann 2>/dev/null || cd /tmp; \
   command -v pi >/dev/null || { echo 'PI NOT FOUND on $BOX'; exit 1; }; \
   pi -p --provider commandcode --model deepseek/deepseek-v4-flash"
