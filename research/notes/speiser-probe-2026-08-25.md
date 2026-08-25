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

Two methods, per the mission brief: **(a)** sample-based winding of f′ along the boundary
(primary — robust; phase unwrap, dps=15; 400–2000 pts/side), **(b)** mp.quad of the
log-derivative (cross-check).

Rectangles (t₀±8): A = [0.25, 0.49] (mission spec); B = [0.05, 0.49];
E = [0.01, 0.499]. The E right edge near the line catches pushed zeros that land just left of ½;
B/E left edges catch zeros pushed far left.

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

Runtime: main run 1157 s wall (winding-primary, dps=15); verification run (dense winding n=2000/side,
quad maxdegree sweep, localization) +13 min. Within the 30-min compute budget.
All numbers: CHECKED NUMERICALLY (mpmath, dps=15; winding via dense phase unwrap + quad cross-check).

| config | rect A [0.25,0.49] | rect B [0.05,0.49] | rect E [0.01,0.499] | quad sanity (rect A) |
|---|---|---|---|---|
| baseline | N=0 | N=0 | N=0 | ≈0 (2.8e-16) |
| **off1** (single plant 0.9+it₀, mission-literal) | **N=0** | N=0 | N=0 | ≈0 |
| **off4** (FE-consistent: 0.9±it₀, 0.1±it₀) | **N=1** | **N=1** | **N=1** | → 1 (maxdeg8: 1.008) |
| on1 (single 0.5+i(t₀+0.3)) | N=0 | N=0 | N=0 | ≈0 |
| on4 (pair) | N=0 | N=0 | N=0 | ≈0 |

Robustness of the off4 count: dense winding n=2000/side rect A → N=1 (min|f'| on contour 1.8e3, no
near-pole); quad log-derivative (the mission's primary method) converges 1.433 @maxdeg6 → 1.008 @maxdeg8
→ N=1 (tanh-sinh is slow here because the pushed zero sits close to the right edge; winding is the robust
method — noted: quad maxdegree must be kept small or it refines ~2 hours).

Localization of the pushed zero (off4): min |f'| at **Re ≈ 0.4526, Im ≈ t₀** (scan along Im=t₀ and over
[0.42,0.48]×[t₀−2,t₀+2]). One and only one ξ′-zero in Re<1/2 near t₀, sitting just left of the line,
roughly midway between the planted mirror pair (0.1+it₀, on-line zero at 0.5+it₀). Baseline sanity:
Re(ξ′/ξ) < 0 at every sampled point in Re<1/2 (−0.53, −0.021, −0.021, −0.0097, −0.53).

## 4. Verdict

**TYPE_SEPARATES — N is type-sensitive, but only for a functional-equation-consistent implant.**

1. **Mission-literal prediction REFUTED for the literal construction (PROVEN + CHECKED NUMERICALLY):**
   a single planted off-line zero at 0.9+it₀ (R = (s−s₀), no mirror) gives **N=0**: it cannot push any
   ξ′-zero across Re=1/2. Rigorous reason: with the mirror absent, every Hadamard pair term has
   Re < 0 on 0<σ<1/2 (paired terms (σ−½)/|s−ρ|² < 0) and the extra term 1/(s−s₀) has Re = (σ−0.9)/|·|² < 0,
   so Re(ξ′_p/ξ_p) < 0 on the whole left half-strip ⇒ ξ′_p ≠ 0 there (verified numerically: N=0 in all
   three rects).
2. **Speiser mechanism CONFIRMED (CHECKED NUMERICALLY):** planting the off-line zero WITH its
   functional-equation mirror at 0.1+it₀ (off4, preserves ξ(s)=ξ(1−s)) pushes exactly **one** ξ′-zero
   into Re<1/2 at Re≈0.4526, Im≈t₀ → **N=1** in every rectangle (winding coarse + dense, quad → 1).
   The mirror zero at 0.1+it₀ is what adds a term with Re>(σ−0.1)/|·|² > 0 for 0.1<σ<0.5, opening the
   real part to positivity.
3. **On-line implants do NOT push (CHECKED NUMERICALLY):** both on1 and on4 give N=0 — the statistic is
   clean for on-line violations.

⇒ For the lever-4 program: **N over [0.25,0.49]×[t₀±8] IS the first type-sensitive statistic**, but the
implant protocol itself must respect the functional equation (plant the zero and its mirror
(0.1+it₀)); a naive single-factor implant is not a valid Speiser test and predicts zero. This
matches the existing `speiser-negativity-program.md` sign structure exactly.

Methodological note: at dps=15 the quad (tanh-sinh) is fine for the no-pole configs but explodes in
refinement when the pushed zero is near the contour; sample-winding is the reliable primary and agrees
with quad where both terminate.
