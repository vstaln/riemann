# Task: Mini-Orchestrator — run your own subagent swarm (ROLE: ORCHESTRATOR)

You are a MINI-ORCHESTRATOR agent in the Riemann swarm. Your job is to spawn YOUR OWN subagents
(you have the subagent tool — spawn isolated agents that run inside your pi runtime), have them
do the research, and SYNTHESIZE their results into one deliverable.

## MANDATORY first steps
1. Read /home/vstaln/riemann/hooks/agents.md — persistence hook binds you and ALL your subagents:
   NEVER give up; a failure is a documented result; escalate through
   PLANNER -> EXECUTIONER -> VALIDATOR -> JUDGE -> SYNTHESIZER.
2. Read /home/vstaln/.pi/agent/skills/s4h/SKILL.md — the master orchestration skill: design a
   multi-skill reasoning workflow and execute it sequentially.
3. Read /home/vstaln/riemann/research/notes/discovery-6732629.md (certified 67.3263% record),
   /home/vstaln/riemann/research/notes/attack-vector-catalog*.md, /home/vstaln/riemann/research/notes/ladder-convergence.md

## RUST-FIRST (mandatory for all subagents)
All computational code in Rust: export PATH=$HOME/.cargo/bin:$PATH
RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" cargo build --release --target x86_64-unknown-linux-musl

## YOUR TASK (orchestrate, don't do it all yourself)
Spawn 4-6 subagents IN PARALLEL (use subagent tool, run_in_background where possible), each with a
distinct role, each instructed to read hooks/agents.md + one s4h skill + the discovery note:

1. IDEA-GEN subagent (s4h-creativity): 10-15 CONJECTURED attack ideas, diverse
2. IDEA-GEN subagent (s4h-analogy): analogies from other fields
3. EXECUTOR subagent (s4h-constraint): probe the window/parameter frontier (Rust) — is a higher
   bound reachable at nearby (alpha, psum)?
4. VERIFIER subagent (s4h-investigation): adversarial check on the record — can it be broken?
5. THEORIST subagent (s4h-systems): what limits the bound at 0.673? leverage analysis

Each subagent writes its findings to /home/vstaln/riemann/research/waves/wave-orch/results/{name}.md.

## THEN synthesize
After collecting subagent results, write YOUR synthesis to
/home/vstaln/riemann/research/waves/wave-orch/results/orch-1-synthesis.md:
- Top 5 ideas ranked by expected impact (with reasons)
- Any verified bound improvements
- The single most promising next move
- Honesty labels everywhere (PROVEN / CHECKED NUMERICALLY / CONJECTURED)

Print at end: RESULT: <status> — <one-line summary>

## YOUR SPECIFIC FOCUS
push the certified bound: subagents explore window functions, n-point generalizations, and higher eps floors in Rust; verify any candidate that beats 0.6732628655343560 with tools/beat673/verify_cos7.py
