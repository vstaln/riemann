# Barrier zoo — Rust port (tools/barrier_zoo_rs)

Status: IN PROGRESS (partial note; refined as the port lands). All numbers below come from
the Rust binary, never from memory.

## Purpose
Rung-0 barrier checker: model worlds where RH provably fails, to catch "proves too much"
claims. Python reference at tools/barrier_zoo/ (read-only). This note documents the Rust
port at tools/barrier_zoo_rs/ (single binary, subcommands dh|weil|epstein|beurling|classify|all).

## Model 2 — Davenport–Heilbronn (PRIORITY)
Certified reference facts (from Python reference, model_dh.py + common.py):
- psi mod 5, psi(2)=i:  psi = [0, 1, i, -i, -1] over a=0..4; psibar = [0, 1, -i, i, -1].
- f(s) = L(s,psi) + c·L(s,psibar), c = +-eps, eps = GaussSum/(i·sqrt(5)), |eps|=1.
- L(s,chi) = q^-s · sum_{a=1}^{q-1} chi(a)·zeta(s, a/q)  (Hurwitz zeta; q=5).
- FE: Phi(s) = (5/pi)^((s+1)/2) · Gamma((s+1)/2) · f(s),  Phi(s) = +Phi(1-s) for c=+eps,
  -Phi(1-s) for c=-eps (checked at s=0.4+it, t in {0.3,1.7,5.1,12.7}).
- Certified off-line zeros of f_plus (50 dps): s = 0.80851718245663737319 + i·85.699348485377592166
  and s = 0.65083008060973707137 + i·114.16334273075698091.
- Search params: sigma [0.02, 0.98] step 0.05, t [0, 130] step 0.5, rel_thresh 0.3, v<0.5;
  Newton: h = 1e-8·(1+|z|) imaginary step, df = (f(z+ih)-f(z-ih))/(2ih), tol 1e-14, maxit 60;
  certify |f| < 1e-9; offline = |Re-1/2| > 1e-5; dedupe gap 1e-4.
- t_hi=40 was the ORIGINAL BUG (finds zero off-line zeros). Must search t_hi>=130.

Implementation plan: Hurwitz zeta via Euler–Maclaurin ported from tools/argprinciple/src/zeta.rs
(same scaled-product Bernoulli trick, sum from n=0 with offset a, N=~100-150, K=~12-20),
complex Gamma via Lanczos (g=7, n=9) + reflection. Self-tests: zeta(2,1)=pi^2/6,
zeta(2,1/2)=pi^2/2, zeta(4,1)=pi^4/90.

## Remaining models (to read + port)
- Model 1 Weil: pure algebra (x^4-5x^3+9x^2-5x+1; Q(y)=y^2-5y+7, |y|=sqrt(7)>2).
- Model 3 Epstein class-2 disc -20: theta–Mellin continuation, cross-checks modularity +
  zeta_K = zeta·L(chi_-20) = (1/2)(zeta_Q1+zeta_Q2).
- Model 4 Beurling planted zero: Z(s)=zeta(s)(1+c·2^-s), c=2^-(1/2+delta), delta=0.1.
  HONEST label: planted zero PROVEN; genuine 0/1 Beurling system INCOMPLETE.
- Classifier: 4-class keyword matcher (CONJECTURED-grade).

## FILLED IN AFTER RUN: binary output + verdicts per model.

## COORDINATOR POSTSCRIPT — build fixed, run verdict: MATH CORES BROKEN (2026-08-17 ~01:45)

Agent A died at 108% context with 8 `expected ','` errors (adjacent string literals in
println!/format! — Rust does NOT concatenate adjacent literals, unlike C). Coordinator fixed
all 8 (joined to single literals) + the borrow-of-moved-value in check_claim. Build now clean
(`cargo build --release --target x86_64-unknown-linux-musl`), binary runs. Full output below.

**RUN VERDICT: the port does NOT reproduce the certified DH zeros — the math cores are broken.**
- model_dh: certified zeros NOT matched (0/2). |f_plus| = 641 and 232 at the certified
  locations s=0.808517182+i·85.699348485 and s=0.650830081+i·114.163342731 (need <1e-9).
  FE sign +1 and sign −1 both FALSE → the constructed f_plus/f_minus are NOT the
  Davenport–Heilbronn-type combination. eps(psi) = −13.877453+66.586728i with |eps|=68.017,
  whereas the certified reference has eps(psi)=0.850650808352+0.525731112119i (|eps|=1,
  GaussSum/i√5) — the ε is wrong by construction.
- model_epstein: modularity identity rel-diff 0.59–0.91 (should be ~0); continuation anchors
  off by 3–6 orders of magnitude (rel 3.3e3, 1.1e6); Dedekind decomposition false. Broken.
- **Gamma is wrong**: Γ(2)=1.5054066594 (expect 1), Γ(5)=32.3955445282 (expect 24) — the
  Lanczos implementation is broken; this poisons every FE check and the DH normalization.
- model_weil: CORRECT (fake polynomial roots |y|=√7>2, all |x|≠1). model_beurling: CORRECT
  (planted zero |Z(s0)|=0.89 — note: should be ~0; the generic-point check shows the planted
  zero is NOT at the claimed location; INCONCLUSIVE). classifier: 9/10 correct (one mismatch:
  class-d tautology classified 'unknown').

**STATUS: ABANDONED as a deliverable, kept as a stub.** The Rust barrier zoo is NOT rung-0
usable yet: it must reproduce the Python-certified DH zeros before any argument is disciplined
by it. Root-cause (conjectured): (i) Γ via Lanczos is misimplemented (verify against
argprinciple's Gamma or the Euler product), (ii) ε(ψ) = GaussSum/(i·√5) was computed wrong
(|eps|=68 instead of 1), (iii) Epstein theta dual exponent slip (agent itself flagged the
Python reference's (4πt/|D|) as a slip — but the Rust port's modularity is ALSO broken, so the
fix is not yet right). Next step when resumed: fix Γ first (self-test pins it), then ε, then
re-run; the certified DH zeros are the acceptance test.

Full binary output is in the coordinator transcript (commit message carries the short verdict).
