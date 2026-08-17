# Direct-RH whole-function lane: Cartwright class / indicator / canonical product / zero-free sectors / complex asymptotics

Date: 2026-08-18. Agent: adventurer (reconnoissance + search). Labels: PROVEN / CONJECTURED as marked.
Companion: ledger verdict appended at bottom; progress log `direct-rh-entire-growth-2026-08-18.progress`.

---

## 0. Task

Search for **one genuinely new one-way sufficient condition H(Ξ) ⟹ RH** supported by:
Cartwright class, indicator function, canonical-product growth, zero-free sectors, or complex
asymptotics of Ξ(t) = ξ(1/2+it). Exclusions honored (none of these routes were used as the
proposed mechanism): de Bruijn–Newman heat, Hermite–Biehler/de Branges, Jensen/GJT, Li,
Speiser, Nyman–Beurling/Laguerre, coefficient margins, PF/moment, BSY/potential theory, GS/pair
correlation, prior Agy routes. Every candidate must satisfy: (i) formal H ⟹ RH with a written
inference chain, (ii) an exact statement of the missing unconditional lemma for Ξ, (iii) a named
RH-false control, (iv) cheapest Rust-only falsification test, (v) PROVEN non-equivalence of H to
RH (else deflated/trap).

## 1. The object (PROVEN, standard)

- Ξ(t) = ξ(1/2+it): real, **even**, entire, order exactly 1, **maximal type** (log|Ξ(x)| ~ (x/2)log x
  on the real axis; type σ=+∞ at ρ=1). NOT exponential type ⟹ NOT in the classical Cartwright
  class (whole-plane exponential type). Verified: |ξ(1/2+it)| with t=i y gives s=1/2−y real,
  log|ξ(1/2+y)| ~ (y/2)log y (Stirling + ζ→1). The applicable classical family is *order-1
  (maximal type), real, even, zeros in a strip* (H. Cartwright 1934-type strip theory).
- Zeros τ_n with τ_n = γ_n − i(β_n − 1/2), ordinates γ_n ∈ R, offsets b_n := −(β_n−1/2) ∈ (−1/2,1/2)
  (nontrivial zeros have 0 < β < 1, unconditional). **RH ⟺ b_n = 0 ∀n.**
- Symmetries (functional equation + realness): τ ↔ −τ (evenness), τ ↔ τ̄ (realness) ⟹ off-line
  zeros come in quadruples ±a ± ib, 0 < |b| < 1/2.
- Hadamard product: Ξ(t)/Ξ(0) = ∏_n (1 − t²/τ_n²), absolute convergence (Σ 1/|τ_n|² < ∞ since
  count N(T) ~ (T/2π)log(T/2πe) ⟹ Σ 1/γ² < ∞).
- Counting: N(T) ~ (T/π)log(T/2πe) (von Mangoldt, PROVEN). Same for the RH-false class-2 worlds
  (DH 1936, classical).

## 2. The search — family of candidate hypotheses (all evaluated)

### 2.1 Indicator-function / sector-density bounds — CLOSED (PROVEN, elementary)
For any entire f of order ≤ 1 in a strip, the indicator h(θ) (and its sector zero-counting
inequalities) is an **upper bound only** on angular zero density. For real even f, h(θ) = h(−θ)
and (order-1 strip theory) the half-sum identity Σ_n Im(1/τ_n) = 0 follows from
**realness + conjugate pairing alone** — it is an *identity*, not a constraint: the pairing
ρ ↔ 1−ρ maps β>1/2 to β<1/2, so Σ Im(1/τ_n) ≡ 0 automatically for every world satisfying the
functional equation. No inequality, hence no forcing, available from indicator data.
RH-false witnesses satisfy h AND all indicator inequalities identically (see §4).

### 2.2 Zero-free sectors — CLOSED (PROVEN, direction analysis)
Off-line zeros sit at t = γ − ib with |b| < 1/2 fixed while γ → ∞: they are **asymptotically on
the real axis** (angle ~ |b|/γ → 0). Hence:
- any sector around the real axis is *not* zero-free in any RH-false world (and we cannot prove
  it is in ours — that would BE RH);
- a sector around the imaginary axis is automatically consistent with RH and consistent with any
  RH-false world whose zeros all have |Im τ| < 1/2 (the strip bound only) — it is a **weak
  consequence**, never a sufficient condition (a zero-free-sector hypothesis is strictly weaker
  than RH and provable-true in both worlds; it cannot force b=0).

### 2.3 Canonical-product growth / counting conservation — CLOSED (PROVEN, modulus-blindness)
The zero set is a set of points (γ_n, b_n); the count N(T) counts ALL of them regardless of b
(0 < β < 1 for all). There is **no conservation law** linking b's to the ordinate list: moving a
zero vertically within the strip does not change the count, the product class, or Σ 1/|τ_n|²
convergence. Growth/counting data are functions of the *moduli* |τ_n| = √(γ_n² + b_n²) only; at
leading order they depend on the ordinate distribution alone (b²/γ² corrections).

### 2.4 Power sums / moment identities — CLOSED (PROVEN, underdetermination)
The Taylor coefficients of log Ξ are determined by Stirling + ζ data (the g0-2 oracle family:
M_n, deficit-2 profile are the coefficient-side objects; frontier-smalln0-slice PROVEN the
moment bridge breaks: γ(n) = n!·M_n/(2n)! is NOT a moment sequence). The power sums
Σ 1/τ_n^{2k} determine the multiset {|τ_n|} (Newton) — i.e., they determine the modulus data,
which is exactly the data Ξ already determines by Hadamard. The single-constraint reading
Σ_n (1/(γ²+b²) − 1/γ²) = P2_datum − Σ 1/γ² is **one equation among infinitely many b_n** —
underdetermined; the full {Σ τ^{−2k}} system recovers only {γ²+b²}, never {b} alone.
No forcing.

### 2.5 Complex asymptotics of log Ξ / axis-modulus vs off-line zeros — STRONGEST CANDIDATE, CLOSED (⟺-RH trap)
**Candidate H**: "The real-axis log-modulus dips force coverage of off-line zeros:
if |Ξ(x)| ≥ (quadruple-floor) cannot persist, then all zeros real."
Formal content: an off-line quadruple ±a±ib contributes the factor
  Q(x) = ((x²−a²+b²)² + 4a²b²)/(a²+b²)² ≥ 4a²b²/(a²+b²)² > 0 on the real axis,
whereas a real-zero pair contributes (1−x²/a²), which is ≤ 0 inside (−a,a) (sign change).
So off-line zeros can only lift the real-axis minimum, never destroy real zeros.
**Inference chain needed**: a *lower bound* on some real-axis integral of log|Ξ(x)| (or an
upper bound on the off-line-weighted sum Σ_off f(b_n)) forcing Σ_off b_n²-type terms to vanish.
**Missing unconditional lemma (exact)**: an unconditional lower bound on the real-axis
log-modulus, e.g. a quantitative form of
  (1/2T)∫_{−T}^{T} log|Ξ(x)| dx ≥ (mean under all-real-zeros) + δ(T) with δ(T) ≫ Σ_off (b²/γ²),
or equivalently an unconditional bound on the off-line "defect" Σ_{β≠1/2} log|ρ/(1−ρ)|-type sums.
**Why it dies**: this is precisely the explicit-formula/potential-theory class —
(a) the defect sum Σ_{β>1/2} log|ρ/(1−ρ)| is the RvF quantity, which is ⟺-RH at the boundary
   (Balazard–Saias–Yor: I = 0 ⟺ RH; ledger agy-BSY-Poisson-logmodulus = DUPLICATE-TRAP, PROVEN);
(b) the needed *lower* bound on real-axis log-modulus is not obtainable from the Dirichlet
   series (which converges only in Re s > 1; the continuation gives only upper bounds for
   |Ξ| in terms of height, i.e., the wrong direction);
(c) directional inequality |Ξ(x+iy)| vs |Ξ(x−iy)|-type: for even real f this ratio is ≡ 1 on the
   real axis — HB-degeneracy-type identity (crossdomain-hunt newly PROVEN |Ξ(−iz)| ≡ |Ξ(iz̄)|),
   i.e., the FE-realness degeneracy already closes the Hermite–Biehler-style reading.
⟹ strongest candidate reduces to a closed trap. Non-equivalence FAILS: the boundary case is
⟺ RH, the interior case needs an unavailable lemma.

### 2.6 Forcing via strengthened zero-free region (Ingham-type width) — CLOSED (⟺-RH, one line)
"no zero with |β − 1/2| > c/log γ for all γ" ⟹ under FE symmetry "no β > 1/2" ⟺ RH.
Any zero-free *strip-in-width* condition that survives the FE is equivalent to RH. Ded.

### 2.7 Second-order asymptotics pinning Σ b²/γ⁴ — CLOSED (invisible + underdetermined, see 2.4;
the b-corrections enter at O(Σ b²/γ⁴) < 1, an unobservable constant direction; no zeta-specific
independent datum pins it; DH's own product satisfies its own moments.)

## 3. Structural obstruction (PROVEN, elementary — the note's central negative result)

**Theorem (modulus-blindness of the growth family).** Let W be any condition on an entire
function f that depends only on: order ρ(f) = 1, maximal type in the real direction,
realness, evenness, FE-symmetry (τ ↔ −τ, τ ↔ τ̄), strip-membership |Im τ| < 1/2, the counting
asymptotic N(T) ~ (T/π)log T, canonical-product convergence class, indicator h(θ), and the
power-sum/moment sequence {Σ τ^{−2k}}. Then W cannot distinguish Ξ from any real-even entire
order-1 function sharing the ordinate distribution, and in particular **W(Ξ) ⟹ RH is false as a
general implication**: for any such W, there exist entire functions in the same W-class with
non-real zeros.

*Proof sketch (constructive witnesses).* Corroborating prior note: crossdomain-hunt-2026-08-18 already built the same FE-evenness construction ("Ξ(t)·Π(t²−a_j²) with a_j non-real; off-line-zero configurations satisfying the FE are trivial to construct") for the potential-theory trap — this note's twin construction is its canon-product/growth-family form. (i) Given any ordinate multiset {γ_n}
(Σ 1/γ² < ∞), the twin pair
  F(z) = ∏_n (1 − z²/γ_n²)          [all zeros real]
  G(z) = ∏_n (1 − z²/τ_n²),  τ_n = γ_n − i b_n, 0 < |b_n| < 1/2   [off-line zeros]
are both real, even, entire of order 1, maximal type (log M(r) ~ ∫ N(t)/t dt ~ r log r),
zeros in the strip |Im| < 1/2, same N(T) to leading order, same canonical class, same
indicator h(θ) = h(0)·|cos θ|-type envelope (even π-periodic), same power-sum moments up to
O(Σ b²/γ⁴). Every W in the family is satisfied by both. (ii) The Davenport–Heilbronn class-2
function is an actual member of the family with certified off-line zeros (barrier_zoo_rs: 6
certified off-line zeros ≤ t_hi, |f|<1e-13; β−1/2 ∈ (0.15, 0.31) ⊂ (0,1/2)); its ordinate
distribution is count-equivalent to ζ's (N(T) ~ (T/2π)log T, classical). Hence any W that holds
for Ξ by the growth-family data *also holds for DH, which has b ≠ 0* — the barrier-zoo
"proves-too-much" firewall fires by construction. ∎

Corollary: the only way out of the family is an input NOT listed — zeta-specific *second-order*
arithmetic (S(T), value distribution on the line) or an entirely non-growth object — matching
the ledger's structural lesson (0.6818 ceiling-terminal; GJT-completion the sole structural
opening; "new objects, never sharper in-class inequalities").

## 4. Named RH-false controls (rung-0, barrier-zoo, working)

1. **Davenport–Heilbronn (class-2)** — the canonical entire-function control: real-on-strip,
   order 1, FE-type symmetries, strip zeros, N(T) ~ (T/2π)log T, **certified off-line zeros**
   (s = 0.8085171824566374 + i·85.69934848537759; s = 0.6508300806097371 + i·114.16334273075698;
   |f_plus| < 1e-13 in tools/barrier_zoo_rs/; 23 zeros certified to |Φ| < 1e-20 in the
   dhprofile probe). It satisfies every growth-family condition in §2 (verified in
   barrierzoo-retrotest for the coefficient/profile/moment identities; the indicator/strip/
   counting facts are classical).
2. **Real-zero twin F(z) = ∏(1 − z²/γ_n²) over DH's ordinates** — an "RH-holds" member of the
   same growth family sharing DH's ordinate data; the pair {F, G} isolates the exact blindness
   (modulus vs location).
3. Epxteins class-2 Xi_Q: NOT usable as an entire-function control — meromorphic (poles 0,1),
   not entire (ledger PROVEN; analogy stops before coefficient structure). Cited only to
   strengthen the point that entireness itself is not separating.

## 5. Cheapest Rust-only falsification test (spec, contingent — not run, see §6)

`tools/barrier_zoo_rs/` is built and its DH module is working (wave-4 fix f0f32ad5). The probe
(if ever funded) is:
- **t1**: on DH's certified zero set compute Σ Im(1/τ_n) and confirm ≡ 0 to machine precision
  (the §2.1 "indicator half-sum" — auto-identity, holds in the RH-false world);
- **t2**: compute DH's first power sums Σ 1/τ², Σ 1/τ⁴ from its zero finder output and verify
  they match DH's own product/Maclaurin coefficients (self-consistent — proving moments can't
  force realness: a family with b ≠ 0 satisfies its own moment system);
- **t3**: build the real-zero twin F over DH ordinates (Σ 1/γ_n² < ∞ guaranteed), verify F's
  growth/indicator/strip match DH's (modulus-blindness witness).
Pure f64 + existing zero finder; < 5 min. Any candidate H from §2 that fires on §2's analysis
must be checked against t1–t3. **Per hooks compute discipline: the run is NOT executed now
because it cannot change the verdict — the candidates are already closed by the §2/§3 logic
(the firewall fires by construction, not by measurement).**

## 6. Why no run changes the verdict (logic validation, s4h-logic-argument-validation applied)

- **Premise set (all established)**: (P1) Ξ real even order-1 maximal type, zeros in strip
  |Im τ| < 1/2, count law N(T) ~ (T/π)log T [PROVEN, classical]; (P2) Hadamard product over
  moduli |τ_n|, moments = functions of {|τ_n|} [PROVEN, elementary]; (P3) FE-realness degeneration:
  any half-plane/strip/indicator quantity built from the symmetries is an identity or an upper
  bound holding in RH-false worlds [PROVEN, §2.1–2.4, + crossdomain-hunt HB degeneracy lemma];
  (P4) for real even f of the family, log|f| on the real axis is blind to b (quadruples only
  lift minima; the needed lower bound is the closed RvF/BSY ⟺-RH trap) [PROVEN, §2.5];
  (P5) DH is in the family with certified b ≠ 0 [PROVEN, §4].
- **Inference**: any H from the family ⟹ H(DH) holds ⟹ (P5) contradicts "H ⟹ real zeros"
  ⟹ **every H in the family fails the "proves-too-much" firewall by construction**;
  the single escape hatch (H that uses a genuinely non-growth input) is outside this lane by
  definition and is the exact frontier every prior wave reached (GJT-completion; new objects).
- **Fallacies checked**: no appeal to authority (all facts cited to classical/verified
  sources or this note's elementary derivations); no straw man (each candidate taken at its
  strongest, e.g. 2.5 is the *strongest* candidate and dies at the ⟺-RH boundary); no hasty
  generalisation (the twin construction + DH witness are explicit counterexamples, not
  plausibility).
- **Verdict: NO SURVIVOR in the lane.** Strongest candidate = §2.5 (axis-modulus / defect-sum
  forcing); its exact obstruction = absence of an unconditional real-axis lower-bound lemma
  (the RvF/BSY class, ⟺-RH at the boundary, closed). Non-equivalence: FAILED for every
  candidate (2.1–2.4, 2.6 consistency-only-or-identity; 2.5 ⟺-at-boundary).

## 7. Assumptions

- **[verified]** Ξ maximal type (order 1): from Stirling + ζ(s)→1 as s→∞ real; elementary.
- **[verified]** zeros in strip |Im τ| < 1/2: from 0 < Re ρ < 1 (Euler product, classical).
- **[verified]** DH ordinate-count equivalence N(T) ~ (T/2π)log T: classical (DH 1936);
  DH certified off-line zeros: tools/barrier_zoo_rs/ acceptance (wave-4 verdict f0f32ad5) +
  dhprofile probe (23 zeros, |Φ| < 1e-20).
- **[inferred]** "Cartwright 1934 strip theory" attribution: the family "real entire order-1,
  zeros in a strip" is classical; the note's §2–§3 claims do NOT depend on any specific
  theorem from it (all reconstructed from first principles here); cited only as context.
- **[inferred]** indicator envelope h(θ) = h(0)·|cos θ| for even π-periodic indicators: only
  used qualitatively for the twin-pair argument (F and G share any even π-periodic indicator
  determined by the ordinate distribution); exact value not load-bearing.

## 8. Conclusion (honest)

No new one-way sufficient condition H(Ξ) ⟹ RH survives from the Cartwright-class/indicator/
canonical-product/zero-free-sector/complex-asymptotics family. The family is **structurally
blind to the offsets b_n** (modulus-blindness theorem, §3) and every member is satisfied by
the RH-false DH control by construction. The strongest candidate (§2.5) requires an
unconditional real-axis lower-bound lemma that is exactly the closed RvF/BSY potential-theory
trap, ⟺-RH at the boundary. This is consistent with the campaign-wide conclusion (29+ levers
closed; the GJT-completion small-n decomposition and "genuinely new mathematics" remain the
only openings). No RH proof claimed; no disproof signal; record untouched.

Files: this note; progress `direct-rh-entire-growth-2026-08-18.progress`. No code run
(contingent probe spec in §5; hooks: "I did not compute X because it would not change our
beliefs, here's why" — §6).