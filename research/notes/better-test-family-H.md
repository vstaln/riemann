# Better test-family for H? — H(λ)=2−1/λ−λ/3 vs Montgomery–Taylor 0.6725, and the band-width ≤ 1 kernel optimum

**Agent:** research (architect), METHOD question
**Date:** 2026-08-13
**Question:** Is there a test-function family with band-width ≤ 1 giving H(α) > 0.6725007 in our
normalization (the cosine-family max at α=√2), which would directly raise the certified record
0.673481 toward the 0.6818 ceiling?
**Verdict: NO — the band-width ≤ 1 window class is PROVEN closed at H = 0.6725007 (cosine at α=√2,
the Montgomery–Taylor constant). The test-function lever is dead; the 0.673481 → 0.6818 gap is not
window-shaped.**
**Compute:** one few-line mpmath probe (autocorrelation identity, 1-D quadrature, <1 s); exact
arithmetic quoted below. No zero-counting, no sweeps.

---

## (a) The H(λ)=2−1/λ−λ/3 vs Montgomery–Taylor 0.6725 subtlety — RESOLVED

The paper (bundle `564f962e…head.txt`, §1.2, eq (1.3)) states the constant

    H(λ) = 2 − 1/λ − λ/3,   0 < λ ≤ 1,   λ = normalised band-limit of the test function.

The apparent paradox in the task brief is: H(√3) = 2 − 2/√3 ≈ 0.8453 formally, so why does the
paper report only 2/3 and then 0.6725?

**Resolution (PROVEN — exact arithmetic):** λ ≤ 1 is the band-width ≤ 1 constraint, and H(λ) is
strictly increasing on (0, 1] (dH/dλ = 1/λ² − 1/3 > 0 for λ < √3), so the max of THIS family over
the allowed range is at the boundary λ = 1:

    H(1) = 2 − 1 − 1/3 = 2/3.                       (paper eq. (1.3), H(1)=2/3 ✓)

The value H(√3) ≈ 0.8453 is correct arithmetic but corresponds to band-width √3 > 1 — it violates
the constraint, exactly as `attack-kernel.md` §2 quantifies: windows beating the cosine (support
half-width c > 1/2, frequency λ > 1) break Claim 2.1 / the Poisson-completion step
supp φ_T + supp φ_T ⊆ [−N/T, N/T].

**Where 0.6725 comes from (PROVEN):** the paper's §1.2: "The constant 2/3 arises as 2−1/λ−λ/3 at
λ = 1 … On RH, 2/3 was improved to 0.6725 by Montgomery and Taylor [Mon75] and to 0.6727 by Cheer
and Goldston [CG93]". 2/3 is the FLAT window at band-limit 1 (verified: flat window on [−1/2,1/2]
gives Q = (∫v² + ∬|s−s′|vv)/(∫v)² = (1 + 1/3)/1 = 4/3, H = 2 − 4/3 = 2/3, exact). The MT 0.6725 is
NOT the H(λ) family — it is the OPTIMAL window within the SAME band-width ≤ 1 constraint: the
cosine v(u) = cos(√2·u) on [−1/2,1/2], whose constant is

    2 − 1/c₁* = 3/2 − (1/√2)cot(1/√2) = 0.6725007036794116…

(= our H(√2); CHECKED NUMERICALLY, mpmath, and identical to the repo's recorded value
`record-coboundary-sqrt2-673320.md` H(√2) = 0.6725007036794116). So: **the improvement 2/3 → 0.6725
is a window-optimization inside the band-width ≤ 1 class, not a violation of it — and it is exactly
our cosine family at α=√2.**

Cheer–Goldston 0.6727, Bui–Heath-Brown 19/27, and Chirre–Gonçalves–de Laat 0.6792 are all in a
DIFFERENT regime: refined inequalities / higher-moment structure (BHB uses more of the pair-
correlation information), or — for CGdL's 0.6792 — SDP majorants that exploit the positivity of
the form factor F OUTSIDE [−1,1]. The paper is explicit: "the optimality statement in Theorem D is
scoped to the values of F on [−1, 1] only, so such majorants operate in a different regime." They
are not band-width ≤ 1 windows in our certificate's sense and do not feed our certificate's H.

**α ↔ λ mapping (PROVEN — mpmath, matches record notes to all printed digits):**
Our α is the frequency of cos(α·u) on the FIXED support [−1/2,1/2]; the paper's λ is the band-limit
with λ = 1 for that support. So all our α-windows sit at λ = 1 (band-width ≤ 1), and H(α) inside
the family is maximized at α = √2:

    H(√2)  = 0.6725007036794116   (record: 0.6725007036794116 ✓)
    H(1.464)= 0.6724674255777881   (record: 0.672467425578 ✓)
    H(1.49) = 0.6724218860964475   (record: 0.6724219 ✓)
    flat    = 0.6666666666666667 = 2/3,  paper H(1) = 2/3 ✓
    paper H(√3) = 0.845299461620748 (formal; λ=√3 > 1 violates band-width) ✓

Script: one-liner under `uv run --with mpmath`, computing H = 2 − Q for cos(αu) on [−1/2,1/2]
using the exact autocorrelation (v⋆v)(w) = (1−w)/2·cos(αw) + sin(α(1−w))/(2α) and the identity
∬|s−s′|vv = 2∫₀¹w(v⋆v)dw (attack-kernel.md). The direct 2-D quadrature of ∬|s−t|… is cusp-limited
to ~4e-6; the 1-D autocorrelation form is exact to all printed digits.

---

## (b) The band-width ≤ 1 kernel-optimization question — ANSWERED from the literature

**Question:** over ALL even test functions with band-width ≤ 1 (support in [−1/2,1/2], the Fourier
completion constraint of Claim 2.1), what is the max of the functional that yields H, and which
kernel attains it?

**Answer (PROVEN in this repo, corroborated by the literature):** the cosine at α=√2 is the UNIQUE
global optimum; H = 0.6725007 is the ceiling of the class.

1. **Variational proof (PROVEN, Lean-formalized + numeric — `attack-kernel.md`, `Zeta23/ThmD/Functional.lean`):**
   the functional is c₁(v) = (∫v)²/(∫v² + ∬|s−s′|vv) (equivalently 1/Q(v)); H = 2 − 1/c₁ = 2 − Q(v).
   Euler–Lagrange forces v″ + 2v = 0 on the interior, so every critical point is a cosine cos(√2·u);
   the operator I+T with T: v ↦ ∫|·−s′|v(s′)ds′ is positive definite (I+T ≻ 0; min eigenvalue ≈ 0.797
   after the validator correction), so Q is strictly convex on the hyperplane ∫v = 1 and the cosine is
   the GLOBAL minimizer over L²([−1/2,1/2]) — no evenness imposed. Free-grid numerical minimization
   (Rust, N=4001) agrees with the cosine to 1.9·10⁻⁹, max asymmetry 7.8·10⁻¹⁶. Hence Q(v) ≥ Q(v₀)
   for every band-width ≤ 1 window, i.e. **H(v) ≤ 2 − Q(v₀) = 0.6725007036794116 for every window in
   the class.**
2. **Literature corroboration (paper §7.1, §1.2):** "no window does better" — cites [CCLM17, Cor. 14]
   (one-delta extremal problem on [−1,1]); the paper's Theorem D optimality statement is scoped to
   values of F on [−1,1] only, i.e. to band-width ≤ 1. Everything above 0.6725 in the literature
   (CGdL 0.6792 via SDP; also CG 0.6727, BHB 19/27) exploits structure OUTSIDE that scope or a
   stronger inequality, and does not transfer to the window input of our certificate.
3. **Why beating windows fail (PROVEN boundary arithmetic, `attack-kernel.md` §2):** the support
   formula Q(c) = c + (1/√2)cot(√2c) for cos(√2u)·1_{|u|≤c} decreases for c > 1/2 down to Q = 1.1107
   (proportion 0.8893) at c = π/(2√2) — but every c > 1/2 breaks Claim 2.1 (aliased modes in the
   Poisson completion), so those candidates are dead ends, not improvements.

**Bottom line for (b): the band-width ≤ 1 kernel-optimization problem is SOLVED: optimum = cosine
at α=√2, H = 0.6725007, PROVEN.** There is no hidden better kernel in the class.

---

## (c) VERDICT: the test-function lever is a CEILING, not a lever

- **Is there a known, checkable band-width ≤ 1 test family with H > 0.6725007 in our normalization?
  NO (PROVEN).** The cosine at α=√2 is the global optimum of the class (variational proof + Lean +
  free-grid numeric), and the only numerically-better candidates violate band-width (Claim 2.1).
- **Implication for the record:** our certificate's H(α) input is capped at 0.6725007. The certified
  record 0.673481 ALREADY exceeds it — via the coboundary redistribution (bound = (H(α) − τ)/(1 − B/m),
  τ = psum·(m−6)/m), not via the window. The α=1.464 choice is the best IN-CLASS trade of H against
  the eps-floor; the window itself contributes nothing more.
- **Where the 0.673481 → 0.6818 gap lives (NOT window-shaped):** the paper's own band-width-one
  certificate ceiling is 0.68185 (PROVEN, Lean `Zeta23/PairCeiling`); the repo's class ceiling is
  0.68183123 = p₀ + |E(1)| (LP dual, PROVEN — `attack-ceiling.md`, `idea-generator-neuro.md`).
  Closing the gap needs more of the configuration/multiplicity structure (a better redistribution /
  higher moments / more of the LP dual), not a different test function. Same conclusion as
  `attack-kernel.md` §5 and `anthropic-methodology-mining.md` T12 ("the window is not a lever",
  ABANDONED, PROVEN dead).
- One asymmetry worth noting (CONJECTURED, out of scope): for ξ′ the functional is DIFFERENT
  (D₁ pair density), and there the quartic window genuinely beats both the flat box and the ζ-cosine
  (0.86864 vs 0.85838, constants PROVEN in Lean, mechanism CONJECTURED — `attack-xiprime.md`,
  `attack-kernel.md` §4). That is a real lever for ξ′ but does not transfer to ζ (PROVEN NO).

---

## Honesty ledger

- PROVEN: H(1) = 2/3 = flat-window constant (exact arithmetic); H(√3) ≈ 0.8453 is formal and
  violates λ ≤ 1 (exact arithmetic); the MT constant equals our cosine optimum
  3/2 − (1/√2)cot(1/√2) = H(√2) = 0.6725007; the band-width ≤ 1 window class is closed at the
  cosine (Euler–Lagrange + I+T ≻ 0 convexity + Lean Thm D; free-grid numeric to 1.9e-9).
- CHECKED NUMERICALLY: α→H mapping for α ∈ {√2, 1.464, 1.49} reproduces the record notes' H values
  to all printed digits (mpmath 1-D autocorrelation quadrature; script in (a)).
- CHECKED NUMERICALLY (prior notes, cited): record 0.673481 at α=1.464 (Arb interval verifier,
  3 identical runs); eps=0.0062 exact boundary; class ceiling 0.68183123 (LP dual).
- CONJECTURED: no claim above rests on a conjecture; the ξ′-quartic mechanism remains CONJECTURED
  (out of scope here).
- [CITATION NEEDED] [CCLM17] full author list not in repo bundle; cited by paper §7.1 as "no window
  does better" (one-delta extremal problem). CGdL20 = Chirre–Gonçalves–de Laat (SDP majorants,
  F outside [−1,1]).

## Reproduction

```
cd /home/vstaln/riemann
uv run --with mpmath --quiet python3 -c "
import mpmath as mp; mp.mp.dps=30
def Hcos(a):
    Iv=2*mp.sin(a/2)/a; Iv2=(1+mp.sin(a)/a)/2
    J=2*mp.quad(lambda w: w*((1-w)/2*mp.cos(a*w)+mp.sin(a*(1-w))/(2*a)),[0,1])
    return 2-(Iv2+J)/Iv**2
for a in [mp.sqrt(2),mp.mpf('1.464'),mp.mpf('1.49')]: print(mp.nstr(a,10), mp.nstr(Hcos(a),16))
# → 1.414213562 0.6725007036794116 ; 1.464 0.6724674255777881 ; 1.49 0.6724218860964475
"
```

## Consequence for the search (per hooks: no duplicate levers)

The window lever is closed and documented (this note + `attack-kernel.md` + `anthropic-methodology-mining.md`
T12). Do NOT dispatch further agents on "better test function for ζ at band-width ≤ 1". The funded
direction for 0.673481 → 0.6818 is the redistribution/multiplicity structure (the LP-dual gap
between tawan's p,q and the PairCeiling certificate), which is exactly where the current record
already sits.
