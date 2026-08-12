# Task: Higher-moment structural theory (THEORIST — s4h-analogy)

You are a THEORIST agent in the Riemann swarm. You MUST use s4h thinking.

## MANDATORY first steps
1. Read /home/vstaln/riemann/hooks/agents.md — persistence hook binds you; escalate through the round protocol.
2. Read /home/vstaln/.pi/agent/skills/s4h-analogy/SKILL.md and s4h-systems/SKILL.md — apply domain transfer + leverage analysis.
3. Read /home/vstaln/riemann/research/notes/discovery-6732629.md, attack-vector-catalog*.md, lean-stability-inequality.md

## Your task: understand why the bound saturates at ~0.673, and find structural upgrades
The bound uses: rank-trace inequality ||P+Q||_F² ≥ 4·tr(P+Q) - 3r - 4b + tr Psi(M) (ainta), window functional H, block defect/Bellman coboundary, local 6-gap floor F ≥ eps.

RUST-FIRST: all computational code in Rust ($HOME/.cargo/bin, RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes", target x86_64-unknown-linux-musl).

Investigate (s4h-analogy: what OTHER fields solve this structure?):
1. WHAT LIMITS the bound at 0.673? Which term: eps floor? H window? B/m block term? the 6-gap structure? (compute the sensitivity of each in Rust)
2. HIGHER MOMENTS: if we used ||P+Q||_F^4 (trace of square) or tr(P^k), what would the bound formula become? Sketch the deduction (CONJECTURED).
3. ANALOGY TRANSFER: random matrix theory, graph eigenvalues, sphere packing (Delsarte), error-correcting codes — what constraints on "atoms must be orthogonal" are analogous? Can a Delsarte-style linear programming bound raise eps?
4. THEORETICAL CEILING: what is the max possible bound of this rank-trace family? Can it reach 2/3? 0.7? (CONJECTURED but argue why)

Write /home/vstaln/riemann/research/waves/wave-1/results/moment-theory.md:
- Limiting-term analysis (with Rust-computed sensitivities, CHECKED NUMERICALLY)
- Higher-moment deduction sketch (CONJECTURED)
- Analogy transfers (CONJECTURED)
- 3-5 concrete next moves ranked by expected impact

Print at end: RESULT: <status> — <one-line summary>
