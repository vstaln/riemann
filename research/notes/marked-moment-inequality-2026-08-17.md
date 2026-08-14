# Marked moment inequality m₃ ≥ m₂² — PROVEN new certificate input

**Date:** 2026-08-17. **Agent:** L2 (builder, lateral-thinking) — note written by main loop after L2 died at 103% context with only the script on disk (deliverable-first salvage). Script: `research/notes/marked-moment-inequality-2026-08-17.py`.
**Status: PROVEN (theorem) + CHECKED NUMERICALLY** (script+cmd below).

## 1. The theorem

For ANY marked Gram configuration: G a PSD kernel matrix (sinc or torus projection — both positive-definite), M = diag(marks ≥ 0), A = M^{1/2}GM^{1/2} ⪰ 0. Marked moments m_k = tr((MG)^k)/tr(M) = tr(A^k)/tr(A). Cauchy–Schwarz on (λ_i^{3/2}), (λ_i^{1/2}):
**m₃ ≥ m₂²** (per configuration). For a law: S₃(law) = E[m₃] ≥ E[m₂²] ≥ (E[m₂])² (Jensen).

This is the missing "connected part T" input L4 identified: m₃ = D + pair + T ≥ m₂² gives T ≥ m₂² − D − pair — a **proven lower bound** on the connected part, no conjecture, no T-decomposition needed.

## 2. Verification (script, all passed)

Command: `cd /home/vstaln/riemann && uv run --quiet --with numpy python3 research/notes/marked-moment-inequality-2026-08-17.py`

- Torus kernel, 20 random marked configs @ λ=1/2 and 2/3: m₃ ≥ m₂² held on ALL, min gap +0.87.
- GUE synthetic family (n=300, K=40, seeds 99 & 7, marks {1,2} at q=(1−p₀)/(1+p₀)): held per-config at EVERY p₁ ∈ {0.5..1.0}, both conventions.
- Real zeros (LMFDB, 52,800, all marks 1, sinc windowed blocks B=2000, λ=1/2): m₃ = 5.3733±0.378 ≥ m₂² = 4.9256 (gap +0.45). ✓

## 3. The key consequence — the certificate's m₃ read is convention-locked

In the certificate's OWN formal setting (torus kernel, B=129 @ λ=1/2), the pair-row reads pin
**E[m₂] = 2.480620 (p₁-INDEPENDENT)**, hence by theorem **S₃(law) ≥ 6.153476**.

- vs the m₃ read window 5+ε = **5.44**: **flat rows + m₃ ≤ 5.44 is EMPTY in the torus convention — by theorem, margin +0.71.**
- vs the pinned bottom D+3u = 5.4419: the theorem bound 6.1535 is *stronger* by +0.71.

In the sinc/point-density convention (where the real zeros are MEASURED), at p₁ ≥ 0.90: m₂² ≤ 4.88 < 5.44 — compatible; theorem does NOT exclude there.

**Interpretation:** the "5±ε" read is a **sinc-convention constant**. The torus-convention floor is 6.15. The certificate LP (torus kernel, EnclOK-style) **cannot consume the m₃ = 5 read as-is** — the reads are only jointly satisfiable in the sinc convention. Two live routes:
(a) **Reformulate the certificate LP in the continuum sinc kernel** (where m₃ = 5 is a genuine read and L4's super-law exclusion applies), or
(b) re-derive the torus-convention m₃ read (would be ≥ 6.15 — likely too weak to exclude anything).

## 4. What this resolves

- **L4's missing input: FOUND** — the T-bound exists as a theorem (m₃ ≥ m₂²), but it reveals the convention split instead of directly excluding the adversary.
- **L5's target A (tension: real zeros 5.373 < pin 5.4419): RESOLVED** — the pin D+3u is torus-convention; the real-zeros measurement is sinc-convention; they were never comparable. Once conventions align, the theorem floor (6.15 torus / 4.93 sinc) governs.
- **L5's target B (point-density 4.07 vs mass-density-1 5.55 at p₁=1): RESOLVED** — the m₂² floor depends on convention; the certificate must fix ONE convention for all reads.

## 5. Labels

- m₃ ≥ m₂² (per-config, PSD Gram): **PROVEN** (Cauchy–Schwarz; verified numerically in both kernels, 3 data sources).
- Torus-pinned E[m₂] = 2.480620 p₁-independent: **CHECKED NUMERICALLY** (script §2, exact to 4e-16; also reproduced u(p₀) = 1.162449/0.675981 matching attack-law-s3).
- S₃ ≥ (E[m₂])² = 6.1535 > 5.44 ⇒ flat rows + m₃ ≤ 5.44 empty in torus convention: **PROVEN** (theorem applied to pinned read).
- "Certificate must be reformulated in sinc convention for the m₃ read to bind": **CONJECTURED** (structural claim; the LP machinery port to continuum kernel is untested).
- Synthetic family saturates m₃ → m₂² as p₁ → 1 (gap +1.12 → +0.33 point-density): **CHECKED NUMERICALLY** — consistent with the inequality being the binding constraint near p₁=1.

**Next lever:** (a) sinc-kernel certificate LP (route (a)) — the single most valuable untested computation; or (b) prove the torus-convention m₃ read for the real zeros directly.
