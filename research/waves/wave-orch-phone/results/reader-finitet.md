# ROLE 1 — READER/THEORIST: exact finite-T error-term structure of the 0.67326 certificate

**Executed by:** orchestrator (inline) — the Agent subagent tool is unavailable in this
environment; the READER role was executed inline from the source notes. Honesty labels per
`hooks/agents.md`. All numbers quoted here are copied from the cited notes (labeled as such),
NOT re-derived here.

**Sources read:** `research/notes/attack-finitet.md`, `attack-finitet-cinf.md`,
`discovery-6732629.md`, `attack-kernel.md`, README P6.

---

## 1. The certificate (from discovery-6732629.md, CHECKED NUMERICALLY there)

```
liminf_{T→∞} N₀ˢ(T,2T)/N(T,2T) ≥ 0.6732628655343560 [RETIRED 2026-08-24]
bound = (H − τ)/(1 − B/m)
  H = H(α=1.49) = 0.6724218860964        (window value, verified to 1.7e-41 vs kink-split quadrature)
  τ = psum·(m−6)/m,  psum = 1/220,  m = 133
  B = Φ_m(ε(m−6)),  Φ_m(x) = 2√((m−1)x/m) − 1 + x/m
  ε from certified floor F ≥ 0.00806     (Arb interval verifier verify_cos7.py, 942,944 nodes)
```

The formula itself contains **no T-dependent dropped term**: every ingredient is either an exact
rational (τ), a certified constant (ε, hence B), or a verified window value (H). The T→∞ content
lives entirely in *which* liminf functional the machinery is derived from (Claim 2.1 Poisson
completion, Lemma 3.2 trW, Lemma 3.3 ‖W‖²_HS) — see §3.

## 2. The finite-T structure of the underlying W_T argument (from attack-finitet*.md)

For the idealized model φ_T(x) = ψ(x·T/N), ψ(u) = cos(√2·u)·1_{|u|≤1/2}, W_T = (1/∫ψ²)·VᵀV,
V[ρ][k] = Ψ(s_ρ−k), s_ρ = (γ_ρ−T)N/T:

- **Ψ(s)** = sin(1/√2−πs)/(√2−2πs) + sin(1/√2+πs)/(√2+2πs) — entire, C⁰ corners of ψ give
  |φ̂_T| ~ |ω|^{-1} decay. **Ψ₂(s)** = sin(πs)/(2πs) + ¼[sin(√2−πs)/(√2−πs)+sin(√2+πs)/(√2+πs)]
  (FT of ψ²). ∫ψ² = 1/2 + sin(√2)/(2√2) = **0.849227999318304**.
- **Claim 2.1 (Poisson)**: Σ_k Ψ(s−k)Ψ(s′−k) = Ψ₂(s−s′). Truncation error = O(1/K) for the
  hard cutoff (measured 2.5e-3 @K=50 → 4.9e-5 @K=2000, ratios exactly 5×/10×); **super-algebraic
  (≤3.9e-19) for C∞ χ-smoothed φ̄** — this is the single place where C∞ vs hard-cutoff provably
  differ, and where the C∞ kernel strictly wins (attack-finitet-cinf.md §3, CHECKED NUMERICALLY).
- **Lemma 3.2**: trW_T/N = 1 + o(1), deficit ≈ edge-zero k-truncation, measured 0.992→0.998.
- **Lemma 3.3**: ‖W‖²_HS/N → c = 1/2 + (1/√2)cot(1/√2) = **1.327499296320588**, measured
  1.265→1.287 at T=100..600 (3% deficit at T=600).
- **bound/N = 2·trW/N − ‖W‖²_HS/N** (rank–trace, Lemma 3.4 with B=0): measured **0.709–0.719**,
  **Δ = bound/N − 0.67250070 = +0.047 → +0.037, positive at every T** (attack-finitet.md §5).

## 3. Labeled error-term inventory (what is dropped / what the T-dependence is)

| term | meaning | T-dependence | status |
|---|---|---|---|
| (E1) edge/k-truncation of the grid | trW deficit (Lemma 3.2 o(1)) | ~O(1/N) | CHECKED NUMERICALLY (attack-finitet) |
| (E2) k-sum truncation of Poisson id. | hard cutoff: |ψ̂|~|ω|^{-1} | O(1/K); C∞: super-algebraic | CHECKED NUMERICALLY (attack-finitet-cinf §3) |
| (E3) HS2 pair-sum deficit vs own window constant Q(v) | finite-T zero statistics under bandwidth-one kernels | ~4% at T=600, decays ~1/log T | **CONJECTURED** (attack-finitet-cinf §7) |
| (E4) overshoot Δ = bound/N − 0.67250 | idealized model limit approached from above | Δ ≈ 0.19/ln(T/2π); fit asymptotes 0.014–0.037 (non-zero, INCONCLUSIVE) | CHECKED NUMERICALLY (attack-finitet §5); asymptote INCONCLUSIVE (validation-001) |
| (E5) smoothing's effect | C∞ χ-ramp (ε=T/N) raises Q(v): 1.33→3.86, bound goes NEGATIVE | pre-asymptotic at T≤600 (ε>T needed flat interior) | CHECKED NUMERICALLY (attack-finitet-cinf §4,§6) |
| (E6) window functional Q(v) | T→∞ limit of HS2/N for a *given* window | constant of the window | PROVEN for cos minimizer (attack-kernel §2, Lean) |

**Key structural fact (E5):** the C∞ χ-smoothed kernel does NOT pull HS2/N toward c=1.3275; it
raises the window constant Q (1.333 → 1.415 → 2.20 → 3.86 for ε=0.1/0.5/T/N) and makes the
rank–trace bound vacuous (negative) at accessible T. The hard-cutoff cosine is the *lowest*
window in the family (attack-kernel.md: cosine = global minimizer of Q, PROVEN). Hence for the
P6 question "C∞ vs hard-cutoff finite-T errors": C∞ fixes (E2) only; the dominant (E3) deficit
is kernel-independent zero statistics.

## 4. P6 restated precisely (open)

At finite T, the empirical windowed functional for a C∞ kernel differs from its hard-cutoff
analog *only* through (E2) (provably better) and through the window constant Q(v) itself
(provably worse for every smoothed window — cosine is the minimizer). The genuinely open part of
P6 is **(E3)**: the ~1/log T pair-sum deficit below the window constant is CONJECTURED to be
zero statistics; a definitive settlement needs T ≫ 10⁵ (γ up to 10⁷), out of reach of current
data (γ ≤ 1419 in the notes; 10⁴–10⁵ zeros available in tools/data — see executor).

**INCONCLUSIVE items inherited:** (i) whether Δ's asymptote is 0 (logarithmic) or a nonzero
level (fits give 0.014–0.037); (ii) whether the finite-T overshoot direction (Δ>0) persists for
the *record* window α=1.49 (all prior probes used the idealized α=√2 hard cutoff).

RESULT: INCONCLUSIVE — error-term structure extracted (E1–E6, all labeled); dominant open term
is the CONJECTURED zero-statistics pair-sum deficit (E3); C∞ provably fixes only the k-truncation
term; the α=1.49 finite-T direction is unprobed.
