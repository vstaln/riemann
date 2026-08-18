# agy wave-22 idea batch — adjudication with probes RUN (2026-08-18)

**Source:** one agy one-shot (gemini-3.7-flash-high) on the current open direct-RH lanes, with
today's new numbers fed in (r′ trend 0.817→0.869; 8C c_BD·√logN ≈ 0.2117; S₁ law shape). Raw:
/tmp/agy-wave22-output.txt. All five candidates were run through probes this session — three
closed, one consistency-only, one vacuous-at-low-height. No new one-way RH lemma survived.

## 1. Hardy-Beurling spectral defect closed form for c_BD — **REFUTED (probe run)**
Claim (80% conf): c_BD² = (1/2π)∫|ζ(1/2+it)|⁻²·(t²+1/4)⁻¹dt = 0.044817 (c_BD ≈ 0.21170).
**Probe result (mpmath, dps=25, certified zeta):** the partial integral does NOT converge to
0.0448 — it is dominated by 1/|ζ|² spikes at every critical-line zero (partial integral 3.10 @
T=50, 2.16 @ 200, 3.93 @ 500, 31.18 @ 1000, growing). |ζ(1/2+iγ)|=0 at real zeros ⟹ the
integrand has poles; the integral (as written) diverges and can't equal ANY finite constant.
Danger: this is the same pole-interrogation trap as the closed Gaussian-Perron lane — the
"formula" is numerology calibrated to the measured 0.2117 (45% conf claimed on the
bound; the 80% identity is dead). **Verdict: ABANDONED (probe REFUTED the identity).**
[CHECKED NUMERICALLY — partial integrals grow with cutoff.]

## 2. Conrey-Snaith shifted-moment law for S₂ — **correction constant REFUTED; limit live**
Claim (85% conf): c₂ = lim S₂/((T/2π)L⁶) = 3/40 = 0.0750 (r_∞ = 9/10), with
r′(T) = 9/10 − α₁/L + O(1/L²), α₁ = 2log2 + 1/3 ≈ 1.7196, claimed to "reproduce the measured
progression". **Probe (against my measured r′ series 0.8168/0.8447/0.8623/0.8688 at
T=150/300/600/900):** the product (0.9 − r′)·L is 0.264/0.214/0.172/0.155 — DECREASING, not
converging to α₁ ≈ 1.72. The α₁ formula is REFUTED by the measured data. The LIMIT
r_∞ = 9/10 itself remains plausible (my trend is monotone up toward ~0.9; my own conjecture
window was 0.87–0.89 vs agy's 0.90 — unseparated at T ≤ 900). c₂ = r_∞/12 = 0.075 vs my
measured a₂ = r′/12 = 0.0724 @ T=900 — same ballpark, unseparated. **Verdict: INCONCLUSIVE
(limit claim live, correction law DEAD).** Honest note: the CUE-conditioned-derivative input
(|P″|² at conditioned zero = (9/10)N²|P′|²) is the plausible mechanism, but the 1/L law as
stated does not fit any of the four points.

## 3. Speiser curvature bound Ψ ≤ C₀ — **CONSISTENCY-ONLY at finite height (probe run)**
Claim: Re(ζ′/ζ)(σ+it) + (1/2−σ)log(t/2π) ≤ C₀ ≤ 1.42 uniformly on 0<σ<1/2, giving
|ζ′(σ+it)| ≥ [(1/2−σ)L − C₀]·|ζ(σ+it)| > 0 in a strip of width 1/log t (a zero-free-STrip
mechanism for ζ′, i.e. Speiser-family). **Probe (grid σ ∈ {0.05..0.45}, t ∈ [10,1000]):
max Ψ = −0.785 (@ σ=0.05, t=200) — the bound holds BY a wide margin (C₀ ≤ 1.42 trivially
satisfied; the inequality is loose, dominated by the −(1/2−σ)L term).** Consistency-only:
the real-world data is already on the line (all known zeros on-line), so a finite-height
check cannot discriminate; and the mechanism is the ledgered 8B Speiser class (zero-free
strip for ζ′ ⟺ RH — certleft band already PROVEN standalone). The DH control demand
(off-line D′-zeros plunge Re(D′/D) to −∞) is correct but argues the bound is RH-equivalent,
not a new input. **Verdict: NOT-A-LEVER (closed class; probe trivially passes).**

## 4. Sub-prime Slepian Weil certificate (R < log 2) — **CONSISTENCY-ONLY / no new object**
Claim: with support R = 0.690 < log 2 the prime sum term vanishes identically and the
Archimedean component alone gives W(f★f) > 0, "bounding off-line excursions".
**Analysis (no compute needed):** killing the prime term by sub-prime support is a genuinely
cute trick — the explicit formula reduces to zeros-vs-Archimedean — but the resulting
positivity W(f★f) > 0 for a SPECIFIC f is exactly consistency (one test function's Weil
positivity); the certificate family must run over ALL f to touch RH, and the ledger already
closes explicit-formula/Weil-positivity as ⟺-equivalent (I=0 ⟺ RH, duplicate). The
"off-line bound" via |ĥ(γ − i(β−½))|² overshoots only if β is tuned to the window — circular.
**Verdict: ABANDONED (duplicate-class; consistency-only mechanism).**

## 5. Derivative-weighted pair correlation repulsion — **VACUOUS at low height (probe run)**
Claim (85% conf): (1/S₁)·J(T,δ) ≤ 24πc₂δ² ≈ 5.65δ², with c₂ = 0.075 (from S₂ law), via
Hadamard + CS; Q_n = |ζ′(ρ_n)ζ′(ρ_{n+1})|/S₁. **Probe (T=300, 138 zeros, central-difference
derivatives): ZERO close pairs with normalized gap < 0.3 (min gap 0.374); at T=600 one pair
@ δ=0.3 → sum Q = 4.9e-5 ≪ 0.51.** The bound holds trivially at these heights because
close pairs do not occur — no falsification possible without Odlyzko-height data (10¹²+),
which is not in the repo. The bound itself (Cauchy–Schwarz + Hadamard on adjacent zeros) is
a repulsion statement about ON-LINE pairs — it has no bearing on off-line zeros (the DH
"control" offered is again the shared-ordinate fraud: pairs at identical ordinates have
β-separation, which the normalized gap does not measure). **Verdict: INCONCLUSIVE-for-RH,
records-only, vacuous at computable height; not funded (needs 10¹²-height data).**

## Net

- 1 REFUTED by probe (C1), 1 correction-law REFUTED + limit live (C2), 1 closed-class
  consistency-only (C3), 1 duplicate-class (C4), 1 vacuous/records-only (C5).
- Best residual: NONE fundable at this height. The S₂-limit r_∞ (=c₂·12, agy: 9/10 vs mine:
  ~0.87–0.89) is the only genuinely open quantitative question raised — but it belongs to the
  zeta-moment lane, not RH; and my measured series does not fit agy's claimed 1/L law, so the
  extrapolation is unverified either way. To separate r_∞ ∈ {0.87, 0.89, 0.90} one needs
  T ≥ 3000+ (or the 1/L law fixed first — both recorded as future work).
- Firewall: nothing here is RH evidence; the wave is closed.

## Files
- agy-wave22-output.txt (/tmp), m4proper-rprime-pin-2026-08-18.md (measured series),
  /tmp/c5_probe.py, ledger update follows.