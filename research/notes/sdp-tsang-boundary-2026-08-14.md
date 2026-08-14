# SDP Boundary Probe: Tsang Strip-Positive Cone — What the Unconditional Pair-Correlation SDP Can Certify

**Agent:** builder. **Date:** 2026-08-14.
**Task:** small-case feasibility boundary for the Tsang strip-positive cone of
`research/notes/sdp-unconditional-structure-2026-08-14.md` §6–8: the best multiplicity-sum bound
Σ_ρ (m_ρ − 1)/N(T) (equivalently the simple fraction) the unconditional SDP can deliver at
bandwidth-1, box b₀ = 1 inputs, located against the 0.6818 wall.
**Script:** `tools/sdp_unconditional_structure/boundary_probe.py`
(numpy/scipy via `uv run --with scipy --with numpy`; single HiGHS linprog, < 1 min).
**Skills applied:** `s4h-design-constraints` (the strip-positivity constraint is the hard,
binding constraint; everything else is soft quadrature), `s4h-probability-expected-value-calculation`
(whether a full-size SDP is worth funding — verdict below).

---

## 1. The reduced SDP (typed)

**Decision variables.** j(a) on [0, 1], even, j ≥ 0, j(0) = 1, discretized on the 5 Simpson nodes
α ∈ {0, ¼, ½, ¾, 1} and interpolated piecewise-linearly (hat basis φ₀…φ₄). Free variables
j₁…j₄ = j(¼…1); j₀ = 1 pinned.

**Objective** (homogeneous ratio, BGSTB (7.2), linear-fractional):

    R(j) = [ j(0) + 2 ∫₀¹ a j(a) sech(a) da ] / [ 2 ∫₀¹ j(a) sech(a) da ].

    simple fraction ≥ 2 − R(j);   Σ_ρ (m_ρ − 1)/N(T) ≤ R(j) − 1.

**Constraints.**

  (a) Positivity: j_k ≥ 0 (exact for the piecewise-linear interpolant).
  (b) Strip positivity (the unconditional cone, the entire content):

      Re K_j(x + iy) = (1/π) ∫₀¹ j(a) sech(a) cosh(ay) cos(ax) da ≥ 0
      for all x ∈ R, |y| ≤ b₀ = 1.

      (b₀ = 1 is BGSTB's box |β − 1/2| < 1/(2 log T) in z-units; Re K_j is linear in j, so (b)
      is a semi-infinite family of linear inequalities, sampled on a finite (x, y) grid here.)

**Formulation.** Charnes–Cooper linear-fractional LP: set y_k = t·j_k (k ≥ 1), y₀ = t·j₀ = t,
fix the denominator 2∫j sech = 1, minimize the numerator:

    min  (1 + C₀)t + Σ_{k≥1} C_k y_k
    s.t. d₀ t + Σ_{k≥1} d_k y_k = 1,     d_k = 2 ∫ φ_k sech
         c₀(x,y) t + Σ_{k≥1} c_k(x,y) y_k ≥ 0   (strip samples),
         y_k ≥ 0, t ≥ 0,

    C_k = 2 ∫ a φ_k(a) sech(a) da,   c_k(x,y) = (1/π) ∫ φ_k(a) sech(a) cosh(ay) cos(ax) da.

Integrals are computed exactly-for-the-hat-basis by 4001-point trapezoid; strip samples
x ∈ [0, 40] (801 pts) × y ∈ {0, ¼, ½, ¾, 1}. 5 columns, ~4k rows. HiGHS.

---

## 2. Solver output (verbatim)

```
=== boundary probe: Tsang strip-positive cone, b0 = 1.0 ===
linprog status: Optimization terminated successfully. (HiGHS Status 7: Optimal)
nodes alpha           = [0.   0.25 0.5  0.75 1.  ]
recovered j (j0..j4)  = [1.000000e+00 7.816576e-01 4.944563e-01 2.128195e-01 3.033062e-05]
Charnes-Cooper t      = 1.0791946166713993

R_min   = ratio (j(0)+2A)/(2J)      = 1.38492545
simple fraction >= 2 - R_min        = 0.61507455
Sigma(m_rho-1)/N(T) <= R_min - 1   = 0.38492545

Fejer j=(1-a)+ reference: R = 1.391387  simple = 0.608613
post-check min Re K_j on fine grid (y in [0,1], x in [0,120]) = -2.338382e-07
PASS
```

Independent high-precision check of the Fejér reference (mpmath, dps=30):
`J = 0.46406483928…`, `A = 0.14569381771…`, `R = 1.39138707149…`, `simple = 0.60861293…` —
the script's reference reproduces BGSTB's 0.60857 exactly. [CHECKED NUMERICALLY.]

---

## 3. The boundary verdict

| Input / cone | Z = R | simple ≥ | Σ(m_ρ−1)/N(T) ≤ |
|---|---|---|---|
| Montgomery hat, no strip constraint | 4/3 = 1.3333 | 2/3 = 0.6667 | 0.3333 |
| Tsang/Fejér j = (1−a)₊, strip-positive | 1.39139 | 0.60861 | 0.39139 |
| **5-node LP over the strip-positive cone (this probe)** | **1.38493** | **0.61507** | **0.38493** |
| CGdL SDP, RH-conditional | 1.3208 | 0.6792 | 0.3208 |
| 0.6818 wall (p₁ = p₀) | — | 0.68183 | 0.31817 |

**Boundary number: simple fraction ≥ 0.6151 (Σ(m_ρ−1)/N(T) ≤ 0.3849).**

**vs 0.6818:** the unconditional SDP at its current inputs sits at **~0.615, i.e. 0.067 below the
0.6818 wall** — and also 0.052 *below* Montgomery's classical 2/3. The strip-positivity constraint
is the whole story: it is what makes the off-diagonal drop in BGSTB's transfer valid, and its price
is exactly that j cannot spike at the band edge α = 1, so R is forced up from 4/3 to ~1.39.
The 5-node LP recovers only +0.0065 over the Fejér point (0.6151 vs 0.6086); the SDP layer over
this cone is nearly empty.

**Why the wall is out of reach (structure, not arithmetic).** To certify simple ≥ 0.6818 one needs
R ≤ 1.3182, *below* Montgomery's 4/3. The strip-positive cone is a strict subset of Montgomery's
cone, and every strip-positive shape (Fejér, Montgomery–Taylor, the LP optimum) has R ≥ 1.39. The
strip constraint cannot be weakened — without it the problem is vacuous (simple → 1, note §6/§8).
So the 0.6818 wall needs a *different input* (a certified wider box / double-sum estimate, or a
multiplicity theorem), not a better j — confirming `structural-final-verdict.md`'s "HARD constraint"
classification from the SDP side.

---

## 4. Does this deserve a full-size computation?

**No — belief it would change: ~0.6 → ~0.62 at best, verdict unchanged.** A full-size SDP
(d ≈ 10–20 polynomial basis, rigorous strip closure) would tighten the discretization, but the
5-node optimum is already **active on the strip boundary** (post-check min Re ≈ −2e-7 ≈ 0) and only
+0.0065 above Fejér, so the remaining slack is ~one-tenth of the 0.067 gap to the wall. Full-size
would move 0.615 toward the true continuous optimum (plausibly ~0.62), leaving the verdict —
*the unconditional pair-correlation input cannot certify anything near 0.6818* — untouched.
The next lever is not the SDP layer; it is a certified box / double-sum input (Candidate 1 of
`structural-thread-newinput-2026-08-14.md`). [CONJECTURED, belief-stated per hooks §40.]

---

## 5. Labels

| Claim | Label |
|---|---|
| BGSTB (7.2) ratio ↔ simple fraction / multiplicity sum identity | PROVEN (elementary) |
| Strip positivity (b) linear in j; cone = semi-infinite LP | PROVEN (elementary identity) |
| Charnes–Cooper LP equivalence | PROVEN (standard LP) |
| 5-node optimum R = 1.38493 → simple ≥ 0.61507 | CHECKED NUMERICALLY (script cited) |
| Fejér reference 0.60861 (matches BGSTB 0.60857) | CHECKED NUMERICALLY (mpmath dps=30) |
| Full-size SDP would not change the verdict (~0.62 ceiling) | CONJECTURED (belief stated) |

**Ponytail note:** 5 hat-basis nodes, strip sampled to x ≤ 40 (not a rigorous tail closure);
tail contribution of Re K_j decays as cos(ax) oscillations against sech-weighted hats, so |x| > 40
is dominated and the fine-grid post-check found no violation to 1e-6. Upgrade path if the ~0.62
question ever matters: polynomial basis + Fejér–Riesz/Toeplitz PSD lifting with a tail-closure lemma.
