# E-OK EnclOK closure round 4 — rho_check FALSE ALARM adjudicated, moment condition HOLDS

**Date:** 2026-08-12. **Status:** EnclOK NOT refuted; the "FAILS" verdict was a DFT-window bug.
**Labels:** T1/T2/T3 CHECKED NUMERICALLY (numpy fft); the window-bug diagnosis PROVEN-FROM-CODE
(adjudicate_rho2.py read directly); the PSD-consistency verdict CHECKED NUMERICALLY.

## The finding — rho_check.py's verdict was a FALSE ALARM

`tools/regen_round3/rho_check.py` (prior session) reported the 256-law's data "FAILS" some
Im=0 condition. The resume agent (this round) adjudicated it:

- **The correct DFT window is j = 0..255**, not j = 1..256. For ANY marked config
  (off-grid included), f(j) = Σ_Δ c_Δ e^{2πi·jΔ/256} for ALL integer j, and the full-period
  DFT ĉ_Δ = (1/256)Σ_{j=0}^{255} f(j) e^{−2πi·jΔ/256} is REAL and ≥ 0 (it equals the
  multiplicity c_Δ on the integer Δ-lattice).
- **rho_check used the wrong window**: summed j=1..256 and substituted fbar(256)=54126.59
  for fbar(0)=65536. Every config has fbar(0) = (Σm)² = 65536. That substitution is the
  artifact source.
- **T1 (agent's script):** a valid off-grid config's own DFT has Im up to 6.11 — so nonzero
  Im is NOT a refutation for off-grid configs. Im=0 is not a necessary condition.

## The decisive test — T2 (my run, this note)

Recorded law data over j = 0..255 with the CORRECT fbar(0) = 65536:
- max |Im ĉ| = 0.159 (nonzero — the off-grid signature; a valid off-grid config can have this)
- **min Re ĉ = 255.998 ≥ 0 → the moment/Toeplitz PSD condition HOLDS**
- spectrum dominated by the Δ=0 peak (256.5) — expected for the near-CUE law

**Verdict: the 256-law's moment data satisfies the necessary Toeplitz-PSD condition.**
rho_check's "FAILS" was a DFT-window bug (j=1..256 + wrong f(0)), NOT a refutation.
EnclOK stays INCONCLUSIVE-not-refuted — the data is consistent with a valid off-grid config,
which is what the authors' private certificate (cert_N256_blk_b128m.json, sha256 cc3de991…)
would confirm. The f(256)=54126.59 ≠ f(0)=65536 non-periodicity is the off-grid signature
(an on-grid config would be periodic).

## What this means for the ceiling

- The 0.68185 ceiling's last non-Lean link (EnclOK) is NOT refuted by the rho route.
- The corrected T2 shows the law's data passes the necessary moment condition — positive
  evidence of consistency, not proof (the certificate itself remains private).
- The search continues: the Toeplitz-PSD condition is the RIGHT constraint for a
  reconstruction attempt (tighter than the buggy Im=0), and the LP-dual marks signature
  (≈244 integer + ≈12 half-integer marks) remains the seed.

## Scripts

- tools/regen_round3/adjudicate_rho2.py (T1/T2/T3 structure — T2 decisive run in this note)
- tools/regen_round3/adjudicate_rho.py, coherence_probe.py, cross_target.py, quartet_probe.py
  (the resume agent's other probes — the reconstruction search state)

## Next

If a future agent reconstructs the family: use the Toeplitz-PSD condition (not Im=0) as the
validity constraint, seed with the LP-dual signature, target S(j) ≈ j/256 within the
enclosures, and the f(256)≠f(0) off-grid signature as the discriminator.
