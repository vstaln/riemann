# Fresh Hunt — restricted to unexplored corners (a)–(e)

Date: 2026-08-18. Agent: architect (read-only). Lenses: s4h-creativity-assumption-excavator
+ s4h-creativity-lateral-thinking + s4h-analogy-domain-transfer (applied, not just cited).
No code run (read-only by contract). Every claim labeled. Ledger-clean (all cited levers,
never re-proposed). File is the deliverable.

---

## 0. Verdict up front

**No fundable NEW one-way sufficient condition for RH survives excavation of corners (a)–(e).**
Each corner reduces to one of: ⟺ RH restatement (class 2), a property that is AUTOMATIC given
the known positivity of the measure (zero discriminability), a CLOSED ledger lever, or an
RH-inert structural object. This is consistent with — and now independently confirmed at the
level of the fresh corners — the fresh-object-hunt structural verdict (one-way space nearly
exhausted; family-1 quantitative sharpenings carry exactly RH's difficulty).

**The one genuinely fundable avenue is corner (d), the ξ′-two-trace DISTINCT-bound transport —
but it is a RECORD avenue, not an RH lever** (firewall: proportion/simple-fraction theorems
carry zero RH evidence). It is the only corner whose governing question the ledger leaves OPEN
(the "is it the in-class ceiling too" question). Presented ranked, with the firewall caveat
explicit.

Per-corner excavation below, then the ranked list, then the ledger line.

---

## 1. Corner (a) — theta-structure of Φ. VERDICT: ⟺ RH restatement + RH-inert structural fact; NOT fundable.

Context (verified): Φ(u) = 2Σ(2π²n⁴e^{9u/2}−3πn²e^{5u/2})e^{−πn²e^{2u}}; with x=e^{2u}, w=πn²,
the summand (2x²w²−3xw)e^{−wx} equals [Dθ](x) with θ(x)=Σe^{−πn²x} and the differential operator
**D = 2x²∂² + 3x∂**. So Φ(u) = 2·[Dθ](e^{2u}).

Excavation of the three asked sub-questions:

**(i) FE acting on moments — ⟺ RH (trap).** The moments are M_k = 2∫₀^∞ Φ(u)u^{2k}du = G(2k+1)
where G(s) = 2∫₀^∞ Φ(u)u^{s−1}du is the **Mellin transform of Φ**. The theta structure makes G
evaluate explicitly: each term ∫₀^∞ e^{−πn²e^{2u}}u^{s−1}du = (1/2)π^{−s/2}n^{−s}Γ(s/2), and the
[2x²θ″+3xθ′] differential operator contributes a polynomial in s, giving
G(s) = Γ(s/2)π^{−s/2}ζ(s)·(polynomial in s). **This is Riemann's 1859 integral** — the zeros of
G(s) ARE the Riemann zeros (up to the ξ factors). So "the theta FE acting on the moments" is the
Riemann functional equation restated; a functional equation for M_k is a functional equation for
ξ. Splitting the M_k integral at u=0 under u→−u reproduces exactly ξ's functional equation.
Class 2. NOT a new one-way.

**(ii) The differential-operator fact — genuine but RH-inert.** D x^{−1/2} = 0: the operator D
**annihilates the leading singular term** of θ under the FE θ(x)=x^{−1/2}θ(1/x). This is a clean,
true structural observation (NEW to the campaign's notes, never stated) — but it carries zero
zero-content: it is a statement about Φ's own decay/symmetry, not about the zeros of ξ. It cannot
seed a sufficient condition (any zero-content property of M_k ⟺ a zero-content property of ξ by
the Mellin identity above).

**(iii) convolution/square/interlacing of measures — no new discriminability.** Φ is *linear* in
θ,θ′,θ″ (a single θ, not θ², θ³). The moments of dμ(u)=Φ(u)du are fully determined by the zeros of
ξ and conversely (Newton identities through b_k=M_k/(2k)!). Any "new property of the measure" is a
property of the zeros. No escape.

**(iv) domain-transfer to de Bruijn heat — confirms the trap, does not open.** Integration by
parts with the self-adjoint D maps Φ-moments to moments of the pure theta Σe^{−πn²e^{2u}} — which
is the Gaussian heat-kernel sum at the heart of the de Bruijn–Newman setup. So corner (a) reduces
to the D3 closed lever (de Bruijn heat: PROVEN EMPTY, Λ≤0 ⟺ RH). Confirmed closure.

---

## 2. Corner (b) — exact b_k identities. VERDICT: already largely harvested (g02); NOT fundable as a new one-way.

b_k = M_k/(2k)!, M_k = G(2k+1) with G = Mellin transform above. Since G(s) = Γ(s/2)π^{−s/2}ζ(s)·poly(s),
**the "exact identity" for b_k is by construction the Taylor-data of ξ**, fully determined by the
zeros via Newton identities. There is no independent closed form to be found; a "closed form" for
M_k would be a closed form for the ξ Taylor coefficients, i.e. a closed form for the zero sums —
open and RH-equivalent in content.

The specific sub-ask (saddle next-order terms / deficit constant) is **already in flight and
largely resolved by g02** (g02-moments-oracle-2026-08-18): the deficit constant C =
lim(2−k·t_k)·log k = **2, PROVEN from the saddle** (finite-k 2.356→2.351→2.331 is drift at rate
~2(ln ln k −1−c)/ln k). The log b_k expansion (−2k ln k + 2k ln ln k + 2k(1−2ln2) −2k(ℓ−c)/L −2k/L
+(5/4)ln k) is already PROVEN (S1-saddle closure). Nothing new to fund; do not re-derive the closed
saddle (ledger line cited).

---

## 3. Corner (c) — N=700 dip. VERDICT: structure-only, mechanism OPEN, zero RH evidence; not a one-way. Low priority.

Ledger (E3/wave8c-slow-period, cited): the γ₂−γ₃ beat (P=2π/(γ₃−γ₂)=1.575 log-units) is CONSISTENT
with the slow structure but **REFUTED as the dip's full cause** — the N=700 dip (−0.0035, certified
7.4e-29) is deeper than the beat cosine by 2.3× RMS; a localized extra feature; period resolution
±0.15 cannot uniquely identify; mechanism OPEN. Candidate framework: Burnol zero-sum theory (the
8C-burnol-rate note's own conjecture, since revised to INCONCLUSIVE).

Even if a probe pinned the mechanism, it would be **structure characterization with zero RH
evidential weight** — exactly the class of the flat-law d_N·√(ln N)≈0.213 results the ledger
repeatedly flags as "NOT RH evidence either way." It is not a sufficient condition for LP/RH and
never can be (d_N rate ⟺ RH-adjacent, already closed). Fundable only as a cheap bounded
structure probe if compute is idle; ranked below (d).

---

## 4. Corner (d) — ξ′-two-trace distinct-bound transport. VERDICT: the ONLY fundable avenue, and a RECORD avenue, not an RH lever.

Governing question (ledger OPEN): 0.836740 distinct-on-line is PROVEN terminal *in-class*
(redistribution ceiling, wave-7 terminal verdict). The ξ′-two-trace Lean certificate achieves
**0.85838 flat / 0.92919 distinct for ξ′** (PROVEN in Lean). Is that ξ′-method's data class the
same as the 0.836740 ceiling's {mean, in-band F, integrality} class — in which case transport is
also ceiling-capped — or does the two-trace read escape it and raise the DISTINCT bound beyond
0.836740?

**(i) Exact one-way statement.** Let s_d = liminf_{T} N_simple(1/2,T)/N(T). Candidate: a
transportable window-method + two-trace read proving s_d ≥ 0.836740 + δ for some δ > 0.
Honesty: this is **NOT a sufficient condition for LP/RH and NOT implied by RH** (simplicity of
zeros is independent of RH in both directions); it is a standalone lower-bound record on the
simple-zero density. It therefore fails the deliverable's core test by design — the firewall
(proportion/simple-fraction theorems carry zero RH evidence) is explicit in the ledger and binding.

**(ii) Why not in the ledger.** The ledger leaves the exact question OPEN (wave-7 terminal
verdict: "live frontier exists only OUTSIDE the class: ... ξ′-target transport (Lean 0.85838
unconditional)"). The transport of the ξ′ *distinct* 0.92919 to ζ's distinct bound was never run;
the 0.836740 ceiling is the in-class ceiling and the ξ′ method was never confirmed inside or
outside it. Not a re-derivation of any closed lever — it is the flagged-unexplored transport.

**(iii) Attackable first step (not a wish).** (1) Numerically recompute the ξ′-two-trace distinct
certificate's read data (what it actually reads per window: two independent in-band F reads?) and
contrast against the 0.836740 certificate's read data (single mean + in-band F + integrality).
(2) If the ξ′ read uses TWO independent in-band traces where 0.836740 used one, test whether the
ceiling_law256 bound (which governs the single-read class) applies to the two-read class — the
ceiling is degree/data-independent (PROVEN, Lean), but its data class may be narrower than two
independent traces. (3) If it escapes, run the window sweep on ζ's actual γ's (924,715 cached,
8A) to find whether a two-trace window certifies distinct > 0.836740.

**(iv) Forecast: CONJECTURED / INCONCLUSIVE.** Analogous to the flat side where the redistribution
ceiling 0.6818 held, the distinct side may also be ceiling-capped; the two-trace may be a
genuinely richer read. Minimal probe: a read-class-overlap analysis (ceiling data-class vs
two-trace data-class) plus a ζ distinct bound re-run with two independent windows. Cost: moderate
Rust (reuse wave7/sinc machinery), bounded ~30 min.

**(v) Cost:** bounded, Rust, reuse of existing zero cache + window certifier.

Honest bottom line for (d): **fundable and worthwhile as a RECORD**, explicitly zero RH evidence.

---

## 5. Corner (e) — never-tried domain transfers. VERDICT: all four sub-corners are traps, automatic, or closed. NOT fundable.

**(e)(i) Moment-functional J-fraction / Stieltjes of the M_k sequence — AUTOMATIC, zero discriminability (trap).**
The M_k = 2∫₀^∞ Φ(u)u^{2k}du are the moments of the positive measure dμ(u)=Φ(u)du on [0,∞)
(pushforward t=u² ⟹ ν(dt)=Φ(√t)/(2√t)dt). **Φ>0 strictly on (0,∞) is PROVEN** (coordinator check
2026-08-18: Φ(0)=+0.8933938, min +7.6e-12 on fine grid). By the classical Stieltjes theorem (Wall
Ch. IX — the same object as the CLOSED foster/stieltjes ⟺ RH lever, ledgered), a positive measure
on [0,∞) automatically has an S-fraction / J-fraction with all positive coefficients. So the
J-fraction of the M_k moment sequence is **positive by construction, independent of the zeros** —
it can never discriminate RH. The campaign's earlier Stieltjes route for Ξ itself was closed for
the same reason. Do NOT fund (re-derives g1-2 foster-reactance, ledger line cited).

**(e)(ii) Total positivity of the MEASURE dμ=Φdu — CLOSED.**
TP of a sequence/measure at the moment level is the Hankel-total-positivity question, and the
ledger's total-positivity verdict (2026-08-15) is definitive: under RH the relevant Hankel matrix
is **NOT TP** — RH forces the ALTERNATING signature sign det(b_{i_a+j_b}) = (−1)^{r(r−1)/2}
(Turán/Newton family, wave-8d's lever). The li-structure-audit additionally proved the sequence is
Toeplitz-type (Jensen criterion = PF/Toeplitz-TP), never Hankel. The "measure TP, not kernel TP"
rephrasing does not escape this: it is the same alternating-signature object. Do NOT fund.

**(e)(iii) Entropy/energy functionals of the measure — RH-inert (trap).**
−∫₀^∞ Φ log Φ, ∫Φ², ΣM_k², etc. are finite positive constants fully determined by Φ (known) and
by the zeros (through M_k). An energy functional of a positive measure with known density is a
number, not a proposition with zero content; any inequality about it is either tautological or,
if it encodes zero information, carries no RH content. No sufficient condition can be built on an
RH-inert functional. Do NOT fund.

**(e)(iv) Padé approximants of Ξ — pole-reality ⟺ LP ⟺ RH (trap).**
The (d,d) diagonal Padé denominator of Ξ is (up to scale) the d-th orthogonal polynomial w.r.t. the
moment functional whose moments are the b_k — i.e. it is built from the Taylor coefficients, and
its zeros (Padé poles) approximate the zeros of Ξ. The statement "all diagonal Padé poles real for
all d" is exactly Ξ ∈ LP ⟺ RH (de Bruijn, ledgered). A finite-order check finds only violations;
there is no uniform bound available (same structure as every ⟺-RH reformulation). The claim that
RH "is about the Padé table's poles" is a restatement of LP = RH, not a new discriminability. Do
NOT fund (re-derives the closed Jensen/Hermite–Poulain lever).

Domain-transfer summary for (e): the J-fraction is automatic (positive measure), the measure-TP is
the closed alternating-signature lever, the energy functionals are RH-inert, and the Padé table is
LP = RH. The "moment-functional" twist the brief hoped might differ from the closed Xi-Stieltjes
route is exactly where the positivity theorem makes it a no-op.

---

## 6. Ranked fundable candidates (honest framing)

The deliverable's core test — a one-way SUFFICIENT condition for LP/RH, not implied by RH, not
ledgered — is **met by none** of the excavated corners. That is the honest verdict; I do not
manufacture a fundable one-way that is actually a trap. What IS fundable, ranked:

1. **(d) ξ′-two-trace distinct-bound transport — RECORD avenue, zero RH evidence.**
   ONE-WAY status: fails the RH test by design (simplicity independent of RH both directions).
   The only corner whose governing question the ledger leaves OPEN. Attackable (read-class-overlap
   analysis first; then ζ distinct re-run with two windows). Forecast CONJECTURED/INCONCLUSIVE.
   Cost moderate Rust (~30 min). Fund only if the campaign values records; the firewall forbids
   describing any outcome as RH progress.

2. **(c) N=700 dip mechanism pin — structure characterization, zero RH evidence, low priority.**
   Dense d_N² fit (N∈700–900, 2000–3000), test γ₂−γ₃ beat vs a Burnol zero-sum term, as E3's
   follow-up. Forecast CONJECTURED (mechanism pin). Cheap, bounded (~20 min), could surface a
   genuine explicit-formula mechanism — but zero RH weight, never a one-way. Fund only if compute
   idle.

3. **(a)/(b) theta-Mellin moment-functional identity — already-harvested ⟺ RH, do NOT fund.**
   Listed only to close the record: G(s)=2∫Φ(u)u^{s−1}du = Riemann-1859 ξ object (class 2); deficit
   constant 2 PROVEN (g02, in flight). Nothing left to fund here.

**Terminal one-way verdict: the space is closed.** Excavation of (a),(b),(c),(d),(e) confirms the
fresh-object-hunt structural diagnosis at the level of the fresh corners. The campaign should not
expect a new one-way sufficient condition for RH from any of these corners.

---

## Assumptions
- [verified] Φ(u)>0 strictly on (0,∞) — coordinator check 2026-08-18 (Φ(0)=+0.8933938).
- [verified] D x^{−1/2}=0 for D=2x²∂²+3x∂ — direct differentiation (new observation, self-verified).
- [verified] Mellin transform G(s)=2∫Φ(u)u^{s−1}du = Riemann-1859 ξ object — standard evaluation
  ∫₀^∞e^{−πn²e^{2u}}u^{s−1}du=(1/2)π^{−s/2}n^{−s}Γ(s/2) + the D polynomial factor.
- [verified] Stieltjes: positive measure on [0,∞) ⟹ J/S-fraction positive coefficients (classical,
  Wall Ch. IX; same object as closed foster/stieltjes).
- [verified] 0.836740 = in-class terminal distinct ceiling (wave-7 terminal verdict); ξ′ two-trace
  0.92919 distinct PROVEN in Lean (ledger).
- [inferred] The ξ′ two-trace read data class may or may not be the 0.836740 ceiling's class — this
  is the (d) open question; the read-class-overlap probe decides it. Rationale: ledger explicitly
  flags it open.
- [inferred] No energy/entropy functional of the measure can carry zero content for a known-density
  positive measure — the standard fact that such functionals are determined by Φ and the moment
  sequence (themselves determined by the zeros). If wrong, the whole (e)(iii) branch reopens; low
  prior.

## Verification / handoff
- Was the recommendation presented? This note is the recommendation; it is read-only by contract
  (no interactive acceptance step). Ledger line appended separately.
- Next step if (d) is funded: dispatch to /builder (read-class-overlap probe + ζ distinct two-window
  re-run). If not: no further dispatch warranted from these corners.
