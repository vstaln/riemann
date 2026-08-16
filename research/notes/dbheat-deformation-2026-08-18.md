# de Bruijn heat-deformation lever (wave-20 g2-2): H_t(z) = 2∫₀^∞ e^{t·u²} Φ(u) cos(zu) du — verdict + t<0 zero-tracking probe

Date: 2026-08-18. Agent: builder (dbheat_probe). Status: COMPLETE.
Labels (honesty guardrails): PROVEN = theorem-level; CHECKED NUMERICALLY = f64 probe, non-rigorous.
Companion artifacts: `tools/dbheat_probe/` (Rust), `research/notes/dbheat-probe-results-main.txt`,
`research/notes/dbheat-probe-results-verify.txt` (raw output), `.progress` log.

## 0. TL;DR

1. **DIRECTION VERDICT (PROVEN): the wave-20 t>0 route is mathematically empty.**
   The premise "H_t has only real zeros for every t>0" is *equivalent to RH* (de Bruijn–Newman
   theorem: zeros of H_t all real ⟺ t ≥ Λ; RH ⟺ Λ ≤ 0; Rodgers–Tao Λ ≥ 0, so the premise ⟺
   Λ ≤ 0 ⟺ RH). Proving it is proving RH; the "then take H_t → H_0" limit step (Hurwitz) is
   valid but has no content — the hypothesis is already the theorem.
2. **The "single t>0" version is FALSE (the trap).** Real-rootedness is preserved by
   INCREASING t (de Bruijn), not by DECREASING t. Concrete counterexample verified:
   Φ̃(u)=e^{−(u−5)²}+e^{−(u+5)²}+3e^{−u²} has H_0 with **all non-real zeros** (explicit:
   z=(π+2πk)/5 ± 0.19249i) but H_{0.5} **real-rooted** (explicit: √(2π)e^{−x²/2}(e^{25}cos(10x)+1.5)+O(e^{−25})).
   Heating heals non-real zeros; realness does not flow downward.
3. **t<0 probe (CHECKED NUMERICALLY):** the first 8 zeros of H_t stay real
   (Im ~ 1e-300, quadrature-noise level) for **t ∈ [−0.98, +0.5] in wave8d units**
   (= t_RT ∈ [−3.92, +2]). The first collision among γ₁..γ₈ is **γ₄+γ₅ at
   t_c ∈ (−0.99, −0.98)**, emerging as the conjugate pair **33.1151 ± 0.15054i** at t=−1.0
   (verified by fresh Newton from 4 seeds, |H|~1e-17, no real zeros in [30,36] at t=−1).
4. **What this certifies (honest label): RH-consistent evidence only — NOT a proof step, and
   NOT a disproof.** Note the correction to the dispatch brief: *finding* non-real zeros at
   t<0 does NOT disprove RH — Rodgers–Tao (Λ≥0) + Newman (all-real ⟺ t≥Λ) PROVE H_t has
   non-real zeros for **every t<0** (at some height). The t=−1 pair is exactly that,
   expected under RH. The only non-circular disproof signal in this family is a non-real zero
   of H_t at **t>0** (forces Λ>t>0 ⟹ RH false): **none found** at any t>0 tested
   (t_RT ∈ {0.004, 0.04, 0.2, 0.4, 1, 2}).

## 1. Setup and normalization

- Ξ(t) = ξ(1/2+it) = 2∫₀^∞ Φ(u)cos(tu)du, Φ(u) = 2 Σ_{n≥1}(2π²n⁴e^{9u/2} − 3πn²e^{5u/2})e^{−πn²e^{2u}}
  (wave8d-corrected, VALIDATED: 2∫Φ = 0.4971207781883 = ξ(1/2); zeros at γ₁,γ₂,… reproduced).
- H_t(z) = 2∫₀^∞ e^{tu²}Φ(u)cos(zu)du (backward heat flow ∂_tH = −∂_x²H; entire in z ∀t since
  Φ ~ exp(−πe^{2u}) beats e^{tu²}).
- Unit correspondence: Φ = 2Φ_RT(u/2) ⟹ H_t^{w8d}(z) = 8·H_{4t}^{RT}(2z); DBN constant
  Λ^{w8d} = Λ^{RT}/4. All t below are wave8d units; t_w8d=0.5 ⟺ t_RT=2.
- Theorems used (PROVEN, cited): Newman 1976 — zeros all real ⟺ t ≥ Λ; RH ⟺ Λ ≤ 0;
  Rodgers–Tao 2018 (Forum Math Pi) — Λ ≥ 0; Polymath 15 (1904.12438) — Λ < 1/2.
  Hence RH ⟺ Λ = 0, and for EVERY t<0, H_t has non-real zeros (t < 0 ≤ Λ).

## 2. Direction verdict (PROVEN)

- "H_t all-real for every t>0" ⟺ [0,∞) ⊆ [Λ,∞) ⟺ Λ ≤ 0 ⟺ RH. **EMPTY route** (wave-20 Idea 3,
  `wave20-swarm-harvest-2026-08-15.md`: premise is a restatement of RH; the Hurwitz limit step
  H_t→H_0 (uniform on compacta, t→0⁺) is valid but presupposes the theorem). See also
  `attack-jensen-ometer.md` ("heat-flow margin is exactly 0; RH ⟹ Λ=0") and
  `lee-yang-integral-handle.md` ("dBN: no closure theorem") — consistent ledger.
- "H_t real-rooted for one t₀>0 ⟹ H_0 real-rooted" is FALSE. Counterexample (PROVEN + CHECKED):
  Φ̃(u) = e^{−(u−5)²}+e^{−(u+5)²}+3e^{−u²} > 0, G_t(z) = ∫₀^∞ e^{tu²}Φ̃ cos(zu)du.
  G_0(z) = ½√π e^{−z²/4}(3+2cos 5z); zeros solve 2cos(5z) = −3, i.e.
  z_k = (π+2πk)/5 ± (i/5)ln((3+√5)/2) = (π+2πk)/5 ± 0.19249i — ALL NON-REAL.
  G_{0.5}(x) = √(2π)e^{−x²/2}(e^{25}cos(10x)+1.5) + O(e^{−25}) — ALL REAL zeros
  (cos(10x) = −1.5e^{−25} has real solutions). So heating created real zeros from a
  non-real-rooted H_0: real-rootedness is not preserved as t decreases.
  (Gaussian-decay example is outside Newman's theorem's class; it serves only to exhibit the
  failure of the single-t implication. The Riemann case is settled exactly by §2 first bullet.)

## 3. Method (Rust, f64, non-rigorous — CHECKED NUMERICALLY)

- `tools/dbheat_probe/src/main.rs`. Evaluates H_t(x+iy) = 2∫₀^∞ e^{tu²}Φ(u)[cos(xu)cosh(yu) − i sin(xu)sinh(yu)]du
  and H_t'(z) = −2∫₀^∞ u e^{tu²}Φ(u)[sin(xu)cosh(yu) + i cos(xu)sinh(yu)]du by
  Richardson-doubled composite Simpson on [0,6] (integrand mass at u≲1; tail < 1e-30 even at
  t=0.5 — Φ's super-exponential decay means no spike-shifting). Complex Newton for zeros.
- t=0 validation: roots reproduce γ₁..γ₈ (abs error ≤ 2e-6 at γ₈; limited by the envelope
  |Ξ(t)| ~ e^{−πt/4} ~ 2e-15 at t=43, so |H'|(γ₈) ~ 2.5e-12; the quadrature itself is
  1e-17-accurate — verified by n-doubling).
- Zero tracking: continuation seeded from published γ₁..γ₈, Newton from (prev, ±1e-3i);
  off-axis threshold |Im| > 1e-4 (≫ noise ≤ 1e-6). Collision pinned by counting real-axis
  zeros of H_t in [31.5,34.5] (no Newton identity assumptions).

## 4. Results (raw: dbheat-probe-results-main.txt / -verify.txt)

### 4.1 t<0: first 8 zeros stay real down to t = −0.98 (wave8d units)

Selected rows (Re of the zero; Im is the converged imaginary part):

| t | γ₁ | γ₂ | γ₃ | γ₄ | γ₅ | γ₆ | γ₇ | γ₈ | max|Im|
|---|----|----|----|----|----|----|----|----|------|
| 0 | 14.1347 | 21.0220 | 25.0109 | 30.4249 | 32.9351 | 37.5862 | 40.9187 | 43.3271 | (0) |
| −0.01 | 14.1463 | 21.0371 | 25.0226 | 30.4440 | 32.9443 | 37.6030 | 40.9359 | 43.3360 | ~1e-30 |
| −0.1 | 14.2508 | 21.1736 | 25.1277 | 30.6185 | 33.0259 | 37.7548 | 41.0922 | 43.4143 | ~1e-30 |
| −0.5 | 14.7187 | 21.7930 | 25.5885 | 31.4594 | 33.3290 | 38.4469 | 41.8414 | 43.6940 | ~1e-30 |
| −0.9 | 15.1918 | 22.4352 | 26.0354 | 32.5535 | 33.3874 | 39.1691 | 42.8120 | 43.7264 | ~1e-30 |
| −0.95 | 15.2514 | 22.5173 | 26.0901 | 32.7658 | 33.3197 | 39.2615 | 42.9925 | 43.6694 | ~1e-30 |
| −0.98 | (only γ₄,γ₅ measured here: 32.9544, 33.2179 — both real) | | | | | | | | ~1e-30 |
| −0.99 | (γ₄,γ₅ merged: 0 real zeros in [31.5,34.5]) | | | | | | | | pair |
| −1.0 | 15.3109 | 22.5998 | 26.1444 | **33.1151 ± 0.15054i** (γ₄&γ₅ merged) | — | 39.3544 | 43.2629 | 43.5219 | 0.1505 |

(γ₄,γ₅ merge between t=−0.98 [2 real zeros: 32.954, 33.218] and t=−0.99 [0 real zeros]. At
t=−1.0 the conjugate pair is at 33.1150940 ± 0.1505390i, verified by fresh Newton from 4
seeds with |H| ~ 1e-17; no real zeros of H_{−1} in [30,36].)

### 4.2 t>0: no off-axis zero in the RH-relevant window (no disproof signal)

t ∈ {0.001, 0.01, 0.05, 0.1, 0.25, 0.5} (t_RT = {0.004, 0.04, 0.2, 0.4, 1, 2}): all first-8
zeros real, Im ~ 1e-300, Re monotone decreasing (e.g. t=0.5: 13.56, 20.28, 24.42, 29.52,
32.43, 36.77, 40.10, 42.83). A non-real zero here would force Λ>t>0 (RH false); none found.
(Note: t=+1.0 row is contaminated by tracking hops j3/j4 and j6/j7 — flagged unreliable, not
interpreted; t_RT=2 (=t_w8d=0.5) is provably real by Polymath's Λ<1/2 anyway.)

### 4.3 Counterexample (PROVEN + CHECKED NUMERICALLY)

- G_0: Newton confirms z = 0.6283185 ± 0.1924847i (analytic: π/5 ± 0.19249i). ✓
- G_0.5: real-axis zeros at x = 0.15708, 0.47124, 0.78540, 1.09955 — match (π/2+kπ)/10 ✓;
  tracked pair's |Im| → 1e-38 already at t=0.05 (collision in (0, 0.05)), stays 0 to t=0.5. ✓

## 5. Honest labels and what this certifies

- **"t>0 direction": EMPTY (PROVEN).** The wave-20 premise is equivalent to RH via the DBN
  equivalence (Newman: all-real ⟺ t ≥ Λ; RH ⟺ Λ ≤ 0; RT: Λ ≥ 0). Any proof of "H_t all-real
  for all t>0" is a proof of RH; the limit step adds nothing.
- **"t<0 probe": CHECKED NUMERICALLY — RH-consistency evidence at best.** Λ ≤ 0 ⟺ RH makes
  t<0 real-zero persistence *equivalent to RH* for the full zero set; the probe checks only
  finitely many (first 8) zeros, so it is not a proof step in either direction. All 8 stay
  real down to t=−0.98; the γ₄+γ₅ collision at t_c∈(−0.99,−0.98) → 33.1151±0.15054i at t=−1
  is *expected* (Rodgers–Tao + Newman PROVE non-real zeros exist for every t<0).
  **Correction to the dispatch brief:** "finding t₀<0 with non-real zeros would DISPROVE RH"
  is wrong — under RH (Λ=0) non-real zeros are forced at every t<0; such a finding is
  RH-consistent, not a disproof. The t=−1 pair is that phenomenon.
- **No RH claim is made.** The probe is a consistency check of the DBN flow's low zeros and a
  demonstration of the direction trap; it cannot distinguish RH from ¬RH (any t<0 outcome is
  RH-compatible, and t>0 outcomes in the tested window are provably real when t_RT ≥ 1/2).

## 6. Ledger / follow-ups

- Add to ledger: **dBN heat-flow lever g2-2 — ABANDONED as a proof route (PROVEN empty:
  premise ⟺ RH); t<0 low-zero table recorded (first-8 collision γ₄γ₅ at t_c∈(−0.99,−0.98),
  pair 33.1151±0.1505i at t=−1, wave8d units; RH-consistent).** Do not re-dispatch: the
  direction analysis is complete; the only open numerical question (a rigorous Λ computation
  with certified interval arithmetic on H_t zeros for t>0) is bounded by Polymath (Λ<1/2) and
  cannot reach Λ=0 — it would at best sharpen a numerical Λ upper bound, which is a finite
  numerical check, not a proof step.
- Possible cheap follow-up (not RH): certify with interval arithmetic that the first 8 zeros
  of H_{−0.5} are real (rigorous consistency certificate), if the project wants a certified
  artifact instead of an f64 probe.
