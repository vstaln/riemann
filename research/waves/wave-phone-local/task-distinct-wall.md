# Task: FOURTH-MOMENT ATTACK on the 5/6 distinct-zeros wall

You are an INVESTIGATOR in the Riemann swarm. Context, verified by the program:
- The known result: ≥ 5/6 of the nontrivial zeros are DISTINCT (from the same Weil-form compression: m² ≥ 2m−1 and m² ≥ 3m−2 integrality steps).
- The program's finding: the 5/6 distinct wall is ROBUST to the third moment — identical on both test worlds (the "RH-true world" and the generic world). The separation between the worlds is a FOURTH-MOMENT phenomenon.
- The program has an Ihara-zeta sandbox (tools/ihara-sandbox, Rust): graphs whose Ihara zeta function is PROVABLY RH-true, used as a "rigidity meter" — the certificate family is a meter, not an RH-meter.

## MANDATORY first steps
1. Read ~/riemann/hooks/agents.md (charter, honesty labels, Rust-first rule).
2. Read ~/riemann/research/notes/attack-ihara-sandbox.md, attack-xiprime2-tower.md, paper-sixthmoment.md, lean-stability-inequality.md (skim; read fully only what you need).
3. Inspect tools/ihara-sandbox/ (Cargo.toml, main) to learn the sandbox API.

## Your task
On provably-RH-true sandbox objects, determine whether a FOURTH-MOMENT inequality can separate the distinct-zero fraction from the generic world — i.e., push the "distinct" bound above 5/6 where the third moment could not.

Specifically:
1. **Fourth-moment integrality step.** The rank–trace argument uses integrality steps m² ≥ 2m−1, m² ≥ 3m−2. Derive (CONJECTURED) the fourth-moment analogue: for a Hermitian PSD block of size m with the compression structure, what inequality on m⁴ (or tr(P⁴)) holds? Sketch the deduction; state the resulting bound formula if the step goes through.
2. **Numerical probe (CHECKED NUMERICALLY — script + output).** In the sandbox (or a small self-built model if the sandbox is absent), compute for RH-true graphs and for random/generic graphs:
   - the empirical distinct-zero fraction on the line,
   - the size of the fourth-moment defect |tr(P⁴) − f(m)| compared with the third-moment defect |tr(P³) − g(m)|,
   - whether the fourth-moment defect separates the two worlds.
   Report exact numbers with the script.
3. **Rust-first**: any CPU-bound computation in Rust (export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes", target x86_64-unknown-linux-musl). Small exploratory scripts may use uv run --quiet python.
4. If the fourth moment DOES separate: quantify how far the distinct bound can move (CONJECTURED bound + numerical evidence). If it does NOT: document the negative precisely — a documented negative is a result.

## Deliverable
Write ~/riemann/research/waves/wave-phone-local/results/distinct-wall-4th.md:
- The fourth-moment deduction sketch (CONJECTURED), the numerical probe with script+output (CHECKED NUMERICALLY), the verdict (does it break the 5/6 wall? how far?), and 3 concrete next moves ranked by impact.

Print at end: RESULT: <status> — <one-line summary>
