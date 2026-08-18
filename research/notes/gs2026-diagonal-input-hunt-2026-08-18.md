# GS-2026 diagonal input hunt — literature audit + mechanism test

Date: 2026-08-18. Agent: research (general-purpose), read-only except this note.
Scope: find ANY unconditional bound on the diagonal pair-count `D(T) := Σ_{γ=γ′≤T} 1` of the form
`D(T) ≤ (C+o(1))N(T)` with `C < 2` — the sole open input of the GS-2026 diagonal bridge
(arXiv 2511.20059). Mechanism-test the five candidate families. Label every claim.

---

## VERDICT (up front)

**NO unconditional C<2 found.** (Label: INCONCLUSIVE-as-literature-fact → verdict "no known such
theorem"; every candidate mechanism is blocked at the mechanism level, PROVEN below.)

I attempted to break the campaign forecast "no unconditional C<2 derivable". I could not. The
reason is structural, not a matter of effort:

> **The diagonal is multiplicity-weighted control of off-line zeros.** `D/N = 1 + (off-line +
> on-line-multiplicity excess)/N`, and every known unconditional input controls either (a) counts of
> off-line zeros [density theorems, Levinson/Conrey on-line proportions] or (b) the total count
> [Riemann–von Mangoldt] — but NONE controls the multiplicity-weighted excess `Σ (m_ρ²−m_ρ)`, which
> is the on-line-sensitive object. Both ingredients (near-line zero control; pointwise multiplicity
> control) are at the level of major open problems. Wave-10's Guth–Maynard closure is a special case
> of this: zero-density cannot reach the near-line band, and even it could, it would not weight
> multiplicities.

**Sharpened target (PROVEN arithmetic):** GS-2026's payoff is "≥ 2−C simple AND ≥ 2−C on-line".
We already have unconditionally: on-line ≥ 5/12 (Pratt–Robles–Zaharescu–Zeindler 2020) and
simple ≥ 1/3 (Levinson 1975; improved since). So a diagonal input only *adds* value if
`2−C > 0.4167`, i.e. **C < 1.5833**; matching the campaign's certified records needs C ≤ 1.3265.
Any "C<2" in (1.5833, 2) is a framework curiosity, not a record improvement.

---

## 0. Conventions — the diagonal must count zeros WITH multiplicity (PROVEN, reductio)

Two natural conventions for `Σ_{γ=γ′}1`:
- (A) zeros listed with multiplicity ⇒ `D = Σ_ρ m_ρ²` (m_ρ = multiplicity of the ordinate γ_ρ);
- (B) zeros listed once per ordinate ⇒ `D = #distinct ordinates ≤ N(T)` trivially.

If GS-2026 meant (B), then `C = 1` is an unconditional input (`D ≤ N`), and the framework would
prove "100% simple AND 100% on-line" — which contradicts the known state (a positive proportion of
zeros off the line is not ruled out; simplicity of all zeros is open). PROVEN (reductio): the
framework's diagonal must be (A), the with-multiplicity convention. Under (A):
`D = N + E`, `E = Σ_{m_ρ≥2} m_ρ(m_ρ−1) ≥ 0`. The campaign's Wave-10 note phrases the same excess
as `Σ_{β≠1/2} m_ρ` (off-line symmetric pairs {ρ, 1−ρ̄} share ordinates); consistent under
multiplicity-2-off-line-only worlds. The context's "(b) diagonal = Σ m_ρ under RH" is convention
sloppiness; under RH, D = Σ m² still needs simplicity for `D ≈ N`.

**Structural identity (PROVEN):** `D(T) ≥ N(T) + Z_off(T)`, where `Z_off` = # off-line zeros
(with multiplicity). Proof: each off-line zero ρ (β<1/2) has twin 1−ρ̄ (β>1/2) with the same
ordinate (functional equation + Schwarz reflection); at an ordinate hosting k off-line pairs,
`m = 2k` and `m²−m = 2k(2k−1) ≥ 2k = #zeros there`. Hence `D < 2N` forces `Z_off < N` — but the
converse fails: `E ≥ Z_off` and the gap (`m(m−1) − m`, on-line multiples, higher multiplicities)
is exactly what is uncontrolled.

---

## 1. Candidate-by-candidate mechanism table

| # | Mechanism family | Status | Why it fails / where it stands |
|---|---|---|---|
| (i-a) | "ζ has no zero of multiplicity ≥ 2" | **NOT KNOWN** (open); ABANDONED as input | Would be revolutionary; no such theorem exists in the literature I can name. Also not known: "no zero of multiplicity ≥ 3", "no double zero". |
| (i-b) | #multiple zeros = o(N(T)) | **NOT KNOWN** (open); ABANDONED | AND insufficient alone: `E = Σ m(m−1) ≤ (max m)·#multiple`; with max m ≪ log T you need `#multiple = o(N/log T)`, far beyond what any known counting argument gives. |
| (i-c) | pointwise `m_ρ ≪ log T` | **PROVEN** (classical, via Riemann–von Mangoldt error term O(log T) in the local zero count) | Best-known general bound; gives only `D ≤ N + N·log T`. No constant bound (i.e. no `m_ρ = O(1)`) is known to me — a constant bound would still be insufficient alone (needs `max m·#off-line < N`). |
| (ii) | Discrete moments `Σ_{ρ simple} 1/|ζ′(ρ)|²` — Gonek conjecture; evaluations by Gonek, Ng, Milinovich–Ng | **CONDITIONAL (RH)**; ABANDONED as a diagonal mechanism | Structurally excludes multiple zeros (1/|ζ′(ρ)|² is infinite at a multiple zero, so the sum is restricted to simple zeros). Carries ZERO information about the diagonal by construction. Conditional anyway (Gonek, Mathematika 1989; Ng 2004; Milinovich–Ng 2014 — exact constants check-me). |
| (iii) | Levinson-type / mollified counting of ordinate-coincidences | ABANDONED at mechanism level | All known mollified counts target zeros ON the line (Levinson 1975 "At least one-third of zeros are simple", Ann. Math.; Conrey 1989 2/5 on-line; Bui–Conrey–Young 2011; PRZZ 2020 5/12 on-line). No known instance targets repeated ordinates. PROVEN inadequate in principle: a lower bound `#simple ≥ cN` does not upper-bound `E` — explicit counter-model: cN simple zeros + (1−c)N zeros clustered at ordinates of multiplicity log T gives `D/N ≈ 1 + (1−c)·log T ≫ 2`. |
| (iii-b) | On-line proportion `N₀ ≥ 2/5 N` (Conrey 1989, PROVEN); 5/12 (PRZZ 2020, PROVEN) | PROVEN but inadequate | Gives `Z_off ≤ 7/12 N` — an UPPER bound on off-line zeros. But `D ≥ N + Z_off` is a LOWER bound on D; `E` (the actual excess) is not controlled. Direction of the inequality is wrong for a C<2 input. |
| (iv) | Density theorems `N(σ,T) = o(N(T))`, σ > 1/2 fixed (Ingham 1940; Huxley; Bourgain; Guth–Maynard 2024) | PROVEN as stated; ABANDONED as C<2 input | No uniformity as σ ↓ 1/2 (exponent → 1); near-line zeros are exactly the S(T)-type obstruction (Wave-10 PROVEN closure). Even a uniform `Z_off = o(N)` would NOT give `E = o(N)` (multiplicity weighting). |
| (v) | Levinson–Montgomery framework for zeros of ζ′ (1974) | PROVEN (N_{ζ′} ~ N(T) in the strip) | Gives `Σ_{m≥2}(m−1) ≤ N + o(N)` — trivial (≤ N); quadratic weighting kills any C<2. |
| (vi) | Bombieri–Hejhal pair correlation ("On the distribution of zeros of linear combinations of Euler products", Duke Math. J. 80, 1995) | **CONDITIONAL (RH-type)**; ABANDONED as unconditional input | Concerns spacing distribution of zeros of Euler-product L-functions under RH — not multiplicities, no unconditional diagonal content. |
| (vii) | Burnol / Beurling–Nyman / explicit-formula Hilbert-space bounds | **INCONCLUSIVE** | I know of NO unconditional multiplicity/diagonal constraint from this circle (Burnol's theta/Hardy-space framework, Beurling–Nyman criterion, de Roton-type refinements — all RH-equivalences or RH-conditional). Specific question to check: does any Burnol-type positivity bound constrain `Σ m_ρ²` or the diagonal of the Weil distribution unconditionally? I cannot cite one; the repo's wave8e Beurling-operator notes (check) pursue the operator route, closed separately (GORTTW firewall). |
| (viii) | Recent ζ′-/multiplicity work (Carneiro–Chirre–Milinovich-adjacent; Chirre; gaps-between-zeros work) | **INCONCLUSIVE** | I cannot name a precise paper from memory that bounds multiplicities of ζ-zeros. Search terms: "multiplicity zeros Riemann zeta function", "Carneiro Chirre Milinovich derivative zeta", "simple zeros proportion 2023 2024 2025". Expected ceiling even if found: O(1)-multiplicity statements, still not `E < N`. |
| (ix) | Decompositions `D ≤ known + small` | ABANDONED | Every natural split (near-line/far-line by δ; simple/multiple; on-line/off-line) reduces to: near-line zero control (open, S(T)-obstruction) + multiplicity weighting (open). No small-remainder candidate is known. |

---

## 2. The single most promising route (if any)

Honest answer: **none is promising; do not fund a new probe on this axis.** Ranked least-hopeless
concrete directions, for the ledger:

1. **Mollified second moment designed to weight ordinate coincidences directly** ("diagonal
   moment"): a Levinson–Conrey-style count whose test function detects repeated ordinates rather
   than zeros on the line. No unconditional instance exists; the arithmetic of such a count is
   genuinely novel territory. INCONCLUSIVE — would need the campaign's moment machinery (already
   PROVEN exhausted on S1/moment-transfer/GJT axes) restructured.
2. **Verify (vii) and (viii) against the actual literature** — cheap, do-once: check Burnol's
   papers and 2023–2026 ζ′/multiplicity preprints (also `research/papers/` + arXiv) for anything
   bounding `Σ m_ρ²` or `Σ_{β≠1/2} m_ρ`. Expected outcome: nothing; that is itself a clean
   negative for the record.
3. **Framework-side**: since 2−C must exceed 0.4167 to matter, keep the certified on-line/simple
   records (PRZZ 5/12; simple-records) as the primary line; the diagonal bridge only pays if it
   beats them, and C<2 inputs do not exist. Record this so future waves do not re-hunt.

Do-not-repeat ledger: this note is a literature + mechanism audit; it re-proposes no mechanism.
Distinct from: Gaussian-Perron (closed), sinc-m3 (REFUTED), LSE symmetry collapse, GORTTW
firewall, wave-10 Guth–Maynard closure (cited, not duplicated).

---

## 3. Honesty section — what would falsify this verdict

1. **A theorem bounding the weighted excess**: any unconditional `Σ (m_ρ²−m_ρ) = o(N(T))`, or
   `#multiple = o(N(T)/log T)`, or a pointwise `m_ρ ≤ C₀`. I found none; none exists to my
   knowledge. A paper proving "the number of multiple zeros of ζ up to T is o(N(T))" would be the
   first hit — I do not believe it is in the literature (it would be famous).
2. **A near-line density theorem with uniformity**: a bound `N(σ,T) ≪ T^{1−c(σ−1/2)}`-type holding
   down to σ−1/2 ≍ 1/log T, strong enough that summing gives `Z_off = o(N)`. Note even this only
   yields Z_off, not the weighted E — the true falsifier is a *multiplicity-weighted* near-line
   estimate.
3. **Mis-remembered conditionality**: if any part of Gonek/Ng/Milinovich–Ng or Bombieri–Hejhal
   were actually unconditional, the table's (ii)/(vi) rows change — they are not (RH-conditional,
   checked against my knowledge; the exact papers to re-verify are listed).
4. **Convention error**: if GS-2026's diagonal is actually convention (B) (no multiplicity), the
   input is trivial and my reductio in §0 shows the framework would over-prove — that falsifies
   the framework's framing, not this note's no-C<2 verdict.
5. **Search terms to run before trusting this verdict**: "multiple zeros Riemann zeta function";
   "multiplicity of zeros zeta"; "simple zeros of the Riemann zeta-function" (records);
   "diagonal pair correlation zeros unconditional"; "Guth Maynard multiplicity"; "Burnol pair
   correlation zeros"; "Carneiro Chirre Milinovich". If any returns an unconditional C<2-type
   bound, this note is superseded.

---

## Claim-label summary

- PROVEN: convention reductio (§0); `D ≥ N + Z_off` identity (§0); `m_ρ ≪ log T` classical bound
  (i-c); Conrey 2/5 and PRZZ 5/12 on-line (iii-b); density-theorem o(N) for fixed σ>1/2 (iv);
  N_{ζ′} ~ N(T) framework (v); mechanism-inadequacy of simple-count lower bounds (iii,
  counter-model); 2−C target arithmetic.
- CONDITIONAL (RH): Gonek-type discrete moments (ii); Bombieri–Hejhal (vi); Montgomery pair
  correlation (framework input (a), per context).
- CONJECTURED: Gonek's asymptotic; simplicity/all-ordinates-distinct conjectures; campaign's
  certified-record C = 1.3265 context.
- INCONCLUSIVE: Burnol/Beurling–Nyman circle (vii); recent ζ′/multiplicity preprints (viii);
  exact current simple-zeros record; exact constants in Gonek/Ng/Milinovich–Ng.
- ABANDONED: (i-a), (i-b), (ii), (iii), (iv), (v), (vi), (ix) as C<2 sources — with reasons above.
