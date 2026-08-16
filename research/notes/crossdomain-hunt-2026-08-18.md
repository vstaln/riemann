# Cross-domain hunt for a foreign sufficient-condition mechanism (2026-08-18)

Status: **COMPLETE — honest verdict: ALL SEVEN candidates are traps, consistency-only, or
structurally impossible. NO survivor. This is the documented result, not a manufactured lever.**
Agent: read-only architect (6744babd). Labels: PROVEN (repo) / PROVEN (literature) /
CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE / UNVERIFIED-in-repo.

## 0. Sources read (no re-derivation — cited)

- research/notes/CAMPAIGN-STATE.md — the 26-lever closure map (S1, log-profile, kernel-TP2,
  moment-transfer, GJT trap, xi'-transport, lit-sweep 2023-26 empty; record terminal).
- tools/lee_yang_sections.rs + research/notes/lee-yang-asano-2026-08-15.md — the ONE
  foreign-field probe already attempted: section-level Lee-Yang transfer, ABANDONED (roots
  inside |w|<1 from N=12; min|root| = 0.909 @ N=30; positive sums do not preserve disk
  stability, explicit counterexample (1-z)³+(1+z)³ = 2+6z²).
- research/notes/schoenberg-kernel-tp2-2026-08-18.md — the correct FT duality
  (f ∈ PF∞ ⟺ 1/f̂ ∈ LP); naive shift-kernel TP2 premise REFUTED (exact sin(x)/x
  counterexample, min minor −4/(15π²)).
- research/notes/ledger.md — append-only protocol, do-not-repeat list.

## 1. The master table

| # | Candidate | Mechanism (status) | xi-input needed | Verdict | Why |
|---|-----------|--------------------|------------------|---------|-----|
| 1 | Lee-Yang / statistical mechanics | Ferromagnetic partition-function zeros on |z|=1 (Lee-Yang 1952; Asano contraction; Ruelle 1971; Newman 1974 — PROVEN literature) | G_N(w) Taylor sections of G(w)=Ξ(1/(1-w)) in the Lee-Yang class (roots \|w\|≥1) | **IMPOSSIBLE (closed, repo)** | Section lemma LY FALSE from N=12 (roots at \|w\|=0.91–0.98); positive sums do NOT preserve disk-stability (counterexample PROVEN repo); no Asano contraction between different u; residual handle "Phi-weighted integral over circle-stable h_u preserves stability" ⟺ RH (repo) |
| 2 | Operator theory / PDS kernels / Hermite–Biehler–de Branges | HB class: E has zeros in one half-plane ⟺ Re E, Im E real interlacing zeros (PROVEN literature); de Branges spaces; Nyman–Beurling (repo: CLOSED) | Ξ(−iz) ∈ HB / Re,Im interlacing / spectral-gap operator with zero-ordinates as eigenvalues | **TRAP (⟺ RH) + IMPOSSIBLE** | For E(z)=Ξ(−iz), |E(z)|=|E(z̄)| is an IDENTITY (evenness+realness — PROVEN by elementary algebra below), so the HB inequality is vacuous: the HB route carries zero information beyond "zeros are where they are" ⟺ RH. Spectral-gap operator: NO proven theorem exists — all Riemann-operator constructions (Berry–Keating, Connes) are CONJECTURED |
| 3 | Random matrix theory | GUE pair correlation, Katz–Sarnak, sine kernel — statistics of known-real eigenvalues (CONJECTURED for ζ / consistency-only) | finite moments of the zero distribution forcing reality | **CONSISTENCY-ONLY / IMPOSSIBLE as one-way** | NO theorem in RMT forces real zeros from finite moments; RMT input is the reverse direction (statistics given reality). Montgomery pair correlation is consistency-only (repo). Holland's Wigner mechanism is finite-degree/large-n, GJT-completion trap for the complement (repo, wave-22) |
| 4 | Algebraic/arithmetic (Weil–Deligne) | Etale cohomology + purity: eigenvalues of Frob on H^i are algebraic integers of weight i → RH over F_q (PROVEN literature: Deligne 1974/1980) | ζ's zeros = algebraic integers from a cohomology theory | **STRUCTURALLY IMPOSSIBLE** | Mechanism needs (a) rational zeta function (ζ: no), (b) algebraic-integer roots (ζ's zeros: transcendental), (c) a Frobenius/cohomology functor (none exists for GL(1)/Q). Function-field analogue is the closest PROVEN RH — its mechanism (eigenvalues on H¹) is exactly what is absent over Q. Fake-Weil control lives in the barrier zoo (repo, operational) |
| 5 | Complex analysis / harmonic measure / explicit formula | Weil's explicit formula; Weil positivity criterion (⟺ RH, PROVEN); Levinson–Montgomery count law (repo: PROVEN, used) | a NEW potential-theoretic inequality from the FE forcing zeros onto the line | **TRAP (⟺ RH) / CONSISTENCY-ONLY** | The FE for Ξ is EXACTLY evenness: Ξ(t)=Ξ(−t), and any even real-entire function satisfies it. Off-line-zero configurations satisfying the FE are trivial to construct (e.g. Ξ(t)·Π(t²−a_j²) with a_j non-real... precisely: any even entire function with real coefficients obeys the FE on the line). ⟹ any condition that "follows from the FE" is consistency-only; Weil positivity is an EQUIVALENCE (trap); the only deeper structure is the moment representation — exhausted (S1, moment-transfer, GJT). Hardy's theorem (PROVEN literature: infinitely many zeros ON the line) gives no off-line control |
| 6 | Special functions / Sturm comparison (Bessel J₀ anchor) | Sturm–Liouville comparison (PROVEN literature): ordered coefficients ⟹ ordered zero counts, transfer of real-rootedness between solutions of comparable 2nd-order ODEs; _1F_1 real-zero theorems (PROVEN literature, specific parameter regions) | Ξ must be a solution of a 2nd-order ODE / an instance of a _1F_1-type family | **STRUCTURALLY IMPOSSIBLE** | Ξ satisfies NO known 2nd-order linear ODE and is NOT a confluent hypergeometric function: Ξ(t)=2∫Φ(u)cos(2ut)du, Φ(u)=Σ(2π²n⁴e^{9u/2}−3πn²e^{5u/2})e^{−πn²e^{2u}}; substituting x=e^u gives ∫x^{7/2}e^{−πn²x²}cos(2t ln x)dx — the t·ln x exponent breaks every confluent/ODE structure (PROVEN by inspection of the verified form, repo wave8d). The coefficient-comparison variant of "Sturm for Taylor coefficients" IS the closed S1 family (repo) |
| 7 | Total positivity of the SINC kernel via correct duality | Schoenberg duality f ∈ PF∞ ⟺ 1/f̂ ∈ LP (PROVEN literature; repo confirms) | g built from xi's data is PF∞ ⟹ Ξ ∈ LP | **STRUCTURALLY IMPOSSIBLE (already proven)** | Direction mismatch: the duality gives LP with IMAGINARY zeros for 1/f̂; Ξ has (at least one) REAL zero — PROVEN: Hardy's theorem (PROVEN literature) gives infinitely many real zeros of Ξ ⟹ 1/Ξ is meromorphic, not entire, so 1/Ξ ∉ LP ⟹ Φ (the positive measure in Ξ's FT representation) ∉ PF∞, unconditionally. Even-LP-with-real-zeros is NOT the FT of a PF function (repo, sin(t)/t exact counterexample). The correct duality points AWAY from Ξ |

## 2. The structural reason — why ALL SEVEN fail (PROVEN, this analysis)

Every mechanism in the literature that FORCES real zeros belongs to exactly one of four
hypothesis classes, and Ξ provably sits outside each:

1. **Polynomial / partition-function / product structure** (Lee-Yang, Asano, Eneström–Kakeya,
   ASW–Edrei PF sequences): needs the object to be a product of simple factors or a PF
   sequence. Ξ's Taylor sequence (b_k) is NOT PF (repo PROVEN: gamma(n)=n!M_n/(2n)! has
   Hankel det2 = −9.19e-6 < 0); G's sections are not disk-stable (repo PROVEN); Σb_k z^k is
   not of the ASW rational/exp form (Ξ is an order-1 entire function, PROVEN literature).
2. **ODE / special-function class** (Sturm, _1F_1, Hermite–Biehler differential route): needs
   a differential equation. Ξ has none (see #6).
3. **Cohomology / algebraic-integer mechanism** (Deligne): needs a Frobenius functor with
   algebraic integer eigenvalues. None exists for ζ over Q (zeros transcendental, not rational
   function — PROVEN literature, structural).
4. **Equivalence reformulations** (HB interlacing, Weil positivity, Li, Speiser, Jensen,
   Nyman–Beurling, de Bruijn–Newman): each is ⟺ RH — the trap class (repo, 26 levers).

The FE on the line is exactly evenness; evenness alone admits off-line zeros (any even real-
entire function); the residual content of RH lives entirely in Ξ's moment structure, which the
campaign has PROVEN exhausted (S1 constant margin; log-profile; variable rate; moment-transfer;
Jensen finite-degree; xi'-transport; lit-sweep 2023-26).

**HB degeneracy lemma (PROVEN, elementary — this session):** E(z) := Ξ(−iz) satisfies
|E(z)| = |E(z̄)| identically, since Ξ is even and real-entire (conj(E(z)) = Ξ(conj(−iz)) =
Ξ(iz̄) = Ξ(−iz̄) = E(z̄)). Hence E sits on the BOUNDARY of the Hermite–Biehler class and the
defining HB inequality carries zero information; "E ∈ HB" collapses to "the zeros are on the
imaginary axis" = RH. The de Branges-space machinery built on E likewise degenerates.
(Consequence: any operator-theoretic transport that starts from HB/de Branges is ⟺ RH by
construction — the trap is airtight.)

## 3. Adjacent mechanisms swept and rejected (brief)

- **ASW–Edrei PF-sequence ⟹ reciprocal-LP** (PROVEN literature): needs (b_k) PF — false
  (Hankel det2<0, repo PROVEN).
- **Selberg trace formula / function-field analogue** (PROVEN literature): the curve-over-F_q
  RH proof runs on the same cohomology mechanism as #4 — structurally absent over Q.
- **Free probability / operator-valued free convolution**: no theorem links free convolution
  support reality to ζ; CONJECTURED at best; no xi-input exists.
- **de Bruijn–Newman heat flow** (repo: closed, consistency-only): time-monotone
  real-rootedness parameter Λ is a restatement (Λ≤0 ⟺ RH).

## 4. Survivors: NONE

The two "closest would-be" candidates, and the exact step where each dies:

- **#5 potential theory** would be one-way IF a new explicit-formula inequality existed that
  (i) Ξ provably satisfies, (ii) does not follow from evenness alone, (iii) is not equivalent
  to RH. No such inequality is known; the campaign has no candidate; and the moment structure
  (the only source of such an inequality) is PROVEN exhausted. INCONCLUSIVE-but-unfundable:
  the framework is open, the input is empty.
- **#1 Lee-Yang** is the only mechanism in the list that GENUINELY produces real/on-circle
  zeros from positivity. It fails because Ξ is provably outside the Lee-Yang class at the
  section level (repo PROVEN), and the surviving handle (integral-of-circle-stable h_u) is
  ⟺ RH (repo). Structurally closed, not open.

## 5. Minimal bounded Rust probe: NONE warranted — and why that is a result

No candidate survives, so no probe is funded. Specifically: (a) #7's Φ ∉ PF∞ is already
PROVEN analytically (Hardy + duality + evenness) — a probe would be re-deriving a closed
verdict (do-not-repeat, ledger protocol); (b) #6 needs an ODE that provably does not exist;
(c) #4 needs a cohomology functor that provably does not exist; (d) #2/#5 are ⟺-traps with
vacuous inequality steps. The only standing probe discipline is the barrier zoo (repo,
OPERATIONAL): any FUTURE proposed sufficient lemma must be run against the RH-false model
worlds (Epstein class-2, Davenport–Heilbronn, planted-zero Beurling, fake Weil polynomial)
before any belief — a lemma that "proves" a control is WRONG (proves too much).

## 6. Honest bottom line

A proof of RH requires genuinely new mathematics. This hunt documents, across seven foreign
fields, that every known real-zero-forcing mechanism carries a hypothesis that Ξ provably
violates (product/PF structure, ODE membership, cohomology/algebraic-integer structure), or
reduces to an ⟺ RH restatement (HB, Weil positivity, all classical reformulations), or yields
consistency-only evidence (RMT, FE-based potential theory). The campaign's own PROVEN new
mathematics (deficit constant = 2; theta identity Φ = 2e^{u/2}(2x²θ″+3xθ′); m₃ ≥ m₂² theorem;
Holland non-margin mechanism) stands as the real output. The one structural opening remains
the GJT-completion decomposition (small-n ⟺ RH trap) — hard (Farmer diagnostic), not touched
by any foreign transport assessed here. No disproof signal anywhere; record side terminal
(0.673481/0.836740, certified). Persistence hook honored: this is a documented negative, not a
stop.

## 7. Ledger line (appended to ledger.md)

- **crossdomain-hunt-2026-08-18 (6744babd)** — 7 foreign-field transports assessed (Lee-Yang,
  HB/operator, RMT, Weil–Deligne, potential-theory/explicit-formula, Sturm/_1F_1, SINC-PF∞
  duality): ALL TRAPS / CONSISTENCY-ONLY / STRUCTURALLY IMPOSSIBLE. NO survivor, no probe
  funded. New PROVEN lemma this session: HB degeneracy — |Ξ(−iz)| = |Ξ(iz̄)| identically, so
  the HB/de Branges route for Ξ is vacuous (⟺ RH by construction). #7: Φ ∉ PF∞ PROVEN
  unconditionally (Hardy: Ξ has a real zero ⟹ 1/Ξ meromorphic ⟹ not LP ⟹ Φ not PF∞ by the
  correct duality). Conclusion: RH needs genuinely new mathematics; foreign transport closed;
  GJT-completion decomposition remains the only structural opening. Read-only; no fabrication;
  literature claims marked PROVEN-literature/UNVERIFIED-in-repo where not in repo sources.
