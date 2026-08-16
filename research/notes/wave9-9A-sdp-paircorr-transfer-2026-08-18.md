# WAVE 9A — SDP pair-correlation → UNCONDITIONAL transfer (completed by coordinator from preserved agent transcript + referee verification)

Date: 2026-08-18. Agent: 9A (f64a98ac) — died at 80% context inside quiet-hours guard blockage (21 tool uses, final analysis message preserved). Coordinator completed the deliverable from the preserved transcript + independent referee re-verification from source. Status: **COMPLETE** (coordinator-completed).

## VERDICT UP FRONT

**The CGdL SDP relaxed-class inequality transfers UNCONDITIONALLY to the N*/multiplicity axis (simple-anywhere, distinct-anywhere) — a live structural thread, the first genuine proportion-side find in waves.** It does NOT move the certified on-line record axes (0.673481 simple-on-line, 0.836740 distinct-on-line via (1+s)/2). Honest boundary: the transfer is structurally confirmed (referee-verified from source); the full formal writeup "N*(T) ≤ (Z_opt + o(1))N(T) unconditionally" is CONJECTURED-STRUCTURALLY, funded as a technical writeup, NOT a record movement.

## The verified structure (referee line, all from source)

CGdL (1810.08843 §3.1) derive, for Montgomery's
  F(x,T) := (1/N(T)) Σ_{0<γ,γ′≤T} T^{ix(γ−γ′)} w(γ−γ′),  w(u)=4/(4+u²),
the pair-sum identity (8): Σ g((γ−γ′)(logT)/2π)·w(γ−γ′) = N(T)∫ f̂(x)F(x,T)dx — **Fourier inversion, unconditional**.

Lemma 8 (N* ≤ Z(f)·N) uses:
  (i) the [0,1] form-factor datum (9): F(x,T) = (T^{−2|x|}log T + |x|)(1+o(1)) for |x| ≤ 1 — **RH-conditional in CGdL; UNCONDITIONAL here** via BGSTB24 Theorem 1 (baluyot-etal-2306.04799.txt lines 49–60): F(α) real, even, nonnegative, F(α) = T^{−2α}(log T + O(1)) + α + O(...) up to α = 1 with explicit error terms;
  (ii) the |x| > 1 tail drop: f̂ ≤ 0 there (SDP class) + F ≥ 0 (BGSTB24 Thm 1, nonnegativity) ⟹ tail integral ≤ 0, dropped by SIGN, no conditioning needed;
  (iii) diagonal lower bound g(0)·Σ m_ρ = N*/r(f) — trivial.
The GRH improvement (~Z(f), constant 1.3155, uses the shifted estimate (11) for 1 ≤ |x| ≤ 3/2−δ) does NOT transfer — needs GRH, explicitly out of scope.

## Sharp division (the honest boundary)

- **Transfers**: N*(T) ≤ (Z(f)+o(1))N(T) for the SDP class — i.e. unconditional lower bounds on **simple-anywhere** (≥ 2 − c) and **distinct-anywhere** zeros. CGdL optimize Z(f) to 1.3208 (RH) ⟹ ≥ 67.92% simple (anywhere) — ABOVE the campaign's anywhere claim and above Cheer–Goldston 1.3275 → 67.27%.
- **Does NOT transfer / no grip**: the **simple-ON-LINE** record 0.673481 and **distinct-ON-LINE** 0.836740 = (1+s)/2. The on-line record requires positive-in-strip kernels + rank–trace machinery, where signed SDP functions give no purchase. This axis is untouched.

## Labels

- BGSTB24 Thm 1 unconditional [0,1] datum + nonnegativity: **PROVEN** (read directly, lines 49–60).
- CGdL Lemma 8 mechaniscs (RH enters only via (9); tail by sign): **CHECKED** (read directly, §3.1).
- Unconditional N* ≤ Z_opt·N (≥67.92% simple-anywhere): **CONJECTURED-STRUCTURALLY** — the transfer is structurally sound (every conditional input identified and replaced), but the complete formal chain (A_LP class definition, the g(0) diagonal sign lemma, (8) regime, error uniformity, explicit SDP certificate) is NOT written up. Funding a writeup is a real option; it is NOT the on-line record and is NOT RH evidence (firewall: proportion ≠ RH; anywhere-axis ≠ on-line record).
- On-line records 0.673481 / 0.836740: **UNCHANGED, certified, untouched.**

## Ledger line

wave9-9A: SDP relaxed-class pair-correlation (CGdL 1810.08843) → unconditional transfer via BGSTB24 Thm 1 — STRUCTURALLY CONFIRMED for N*/anywhere axis (live thread, ≥67.92% simple-anywhere candidate, CONJECTURED-STRUCTURALLY); NO effect on on-line records (sign/kernel boundary). No disproof anywhere. closure-DAG: register 9A as OPEN-STRUCTURAL on anywhere-axis / CLOSED-on on-line-axis (edge: does NOT touch S1/logprofile/barrierzoo — different machinery).