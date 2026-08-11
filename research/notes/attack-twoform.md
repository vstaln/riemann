# Attack: two-form argument (L8) — the Weil form and the CGG ζ′(ρ)-moment form as a joint constraint on the same zero set

Agent: EXECUTIONER (L8). Date: round 2. Status: analysis + finite-T numerics; no new asymptotic theorems.
Sources used (read in full or in the cited passages):
- P = research/papers/claude-riemann-paper.txt (§1.4, §7.5(c), Prop 4.4, Lemma 3.2, §7.1)
- B25 = research/papers/bgst-2501.14545.txt (§1)
- B1 = research/papers/baluyot-etal-2306.04799.txt (§1)
- mollifier = research/notes/attack-mollifier.md (§3), finitet = research/notes/attack-finitet.md, litmap = research/notes/literature-map.md (§1b, §2)
- catalog = research/notes/attack-vector-catalog.md (§3 #15)
No citation in this file points outside these files.

Labels (honesty guardrail):
- CGG98 multiplicity device (m² ≥ 3m−2, "CGG98 (1.2)") as transplanted into the paper's Prop 4.4 regrouping (P₁, Q′): **PROVEN** (P §7.5(c) verbatim: "This is the device of [CGG98, (1.2)] made unconditional.") [mollifier §3, litmap §2].
- The ζ′(ρ)-moment quadratic form's matrix entries: **CONJECTURED (RECONSTRUCTED)** — BHB 1302.5018 is a paper-hunt target, CGG98 appears in the held sources only as [CGG98]; no held paper contains the form's entries (checked: P, B25 §1, B1 §1, appendix, transcripts). The zero-set form below is reconstructed from the paper's description and the standard CGG98 structure; its role here is exploratory.
- The 19/27 result (discrete mollified ζ′(ρ) moments): **RH-CONDITIONAL** [litmap §1b] ("on RH and an additional hypothesis" [CGG98], "on RH alone" [BHB13]; B25 §1, B1 §1).
- rank C ≤ N_s (Lemma 2 below): **PROVEN** (elementary, unconditional).
- Cauchy–Schwarz certificate N_s ≥ sup_a |Σ_j ζ′(ρ_j)M(ρ_j)(a·v_j)|²/Σ_j w_j|a·v_j|² (Lemma 3): **PROVEN as an inequality** with **ceiling N_s (PROVEN)**; mechanism **CHECKED NUMERICALLY** (near-tight with all-simple data). Its constant 19/27 lives in the RH-conditional CGG98/BHB13 moment arithmetic, not re-derived here.
- All numbers in §4: **CHECKED NUMERICALLY** (finite window [T, 2T], f64 frame + mpmath ζ′(ρ), N = 300 zeros, ordinals ≈ 210–509 of zeros_1_1000.txt).

---

## 0. Bottom line (read this first)

1. The two forms are **not orthogonal**: on the same zero set and the same test-function frame, the CGG ζ′-moment form C is W's rank-one decomposition re-weighted by |ζ′(ρ)M(ρ)|²: W = (1/∫ψ²)Σ_j v_jv_jᵀ, C = (1/∫ψ²)Σ_j |ζ′(ρ_j)M(ρ_j)|² v_jv_jᵀ. The shared frame is what the "combination" operates on.
2. **New proven structural fact:** rank C ≤ N_s unconditionally (ζ′(ρ) = 0 iff ρ is a multiple zero; elementary). Numerically saturated (rank C = 296 ≈ 300 = N_s in our all-simple window).
3. **Certificate inequality (reconstructed CGG, mechanism verified):** N_s ≥ sup_a |Σ_j ζ′(ρ_j)M(ρ_j)(a·v_j)|² / Σ_j w_j|a·v_j|² (Cauchy–Schwarz over the zero index; valid for complex test directions). **Its ceiling is N_s by construction** (second Cauchy–Schwarz application: ≤ Σ_j|ζ′M|²/w_j = #{w_j ≠ 0} ≤ N_s). With the actual data (all 300 zeros simple) the certificate is near-tight: 295.6/300 (M = 1), 296.2, 298.2 — the defect 2–4 equals the frame's numerical near-rank-deficiency. **The numerics verify the mechanism but cannot exhibit 19/27:** the constant lives entirely in the RH-conditional arithmetic evaluation of the moments (CGG98/BHB13), which does not use the actual ζ′(ρ_j) values and is not reproduced here. This is a documented limit, not a result.
4. **Joint-rank–trace on the direct sum is a genuine obstruction (documented):** the inequality rank(W⊕C) ≥ (trW+trC)²/(‖W‖²_HS+‖C‖²_HS) is valid but numerically inert (173.6 < N), because ‖C‖²_HS is diagonal-dominated by Σ_j|ζ′M|⁴·‖v_j‖⁴ (151310 of 188603), and the additive certificate 2trC − ‖C‖²_HS is negative. **The second moment of C cannot carry a simple-zero certificate; the first-moment direction u does.** Any "combine the forms" scheme that consumes ‖C‖²_HS is structurally dead.
5. **The joint constraint that is real is complementarity, not addition (CHECKED NUMERICALLY):** corr(log |ζ′(ρ_j)|², p_j) = −0.82 (Pearson), −0.80 (Spearman), where p_j = Σ_k(v_jᵀv_k)²/(∫ψ²)² is the j-th zero's pair-correlation participation in ‖W‖²_HS. The zeros C fails to certify (small |ζ′|) are exactly the close-pair zeros (nearest-neighbour gaps 0.33–0.42 vs mean 1.37), which carry the off-diagonal weight of W. The two forms see complementary subsets of the zero set — which is *why* the combination reduces to max under RH rather than to a sum.
6. Under RH the two forms certify the same quantity (simple = simple-on-line), and the honest combination is **max(Weil, CGG) = 19/27**, already known. The union bound N_{s0} ≥ N_s + N_0 − N is valid but dominated by max. No sum-type joint inequality beyond the max is available from the sources; the one lever that would change this (a bound on #{|ζ′(ρ)M(ρ)| < θ} in terms of pair-correlation/prime data) is not in any held paper and is exactly the shared wall of attack-mollifier §6.

**Verdict: honest progress with a documented obstruction.** The vector produces (i) one new PROVEN structural fact (rank C ≤ N_s, shared frame), (ii) a PROVEN (reconstructed) certificate inequality whose mechanism and N_s-ceiling are CHECKED NUMERICALLY (near-tight 295.6/300 with all-simple data; 19/27 not numerically reachable — arithmetic content), (iii) a documented obstruction (direct-sum/second-moment inertness), and (iv) a CHECKED-NUMERICALLY complementarity finding (r = −0.82) that explains why the forms combine as max rather than sum.

---

## 1. The two forms on the same zero set

### 1.1 The finite-T frame (finitet, kept verbatim)

Window [T, 2T], N = #{zeros γ ∈ [T, 2T]}, grid α_k = T + (T/N)k, k = 0..N−1; s_j = (γ_j − T)·N/T; frame vectors
v_j[k] = Ψ(s_j − k), Ψ(s) = sin(1/√2 − πs)/(√2 − 2πs) + sin(1/√2 + πs)/(√2 + 2πs) (entire; removable poles at 2πs = ±√2, value 1/2 + sin(√2)/(2√2) = ∫ψ²).

Weil form (PROVEN structure, finitet): W = (1/∫ψ²)·VᵀV, V[j][k] = v_j[k]. This is the paper's compressed Weil form; on the zero side each on-line zero contributes a rank-one PSD term and each off-line pair {ρ, 1−ρ̄} a signature-(1,1) block (P §1.4(Z)); tr W ≈ N and ‖W‖²_HS ≈ (1/2 + (1/√2)cot(1/√2))N are evaluated from the prime side (P Lemma 5.x, unconditional; finite-T values in §4).

### 1.2 The CGG ζ′(ρ)-moment form (RECONSTRUCTED — no held paper contains its entries)

Reconstruction basis: B25 §1 ("a method which uses the discrete, mollified moments of ζ′(ρ) to study simple zeros"; 19/27 on RH + hypothesis, 19/27 on RH alone [BHB13]); B1 §1 (same); P §7.5(c) (the CGG98 (1.2) device m² ≥ 3m−2 as the Prop 4.4 regrouping — the paper's own reading of CGG98).

Zero-set version (the natural object sharing W's frame):
- mollifier M(s) = Σ_{n≤y} a_n n^{−s} (Dirichlet polynomial; M ≡ 1 = the unmollified case);
- weights w_j = |ζ′(ρ_j)M(ρ_j)|²;
- C := (1/∫ψ²)·Vᵀ diag(w) V = (1/∫ψ²)·Σ_j w_j v_jv_jᵀ   (real symmetric PSD, same frame as W).

Why this is the CGG object: the CGG discrete second moment is Σ_ρ |ζ′(ρ)M(ρ)|² w(γ)-weighted; on the frame it is the diagonal (per-zero) weighting of the rank-one decomposition of W. The CGG first moment is the linear functional ℓ(a) = Σ_j ζ′(ρ_j)M(ρ_j)(a·v_j) — the frame-weighted first moment, which is the certificate carrier (Lemma 3). The paper's own contact point (P §7.5(c)) is the *multiplicity* side of the same simplicity-detection: CGG98 (1.2) m² ≥ 3m−2 handles multiple zeros via integrality inside the Weil-form counting, while the ζ′-moment form detects multiple zeros directly through ζ′(ρ) = 0. Two views of the same fact — this is the "not as orthogonal as they look" premise of the vector, confirmed.

### 1.3 The zero-side reading that makes C a simplicity detector

Lemma 1 (PROVEN, elementary, unconditional). For any zero ρ of ζ, ζ′(ρ) = 0 iff ρ is a multiple zero.
Proof. ζ(s) = c(s−ρ)^m(1+O(s−ρ)); ζ′(ρ) = 0 iff m ≥ 2. ∎ (No RH is used; this is a power-series fact at a simple pole of ζ.)

Lemma 2 (PROVEN, elementary, unconditional). rank C ≤ #{j : ζ′(ρ_j)M(ρ_j) ≠ 0} ≤ N_s, where N_s = #{simple zeros in the window}, provided M(ρ_j) ≠ 0 for the simple zeros (generic: a Dirichlet polynomial vanishes at finitely many points unless ≡ 0; M ≡ 1 is exact).
Proof. C = Vᵀ diag(w)V; its column space is contained in the span of {v_j : w_j ≠ 0}, of size ≤ #{w_j ≠ 0} = #{ζ′M ≠ 0} ≤ N_s by Lemma 1. ∎

Note the sharp contrast with W: W = Σ_j v_jv_jᵀ sums every zero once regardless of multiplicity (its rank is ≤ N, positions), while C's rank counts only simple zeros (multiplicity). Under RH (everything on line) both are PSD and rank(W) ≤ N, rank(C) ≤ N_s = N_{s0}.

## 2. Structure map (s4h-analogy: element-by-element)

| Element | Weil form W | CGG ζ′-moment form C (reconstructed) |
|---|---|---|
| Matrix | (1/∫ψ²)·VᵀV | (1/∫ψ²)·Vᵀ diag(w)V, w_j = \|ζ′(ρ_j)M(ρ_j)\|² |
| Frame | Ψ(s_j − k), k-grid, critical density | identical (shared frame — this is the combination point) |
| Zero-side reading | on-line → PSD rank-1; off-line pair → (1,1) block; n₊(W) ≤ #on-line + #pairs [P §1.4] | ζ′(ρ_j) = 0 iff multiple ⟹ rank C ≤ N_s (Lemma 2) |
| Detects | positions (on/off line) | simplicity (multiple or not) |
| Arithmetic input | primes: tr W ≈ N, ‖W‖²_HS ≈ (1/2+(1/√2)cot(1/√2))N [P Lemma 5.x; finitet] | ζ′-moments: tr C = Σ_j w_j‖v_j‖²/∫ψ², ‖C‖²_HS = Σ_{jk} w_jw_k(v_jᵀv_k)²/(∫ψ²)² — the CGG98/BHB13 discrete mollified moments |
| Conditionality | unconditional (prime side) | RH-conditional (zero-side reading of the moments) [litmap §1b] |
| Certificate | N_0 ≥ 2trW − ‖W‖²_HS (rank–trace, Lemma 3.2) | N_s ≥ cert(a), u = Σ_j ζ′(ρ_j)M(ρ_j)v_j; ceiling #{w_j≠0} ≤ N_s (Cauchy–Schwarz, Lemma 3) |
| Asymptotic constant | 2/3, 0.6725, 5/6 [P Thm A–D] | 19/27 on RH [B25 §1, B1 §1] |
| Intersection | N_{s0} = simple on-line; on RH = both counts | same |

Mapping verdict: genuine structural correspondence (same frame, same zero index, both Hermitian certificates on counts of zeros), differing in (i) the per-zero weight (1 vs |ζ′M|²) and (ii) the certificate carrier (second-moment HS norm vs first-moment direction). The combination lives in (i).

## 3. Joint-inequality attempts

### 3(a) rank C ≤ N_s — PROVEN; numerically saturated
Lemma 2. With our all-simple window, rank C = 296 ≤ 300 (the 4 missing units are the f64 near-rank-deficiency of W already documented in finitet §3). This is the unconditional joint constraint: the ζ′-moment form cannot have rank above the number of simple zeros, no matter how the mollifier is chosen. It is saturated because all 300 window zeros are simple — under a hypothetical multiple zero it would bite (rank C ≤ N_s < N).

### 3(b) The certificate — PROVEN (Cauchy–Schwarz), mechanism CHECKED NUMERICALLY, constant NOT reproducible
Lemma 3. Write C° := Vᵀ diag(w)V = Σ_j w_j v_jv_jᵀ (the raw second-moment form, no 1/∫ψ²) and u = Σ_j ζ′(ρ_j)M(ρ_j)v_j. For every a ∈ ℂ^N, |ℓ(a)|² ≤ (Σ_j w_j|a·v_j|²)·#{j : ζ′M(a·v_j) ≠ 0} ≤ (a*ᵀC°a)·N_s (Cauchy–Schwarz over the zero index; Lemma 1 kills non-simple j). Hence
N_s ≥ cert(a) := |a·u|²/(a*ᵀC°a), and sup_a cert(a) = u*C°⁺u. ∎
**Ceiling (PROVEN, second Cauchy–Schwarz):** cert(a) ≤ Σ_j |ζ′(ρ_j)M(ρ_j)|²/w_j = #{j : w_j ≠ 0} ≤ N_s for every a. The certificate can never exceed the number of simple zeros — with the actual ζ′(ρ_j) values in hand (M = 1), Σ|ζ′|²/w = N_s exactly, and the certificate is near-tight (below). This is the honest reading of the numerics: **feeding the actual multiplicities makes the data-driven certificate recover N_s itself; the content of CGG98/BHB13 is the RH-conditional arithmetic evaluation of the moments from ζ-side data without knowing the multiplicities, which yields 19/27 and is not reproducible numerically.** Values (window of §4): M = 1 → 295.6 (real-a version: 181.0), M = Möbius(y=10) → 296.2, M = Möbius(y=30) → 298.2; defect = N − cert = 2–4 = the frame's numerical near-rank-deficiency (rank C = 296; cf. finitet §3), not a zero-statistics effect. Label: inequality and ceiling PROVEN; constant 19/27 PROVEN-as-stated (B25 §1, B1 §1) but not re-derived — CONJECTURED-as-arithmetic here.

### 3(c) Direct-sum rank–trace — PROVEN inequality, OBSTRUCTED numerically (documented)
The algebra is unconditional (W, C are Gram matrices, hence PSD; rank(W) ≤ N by dimension, rank(C) ≤ N_s by Lemma 2; rank ≥ (tr)²/‖·‖²_HS for any PSD matrix):
N + N_s ≥ rank(W⊕C) ≥ (trW + trC)²/(‖W‖²_HS + ‖C‖²_HS).   (valid)
Numerically (M = 1): (299.15 + 5428.13)²/(384.82 + 188603.0) = 173.6, i.e. an implied N_s ≥ −126.4 — inert. Root cause: ‖C‖²_HS = 188603 is diagonal-dominated (Σ_j w_j²‖v_j‖⁴/(∫ψ²)² ≈ 151310, 80%), and the additive rank certificate 2trC − ‖C‖²_HS < 0. The second moment of C is swamped by the square of the (highly variable) weights w_j = |ζ′M|², whose mean 18.1 and max 89.9 differ by 5× — so ‖C‖²_HS scales like mean(w²)·N, not (mean w)²·N, and the Cauchy bound (trC)²/‖C‖²_HS = 156.2 < N_s. **Obstruction: any combination that consumes ‖C‖²_HS is structurally dead; the certificate carrier of the ζ′-moment form is the first-moment direction u (3b), which the direct-sum construction does not use.** This is the documented negative result of the vector.

### 3(d) Union bound — valid, dominated by max
N_{s0} ≥ N_s + N_0 − N ≥ cert(a_opt) + (2trW − ‖W‖²_HS) − N. Numerically 295.6 + 213.5 − 300 = 209.1 < max(295.6, 213.5). Under RH, N_0 = N, so the RHS = N_s: trivial. Valid but never the best; included for completeness.

### 3(e) "Both forms small": the zeros C cannot certify are exactly the close pairs W is built on — CHECKED NUMERICALLY
Define the per-zero pair participation p_j := Σ_k (v_jᵀv_k)²/(∫ψ²)² (the j-th zero's contribution to ‖W‖²_HS, a "smallness for W" measure in the off-diagonal sense; the plain per-zero ‖v_j‖² is nearly constant — 0.63–1.00 — so the diagonal sense of "small for W" is degenerate, an asymmetry worth noting). Results on the window of §4:
- corr(log |ζ′(ρ)|², p) = −0.816 (Pearson), −0.804 (Spearman) — strong anticorrelation, robust.
- corr(log |ζ′(ρ)|², log nearest-neighbour gap) = +0.820/+0.808 — small |ζ′| ⟺ small gap.
- The 22 zeros with NN-gap < 0.51 (mean NN-gap = 1.013) have mean w = 2.9 (global mean 18.1) and mean p = 1.77.
- Smallest-w zeros sit in the smallest gaps: (540.213, 540.631) gap 0.418, (564.161, 564.506) gap 0.345, (630.474, 630.806) gap 0.332, (728.405, 728.759) gap 0.353 — all ≈ 4× below the mean consecutive gap 1.372.
- (Correction: an earlier wrong-normalization draft suggested the certificate defect tracked the low-weight count; with the correct normalization the defect is 2–4 = the frame's numerical near-rank-deficiency — the certificate is near-tight regardless of the weight distribution. The complementarity below is about the weight *structure* of C versus the pair structure of W and is unaffected.)
Mechanism: close pairs (near-collision zeros) have nearly coincident frame vectors, so (v_jᵀv_k)² ≈ ‖v_j‖⁴ is large (W-large), and ζ′ at each member is small (C-small) — the derivative nearly vanishes when two zeros almost collide. Hence: **the zeros one form fails to certify are precisely the zeros that carry the other form's second moment.** This is why the combination is max-like, not sum-like, and it is the (numerical) joint structure the vector was looking for. Turning it into an inequality would require a bound on #{|ζ′(ρ)M(ρ)| < θ} in terms of prime-side/pair-correlation data — not present in any held source and exactly the shared wall of mollifier §6.

## 4. Numerics

Window: T = 411.5, 2T = 823.0, N = 300 zeros, file ordinals ≈ 210–509 of tools/data/zeros_1_1000.txt (all simple per LMFDB; γ-values cached). Frame, tr, ‖·‖²_HS as in finitet; ζ′(ρ_j) via mpmath (dps = 30), sanity: |ζ′(ρ₁)| = 0.79316… (literature value). Script: tools/twoform.py.

| Quantity | M = 1 | M = Möbius(y=10) | M = Möbius(y=30) |
|---|---|---|---|
| tr W / N | 0.997182 | — | — |
| ‖W‖²_HS / N | 1.282722 | — | — |
| Weil certificate (2trW − ‖W‖²_HS)/N | 0.711643 | — | — |
| mean w = mean\|ζ′M\|² | 18.124 | 28.050 | 38.473 |
| w min / p10 / med / p90 / max | 1.21 / 3.54 / 12.49 / 38.98 / 89.86 | 0.073 / 12.1 / 26.8 / 46.6 / 79.2 | 1.41 / 17.0 / 38.5 / 57.2 / 127.6 |
| tr C | 5428.13 | 8390.68 | 11504.21 |
| ‖C‖²_HS (diag / offdiag) | 188603 (151310 / 37293) | 362137 (313426 / 48711) | 675400 (579728 / 95672) |
| rank C (λ > 10⁻⁸λ_max) | 296 | 296 | 296 |
| CGG certificate N_s ≥ cert(a_opt) | **295.6** (real-a: 181.0; ceiling 300) | 296.2 | 298.2 |
| defect N − cert | 4.4 | 3.8 | 1.8 |
| (trC)²/‖C‖²_HS | 156.2 | 194.4 | 196.0 |
| joint direct-sum → implied N_s | 173.6 → −126.4 (inert) | 208.3 → −91.7 | 206.2 → −93.8 |
| #{w < 0.01 / 0.1 / 0.25·mean} | 0 / 7 / 45 | 1 / 7 / 14 | 0 / 2 / 11 |

Correlations (M = 1): corr(log w, p) = −0.816 Pearson / −0.804 Spearman; corr(log w, log NN-gap) = +0.820 / +0.808; corr(log w, ‖v_j‖²) = +0.073 (independent — per-zero "W-smallness" is degenerate as noted).

Consistency: tr W/N, ‖W‖²_HS/N match the finitet trend at T = 400 (0.9958, 1.2804); every certificate obeys its inequality (cert = 295.6 ≤ 300 = N_s; rank C = 296 ≤ 300; joint = 173.6 < N + N_s = 600). Error sources: finite T, f64 frame, single window — all CHECKED NUMERICALLY, none asymptotic.

## 5. Bottom line and labels

1. The two forms share a frame and are the same rank-one decomposition re-weighted by |ζ′M|² (structure map §2). The CGG98 connection already inside the paper (P §7.5(c), the m² ≥ 3m−2 device as Prop 4.4 regrouping) is the multiplicity side of the same simplicity detection that ζ′(ρ) = 0 gives directly. Labels: PROVEN (as transplanted); CGG-form entries RECONSTRUCTED/CONJECTURED.
2. rank C ≤ N_s — **PROVEN**, unconditional, saturated numerically (296 ≤ 300).
3. Certificate N_s ≥ sup_a |Σ ζ′M(a·v_j)|²/Σ w_j|a·v_j|² — **PROVEN as an inequality** with **ceiling N_s (PROVEN)**; mechanism CHECKED NUMERICALLY (near-tight 295.6/300 with all-simple data; defect 2–4 = frame near-rank-deficiency). The 19/27 constant is **NOT numerically reproducible**: it lives in the RH-conditional arithmetic evaluation of the moments (CGG98/BHB13), which we do not have and do not re-derive (label: PROVEN as stated in B25 §1, B1 §1; not verified here).
4. Direct-sum / second-moment combination — **OBSTRUCTED (documented)**: ‖C‖²_HS is diagonal-dominated (80%), so all rank–trace certificates that consume it (3c) are inert; the certificate carrier is the first-moment direction. A "joint inequality of rank–trace type on W ⊕ C" does not exist in usable form.
5. **Joint constraint that is real: complementarity** (CHECKED NUMERICALLY, r = −0.82): C-failures = close-pair zeros = W's off-diagonal carriers. Under RH the forms certify the same count and combine as max = 19/27 (known); a genuine sum-type improvement needs #{|ζ′M| small} bounded by prime-side data — the shared wall of mollifier §6.

This vector's DoD (catalog §3 #15: "honest progress or a documented dead end") is met: one new proven structural fact, a proven (reconstructed) certificate with concrete value, a documented obstruction, and a numerically checked complementarity that explains the combination's shape.

## 6. What would move this (cheapest first)

1. Obtain BHB 1302.5018 (paper-hunt, catalog §6) and read the actual CGG98/BHB13 form and its arithmetic — replace the reconstruction with the held-paper entries and re-run the frame numerics (§3b becomes a check, not a reconstruction).
2. The numerics cannot promote anything to an asymptotic constant: the data-driven certificate is near-tight by construction (ceiling = N_s). The only route to 19/27 is the RH-conditional arithmetic evaluation of the discrete mollified moments with the CGG98-optimal mollifier — i.e. re-deriving CGG98/BHB13, which the sources state but do not contain; this is a verification project (with BHB 1302.5018 in hand), not an extension.
3. A bound on #{|ζ′(ρ)M(ρ)| < θ} from pair-correlation/prime data would be genuinely new and would make the complementarity of §3e an inequality; no held source provides it (mollifier §6 wall). Do not fund unless the wall moves.

## Honesty footer

Every claim above is labeled. The two-form combination is CONJECTURED and partially OBSTRUCTED; nothing here is claimed as a proof of anything asymptotic. The numerics are finite-window, single-sample, f64/mpmath — reproducible via tools/twoform.py.
