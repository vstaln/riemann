# Task: Executor: n-point generalization beyond 7 — role: executor (s4h-constraint)

You are an agent in the Riemann swarm. You MUST use s4h thinking.

## MANDATORY first steps
1. Read /home/vstaln/riemann/hooks/agents.md — the persistence hook binds you:
   NEVER give up. A failure is a documented result, not a stop. Escalate:
   PLANNER -> EXECUTIONER -> VALIDATOR -> JUDGE -> SYNTHESIZER -> CRITIQUE.
2. Read /home/vstaln/.pi/agent/skills/s4h-constraint/SKILL.md and apply its methods.
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
The bound used n=7 (6 gaps). trmdy mentioned n=9/11. Implement the n-point generalized deduction (F_n(g) = p sum g_i + sum_{i<j} a_ij w(y_j-y_i) >= eps, uniform weights a_ij = 2/(n-(j-i))) in Rust, sweep (n, eps, m, alpha, psum), and find configurations beating 0.6732628655343560. Read research/ladder-f-family/threshold.py for the exact formula. Report top candidates.

## Deliverable
Write your deliverable to ~/riemann/research/waves/wave-blast/results/verify-ntone.md (create the dir if needed). The repo root on THIS machine is $HOME/riemann — use the absolute path. with your full
findings (ideas, analysis, code outputs). Every quantitative claim cites its script+command.

Print at end: RESULT: <status> — <one-line summary>
