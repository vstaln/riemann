# IPR diagnostics: is the realized world spectrally near the crystal?

**Agent:** EXECUTIONER (measurement) — vector #6 "IPR — spectral-slack diagnostics (C4.1/C4.3/C6.1)" (attack-vector-catalog-3.md §3, score 365)
**Question:** Where does the spectrum of the real certificate Gram matrix W_T sit — GUE-like delocalized (IPR ~ c/N) or crystal-like localized (IPR ~ O(1))? What does that say about whether the 0.68185 ceiling is tight in the realized world?
**Status:** MEASURED, all numbers code-backed. Verdict: the realized W_T (paper-realistic kernel) is **fully delocalized, GOE-class** — zero delta-like modes at every height, no mobility edge — and a control shows this is *discriminative* (lattice < real < poisson) but that **no zero configuration at all** (including a perfect lattice and a lattice with the crystal's coincident-pair defect) produces O(1)-localized eigenvectors through the actual certificate kernel. The "crystal ⇒ IPR O(1)" signature that C4.1 postulates is **invisible through this kernel**, so IPR is a weak probe of crystal proximity; the robust realized-world slack statements come from the spectrum (λ_max ≈ 5.4–5.6, effective rank ≈ 0.52N, real-data bound/N = −1.8 ≪ 0.6725) and are configuration-independent in direction.

---

## 1. Object, kernels, pipeline (CHECKED NUMERICALLY)

- **Object:** W_T = (1/∫φ²)·VᵀV, V[ρ][k] = Φ̂(s_ρ − k), s_ρ = (γ_ρ − T)·N/T, N = #{γ ∈ [T, 2T)} — the frequency-indexed two-moment/certificate Gram matrix of the finitet construction (tools/finitet, `bin_cinf.rs`). Windows: **T = 200 → N = 123; T = 400 → N = 289; T = 600 → N = 472** (zeros from tools/data/zeros_1_1000.txt, γ_max = 1419.42).
- **Kernels:** (i) *hard-cos* — round-1 idealized C⁰ model ψ(u) = cos(√2u)1_{|u|≤1/2}; (ii) *c^inf-cos* — paper-realistic C⁸-smoothed χ-ramp kernel with the paper's ε = T/N (the "real world" certificate kernel); (iii) *c^inf-sqrtcos* — the literal paper kernel φ = χχ√cos. 
- **Pipeline:** Rust builds W_T (kernel construction copied verbatim from the validated tools/finitet code — cross-checked: trW/N, HS2/N, bound/N reproduce run_output_cinf.txt exactly); numpy `linalg.eigh` gives the full spectrum; IPR_j = Σ_k v_jk⁴/(Σ_k v_jk²)² per eigenvector.
- **IPR conventions:** delta (one component) ⇒ IPR = 1; GOE bulk ⇒ IPR ≈ 3/(N+2); "delta-like" threshold IPR ≥ 0.5 (≤ 2 effective components). Empirical GOE reference (symmetric Gaussian ensemble, 30 draws) matches 3/(N+2): 0.02411±0.00044 vs 0.02400 (N=123), 0.01031±0.00009 vs 0.01031 (N=289), 0.00632±0.00003 vs 0.00633 (N=472).

## 2. Headline table — spectrum and localization by kernel and height

| kernel | T | N | λ_max | median λ | eff.rank (λ>10⁻³λ_max) | mean IPR·N | weight-IPR·N¹ | #modes IPR≥0.1 | #modes IPR≥0.5 | #neg-eig |
|---|---|---|---|---|---|---|---|---|---|---|
| c^inf-cos (ε=T/N) | 200 | 123 | 5.393 | 0.018 | 67 (0.545N) | 2.22 | 2.01 | 0 | 0 | 0 |
| c^inf-cos (ε=T/N) | 400 | 289 | 5.530 | 0.013 | 153 (0.529N) | 3.55 | 2.45 | 0 | 0 | 0 |
| c^inf-cos (ε=T/N) | 600 | 472 | 5.588 | 0.012 | 246 (0.521N) | 4.22 | 2.72 | 0 | 0 | 0 |
| c^inf-sqrtcos | 600 | 472 | 5.558 | 0.012 | 247 (0.523N) | 4.24 | 2.74 | 0 | 0 | 0 |
| hard-cos (C⁰ model) | 200 | 123 | 2.015 | 1.080 | 120 (0.976N) | 25.6 | — | 91 | 6 | 0 |
| hard-cos (C⁰ model) | 400 | 289 | 2.009 | 1.086 | 283 (0.979N) | 60.6 | — | 181 | 31 | 0 |
| hard-cos (C⁰ model) | 600 | 472 | 2.175 | 1.074 | 464 (0.983N) | 88.3 | 110.7 | 245 | 40 | 0 |
| GOE bulk (theory) | any | N | — | — | — | 3 | 3 | — | — | — |

¹ weight-IPR·N = (Σ_j λ_j·IPR_j / Σ_j λ_j)·N — localization weighted by spectral weight (certificate-relevant).

**Reading:** the paper-realistic kernel gives a *delocalized, GOE-class* spectrum at every height (mean IPR·N ∈ [2.2, 4.2] vs GOE 3), zero modes with IPR ≥ 0.1 out of 123/289/472, zero negative eigenvalues, and a *near-rank-deficient* matrix (effective rank ≈ 0.52–0.55N; λ_max ≈ 5.4–5.6 with median λ ≈ 0.01–0.02 — the trace is carried by a minority of O(3–5) eigenvalues). The C⁰ idealized model is qualitatively different: strongly localized (mean IPR·N ≈ 26–88, growing with N) with genuine near-delta modes (max IPR ≈ 0.85 at T=600). The IPR is therefore **kernel-observable, not a zero-set invariant** — only the smoothed kernels are the paper's actual φ_T (the theorems' hypotheses are C^∞), so the delocalized picture is the relevant one.

## 3. Energy-resolved IPR — mobility-edge scan (C4.3) (CHECKED NUMERICALLY)

Real zeros, c^inf-cos ε=T/N, T=600, 12 equal-count bins in λ (descending):

| λ range | mean IPR·N | λ range | mean IPR·N |
|---|---|---|---|
| [0, ~10⁻¹⁴) ² | 19.3 | [0.38, 1.27) | 3.05 |
| [~10⁻¹⁴, ~10⁻¹⁴) ² | 5.5 | [1.27, 2.80) | 2.35 |
| [~10⁻¹⁴, ~10⁻¹⁴) ² | 2.3 | [2.80, 4.58) | 3.03 |
| [~10⁻¹⁴, ~10⁻¹⁴) ² | 2.7 | [4.58, 5.60) | 2.68 |
| [~10⁻¹⁴, 0.0008) ² | 2.6 | | |
| [0.0008, 0.0116) | 2.4 | top-decile/bulk ratio | 0.57 |
| [0.0116, 0.088) | 2.4 | | |
| [0.088, 0.38) | 2.1 | | |

² Numerical null-space tail (λ ~ 10⁻¹⁴, ~8% of modes): IPR there is **basis-dependent** (arbitrary vectors in a degenerate subspace returned by eigh) and carries zero spectral weight — not a physical statement.

**No mobility edge:** over the spectral-weight-carrying range (λ ≳ 10⁻³·λ_max), mean IPR·N is flat in [2.1, 3.1] — single-phase, GOE-class, delocalized at every energy. The only "localized-looking" modes are the numerical null space (λ ~ 10⁻¹⁴), which is an artifact of basis choice in a degenerate subspace, not a two-phase structure. For hard-cos, by contrast, there **is** a clear energy profile (bulk IPR·N ≈ 31–36, top-λ modes IPR·N ≈ 128–196, max IPR 0.85) — but that is the C⁰ idealized model, not the paper kernel. Note: C6.2's "localized modes at eigenvalue ≈ 2" prediction appears in the hard-cos model (λ ≈ 1.7–2.2 modes localized) and is **absent** in the paper-realistic kernel (near λ = 2: IPR·N ≈ 2.4).

## 4. Localized-fraction scaling n₋/N vs T (C6.1) (CHECKED NUMERICALLY)

Task definition (delta-like, IPR ≥ 0.5) — c^inf-cos:

| T | N | n₋/N (IPR ≥ 0.5) | n₋/N (IPR ≥ 0.1) | n₋/N (IPR·N ≥ 3) | n₋/N (IPR·N ≥ 10) | mean IPR·N |
|---|---|---|---|---|---|---|
| 200 | 123 | **0.0000** (0) | 0.0000 | 0.130 | 0.000 | 2.22 |
| 400 | 289 | **0.0000** (0) | 0.0000 | 0.204 | 0.090 | 3.55 |
| 600 | 472 | **0.0000** (0) | 0.0000 | 0.261 | 0.100 | 4.22 |

C6.1's original definition (negative-eigenvalue count): **n₋ = 0 at every T**, every kernel (λ_min ≥ −3.3×10⁻¹³, numerical). The realized world is fully on-line: no off-line/defect structure at IPR resolution, no localized fraction at any height up to T = 600. The "→ 0 or → const?" question answers trivially: it is *already 0 at the smallest T*; there are no localized modes to delocalize. The soft metric IPR·N ≥ 3 (modes above GOE-typical) grows 0.13 → 0.26 — a weak trend in the *delocalized* regime (mean IPR·N: 2.2 → 4.2, still O(1)), not toward the crystal (which would need IPR·N ~ N).

## 5. Controls — is the IPR diagnostic discriminative? (CHECKED NUMERICALLY)

Because the "crystal ⇒ IPR ~ O(1)" side is a postulate (chem C4.1) and IPR is kernel-observable, I ran the same smoothed-kernel measurement on synthetic zero sets (T=600, N=472, c^inf-cos ε=T/N):

| zero set | mean IPR·N | weighted IPR·N | #modes IPR ≥ 0.1 | λ_max |
|---|---|---|---|---|
| perfect lattice (extreme order) | 1.77 | 1.50 | 0 | 5.300 |
| lattice + one coincident pair (256-law "double-mark atom") | 1.83 | 1.49 | 0 | 5.301 |
| **real zeros** | **4.22** | **2.72** | **0** | **5.588** |
| Poisson (lattice + uniform jitter) | 5.45 | 4.97 | 0 | 5.344 |
| GOE bulk (empirical) | 3.00 | 3.00 | — | — |

**Three honest consequences:**
1. The smoothed-kernel IPR **does discriminate zero-set order**: lattice (1.77) < real (4.22) < poisson (5.45), each distinct beyond noise. The real zeros sit between perfect order and pure disorder — consistent with GUE-type repulsion, i.e. the delocalized phase.
2. But **every** configuration — including the maximally-ordered lattice and the crystal's own signature defect — lands in the O(1)-delocalized class. No zero set produces IPR ~ O(1) through the paper kernel. The C4.1 "crystal ⇒ localized eigenvectors" signature is **unreachable through the actual certificate kernel**, so IPR cannot *certify* "realized world near the crystal" — that reading of the diagnostic is empirically vacuous as posed.
3. The hard-cos (C⁰) kernel *does* produce localized modes, which shows where the "crystal-like" signature can live — but it is the idealized model, not the paper's φ_T.

## 6. Interpretation — what the IPR profile says about the 0.68185 ceiling (CONJECTURED)

- **CHECKED NUMERICALLY:** the realized W_T (paper-realistic kernel) has GOE-class delocalized eigenvectors (IPR·N ∈ [2.2, 4.2] ≈ 3), **zero** delta-like modes at every T ∈ {200, 400, 600}, no mobility edge, λ_max ≈ 5.4–5.6, effective rank ≈ 0.52N. It is nothing like any configuration that could attain the extremal bound: real-data bound/N = 2·trW/N − ‖W‖²_HS/N is **0.71 (hard-cos) and −1.8 (paper kernel)** vs the extremal-world value 2 − 1/c₁ = 0.6725 and the PairCeiling 0.68185.
- **CONJECTURED (direction per task + C4.1):** the realized world is spectrally *delocalized*, i.e. far from the crystal in the sense C4.1 intended — the extremal law is NOT what nature realizes, so the 0.68185 ceiling (an extremal-world/in-class statement, vector #25 DEAD for beating it in-class) is **far from tight in the realized world**: there is realized-world slack. Consistent with the C6 framing that reality sits deep in the delocalized phase (all first 1000 zeros simple).
- **CONJECTURED (caveat that constrains the redirect):** the IPR observable specifically is a *weak* probe of crystal proximity — section 5 shows no configuration produces the O(1) signature through the paper kernel. The robust, configuration-independent slack statements are the spectral facts (λ_max ≈ 5.4–5.6, eff. rank ≈ 0.52N, negative real-data bound/N) plus the *absence* of defect/localized modes, not the IPR magnitude itself.
- **What this does NOT say:** it does not say the ceiling can be beaten by a certificate of the same class (that is proven DEAD — vector #25). "Slack in the realized world" means the real W_T has room relative to the extremal law — harvesting it requires new certificate inputs (multiplicity/moment structure, statistical certificates — vectors #1/#2/#4 style targets), not a better window.
- **Open follow-ups:** (i) the near-rank-deficiency (eff. rank ≈ 0.52N) is the [AF] finding now quantified — worth understanding whether it is a kernel-width effect (ε = T/N) or zero-set structure; (ii) the mean IPR·N creep 2.2 → 4.2 with T is inside the delocalized phase and needs T ≫ 600 (data-limited: 1000 zeros) to extrapolate; (iii) hard-cos's localized top modes (λ ≈ 2) are a C⁰ artifact worth one sentence in any future idealized-model analysis.

## 7. Verdict (honest)

**The realized world's certificate Gram matrix is delocalized, GOE-class, with zero localized modes, no mobility edge, and no crystal-defect structure at IPR resolution (T = 200, 400, 600).** Under the task's mapping (delocalized ⇒ the realized world is far from the extremal law ⇒ the 0.68185 ceiling is not tight in the realized world — real slack exists), the measurement supports **delocalized / redirect**: the realized spectrum has room, and new-target certificates are where any of it could be harvested. The honest caveat: IPR is a kernel-observable and a weak crystal-proximity probe (controls, §5); the strongest realized-world-slack statements from this measurement are the spectrum-level facts (λ_max ≈ 5.4–5.6, eff. rank ≈ 0.52N, bound/N = −1.8 ≪ 0.6725) and the total absence of localized/defect modes.

## 8. Code and reproducibility (every number cites its script)

All code lives in **scratch/ipr/** (the task's designated location; tools/finitet is owned by another agent and was copied, not edited).

- **Matrix construction** (Rust, musl): `scratch/ipr/src/main.rs` (real zeros + lattice/poisson controls), `scratch/ipr/src/control2.rs` (coincident-pair defect control), kernel library `scratch/ipr/src/finitet_kernel.rs` (copied from tools/finitet/src/bin_cinf.rs, main() stripped).
  - Build: `export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld" && cargo build --release --target x86_64-unknown-linux-musl`
  - Run: `./target/x86_64-unknown-linux-musl/release/ipr` → `run_output_ipr.txt` (cross-checks trW/N, HS2/N, bound/N vs run_output_cinf.txt — exact match); `./target/x86_64-unknown-linux-musl/release/control2` → dumps the pair-defect matrix.
  - Outputs: `scratch/ipr/data/W_T{T}_{hard,cinf,sqrt}.txt` (T = 200, 400, 600) and `W_T600_{lattice,poisson,pair}_cinf.txt`.
- **Eigenanalysis + IPR + tables** (numpy): `scratch/ipr/ipr_analysis.py` (spectra, IPR, mobility-edge bins, localized fractions, GOE reference), `scratch/ipr/analyze_controls.py`, `scratch/ipr/analyze_pair.py`, `scratch/ipr/supplement.py` (weighted IPR).
  - Run: `uv run --quiet --with numpy python ipr_analysis.py` → `run_output_ipr_py.txt`; same for the control scripts.
- **Authoritative numbers in this note:** Tables 1–4 from run_output_ipr_py.txt + run_output_controls.txt + run_output_pair.txt + run_output_supp.txt; λ_max cross-checked between numpy eigh and the Rust power iteration (5.393/5.530/5.588 vs 5.394/5.535/5.597 — the earlier run_output_ipr.txt power-iteration bug was fixed; matrices were never affected).

## 9. Cross-references

- attack-vector-catalog-3.md §3 vector #6 (IPR, score 365) — this note executes it.
- idea-generator-chem.md C4.1 (IPR diagnostic), C4.3 (mobility edge), C6.1 (localized-fraction scaling), C6.2 (IPR at eigenvalue 2), Pool-6 verdict — this note measures all of them.
- attack-kernel.md (0.67250 window ceiling PROVEN; bandwidth-one PairCeiling 0.68185; the "realized-world slack" question) — the ceiling this diagnostic bears on.
- attack-finitet-cinf.md, attack-finitet.md ([AF]: near-rank-deficiency; finite-T bound/N behavior) — the negative real-data bound/N and rank-deficiency are consistent with the [AF] findings; not re-adjudicated here.
- attack-vector-catalog-3.md vector #25 (in-class ceiling tight, DEAD to beat) — the ceiling statement this note distinguishes from "tight in the realized world".
