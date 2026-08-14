# Ihara Reverse Transfer — graph-side structures that suggest NEW input lemmas for the ζ certificate

**Agent:** ARCHITECT (s4h-analogy-domain-transfer + s4h-creativity-assumption-excavator)
**Task:** Reverse-transfer the Ihara sandbox finding (attack-ihara-sandbox.md) into new inequality/input families for the two-moment ζ certificate. Literature/structure only; no compute.
**Date:** 2026-08-14
**Status:** candidates typed as lemmas; labels PROVEN / CONJECTURED / INCONCLUSIVE per honesty charter.

---

## 1. Recap — what made the certificate a rigidity meter in the Ihara sandbox

The Ihara sandbox (attack-ihara-sandbox.md, §3–§4) ran the exact two-moment Weil-form certificate on the Ihara zeta of regular graphs — an object where RH is a *theorem* (nontrivial zeros on |u| = 1/√q iff the graph is Ramanujan). It found the certificate does not measure RH: on RH-true objects it ranges from **−22.9** (coincident-zero Ramanujan graphs) to **+0.98** (rigid lattice). The decisive mechanism is that the certificate is a pure *pair-correlation functional*,

```
cert(g) = 1 − (1/∫ψ²)² · ∫ g(u) Ψ₂(u)² du ,        (∗)
```

so its value is pinned by the realized two-point law g of the zero configuration, not by RH. Three graph-side facts did the work and are the raw material for the reverse transfer: (i) **the zeros come from an explicit algebraic equation** — each adjacency eigenvalue λ solves q u² − λ u + 1 = 0, so every pair {u, ū} is parameterized by one real λ through θ = arccos(λ/(2√q)); (ii) **closed-walk counting** — the power sums pₙ = tr(Aⁿ) = # closed walks of length n are nonnegative integers that *determine* the eigenvalue multiset (Newton identities), i.e. the certificate is secretly a functional of integer prime-side data; (iii) **the coincidence collapse** — repeated eigenvalues make coincident angles, the Gram matrix W = VᵀV/∫ψ² collapses in rank, and the certificate has the exact closed form HS²ₐₙ/N = 1 + (1/N)Σ_groups m_g(m_g−1) + (cross-pairs), giving cert = 2 − N for an N-fold-coincident configuration (PROVEN, verified). All three are unconditionally provable in the graph world; the reverse-transfer question is what each becomes on the ζ side.

---

## 2. The reverse transfer — three candidate inputs

### Candidate A — "Multiplicity-rank identity" (exact decomposition of the certificate into its two channels)

**Graph-side intuition.** Fact (iii): coincident zeros inject an *additive* multiplicity term (1/N)·Σ m_g(m_g−1) into the Hilbert–Schmidt norm, independent of the off-diagonal pair-correlation term. The two channels (multiplicity vs pair correlation) are exactly separated. For ζ all known zeros are simple, so the multiplicity channel is *provably zero* in the tested range — but the current certificate never states this, it merely assumes it.

**Candidate lemma (A).** Let the (rescaled, unit-density) zero configuration have multiplicity groups {m_g}. Then
```
cert = 1 − (1/N)·Σ_g m_g(m_g−1) − (1/N)·Σ_{g≠g'} m_g m_{g'} f(θ_g−θ_{g'}) ,
```
where f is the two-point kernel Ψ₂²/(∫ψ²)². Equivalently, writing m_ρ for the multiplicity of zero ρ,
```
cert = 1 − (1/N)·Σ_ρ (m_ρ² − m_ρ) − (off-diagonal pair term).
```
For a simple zero-set (all m_ρ = 1) the middle term vanishes, so the *entire* 0.6725 deficit is the off-diagonal term — the pair-correlation rigidity, nothing else.

**What it gives.** A clean, exact decomposition that (a) makes the "simple zeros" hypothesis a *visible, additive* term in the certificate rather than a silent assumption, (b) reframes the structural-final-verdict's "new input" requirement precisely: any certificate that *certifies* simple-ness (a lower bound on p₁ = simple fraction) converts to a *provable additive gain* of order Σ(m_ρ²−m_ρ)/N in the bound, and (c) transfers verbatim — the graph closed form in attack-ihara §3 has no graph-specific ingredient beyond "unit density + multiplicity groups."

**Blocker.** For ζ this term is already 0 empirically, so the lemma alone does *not* raise the bound; it only *locates* the missing input. To use it, one still needs an unconditional upper bound on Σ_ρ (m_ρ − 1) — precisely the deep multiplicity theorem the structural verdict names as out-of-reach for current machinery.

**Label:** the lemma identity itself **PROVEN** (verbatim transfer of the graph closed form); its use as a ζ input **INCONCLUSIVE** (needs a multiplicity bound that does not exist unconditionally).

---

### Candidate B — Prime-side bandwidth extension (closed-walk counts ↔ prime pair correlation)

**Graph-side intuition.** Fact (ii) is the sharpest transfer. In Ihara the form factor (Fourier transform of the pair-correlation) extends to *all* frequencies exactly, because the zero set is the spectrum of a finite matrix and its complete statistics are encoded by the closed-walk counts pₙ = tr(Aⁿ) ∈ ℤ≥0 for *every* n — no bandwidth restriction. The two-moment ζ ceiling 0.6818 (PROVEN Lean, attack-ceiling) exists *only because* Montgomery's pair-correlation datum F(α) ≡ 1 is known unconditionally on α ∈ [0,1] and nowhere beyond. The graph setting says: the bandwidth is an artifact of how much prime-side data we can prove; extend the prime data, extend the bandwidth.

**Candidate lemma (B).** Let ψ have Fourier support in [−1−δ, 1+δ], δ > 0. Then the certificate ceiling for bandwidth 1+δ is controlled not by Montgomery's F(α) (unknown on (1, 1+δ]) but by the *prime* two-point data Σ_{n} Λ(n)Λ(n+h), via the Goldston–Montgomery equivalence (pair correlation of zeros ⇔ pair correlation of primes in short intervals, Goldston–Montgomery 1987 — PROVEN equivalence, classical). The unconditionally-proven instance of the prime side is the Barban–Davenport–Halberstam mean-square theorem (primes in arithmetic progressions, PROVEN, classical): for Q ≤ x/(log x)^A,
```
Σ_{q ≤ Q} Σ_{a mod q} |Σ_{n ≤ x, n≡a(q)} Λ(n) − x/φ(q)|² = O(x² / log^A x).
```
**Conjecture-transfer:** the BDH mean-square datum is exactly the input needed to certify a bandwidth-(1+δ) test function, giving an in-class ceiling strictly above 0.6818 on an *unconditional* (mean-square) prime datum.

**What it gives.** A genuinely new input structure: feed the certificate *primes* (Λ in arithmetic progressions), not zero pair correlation. This is the graph's "the certificate is a functional of pₙ" translated literally — pₙ = closed-walk counts become Λ(n), and "pₙ for all n" becomes "prime pair correlation beyond α=1", the only place a higher bound can come from. It also explains *why* V2's in-class target stops at 0.6818 (bandwidth-1 = Montgomery on [0,1] = the only unconditional zero-side datum) and reframes the missing piece as a *prime-side* mean-value that already exists (BDH) rather than an unproven zero-side conjecture.

**Blocker.** The Goldston–Montgomery equivalence is proven in *mean-square* form; the variational problem underlying the certificate ceiling is *pointwise in α*. Whether a mean-square prime datum transfers a pointwise bandwidth extension (and with what constant) is a theorem that has not been written. The BDH bound's O(x²/log^A x) saving also has to be traded against the certificate's normalization — it may yield only a δ → 0 gain unless the logarithmic saving can be sharpened or a second moment in the right range is substituted.

**Label:** **CONJECTURED** (transfer), resting on two PROVEN classical pillars (BDH unconditional; Goldston–Montgomery equivalence).

---

### Candidate C — "Operator eigenvalue parameterization" (the arccos map, and the absence of its ζ analogue)

**Graph-side intuition.** Fact (i): the graph zero set is the *image* of a bounded self-adjoint operator's spectrum under θ = arccos(λ/(2√q)). The certificate is a trace identity on the operator, and the rigidity meter's value is a function of the eigenvalue density (Kesten–McKay pulled through arccos). Crucially, the ceiling in the graph world is *not* 0.68 — the lattice (a legitimately achievable eigenvalue configuration) hits 0.98. The graph ceiling is 1, reached when eigenvalues are uniformly spaced; the ζ ceiling 0.6818 is the signature of a world that *lacks* this operator parameterization.

**Candidate lemma (C).** *Negative structure (INCONCLUSIVE, but load-bearing):* the Ihara algebraic equation q u² − λ u + 1 = 0 has **no ζ analogue** — ξ(s) has no known determinantal/polynomial equation, and the functional equation ξ(s) = ξ(1−s) only pairs ρ with 1−ρ̄, producing the *same* free parameter γ (height) that the certificate already uses. This absence is the reason the ceiling sits at 0.6818 rather than 1: the certificate is a pair-correlation functional (∗) with no operator to supply rigidity beyond the bandwidth-1 datum. *Positive transfer:* any new input structure that beats 0.6818 must *supply* the missing operator — i.e. the certificate must be lifted from the zero set to a Hilbert–Pólya operator H with the ζ zeros as spectrum, and the certificate read as tr(Ψ₂(D)²) on H. Under that lift, the higher zero moments Σ γ^{2m} play exactly the role of tr(Aⁿ) in Newton identities — the *only* invariants that determine the zero set, and the ζ-analogue of closed-walk counts.

**What it gives.** (a) A precise structural diagnosis of *why* the ceiling is 0.6818 (absence of operator parameterization, not a theorem's weakness); (b) a reframing of the already-funded V3/V4/V5 "moment" inputs as the ζ-analogue of Newton identities (tr(Hⁿ)), which is the correct lens for pricing how much each conjectural moment buys; (c) a concrete target: a trace inequality on H (Weil quadratic form on an operator, not on the zero list) is the one input family the graph world proves can reach the lattice's 0.98 rigidity.

**Blocker.** No Hilbert–Pólya operator is known or proven to exist; the higher moments are conjectural (Keating–Snaith/RMT), with no unconditional theorems in the needed range. This is the deepest and least immediately actionable of the three.

**Label:** **CONJECTURED** (the lift and the moment reframing); the negative structural claim (no known algebraic equation for ξ) is a **PROVEN-absence** statement about the literature, flagged INCONCLUSIVE as a ζ *structure*.

---

## 3. Ranking and next step

**Ranking (value to the 0.6818 goal, unconditional anchor, and immediate actionability):**

1. **Candidate B** — the only one that directly attacks the ceiling with an *unconditional* prime-side anchor (BDH) and is the cleanest instance of the graph's core mechanism (closed-walk counts = prime data). Genuinely new input structure, never tried in the certificate.
2. **Candidate A** — immediately actionable (PROVEN identity, Lean-checkable, no compute), but locates the missing input rather than supplying it.
3. **Candidate C** — deepest diagnosis and the correct long-term framing of V3/V4/V5, but rests on a conjectural operator.

**Single best candidate to hand to a builder:** **Candidate B.**

**Concrete next step (for a builder, literature/structure only):** State Candidate B as a precise lemma and check the transfer's one uncertain joint — *does the Goldston–Montgomery mean-square equivalence yield a pointwise-in-α bandwidth extension, or only a mean-square one?* Deliverable: a one-page lemma statement "BHD-mean-square ⇒ bandwidth-(1+δ) certificate ceiling > 0.6818," with the exact normalization trade (the BDH O(x²/log^A x) saving against the certificate's ∫ψ² normalization), the value of δ (if any) it certifies, and the constant it predicts — labeled PROVEN if the pointwise joint holds from the cited theorems, CONJECTURED otherwise. No compute; this is a reduction-argument check against Goldston–Montgomery (1987) and Barban–Davenport–Halberstam.

---

## Assumptions

- `[verified]` All graph-side facts (certificate = pair-correlation functional (∗); closed form HS²ₐₙ/N = 1 + (1/N)Σm_g(m_g−1) + cross; cert = 2−N for coincidence; ceiling 0.6818 PROVEN on bandwidth-1; lattice 0.977/GUE 0.6674) are taken from attack-ihara-sandbox.md and structural-final-verdict.md, read this session.
- `[verified]` The structural verdict's "only lever = new unconditional theorem on p₁ / explicit-formula bound on Σ(m_ρ−1)" is read this session; Candidate A is its precise certificate-level form.
- `[inferred]` The classical literature (Ihara/Bass determinant; Montgomery F(α)≡1 on [0,1]; Barban–Davenport–Halberstam mean-square; Goldston–Montgomery equivalence) is cited from general knowledge and is standard; it was **not** re-derived or fetched this session. No new citation was fabricated; each is a named classical theorem.
- `[inferred]` Candidate B's transfer (mean-square ⇒ pointwise bandwidth) is the untested joint; it is flagged CONJECTURED, not assumed true.

## Alternatives considered (and set aside)

- *Direct re-use of the Ihara certificate as a ζ input:* rejected — the ζ zero set has no finite-matrix realization, so facts (i)–(iii) do not carry as objects, only as structural hints.
- *Higher-moment-only input (V3/V4/V5 as-is):* already funded; Candidate C reframes but does not replace them.
- *Ramanujan/RH-true calibration as an input:* the sandbox itself refuted this (RH-true-ness determines nothing about the certificate).

## Date
2026-08-14
