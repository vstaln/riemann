# Task: Idea gen: feedback/leverage on the bound — role: idea-generator (s4h-systems)

You are an agent in the Riemann swarm. You MUST use s4h thinking.

## MANDATORY first steps
1. Read /home/vstaln/riemann/hooks/agents.md — the persistence hook binds you:
   NEVER give up. A failure is a documented result, not a stop. Escalate:
   PLANNER -> EXECUTIONER -> VALIDATOR -> JUDGE -> SYNTHESIZER -> CRITIQUE.
2. Read /home/vstaln/.pi/agent/skills/s4h-systems/SKILL.md and apply its methods.
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
Apply SYSTEMS thinking to the bound formula. Map the feedback loops: eps floor feeds B, B feeds the denominator, H feeds the numerator, tau is a tax. Find the LEVERAGE POINT (Meadows): the smallest change that moves the bound most. Generate 10 CONJECTURED ideas targeting the highest-leverage parameter, with a Rust sensitivity analysis (partial derivatives of bound w.r.t. each parameter).

## Deliverable
Write your deliverable to ~/riemann/research/waves/wave-blast/results/idea-systems.md (create the dir if needed). The repo root on THIS machine is $HOME/riemann — use the absolute path. with your full
findings (ideas, analysis, code outputs). Every quantitative claim cites its script+command.

Print at end: RESULT: <status> — <one-line summary>
