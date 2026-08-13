# Design: raise a proved lower bound (sleep-mode, no further gates)

**Date:** 2026-08-13
**Status:** locked by user choice **C** (“whichever is reachable; never stop until a breakthrough”). Review gate waived.
**Labels bind:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE.

## Goal (what “above 67%” can mean)

Our certified simple-on-line record is **0.6734808616745137** (coboundary, α=1.464, eps=0.0062). Anthropic’s 67.25% sits below that. The in-class structural ceiling is **0.6818287** (256-law). Breaking 0.6818 needs an unconditional simple-fraction theorem with p₁ > p₀; that input does not exist in this repo (`structural-final-verdict.md`, PROVEN arithmetic).

This pod has `python3`+numpy only: **no scipy, no mpmath, no python-flint, no uv**. The coboundary interval verifier cannot run here. A new certified 0.673481+ record is therefore **not reachable on this machine** without porting Arb verification to Rust `rug` (large, still in-class grind).

**Success, in order, given C and the machine:**

1. A **new proved constant** that is a genuine lemma (not a Ritz upper bound), documented with script+command.
2. If that constant is `μ₂ ≥ 1.355`, the even mean-zero complement of Suzuki (4.5) is safe at `a₂` — an explicit-δ method, **not** a 67% proportion and **not** RH.
3. A certified simple-on-line bound `> 0.67348086` is **out of scope on this pod**. Do not claim it.

## Approaches (trade-offs)

### A — Tangent-LP coboundary (in-class tick)

Handoff: the only remaining in-class slot. Affine tangent-plane constraints on `(l,c)` at psum=1/335, target eps≥0.0059904, α=1.464, could certify ≈0.673482.

- **Pro:** only path to a number above 0.673481 without new theorems.
- **Con:** class already exhausted at the 0.0062 / α=1.464 saddle; expected gain ~10^{-6}; METHOD FIRST forbids grind; **this pod cannot run the Arb verifier**.
- **Verdict:** ABANDONED on this pod (tooling). Do not port the verifier tonight.

### B — Marked-m₃ certificate class

Super-law marked-windowed m₃(1/2)≈7.98 vs sine 5 (CHECKED). That **excludes the super-law as an adversary** for a functional we do not yet have a prime-side value for. Unconditional m₃ of *unmarked* zeros is the sine kernel (Rudnick–Sarnak, λ<1) and is already dead as a plug-in to the existing LP. Marked m₃ of ζ needs multiplicities. The 256-law configuration is BLOCKED-ON-DATA.

- **Pro:** the only advertised “new class.”
- **Con:** cannot produce a number without a new prime-side marked moment.
- **Verdict:** ABANDONED as a bound-producer until a prime-side marked input exists. The exclusion of the super-law stands.

### C — Tighten the even mean-zero `μ₂` envelope (recommended)

Current PROVEN envelope: `|ŵ(ξ)| ≤ (ξ²/2)√(2/5)‖w‖` for even mean-zero compactly supported on `[-1,1]`, hence Plancherel mass in `|ξ|<Ω` is `≤ Ω⁵/(50π)`, hence

```
μ₂ ≥ max_Ω (1 − Ω⁵/(50π))(log Ω + γ) − 7.09e-5 = 1.02797
```

at Ω=1.865. Need **1.355** to clear `threshold(a₂)`, **1.816** for `a₃`. Ritz says true `μ₂ ≈ 1.96`, so the room is real; the envelope is loose.

- **Pro:** elementary, runs on this pod, is a lemma (lower bound, not Ritz), continues the live Weil line.
- **Con:** does **not** raise the 67% proportion. A local `δ` is not RH.
- **Verdict:** **do this.** It is the only breakthrough-shaped constant we can actually prove tonight.

## Design (Approach C)

### Object

Lower-bound

```
μ₂ := inf { L(w)/‖w‖²_{L²(-1,1)} : w even, ∫w=0, supp w ⊂ [-1,1], w≠0 }
```

with `L(w) = (1/2π) ∫ (log|ξ|+γ) |ŵ(ξ)|² dξ` (Suzuki (4.6), CHECKED vs the jumping form to 4×10^{-6} on the cosine).

### Levers, in order (stop at the first that clears 1.355)

1. **Clipped envelope.** Replace `|cos(ξt)−1| ≤ ξ² t²/2` by `min(ξ² t²/2, 2)`. Integrate the clipped kernel against `|w|` via Cauchy in the form `∫ κ_Ω(t) |w(t)| dt ≤ ‖κ_Ω‖_{L²} ‖w‖`. This can only shrink the low-mass constant below `Ω⁵/(50π)`.
2. **Hilbert–Schmidt of the bandlimited projector on even mean-zero.** Let `Q_Ω` be the integral operator on `L²(-1,1)` with kernel `sin(Ω(x−y))/(π(x−y))`, restricted to `{even} ∩ {∫=0}`. Then low-frequency Plancherel mass `≤ λ_max(Q_Ω)`. Bound `λ_max ≤ ‖Q_Ω‖_{HS}` by a 1-D/2-D quadrature of `sinc²` (numpy). Then

   ```
   μ₂ ≥ max_Ω (1 − ‖Q_Ω‖_{HS})(log Ω + γ) + (negative log piece).
   ```

   If `‖Q‖_{HS}` is still too large, Gershgorin / row-sum of `|sinc|` is a coarser upper bound (likely useless); do not use Ritz max-eig as an upper bound.
3. **Dirichlet vanishing `w(±1)=0`.** Integrate by parts: `ŵ(ξ) = −ξ^{-1} ∫ w'(t) sin(ξ t) dt`. Combine with the `ξ²` zero at the origin *only near ξ=0*; at large Ω the `1/ξ` decay does not help an *upper* bound on low-frequency mass. Use it only if it tightens the clipped kernel in lever 1.
4. **Hard stop.** If none of 1–3 reaches 1.355, record the best proved `μ₂` and the residual gap. Do not substitute a Ritz value. Next lemma (future): a true upper bound on the second even prolate eigenvalue `λ_2(c)` at `c=Ω`.

### Non-goals

- No coboundary / `(psum,l,c)` / tangent-LP on this pod.
- No zero-counting, no LMFDB, no certificate grinding.
- No claim that `μ₂ ≥ 1.355` implies RH. It implies the even mean-zero sector of (4.5) is safe at `a₂` *after* a separate 1-mode check of the ground ray (rank-one + `ρ` + prime overlap). That 1-mode check is **out of this spec** unless `μ₂` actually clears 1.355.

### Verification

Every number from a script under `tools/weil_first_prime/` (new file `mu2_envelope.py`). Command cited in `research/notes/attack-weil-first-prime.md` §21.7. Exploratory `f64` numpy; label CHECKED NUMERICALLY. The *inequalities* (`|cos−1|≤ξ²t²/2`, Plancherel, (4.6)) stay PROVEN elementary / at source.

### Implementation plan (short)

1. Script `tools/weil_first_prime/mu2_envelope.py`: clipped Cauchy envelope; HS norm of `Q_Ω` on a trapezoid grid for a list of Ω; print `μ₂` lower bound vs `threshold(a₂)` / `threshold(a₃)`.
2. Run it. If `μ₂_lo ≥ 1.355`, write the lemma into §21.7 and state the remaining 1-mode task. If not, write the best constant and residual.
3. Commit, push, update PR #1. Ledger line `weil-first-prime-5`.

## Outcome (executed same session)

- Approach A/B not run (tooling / no prime-side marked moment), as specified.
- `tools/weil_first_prime/mu2_envelope.py`: nested conservative `μ₂ ≥ 1.6414` at `Ω=3.2` (n=81 HS × 1.05) **clears `threshold(a₂)=1.3554`** (margin 0.286). Hard cutoff maxed at 1.270 (method wall). Does not clear `a₃`.
- Even mean-zero sector at `a=a₂`: `R≥0.213` after L¹ `ρ` (`‖ρ''‖_1=0.0725`). Ground ray: cosine clears by `2.65×10^{-3}`; `λ_min(V_80)−th=+1.34×10^{-3}`; 1/`k` Schur candidate (not a closed lemma). 67% record unchanged. RH not proved.

Commands: `python3 tools/weil_first_prime/mu2_envelope.py`, `python3 tools/weil_first_prime/ground_ray.py`, `python3 tools/weil_first_prime/ground_ray_cross.py`.

## Follow-up (same campaign, after μ₂ cleared)

The spec's "1-mode check of the ground ray" is now the live lemma (`research/notes/attack-weil-first-prime.md` §23). Remaining: prove `|Q(φ_0,φ_k)|≤C/k` so the Schur of §23.4 is a theorem. Do not resume coboundary.

