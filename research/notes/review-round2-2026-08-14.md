# Review Round 2 — Adversarial Validation (2026-08-14)

**Reviewer:** adversarial validator (read-only; deliverable written by the main loop per role split).
**Scope:** five round-2 notes (a)–(e), validated against primary sources `baluyot-etal-2306.04799.txt`,
ar5iv full text of `arXiv:1302.5018` (BHB), ar5iv full text of `arXiv:1106.1160` (Milinovich–Ng), and the
2603.28104 abstract. Skills applied: s4h-investigation-counter-hypothesis, s4h-logic-argument-validation.

## 1. Per-note verdicts

| Note | Verdict | Severity |
|---|---|---|
| (a) scale-gap-lemma | **VALID** (one scope-precision fix required) | minor |
| (b) gs-pcurve-boxwidth | **VALID** (one label-protocol nit) | minor |
| (c) gm-bandwidth-joint | **VALID** | — |
| (d) bhb-lemmaN-firstcheck | **VALID** (self-labeled INCONCLUSIVE is correct) | — |
| (e) xitower-G-explicitformula | **VALID** | — |

## 2. Confirmations (verified against sources)

**(a) Scale-gap lemma — PROVEN, correct, but "CLOSED" needs the fixed-σ qualifier.**
- Functional-equation pairing: for ρ=(1/2+ε)+iγ, the partner under ρ↦1−ρ̄ is (1/2−ε)+iγ. The symmetry
  forces an equal split, correctly captured as N(σ_b,T) ≤ M(T)/2.
- von Mangoldt: 2m = 2⌊(T/4π)L⌋ = (T/2π)L + O(1), matches to main term.
- Scope boundary holds: F is pure fixed-σ count-inequalities; moment inputs are excluded and correctly
  identified as a different class. The "moment caveat" is a scope statement, not a proof gap.
- **Minor issue:** the witness C_T is a zero *configuration*, not an actual ξ-function; consistency with
  the full Riemann–von Mangoldt explicit formula or Hadamard factorization is NOT checked (outside the
  premise set). Fine for the lemma as stated; §9's flat "CLOSED" needs the fixed-σ qualifier because
  BGSTB's density hypothesis (1.6) is asserted down to the moving boundary and WOULD imply the box.

**(b) P(b) — faithful, all constants verified.**
- `baluyot-etal-2306.04799.txt`: box (1.5) is |β−1/2| < 1/(2 log T) = the b=1 case — parent note's
  "P(1/2)" anchor is an error. Confirmed.
- Box enters only as the fixed threshold 1/log T, not a parameter: "P(b) constant, gate at b=1" faithful.
- 0.617483786 = 2 − 1.289389678/(2×0.466319912); hand arithmetic reproduces (2×10⁻⁹ rounding noise).
- 2603.28104's 2/3 is a different kernel/mechanism (Fejér generalization of Montgomery), b→0, "simple
  AND on the critical line" — the "no continuous P(b) interpolation" refutation holds.
- sup_b P(b) ≤ max(2/3, 0.61748) = 2/3 < 0.6818. ✓

**(c) GM87/BDH — GM87 statement correctly cited, δ=0 reduction sound.** GM87 as RH-conditional
equivalence of two L² variance asymptotics, each ⟺ Montgomery PCC, is correct (consistent with BGSTB's
own citation). "Equivalence, not a datum" and "L² cannot recover F pointwise" are sound. BDH log-power
moduli vs fixed-δ needing q ~ x^{1−δ} is robust qualitatively; the δ=0 verdict does not depend on the
exact exponent. ✓

**(d) BHB Lemma N — notation correction verified verbatim.** ar5iv 1302.5018, Lemma 1: "S₂ :=
Σ_{0<γ≤T} Bζ′(ρ)Bζ′(1−ρ)" and "Assuming RH we have S₂ = Σ_{0<γ≤T}|Bζ′(ρ)|². Note that this is the only
place we need RH." The mollified object is F=Bζ′, not B′; the correction is right. Good-part arithmetic
verified by hand (P(u)=−ϑu²+(1+ϑ)u at ϑ=1/2: ∫P²=17/40, ∫u²P²=33/140, r_diag=99/1274≈0.0777, b≈0.0558;
net-S₂ 57/64 gives b≈0.0494). ζ″-blocker correctly identified as outside Lemma 1. ✓

**(e) Gonek constant — verified verbatim, all three findings correct.** ar5iv 1106.1160, (1.1):
Σ_{0<γ≤T} 1/|ζ′(ρ)|² ~ (3/π³)T; (1.3): ≥ (3/(2π³)−ε)T. Prior notes' "(6/π³)T log T" is wrong on both
counts. M₂=(3/π³)(ϑ+ϑ²)T log²T, M₁=(3ϑ/π³)T log T verbatim. ξ′ normalization via Stirling re-derived,
correct. G_ξ ≫ e^{πT/2} and the vanishing Cauchy ratio are correct. ABANDONED verdict well-supported. ✓

## 3. Issues by severity

- **issue (minor) [fix] — note (a) §9 "CLOSED" overreaches without the qualifier.** Amend §9/§10 to read
  "closed for fixed-σ density families (Guth–Maynard-type)"; add: "a density hypothesis extended down to
  the moving boundary 1/2+c/log T (BGSTB (1.6)-style) is a distinct, correctly-scaled input that WOULD
  imply the box." **(APPLIED 2026-08-14.)**
- **issue (minor) [fix] — note (a) witness is a configuration, not a function.** Add to §8 assumptions the
  parenthetical "(as a statement about zero configurations satisfying (1)–(3)); explicit-formula/Hadamard
  consistency not checked." **(APPLIED 2026-08-14.)**
- **nitpick (minor) [fix] — note (b) "CHECKED NUMERICALLY" without a script.** Relabel to "verified
  against paper §7 (hand arithmetic)" or run the mpmath snippet. **(APPLIED 2026-08-14: relabeled.)**
- **nitpick [dismiss] — note (b) "Montgomery–Taylor at 67.2%"** should be 67.25%; immaterial rounding.

## 4. What was verified and what was NOT

**Verified:** all five notes' load-bearing constants and quoted statements against the cited primary
sources. Every PROVEN-labeled claim that could be checked against a source held up.

**NOT verified:** (i) note (a)'s explicit-formula/Hadamard consistency of C_T (outside its premise set);
(ii) note (c)'s exact BDH statement and AP↔gap dictionary exponent (marked `[inferred]`; qualitative δ=0
independent); (iii) note (d)'s M₂^Q off-diagonal term in the "B′ transfer" (asserted to shift the constant
not the L-power; hedged); (iv) note (b)'s Fejér 2/3 proof details (self-labeled INCONCLUSIVE).

## 5. Recommendation

**Approve all five notes** with the two named fixes to (a) and the one relabel in (b) — all applied
2026-08-14. No claim downgraded from PROVEN to CONJECTURED; none of the ABANDONED/INCONCLUSIVE verdicts
is premature.

## 6. Verification commands

```
grep "0.617483\|1.289389678\|0.4663199124" research/papers/baluyot-etal-2306.04799.txt
curl ar5iv.labs.arxiv.org/html/1302.5018   # Lemma 1: S₂ = Σ Bζ′(ρ)Bζ′(1−ρ); "only place we need RH"
curl ar5iv.labs.arxiv.org/html/1106.1160   # (1.1) = (3/π³)T, (1.3) = (3/(2π³)−ε)T
```
