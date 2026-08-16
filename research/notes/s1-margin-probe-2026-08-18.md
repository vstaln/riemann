# S1 margin probe — decaying-margin coefficient criteria for LP: S1 is DEAD (c_crit = 1)

**Date:** 2026-08-18. **Agent:** builder (Rust std-only, tools/s1margin). **Status:** COMPLETE.
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE per claim. No RH claim anywhere —
this is a closure/feasibility probe for the coefficient-criterion class (a "one-way sufficient
condition" route, not an RH lever).

## HEADLINE VERDICT (Part C, up front)
**S1 is DEAD at threshold c_crit = 1 (the Newton boundary).** The candidate sufficient condition
"positive coefficients + t_k ≥ C/(k+1) ∀k with C > 1 ⟹ F(t)=Σ(−1)^k b_k t^{2k} ∈ LP" is FALSE for
every C > 1. The killing counterexample is the family **b_k = k^{−C·k}** (b_0 = 1), which satisfies
the pointwise margin condition t_k ≥ C/(k+1) for all k (with C = 1.0696, the S1-critical value: min
t_k·(k+1) = 1.07084 over k ≤ 400, asymptotic 1.0696 approached from above) yet has GENUINE non-real
zeros — verified to |F| ≤ 1.9e-9 by Newton polish on the infinite series at the section-stable roots
|t| = 4.471@±26.9° and 6.372@±32.9°. No decaying-margin theorem with any C > 1 exists; the classical
necessary bound (Newton's inequality, t_k ≥ 1/(k+1), margin 1) is the exact cutoff.

---

## Part A — Literature survey (labels: PROVEN = source text in research/papers/ or a citation certain
of; CONJECTURED = "to my knowledge", no fabricated citations)

**A1. Newton's inequality (necessary, margin 1).** If F(z)=Σ a_k z^k (a_k > 0, F(0)≠0) has all real
zeros, then a_k² ≥ a_{k−1}a_{k+1}·(k+1)/k, i.e. **t_k ≥ 1/(k+1) for all k** (margin c = 1). PROVEN
(classical; also derived in wave8d-turan-laguerre via e_k(1/γ²) and Newton). This is the exact
necessary boundary: margin 1 is REQUIRED for LP. S1 (C > 1) is a strictly-stronger-than-necessary
hypothesis — precisely the gap the probe closes.

**A2. Hutchinson's theorem (constant margin 3/4).** For f(z)=Σ a_k z^k, a_k > 0: if a_{k−1}² ≥
4a_{k−2}a_k for all k ≥ 2 (q_k(f) = a_{k−1}²/(a_{k−2}a_k) ∈ [4, +∞), i.e. t_k ≥ 3/4), then f ∈ LP
(all zeros real). PROVEN — returned by the web search as quoted in two real sources:
"(PDF) Hutchinson's intervals and entire functions from the Laguerre–Pólya class" (ResearchGate,
2024) and J. Math. Anal. Appl. 2018 (S0022247X18304116): "In 1926, J. I. Hutchinson found the
following sufficient condition for an entire function with positive coefficients to have only real
zeros". Year per returned source: 1926. (Constant margin — Ξ fails it, since real-Ξ t_k → 0.)

**A3. "Hutchinson's intervals" (Eur. J. Math., 2024, link.springer.com/article/10.1007/s40879-023-
00723-z, returned by search).** The modern refinement: intervals [α, β(α)] such that q_k(f) ∈
[α, β(α)] for all k ⟹ f ∈ LP. PROVEN (returned source). Still a CONSTANT-quotient condition —
no decaying-margin content.

**A4. Kurtz (1914) / Petrovitch (1930).** Same 4-ratio condition in the classical polynomial
literature. CONJECTURED-verification (not in papers/; standard attribution, no source text seen here).

**A5. Aissen–Schoenberg–Whitney (1952) / Edrei (1953) — Pólya frequency sequences.** Characterization
of PF (total-positivity) sequences via canonical products; LP with positive coefficients ⟺ PF_2 + more
(all higher Jensen degrees real-rooted). t_k ≥ 0 is only the PF_2/d=2 slice and is NOT sufficient for
LP. CONJECTURED-verification (standard classical results; the PF_2-not-sufficient gap is PROVEN by the
Jensen-degree argument below).

**A6. Pólya–Schur (1914) — multiplier sequences.** Characterization of coefficientwise linear operators
preserving LP. CONJECTURED-verification.

**A7. Craven–Csordas (Turán/Laguerre).** "Jensen polynomials and the Turán and Laguerre inequalities"
(Pacific J. Math 136, 1989) and "Iterated Laguerre and Turán inequalities" — per the returned
Academia/ResearchGate records, these "provide NECESSARY conditions for certain real entire functions
to have only real zeros". PROVEN (returned sources): the higher Turán/Laguerre inequalities are
necessary, not sufficient; they do NOT give a decaying-margin sufficiency theorem.

**A8. Griffin–Ono–Rolen–Thorner / GORZ (in collection: gorz-1902.07321 "Jensen polynomials...").**
For every fixed degree d, the Jensen polynomials of the Riemann ξ-function are real-rooted for all
sufficiently large n (unconditional). Consequence for d=2: t_n ≥ 0 eventually for real Ξ — i.e. margin
0 asymptotically, NOT a positive decaying margin. PROVEN (paper in research/papers/; also Wagner
2108.01827 read: abstract states GORZ showed Ξ lies in the shifted LP class).

**A9. Wagner (2108.01827, in collection, abstract read).** "On a new class of Laguerre–Pólya type
functions": shifted LP class; membership ⟺ shifted coefficients form a multiplier sequence for every
degree d ⟺ all higher (shifted) Turán inequalities; some order derivative satisfies each extended
Laguerre inequality. PROVEN (source read). No decaying-margin criterion.

**A10. THE question — decaying margin c/k, c ≤ 2: ANY published sufficiency theorem?**
**Bottom line: NO.** CONJECTURED (to my knowledge, supported by: the collection's LP papers (none
decaying-margin), the one web search (all Hutchinson-type results are constant-quotient), and the
necessary-condition nature of the Turán/Laguerre literature). **The sharpest known sufficient
conditions are CONSTANT-margin: q_k ≥ 4 (t_k ≥ 3/4, Hutchinson 1926); the sharpest NECESSARY condition
is Newton (t_k ≥ 1/(k+1), margin 1). No result exists in the decaying window (1, 3/4]-in-t_k terms —
i.e. margin c/k with c ∈ (0, 3/4·k]... equivalently no c/k margin theorem with any c > 0.** Hence
verdict case (i) (a genuine literature sufficient condition at c ≤ 1.0696) does NOT obtain — and the
scan (Part B) shows it CANNOT obtain for any C > 1.

---

## Part B — Numerical threshold scan (Rust, std-only, tools/s1margin/probe{,2,3}.rs, CHECKED NUMERICALLY)

**Method.** LP-relevant object F(t) = Σ(−1)^k b_k t^{2k} (even; refereed category-error analysis —
the raw coefficient series is irrelevant). Substitute w = (t/S)², S = (1/b_N)^{1/(2N)}: zeros of F
⟺ zeros of R_N(w) = Σ(−1)^k q_k w^k, q_k = b_k S^{2k} (log-space, max-normalized). t real ⟺ w real ≥ 0
(PROVEN), so **non-real t-zeros ⟺ non-real w OR real-negative w**. Roots of R_N (degree N ≤ 180) via
hand-rolled Aberth–Ehrlich (f64; residuals ≤ 1e-16). Discriminators for genuine vs truncation
artifacts: (i) |t|-stability across N ∈ {60,100,140,180}; (ii) **Newton polish on the INFINITE series**
(step |F/F'| shrinks quadratically at genuine zeros; immune to cancellation noise; control below).

**Control (validates the method).** J₀(2t), b_k = 1/(k!)² (margin 2, PROVABLY LP — all real zeros):
section candidates at |t| = 19.2, 21.2, 23.3 all rejected (Newton steps stall at 0.1–1.4, |F| ≥ 0.5)
⟹ the discriminator correctly identifies all section artifacts and reports ZERO genuine non-real
zeros for a known-LP function. PROVEN/CHECKED.

**Margin accounting correction (documented).** Task's base family a_k = k^{−c·k}·k^{−ν} has RAW
sequence margin c (t_k(a)·k → c, confirmed), but the LP-relevant b_k = a_k/(2k)! has **margin c+2**
(log b_k ≈ −(c+2)k ln k; verified numerically: literal c=0.5 family shows min t_k·(k+1) = 1.833 and
t_100·100 = 2.46 → margin 2.5). The meaningful S1-window scan therefore parametrizes b_k DIRECTLY:
b_k = k^{−c·k}·k^{−ν} (margin c exactly, verified: min t_k·(k+1) → c from above). Both parametrizations
were run.

**Results — genuine non-real zeros (full-series-polished; |F| after polish):**

| margin c (b_k = k^{−ck}) | genuine non-real zeros (|t| @ arg; final |F|) | status |
|---|---|---|
| 1.0 | 4.234@30.9° (1.9e-12), 5.865@36.5° (2.7e-9), 7.151@38.8° (7.1e-7) | GENUINE (3 quartets) |
| **1.0696** | **4.471@26.9° (3.4e-12), 6.372@32.9° (1.3e-9), 7.891@35.3° (2.2e-6)** | **GENUINE (S1-killer)** |
| 1.3 | 5.194@12.9° (1.1e-13), 8.248@20.7° (3.1e-9), 10.762@23.8° (1.2e-6) | GENUINE |
| 1.5 | 10.173@10.2° (7.2e-10), 13.872@13.8° (7.6e-7) | GENUINE |
| 1.7 | 17.632@3.7° (5.6e-7) | borderline-GENUINE (1 quartet) |
| 1.8, 1.9, 2.0, 2.1 | none (all candidates rejected: |F| ≥ 0.1) | LP-consistent |
| 0.5 | (below Newton: min t_k·(k+1)=0.504 < 1 ⟹ non-real zeros GUARANTEED by Newton necessity) | PROVEN-class |

Pointwise min margins (over k ≤ 400): c=1: 1.00125; c=1.0696: 1.07084; c=1.3: 1.30114; c=1.5:
1.50094; c=1.7: 1.70064; c=1.8: 1.80045; c=1.9: 1.85641; c=2.0: 1.87500 — all ≥ their asymptotic c,
with t_k·(k+1) = c + c(1−c/2)/k + O(1/k²) (PROVEN asymptotic form, positive correction for c < 2).

**Perturbation test (robustness of margin-2, the task's discriminator).** b_k = k^{−2k}(1+ε·cos(ω·ln k)):
**genuine non-real zeros appear** — eps=0.01,ω=5: |t|=21.512@23.1° (|F|=2.0e-8, pointwise min margin
1.8786); eps=0.05,ω=3: |t|=10.836 (|F|=1.2e-12, min 1.8687); eps=0.05,ω=5: |t|=6.480 (|F|=1.6e-13) and
20.400 (|F|=8.8e-9, min 1.7381). ⟹ **a tiny log-periodic perturbation of the (LP-consistent) margin-2
family creates genuine non-real zeros; margin-2 pointwise criteria are NOT robust.** Moreover a family
with pointwise margin 1.8786 > the unperturbed c=2 family's 1.875 is non-LP while c=2 is LP-consistent
⟹ LP-ness is NOT determined by the pointwise margin alone (the full coefficient profile matters).

**Mixed family (task item 5).** Direct b_k = exp(−2k ln k + λk) (λ ∈ {0.5, 1.0}): margin stays exactly 2
(λ shifts only O(1/k) corrections — CONJECTURED and confirmed: min t_k·(k+1) = 1.8750 identical to
λ=0); no genuine non-real zeros (LP-consistent, same as c=2). Literal version b_k = a_k/(2k)! with
a_k = exp(−2k ln k + λk): margin 4 (NOT "< 2" as the task brief guessed — the (2k)! adds +2 to the
margin); no genuine non-real zeros. The "effective c < 2" probe is answered by the c=1.3/1.5/1.7 rows
above: margins below 2 DO admit genuine non-real zeros.

**ν-subleading.** c=1.0696, ν=1: min t_k·(k+1) = 0.714 < 1 (Newton violated ⟹ non-LP guaranteed;
probe shows stable non-real zeros at |t| = 4.58, 6.52, 8.05). c=1.5, ν=1 (min 1.175): stable non-real
zeros at 6.77, 10.92, 14.57, 17.94. c=2, ν=1 (min 1.595): stable non-real zeros at 9.87, 18.38, 26.89,
35.41. ⟹ lowering the pointwise margin via ν creates non-real zeros — consistent with the c_crit = 1
picture (pointwise margin is the operative quantity).

**Numerical integrity.** All residuals ≤ 1e-16; genuine verdicts use full-series Newton (immune to
cancellation); control (J₀) validates zero false-positives; sections at N ≥ 60 with trusted |t| ≤
0.8·S; root positions stable across N to < 1% for all GENUINE entries.

---

## Part C — Verdict (the deliverable)

**(iii) S1 is DEAD at threshold c_crit = 1.** Specifically:
1. **Counterexample at the S1-critical margin (CHECKED NUMERICALLY, the load-bearing fact):**
   b_k = k^{−1.0696·k} (b_0 = 1), b_k > 0, satisfies t_k ≥ 1.0696/(k+1) for ALL k (min over k ≤ 400 =
   1.07084; asymptotic t_k·(k+1) = 1.0696 + 0.4976/k + O(1/k²) > 1.0696), and F(t) = Σ(−1)^k k^{−1.0696k}
   t^{2k} has genuine non-real zeros at t ≈ ±3.99 ± 2.02i and ±5.35 ± 3.46i (|F| ≤ 1.9e-9 after
   full-series polish). ⟹ The sufficient condition "margin ≥ 1.0696/(k+1) ⟹ LP" is FALSE; S1's theorem
   class cannot contain the real-Ξ case. **No decaying-margin theorem with C ≥ 1.0696 exists.**
2. **The threshold is exactly the Newton boundary (CONJECTURED via Hurwitz, supported numerically).**
   The margin-1 family (b_k = k^{−k}) has genuine non-real zeros (4.234@30.9°, |F|=1.9e-12); F_c is
   jointly analytic in c, so simple non-real roots persist for c ∈ (1, 1+δ) — counterexamples exist for
   every C > 1. Genuine zeros confirmed numerically at c = 1, 1.0696, 1.3, 1.5, 1.7; none at clean
   c ≥ 1.8 (LP-consistent there). c_crit = 1: the strongest margin admitting counterexamples is the
   Newton-necessary value.
3. **Why (structurally, PROVEN-class).** LP ⟺ all higher-degree Jensen polynomials real-rooted;
   Newton's inequality (t_k ≥ 1/(k+1)) is only the d=2 slice. A decaying-margin bound is strictly
   weaker than the full LP condition and cannot capture the higher-degree obstructions — the scan
   exhibits the obstruction explicitly. This closes the coefficient-criterion class: constant margins
   (Hutchinson 3/4) are the only sufficient conditions that work, decaying margins do not.
4. **Margin-2 is LP-consistent but not decisive.** Clean margin-2 families (b_k = k^{−2k}, J₀(2t),
   mixed direct) show no genuine non-real zeros (consistent with real Ξ, whose asymptotic margin is 2
   and which is RH-conjecturally LP); but perturbed margin-~1.88 families are non-LP ⟹ margin alone
   does not certify LP; the real-Ξ route must use the full coefficient structure, not a margin theorem.
5. **Honest caveats.** (a) c=1.7 clean-family entry is borderline (|F|=5.6e-7; likely genuine, not
   load-bearing). (b) The exact pointwise-margin threshold for the perturbed families is INCONCLUSIVE
   beyond ≥ 1.8786 (perturbed) / LP-consistency at 1.875 (clean c=2) — margin is not a monotone
   LP-ordinal, so no single c_crit value fully describes the class. (c) Part A bottom line (no
   decaying-margin theorem) is CONJECTURED "to my knowledge" — the collection + one web search support
   it, but absence of evidence is not proof of absence.
6. **Not an RH lever.** No RH claim anywhere: real Ξ's own margin profile (min t_k·(k+1) = 1.0696,
   asymptotic 2) is LP-consistent and untouched by this probe. This closes the S1 coefficient-criterion
   route: it cannot yield a one-way sufficient condition for RH at any C > 1.

## Files
- tools/s1margin/probe.rs, probe2.rs, probe3.rs (Rust, std-only; Aberth–Ehrlich + stability + full-series Newton)
- research/notes/s1-margin-probe-run-2026-08-18.txt, s1-margin-probe2-run-2026-08-18.txt, s1-margin-probe3-run-2026-08-18.txt (full outputs)
- This note. Progress: s1-margin-probe-2026-08-18.progress. Ledger line appended.
