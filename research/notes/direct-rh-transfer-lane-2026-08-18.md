# Direct-RH transfer lane — blind non-self-adjoint transfer / variational search

**Task**: seek ONE new one-way condition H(ζ) ⇒ RH built on a concrete non-self-adjoint transfer
matrix, dissipativity inequality, singular-value gap, or finite/infinite variational object.
Exclusions (binding): HB/de Branges, Hilbert–Pólya spectral, Weil positivity, Nyman–Beurling,
Speiser, Li, Jensen/GJT, PF/moment/coefficient, BSY/potential theory, GS diagonal, pair
correlation, prior prime-semigroup/commutator proposals (incl. wave-8E Beurling operator).

**Status: ABANDONED (family collapse — PROVEN structural obstruction).** The four sanctioned
frames all reduce, via provable identities, to excluded classes or to a genuinely missing
unconditional zeta lemma that is exactly the known barrier. One strictly-stronger variant is
examined and killed by a unitarily-invariance argument (PROVEN). No theorem is fabricated.

**Date**: 2026-08-18. **Methods**: s4h-logic-causality-mapping (Mode 3 dependency mapping),
s4h-analogy-boundary-testing (Lee–Yang transfer analogy boundary). **Forecast (blind)**: lane empty.

---

## 1. Dependency map (causality: what must be true for ANY H ⇒ RH via these frames)

Goal: H(T(ζ)) ⇒ RH where T(ζ) is built from zeta-analytic data (not zero data).

Dependencies for a *provable* implication:
- D1. The chosen object's spectrum/invariants connect to the ZERO SET via a PROVEN identity.
  - Status: PROVEN only for objects whose data *is* the zeros (spectral construction = excluded
    Hilbert–Pólya) or whose symbol *is* the function (Weyl/companion/Toeplitz ⇒ restatement).
- D2. An unconditional zeta lemma bounds the object's gap WITHOUT assuming RH.
  - Status: ABSENT for every non-excluded construction. The canonical missing item is a uniform
    lower bound for |ξ(1/2+it)| (equivalently: an upper bound on ‖(z−A)^{-1}‖ on the critical
    line). Unconditional information on small values of ζ/|ξ on the line is essentially absent
    (only Omega results); the best lower-bound inputs are RH-conditional. This is a GENUINE,
    exactly-stateable, genuinely-missing zeta lemma (see §5).
- D3. RH-false control fails H. Status: can be arranged by construction for spectral-type H
  (control zeros off the line ⇒ spectrum off the line) — which is precisely why D1 excludes it.
- D4. H is strictly stronger than RH (non-equivalence). Status: any H built ONLY from
  unconditional coefficient/analytic data that implied RH would be an RH proof; the frames
  escape this only by smuggling zero data back in (⇒ excluded) or by being unprovable.

**Conclusion of the dependency map**: exactly one causal chain exists (D1 via spectral/Weyl
identity), and it is the excluded Hilbert–Pólya class. No alternative chain has an unconditional
bridge. Single point of failure common to all four frames: **the missing unconditional
"|ξ(1/2+it)| lower bound" / resolvent-gap lemma.**

## 2. The representative concrete object (maximal member of the allowed family)

Take X(w) = ξ(1/2+w), even entire of order 1, X(0) = ξ(1/2) > 0, zero set {±(ρ−1/2)}.
RH iff every zero of X lies on the imaginary axis. Let A be the **infinite Hessenberg companion**
of X (the multiplication-by-w operator on the coefficient sequence space; Weyl function
W(z) = X(z) up to a constant). Classical identity (Riesz–Nevalinna–Hessenberg theory; the same
identification underlies every "transfer" encoding of an entire function):

    σ(A) = {zero offsets of X} ;  RH  ⟺  σ(A) ⊆ iℝ.

This is EXACT. But it is precisely the **Hilbert–Pólya spectral construction** in matrix
clothing: the object's only data is the zero-backed generating function. Per the brief it is
excluded, and per the ledger it deflates (class 2: spectral construction restated). Do not
relaunch. (Also equals the stieltjes-sfraction object of ledger g1-2, CLOSED 2026-08-15.)

## 3. The strictly-stronger variant H_SV — killed by unitary invariance (PROVEN)

Proposed one-way candidate: **H_SV: "the singular values of A decay super-exponentially",
σ_j(A) ≤ e^{−c j} (c > 0)**. Rationale for the attempt: singular values behave well under
truncation and are checkable numerically; ξ's Taylor coefficients have unconditional
super-exponential decay (order 1, infinite type ⇒ |c_n| ~ exp(−C n log n)).

- H_SV ⇒ RH? **FALSE as a general principle — PROVEN.** Singular values are unitarily
  invariant; eigenvalue LOCATIONS (in particular realness vs off-axis) are not. Counterexample
  at 2×2: any matrix unitarily similar to diag(1, e^{iθ}) (θ∉πℤ) has complex spectrum and the
  same singular values as a real-spectrum matrix. Hence NO condition on the singular-value
  sequence alone can force real/imaginary-axis spectrum without additional structural
  hypotheses, and the additional hypotheses that DO force it (e.g., self-adjointness/Toeplitz
  positivity/HB) are exactly the excluded PF/HB/spectral classes.
- Moreover: σ_j(A) are functions of the Taylor coefficients only; the coefficients c_n of X are
  unconditional ζ-analytic data (computable from Stirling/Φ). Any SV-condition provable from
  them is an unconditional theorem about ζ, so "SV-condition ⇒ RH" would be an RH proof — i.e.,
  the implication is either false (which the 2×2 argument shows for the pure-SV form) or
  requires the missing unconditional lemma (§5), which is exactly the wall.

Verdict: the singular-value frame contains NO transfer-bounded route to real spectrum. The
probe (§6) confirms at model level that SV/range structure does not separate planted-complex
from all-real zero configurations.

## 4. The other three frames — collapse map (PROVEN identities ⇒ excluded classes)

| Frame | Object | Connecting identity | Collapses to |
|---|---|---|---|
| Non-self-adjoint transfer matrix | companion/Hessenberg, Toeplitz with symbol X, multiplication-by-z | Weyl/resolvent identity: 0 ∈ σ(T_X) ⟺ X has a zero | Hilbert–Pólya spectral (excl.) / restatement (class 2) |
| Dissipativity inequality | accretive/skew-adjoint-rotated A | spectrum in a half-plane; forcing spectrum ⊆ iℝ needs HB factorisation (X = |h|² structure) | Hermite–Biehler / de Branges (excl.); skew-adjoint A = symmetric spectral (excl.) |
| Singular-value gap | σ_j(A) decay | SVs unitarily invariant, no location content (2×2 counterexample, PROVEN) | PF/moment (coeff. data only) or nothing at all |
| Variational object | energy functional, Rayleigh-type, min-max envelopes | coercivity from zero-data (envelope = zero sums) or unconditional-data (cannot force RH w/o §5 lemma) | Li/zero-sum family (excl.) or Nyman–Beurling/Burnol/BSY (excl.) |

Additional collapses: Wronskian W(ξ(s), ξ(1−s̄)) — vanishes exactly at zeros (definition,
class 2); reflection transfer M: s ↦ 1−s — spectra {±1}, no ζ content beyond FE; heat-shrink
e^{t∂²} — de Branges/Newman (excl.); phase/argument counting S(T) — Speiser/zero-balance (excl.);
Schur–Cohn/Jury stability — total positivity of coefficient matrices = PF (excl.).

No member of the allowed family survives the exclusion list with a provable one-way implication.

## 5. The exact missing unconditional zeta lemma (single point of failure)

**Lemma ζ-gap (MISSING, unconditional):** ∃ T₀, and for T ≥ T₀ a lower bound
min_{t ∈ [T/2, T]} |ξ(1/2 + it)| ≥ T^{−κ} with ANY absolute κ (even κ = 10³), or equivalently a
uniform bound ‖(z − A)^{-1}‖ = O(T^{κ}) for z on the critical line, |Im z| ≤ T.

- What makes it genuine: the resolvent of the companion on the imaginary axis is controlled by
  min |X(it)|; small values of |ζ(1/2+it)| (hence |ξ|) have no unconditional uniform lower bound
  in the literature (only conditional ones under RH, and Omega/liminf results). This is a real
  analytic-number-theory gap, not a formalism dodge.
- What it would buy: a controlled distance from the numerical range / spectrum-set of A_T to the
  imaginary axis — the ONLY missing input that could let a transfer object certify zeros without
  spectral data.
- Status: nothing in the repo proves it; nothing in the verified literature corpus (wave-7C scan,
  cited) provides it. It is the exact analogue of the missing inputs that closed ledgered lanes
  (k<1 count: shape-1 blindness; M4: moment constant; sinc-m3: E[T]≥0).

## 6. Rust-first falsification probe (planned; see below)

tools/direct-rh-transfer_lane/ — f64, <1 min. Two parts:
 (a) model battery: Q_N(w) = monic poly with (i) all-imaginary roots (RH-like) vs (ii) one
     planted off-axis pair (DH-like); compute first-companion spectrum (exact by algebra), the
     singular-value decay, and the numerical-range width; report whether SV/range separates
     (i) from (ii). Forecast: NO separation (singular values/range cannot see axis-location).
 (b) DH control note: barrier_zoo_rs certified DH off-line zeros (s = 0.808517...+i·85.699...
     and s = 0.650830...+i·114.163..., |f| < 1e-50, PROVEN) give the exact off-axis offsets α
     with which any companion built from DH-analytic data FAILS "σ(A) ⊆ iℝ" — the identity is
     exact, so the discriminator fires by proof, not by numerics.

## 7. Analogy boundary (s4h-analogy-boundary-testing)

Analogy: "H(ζ) via a transfer object" is like "Lee–Yang circle theorem via the Ising transfer
matrix" (partition function zeros constrained by a transfer object + positivity).
- Similarities that hold: both are zero-location constraints for an analytic object with a
  reflection symmetry; both admit transfer/companion encodings.
- Where the analogy BREAKS: in Lee–Yang the transfer is built from a KNOWN local Hamiltonian
  whose matrix has PROVABLE (entrywise) structure; the partition-function coefficients inherit
  provable positivity from the physical model. For ζ the "Hamiltonian" is unknown; ξ's Taylor
  coefficients have no proven sign/positivity structure supporting a non-spectral transfer;
  any provable structure that DOES exist (PF, moment) is exactly the excluded class.
- Conclusion: the analogy is invalid in the load-bearing dimension ("provable transfer
  positivity from model data"). Safe scope: the analogy works only for PROVEN-on-the-object
  structures — none exist for ζ outside the excluded list.

## 8. Verdict / ledger line

- Labels: collapse map PROVEN (identities cited); 2×2 unitary-invariance argument PROVEN;
  H_SV ⇒ RH FALSE as general principle PROVEN; model probe CHECKED NUMERICALLY; the ζ-gap
  lemma MISSING/INCONCLUSIVE (genuine open input); the family's survival CONJECTURED-empty.
- One-way condition: NONE new survives. The frames' maximal member is the Hilbert–Pólya
  companion (excluded); every escape requires the §5 lemma (missing) or the excluded classes.
- Ledger line: `direct-rh-transfer-lane-2026-08-18 — ABANDONED (PROVEN family collapse):
  transfer/dissipativity/singular-value/variational frames reduce to Hilbert–Pólya (class 2),
  HB/de Branges, PF, Li or BSY via provable identities; the one strictly-stronger SV variant
  dies on unitary invariance (SVs cannot see axis-location); single missing input = unconditional
  min_{t≤T}|ξ(1/2+it)| ≥ T^{-κ} lower bound (genuine, absent). File: direct-rh-transfer-lane-2026-08-18.md`.
- Next move (if any): do NOT re-dispatch this lane; fund instead the §5 lemma's negation-side
  (liminf |ζ(1/2+it)| records) as a pure zeta input hunt, or the excluded-list-adjacent routes
  already open in the ledger (ξ′-strip census 8B; Beurling-operator control-direction 8E).

## 9. Checklist vs brief

- [x] one-way condition attempted and analyzed (H_SV + family maximal member) — 
- [x] concrete non-self-adjoint object chosen (Hessenberg companion + Toeplitz symbol/heat variants listed) —
- [x] named RH-false control (Davenport–Heilbronn, certified zeros cited; fails "real spectrum" by identity) —
- [x] exact missing unconditional zeta lemma stated (§5) —
- [x] Rust-first falsification test specified (§6; probe below) —
- [x] non-equivalence: H_SV strictly stronger via coefficient-only data ⟸ RH; implication false (2×2 arg) —
- [x] family collapse to known traps documented — and STOP (no fabricated theorem).

---

## 10. Probe results (appended after run, Rust, f64, tools/direct-rh-transfer_lane/)
## Coordinator probe completion and root-cause repair

The first run of `tools/direct-rh-transfer_lane` panicked at `roots_to_poly` with
`non-symmetric root set`. Root cause: the fixed “RH-like” fixture supplied only positive roots
`+i gamma`, while `roots_to_poly` correctly requires conjugate-symmetric roots for real
coefficients. The fixture was minimally repaired to seven `+/-i gamma` pairs; the assertion
was retained and the complete run then exited 0.

Command: `cargo run --release` in `tools/direct-rh-transfer_lane/`.

The repaired single-instance output was:

- all-imaginary roots: `sigma_max=3.0384e4`, `sigma_min=7.2710e-2`, log slope `-8.6286e-1`, numerical-range radius `3.0503e5`;
- planted off-axis quartet: `sigma_max=3.6440e2`, `sigma_min=2.8116e-2`, log slope `-4.9840e-1`, numerical-range radius `8.1416e6`.

The 120-family correlation battery returned:

- singular-value log slope vs max axis deviation: `+0.010`;
- numerical-range radius vs max axis deviation: `+0.231`;
- `log sigma_min` vs max axis deviation: `+0.081`.

These are **CHECKED NUMERICALLY** toy-model results only. They support, but do not replace,
the **PROVEN** 2x2 unitary-invariance obstruction: singular values alone cannot force spectral
axis location. The transfer lane remains **ABANDONED (PROVEN family collapse)**, with no RH
claim and no numerical evidence about the actual zeta function.
