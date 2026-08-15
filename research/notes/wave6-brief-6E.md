# 6E — pin the record's explicit certificate (c₀, r) and the discrete-value identity

**Context (wave-6 so far):** 6A (algebra) PROVEN via tawan JOINT_WINDOW_PROOF §6–7, 6B
(unconditional liminf) confirmed, 6C (second machine) reproduces 0.6734808616745137 to
1e-16, 6D (endpoint) closed: the transfer survives with the certified quantity = the
**discrete value** v_discrete = c₀ + Σ_{j=1}^{256} (j/256²)·r(j/256), and r(1)=0 is NOT
needed (BGSTB24's uniformity at α=1 gives F(1,T)→1, s_256(T)→1/256). 6D's exact E(1)=
−1/(6·256²)=−2.5431315104e-6 reproduced by the coordinator, matching ceiling_law256's
coefficient 2.5431316e-6.

**The ONE remaining handoff (from 6D §Q3):** pin the record's explicit (c₀, r) and confirm
the rank–trace validity covers the full sum including j=256 — i.e., establish that the
16-digit certified constant 0.6734808616745137 IS v_discrete for an explicit certificate
(c₀, r) valid against the 256-law configuration, and that the tawan bound chain
(H−τ)/(1−B/m) computes exactly v_discrete (not a different object).

**READ FIRST (in order):**
1. /home/vstaln/riemann/research/notes/wave6-brief-6E.md
2. /home/vstaln/riemann/research/notes/wave6-synthesis-2026-08-17.md (wave-6 state)
3. /home/vstaln/riemann/research/external-results/tawanerguo-zeta-simple-zeros/archive/original/JOINT_WINDOW_PROOF.md (the chain: (6.1)→(7.1))
4. /home/vstaln/riemann/tools/verify_coboundary_floor.py (what the verifier actually certifies: F_B(g) ≥ eps — how does this map to c₀ + Σ s_j r(j/N) ≤ p₁?)
5. /home/vstaln/riemann/scratch/lean-inclass-build/Zeta23/PairCeiling/{Defs,Ceiling,Stability,CeilingLaw256}.lean (the certificate class: what (c₀,r) is, validity, the law's weights)

**Answer precisely:**
1. Reconstruct the EXPLICIT (c₀, r) whose value is 0.6734808616745137: c₀ and the function
   r on [0,1] (piecewise structure, values at knots j/256). Where does c₀ come from in the
   tawan chain (is it H_α − τ, or something else)? Where does r come from (the window
   kernel, the redistributed weight)?
2. Compute v_discrete = c₀ + Σ_{j=1}^{256} (j/256²)·r(j/256) with your explicit (c₀,r) and
   compare to 0.6734808616745137 and to the continuum v = c₀ + ∫₀¹ r(x)x dx. Which one does
   the tawan bound (H−τ)/(1−B/m) equal? 6D says the certified quantity is v_discrete; if the
   record's number is v (continuum), it must be corrected downward by ≤1e-5 — determine
   which.
3. Confirm the rank–trace validity: the inequality c₀ + Σ s_j r(j/N) ≤ p₁ must hold for the
   LAW's grid masses s_j (with j=256 included, s_256 = 256/256² = 1/256) and the transfer
   needs it for ζ's limiting masses j/256². Check the j=256 term contributes consistently on
   both sides (validity and value).
4. VERDICT: (i) record IS v_discrete (16-digit constant stands), (ii) record is continuum,
   correct to v_discrete with the ≤1e-5 shift quantified, or (iii) a genuine gap.

**Discipline:** PROVEN / CHECKED NUMERICALLY (binary+cmd) / CONJECTURED / INCONCLUSIVE;
Rust preferred for new computation (Python only for mpmath-level, one-line justification);
≤3 reads then write deliverable research/notes/wave6-refereeE-certificate-2026-08-17.md;
≤12 turns, ≤15 tool calls; stop at ~85% context; never weaken anything.
