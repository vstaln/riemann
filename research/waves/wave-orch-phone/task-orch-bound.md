# Task: Mini-Orchestrator — run your own subagent swarm (ROLE: ORCHESTRATOR — FOCUS: push the certified bound)

You are a MINI-ORCHESTRATOR agent in the Riemann swarm. Your job is to spawn YOUR OWN subagents
(you have the subagent tool — spawn isolated agents), have them research, and SYNTHESIZE their
results into ONE deliverable. You orchestrate; you do not do everything yourself.

## MANDATORY first steps
1. Read ~/riemann/hooks/agents.md — the persistence hook binds you AND all your subagents:
   never give up; a failure is a documented result; escalate PLANNER → EXECUTIONER → VALIDATOR → JUDGE → SYNTHESIZER.
   Honesty labels mandatory: PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE.
2. Read ~/riemann/research/notes/discovery-6732629.md (the certified 0.6732628655343560 record: [RETIRED 2026-08-24]
   cosine window α=1.49, psum=1/220, block m=133, floor F≥0.00806, H=0.6724218860964,
   bound=(H−τ)/(1−B/m)) and skim attack-vector-catalog*.md so you don't duplicate tried ideas.

## YOUR FOCUS: push the certified lower bound
Subagents explore: (a) window functions beyond cos(αs) that raise H without lowering the certifiable
floor ε; (b) n-point / higher-ε floor structures; (c) nearby (α, psum) parameter frontier — is
anything strictly better than α=1.49, psum=1/220? Any candidate that beats 0.6732628655343560 must be [RETIRED 2026-08-24]
certified rigorously (interval arithmetic; Rust if available, else mpmath with strict error bounds).

## SPAWN 4–6 SUBAGENTS IN PARALLEL (subagent tool, run_in_background where possible)
1. IDEA-GEN (s4h-creativity): 10–15 CONJECTURED ideas for raising the bound, diverse
2. IDEA-GEN (s4h-analogy): analogies from other fields (Delsarte/LP, sphere packing, RMT)
3. EXECUTOR (s4h-constraint): numerical probe of nearby (α, psum, window) — run real computations,
   CHECKED NUMERICALLY with script+output
4. VERIFIER (s4h-investigation): adversarial check on the 0.67326 record — try to break it with
   independent code; also try to break any new candidate
5. THEORIST (s4h-systems): what limits the bound at 0.673? leverage analysis; what is the tightest
   achievable in-class constant and what exactly blocks it?

Each subagent: read ~/riemann/hooks/agents.md first; write findings to
~/riemann/research/waves/wave-orch-phone/results/{subagent-name}.md; print RESULT: <status> — <one line>.

## ENVIRONMENT (this may be a cloud box or a phone — adapt)
- Repo at ~/riemann. Python: python3 (if Rust/cargo is NOT available, use python3/mpmath with strict
  error bounds and SAY the rigor scheme; do not attempt Rust builds if cargo is missing).
- CPU-bound work that is large: use Rust if cargo exists (export PATH=$HOME/.cargo/bin:$PATH
  RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes", target x86_64-unknown-linux-musl).
- Do NOT edit canonical tools/ — copy to /tmp or a new dir, say where the code lives.

## THEN SYNTHESIZE
Write ~/riemann/research/waves/wave-orch-phone/results/orch-bound-synthesis.md:
- Top 5 ideas ranked by expected impact (with reasons)
- Any verified bound improvement (exact number + certificate)
- The single most promising next move
- Honesty labels everywhere

Print at end: RESULT: <status> — <one-line summary>
