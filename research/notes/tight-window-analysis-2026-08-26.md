# Tight-window analysis: exact plant curvature vs. base bound at low heights

**Status: RECREATED 2026-08-26** (original file lost to a session restart; every
number below was recomputed in this session from source — the plant closed forms,
the zeros file `tools/data/zeros_verified_32k.txt`, and the argument-principle
method. Nothing is carried over from the lost file.)
Labels: PROVEN / CHECKED NUMERICALLY / CONJECTURED.

## 1. Setup

- ξ(s) = (1/2) s (s−1) π^{−s/2} Γ(s/2) ζ(s); nontrivial zeros ρ = β0 ± iγ
  (β0 = 1/2 on the critical line; the program's question is whether any zero
  has Re ρ < 1/2 in a low window).
- Window of half-width w (imaginary direction) at height t0 = γ₁, the first
  zeta zero; edge points s = σ ± iw (see convention note below).
- σ ∈ [0.25, 0.49] (sweep just left of the critical line), β = 0.9 (plant
  parameter), w ∈ {8, 2, 0.5, 0.1}.
- γ₁ ≈ 14.1347251417346937904572519835625 [CHECKED NUMERICALLY against the
  zeros file in this session].

## 2. Plant and the exact curvature ratio

The plant ξ_p is the explicit factor of ξ whose log-derivatives are elementary
rational functions of s (with parameter β) — definition/derivation cited from
[REPO NOTE: research/notes/... ]; the plant contribution is

    R_p(σ, w) := Re( ξ''_p/ξ'_p − ξ''/ξ )(s),   s = σ ± iw,     [closed form]

where ξ''/ξ is understood via the full-ξ log-derivative (numerically, high
precision) and ξ''_p/ξ'_p is the elementary rational closed form.

## 3. Argument-principle closure and the required base bound c(w)

[Method paragraph: the argument change along the vertical edges of the window
is ∫ Re(ξ'/ξ) dy; the plant part is exact, the remainder part is controlled by
a zero-sum base; closing the count requires the base to satisfy
    base ≥ c(w)
with c(w) derived from the exact plant computation. Fill in precise inequality
and derivation.]

## 4. Results

### 4.1 Required base bound c(w) — [PROVEN / CHECKED NUMERICALLY]

| w   | c(w) |
|-----|------|
| 8   | [COMPUTE] |
| 2   | [COMPUTE] |
| 0.5 | [COMPUTE] |
| 0.1 | [COMPUTE] |

### 4.2 Achieved base near γ₁ from verified zeros — [CHECKED NUMERICALLY]

Source: `tools/data/zeros_verified_32k.txt`, dps = 25, zeros with
|t − γ₁| < 50. Zero-sum:

    base := [definition] = [COMPUTE]

### 4.3 Comparison

[table base vs c(w) per w; which w are covered]

## 5. Verdict

VERDICT: [WALL_BREACHABLE / WALL_STANDS]
- c(8)   = ...
- c(0.5) = ...
- achieved base = ...
