# Task: Executor: certify a higher eps at (alpha=1.49, psum=1/220) — role: executor (s4h-investigation)

You are an agent in the Riemann swarm. You MUST use s4h thinking.

## MANDATORY first steps
1. Read /home/vstaln/riemann/hooks/agents.md — the persistence hook binds you:
   NEVER give up. A failure is a documented result, not a stop. Escalate:
   PLANNER -> EXECUTIONER -> VALIDATOR -> JUDGE -> SYNTHESIZER -> CRITIQUE.
2. Read /home/vstaln/.pi/agent/skills/s4h-investigation/SKILL.md and apply its methods.
3. Read /home/vstaln/riemann/research/notes/discovery-6732629.md (the certified
   67.3263% record) and /home/vstaln/riemann/research/notes/attack-vector-catalog*.md

## RUST-FIRST (mandatory)
All computational code in Rust: export PATH=$HOME/.cargo/bin:$PATH
RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes"
cargo build --release --target x86_64-unknown-linux-musl
(Python mpmath ONLY for quick exploration, never the final computation.)

## Honesty labels (mandatory)
PROVEN / CHECKED NUMERICALLY (script+command) / CONJECTURED / ABANDONED / INCONCLUSIVE.
Never fabricate. A wrong confident result is worse than none.

## The task
The record has eps=0.00806 at (alpha=1.49, psum=1/220). Investigate whether a HIGHER eps is certifiable at this exact (alpha, psum) — i.e. was the original floor search complete? Use the rigorous verifier: cd ~/riemann/tools/beat673 && uv run --with python-flint python verify_cos7.py 149 100 1 1320 <target_num> 1000000. Binary-search the max target that verifies (start 8060, try 8061, 8065, 8070, 8100...). ALSO test alpha=1.49 with psum=1/225 and 1/215. Report the max certified eps for each and the resulting bound. This is the cheapest possible win.

## Deliverable
Write your deliverable to ~/riemann/research/waves/wave-blast/results/verify-eps.md (create the dir if needed). The repo root on THIS machine is $HOME/riemann — use the absolute path. with your full
findings (ideas, analysis, code outputs). Every quantitative claim cites its script+command.

Print at end: RESULT: <status> — <one-line summary>
