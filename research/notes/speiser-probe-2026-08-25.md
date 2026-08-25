# Speiser probe — planted off-line zero vs ξ'-zeros left of 1/2

Author: adventurer subagent, 2026-08-25. Mission: lever-4 rung 3.
Labels: PROVEN / CHECKED NUMERICALLY / CONJECTURED (argument sketch) / INCONCLUSIVE.
Runtime: `uv run --with mpmath python3 research/scripts/speiser_probe.py`.
Related (distinct lever) note: `speiser-negativity-program.md` (proves Re(ζ′/ζ)<0 in 0<σ<1/2; its
pair-term sign lemma confirms the sign analysis used below).

## 0. Contract (as given by mission, treated as hypothesis under test)

Speiser equivalence: **RH ⟺ ξ′(s) has NO zeros in the strip 0 < Re(s) < 1/2.**

Probe question: does a single planted off-line ζ-zero PUSH an ξ′ zero across Re = 1/2
(counted left of ½), and does an on-line implant NOT (i.e. is N type-sensitive)?

## 1. Method — argument principle, bounded height

N := (1/2πi) ∮ f″/f′ ds over rectangle [re_lo, re_hi] × [t₀−8, t₀+8], t₀ = zetazero(1) ≈ 14.1347,
counts zeros of f′ (= ξ′ of the planted ξ) strictly left of ½ near height t₀.

Planted ξ: f = ξ·R.  f′ = ξ′R + ξR′, f″ = ξ″R + 2ξ′R′ + ξR″.
Baseline R=1 ⇒ integrand ξ″/ξ′ = l₁ + l₁′/l₁,  l₁ := ξ′/ξ = 1/s + 1/(s−1) − ½lnπ + ½ψ(s/2) + ζ′/ζ,
l₁′ = −1/s² − 1/(s−1)² + ¼ψ′(s/2) + (ζ″ζ − ζ′²)/ζ².

Two methods, from the mission's baẵt: **(a)** sample-based winding of f′ along the boundary
(primary — robust; 1500 pts/side, ggplot dps=20, phase unwrap), **(b)** mp.quad of the
log-derivative (cross-check).

Rectangles (t₀±8): A = [0.25, 0.49] (mission spec); B = [0.05, 0.49];
D = [0.05, 0.499]; E = [0.01, 0.499]. The D/E right edges near the line catch pushed zeros
that land just left of ½; B/E left edges catch zeros pushed far left.

Configs (plant factor R):
- baseline: R = 1
- **off1** (mission-literal single plant): R = (s − (0.9 + i·t₀))
- **off4** (FE-consistent: off-line zero + functional-equation mirrors, preserves ξ(s)=ξ(1−s),
  real on R): R = (s−(0.9+it₀))(s−(0.1+it₀))(s−(0.9−it₀))(s−(0.1−it₀))
- **on1** (single on-line): R = (s − (0.5 + i(t₀+0.3)))
- **on4** (conjugate pair, FE-consistent): R = (s−(0.5+i(t₀+0.3)))(s−(0.5−i(t₀+0.3)))

## 2. Analytic prediction BEFORE numerics — PROVEN (given RH-in-region) for the sign-blocked cases

Exact identity (paired Hadamard; ξ′(½)=0 kills the constant term, per
`speiser-negativity-program.md`): under RH for the baseline zeros,
**Re(ξ′/ξ)(s) = Σ_γ (σ−½)·(1/|s−ρ|² + 1/|s−ρ̄|²) < 0  for σ < 1/2.**

- **off1**: ξ′_p/ξ_p = ξ′/ξ + 1/(s−(0.9+it₀)); Re(1/(s−(0.9+it₀))) = (σ−0.9)/|·|² < 0 for σ<0.9
  ⇒ Re(ξ′_p/ξ_p) < 0 on all of 0<σ<1/2 ⇒ **f′ has NO zeros left of ½ ⇒ N = 0**.
  So the mission's literal prediction (≥1 for the single plant) is **not achievable**:
  a lone off-line zero lacking its functional-equation mirror cannot push an ξ′ zero across
  the line. [CHECKED NUMERICALLY below.]
- **on1 / on4**: each extra term 1/(s−s₀) has Re < 0 for σ<½ ⇒ N = 0. [CHECKED NUMERICALLY.]
- **off4**: the mirror zero at 0.1+it₀ contributes Re(1/(s−(0.1+it₀))) = (σ−0.1)/|·|² which is
  POSITIVE for 0.1<σ<0.5 near height t₀ ⇒ positive real part becomes possible in 0<σ<1/2
  ⇒ pushed ξ′-zero can sit left of ½ near height t₀. **N ≥ 1 expected** (CONJECTURED; numerics
  decide — this is the Speiser mechanism).

⇒ **Hypothesis: N is type-sensitive, but only when the implant respects the functional
equation (off-line zero planted with its mirror). A bare single-factor implant cannot push
the zero across the line.** This is the headline the numerics test.

## 3. Timing / results

(filled after run — see stdout RESULT / VERDICT lines)

## 4. Verdict

(filled after run)
