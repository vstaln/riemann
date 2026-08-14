# Adversarial validation: bhb-zeta2-moment-2026-08-14.md (r′ = 3/5 claim)

**Validator:** main loop, in-session (background subagents repeatedly failed to complete this
session; see §7). **Date:** 2026-08-14.
**Target:** `bhb-zeta2-moment-2026-08-14.md` — the claim M = Σ|Bζ″(ρ)|² = (3/5)L²S₂(1+o(1)) and
the box values b ≈ 0.0134/0.0201 derived from it.
**Method:** re-derivation against the fetched BHB paper text (arXiv:1302.5018, ar5iv HTML, in
/tmp/riem_m3/bhb_full.html this session) + independent algebra. Every attack below was attempted.

## Verdict up front

**The note survives the attack set; two labels are downgraded.** (1) The exact constant
r′ = 3/5 is CONJECTURED, not "PROVEN (transfer)": it rests on the un-mollified ζ″-moment constant
(T/2π)L⁵/5 which the note itself tags `[inferred]`, on MF-derivative-independence (unproven), and
on cross-term diagonal subdominance (bounded, not evaluated). (2) "No genuinely new arithmetic
sum" is INCONCLUSIVE: the q = 1 main-term pieces of the ℳ₂-analogue are main-term-scale, not
T^ε-absorbed; the transfer needs the mechanical re-derivation (the note's own §8.1). Everything
else — the residue structure, the FE identities, the Lemma 1 quote, c(S₂) = 57/64 — is confirmed.

## Attack 1: Lemma 1 quote and ℳ₂,₁ coefficient — NOT BROKEN (verdict: VERIFIED)

Fetched the paper (arXiv:1302.5018). Lemma 1 verbatim: S₂ = Σ_{0<γ≤T}Bζ′(ρ)Bζ′(1−ρ) =
(Tℒ³/2π)(1/2 + 3ϑ∫₀¹P(u)²du) − 2Re(ℳ₂) + O_ε(Tℒ^{2+ε}) + O_ε(yT^{1/2+ε}), ℳ_ν =
Σ_{k≤y}Σ_{m≤kT/2π} a_ν(m)b(k)/k·e(−m/k), a₂ from ζ′/ζ·ζ′²·B. The paper's ℳ₂,₁ formula begins
(Tℒ³/2π)(1/12 − ϑ/2∫P + 3ϑ/2∫P² − …) and the paper states "The case q = 1 gives rise to the main
terms" — matching the note's five-term coefficient (1/12 − ϑ/2∫P + 3ϑ/2∫P² − ϑ²/2(∫P)² −
(1/24ϑ)∫P′²) and c(S₂) = 57/64 (script-verified).

## Attack 2: the ζ″(1−s) functional-equation formula — NOT BROKEN (VERIFIED)

The note claims ζ″(1−s) = χ(1−s)[ζ″(s) + 2Lζ′(s) + L²ζ(s)] + O(t^{−1}·(ζ-terms)). Re-derived
independently this session (twice — a first attempt produced a spurious sign error in the
validator's own algebra, caught on the second pass): from ζ′(1−s) = −ζ′(s)χ(1−s) + ζ(s)χ′(1−s),
differentiating gives −ζ″(1−s) = 2χ′(1−s)ζ′(s) − χ(1−s)ζ″(s) − χ″(1−s)ζ(s), and with
(χ′/χ)(1−s) = (χ′/χ)(s) = −L + O(1/t) (the logarithmic derivative of χ is even under
s ↦ 1−s: log χ(1−s) = −log χ(s)) and χ″/χ = L² + O(1/t):
ζ″(1−s) = χ(1−s)[ζ″(s) + 2Lζ′(s) + L²ζ(s)] + O(t^{−1}). CONFIRMED, including the PLUS signs.

## Attack 3: "no double pole at zeros" — NOT BROKEN (VERIFIED)

In the M-integrand B(s)ζ″(s)B(1−s)ζ″(1−s)(ζ′/ζ)(s), the pole at each zero ρ is the simple pole of
ζ′/ζ only; ζ″(ρ) is a finite value (zeros are simple). At s = 1 the product has a pole of order 4
(ζ″ triple + ζ′/ζ simple) — main term only, as the note says.

## Attack 4: the un-mollified constants 1/3 and 1/5 — PARTIALLY BROKEN (labels downgraded)

- **1/3 for Σ|ζ′(ρ)|²:** VERIFIED internally consistent: the B = 1 limit of Lemma 1 (b(k) = δ_{k=1},
  the q = 1 case) gives (T/2π)ℒ³·(1/2 − 2·(1/12)) = (T/2π)ℒ³/3. Also matches the literature value
  (Gonek-type; arXiv search was down this session, cite with care).
- **1/5 for Σ|ζ″(ρ)|²:** NOT VERIFIED. The note's only justification is the 1/(2k+1) pattern
  (k = 1 → 1/3 ✓, k = 2 → 1/5). No computation in the note evaluates it; the honest evaluation
  requires the full diagonal of [ζ″² + 2Lζ″ζ′ + L²ζ″ζ]·χ(1−s) against ζ′/ζ — the note BOUNDS the
  cross terms ("all are ≪ the ζ″² diagonal") instead of evaluating their diagonal, and they are
  in fact L⁵-scale at the s = 1 pole (ζ″ζ′ ~ pole of order 4, ζ″ζ ~ order 4). **The constant 1/5
  (hence r′ = 3/5) is CONJECTURED.** The order claim M = O(L²S₂) is unaffected by this.

## Attack 5: MF-derivative-independence — NOT BROKEN but NOT PROVEN (label stays structural)

c(S₂) = 57/64 = (1/3)(1 + 107/64) is an exact factorization (script-verified), but the claim that
the SAME factor (1 + MF) multiplies the un-mollified constant for every derivative order is a
structural assertion about the mollifier diagonal — plausible (the mollifier multiplies ζ^(m)(ρ)²
as an exterior weight) but not derived for m = 2 in the note. Downgraded accordingly.

## Attack 6: "no genuinely new arithmetic sum" — NOT BROKEN but INCONCLUSIVE

The ℳ₂-analogue has coefficients from ζ′/ζ·ζ″²·B with (log n)⁴ weights. The q = 1 (k = 1) piece
is a genuine main-term-scale sum (partial sums of the coefficient series of a pole of order 4 at
s = 1 are ~ X·(log X)³/6-scale), NOT absorbed into y^εT^ε as the note's "log-powers absorbed"
phrase suggests. The paper's own ℳ_ν,₁ structure carries these explicitly, so the transfer is
structurally sound, but the mechanical re-derivation (note §8.1) is genuinely required before
"no new arithmetic sum" can be called PROVEN. Label: INCONCLUSIVE (transfer plausible).

## Attack 7: the box values — NOT BROKEN (remain CONDITIONAL)

b = 0.0311/(2√r′) ≈ 0.0201 and b = 0.0311/(2√(2(r+r′))) ≈ 0.0134: arithmetic VERIFIED
(`tools/check_bhb_arithmetic.py` §§4–5). Values inherit the CONJECTURED status of r′. With the
pair-form upgrade from the M3 note (E/S₂ ≤ 8b²(r+r′)) the honest box statement is:
b_pair ∈ [0.0758, 0.2237] as r′ ranges over [3/5, 0] (r′ = 0 = ζ″-free ceiling).

## Impact on the milestone chain

- Pair identity (M3), M2 verdicts (FE ζ″-elimination REFUTED), M3 verdicts (Route D GAP, GM
  right-tail Δ > 19/70, left-tail obstruction): UNAFFECTED — none depend on r′.
- b_pair = 0.0758: CONDITIONAL on r′ = 3/5 (as already labeled in the M3 note).
- Route C / M4 (ζ″-moment theorem): still open; the required work is the mechanical Lemma 1
  re-derivation for ζ″ (the note's own next step).

## Scripts

`tools/check_bhb_arithmetic.py` and `tools/check_pair_identity.py` — all checks pass (run:
`uv run --quiet python tools/check_bhb_arithmetic.py`).

## Status of the other two validation targets (same session)

- `bhb-m2-fe-zeta2-elimination-2026-08-14.md`: identities re-derived independently (exact
  decomposition E = S₂ − ΣF(ρ)F(1−ρ); F(ρ̄)−F(1−ρ) = B(ρ̄)δ(ρ) + [B(1−ρ)−B(ρ̄)]ζ′(ρ)/χ(ρ) via
  ζ′(1−ρ) = −ζ′(ρ)/χ(ρ); δ(ρ) = 2(β−1/2)ζ″(1/2−iγ) + O((β−1/2)³) by Taylor about the midpoint
  1/2−iγ of ρ̄ and 1−ρ). NOT BROKEN. Consistent with the M3 pair identity.
- `bhb-m3-density-gap-2026-08-14.md`: pair identity verified numerically (20 random trials,
  machine precision); GM thresholds Δ > 19/70 (sharper), Δ > 17/60 (uniform) verified; left-tail
  worst case re-derived. NOT BROKEN.

## §7 note: why validation ran in-session

Background validator subagents failed three times this session (M2 agent twice, M3 agent once)
with no closing message — an infrastructure failure, not a task failure. Per hooks/agents.md
("try again by a different route") validation was completed in-session; a fresh validator
subagent was attempted once more afterwards for the record.
