# Task: Extend the rigorous verifier to two-tone windows (EXECUTOR — highest priority)

You are an EXECUTOR agent in the Riemann swarm. This is the SINGLE HIGHEST-VALUE task right now.

## MANDATORY first steps
1. Read /home/vstaln/riemann/hooks/agents.md — persistence hook: NEVER give up; a failure is a documented result; try a different route.
2. Read /home/vstaln/.pi/agent/skills/s4h-constraint/SKILL.md and s4h-investigation/SKILL.md.
3. Read /home/vstaln/riemann/research/notes/discovery-6732629.md — the record: bound 0.6732628655343560 from (alpha=1.49, psum=1/220, m=133, eps=0.00806).

## THE FINDING TO CERTIFY (from exec-two-tone.md)
The two-tone executor found: window v(s) = cos(1.407s) + 0.005·cos(2.53s), psum=1/300, m=135 gives
H = 0.672500703285 and bound = 0.6745091758911242 — a potential +1.25e-3 over the record.
BUT: eps=0.00806 was ASSUMED achievable for this window (CONJECTURED). The current verifier
(tools/beat673/verify_cos7.py) only handles PURE COSINE windows — its kernel is
k_alpha(x) = (sinc(pi x - a) + sinc(pi x + a)) / (2 sinc(a)), w = k_alpha^2.

## YOUR TASK: extend verify_cos7.py to two-tone windows
The window v(s) = cos(a·s) + c·cos(b·s) on [-1/2,1/2] has kernel:
  k(x) = K(x)/K(0) where K(x) = ∫_{-1/2}^{1/2} [cos(a t) + c cos(b t)]·cos(2 pi x t) dt
  (the window enters through its Fourier cosine transform).
Work out K(x) in closed form (it's a sum of sinc terms), then generalize the verifier:
- The kernel tables w(x) = k(x)^2 and its second derivative must use the two-tone K
- The local 6-gap floor F = p·sum g_i + sum_{i<j} a_ij w(y_j-y_i) then uses the two-tone w
- Everything else (subdivision, pruning, LDL checks) stays the same

Build it as a COPY: cp -r tools/beat673/verify_cos7.py tools/beat673/verify_twotone7.py then modify.
Do NOT break the original.

## THEN verify the finding
Run your two-tone verifier on the winning config: alpha a=1.407, b=2.53, c=0.005,
per-gap pressure p = (1/300)/6 = 1/1800, target eps = 8060/1e6 (and binary-search the max).
If it verifies eps >= 0.00806, recompute the bound — that's a NEW RECORD to report.

## Deliverable
Write /home/vstaln/riemann/research/waves/wave-local/results/exec-twotone-verify.md:
- The closed-form K(x) for two-tone (show your derivation)
- The verifier changes (what you modified)
- The verification result: does (a=1.407, b=2.53, c=0.005, psum=1/300, eps=0.00806) verify?
- Max verified eps and the resulting bound (CHECKED NUMERICALLY — cite exact command + output)
- Honesty labels: "verified" means PROVEN (interval-certified); "beats record" only if verified
Print at end: RESULT: <status> — <one-line summary>

If the two-tone window certifies eps >= 0.00806, we have a new certified record ~0.67451. This is the breakthrough the whole swarm is after.