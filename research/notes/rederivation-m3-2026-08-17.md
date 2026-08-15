# RE-DERIVATION: m₃ ≥ m₂² for the marked zero-law (independent proof)

**Agent:** re-derivation (builder). **Date:** 2026-08-17. **Model:** opencode-go/deepseek-v4-flash.
**Status:** PROVEN (Cauchy–Schwarz) + CHECKED NUMERICALLY (Rust).
**Discipline:** did NOT read `marked-moment-inequality-*`, `adversarial-m3-*`, `marked-m3-certificate-*`,
`sinc-m3-certificate-*` (note only), or any `*m3*`/`*marked-moment*` file. Read only the allowed set:
barrier-zoo note, sdp-unconditional-structure note, structural-final-verdict, `tools/sinc_m3_cert/src/main.rs`
(use-site). No contamination.

## 1. Object (from allowed sources)
Marked measure on the 256-lattice: μ = Σ_j m_j δ_{x_j}, x_j = j/256, marks m_j ∈ {1,2},
μ̂(k) = Σ_j m_j e^{−2πikj/N}, M = μ̂(0) = Σ_j m_j. Kernel K = sinc²(πBx), B=128; Ĝ = kk = (K̂*K̂)
(circular conv = DFT of K²). Pair rows (PROVEN for real zeros): E|μ̂(k)|² = c·k, k≥1.
Certificate consequence: floor S₃ ≥ max(D+P₃, (E[m₂])²), D = E[m³]/E[m].

## 2. THEOREM (my independent statement) — PROVEN
Let ν = μ/M (probability measure), T the convolution-by-G operator on L²(ν), G even real
(here G = K²). Define per configuration
  m₂ = (N/M)·Σ_k kk[k]|μ̂(k)|²   = N·M·⟨1,T1⟩_ν
  m₃ = (N²/M)·Σ_{k,l} kk[k]kk[l] μ̂(−k−l)μ̂(k)μ̂(l)  = N²·M²·‖T1‖²_ν
(Parseval on the lattice: Σ_k kk[k]|μ̂(k)|² = Σ_{ij} m_i m_j G(x_i−x_j); the cubic form equals
Σ_i m_i (G*μ)(x_i)²). Then
  m₃ − m₂² = N²M²·( ‖T1‖²_ν − ⟨1,T1⟩²_ν ) ≥ 0   by Cauchy–Schwarz, since ‖1‖_ν = 1 (ν probability).
Equality ⟺ T1 ≡ const ν-a.e. ⟺ (G*μ)(x) constant on supp μ. Extremal case: **uniform marks**
(m_j ≡ 2 ⇒ ν uniform ⇒ G*ν constant) attain equality — verified numerically (slack −1.16e-10).
Marks ∈ {1,2} enter only through ν being a probability measure and M ≥ N ≥ 1; **G needs no
positivity** (real CS). The inequality is per-configuration and scale-covariant (m → λm: m₂,m₃ → λ·).

**Firewall (what the theorem is NOT):** it is NOT about the raw mark moments. For X ∈ {1,2},
P(X=1)=p₁: E[X³]−(E[X²])² = −8+17p₁−9p₁² < 0 for p₁ < 8/9 (hand + numeric). The mean-1 variable
Y = m/E[m] does satisfy E[Y³]≥(E[Y²])² in both laws ((a): 2p₁(1−p₁)/(2−p₁)⁴ ≥ 0; (b):
(1+p₁)²p₁(1−p₁)/4 ≥ 0; equality iff p₁∈{0,1}) — confirmed numerically. So the theorem's content is
the normalized-marked-measure structure, not the mark law alone.

## 3. CONVENTION VERDICT (load-bearing output)
The theorem is a statement about ν = μ/M and holds for **ANY** mark law on {1,2} — both
(a) P(m=1)=p₁, E[m]=2−p₁ and (b) P(m=1)=2p₁/(1+p₁), E[m]=2/(1+p₁) — since marks enter only via
ν being a probability measure. The m₂ the theorem's Jensen step E[m₃] ≥ (E[m₂])² binds is the
pair-row functional E[m₂] = (N/E[m])·[kk[0]·E|μ̂(0)|² + Σ_{k≥1} kk[k]·c·k], which is **p₁-DEPENDENT
in both (a) and (b)**. Closed form in (b) (hand-derived, matches the certificate exactly at p₁=1):
m₂(p₁) = kk[0](2−p₁) + kk[0](N−1)·2/(1+p₁) + c·C·N·(1+p₁)/2, C = Σ_{k≥1}kk[k]k = 127.4583,
kk[0] = 0.004232 ⇒ m₂(1) = 2.225 ≈ certificate's calibrated 2.22. **Hence the certificate's sinc
branch (m₂(p₁) as a function of p₁, calibrated m₂(1)=2.22) IS the theorem's legitimate object.**

The torus value E[m₂] = 2.480620 (claimed p₁-independent) **cannot be the theorem's m₂** under
either normalization: my closed form is p₁-dependent, and the certificate's own sinc m₂(p₁) ranges
≈2.22–2.30 over p₁∈[0,1], never 2.4806. Its use to declare infeasibility (floor = max(5.4419,
2.4806²) = 6.1535 > 5.44) is **outside the theorem's scope** — the theorem does not produce a
p₁-independent (E[m₂])². What 2.480620 is (kernel? prefactor? p₁-average?) is INCONCLUSIVE from
allowed sources (its definition lives in the forbidden file). Even so, the certificate does not
beat the wall in either convention: sinc branch min-p₁ = 0.7488 ⇒ κ = 0.7488 > 0.6818 (and its
own minilp at the optimum returned Infeasible — flagged as a follow-up). Verdict: the feasible
sinc branch is legitimate under the theorem; the torus-infeasibility conclusion is not supported
by the theorem as derivable from the public contract.

## 4. Numeric checks (Rust ONLY, binary output)
Probe: `tools/rederivation_m3/` (src/main.rs, ~150 lines). Build/run:
`cargo build --release --target x86_64-unknown-linux-musl --manifest-path tools/rederivation_m3/Cargo.toml`
then `./tools/rederivation_m3/target/x86_64-unknown-linux-musl/release/rederivation_m3`.
Output (verbatim, key lines):
- per-config worst slack over 6 configs, laws A and B, p₁ ∈ {0.10, 0.40, 0.6818, 0.90}:
  all **PASS**, slack ∈ [+2.2e3, +1.6e4] (m₂ ≈ 305–544, m₃ ≈ 99k–299k; huge positive margin).
- uniform marks (m_j ≡ 2): m₂ = 554.668, m₃ = 307656.902, m₃−m₂² = **−1.16e-10** [EQUALITY, extremal].
- raw mark moments: law A p₁=0.5: −1.7500 [FAIL as expected]; law B p₁=0.5: −0.6667 [FAIL as expected].
- mean-1 Y: laws A,B all p₁: E[Y³]−(E[Y²])² = +1.4e-2 … +1.5e-1 [HOLDS].
- random-position control (positions arbitrary, marks law B): worst slack **+1.08e5 [PASS]**.
- OVERALL: ALL CONFIGS PASS: m3 >= m2^2 CONFIRMED.

## 5. RH-inert control (firewall, stated plainly)
The proof uses only: ν a probability measure on a compact abelian group, G even real, Parseval —
**nothing about the critical line**. Positions enter solely as the support of ν; the probe
demonstrates the inequality with arbitrary (random) positions, so it holds identically in the
fake-Weil world (same marked-measure structure: positions = imaginary parts, marks ∈ {1,2}) and in
any RH-false model world. **m₃ ≥ m₂² is a pure measure-theoretic inequality on the marked measure's
moments; it is ZERO evidence about zeros-on-the-line or their simplicity.** A proportion/simplicity
conclusion from it requires the extra (RH-type) hypothesis that off-line zeros are all non-simple
(per the certificate's own control block). Proportion ≠ RH: stated plainly.

## 6. Labels
- Per-config m₃ ≥ m₂² with (N/M),(N²/M) normalization: **PROVEN** (Cauchy–Schwarz) + **CHECKED
  NUMERICALLY** (binary + command in §4).
- Equality ⟺ uniform marks (extremal): PROVEN (CS equality condition) + numeric −1.16e-10.
- Raw mark moments fail both laws: PROVEN by hand (−8+17p₁−9p₁²) + numeric.
- Mean-1 mark variable holds both laws: PROVEN by hand + numeric.
- Certificate sinc branch is the theorem's branch (m₂(p₁) p₁-dependent, m₂(1)=2.22): PROVEN
  (closed form reproduces certificate's m₂(1)) + numeric read of certificate binary.
- Torus E[m₂]=2.480620 identity: **INCONCLUSIVE** (definition in forbidden file; theorem's m₂ is
  p₁-dependent in both normalizations, so 2.4806 ≠ theorem's m₂ as derivable from the contract).
- Certificate minilp at optimum infeasible: CHECKED NUMERICALLY (its own output) — follow-up flag.
