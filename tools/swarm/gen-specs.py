#!/usr/bin/env python3
"""gen-specs.py — generate a batch of differentiated swarm task specs.

Each spec: distinct role + distinct s4h lens + distinct attack axis, all
sharing the mandatory preamble (hooks, s4h, honesty, Rust-first, write-back).

Usage: python gen-specs.py <out-dir> [count]
"""
import os, sys, textwrap

OUT = sys.argv[1] if len(sys.argv) > 1 else "research/waves/wave-blast"
COUNT = int(sys.argv[2]) if len(sys.argv) > 2 else 12
os.makedirs(OUT, exist_ok=True)

PREAMBLE = textwrap.dedent("""\
    # Task: {title} — role: {role} ({lens})

    You are an agent in the Riemann swarm. You MUST use s4h thinking.

    ## MANDATORY first steps
    1. Read /home/vstaln/riemann/hooks/agents.md — the persistence hook binds you:
       NEVER give up. A failure is a documented result, not a stop. Escalate:
       PLANNER -> EXECUTIONER -> VALIDATOR -> JUDGE -> SYNTHESIZER -> CRITIQUE.
    2. Read /home/vstaln/.pi/agent/skills/{skill}/SKILL.md and apply its methods.
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
    {task}

    ## Deliverable
    Write your deliverable to ~/riemann/research/waves/{wave}/results/{outfile}.md (create the dir if needed). The repo root on THIS machine is $HOME/riemann — use the absolute path. with your full
    findings (ideas, analysis, code outputs). Every quantitative claim cites its script+command.

    Print at end: RESULT: <status> — <one-line summary>
    """)

# (id, title, role, skill, task)
SPECS = [
    ("idea-analogy", "Idea gen: analogy transfer from X", "idea-generator", "s4h-analogy",
     "Generate 12-15 CONJECTURED attack ideas for RH by ANALOGY TRANSFER: import solutions from "
     "unrelated fields (random matrix theory, graph eigenvalues, sphere packing/Delsarte, error-"
     "correcting codes, statistical mechanics of zeros, quantum chaos, Boolean functions). For each: "
     "the analogous problem, the structural mapping, the concrete RH attack it suggests, and how to "
     "test it (Rust). Aim for NON-OBVIOUS transfers — not the standard ones."),
    ("idea-constraint", "Idea gen: constraint inversion on the 0.673 ceiling", "idea-generator", "s4h-constraint",
     "The bound saturates near 0.673. Identify the HARD CONSTRAINTS that limit it (the eps floor, "
     "the H window ceiling, the B/m block term, the 6-gap structure). For each, apply CONSTRAINT "
     "INVERSION: what if the constraint were the REQUIREMENT? Generate 10-15 CONJECTURED ideas that "
     "either remove, invert, or route around each constraint to push the bound toward 2/3 and beyond."),
    ("idea-provocation", "Idea gen: provocation / absurdity engine", "idea-generator", "s4h-creativity",
     "Use Edward de Bono PROVOCATION (Po): start from deliberately absurd statements about the zeros "
     "('all zeros are on a curve, not a line', 'the zeta function is a polynomial', 'the zeros form a "
     "lattice', 'RH is false and we can find the counterexample') and derive 10-15 CONJECTURED ideas. "
     "For each absurd provocation, extract the serious mathematical kernel and a concrete test."),
    ("idea-random", "Idea gen: random entry into RH", "idea-generator", "s4h-creativity",
     "Use RANDOM ENTRY: pick unrelated random words/concepts (e.g. 'vortex', 'auction', 'crystal', "
     "'economy', 'hurricane', 'clock', 'fractal', 'membrane') and force connections to the zeta zeros. "
     "Generate 10-15 CONJECTURED ideas. The randomness is the point — find the kernels that suggest "
     "non-obvious structure in the zeros."),
    ("idea-lateral", "Idea gen: lateral thinking on the certificate", "idea-generator", "s4h-creativity",
     "Apply LATERAL THINKING to the certificate machinery itself. The bound = (H - tau)/(1 - B/m). "
     "Escape the dominant pattern: what if we don't need the window functional at all? What if the "
     "local floor F >= eps is the wrong functional? What if a DIFFERENT 6-point configuration (not "
     "equally spaced) certifies a higher eps? Generate 10-15 CONJECTURED lateral moves."),
    ("idea-network", "Idea gen: zeros as a network", "idea-generator", "s4h-network",
     "Model the zeta zeros as a NETWORK (nodes = zeros, edges = correlations). Apply network analysis: "
     "centrality, contagion, community structure, weak ties. What would a 'community' of zeros mean? "
     "Could the pair-correlation structure be a network property that forces simple+on-line? Generate "
     "8-12 CONJECTURED ideas + how to test each with the zeros data in tools/data/."),
    ("idea-systems", "Idea gen: feedback/leverage on the bound", "idea-generator", "s4h-systems",
     "Apply SYSTEMS thinking to the bound formula. Map the feedback loops: eps floor feeds B, B feeds "
     "the denominator, H feeds the numerator, tau is a tax. Find the LEVERAGE POINT (Meadows): the "
     "smallest change that moves the bound most. Generate 10 CONJECTURED ideas targeting the highest-"
     "leverage parameter, with a Rust sensitivity analysis (partial derivatives of bound w.r.t. each "
     "parameter)."),
    ("idea-historical", "Idea gen: historical attack patterns", "idea-generator", "s4h-historical",
     "Study FAILURE ANALYSIS of past RH attacks: Levinson, Conrey, Bui-Conrey-Young, Feng, the 41.6% "
     "wall, and the 2026 67.25% breakthrough. What recurring failure modes killed previous attacks? "
     "What did the 67.25% breakthrough do DIFFERENTLY? Extract the transferable principle and generate "
     "8-12 CONJECTURED ideas that exploit the pattern (read research/notes/literature-map.md, "
     "attack-vector-catalog*.md, and any papers in research/papers/)."),
    ("idea-probability", "Idea gen: probabilistic structure of zeros", "idea-generator", "s4h-probability",
     "Model the zeros as a random process (Montgomery pair correlation = GUE). What does the PROBABILITY "
     "structure imply for simple-on-line proportions? Base-rate anchor: what fraction of a GUE matrix's "
     "eigenvalues are simple? Generate 8-12 CONJECTURED ideas connecting the probabilistic model to the "
     "certified bound machinery, and how to test with tools/zeta-rs paircorr."),
    ("verify-eps", "Executor: certify a higher eps at (alpha=1.49, psum=1/220)", "executor", "s4h-investigation",
     "The record has eps=0.00806 at (alpha=1.49, psum=1/220). Investigate whether a HIGHER eps is "
     "certifiable at this exact (alpha, psum) — i.e. was the original floor search complete? Use the "
     "rigorous verifier: cd ~/riemann/tools/beat673 && uv run --with python-flint python verify_cos7.py "
     "149 100 1 1320 <target_num> 1000000. Binary-search the max target that verifies (start 8060, try "
     "8061, 8065, 8070, 8100...). ALSO test alpha=1.49 with psum=1/225 and 1/215. Report the max "
     "certified eps for each and the resulting bound. This is the cheapest possible win."),
    ("verify-window2", "Executor: two-tone window v=cos(a s)+c cos(b s)", "executor", "s4h-constraint",
     "Implement in Rust the H-functional for two-tone windows v(s)=cos(a s)+c cos(b s) on [-1/2,1/2] "
     "(generalize the I0, I2, J integrals; derive them symbolically or numerically with rigorous bounds). "
     "Sweep (a, b, c, psum, m) to find configurations beating 0.6732628655343560. The H functional is "
     "the lever — a window with higher H(alpha) directly raises the bound. Report top candidates + the "
     "H values. CONJECTURED until interval-verified."),
    ("verify-ntone", "Executor: n-point generalization beyond 7", "executor", "s4h-constraint",
     "The bound used n=7 (6 gaps). trmdy mentioned n=9/11. Implement the n-point generalized deduction "
     "(F_n(g) = p sum g_i + sum_{i<j} a_ij w(y_j-y_i) >= eps, uniform weights a_ij = 2/(n-(j-i))) in "
     "Rust, sweep (n, eps, m, alpha, psum), and find configurations beating 0.6732628655343560. Read "
     "research/ladder-f-family/threshold.py for the exact formula. Report top candidates."),
]

# Cycle through the SPECS list, repeating if count > len
os.makedirs(OUT, exist_ok=True)
written = 0
for i in range(COUNT):
    sid, title, role, skill, task = SPECS[i % len(SPECS)]
    wave = os.path.basename(OUT)
    content = PREAMBLE.format(title=title, role=role, lens=skill, skill=skill,
                              task=task, wave=wave, outfile=sid)
    with open(f"{OUT}/task-{sid}.md", "w") as f:
        f.write(content)
    written += 1
print(f"generated {written} task specs in {OUT}/")
