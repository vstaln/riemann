# PAPER — arXiv:2508.10857 "The Alternative Hypothesis for Zeros of the Riemann Zeta-Function" (BGSTB 2025)

**Date:** 2026-08-12 (round 2.5, night session) · **Agent:** EXECUTIONER (AH deep-read + mapping)
**Status:** READ FULLY (10-page PDF → 1996-line text, converted via markitdown; source `research/papers/bgst-2508.10857-alternative-hypothesis.pdf` / `.txt`; paper dated 2025-08-14/15, 27 pages incl. refs)

**HEADLINE VERDICT: DEAD as a new input that raises the certified bound above 0.6731929.**
AH is a *conjectural* structural statement (RH + AH) about limiting **pair densities** at half-integer normalized spacings; it contributes **no constant** to the certificate's universal floor ε_univ (which is kernel-geometry-only). It cannot strengthen the stability floor, cannot move the in-class ceiling, and cannot push the certified simple-zeros bound past the external best 0.6731929114731423. It remains *contextually* alive (consecutive-gap structure corroborates the ladder object; p₀=1 is compatible with Essential Simplicity), not as a certificate input. [VERIFIED-FROM-PAPER + CHECKED NUMERICALLY — script `tools/ah_2508_mapping_check.py`]

---

## 1. Source / provenance

- Authors: Siegfred Alan C. Baluyot, Daniel Alan Goldston, Ade Irma Suriajaya, Caroline L. Turnage-Butterbaugh.
- arXiv:2508.10857 (submitted 2025-08-14). PDF already in the corpus (`bgst-2508.10857-alternative-hypothesis.pdf`, 574 KB, 10 PDF pages). Converted with `uvx --from 'markitdown[pdf]' markitdown` → 1996-line txt. [VERIFIED: file exists, PDF v1.5, 10 pages; extraction exit 0]
- Same group's earlier inputs: BGSTB24 (unconditional Montgomery, arXiv:2306.04799), BGSTB25 (Pair Correlation I: simple & critical zeros, arXiv:2501.14545) — already program inputs.

---

## 2. The Alternative Hypothesis — exact formulation [VERIFIED-FROM-PAPER]

**Normalized ordinate** (p.1): γ̃ = (γ/2π) log γ, so consecutive γ̃ have asymptotic mean spacing 1.

**AH** (p.2, from [Bal16]): for each n ≥ 1 there is an integer k_n ≥ 0 with
  γ̃_{n+1} − γ̃_n = k_n/2 + O(|γ̃_{n+1} − γ̃_n| · ψ(γ_n)),
where ψ(γ) → ∞, ψ(γ) = o(log γ).

**AH-Pairs** (p.2, (1.2)–(1.3)) — the working form: for pairs (γ,γ′) with |γ−γ′| logT/2π ≤ M (set P(T,M)), there is an integer k ≪ M with
  (γ−γ′) logT/2π = k/2 + O((|k|+1) R(T)),  R(T) → 0.
Density of pairs closest to k/2: P_{k/2}(T) = (logT/2π / T)·|B_{k/2}|, B_{k/2} = pairs with normalized difference in (k/2 − δ/2, k/2 + δ/2].

**Strong AH-Pairs** (p.3): same with |γ−γ′| logT/2π ≤ M logT and R(T)logT → 0, k ≪ M logT.

**Density parameter (answer to task 3a):** the density parameter is **p_{k/2}**, the asymptotic density of zero-pairs at normalized separation k/2 (k/2 multiples of half the average spacing). For k=0 this is p₀ (pairs at equal ordinates, i.e. multiplicity-weighted). Its permitted range (Thm 1, Cor 1): **1 ≤ p₀ ≤ 3/2 − 2/π² = 1.2973576...**; the other densities are determined by p₀:
  p_{k/2} = p₀ − 1/2 (k ≠ 0 even);  p_{k/2} = 3/2 − 2/(π²k²) − p₀ (k odd).

**AH-Density** (p.5) and Theorem 4 (p.11): if the limiting densities exist, then for any even r ∈ L¹, supp r̂ ⊂ [−1,1]:
  Σ_k r̂(k/2) p_{k/2} = r(0) + 2∫₀¹ α r(α) dα.   ← the p₀ enters only as the k=0 term of this weighted density sum.

## 3. The constraints on pair density at k/2 and the multiple-zero restriction [VERIFIED-FROM-PAPER]

- **Pair-density constraints (Thm 1 / Cor 1–3, pp.3,7):** exactly the p_{k/2} relations above. Cor 2 (p₀=1): p_{k/2}=1/2 (even≠0), 1/2 − 2/(π²k²) (odd). Cor 3 (p₀=3/2−2/π²): p₀ = 1.29736, p_{k/2}=1−2/π² (even≠0), (2/π²)(1−1/k²) (odd); note p_{1/2}=0. [CHECKED NUMERICALLY: p₀=1.2973576327, p_{1/2}=0, p_{3/2}=0.1801, p_{5/2}=0.1945, Cor2 p_{1/2}=0.29736]
- **Multiple-zero restriction (task 3c):** the paper's only content here is *qualitative*. The abstract says the pair-density constraints "restrict the density of (possible) multiple zeros", and Remark 1 (p.2) notes k=0 pairs occur (a) at γ=γ′ — m² times for a multiplicity-m zero, and (b) for distinct zeros very close together. **No quantitative multiplicity-density constant, theorem, or bound is displayed anywhere in the paper** (full-text scan for multiple/multiplicity: only abstract line, Remark 1, and the keyword list). The multiple-zero restriction is therefore *implicit only*: a large multiplicity density would inflate p₀ beyond its allowed range 1 ≤ p₀ ≤ 1.29736. [VERIFIED-FROM-PAPER: no displayed constant; grep confirms]
- **"Strong AH ⇒ Essential Simplicity" (task 3d):** Theorem 2 (p.3): RH + Strong AH-Pairs ⇒ p₀ = lim P₀ = 1, hence ESH (almost all zeros simple; almost all distinct zeros not spaced closer than average). Proof (Section 4): uses Montgomery's β=1 kernel, discards |γ−γ′|>M terms, and uses R(T)logT→0 to isolate |B₀|. [VERIFIED-FROM-PAPER]
- **Other quantitative constants (task 3e):** Corollary 4 (p.10): C := lim ∫₁^∞ F(α)/α² dα. Under RH + Montgomery conjecture, C=1; under RH + AH-Pairs with p₀=1: **C = 1 + π²/24 + log(2/π) = 0.9596508...**; with p₀=3/2−2/π²: **C = 1/2 + π²/6 + log(2/π) = 1.6933514...**. Also limsup P₀ ≤ 3/2−2/π² = 1.29736 (Remark 4) vs the unconditional record limsup ≤ 1.3208 (CGdL20). Lemma 4 supplies the kernel ĝ_n(t) = sin(2πt)(n²/(n²−4t²))/2πt vanishing at half-integers except 0,±n/2. [CHECKED NUMERICALLY: all reproduce]

---

## 4. MAP to the program — the decisive question

**The certificate mechanics (from `discovery-gram-stability-673.md`, `ceiling-gram-constraint.md`, `verify-tawanerguo-bellman.md`, and the external repos' proof docs):**

The rank–trace stability argument gives (ainta proof.md §2; trmdy proof.md §0):
  S ≥ H(v)·N + tr Ψ(M) − o(N),  Ψ(t) = (t−1)² on [0,2], 2t−3 beyond,
and the *universal floor*: tr Ψ(M) ≥ ε_univ·N, where ε_univ comes from a **pointwise** bound on the Gram matrix of simple-zero atoms:
- 3-point: ε₄ = min_{u,v≥0,u+v≤4} (k(u)²+k(v)²+k(u+v)²) ≥ 221/10⁶, positivity from the kernel zero set being sum-free (x tan πx = c has no x,y,x+y all zeros; ainta §3) → bound (H₀−ε/4)/(1−ε/2) = 0.6725198.
- 7-point: F₆(g₁..g₆) = (1/3000)Σgᵢ + Σ_s 2/(7−s) Σ w(gᵢ+⋯+gᵢ₊ₛ₋₁) ≥ 19/5000 for all g ≥ 0 (exhaustive interval cert) → 0.6730085 (ainta), 0.6731377 (trmdy, re-optimized window).
- Bellman coboundary: F_B ≥ 577/100000, block m=183, Φ_m envelope → (H_α − 59/19520)/(1 − B/183) = **0.6731929114731423** (tawanerguo).

**The floor ε_univ is a pure function of the kernel k(x) and the gap geometry.** It is certified by exhaustive interval subdivision over *all* gap tuples (g ≥ 0) — a universal statement about positive-semidefinite Gram matrices of the atom system. It reads **no** pair density, **no** p_{k/2}, **no** multiplicity statistic, **no** AH.

**AH's consecutive-gap structure is a different object:** it constrains the *limiting statistics* of gap lengths (multiples of 1/2 average spacing) — a distributional statement about which k/2 values occur with which density. The certificate's floor is a *worst-case* (min over Gram matrices) statement that must hold for every configuration, including those violating AH. AH is also a *conjecture* (RH + AH-Pairs assumed), whereas the certificate is *unconditional*.

**Therefore:**
1. AH provides **no new input** that raises ε_univ (3-point 221/10⁶, 7-point 19/5000, Bellman 577/100000). [STRUCTURAL — the floor's proof never invokes any p_{k/2}]
2. AH cannot beat **0.6731929**: to lift the certified bound you must raise the universal floor or the window constant H(v); the paper contains neither a larger F constant nor a larger H. Its constants (1.29736, 0.95965, 1.69335) are pair-density / F-average constants with no route into the Gram-floor chain. [VERIFIED-FROM-PAPER + NUMERICAL]
3. AH cannot move the in-class ceiling 0.68183123: the ceiling is a feasible-set restriction of the LP (Q2b, PROVEN); a restriction of the feasible set cannot raise a maximization optimum, and the floor's size is irrelevant to that structure. AH adds no constraint to the LP. [PROVEN under the LP framing in `ceiling-gram-constraint.md`]
4. The ladder (Q3, 3→7→9→11) raises ε_univ by adding *more gaps* to the F functional (more w(y_j−y_i) terms with span capacity 2) — a pointwise nonnegativity certification over larger tuples. AH's gap-length statistics do not substitute for or augment this. [STRUCTURAL]

**Conditional caveat (the honest PARTIAL):** If a *future* certificate class were built to read pair-density constraints directly (e.g. a two-point-conditioned Gram floor "given that a fraction ≥ f of gaps lie at multiples of 1/2 average spacing, tr Ψ ≥ ε(f)"), then AH's p_{k/2} constraints could in principle feed it — but (a) the paper constructs no such class, (b) AH is conjectural (conditional on RH), so any such certificate would be conditional, losing the unconditional 67.3193% guarantee, and (c) no quantitative ε(f) is derivable from the paper as written. [CONJECTURED — no such class exists in the literature we found]

---

## 5. VERDICT (task 5)

**DEAD as a ladder input / new certificate input that raises the certified bound above 0.6731929.** [VERIFIED-FROM-PAPER + NUMERICAL + STRUCTURAL]

| Question | Answer | Label |
|---|---|---|
| Does AH give a NEW input to the certificate? | No — it constrains pair densities p_{k/2}, never read by the certificate | VERIFIED-FROM-PAPER |
| Does AH strengthen the ε_univ floor (tighter ε → larger bound)? | No — the floor is a pointwise Gram-min over all gap tuples; AH adds no F-constant, no H-constant | STRUCTURAL + NUMERICAL |
| Can AH certify a bound > 0.6731929? | **No** — it is conjectural (RH + AH) and contributes no constant to the floor/window | VERIFIED-FROM-PAPER |
| Is AH compatible with a large simple-zeros density (the program's object)? | Yes — p₀=1 is the ESH case (Cor 2, Thm 2); the pair-density bound 1.297 does not cap the simple fraction | VERIFIED-FROM-PAPER |
| Does AH move the in-class ceiling 0.6818? | No — ceiling is an LP feasible-set property, insensitive to any floor size | PROVEN (ceiling note Q2b) |
| Value for the program | Context only: (1) corroborates that consecutive-gap structure is real input (same object as the ladder's F₆); (2) its p₀ ≤ 1.297 is not a contradiction of large simple density; (3) re-confirms the ladder/Q3 convergence question is the live frontier | CONJECTURED (interpretive) |

**The one live route the sweep named (consecutive-gap → Gram-stability) is NOT in this paper.** The paper is about pair *density statistics* under a conjecture; the certificate needs *pointwise Gram floors* under no conjecture. Those are different layers of the problem.

---

## 6. Honesty labels (full inventory)

- [VERIFIED-FROM-PAPER] — AH / AH-Pairs / Strong AH-Pairs formulations (pp.1–3); Thm 1 (1.5)–(1.6) p.3; Cor 1–3 p.7; Thm 2 p.3; Thm 3 (2.16) p.9/22; Thm 4 (2.17) p.11; Cor 4 p.10; Lemma 4 kernel; ESH def p.3; multiplicity remark p.2; "restrict the density of (possible) multiple zeros" (abstract) — no quantitative multiple-zero constant exists anywhere in the paper.
- [CHECKED NUMERICALLY] — script `tools/ah_2508_mapping_check.py` + one-liner: limsup P₀ = 1.2973576327153244571; Cor2 C = 0.9596508114226017; Cor3 C = 1.6933513615587716; Cor3 p_{1/2}=0, p_{3/2}=0.1801, p_{5/2}=0.1945, p_even=0.79736; Cor2 p_{1/2}=0.29736. Certificate chain reproduced from repo inputs: H0=0.6725007036794116, ainta3=0.6725197671136777, ainta7=0.6730085279277798, trmdy=0.6731376723147616 (uses H(v)=0.67245704141454 rounded as in repo; exact repo bound 0.6731376306993446), tawanerguo (H_window=0.6724587094007293, A=1.02129, block=1.0212287852929822, bound=0.6731929114731423).
- [PROVEN] — in-class ceiling is a feasible-set restriction; a restriction cannot raise a maximization optimum (ceiling-gram-constraint.md Q2b).
- [CONJECTURED] — the interpretive claims (any future density-reading certificate class; that no such class exists).
- [INCONCLUSIVE — blocker stated] — none for this task; the mapping is fully determined by the paper text + repo mechanics. (Note: trmdy exact bound differs at the 10th digit from my reproduction because I used the README's rounded H(v); the repo's own certified H_cert gives 0.6731376306993446 — not material to the verdict.)

---

## 7. Scripts and commands

- Paper conversion: `cd /home/vstaln/.pi/agent/npm/node_modules/mitsupi/skills/summarize && timeout 600 uvx --from 'markitdown[pdf]' markitdown /home/vstaln/riemann/research/papers/bgst-2508.10857-alternative-hypothesis.pdf > /home/vstaln/riemann/research/papers/bgst-2508.10857-alternative-hypothesis.txt` (exit 0; 1996 lines).
- All numbers in this note: `cd /home/vstaln/riemann && uv run --quiet --with mpmath python tools/ah_2508_mapping_check.py` (script saved at `tools/ah_2508_mapping_check.py`, self-contained, no data files).
- Cor 2/3 p_{k/2} spot checks: one-liner `uv run --quiet --with mpmath python -c "..."` (reproduced in section 4).

## 8. Relation to other notes / next steps

- `discovery-gram-stability-673.md` — the stability mechanism (the real source of 0.6730+).
- `ceiling-gram-constraint.md` — Q2b PROVEN: ceiling 0.68183123 stands; stability moves the constant toward it.
- `verify-tawanerguo-bellman.md` — third mechanism; NEXT_FRONTIER: global spectral-dual/Bellman subaction = the live convergence question.
- **Recommendation for the next round:** fund the *ladder/global-coboundary convergence* question (Q3 / NEXT_FRONTIER direction 1), not AH. The 1%+ goal needs either (a) a new unconditional F-functional (larger blocks, better windows — the trmdy window re-optimization route, which gained ~34% in the window constant), or (b) breaking the 0.6818 ceiling via a *new* certificate-class read (e.g. distinct-zero or on-line transfer, Q1), or (c) a genuinely new analytic input — AH does not supply it.
