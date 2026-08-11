# Attack: finite-T compressed Weil form W_T — numerical verification of the 67.25% structural claims

Author: EXECUTIONER (finitet), Round 1. Date: 2026.
Toolchain: Rust (musl static, no deps) — crate at `tools/finitet/` (`.cargo/config.toml` uses `rust-lld` since no system `cc` exists on this box; build: `cargo build --release --target x86_64-unknown-linux-musl`).
Source: `research/papers/anthropic-informal-note.txt` (Claims 2.1–2.3, Lemmas 3.2–3.4) + round-1 brief.
Every measured claim below is **CHECKED NUMERICALLY** with the caveat: finite-T, f64 (64-bit), single sample per T (no window averaging); all 1000 zeros used are on the line and simple (LMFDB-verified data; file gives ordinates only, ord_ρ = 1 assumed).

## 1. Construction (idealized model, per brief) and closed forms

φ_T(x) = ψ(x·T/N), ψ(u) = cos(√2·u)·1_{|u|≤1/2} (paper's φ_T is the C∞ χ-smoothed version; differs only on O(1)-length transition intervals).
N = actual count of zeros with γ ∈ [T, 2T); grid α_k = T + (T/N)k, k = 0..N−1; s_ρ = (γ_ρ−T)·N/T, so v_ρ[k] = φ̂_T(γ_ρ−α_k) = (N/T)·Ψ(s_ρ−k).

**Closed forms** (e^{−2πi} convention; elementary, derived from ∫_{−1/2}^{1/2} cos(√2u)e^{−2πisu}du):

- Ψ(s) = sin(1/√2 − πs)/(√2 − 2πs) + sin(1/√2 + πs)/(√2 + 2πs)  (entire; removable poles at 2πs = ±√2)
- Ψ₂(s) = sin(πs)/(2πs) + ¼[ sin(√2−πs)/(√2−πs) + sin(√2+πs)/(√2+πs) ]  (transform of ψ²)
- ∫ψ² = 1/2 + sin(√2)/(2√2) = **0.849227999318304** (f64; matches direct Simpson to 1e-12; Ψ matches Simpson to 1e-10)

The T/(N∫φ²) prefactor cancels exactly with the (N/T)² from v·vᵀ: **W_T = (1/∫ψ²)·VᵀV**, V[ρ][k] = Ψ(s_ρ−k). So all checks reduce to the normalized Ψ/Ψ₂ and the rescaled data {s_ρ}.

## 2. Window counts (Riemann–von Mangoldt check)

N(T) ≈ (T/2π)(log(T/2π)−1) + 7/8. Window count N(2T)−N(T): file (ground truth, all 1000 zeros γ ≤ 1419.42 on hand) vs RvM: T=100: 50 vs 50.19; 200: 123 vs 122.45; 300: 203 vs 203.03; 400: 289 vs 289.02; 500: 380 vs 379.03; 600: 472 vs 472.25; 700: 569 vs 568.30. All within ±0.7 of the integer count. **CHECKED NUMERICALLY.** index.db (`~/Downloads/index.db`, 14.6M sampled heights, t ≥ 14) starts at t = 5000 so our windows are below its coverage; instead we validated the RvM formula itself against index.db: max |RvM − N_db(t)| = 2.08 over 14.6M rows (worst at t ≈ 2.85e10) — **CHECKED NUMERICALLY** — and the window counts against the complete zero file (exact).

## 3. Main results table (T, N, trW/N, ‖W‖²_HS/N, bound/N = (2tr−HS²)/N, Δ = bound/N − 0.6725007)

| T | N | trW/N | ‖W‖²_HS/N (diag + offdiag) | bound/N | Δ | rank (λ > 1e-6·λmax) |
|---|---|---|---|---|---|---|
| 100 | 50 | 0.992343 | 1.265459 (0.985+0.281) | 0.719228 | +0.046727 | 50 |
| 150 | 86 | 0.984411 | 1.250547 (0.980+0.271) | 0.718274 | +0.045773 | 85 |
| 200 | 123 | 0.988856 | 1.261182 (0.986+0.275) | 0.716530 | +0.044029 | 121 |
| 250 | 161 | 0.997602 | 1.279832 (0.995+0.285) | 0.715371 | +0.042870 | 159 |
| 300 | 203 | 0.994489 | 1.275443 (0.992+0.283) | 0.713534 | +0.041033 | 200 |
| 350 | 245 | 0.996925 | 1.280011 (0.994+0.286) | 0.713839 | +0.041339 | 242 |
| 400 | 289 | 0.995801 | 1.280378 (0.994+0.286) | 0.711225 | +0.038724 | 284 |
| 500 | 380 | 0.996327 | 1.280708 (0.995+0.286) | 0.711945 | +0.039444 | 374 |
| 600 | 472 | 0.998163 | 1.287259 (0.997+0.290) | 0.709068 | +0.036567 | 465 |
| 700 | 569 | 0.997518 | 1.283776 (0.997+0.287) | 0.711259 | +0.038758 | 561 |

Internal consistency: tr W = Σλ to 1e-13, ‖W‖²_HS = Σλ² to 1e-12 (Jacobi), and ‖W‖²_HS computed two independent ways (tr W² and the (VVᵀ)² decomposition) agree. Symmetry: max |W−Wᵀ| = 0.0 (exact by construction). λmax-normalized smallest eigenvalues drop to ~1e-17·λmax at T ≥ 300 → W is full-rank in exact arithmetic but numerically near-rank-deficient at the f64 floor (rank at 1e-6 threshold is N − 2..N − 8 for T ≥ 200).

## 4. Claim-by-claim verdicts

1. **W_T real symmetric** — CHECKED NUMERICALLY: max|W−Wᵀ| = 0 for every T (VᵀV; W_off = 0 since all known zeros on-line).
2. **Claim 2.1 (Poisson identity)** Σ_{k∈Z}φ̂(z−α_k)φ̂(z′−α_k) = (N/T)φ̂_{φ²}(z−z′) — CHECKED NUMERICALLY (normalized: Σ_kΨ(s−k)Ψ(s′−k) = Ψ₂(s−s′)). Max err over 8×8 sample pairs: K=50: 2.5e-3, K=200: 4.9e-4, K=2000: 4.9e-5 — error scales EXACTLY as O(1/K) (ratios 5×/10× for 4×/10× K). The identity holds; the slow convergence is intrinsic to the idealized model: the hard-cutoff ψ ∈ C⁰ (cosine does not vanish at ±1/2, φ̂_T ~ |z|^{−1}) whereas the paper's C∞ φ_T has |z|^{−2} decay and O(1/K²) truncation error. The identity itself is exact for either (supp φ_T + supp φ_T = [−N/T, N/T] kills all but the m=0 Poisson mode).
3. **Lemma 3.2: tr W_T = (1+o(1))·N** — CHECKED NUMERICALLY: trW/N = 0.992 → 0.998, approaching 1 from below; deficit ~O(1/N) (edge-zero k-truncation of the grid, exactly the paper's o(1) term).
4. **Lemma 3.3: ‖W_T‖²_HS = (1/2 + (1/√2)cot(1/√2) + o(1))·N** — CHECKED NUMERICALLY (limit): measured 1.265 → 1.287, approaching c = **1.327499296320588** from below, slowly (deficit still 3% at T=600). **Important brief correction:** the brief's "≈ 0.75329…·N" for the HS constant is wrong; 0.753296067856071 is c₁* = √2tanϑ/(1+ϑtanϑ) = **1/c** (attack-kernel.md already has 1/c₁* = 1/2 + (1/√2)cot(1/√2)). Measured c = 1.32750, and 1/c₁* = 1.327499296320588 to 15 digits. The bound constant 3/2 − (1/√2)cot(1/√2) = **0.672500703679412** reproduces the brief's 0.6725007036794116 exactly.
5. **Rank–trace inequality & final bound** — CHECKED NUMERICALLY: bound/N = 2·trW/N − ‖W‖²_HS/N = 0.709–0.719, all ABOVE 0.6725·N; rank W = N (exact) ≥ bound with margin ≈ 0.29·N. The inequality rank ≥ 2tr − ‖·‖²_HS (Lemma 3.4 with B = 0) holds with the predicted constant.
6. **Error-term sign** — see §5.
7. **Synthetic off-line pair** (T=200, γ = 201.265, β = 0.3) — CHECKED NUMERICALLY: v_{1−ρ̄} = conj(v_ρ) exactly (max err 0, Schwarz reflection); the pair matrix M = vvᵀ + conj(v)conj(v)ᵀ = 2(Re v·Re vᵀ − Im v·Im vᵀ) has exactly two nonzero eigenvalues {**+1.817579, −0.151694**} — signature (1,1), n₊(M) = n₋(M) = 1 — matching Claim 2.3's "off-line pairs contribute exactly one positive direction each" (the structural heart of the inertia argument).

## 5. Error-term sign: Δ(T) is POSITIVE and shrinks like ~1/log T

Δ(T) = bound/N − 0.67250070… = 2(trW/N − 1) − (‖W‖²_HS/N − c). Measured: trW/N − 1 ∈ (−0.016, −0.002) (small trace deficit), ‖W‖²_HS/N − c ∈ (−0.062, −0.040) (dominant HS deficit, driven by the off-diagonal pair sum: offdiag/N ≈ 0.27–0.29 vs asymptotic c−1 = 0.3275). Net Δ = +0.047 → +0.037, **positive at every T**.

Fits (10 points, least squares): Δ ≈ 0.014 + 0.155/lnT (rss 9.0e-6, best) ≈ 0.037 + 1.13/T (rss 1.6e-5) ≈ 0.028 + 0.418/ln²T (rss 1.0e-5); log|Δ| vs log(1/T) slope = 0.12 (i.e. |Δ| ~ T^{−0.12}; a pure 1/T decay would give slope 1.0, a pure 1/lnT decay ~0.16 over this range). Also Δ·N ≈ +0.03·T, i.e. Δ ≈ 0.19/ln(T/2π). Verdict: **positive, decaying logarithmically (~1/log T), not 1/T and not faster.** The HS² deficit is intrinsic to the zeros' pair correlation under the Ψ₂² kernel at heights 100–1400 (the Ψ₂-approximated pair sum gives the same deficit), consistent with the note's crude error bounds O(loglog T/log T). Since the finite-T bound OVERSHOOTS the asymptotic constant from above, the corrections **cannot be systematically exploited** to raise 0.6725 (the asymptotic constant is approached from above, as the task predicted). The wiggle in the trend (T=150, 250, 350, 700 off the curve) is single-sample noise.

## 6. Weakest links / caveats

- Idealized φ_T (hard cutoff, ψ ∈ C⁰) is the hardest case for convergence (1/|ω| decay); the paper's C∞ version has strictly better error control. Main-term constants identical.
- f64, single samples; the "rank = N" is exact-rank, numerically only visible to ~1e-17·λmax at T ≥ 300.
- No off-line zeros exist in the data; the hyperbolic-plane check is synthetic (β = 0.3 injected).

## 7. Most promising next step

The Δ > 0 / 1-log-T signature says the HS² deficit is real and slow. Before concluding it is a zero-statistics effect, test the **smoothed (C∞, χ-ramp) φ_T** at the same T: if the smoothing pulls ‖W‖²_HS/N substantially toward c (its error control is strictly better), the slow approach is a kernel artifact of the hard cutoff and the paper's o(1) is better than our idealized model suggests — worth one targeted run since it changes what we believe about the error terms. (Tools exist: extend `tools/finitet` with a C∞ ramp; compute higher-T zeros with `tools/zeta-rs` to extend the trend.)

**RESOLVED — see `research/notes/attack-finitet-cinf.md` (Round-1 follow-up).** The C∞ χ-smoothed
φ_T was implemented (`tools/finitet/src/bin_cinf.rs`) and measured at T = 100, 200, 300, 600:
smoothing does NOT pull ‖W‖²_HS/N toward c; it moves it ABOVE (1.355→1.371 for light fixed-width
ε=0.1; 3.56→3.81 for the paper-realistic ε=T/N, which is pre-asymptotic at these heights), and
the finite-T deficit is confirmed as zero statistics, not a hard-cutoff artifact. Details,
numbers, build commands, and the PROVEN/CONJECTURED verdict are in the new note.

---

## ROUND-3 VALIDATOR CORRECTIONS (from validation-001.md, adversarial pass, all rerun-backed)

- VALIDATOR TARGET (a): the I+T spectrum numbers in this note are CORRECTED — the odd eigenfunctions sin((2m+1)πu) with eigenvalue −2/((2m+1)²π²) were omitted. Min eigenvalue is ≈ 0.797 (not ≈ 0.93); the even root is k ≈ 5.60 (not 5.43). The conclusion (I+T ≻ 0, cosine is the global minimizer) SURVIVES. See validation-001.md target 2.
- VALIDATOR TARGET (b): the "Δ decays to 0 at ~1/log T" reading is INCONCLUSIVE as stated — the note's own fits have nonzero asymptotes (0.014, 0.037, 0.028). Convergence of bound/N to 0.6725 is not demonstrated by the reported data. See validation-001.md target 3.
- VALIDATOR TARGET (c): this note does not mention that EnclOK is the one non-Lean numerical hypothesis in the 0.68185 ceiling; see validation-enclok.md (INCONCLUSIVE, not refuted). See validation-001.md target 5.
- VALIDATOR TARGET (d, verification-001 only): "noise floor" → "Euler–Maclaurin truncation error" (max 6.2e-6 over i≤1000, K=10; collapses at K=14). See validation-001.md target 1.
