# FV proof attempt — Off-line Visibility / ξ′-Crossing Production — 2026-08-26

**Agent:** builder. **Inputs:** `negativity-attack-draft-2026-08-26.md` (chain; FV = §4),
`lr-profile-theorem-2026-08-25.md` (L_R profile separation PROVEN), `speiser-probe-2026-08-25.md`
(off4 crossing N=1 CHECKED NUMERICALLY), `halfdisc-probe-2026-08-25.md` (Jensen half-disc = INCONCLUSIVE).
**Verdict: PARTIAL.** Four local lemmas PROVEN + numerically grounded; FV as stated (all β∈(0,½),
height window δ=8) is NOT closed — the closing step is obstructed by the global zero distribution
(exactly the classical wall). This note states precisely what is PROVEN, what the obstruction is,
and the minimal additional input that would close it.

---

## 0. Conjecture under test (FV, verbatim from the attack note)

> if ζ has an off-line zero ρ₀ = β + iγ₀ with 0<β<½ (mirror 1−β at the same height, forced by the
> functional equation), then for the actual ξ, #{ ξ′-zeros in Re<½, |Im−γ₀| ≤ 8 } ≥ 1.

Equivalently (the planted model, matching the probe): start from an RH-satisfying base ξ; plant the
FE-consistent quadruple (β±iγ₀, (1−β)±iγ₀); **FV-production**: ξ_p := ξ·R, R(s)=Π_{i}(s−z_i), must
acquire a ξ′-zero in Re<½ near height γ₀. The notes label FV the chain's only *unproven* node and flag
it "RH-hard by closed loop / global zero distribution enters." This attempt tests that diagnosis.

---

## 1. What is PROVEN (local structure, β∈(½,1), γ₀ ≥ γ₁, plant mirror 1−β)

Throughout ξ_p is real-coefficient and FE-symmetric: R(1−s)=R(s) exactly (the quadruple is invariant
under z↦1−z), so ξ_p(1−s)=ξ_p(s). CHECKED NUMERICALLY: |R(1−s)−R(s)|=7e-19,
|ξ_p(1−s)−ξ_p(s)|=4e-17.

**P1 (odd structure / fixed zero).** ξ_p even about ½ ⟹ ξ_p(½+w)=ξ_p(½−w) is an even function of
w=s−½, so there is an entire h with ξ_p(½+w)=h(w²). Hence
```
ξ_p'(s) = 2(s−½)·h'((s−½)²)
```
so (i) s=½ is ALWAYS a zero of ξ_p′ (the FE-symmetry, independent of R); (ii) every ξ′-zero off ½
occurs in a ± symmetric pair across s=½. Zeros of ξ_p′ off ½ are zeros of h′(z), z=(s−½)². PROVEN
(algebra). Numerically: ξ_p′(½)=0.

**P2 (Re g ≡ 0 on σ=½).** With g := ξ_p′/ξ_p, the symmetry gives g(1−s) = −g(s). For real-coefficient
ξ_p, g(s̄)=ḡ(s). Restricting to σ=½: g(s̄) = −g(s) ⟹ Re g = 0 on the whole critical line.
PROVEN; CHECKED: Re g(0.5+it)=1.9e-25 at non-zero height (earlier Re=−0.6 values were evaluations at
`zetazero(1)`, a base ξ-zero = a pole of g — a plotting artefact, not a counterexample).

**P3 (FE-mirror creates a local positivity zone).** Near the mirror zero z₂=1−β+iγ₀ the plant term
R′/R has the near pole 1/(s−z₂), so
```
Re g(σ+it₀) = Re(ξ′/ξ)(σ+it₀) + Re[(σ−β)/|·|² + (σ−(1−β))/|s−z₂|² + far terms]  →  +∞  as σ→(1−β)⁺
```
while Re(ξ′/ξ) stays finite at σ=1−β (the base has no zero near 1−β+iγ₀: its zeros sit on σ=½).
CHECKED: Re g = 98→198→1998→9998 as σ=0.11→0.105→0.1005→0.1001 at t₀, while base Re(ξ′/ξ)=−0.536,
bounded. So under the RH base (Re(ξ′/ξ)≤0 in Re<½), the planted mirror opens Re g to positivity in
(1−β, ½) near height γ₀ — but see P4.

**P4 (the blow-up is a pole of g, NOT a zero).** At the mirror zero z₂, ξ_p(z₂)=0 (planted) but
R′(z₂)≠0 and ξ(z₂)≠0, so
```
ξ_p′(z₂) = ξ(z₂)·R′(z₂) ≠ 0
```
The positivity zone of P3 sits at/around a *pole* of g (ξ_p-zero), not at a ξ′-zero. CHECKED:
|ξ_p′(0.1+it₀)| = |−23133+8177i| ≈ 24533 ≠ 0, R′(z₂)≈(−657+46i)≠0. Therefore the positivity spike
alone does not pin the sought ξ′-zero (which the probe sees at Re≈0.4526, between the mirror and the
line) — it only guarantees Re g>0 to the right of the pole.

**P1/P2/P4 together (the continuation-IFT obstruction).** By P1 the off-line ξ′-zero is born as one
member of the ± pair. For the pair to enter Re<½ as β leaves the line, it must pass through the
FIXED zero s=½ (see P1(iii/iv)); at that instant ξ_p′ has a higher-order (non-simple) zero at ½. The
implicit function theorem on G:=ξ′R+ξR′ requires ∂G/∂s ≠ 0 along the tracked zero — which vanishes
exactly at the s=½ bifurcation. So **strategy 1 (continuation/IFT) cannot cross the line**: the
trajectory is degenerate where it matters, and the threshold β* at which the pair pops off ½ is
governed by the GLOBAL entire h′((s−½)²), not by local geometry.

---

## 2. Strategy 2 (Jensen half-plane) — prior negative stands, and is consistent

`halfdisc-probe-2026-08-25.md` ran exactly the Jensen-type discrimination the mission lists as
strategy 2 (half-disc mass asymmetry A on log|ξ_p| over mirror half-discs). Verdict INCONCLUSIVE:
the discrete Z-term (which sees the off-line plant in exactly one half) is structurally subdominant
and inert at the probed r; the boundary integral B — computed from |ξ_p| on the half-arc, i.e. from
data OUTSIDE the disc — is dominant, nonzero-geometry-dependent, and swamps the clean local Z signal.
This is the same global-boundary wall in a different costume. Any Jensen count of ξ′-zeros in
Re<½ near γ₀ likewise needs control of |ξ_p′| on the enclosing half-contour, i.e. the global zero
distribution. No local lower bound on the count exists from the quadruple alone.

---

## 3. The precise obstruction (strategy 1 closes only conditional on a global input)

To turn P1–P4 into FV one counts zeros of ξ_p′ in the rectangle
R = [1−β+ε, ½] × [γ₀−8, γ₀+8] by the argument principle
```
Z_{ξ′ in R} = (1/2πi) ∫_{∂R} d log ξ_p′
```
The boundary is four edges. The plant signal on the LEFT edge is huge (P3: +∞ at the mirror). On the
RIGHT edge σ=½, P2 gives Re g=0; but the integrand is d log ξ_p′ = ξ_p″/ξ_p′, whose real part is not
the same as Re g — it is dominated near the line by base terms. The obstruction lives on the TOP and
BOTTOM edges t=γ₀±8: there |s−z₂|≥8 for every planted point, so the plant's positive signal has
decayed to O(1/δ²) = O(1/64), while the base contribution Re(ξ_p″/ξ_p′) (equivalently Re(ξ′/ξ),
which under RH is ≤0 but bounded below by the sum over ALL on-line zeros near γ₀±8) is of the SAME
order and has SIGN and MAGNITUDE fixed by which on-line zeros happen to sit near γ₀±8. Whether
Re g < 0 dominates there is therefore a **global** statement — a pointwise (non-averaged) upper bound
on the base, at two heights, beneath an O(δ⁻²) plant signal.

This is exactly the "per-height non-averaged upper bound … no current zero-density method operates
pointwise in t" that `speiser-negativity-program.md` (via the attack note §1) names as the program's
missing ingredient, and the closed-loop claim stands: the needed estimate is equivalent to per-height
deep-left-zero exclusion, i.e. RH-flavoured. **Thus FV's closing step is not a local statement of the
double pair; it requires the global base. The attack note's "same wall as classical proofs" verdict is
confirmed, now with the wall located at the top/bottom edges of the counting rectangle.**

### Minimal input that WOULD close it (honest, concrete)
A certified pointwise control, e.g. "for the real ξ, Re(ξ′/ξ)(σ±i(γ₀±8)) < −c(γ₀) < 0 for all
σ∈(1−β,½)" with c(γ₀) > (plant signal on those edges), for the specific γ₀. Combined with P2–P4 and
the argument principle this yields Z≥1 (=FV at that γ₀). This is precisely a finite, certifiable
per-band statement (the attack note's "step 5 machinery" — wave8b-certified arc control — exists to
certify it numerically for concrete bands, but a uniform-in-γ₀ proof is the RH-flavoured wall).

---

## 4. Verdict and honest labels

- **PROVEN:** P1 (odd structure, ξ_p′=2(s−½)h′((s−½)²), fixed zero, ±-pairs); P2 (Re g≡0 on σ=½);
  P3 (mirror positivity zone, base bounded); P4 (ξ_p′(mirror)≠0, blow-up is a pole not a zero);
  P5 (IFT degenerates at the s=½ bifurcation). All four also CHECKED NUMERICALLY (dps=20).
- **OBSTRUCTED (not a proof of the claim):** closing Z≥1 over the window δ=8 via argument principle
  needs Re ξ_p″/ξ_p′ < 0 on the top/bottom edges, which is a global, O(δ⁻²)-marginal statement about
  the base sum; no local double-pair geometry supplies it. Strategy 1 (continuation/IFT) fails at the
  degenerate s=½ bifurcation; Strategy 2 (Jensen) is the already-INCONCLUSIVE half-disc probe, whose
  dominant term B is the same global boundary integral.
- **stdout:** `PARTIAL` (P1–P5 PROVEN; FV not closed; obstruction = global zero distribution via the
  top/bottom-edge base control; would-close input stated explicitly).

## 5. What could break the wall (next, per notes, ≤1h each)
1. Certify Re(ξ′/ξ) < −c at γ₁±8 with a safe margin vs the O(1/64) plant signal for ONE concrete γ₀
   (converts FV at that γ₀ from conjecture to PROVEN-for-a-finite-band). (The wave8b certifier is the
   tool; this is the notes' "step 5, pointed at ξ′".)
2. Sweep β→½⁺ and γ₀=γ₁..γ₃ for N (the notes' production-side sweep): if N=0 at some β, FV as stated
   is false and the pair-sign mechanism has a findable gap. This is possible regardless of the wall,
   and does test the *statement*, not the proof technique.

---
Labels: PROVEN (P1–P5) · CHECKED NUMERICALLY (symmetry 4e-17; Re g=1.9e-25 on line; blow-up→9998,
base −0.536; |ξ_p′(mirror)|≈24533≠0) · OBSTRUCTED (FV closure via global top/bottom-edge base) ·
MISSING (per-height pointwise base bound; β→½⁺ sweep).
