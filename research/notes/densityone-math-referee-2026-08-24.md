# Hostile math referee — density-one theorem (zeta zeros), static reading
Date: 2026-08-24. Agent: diagnose (read-only).
Target: /home/vstaln/.cache/checkouts/github.com/JoshuaHKU/zeta-density-one-reproduction/paper.tex (4727 lines).
Claim under attack: Theorem t:dens1 — lim N_0^s/N = lim N_d/N = 1, "unconditional", ineffective constants,
via (i) trace-moment tower of Gabor-compressed Weil matrix determinate at (b!)^2 growth (Stieltjes-Carleman),
(ii) limiting spectral measure ν has no atom at zero (exact finite-N log law), (iii) Christoffel values λ_k(0) ↓ 0
(Akhiezer), (iv) sup_k(1 - 2λ_k(0)) = 1. Arithmetic inputs claimed: Montgomery band-limited pair correlation,
Siegel-Walfisz, MRT; ineffective constants.

METHOD NOTE: static reading only, no computation. I verified the DEDUCTIVE structure of each consumed step
against what the text actually cites/proves. The layer-(b) analytic theorems (transport, ledgers) are
unverifiable by reading; I record them as residual risk, not as verified.

============================================================================
SURFACE 1 — Montgomery band-limited pair correlation: SOUND_AS_WRITTEN
============================================================================
What the tower actually consumes from Montgomery: only the first two moments, and only the
UPPER-BOUND direction on the even moment m_2 ≤ 4/3.

Evidence:
- Provenance (lines ~3893-3902): "Montgomery's theorem feeds only the first two moments. Every higher
  moment is a separate, separately proved, unconditional arithmetic input: through the explicit formula
  and the cell ledger it becomes a higher-order autocorrelation sum of Λ ... closed by the Siegel--Walfisz
  theorem and Vaughan's estimate at moduli up to (log X)^B (Theorem t:D, Theorem t:winfty, Lemma l:pure)."
- Two-moment barrier acknowledged and quantified (lines ~3886-3893): "pair-correlation information with
  Fourier support in (-1,1) famously cannot, by itself, push proportions past well-known ceilings --- and
  this paper agrees, having quantified its own instance (0.68185 for any certificate consuming bandwidth-one
  data alone ...). The resolution is that the tower never widens the band: it climbs in k."
- Direction check via the sign lemma (Lemma l:christoffel, ~line 2910): "(Q*)^2 = Σ y_j x^j has sign(y_j)=(-1)^j:
  the certificate always consumes odd moments from below and even moments from above --- exactly the one-sided
  data the ledgers deliver, with zero premium at every degree."  Even moments from above ⇒ m_2 enters the
  certificate as m_2 ≤ 4/3. That is Montgomery's UNCONDITIONAL direction (limsup of averaged pair correlation
  ≤ GUE value at bandwidth ≤ 1); the RH-dependent direction (liminf / equality) is never consumed.
- The λ=1,k=2 corner is 2/3 and the paper's own ceiling theorem for bandwidth-one-only certificates
  (0.68185, Rem. 1.1 of C26 quoted in intro) is consistent with an unconditional reading.

Residual risk (not a logical gap): the strict "two-sided" convergence m_2(T) → 4/3 claimed for the
framework is C26-layer; the certificate only needs m_2 ≤ 4/3 in the limit, which is the standard
unconditional Montgomery content.

============================================================================
SURFACE 2 — Determinacy ⇒ existence of ν: SOUND_AS_WRITTEN (no smuggling)
============================================================================
Concern: Carleman gives uniqueness GIVEN existence; is existence (weak limit) assumed?
Resolution in text: existence is DERIVED, not assumed. Proposition p:det (~line 3257):
- tightness: "The measures ν_N are tight (m_1(N) = 1 exactly)" — Markov: ν_N([M,∞)) ≤ m_1(N)/M = 1/M, uniform in N.
- fixed-b uniform integrability: "for every b the family x^b is uniformly ν_N-integrable (m_{b+1}(N) ≤ ((b+1)!)^2
  uniformly)" — Markov with x^{b+1} at fixed b.
- moment convergence at fixed b: "by Lemma l:transfer every moment converges, m_b(N) → m_b".
- conclusion: "every subsequential weak limit of (ν_N) has moments (m_b) and by determinacy equals the same
  measure ν: the full sequence converges."
This is Helly selection + Carleman uniqueness forcing all subsequential limits equal. Legitimate. The
Carleman divergence Σ_b m_b^{-1/2b} ≥ Σ e/b = ∞ uses only the UPPER bound m_b ≤ (b!)^2 (Lemma l:growth), which
for the limit moments follows from the arithmetic moments' convergence (and arithmetically is trivially
available from uniform boundedness of the spectrum of the compression). No circularity: Carleman is consumed
for uniqueness, tightness supplies existence.

Minor notes (not gaps): (i) Lemma l:growth's PROOF is model-side (determinantal cumulants, kernel chains,
lattice box counts "lying in [0,N]"); for the arithmetic m_b(N) the (b!)^2 bound is trivially implied by
spectrum boundedness, so the direction is safe; (ii) the convergence m_b(N) → m_b at each fixed b is the
schema's arithmetic content (see Weakest Link).

============================================================================
SURFACE 3 — No-atom-at-zero log law: SOUND_AS_WRITTEN structurally
============================================================================
Concern: finite-N exact law vs N→∞ interchange, uniformity in N.
Resolution in text (Prop p:noatom, ~line 3277):
- exact finite-N law (§s:conv(vi), line 2053): ∫log x dν_N = H_N - 1 - log N; limit ∫log x dν = γ - 1 (line 2061).
- uniform bound: ∫log^- x dν_N = ∫log^+ x dν_N − ∫log x dν_N ≤ 1 + (1 + log N − H_N) ≤ 2 − γ
  uniformly in N (uses log^+ x ≤ x and m_1(N) = 1; H_N − log N ↓ γ). Arithmetic checks out.
- Portmanteau in the CORRECT direction: "log^- is nonnegative and lower semicontinuous ... so by the
  Portmanteau theorem and Prop p:det, ∫log^- x dν ≤ liminf_N ∫log^- x dν_N ≤ 2 − γ < ∞. An atom at 0 would
  make the integral infinite."  LSC ⇒ liminf inequality; atom at 0 ⇒ ∫log^- = +∞. Sound.
Dependency: requires the exact identity (layer-(a) model claim) to hold for the SAME ν_N whose weak limit
is the arithmetic limiting measure; i.e., the model/arithmetic identification through t:schema. If the
finite-N log law were not exact, the uniform bound could fail at intermediate scales.

============================================================================
SURFACE 4 — Density-one from tower supremum with ineffective constants: SOUND_AS_WRITTEN
============================================================================
Concern: is the k→∞ limit justified, or only each finite rung?
Resolution in text: the step is a COUNTABLE SUPREMUM of fixed-k theorems, not an interchange.
Remark r:nounif (~line 3345): "For each fixed k, the rung liminf_T N_0^s/N ≥ 1 − 2λ_k(0) is a self-contained
finite theorem: T→∞ is taken at fixed k, and its constants may depend on k (and are ineffective) without
harm. The left-hand side is a single number independent of k; it therefore dominates every rung, i.e.
liminf_T N_0^s/N ≥ sup_k(1 − 2λ_k(0)) — a supremum over countably many true statements, not a limit
interchange, requiring no k-uniform error control."
The proof of t:dens1 (~line 3310): "By Theorem t:schema, for every k, liminf_T N_0^s/N ≥ 1 − 2λ_k(0) ... By
Lemma l:chr with Props p:det and p:noatom, sup_k(1 − 2λ_k(0)) = 1 − 2ν({0}) = 1."
λ_k(0) ↓ ν({0}) is classical for DETERMINATE problems (cited [Akh, Sim98]); monotone decrease gives
inf_k λ_k(0) = lim_k λ_k(0). Ineffective constants are genuinely harmless because each rung is a finite
theorem and the supremum contains no error term. This is the strongest part of the paper's logic.
Requirement: t:schema must hold at EVERY k (order-uniform transport), and the Christoffel value consumed at
rung k must be the limit-data value — the fixed-k passage λ_k(0; ν_N) → λ_k(0; ν) needs moment convergence
at fixed k (t:schema) plus nonsingular limit Hankel (Stieltjes condition, verified for the tower in exact
rational arithmetic, gate F-STIELTJES). Handled in text.

============================================================================
SURFACE 5 — Weil/compressed-matrix positivity: SOUND_AS_WRITTEN structurally
============================================================================
Concern: positivity of the form on test functions vs almost-sure non-vanishing of eigenvalues.
Resolution in text: the consumption is a kernel-dimension ledger, not an a.s. statement. Remark r:tight2
(~line 2940): "an m-fold zero contributes an exact (m−1)-dimensional kernel, whence distinct ≥ 1 − λ and,
since (m−1)/m ≥ 1/2, simple ≥ 1 − 2λ — the factor 2 coming from the all-double extremal." The Christoffel
value λ_k(0) bounds the mass ν({0}) = proportion of zero eigenvalues; ν({0}) = 0 forces the bad-zero
proportion to 0. The identification "zero eigenvalue ⇔ off-line or non-simple, multiplicity (m−1)" is the
C26 framework layer (Nyquist diagonal collapse, §s:recentre) — imported, unreviewed preprint, but no
internal inconsistency found.

============================================================================
WEAKEST LINK (the real risk, not in the ranked list)
============================================================================
The capstone's deductive chain is complete and sound AS WRITTEN, but EVERYTHING hangs on the
layer-(b) analytic theorem t:schema at EVERY order:
"For every b ≥ 2, in the endpoint regime, the arithmetic trace moment converges two-sidedly to the model
constant, m_b(T) → m_b, at the grade of §s:verif layer (b). Consequently, for every k ≥ 2, liminf_T N_0^s/N
≥ 1 − 2λ_k(0) ..."
This is an extraordinary unconditional claim (higher-order autocorrelation sums of Λ over b-tuples of zeros
converge to F-CYC model constants, two-sidedly, at every b), graded certified-candidate: layer (b) is
explicitly "pre-Lean, pre-review" and "the analytic layer is unformalized" (§s:verif(f)). Static reading
cannot falsify it; equally, nothing short of external review/formalization can certify it. If any order
b ≥ 3 evaluation fails (wrong constant, or one-sided in the wrong direction), the certificates at all rungs
k ≥ b/2 fail to bound the true ν({0}), and the supremum cannot be certified to equal 1 — the conclusion is
then unsupported, though the shape of the argument (supremum of fixed-k rungs) survives.

Concrete items inside the weakest link (all layer (b)/(a)-pending):
1. Fourth moment ledger (Theorem t:D, 197/60 ledger, §s:four) — layer (b).
2. Transport at general order (Theorem t:winfty at general b, ℬ; Lemma l:pure; writeouts W1-W3) — layer (b).
3. F-CYC cluster constants at every b (Lemma l:transfer + Theorem t:poly: branch-equality and parity theorems,
   Ehrhart) — layer (a)/(b); C_8's pedigree recorded as single symbolic path + model-side checks.
4. Exact finite-N log law (line 2053) — the identity ∫log x dν_N = H_N − 1 − log N must be exact at finite N.
5. Consumption identification (bad zeros ⇔ eigenvalue-0 kernel of multiplicity (m−1)) — imported C26 framework.

============================================================================
OTHER OBSERVATIONS (supporting credibility, for the record)
============================================================================
- The paper documents its own earlier unsound rung (register D6: the 0.7295/0.8647 fifth-moment-only rung was
  found unsound by its own audit and demoted) and the anti-correlated band-model accounting (D3). This is
  consistent with a genuinely adversarial self-audit.
- r:nounif and r:dens explicitly state the capstone consumes no numerical tables: "the archived moment tables
  play no role in the proof of Theorem t:dens1, only in its effective instantiated rungs." True in the text.
- The λ=1 ceiling (0.68185) and the "RH is the λ→∞ corner" map are stated honestly.

============================================================================
VERDICT
============================================================================
Per-surface: Montgomery SOUND_AS_WRITTEN | existence SOUND_AS_WRITTEN | log-law SOUND_AS_WRITTEN
(structurally) | limit/supremum SOUND_AS_WRITTEN | positivity SOUND_AS_WRITTEN (structurally).
ONE-LINE: CLAIM_STANDS — the density-one deduction (determinacy ⇒ existence via tightness, exact log law ⇒
ν({0})=0, Christoffel limit, countable supremum of fixed-k rungs with no interchange) is logically sound as
written; the true risk is entirely in the unverified layer-(b) arithmetic input t:schema (m_b(T) → m_b
two-sided at every b, unconditionally), which static reading cannot falsify and which nothing short of
external review or formalization can certify.

Weakest link (verbatim):
"For every $b\ge2$, in the endpoint regime, the arithmetic trace moment converges two-sidedly to the model constant, $m_b(T)\to m_b$, at the grade of \S\ref{s:verif} layer (b)."

============================================================================
REFINEMENTS (verified by direct reading after initial write; 2026-08-24)
============================================================================
1. Surface 3 strengthened. The exact finite-N log law is a CUE-type identity, not an assumption:
   §s:conv(vi) (~line 2041): "the Gram matrix Ĝ_N = WW*/N of the Fourier system W_{jm} = e^{imθ_j}
   (m = 0,...,N−1) at the eigenangles θ_j of a Haar-random N×N unitary, whose expected spectral moments
   reproduce the sine-model tower. Its log-determinant is exactly computable at every finite N ... Morris's
   integral ... gives E[(1/N)Σ_i log λ_i] = H_N − 1 − log N, exactly for every N", plus the exact variance
   Var = ψ'(N+1) − ψ'(2)/N. There is ALSO a quantitative no-atom route in §s:conv(vi): with Σ_2 = 1/3,
   ν([0,ε]) ≤ (1/√3 + 1 − γ)/log(1/ε) → 0 (Cauchy-Schwarz + Markov), enforced as gate F-LOGDET. Consistent
   with Prop p:noatom's Portmanteau route. Both require the arithmetic moments to converge to THIS model
   (t:schema) — reinforcing the Weakest Link.

2. Surface 5 strengthened. The bad-zero↔spectrum link is INERTIA, not a.s. eigenvalue non-vanishing.
   Prop p:inertiaA (~line 491): "an on-line zero contributes a positive 1×1 block, an off-line pair a
   hyperbolic block of signature (1,1)", giving n_+(Ã) ≤ s_1+s_2+p. Prop p:count (~line 527): "s_1 ≥
   2 n_+^θ(Ĝ) − N(I'), #Z(I') ≥ n_+^θ(Ĝ)" via Weyl's inequality + tail ‖Ẽ‖_op ≤ θ_0 ≪ lT^{λ/2−1} (λ<1).
   The Christoffel ν({0}) = 0 then forces n_+^θ ≈ #Z. Imported from C26 (Props 4.1/4.2/4.5) — unreviewed
   preprint, no internal inconsistency found.

3. Surface 1 confirmed verbatim. Prop p:mu12 (~line 569): "tr Ĝ² = 2πbL∫_T^{2T}μ² + (T/π)Σ_{n≤X}Λ(n)²/n·g(log n)
   + O(...) ... the second moment by Montgomery's prime-side evaluation of the pair-correlation second
   moment at bandwidth ≤ 1, unconditional in the band [Mon73,BGST]. Consequently, in the endpoint regime
   λ→1^−, w/L→0: μ_1→1 and μ_2→4/3." Montgomery enters ONLY here, in its unconditional band-limited form,
   consumed for the even moment from above.

4. t:k14 confirmed verbatim (~line 2793): "λ_7(0) = 352633869846878511557783511830740995191 /
   7876602339133293193971616991853147607579 = 0.04476979..., ... liminf N_0^s/N ≥ 1−2λ_7 = 0.9104604105...,
   liminf N_d/N ≥ 1−λ_7 = 0.955230205...", 8×8 Hankel PD with shift, Q_7* strictly alternating rationals.
   The rehearsal note (pre-registered window ≈0.9101/0.9551 "opened after the fact and hit") and the
   band-grade-worthlessness remark support honesty but do not bear on the capstone (which consumes no tables).
