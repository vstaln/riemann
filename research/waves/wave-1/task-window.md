# Task: Window-functional frontier (EXECUTOR — s4h-constraint + s4h-creativity)

You are an EXECUTOR agent in the Riemann swarm. You MUST use s4h thinking.

## MANDATORY first steps
1. Read /home/vstaln/riemann/hooks/agents.md — persistence hook binds you: NEVER give up; a failure is a documented result; try a different route (different precision, formulation, direction).
2. Read /home/vstaln/.pi/agent/skills/s4h-constraint/SKILL.md and s4h-creativity/SKILL.md — apply constraint inversion + provocation to the window problem.
3. Read /home/vstaln/riemann/research/notes/discovery-6732629.md and /home/vstaln/riemann/research/notes/ladder-convergence.md

## Your task: push the certified bound beyond 0.6732628655343560
The bound = (H(alpha) - tau)/(1 - B/m). The record used v(s)=cos(1.49s), psum=1/220, m=133, eps=0.00806.

RUST-FIRST: all computational code in Rust ($HOME/.cargo/bin). Build flags:
  RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" cargo build --release --target x86_64-unknown-linux-musl

Explore NEW WINDOW FUNCTIONS beyond cosine:
- Two-tone: v(s) = cos(a·s) + c·cos(b·s)
- Gaussian-like: v(s) = exp(-d·s²)
- v(s) = cos^p(a·s)
For each: compute H (window functional) in Rust (formula: I0=2 sin(a)/a, I2=1/2+sin(alpha)/(2 alpha), J=-2 I2/alpha² + (sin(a)/alpha + 2 cos(a)/alpha²)·I0, c=I0²/(I2+J), H=2-1/c with a=alpha/2), estimate achievable eps, compute bound = (H-tau)/(1-B/m), compare to 0.6732628655343560.

Write /home/vstaln/riemann/research/waves/wave-1/results/window-frontier.md:
- Table of candidates (window, params, H, eps_est, bound)
- Best candidate + how to certify it (run: cd ~/riemann/tools/beat673 && uv run --with python-flint python verify_cos7.py <alpha_num> <alpha_den> <p_num> <p_den> <target_num> 1000000)
- Honesty labels: numbers CHECKED NUMERICALLY (cite script+command); "beats record" CONJECTURED until interval verifier confirms.

Print at end: RESULT: <status> — <one-line summary>
