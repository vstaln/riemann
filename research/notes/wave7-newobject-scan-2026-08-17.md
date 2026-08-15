# WAVE 7 (7C) — NEW-OBJECT FRONTIER SCAN: where (if anywhere) the 0.6818 class ceiling breaks

**Agent:** adventurer (joint 7C). **Date:** 2026-08-17. **Status:** COMPLETE.
**Question:** the 0.6818 ceiling is PROVEN (Lean, modulo EnclOK) for the rank-trace/pair-correlation
certificate class reading {mean density, form factor F on [0,1], integrality}. Can ANY genuinely new
object/input break it? Scan of the verified-literature corpus (`research/papers/`, `research/external-results/`,
`research/notes/`) for the three candidate classes of the brief.

**Bottom line up front:** all three classes are EMPTY of enterable inputs. 0.6818 is the **terminal ceiling**
for this certificate class and **0.6734808616745137 the terminal in-class record** — the frontier is closed
*inside* the class, in the precise sense that no PROVEN object in the corpus (a) evaluates the form factor
at |α| > 1, (b) gives an unconditional simple-fraction above 0.6818, or (c) supplies a proven new input that
the certificate can consume. Live frontier exists only *outside* the class: ξ′-target transports (Lean
0.85838 unconditional) and the explicitly-conjectural regime. One in-class hole remains bounded by the
ceiling: the 0.6725 → 0.6818 window-vs-class-optimum gap (dual certificate, keep-alive from attack-ceiling §4).

---

## 1. The certificate class and the ceiling (recap, from attack-ceiling.md)

- A certificate is (c₀, r), r ∈ C¹[0,1], value v = c₀ + ∫₀¹ r(x)x dx, valid iff c₀ + Σ_j s_j r(j/N) ≤ p₁ for
  every configuration; inputs = mean density, F on [0,1], integrality (attack-ceiling.md §1; paper Remark 1.1).
- Ceiling: there exists a legitimate 256-periodic near-CUE marked configuration (exact rational weights,
  marks ∈ {1,2}, F matching CUE to 3·10⁻⁴⁰ on [0,1], simple fraction p₀ = 0.6818286874638…) against which
  every certificate is forced to v ≤ 0.6818287 + 2.5431316·10⁻⁶·(|r′(1)| + V(r′)). `ceiling_law256_signed`
  PROVEN in Lean, axioms {propext, Classical.choice, Quot.sound}; EnclOK is the one numerically-checked
  (INCONCLUSIVE-as-of-r3, not refuted) link (attack-ceiling.md §1). Any beyond-bandwidth-1 datum or any
  structural constraint excluding the near-CUE law would break it; none exists (attack-ceiling.md §3–4).
- In-class record (unconditional liminf, validated by 5 referees): simple-on-line ≥ 0.6734808616745137,
  distinct ≥ 0.8367404308372568; inputs (i)–(v) all unconditional; 6B/6D/6E (wave6-synthesis-2026-08-17.md
  §"What the record proves").

---

## 2. Class (a): PROVEN form-factor estimates for |α| > 1 — VERDICT: EMPTY

**Candidate a1 — BGSTB24 / BGST Thm 1 (unconditional Montgomery theorem).**
- Exact statement (local, verified): `research/papers/baluyot-etal-2306.04799.txt:49–50` — "Theorem 1. The
  function F(α) is real, even, and nonnegative. Moreover, as T → ∞, we have (1.4) F(α) = T^(−2α)(log T + O(1))
  + α + O(1/√log T)" (F via the w(u) = 4/(4−u²) kernel, line 37; proof lines 498–532, "Since L(x,T) = R(x,T),
  (2.18) and (2.19) prove Theorem 1"). Line 58: "nearly identical to Montgomery's theorem in [Mon73] and
  [GM87, Lemma 8] except it does [not assume RH and has] explicit error terms." Range = bandwidth one,
  0 ≤ α ≤ 1 (attack-ceiling.md §2 row (a), §3.1).
- **The T^(−2α)·log T atom — sliver analysis.** The atom is the near-diagonal contribution of off-line zeros;
  for any fixed α > 0 it is o(1) (T^(−2α) log T → 0), and its proof mechanism (L(x,T) = R(x,T) diagonal
  dominance, line 532) fails once x > T (α > 1). So it is a vanishing correction, not a value, and it is NOT
  stated for |α| > 1. **[inferred, my analysis]** Even a hypothetical extrapolation F(α) ≈ α on (1, 1+δ) would
  read ≈ CUE (1.001 at α = 1.001) and would not exclude the near-CUE law on any usable kernel support — but no
  such extrapolation is proven or claimed.
- Erratum status (IMPORTANT): `research/papers/bgst-2501.14545.txt` is the 2025 CORRECTION paper — "before we
  prove Theorem 1, we explain how to correct the proof of [BGSTB24]"; "the source of the error came from
  applying Lemma 8 of [GM87]"; "all the applications of Theorem 1 in [BGSTB24] ... remain correct";
  "Montgomery and Vaughan (to appear) have obtained on RH a more refined version". The certificate's
  bandwidth-one input is unaffected (no consequence changed). Conditional application stated there (Thm 1):
  if all zeros with T < γ ≤ 2T lie in the thin box B_b, then ≥ 2/3 on the line, ≥ 67.25% with the Tsang kernel.
  **Note: 67.25% (conditional!) < 0.6734808616745137 = our unconditional record** — even the conditional
  Tsang-kernel pair-correlation application does not reach our record.
- **Status: PROVEN (unconditional) but strictly inside bandwidth one. NO |α|>1 sliver.**

**Candidate a2 — Goldston–Gonek–Montgomery (1987) / Montgomery (1973).** F(α) = 1 for |α| ≤ 1 only under RH;
nothing pointwise for α > 1 even under RH; the α > 1 regime is equivalent to the Hardy–Littlewood prime-pair
conjecture (attack-ceiling.md §3.1, §3.3, §7.5(a) of the main paper). GM87 Lemma 8 is precisely the bandwidth-one
lemma (and its misapplication is what the bgst erratum fixed). **CONJECTURED beyond 1; EMPTY.**

**Candidate a3 — variance flank (Goldston–Montgomery variance; Selberg S(t); Fujii; Gallagher–Mueller).**
`research/notes/attack-gm-variance.md` (the dedicated flank attack) — verdict line 13: "DEAD as a route to
reopen M29 — a documented confirmation of the wall from the variance side." Details at lines 106–108: Selberg
1946 ∫|S(t)|^(2k) ~ (2k)!/(k!(2π)^(2k))·T(loglogT)^k **PROVEN UNCONDITIONAL** but α ≈ 0 only; Fujii variance
**PROVEN UNCONDITIONAL** but "vacuous at UL ≪ 1 (α > 1: error ≈ 0.83 dominates main term ≈ 0.07)"; Gallagher–
Mueller **PROVEN UNCONDITIONAL** but 0 ≤ β ≤ 1 in-band only; CCCM equivalence to Montgomery's PCC **CONJECTURED**
(line 25). Line 33: "PROVEN beyond-1 variance would not bound the certificate's mean pair sums." **EMPTY.**

**Candidate a4 — unconditional pair correlation beyond the unit interval, any source.** None exists. The only
unconditional pair-correlation statements in the corpus are bandwidth-one (Montgomery [0,1] via BGSTB24) or
trivialities (F real/even/nonnegative, baluyot-etal-2306.04799.txt:49). **EMPTY.**

**Candidate a5 — Selberg N(1/2,T) / Levinson / Conrey–Iwaniec line.** Selberg 1942: positive proportion κ on the
line, small, not explicit (literature-map.md:34). Levinson 1974 1/3; Heath-Brown 1979 +34.74% simple;
Conrey 1989 2/5; BCY 2011 >41%; PRZZ 2020 5/12 ≈ 41.6% — "every result in this line uses Levinson's method"
(anthropic bundle 564f…:105–106; literature-map.md:188). Conrey–Iwaniec per se: corpus carries no usable ζ
constant (CIS13 14/25 is for Dirichlet L, literature-map.md:56). These are proportions on the line via the
mollifier mechanism — NOT form-factor values, all far below the record, and the Levinson class is stated to have
"no analogue of the 0.6818 ceiling" but is independent and capped ~0.417 (wave-phone-2/results/paper-main.txt:
161). **Not enterable; EMPTY for the certificate.**

---

## 3. Class (b): PROVEN lower bounds on the simple fraction p₁ above 0.6818 — VERDICT: EMPTY

**Candidate b1 — Bui–Heath-Brown 19/27 = 0.7037.** RH-CONDITIONAL. Main paper (anthropic bundle 564f…:3593):
"Bui and Heath-Brown [BHB13] obtained 19/27 (on RH and GLH earlier in [CGG98])". literature-sweep-simplezeros.md:
30: "19/27 simple under RH (Conrey–Ghosh–Gonek constant without GLH)". idea-generator-literature.md:35: CGG98
19/27 (RH+GLH). **Cannot enter an unconditional certificate.** (Even as a number it exceeds the ceiling only
because it uses a different mechanism — mollified discrete moments of ζ′(ρ).)

**Candidate b2 — Farmer–Gonek–Lee (2014).** The ξ′ function, not ζ: "assuming RH, Farmer, Gonek and Lee
[FGL14, Cor. 1.3] obtain > 85.84% simple [for ξ′] by Montgomery's method" (anthropic bundle 564f…:2619–2622);
the program's flat-window 0.85838 is "FGL's RH-conditional constant with RH removed" — Lean-PROVEN but for ξ′,
a different certificate target, and it "does not move the ζ-bound" (anthropic-methodology-mining.md:110;
attack-ceiling.md §3.6). **EMPTY for ζ's p₁.**

**Candidate b3 — Gonek's conjecture (simple zeros).** **CONJECTURED by nature; cannot enter an unconditional
certificate regardless of content.** The corpus does not carry a citable explicit statement of it
(INCONCLUSIVE-in-corpus: no local source located; nearest verifiable items are CGG98 19/27 RH+GLH and
Çiçek–Gonek 2310.10119 which is RH-conditional machinery, literature-sweep-simplezeros.md:32).

**Candidate b4 — everything else above 0.6818 in the corpus.** Exhaustive inventory of simple/on-line
constants in the corpus, all conditional or off-target:
- 0.6792 — Chirre–Gonçalves–de Laat 2020, SDP exploiting F ≥ 0 outside [−1,1]: RH-CONDITIONAL (attack-ceiling.md
  §2 row (c) notes the trivial F ≥ 0 gives upper constraints, not values; bundle 564f…:3593 region). Note
  0.6792 < 0.6818: it does not even reach the ceiling.
- 61.7% simple — Baluyot et al. Thm 2, CONDITIONAL on the box |β−1/2| < 1/(2log T) for T^(3/8) < γ ≤ T (or a
  strong zero-density hypothesis), baluyot-etal-2306.04799.txt:63, abstract.
- 2/3 ≈ 66.67% simple (box hypothesis), and 67.25% on-line (Tsang kernel, box hypothesis) — conditional, and
  both < 0.673481 (bgst-2501.14545 strings; baluyot-etal Thm 1 applications).
- 2/3 simple under a zero-density hypothesis — Aryan 2019 (Landau–Gonek extension), conditional
  (literature-sweep-simplezeros.md:33, flagged "maybe" for the unconditional-input stack — but zero-density
  hypotheses are still hypotheses).
- 14/25 = 56% (CIS13) and 58.65% (CIS) for Dirichlet L-functions: UNCONDITIONAL but different function, below
  the record (literature-map.md:56; paper-wu-bgstb25.md:47).
- ξ′-function 0.8825/0.9412 (CGdL20 Cor. 7, RH) — different function (bundle 564f…:2619–2622).
**No unconditional p₁ > 0.6818 exists anywhere in the corpus. EMPTY.**

---

## 4. Class (c): genuinely NEW certificate inputs, PROVEN for ζ, outside {mean, F on [0,1], integrality} — VERDICT: EMPTY (nothing enterable)

**Candidate c1 — Aggarwal sixth-moment upper bound ∫|ζ(1/2+it)|⁶ dt ≪ T^(1+ε).**
`research/papers/aggarwal-2304.07581-sixth-moment-upper.txt` (header garbled in extraction but the result is
the sharp sixth-moment upper bound; the txt opens with the Laplace-transform bound and "this implies
∫|ζ(1/2+it)|⁶ dt ≪ T^(1+ε)"). **PROVEN, UNCONDITIONAL.** Enterability: NONE PROVEN — it is a moment bound on
the prime/mollifier side; there is no proven bridge from a sixth-moment bound to a form-factor value or to a
constraint on the near-CUE law, and the paper's own §7.5(e) shows higher Gram-matrix moments add nothing in the
Rudnick–Sarnak range kλ < 2 (see c3). The sixth moment is exactly the conjectural-correlation regime's
moment-side twin, not a certificate input. **PROVEN but NOT ENTERABLE.**

**Candidate c2 — Second shifted moment of ζ on the line (Bettin 2015; Chan lower-order terms).**
`research/papers/bettin-1111.0925-second-shifted-moment.pdf` (no .txt in corpus — INCONCLUSIVE on exact
statement locally); `chan-0411501-lower-order-second-moment-ST.pdf`. These refine the mean-density input
(input (i)), which the certificate already consumes at full strength; no form-factor content. **Not new for the
certificate; EMPTY.**

**Candidate c3 — Higher Gram-matrix moments, kλ < 2 (Rudnick–Sarnak range).**
Main paper §7.5(e) (via attack-ceiling.md §3.4): unconditional evaluation available exactly in kλ < 2; for
λ ∈ (1/2,1) at most k = 3 and only for λ < 2/3; odd moments do not lower Λ₁(0); "unconditionally, higher
moments add nothing to the n₊-bound on (1/2,1)"; for λ ≤ 1/2, Prop. 7.4 (rank ≤ d = λ₁N) makes them useless.
**PROVEN — and PROVEN to add nothing in-range.** EMPTY.

**Candidate c4 — Triple correlation (Hejhal 1994; Rudnick–Sarnak 1996).** RH-CONDITIONAL, and only in kλ < 2;
serves distinct-zero counts (N_d ≥ 0.85082 under RH), not simple-on-line (attack-ceiling.md §3.4). **EMPTY.**

**Candidate c5 — Banks two-ordinate pair correlation (2026, v2).**
`research/papers/banks-2502.20569-paircorr-two-ordinates.txt`: "Pair correlation for sums of two ordinates";
abstract: "**Assuming the Riemann Hypothesis**, we extend Montgomery's pair correlation method to study the
distribution of differences between sums γ₁+γ₂ of two ordinates", with G₂(α,T) = (1/log T)(4α³/(3T^α)) + 1 +
O(loglogT/logT) (extraction-garbled). Novel OBJECT TYPE (two-ordinate pair sums) but RH-CONDITIONAL.
**Not enterable unconditionally; EMPTY (but the object type is the shape a future breakthrough would take).**

**Candidate c6 — BGMM small gaps/spacings (2022).** "We assume the Riemann hypothesis (RH) throughout"
(bgmm-2208.02359-small-gaps-spacings.txt, line 1). RH-CONDITIONAL. **EMPTY.**

**Candidate c7 — Simonič–Trudgian–Turnage-Butterbaugh (2020) explicit unconditional gaps.**
literature-sweep-simplezeros.md:46: "First unconditional explicit large/small gaps with positive proportion
(explicit Landau–Gonek)." **PROVEN, UNCONDITIONAL** — but it constrains consecutive-gap structure, not
form-factor values; it would only matter if it excluded the near-CUE law's gap spectrum, which (256-periodic
law, gaps down to ~1/256-scale) it does not — **[inferred]** the explicit constants in that line are far larger
than the law's minimal gaps. The sweep itself flags it "maybe" for the *gaps* ladder (Q3), not the
simple-fraction certificate. **PROVEN but not shown enterable; EMPTY.**

**Candidate c8 — Selberg 1946 S(t) moment asymptotics.** ∫|S(t)|^(2k) ~ (2k)!/(k!(2π)^(2k))·T(loglogT)^k,
**PROVEN UNCONDITIONAL** (attack-gm-variance.md:106). S(t) controls on-line counting via the argument, not pair
correlation; no proven bridge into the rank-trace certificate. **PROVEN but NOT ENTERABLE; EMPTY.**

**Candidate c9 — Mollifier/Levinson inputs (μ²-weighted discrete moments; Conrey 1989 machinery).**
Produce the 40–41.7% line via a different mechanism; produce no form-factor values; unconditional-only up to
5/12 (PRZZ 2020), all below the record (anthropic bundle 564f…:105–106; literature-map.md:188). **EMPTY.**

---

## 5. Verdicts and bottom line

| Class | Verdict | Reason |
|---|---|---|
| (a) PROVEN F for \|α\|>1 | **EMPTY** | BGSTB24 Thm 1 is bandwidth-one; the T^(−2α) atom is a vanishing correction not stated beyond 1; its proof collapses at x > T; α > 1 is equivalent to Hardy–Littlewood/PCC (attack-ceiling.md §3, §7.5(a)); variance flank proven dead (attack-gm-variance.md:13); only F ≥ 0 (an upper constraint, not a value) is unconditional outside [0,1] |
| (b) unconditional p₁ > 0.6818 | **EMPTY** | Only exceeders: 19/27 = 0.7037 (BHB13, RH), 0.6792 (CGdL20, RH; and < 0.6818 anyway), ξ′-constants (different function). Every in-class pair-correlation number — even conditional (2/3, 67.25%, 61.7%) — is below our unconditional 0.673481 |
| (c) new proven certificate inputs | **EMPTY** | Every PROVEN candidate is (i) not bridged into the certificate (Aggarwal sixth moment, Bettin second moment, Selberg S(t) — moment side), (ii) proven to add nothing in-range (Gram moments, §7.5(e)), (iii) conditional (triple correlation, Banks two-ordinate, BGMM, Aryan), or (iv) a different function (FGL/CIS). None supplies a value, a beyond-1 datum, or a law-excluding constraint |

**Frontier statement.** 0.6818 is the **terminal ceiling** and 0.6734808616745137 the **terminal in-class
record** for the rank-trace/pair-correlation certificate class — no PROVEN object in the verified corpus enters
the certificate as a fourth input. The frontier is closed *within the class*. Live frontier, in order of
fundability:
1. **In-class, ceiling-bounded:** compute the dual of the 256-law LP → close 0.6725 → 0.6818 and adversarially
   validate the ceiling (attack-ceiling.md §4 keep-alive 1). Expected yield < 0.6818.
2. **Outside-class, PROVEN:** ξ′-target transport (Lean 0.85838 simple-on-line unconditional, quartic 0.86864)
   — different function, moves a different bound (anthropic-methodology-mining.md:110).
3. **Conjectural regime, label-honest:** RH/PCC-conditional numbers (0.6792, 19/27) are real theorems but
   cannot strengthen an unconditional certificate — only an explicitly conditional companion record.
4. **The only genuine ceiling breaker** would be a PROVEN (a) form-factor value on (1, 1+δ), (b) unconditional
   bound on Σ_m (Λ∗Λ)(m)(Λ∗Λ)(m+h) for h ≤ X²/T (currently equivalent to Hardy–Littlewood, attack-ceiling.md
   §3.8), (c) Gram-moment evaluation outside kλ < 2, or (d) a structural constraint ruling out near-CUE laws.
   The corpus contains none; Banks' two-ordinate object (c5) is the closest shape but is RH-conditional.

**Surprise (worth recording):** the BGST erratum (bgst-2501.14545) fixes a GM87 Lemma 8 misapplication with no
consequential damage — the certificate's foundational input survived a published correction; and even the
*conditional* pair-correlation applications (67.25% Tsang-kernel) sit below our *unconditional* record, which
is a strong robustness signal for 0.673481.

**Labels:** all claims above cite local files + lines as given; "sliver analysis" in a1 and the gap-spectrum
note in c7 are **[inferred]** (my analysis, no citation exists); everything else is PROVEN (as stated in the
cited source). No new numerics were produced in this scan (no scripts run — a literature-only joint, per brief).

## Context for next agent
- Do NOT re-attack 0.6818 unconditionally by this class (attack-ceiling.md §4 ABANDON). Fundable: dual-LP
  certificate (item 1), EnclOK adversarial recheck, ξ′ transport documentation.
- If a "new input" is proposed, run it against this checklist: PROVEN? for ζ (not ξ′/L)? a VALUE on |α|>1 or a
  law-excluding constraint (not a moment-side bound)? If it fails any, it is not a ceiling breaker.
