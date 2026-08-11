# Q1 — Does the Gram-stability refinement transfer to the ON-LINE (Theorem A) and DISTINCT (Theorem C) proportions?

**One-line verdict:**
- **Theorem C (distinct, 5/6):** transfer **CONJECTURED — method-level transfer verified** (the stability term tr Ψ(M) for C's atoms is positive with the same kernel-ε as Theorem D; numerically supported), **constant-level transfer chain-dependent** (5/6 → 5/6 + δ needs C's rank–trace chain algebra, which is not available on the phone; if the linear response of D's chain transfers, δ ≈ +1.9×10⁻⁵ (3-pt) / +3.3×10⁻⁴ (7-pt), labeled HYPOTHETICAL).
- **Theorem A (on-line with multiplicity, 2/3):** transfer **INCONCLUSIVE — precise blocker named**. The stability term is positive for A's atoms too (ε_A ≥ ε_D, numerically supported), but A's equality case is doubly impossible (orthogonality *and* equal multiplicities), the PLAN.md finding "the 2/3 deficit is arithmetic — pair-correlation content, not method-inherent" indicates the 2/3 is data-limited rather than slack-limited, and the task's own hint ("the equality case may involve different vectors") suggests A's chain has no atom-orthogonality slack to recover. If A's chain is data-saturated, the transfer is **vacuous** (constant unchanged); a definitive answer requires A's actual chain.

Status labels: PROVEN / CHECKED NUMERICALLY (script + command) / CONJECTURED / ABANDONED / INCONCLUSIVE (blocker named).

---

## 0. What was available (and what was not)

The full paper text is NOT on the phone. A network fetch of the arXiv paper / external repos was attempted and **blocked by the sandbox permission system** (curl to export.arxiv.org and api.github.com both require approval with no interactive UI). This analysis therefore works from: (i) the structural description in the task, (ii) the discovery note, (iii) the known constants, (iv) the standard rank–trace / Sylvester-inertia machinery of the compressed-Weil-form method (Bombieri 2000; Conrey 1989; Feng 2012; Bui–Conrey–Young 2011). **Every reconstruction below that goes beyond those sources is flagged as an assumption.**

---

## 1. Reconstruction of the common machinery (ASSUMED, flagged)

The three theorems share a Hermitian "compressed Weil form" W with spectral decomposition W = P − Q (P, Q ≥ 0, P ⊥ Q), and the following bookkeeping (assumptions in brackets):

- **On-line zero at ordinate γ:** contributes a rank-one atom v_γ. Its Gram entries are
  ⟨v_γ, v_γ′⟩ = k(γ − γ′) with k(x) = K(x)/K(0), K(x) = ∫_{−1/2}^{1/2} cos(√2 t) cos(2π x t) dt. [Assumed: the SAME kernel k governs the atoms in all three theorems — the task's framing; if a theorem uses a different optimized window, its kernel and hence its ε differ.]
- **Off-line pair {ρ, 1−ρ̄}:** a 2×2 block made indefinite by the window choice; by Sylvester's law of inertia each pair contributes exactly one positive and one negative eigenvalue. So rank(P) ≥ N_d + N_p, rank(Q) ≥ N_p, where N_d = # distinct on-line ordinates, N_p = # off-line pairs, N = N₀ + 2N_p, N₀ = on-line count with multiplicity. [Assumed: the (1,1)-indefinite block structure is as in the method's standard form.]
- **Two-moment data:** t = tr(P), t₂ = ‖P‖²_F are computed unconditionally via Montgomery's pair-correlation second moment (bandwidth ≤ 1). [Assumed: same as in the discovery note's description.]
- **Rank–trace inequality** (von Neumann / Cauchy–Schwarz on the eigenvalues λᵢ of P):
  t² ≤ r·t₂,  r = rank(P), equality iff all λᵢ equal **and** the atoms mutually orthogonal.
- **Exact refinement** (used by the external groups on Theorem D):
  t₂ = 2t − r + tr Ψ(M),  Ψ(t) = (t−1)² on [0,2], 2t−3 beyond,  M = Gram matrix of the atoms.
  This is an **exact algebraic identity** for any PSD P (the nonzero eigenvalues of M are those of P, and (t−1)² = t² − 2t + 1). It holds for the atoms of *any* counting scheme; the [0,2]-normalization only matters for interpreting Ψ as (t−1)², and the linear bound 2t−3 for t ≥ 2 only makes the positivity manifest. **The identity is unconditional; the positivity tr Ψ(M) > 0 is a kernel/gap property.**

---

## 2. The three equality cases (reconstruction)

| | Theorem A (on-line, with mult.) | Theorem D (simple on-line) | Theorem C (distinct on-line) |
|---|---|---|---|
| Atoms | v_γ at every distinct ordinate, **multiplicity-scaled**: v′_γ = √(m_γ)·v_γ, so M′ has diag m_γ and off-diag √(m_γ m_γ′) k(γ−γ′) | v_γ at **simple** ordinates only, M with diag 1, off-diag k(γ−γ′) | v_γ at **all distinct** ordinates, M with diag 1, off-diag k(γ−γ′) (same form as D) |
| Count enters as | **trace** t = Σ m_γ = N₀ (multiplicity) | **rank** (and trace of the simple-atom part) = N_s | **rank** (and trace of the distinct-atom part) = N_d |
| Equality case of t² ≤ rt₂ | atoms orthogonal **and** all λᵢ equal ⟹ all m_γ equal (all zeros simple) **and** orthogonal atoms | atoms orthogonal (equal norms are achievable by window choice) | atoms orthogonal (equal norms achievable) |
| Kernel obstruction | k(γ−γ′) ≠ 0 for gaps ≤ 4 in the window ⟹ orthogonality impossible (numerically: max |k| ≥ 1.07×10⁻² even at the best configuration); PLUS m_γ not all equal | same | same |

**Key structural facts (the heart of the transfer question):**

1. **The Gram form is identical across all three theorems.** The atom inner products are determined *only* by ordinate differences through the same k. The counting scheme decides *which* ordinates are atoms and *how the diagonal is weighted* (multiplicity scaling for A; plain for C and D). The D-atoms are a sub-configuration of the C-atoms (simple ordinates ⊂ distinct ordinates).
2. **The exact identity t₂ = 2t − r + tr Ψ(M) transfers to any atom scheme** — it is linear-algebra, not specific to simple zeros.
3. **The positivity/quantification of tr Ψ(M) transfers with the same kernel-ε**, because it is a property of k over the gap domain (u, v, u+v ≤ 4), which is the same for distinct ordinates as for simple ordinates (see §4).
4. **Multiplicity scaling can only increase tr Ψ**: numerically, tr Ψ(M′) ≥ tr Ψ(Mₐₗₗ₋ₛᵢₘₚₗₑ) at the domain minimizer and in 4000 random configurations (0 violations). Hence ε_A ≥ ε_D. (Numerical support, not a proof.)

---

## 3. Numerics — CHECKED NUMERICALLY

Script: `tools/online_kernel_check.py`
Command: `proot-distro login ubuntu -- python3 /data/data/com.termux/files/home/riemann/tools/online_kernel_check.py`
(mpmath 1.4.1 + numpy 2.3.5 + scipy 1.18.0, ~1 min wall).

| Check | Result |
|---|---|
| K(x) closed form vs mpmath quad | agree to ≤ 1.1×10⁻¹⁷; K(0) = 0.918725369865568427 |
| k(0) = 1; k(2) = −0.01283; k(4) = −0.00318 | confirmed |
| Zeros of k on (0,4] | x = 1.057278, 2.030068, 3.020243 |
| **3-point ε₄ = inf tr Ψ(G(u,v))**, u,v > 0, u+v ≤ 4 | **4.45×10⁻⁴** (grid) / **4.4502×10⁻⁴** (mpmath), at gaps (1.0526, 2.0150), u+v = 3.0677 — interior of the domain |
| Claimed certified bound 221/10⁶ = 2.21×10⁻⁴ | ✓ consistent (bound < true infimum) |
| **Orthogonality impossibility** | min over domain of max(|k(u)|,|k(v)|,|k(u+v)|) = **1.066×10⁻²** > 0 (no triple of gaps makes the atoms orthogonal) |
| **A-case multiplicity blocks** (diag m_γ, off-diag √(mᵢmⱼ)k) | at the ε₄-argmin: tr Ψ = 0.45×10⁻³ (all-simple) vs ≥ 1.00 for any m ≥ 2; 4000 random (u,v,m) samples: **0 violations** of tr Ψ(M′) ≥ tr Ψ(all-simple) |
| 7-point, natural domains (span ≤ 4; and every triple ≤ 4) | sampled min 3.53 / 1.57×10⁻¹ ≫ 19/5000; **19/5000 not independently re-derived** (my domain assumptions may differ from ainta's) |
| H0 = 3/2 − (1/√2)cot(1/√2) | 0.67250070367941164573… ✓ (30 digits) |
| (H0 − ε/4)/(1 − ε/2), ε = 221/10⁶ | 0.672519767113… ✓ |
| (1345000·H0 − 2680)/1340003 | 0.673008527927… ✓ |
| Linear response dc/dε of D's 3-pt formula | H0/2 − 1/4 = 0.086250 |

**Hypothetical constant shifts if the same linear response transfers** (NOT verified; chain algebra needed):
- 3-pt: Theorem A 2/3 → 0.666686 (+1.9×10⁻⁵); Theorem C 5/6 → 0.833352 (+1.9×10⁻⁵)
- 7-pt: Theorem A 2/3 → 0.666994 (+3.3×10⁻⁴); Theorem C 5/6 → 0.833661 (+3.3×10⁻⁴)

---

## 4. Theorem C (distinct zeros, 5/6) — analysis

**Method-level transfer: YES (CHECKED NUMERICALLY, modulo the kernel assumption).**
C's atoms sit at all distinct on-line ordinates; their Gram matrix M has the *identical form* to D's (unit diagonal, entries k(γ−γ′)). The three-consecutive-gap argument goes through verbatim:
- any three consecutive distinct ordinates with gaps u, v satisfy u, v, u+v ≤ 4 (window property, same as for simple ordinates);
- the infimum of tr Ψ over that gap domain is interior (at (1.053, 2.015)), so it is achieved by both simple and distinct configurations;
- hence **ε_C = ε_D = 4.45×10⁻⁴ numerically** (certified lower bound 221/10⁶ in both cases);
- the exact identity t₂ = 2t − r + tr Ψ(M) holds for C's PSD block with the same M-form.

So *if* Theorem C's 5/6 is obtained from the rank–trace chain on the distinct-atom Gram matrix (same two-moment data as D), the stability refinement applies and moves 5/6 by δ = (dc/dε)·ε ≈ +1.9×10⁻⁵ (3-pt) / +3.3×10⁻⁴ (7-pt) — the numbers in §3, labeled HYPOTHETICAL.

**Blocker for a clean verdict (the precise gap):**
1. **C's chain is not available on the phone.** The 5/6 might *not* come from the t² ≤ rt₂ chain on atoms. PLAN.md describes a "two-moment 5/6 distinct wall … robust to the third moment (the separation is a fourth-moment phenomenon)" and lists the integrality steps m² ≥ 2m−1, m² ≥ 3m−2. A natural alternative chain is the Cauchy–Schwarz identity N_d ≥ N₀²/Σm_γ² (multiplicity-moment), in which the operative slack is the *integrality/multiplicity* structure (m_γ ∈ ℕ, m² ≥ 2m−1), **not atom orthogonality** — in that chain the Gram geometry (the k-off-diagonals) is not the quantity the stability term corrects.
2. **Window/kernel dependence.** If C's optimized window differs from D's (the constants 5/6 vs 0.6725 are far apart, which suggests different optimized data), the kernel K, hence ε, must be recomputed. The *method* transfers; the *number* ε is kernel-specific.
3. **Consistency check on the reading of C.** N_d ≥ (5/6)·N is incompatible with Theorem A's 2/3 unless N₀ ≥ 5/6·N is also being proven, which the paper does not claim; the coherent reading is N_d ≥ (5/6)·N₀ (at most 1/6 of on-line zeros, with multiplicity, sit at multiple ordinates). Both readings are insensitive to the transfer analysis below.

**Verdict (C): CONJECTURED.** The stability term exists, is positive, and has the same ε for C's atoms as for D's (verified numerically). Whether it moves the constant 5/6 depends on C's chain: if rank–trace-on-distinct-atoms, yes with δ above (hypothetical numbers); if multiplicity-moment CS, no (different slack). Gap named: C's chain algebra (paper unavailable; fetch blocked).

---

## 5. Theorem A (on-line with multiplicity, 2/3) — analysis

**Method-level transfer: YES for positivity (CHECKED NUMERICALLY), but the constant-level transfer is blocked.**

*Why the positivity still holds:* A's atoms are the multiplicity-scaled atoms v′_γ = √(m_γ) v_γ with Gram M′ (diag m_γ, off-diag √(mᵢmⱼ) k(γ−γ′)). The exact identity t₂ = 2t − r + tr Ψ(M′) holds; numerically tr Ψ(M′) ≥ tr Ψ(Mₐₗₗ₋ₛᵢₘₚₗₑ) uniformly over sampled (gaps, multiplicities), so **ε_A ≥ ε_D = 4.45×10⁻⁴** (numerical support; a proof that the infimum is attained at all-simple is still open).

*Why the constant-level transfer is blocked (the precise structural blockers):*

**Blocker A1 — A's equality case is doubly impossible.** For the with-multiplicity count, the trace is t = Σ m_γ = N₀ but the rank counts *distinct* ordinates, r ≥ N_d + N_p. The rank–trace equality case t² = rt₂ requires both (i) mutually orthogonal atoms — impossible by the kernel (as in D) — and (ii) *all positive eigenvalues equal*, i.e., **all m_γ equal** — false as soon as any multiple zero exists (and Theorem D's own content, 0.6725 of zeros simple, plus the existence of N₀ ≥ N_s counting, does not exclude multiple zeros; the equality case would need all on-line zeros simple, making A ≡ D). So even the ideal refinement cannot attain equality; the multiplicity variation is a *separate* obstruction that the Ψ-correction does capture numerically (tr Ψ(M′) ≥ 1 when any m ≥ 2, vs 4.45×10⁻⁴ all-simple) but whose *conversion into a constant shift* is governed by A's chain, which we do not have.

**Blocker A2 — evidence the 2/3 is data-limited, not slack-limited.** PLAN.md's headline finding: "The 2/3 deficit is arithmetic — pair-correlation content, not method-inherent (Ihara-zeta sandbox on provably-RH-true objects)." If the 2/3 is limited by the pair-correlation *data* (the two moments themselves) rather than by the rank–trace inequality's slack, then tightening the inequality via tr Ψ(M) moves nothing — the transfer is **vacuous for the constant**. The D-case was different: D's 0.6725 had measurable slack (external groups recovered ~5–7×10⁻⁴), which is exactly what made the stability term bite. A discriminator exists: compute the with-multiplicity certificate's two-moment ratio at the optimized window; if the bound is already saturated by the data, no ε can move it.

**Blocker A3 — the task's hint.** "The equality case may involve different vectors." If A's chain is a trace + Sylvester-rank argument (count via tr(W) with eigenvalue *saturation* bounds, N_d = N₀ at equality) rather than the atom rank–trace, then A's equality case involves *top eigenvectors*, not atom orthogonality, and the Gram-stability term is simply not the right correction for A — the operative refinement for A would be a *multiplicity-integrality* correction (m² ≥ 2m−1, 3m−2), not tr Ψ(M).

**Verdict (A): INCONCLUSIVE (blocker named).** The stability term is positive for A's atoms (ε_A ≥ ε_D, numerically supported), but (a) A's equality case requires equal multiplicities in addition to orthogonality; (b) the "2/3 is arithmetic" finding suggests data-saturation, making the transfer vacuous; (c) A's equality case may involve different vectors (eigenvalue saturation), making tr Ψ(M) the wrong object. A definitive constant-level statement requires A's actual chain.

---

## 6. Assumptions register

1. Same kernel k for all three theorems (task's framing). If a theorem's optimized window differs, its ε must be recomputed.
2. Off-line pairs give exactly (1,1)-indefinite Sylvester blocks; rank(P) ≥ N_d + N_p.
3. The two-moment data (t, t₂) are the same inputs in all three theorems, differing only in which atoms are counted.
4. Reading of Theorem C: N_d ≥ (5/6)·N₀ (distinct proportion of on-line zeros), which is the only reading consistent with Theorem A = 2/3 and Theorem D = 0.6725; the analysis is insensitive to the exact normalization.
5. The "ε per 3-block" normalization of the external groups matches tr Ψ of the 3×3 Gram block (the 221/10⁶ and 19/5000 values are their *certified* bounds; the 3-point infimum recomputed here is sharper, 4.45×10⁻⁴, and consistent).

## 7. What would settle this (discriminators)

1. **Get the paper / repo texts** (unblock network or pull via the laptop when the pclink is restored): read Theorem A's and Theorem C's actual inequality chains. This alone settles whether they use atom rank–trace (transfer applies) or a different chain (does not / different correction).
2. **Data-saturation test for A:** compute the optimized with-multiplicity certificate's m₁²/m₂; if data-saturated, transfer is vacuous.
3. **Kernel audit:** confirm whether C's optimized window is the same as D's; if not, recompute ε for C's kernel (cheap: same script, new K).
4. **Adversarial check of the ε-transfer claim:** prove (or refute) that tr Ψ(D^{1/2} G D^{1/2}) ≥ tr Ψ(G) for diagonal D ≥ I over the gap domain (numerically supported here; a proof would upgrade ε_A ≥ ε_D from CONJECTURED to PROVEN).
5. **Q2 linkage:** the discovery note's Q2 (does the stability term beat the 0.6818 in-class ceiling for simple zeros) is the same question for A/C: does tr Ψ(M) escape the certificate-class ceiling that produced the "arithmetic" 2/3? Run the LP/certificate-class analysis including tr Ψ as a constraint.

## 8. Files
- `tools/online_kernel_check.py` — all numerics above (self-contained; prints verdicts).
- `research/notes/discovery-gram-stability-673.md` — updated with a pointer to this note (Q1 status).
