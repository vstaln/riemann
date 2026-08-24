# Unmined external certificate machinery — sweep 2026-08-24

Survey of `research/external-results/` repos NOT yet reverse-engineered by our
pipeline (tawanerguo already mined — skipped). Each: claim, machinery,
portability into our corrected F_T coboundary + interval-B&B pipeline,
provenance sanity. Labels: PROVEN (has own verifier/cert), CLAIMED (no
independent verifier), FORMALIZED (Lean).

---

## 1. ainta-zeta-simple-zeros — "67.30085% simple zeros"

- **Result**: liminf N_0^s(T,2T)/N(T,2T) ≥ 0.673008527927… (> Anthropic Thm D 0.67250…).
  Two certified inequalities: (a) 3 consecutive zeros: ε_4 ≥ 221/10^6; (b) 7 consecutive
  zeros: F_6(g) ≥ 19/5000 (weighted six-gap six-variable bound).
- **Machinery**:
  - **Stability-enhanced rank-inertia inequality** (eq 2.1): keeps the defect
    term Δ(M)=tr Ψ(M) that the two-trace argument drops, where
    Ψ(t)=(t−1)² on [0,2], 2t−3 on t≥2. Counting: S ≥ H_0 N + Δ(M) − o(N).
  - **Dual form of Ψ** (eq 3.4): Δ(V*V) ≥ (3/2)Σ|⟨V_i,V_j⟩|² over any max-degree-2
    graph E — converts pairwise inner products into global defect.
  - **Kernel positivity**: Montgomery–Taylor overlap kernel K has *sum-free* zero set
    (x tan πx = c; x,y,x+y zeros impossible). This is a non-computational analytic
    reason ε_4 > 0; verifier makes it quantitative (Arb).
  - 3-point: partition into length-4 cells, disjoint triples, triangle → eq 3.5-3.6.
  - 7-point: F_6(g)= (1/3000)Σg_i + Σ_s 2/(7−s) Σ w(g_i+…+g_{i+s−1}), w=k²; sum over
    consecutive 7-windows → eq 4.3-4.6; blocks m=269, G_B convex pinching (eq 4.4).
- **Portability**: HIGH for the **dual-of-Ψ / graph-defect** step and the **sum-free
  kernel zero-set** idea. Our coboundary machinery is about F_T zero/difference
  structure; the idea that preserved inner-product info (not just rank/traces) can be
  carried through via Ψ and a max-degree-2 graph is a directly transportable template.
- **Provenance**: PROVEN — ships Python verifier (Arb interval), recorded certs
  (three-point.txt, seven-point.txt), tests. Rubs off Anthropic's Lean artifact.

---

## 2. trmdy-zeta-simple-zeros-673137 — "67.31376% simple zeros" (current record family)

- **Result**: liminf ≥ 0.673137630699… > 420711/625000. Three new ingredients lift the
  ainta 67.30085% → 67.31376%; repeatedly rebuilds ainta's 7-pt cert as a correctness
  gate.
- **Machinery**:
  1. **Re-optimized 7-term rational cosine window** (`design.py`): v(s)=Σ c_j cos(ω_j s),
     ω=(√2,2π,…,12π), exact rationals /1e9. Gives up 4.4e-5 of prime-side H(v) to push
     overlap-kernel early zeros so cheapest near-annihilating gap configs lengthen ~10%.
     This is a **tunable window family** (KernelSpec + window_functional computes H(v),
     c_1(v) in Arb with exact rational coeffs).
  2. **Position-weighted seven-point inequality**: F(g_1..g_6) ≥ 1/200 for all g_i ≥ 0,
     weighted by reflection-symmetric rational pair weights a_{ij}/1e6 with **every span
     capacity Σ_i a_{i,i+r} = 2 exactly**, pressure 1/2300. Certified by **exhaustive
     interval subdivision over the 6-D gap simplex, 1,000,984 nodes** (Arb, parallelized).
     This is an interval-B&B over gap space — the SAME skeleton as our pipeline.
  3. **Sharp square-root tail for block defect** (`docs/proof.md` §, cli.py):
     tr Ψ(G) ≥ h(E), h(E)=E for E≤1, 2√E−1 for E≥1 (sharp), plus convex-fraction
     h(E) ≥ (h(A)/A)·E on [0,A]. Replaces the "unit cap" h≤1 of the earlier argument,
     letting blocks run to m=257.
  - Final deduction: S/N ≥ (257 H_cert − η·(3/1150)·256)/(257−R), η=R/A, A=251/200,
    R=2√A−1.
- **Portability**: **HIGHEST.** This is effectively a superset of ainta's engine and it
  aligns almost 1:1 with what our pipeline wants (interval-B&B over gap simplex,
  pressure/envelope tuning, new windows). The exact-rational **KernelSpec + Arb
  window_functional** is directly importable as a *new kernel family for* F_T. The
  **span-capacity-equal-2 weight design** is a concrete pressure scheme. The **sharp
  sqrt-tail h(E)** is a strictly better envelope than any unit cap.
- **Provenance**: PROVEN — pins python-flint exactly, hashes recorded tables, verifier
  reproduces ainta's 7-pt cert as gate before certifying new; provenance.md says
  rank–trace stability machinery "independently audited twice", produced by multi-model
  session (Claude Fable, GPT-5.6 Sol, Grok) 2026-08-11.

---

## 3. anthropic-zeta23 (bundle) — Lean 4 formalization of "More Than Two Thirds…"

- **Result**: sorry-free Lean/Mathlib formalization of Theorems A–E (+ 6 ξ′ statements,
  + PairCeiling bandwidth-one ceiling). Constants: A 2/3, B 2/3 simple, C 5/6 distinct,
  D 0.67250 with Montgomery–Taylor window, E Dirichlet analogues.
- **Machinery** (formalized): Weil explicit formula, Riemann–von Mangoldt, Stirling for
  Γ′/Γ, Chebyshev–Mertens, Montgomery–Vaughan; §3 linear algebra: Sylvester inertia,
  **rank–trace inequality + "Lemma R" TIGHTNESS** (defect equality
  2c·tr(P+Q)−‖P+Q‖_F² = Σ k_c(m_j)+c²·b on tight config); **PairCeiling stability
  inequality** (two IBP identities → the bandwidth-one CEILING 0.6818287 + 2.55e-6·(…));
  **XiPrime** (simple-on-line zeros of ξ′, ≥0.85838 simple / 0.92919 distinct).
- **Portability**: LOW-to-MEDIUM as *code* (Lean, no direct import into Python). HIGH as
  *mathematical ceiling signal*: the PairCeiling result **bounds what ANY bandwidth-one
  certificate can achieve (≤0.6818…)** — this is the honest ceiling of our bandwidth-one
  F_T approach; our pipeline should treat 0.6818… as the target ceiling, not exceedable
  within the method (only by breaking out of bandwidth-one/window-family assumptions,
  which trmdy already does with the re-optimized window). Lemma R tightness tells us our
  coboundary can't be improved by just tightening rank-trace — we must carry more structure
  (matching ainta/trmdy's preserved inner-product/Ψ idea). XiPrime gives a second
  functional (ξ′) to cross-check/transfer pressure schemes.
- **Provenance**: PROVEN — #print axioms = [propext, Classical.choice, Quot.sound] only;
  comparator configs; axiom-audit scripts; ported PrimeNumberTheoremAnd files attributed.

---

## 4. openai-ten-proofs — "Ten Advances in Mathematics and TCS" (NOT Riemann)

- **Result**: Lean 4 formalizations of 10 unrelated results: sphere packing, binary/
  spherical codes, non-sofic groups, Connes rigidity, permanent lower bounds, quantum
  parallel repetition, GapCVP, Ehrhart volume, multicolor Ramsey, extremal graph
  conjectures. **None involve ζ or the critical line.**
- **Machinery**: sphere packing (Cohn–Elkies **linear-programming bound**, Fourier
  positive-x kernel / "magic function" search), metric codes (LP bounds), permanent ∏-2
  circuits, quantum repetition, lattice/holographic. The one structurally resonant item
  is **sphere-packing LP bounds** (optimize a positive-definite/positive-Fourier kernel
  over a lattice-shift polytope) — a *different* optimization family from our interval-B&B,
  but the "find the best admissible kernel by optimization then certify by interval
  arithmetic" pattern matches trmdy's window-reoptimization philosophy.
- **Portability**: LOW for RH (orthogonal problem domain). Only the *methodological*
  pattern (optimize-then-certify kernels; LP vs B&B tension) is worth noting; the actual
  kernels don't transfer.
- **Provenance**: PROVEN (Lean, Comparator challenges per file), but **irrelevant to the
  Riemann pipeline** — flagged so we don't waste port effort here.

---

## Ranked portable ideas — by gain-per-port-hour

1. **Import trmdy's exact-rational KernelSpec + Arb window functional as a new tunable
   kernel family for F_T** — see src/zeta_ext/kernel.py, design.py, h0_cert.py.
   Gain: one knob that repositions overlap-kernel zeros (their ~10% gap-lengthening
   moved the window constant ~34%). Port ~2-3h. Highest raw payoff.
2. **Port trmdy's span-capacity-equal-2 position-weighted seven-point pressure scheme**
   (design.py WEIGHT_NUMERATORS, pressure 1/2300, 6-D gap-simplex interval B&B,
   verify_general.py). Gain: a concrete, already-certified pressure+envelope recipe that
   is structurally identical to our pipeline's bottleneck. Port ~3-4h.
3. **Adopt the sharp square-root tail h(E)=E (E≤1), 2√E−1 (E≥1)** as our block-defect
   envelope (trmdy docs/proof.md; ainta Ψ 2.1). Gain: strictly tighter than a unit cap,
   enables larger blocks (m up to 257). Port ~1-2h, tiny diff.
4. **Port ainta's dual-of-Ψ graph-defect step** (Δ≥(3/2)Σ|inner|² over max-degree-2
   graphs) + **sum-free-kernel zero-set argument** (ainta proof.md §3) into our coboundary.
   Gain: carries preserved inner-product info instead of dropping it — directly addresses
   Lemma-R tightness. Port ~2-3h.
5. **Treat 0.6818… as the hard bandwidth-one ceiling** (anthropic PairCeiling Stability.lean).
   Gain: *not* a kernel but an honest expectation-setter + tells us the only way past it is
   breaking out of the bandwidth-one/window class (which 2 & the window reopt already do).
   Port ~0 (read-only), do it first to calibrate.
6. **(Optional, later) ξ′ as a second functional** (anthropic XiPrime) — pressure/weight
   ideas cross-check on a different L-function-like object. Port ~+hours; low urgency.

Not ranked (do not port): openai-ten-proofs (orthogonal domain; only the optimize-then-
certify pattern is methodologically resonant), anthropic Lean code as importable code
(no direct Python path; consume it as math/ceiling only).

---

Status: recon-level sweep based on READMEs, docs/proof.md (ainta, trmdy), design.py/h0_cert.py
(trmdy), PairCeiling/Stability.lean + main README (anthropic), README (openai). Constants
and mechanics quoted verbatim from those sources; portable-ness judgments are mine
(CONJECTURED until exercised against our pipeline).
