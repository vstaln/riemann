# REFUTATION: 9A "unconditional N* ≤ (1.3208+o(1))N via BGSTB24 + CGdL" — identity mismatch at step (i)

Date: 2026-08-18 (night session, hostile blind referee pass against arXiv LaTeX sources).
Status: **REFUTED-AS-UNCONDITIONAL** (remains exactly what CGdL state: RH/GRH-conditional).
Verdict replaces the earlier PROVEN-STRUCTURAL label in `wave9-9A-unconditional-Nstar-2026-08-18.md`.

## The claim that was made (9A)
Take CGdL Lemma 8's RH-part chain (Fourier inversion (8); sign-drop ĝ(x)≤0 for |x|≥1 + F≥0;
[0,1] datum (9); diagonal lower bound (10)) and replace the RH-conditional datum (9)
(F(x,T)=(T^{−2|x|}logT+|x|)(1+o(1)) uniformly |x|≤1) with BGSTB24's Theorem 1
(unconditional F(α) = T^{−2α}(logT+O(1)) + α + O(1/√logT), 0≤α≤1, F real even nonnegative).
If valid: N*(T) ≤ (1.3208+o(1))N(T) unconditionally ⟹ ≥ 67.92% simple (anywhere), a "new
unconditional theorem", first of its kind for the campaign.

## The refutation (from the primary sources, LangGraph-verified)
The transfer requires the object in BGSTB24's Theorem 1 to BE the object in CGdL's identity (8).
It is NOT. The two papers define DIFFERENT pair correlation functions:

    CGdL (LPBandZETAV_17.tex line 444):
        F(x,T) := (1/N(T)) Σ_{0<γ,γ'≤T} T^{ix(γ−γ')} w(γ−γ'),   w(u) = 4/(4+u²),
        ordinate-only (sum over ordinates, zeros with multiplicity).

    BGSTB24 (UnconditionalPC_230606.tex line 141):
        F(x,T) := Σ_{ρ,ρ', 0<γ,γ'≤T} x^{ρ−ρ'} w(ρ−ρ'),         w(u) = 4/(4−u²),
        zeros with multiplicity; the COMPLEX quantity (ρ−ρ') enters, so the real parts do.

    BGSTB24 line 143: "Note that if RH holds then F(x,T) agrees with [Montgomery's F]."

So BGSTB24's unconditional Theorem 1 is an unconditional statement about THEIR real-part-
dependent F, which reduces to Montgomery's ordinate-only F **only under RH**. CGdL's identity
(8) — Σ g((γ−γ')logT/2π)w(γ−γ') = N(T)∫ ĝ(x)F(x,T)dx — is a Fourier-inversion identity tied
to the ordinate-only F; substituting the unconditional asymptotics of the other F is not
justified. The [0,1] asymptotics of the ORDINATE-only Montgomery F remain
Goldston–Montgomery [GM87, Lemma 8], which is RH-conditional — this is exactly the open
problem GS (2026) still pose.

## Consistent authority signals (all three now read at LaTeX level)
1. BGSTB24's own application of their Theorem 1 to simple zeros (their §7) reaches
   **61.7% (simple, under the thin-box hypothesis |β−1/2|<1/(2logT))** with constants
   1.29…/0.93… ≈ 1.38–1.39 via Sech-weighted kernels — BELOW the 67.92% the transfer claims
   would be free with NO hypothesis. Logically impossible if the transfer were valid. The
   GK sech kernels and the "Re K(−i(ρ−ρ')logT) > 0 for |β−β'| < 1/logT" strip-positivity
   condition (Lemma 6(c)) are the unconditional price: kernels must be positive on a
   vertical strip to survive the complex argument ρ−ρ', which forces sech-type weights and
   degrades the constants from Montgomery's classical 4/3/Fejér (RH) to 1.39 (unconditional).
2. BGSTB24 Remark (after Theorem 2): "The pair correlation method developed in this paper
   neither requires nor provides any information as to whether or not the nontrivial zeros
   of ζ(s) satisfy β = 1/2." — i.e., their strip machinery deliberately avoids the real
   parts; it does NOT reduce to Montgomery's on-line framework unconditionally.
3. GS 2511.20059 (Feb 2026, AFTER BGSTB24): "if RH could be removed from Montgomery's
   simple zero proof, then this would also give a proof that 2/3 of the zeros are simple
   and on the critical line" — present/future conditional, i.e., the field's state is that
   this has NOT been done. A valid CGdL×BGSTB24 transfer would have settled it in 2024.

## What does survive (corrected)
- CGdL's N* ≤ 1.3208N (simple ≥ 67.92%, anywhere) stands **under RH** as published;
  ~Z (GRH) gives 1.3155 → 68.45% as published. No change.
- BGSTB24's Theorem 1 is a genuine unconditional pair-correlation theorem, but for a
  different functional; their thin-box conditional 61.7% simple is their best from it.
- GS Theorem 2 (NEW, 2026): IF the diagonal pair count (5.2) Σ_{γ=γ'}1 ≤ (C+o(1))N with
  C<2, THEN ≥ 2−C simple AND ≥ 2−C on the critical line. This is a genuinely new structural
  bridge (diagonal-count ⟹ simple+critical). **Open**: any unconditional diagonal bound
  with C<2. The campaign's 0.673481 simple-on-line / 0.836740 distinct-on-line are of
  exactly the strength 2−C ≈ 0.6735 would give, i.e., the campaign's records are strong
  evidence the diagonal C is ≤ 1.3265 — but nothing unconditional below 2 is known.
- The campaign's redistribution-chain records are UNAFFECTED (different machinery:
  H(α)/(1−B/m) redistribution on on-line zeros; no pair-correlation diagonal count).

## Ledger statement
9A (sdp-paircorr-transfer): **CLOSED-REFUTED** at the identification step (BGSTB24 F ≠
CGdL F unless RH). No new unconditional theorem; no record movement; no RH evidence.
The transfer idea is CONJECTURED-STRUCTURALLY-INVALID as unconditional; it remains an
equivalent restatement of Goldston–Montgomery's conditional datum.

## Lessons
- The wave-9 synthesis labeled the chain PROVEN-STRUCTURAL after verifying step (9) against
  BGSTB24's Theorem 1 — but never checked that the F in BGSTB24's Theorem 1 is the SAME F
  appearing in CGdL's (8). The hostile-referee pass against the primary LaTeX of ALL THREE
  papers (CGdL, BGSTB24, GS) caught it. Verdict labels must include object-identity checks,
  not just "this asymptotic exists somewhere unconditionally".
- 61.7% < 67.92% under a hypothesis weaker than RH is the cleanest internal contradiction
  (BGSTB24's own §7 would have been subsumed). That alone should have halted the claim.