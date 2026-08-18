# agy wave-23 batch — adjudication with probes RUN (2026-08-19)

**Source:** one agy one-shot (`agy --print`, default model, prompt `/tmp/agy-wave23-prompt.txt`,
output `/tmp/agy-wave23-output.txt`) on the corrected frontier (S₂-limit, d_N finite-N
correction, ξ-jet certificate, Weil new families, one-way separators). Four levers produced.

## Lever-by-lever verdict

1. **Lever 1 — S₂-limit saturation law** (`r′ ≤ 1 − c₁/L` with c₁∈(0.20,0.40), r∞<1).
   **INCONCLUSIVE / ALREADY-BEING-MEASURED.** Attacks open lane #1 directly (good form), but
   the proposed law `1 − r′ = c₁/L` is not what my five measured points show: the 1/L fit
   gives 1 − r′ = 0.037 + 0.462/L (both an offset AND the slope), not a pure c₁/L with the
   claimed range. The discriminating T=6000 run (0.955 vs 0.930) is the real test of the
   underlying law family; this lever adds no new object beyond what the fits already state.
   Label: CONJECTURED, superseded by measurement.

2. **Lever 2 — Δ(N) = d_N²·logN = C₀ − C₁/√logN, C₀∈(0.22,0.28).**
   **REFUTED — CHECKED NUMERICALLY (corrected basis).** Tested against the certified wave8c
   ladder + my corrected k=1..N port (which matches certified d_N exactly):
   least-squares gives **C₀≈0.040, C₁≈0.013**; Δ(N) is flat 0.045–0.048 over N=20..5000 with
   a small N=10 bump (0.0525). agy's stated C₀∈(0.22,0.28) is an order of magnitude off —
   that range belongs to d_N·√logN (≈0.213), not Δ(N) = (d_N·√logN)²; the lever confused the
   two normalizations. The claimed C₁/√logN sub-diffusive correction is NOT visible; the
   finite-N effect is a gentle bend. Control attached (Δ_B(N) ~ c·log N for planted-zero) is
   plausible but nothing here survives; do-not-re-fit. Closed.

3. **Lever 3 — Ξ-jet curvature Q(t) ≥ 0 + 3-jet ratio at zeros.**
   **REFUTED — CHECKED NUMERICALLY (probe run).** The cheap probe was run: Q(t) on
   t∈[0,50] (step 0.1, central differences h=1e-4, dps=25). **Q(Xi) < 0 at 25/501 points**
   — including t=10.0 with a clean negative (Q = −1.13e-5; components: jet term +1.53e-4,
   Gamma-term +3.6e-6, regularizer term −1.68e-4; Xi=3.8e-2, Xi′=−2.2e-2, Xi″=9.2e-3 —
   all moderate, so the negative is NOT a 1e-12-denominator artifact). The claimed
   hypothesis "Q(t) ≥ 0 for all t∈[0,∞)" is FALSE at the sample level, so the certificate
   cannot be instantiated as stated. The DH-planted control also goes negative (60/501),
   so the claimed separator (Q_Ξ≥0 vs Q_DH<0) fails on BOTH sides — my planted model may
   be crude, but the Riemann-side failure alone kills the claim. Also note the structural
   point stands: this lever never addresses the rung-2-kill/Cauchy-fatality closure; probe
   closed. Do-not-re-propose this exact Q-form.

4. **Lever 4 — spacing variance V(T) ≤ GUE envelope (0.8987 + 0.85/logT).**
   **ABANDONED as stated.** V(T) on projected on-line zeros requires missing-zero resolution
   that only exists at Odlyzko height (T ≥ 10¹²); at T≤6000 the on-line zero set IS complete
   (all our zeros are on-line by construction), so the "missing zeros" diagnostic is vacuous —
   the same blocker as wave-22 C5 pair repulsion. The RH-false control claim (V_DH > 1.62) is
   untested. Consistency-level only; do-not-fund at computable height.

## Net

- 3 closed (L2 REFUTED numerically, L4 ABANDONED, L1 superseded), L3 **probe-run and**
  **REFUTED** (Q(Xi)<0 at 25/501 points incl. clean t=10 negative; certificate form dead).
  No survivor this batch.
- Firewall: nothing RH-implying survives; L2's failure is a clean falsification of a stated
  finite-N law; L3's failure falsifies the stated Q-form at the sample level.

## L3 probe (RUN)

Q(t) = (Ξ′)² − ΞΞ″ + (1/(4t²+1))Ξ² − (1/log(t+3))·Ξ′⁴/(Ξ′²+Ξ″²+10⁻¹²) on t∈[0,50]
(step 0.1, central differences h=1e-4, dps=25). **Result: Q(Xi) < 0 at 25/501 points;**
clean negative at t=10.0 (see above). Claim's hypothesis Q≥0 false at the sample level.
Probe code: /tmp/qjet_probe.py (this session).

## Files

- prompt: /tmp/agy-wave23-prompt.txt; output: /tmp/agy-wave23-output.txt
- this note: research/notes/agy-wave23-adjudication-2026-08-18.md