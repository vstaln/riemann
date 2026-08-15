# 6D — the r(1)=0 endpoint question (last open link on the 0.673481 transfer)

**Context:** Referee 6B confirmed the record's transfer is an unconditional liminf
(liminf N_s(1/2,T)/N(T) ≥ 0.6734808616745137) with only the three unconditional inputs
(von Mangoldt, Montgomery/BGSTB24 form factor on [0,1], integrality). The ONE open link:
the certificate's r must satisfy r(1)=0 so that the j=256 (α=1) grid point — the endpoint of
Montgomery's range — contributes nothing (the stability term |r(1)||D(1)| must vanish).
6B computed the RAW verifier kernel weight w(1)=(K(1)/K0)² ≈ 0.0033 ≠ 0 for α=1.464, so
"r(1)=0" must be a property of the EFFECTIVE certificate weight, not the raw kernel.

**Coordinator's lead hypothesis:** the certificate's r is the profile autocorrelation
(v⋆v)(x) = ∫ v(s)v(s−x) ds of v(s)=cos(αs) on [−1/2,1/2], which has support [−1,1] and
vanishes EXACTLY at x=1 (convolution of compactly-supported functions at extreme shift;
verified numerically: autocorr(1)=0.0). The tawan JOINT_WINDOW_PROOF's two-trace baseline
H(v) = 2 − 1/c₁(v) with c₁(v) = (∫v)²/(∫v² + ∫∫|s−t|v(s)v(t)dsdt) uses the profile v
directly.

**Your joint (read first, in order):**
1. /home/vstaln/riemann/research/notes/wave6-brief-6D.md (this file)
2. /home/vstaln/riemann/research/external-results/tawanerguo-zeta-simple-zeros/archive/original/JOINT_WINDOW_PROOF.md (full, esp. §0–§2 profile/c₁, §6 stability, §8 trust boundary)
3. /home/vstaln/riemann/tools/verify_coboundary_floor.py (the KernelArb class + verify_floor signature — what weight w(x) the verifier actually sums)
4. /home/vstaln/riemann/scratch/lean-inclass-build/Zeta23/PairCeiling/Ceiling.lean (the certificate validity + stability inequality, what r is)

**Answer precisely:**
1. What EXACTLY is the certificate's r for the α=1.464 record: the raw squared sinc kernel
   w(x)=(K(x)/K0)² (r(1)≠0), or the profile autocorrelation (v⋆v)(x) (r(1)=0 exactly), or
   something else? Trace which object enters (a) the verifier's F_B sum, (b) the ceiling
   theorem's |r(1)||D(1)| term, (c) the tawan H(v) two-trace baseline.
2. If the record's certificate has r(1)≠0: does the transfer to ζ still hold because BGSTB24
   Thm 1 (quoted in attack-ceiling.md: "F(α) = T^(−2α)(log T + O(1)) + α + O(1/√log T)
   uniformly for 0 ≤ α ≤ 1") controls the endpoint uniformly — i.e., does the stability
   error |r(1)||D_ζ(1)| → 0 as T→∞ anyway (D_ζ(1) = C_ζ(1) − 1/2, cumulative form factor
   discrepancy)? Verify: does the cumulative C_ζ(1) → 1/2 with BGSTB24's uniformity including
   the endpoint?
3. VERDICT: (i) r(1)=0 exactly for the record certificate [then 6B's link closes], or
   (ii) r(1)≠0 but the liminf transfer holds via uniform endpoint control [link closes
   differently], or (iii) the transfer genuinely needs a fact not established [link stays
   open, state exactly what].

Honesty: PROVEN / CHECKED NUMERICALLY (binary+cmd) / CONJECTURED / INCONCLUSIVE labels;
Rust preferred for any new computation, Python only for mpmath-level; ≤3 reads then write
deliverable research/notes/wave6-refereeD-endpoint-2026-08-17.md; ≤12 turns, ≤15 tool calls;
stop at ~85% context; never weaken anything.
