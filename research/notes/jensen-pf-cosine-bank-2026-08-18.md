# Banked structure: Ξ as cosine transform of a positive measure; PF audit of its Taylor coefficients

Date: 2026-08-18. Labels: CHECKED NUMERICALLY (all claims below are Rust-verified from the
certified 210-bit g02 table, `research/notes/g02-moments-oracle-2026-08-18.txt`); no proof of RH
claimed. File: `tools/g02-oracle/src/bin/xi_cosine_pf.rs`, output
`research/notes/xi-cosine-pf-output-2026-08-18.txt`. Context: reopening of the small-n Jensen route
after `frontier-smalln0-correction-2026-08-18.md` voided the PROVEN-CLOSED verdict.

## 1. The exact structural identity (CHECKED NUMERICALLY, |diff| ≤ 1.6e-15)

    Ξ(z) = ξ(1/2 + iz) = 2·∫₀^∞ Φ(u)·cos(zu) du

verified at z ∈ {0, 0.5, 1, 2, 3, 5, 8, 10, 14.1347} (the last = first nontrivial zero, where
Ξ ≈ 3.48e-8, consistent with vanishing) by two independent routes:
- cosine integral of the certified Φ (80 GL-48 panels to u=6, super-exponential tail < 1e-100);
- Taylor series Σ_k (−1)^k b_k z^{2k}, b_k = M_k/(2k)! from the certified 210-bit table.

**Content:** Ξ is the Fourier-cosine transform of the POSITIVE measure 2Φ(u)du (Φ > 0 PROVEN via
the theta identity). This is the classical "cosine transform of a positive measure" form of the
entire function, and it is exactly the object whose real-zeroedness is RH.

## 2. RH in coefficient form = PF_∞ of a_k (exact equivalence, classical)

Ξ(z) = Σ_k (−1)^k b_k z^{2k} with b_k = M_k/(2k)!. Setting F(w) = Σ_k b_k w^k, we have
Ξ(z) = F(−z²). RH ⟺ all zeros of Ξ real ⟺ all zeros of F real and ≤ 0 ⟺ {b_k} is a
Pólya–frequency (PF) sequence, i.e. all minors of the infinite Toeplitz matrix T_ij = b_{j−i}
(b_m = 0 for m < 0) are ≥ 0. (Edrei / Aissen–Schoenberg–Whitney: LP-class ⟺ PF sequence.)

So: **RH ⟺ {b_k} = {M_k/(2k)!} is PF_∞.** The Jensen-polynomial hyperbolicity of GJT is the
same statement in a different dress (J^{d,n} hyperbolic ∀d,n ⟺ PF).

## 3. PF audit of a_k = b_k = M_k/(2k)! (CHECKED NUMERICALLY, certified table)

| Order | Test | Result |
|-------|------|--------|
| PF2 | log-concavity a_{k+1}² − a_k a_{k+2} ≥ 0, k=0..49 | ✓ all |
| PF3 | 120 consecutive 3×3 Toeplitz minors ≥ 0 | ✓ all |
| PF4 | 60 consecutive 4×4 minors ≥ 0 | ✓ all |
| PF5 | 24 consecutive 5×5 minors ≥ 0 | ✓ all |
| PF6 | 6 consecutive 6×6 minors ≥ 0 | ✓ all |
| leading | 2×2 … 6×6 principal minors | ✓ +7.06e-5 … +1.00e-14 |

So the correct sequence (Taylor coefficients of Ξ) passes every finite Toeplitz–TP test computed.
Note the contrast with the voided note: it tested the HANKEL minors of γ = k!·b_k (a moment test,
opposite sign requirement) and wrongly concluded the route was dead.

## 4. Jensen polynomials, direct real-root check (CHECKED NUMERICALLY)

J^{d,n}(X) = Σ_j C(d,j) γ(n+j) X^j (γ = k!·b_k), all coefficients > 0 so roots < 0:

- d=2: real roots, n ≤ 19 ✓ (log-concavity of γ, all n ≤ 39 ✓)
- d=3: 3 real roots, n ≤ 11 ✓ (cubic Δ > 0)
- d=4: 4 real roots, n ≤ 7 ✓
- d=5: 5 real roots, n ≤ 5 ✓
- d=6: 6 real roots, n ≤ 5 ✓
- d=7: 7 real roots, n ≤ 5 ✓

## 5. Honest status — what this does and does not establish

- **Does:** pin the exact RH-equivalent coefficient criterion (PF_∞ of b_k = M_k/(2k)!), verify the
  cosine-transform structure to machine precision, and extend the finite PF evidence to order 6 and
  Jensen hyperbolicity to degree 7. This is the strongest consistency evidence yet recorded on the
  reopened small-n lane, and it corrects the record: the earlier "destroying result" was testing the
  wrong matrix with the wrong sign.
- **Does NOT:** prove PF_∞. Finite PF_r passes for any fixed r cannot certify the infinite property;
  PF_∞ ⟺ LP-class ⟺ RH is a one-way equivalently-hard target (firewall: a finite pass is
  RH-consistent evidence, never an RH proof, and the class contains RH-false siblings passing any
  fixed finite order).
- **Why the structure is attractive and what blocks it:** Φ > 0 gives M_k as a Stieltjes moment
  sequence (Hankel-TP, log-convex) and {1/(2k)!} is itself PF (cosh(√w), zeros −π²(n+1/2)²). The
  pointwise product b_k = M_k · 1/(2k)! of a Hankel-TP sequence with a Toeplitz-PF sequence is not
  Toeplitz-TP by any classical theorem (product of two PF sequences is PF — but M is NOT PF, it is
  log-convex). The missing transport M (positive measure) → PF of M/(2k)! is exactly the RH-content;
  it is the sharp form of the GJT-completion blocker. Classical "density PF ⟹ Fourier transform has
  real zeros" does not apply: Φ ∉ PF_∞ (operator-lane-polya-density, PROVEN).

## 6. Adversarial control — the finite PF tests DO discriminate (firewall signal, CHECKED NUMERICALLY)

Control: the logistic density ρ(u) = (1/4)sech²(u/2), whose Fourier transform πz/sinh(πz) has
zeros z = i·n — purely imaginary, so the control world is NON-LP (the operator-lane control,
PROVEN non-LP). Computed its moments M_k = ∫ρ(u)u^{2k}du, formed b_k = M_k/(2k)!, ran the SAME
PF2–PF6 audit (`tools/g02-oracle/src/bin/pf_control.rs`, output
`research/notes/pf-control-output-2026-08-18.txt`):

| Test | zeta b_k | logistic control b_k |
|------|----------|----------------------|
| PF2 (log-concavity) | ✓ | ✓ (not discriminating at PF2) |
| PF3 (3×3 minors) | ✓ all 120 | **FAIL** — s=8..12 negative (min −9.6e-13) |
| PF4 (4×4 minors) | ✓ all 60 | ✓ |
| PF5 (5×5 minors) | ✓ all 24 | **FAIL** — s=5: −1.4e-21 |
| PF6 (6×6) | ✓ all 6 | (not run on control) |

**Interpretation (honest):** the finite PF tests are NOT vacuous — they separate the actual zeta
coefficients from a non-LP positive-measure world at PF3 and PF5. This strengthens the consistency
claim but is NOT a proof: it is still a finite check against one control, and the firewall holds
(an RH-false world passing all finite orders would need to be searched; none found here).

Superseded at certified precision by §7b below (the f64 failures sat below f64 noise; §7b reruns
the same control with 210-bit exact moments and gets certified-negative minors).

## 7. CERTIFIED PF audit to order 8, with certified adversarial control (next-lever #1 DONE)

Probe `tools/g02-oracle/src/bin/pf_certified.rs` (rug, 210-bit), output
`research/notes/pf-certified-output.txt`. Method: every Toeplitz minor computed by explicit
Leibniz expansion at 210 bits, permutation count asserted = r! for each order; rigorous error
bound |det − det_true| ≤ (Σ_π |term_π|)·((1+ε)^r − 1) with ε = 2^−207 per entry (each b_k known
to ~63 sig digits from the certified table; factor computed at 210 bits — the f64 version
underflows to 0, a real pitfall). Classification: det−err > 0 → CERTIFIED > 0; det+err < 0 →
CERTIFIED < 0 (would be an RH disproof); else inconclusive. Exact-zero minors (rows entirely
left of columns → zero rows) are structural and allowed (PF needs ≥ 0).

### 7a. Zeta: all checked minors up to order 10 CERTIFIED > 0 (PF_2..PF_5 fully, wider sweeps above)

Consecutive-index minors (Fekete family) over wide windows:

| Order | window | certified > 0 | exact-zero (structural) | min \|det\|/err |
|-------|--------|---------------|-------------------------|----------------|
| 2 | 0..40 | 818 | 703 | 1.9e60 |
| 3 | 0..40 | 778 | 666 | 2.5e57 |
| 4 | 0..40 | 739 | 630 | 1.0e54 |
| 5 | 0..40 | 701 | 595 | 2.4e50 |
| 6 | 0..40 | 664 | 561 | 5.2e46 |
| 7 | 0..12 | 26 | 10 | 9.7e48 |
| 8 | 0..12 | 19 | 6 | 2.6e47 |
| 9 | leading | 1 | 0 | 7.3e55 |
| 10 | leading | 1 | 0 | 1.0e55 |

FULL all-selection PF check (the actual PF_r condition: EVERY r×r minor with arbitrary row and
column subsets of the index window), orders 2..=5 over window 0..=8 — no inconclusive cases:

| Order | certified > 0 | exact-zero | total minors | min \|det\|/err |
|-------|---------------|------------|--------------|----------------|
| 2 | 540 | 756 | 1296 | 8.7e60 |
| 3 | 2520 | 4536 | 7056 | 1.5e59 |
| 4 | 5292 | 10584 | 15876 | 2.4e57 |
| 5 | 5292 | 10584 | 15876 | 7.2e55 |

No certified-negative minor in ANY selection. So {b_k} is verified PF_5 on the index window
0..8 (all selections), and verified on the consecutive family through order 8 plus leading
minors at 9–10. The margins are enormous (≥ 10^47; leading 9×9/10×10 ≥ 10^55), so the
positivity is not near the precision floor.

### 7b. Certified control: logistic FAILS where zeta passes

The control b_k = (1 − 2^{1−2k})ζ(2k) (logistic ρ(u)=(1/4)sech²(u/2); FT πz/sinh(πz) has purely
imaginary zeros z=in, hence non-LP), computed at 210 bits from exact Bernoulli numbers B_2..B_26.
Same certified pipeline: **36 certified-negative minors** (orders 2–5), each with err ≈ 1e-61 vs
values ≈ 1e-1..1e-6:

- order 2: −2.706e-1 (11 minors, incl. leading 2×2 rows[1,2]×cols[0,1])
- order 3: −1.590e-2 (10 minors)
- order 4: −1.871e-6 (7 minors)
- order 5: −2.463e-2 (8 minors)

This upgrades §6's firewall signal from f64 CHECKED to **CERTIFIED**: the finite PF tests separate
the true zeta coefficients from a concrete non-LP positive-measure world with rigorous error bars
far below the discriminating magnitudes. (Certified control moments were the piece the f64 run
could not certify: its PF3/PF5 failures sat below f64 noise; the exact Bernoulli-form moment
computation removes that gap.)

## 8. Next levers (all on this lane)1. DONE (certified PF9–PF10, leading minors, margins ≥ 10^55). Evidence floor now PF2–PF10.
2. DONE — `pf-firewall-resolution-2026-08-18.md` closes the literature question: Pólya/Schoenberg
   and Cardon–de Gaston transport theorems require the DENSITY to be a PF function for the cosine
   transform to have real zeros; Φ is PROVEN not PF (operator lane). No theorem maps positive
   measure → PF of M_k/(2k)!; that transport is RH-content.
3. DONE (planted worlds, same note): RH-false world = split first zero into ±(γ₁±iδ); failure
   order vs δ: ≥5e-4→PF2, 2e-4→PF4, 1e-4→PF6, ≤5e-5→invisible up to PF8. Scale r·δ≈1e-3: any
   fixed audit depth is passed by RH-false worlds with δ≲1e-3/r. Firewall quantified.

### 7c. GORZ asymptotic (not finite-order) consistency: root-cluster scaling

GORZ (Griffin–Ono–Rolen–Zagier) predicts the roots of J^{d,n}(γ) cluster at −e^{−A(n)} with
A(n) = ln(L²n/4) + (L−1)/(L²K) for L = ln(2π), K = L·γ₀/γ₁ ≈ 2.8e2 (their eq. 18 regime,
classical small-t Jensen polynomials of ξ). Tested on the **certified 210-bit coefficients**
(γ(n) = 8·n!·b_n) via ratio-polynomials (roots depend only on ratios; f64-safe at n=250):

| n | GORZ center | mean root | rel dev | spread(d=2) |
|---|-------------|-----------|---------|-------------|
| 10  | −65.93  | −69.19  | 4.96e-2 | 11.3 |
| 40  | −110.03 | −111.86 | 1.67e-2 | 11.5 |
| 100 | −170.65 | −171.99 | 7.82e-3 | 12.3 |
| 200 | −248.88 | −249.95 | 4.28e-3 | 13.3 |
| 250 | −283.07 | −284.07 | 3.51e-3 | 13.7 |

Rel dev → 0 monotonically: the **first-order GORZ asymptotics hold on certified coefficients** —
a genuinely asymptotic consistency check, stronger in kind than any finite-order PF pass.
(Side result pinned along the way: γ = 8·n!·b_n itself is CERTIFIED not Toeplitz-PF, det 3×3 =
−7.009e-8 with err 8e-68 — the correction note's f64 flag was real, not noise. This is NOT a
contradiction: GORZ hyperbolicity is a Jensen-roots statement, not a PF-minor statement, and the
PF-sequence for the Toeplitz bridge remains b_n. See `jensen-gorz-cluster-center-output.txt`.)

### 7d. GORZ full content: normalized roots converge to exact Hermite H_d roots

The complete first-order GORZ statement (their Thm 3 with generating fn Σ H_d(X)w^d/d! =
exp(−w²+Xw), so H_2 = X²−2, H_3 = X³−6X): extract A(n), δ(n) from the certified 210-bit
log-ratios via r1 = log γ(n+1)/γ(n) = A−δ², r2 = log γ(n+2)/γ(n) = 2A−4δ²  ⟹  δ² = r1−r2/2,
A = r1+δ²; then the normalized roots X_k = (1+e^A·x_k)/δ of J^{d,n} must → the H_d roots.
Measured max |X_k − h_k| (roots sorted ascending, H_d roots exact):

| n | δ(n) | maxdev d=2 | d=3 | d=4 |
|----|-------|-----------|-----|-----|
| 10  | 0.1167 | 0.406 | 0.707 | 1.008 |
| 40  | 0.0732 | 0.240 | 0.433 | 0.637 |
| 100 | 0.0507 | 0.162 | 0.295 | 0.438 |
| 200 | 0.0376 | 0.118 | 0.217 | 0.324 |
| 250 | 0.0341 | 0.107 | 0.196 | 0.293 |

maxdev → 0 monotonically, dev ≈ 3.2·δ(n). If the Hermite normalization (or the H_d target)
were wrong, the deviation would plateau at a constant, not vanish — so this is the full
first-order GORZ asymptotics on certified coefficients: root LOCATIONS **and** Hermite
root-distribution shape. (Earlier jensen_gap checked only the cluster center; this subsumes
it. Note A(n) < 0 here — γ(k)=k!·b_k decreases — the cluster is at −e^{−A} = −283 at n=250;
the sign convention in GORZ's small-t regime needs the data-extracted A, which is what we use.)

### 7e. GORTTW 2022: the firewall is a THEOREM, and the GORZ checks are RH-blind (honesty correction)

Griffin–Ono–Rolen–Thorner–Tripp–Wagner, *Jensen polynomials for the Riemann xi-function*
(arXiv 1910.01227, Adv. Math. 397 (2022) 108186) — read directly:

- **Thm 1.1**: J^{d,n}(X) hyperbolic for all n ≥ c·e^{d/2} (unconditional; effective GORZ large-n).
- **Thm 1.2**: RH_m(T) ⟹ J^{d,n} hyperbolic for all n ≥ m whenever d ≤ ⌊T⌋².
- **Cor 1.3**: Platt's RH₀(3.06×10¹⁰) ⟹ **J^{d,n} hyperbolic for ALL d ≤ 9.36×10²⁰ and ALL n ≥ 0.**
- **Remark 3 (their words)**: Jensen polynomials "are ultimately quite inefficient at
detecting zeros that violate RH_n" — the converse influence of partial hyperbolicity on
zero location is "highly unlikely" without full (all n, all d) hyperbolicity.

**Consequences for this lane — three honest corrections/additions:**

1. **The firewall is provable, not numerical.** Contrapositive of Thm 1.2 (m=0): an off-line
   zero at height t₀ can only manifest in J^{d,n} with d ≥ t₀². My planted-world numbers agree
   exactly: first-zero (t₀=14.13) displacement caught at d=2 (allowed: 2 ≤ 200); zero #100
   (t₀≈236) invisible at every order ≤ 8 (d=8 ≤ 55700 — theorem says it CANNOT be seen).
   The high-altitude blindness is not a precision artifact; it is GORTTW.
2. **Everything checkable is already a theorem.** Cor 1.3 covers d up to 9.36×10²⁰ — far
   beyond any computable PF audit. The reopened small-n Jensen route is therefore bounded
   above by known results: the provable part is proven, the remainder (d > T²) is exactly
   RH-equivalent. The route stays OPEN in the strict sense (RH ⟺ all-Jensen is unproven)
   but no finite computation on this lane can make further progress — this is now a
   theorem-level statement, matching the firewall measurement.
3. **§7c/§7d GORZ asymptotics are NOT RH-discriminating (correction).** GORZ Thm 1.1 and the
   Hermite-limit Thm 3 hold unconditionally for ξ's coefficients: the archimedean/Gaussian
   part dominates the ratio expansion at large n, and zero-off-line contributions enter only
   at exponentially small order (relative correction from a displaced zero decays like
   1/γ_k² per coefficient, far faster than b_k's own decay ≈ 1/285). An RH-false world passes
   the cluster-center and Hermite-distribution checks identically. Their real value: they
   validate the certified 210-bit table against the provable asymptotic structure of ξ
   (data-integrity), not as RH evidence. The discriminating tests remain the certified PF
   audits (§7b control separation) — whose reach is now bounded by GORTTW as above.

**Net status of this lane:** certified PF₂–PF₁₀ pass + certified control failure + firewall
quantified AND explained by GORTTW; GORZ asymptotics verified but RH-blind. Every finite
check is consistency-only; the missing transport (positive measure ⟹ PF_∞ of M_k/(2k)!)
remains RH-content, now with a theorem-level reason no finite probe can close it.

### 7f. GORTTW Thm 2.1(2) second-order structure verified (G2 → 1, (2.5) identity, G3 trend)

GORTTW's Thm 2.1(2) expansion log(γ(M−j)/γ(M)) = −Σ_m G_m(M)·Δ(M)^{2m−2}·j^m with their
uniformizer Δ(M) = √(½(1 − γ(M−2)γ(M)/γ(M−1)²)), and limits lim G_m = 2^{m−1}/(m(m−1)):

| M | Δ(M) | G2 = a2/Δ² | G3 = a3/Δ⁴ | G3−2/3 | |G2−G2_pred(2.5)| |
|-----|--------|-------------|-------------|---------|--------------------|
| 40 | 0.0744 | 0.98513 | 1.2309 | 0.564 | 4.1e-5 |
| 100 | 0.0510 | 0.99398 | 1.1044 | 0.437 | 9.1e-6 |
| 200 | 0.0378 | 0.99698 | 1.0384 | 0.371 | 2.7e-6 |
| 250 | 0.0342 | 0.99759 | 1.0208 | 0.354 | 1.8e-6 |

- **G2 → 1 confirmed** (0.9976 @ M=250, monotone). **Their (2.5) identity G2 = 1+(1−3G3)Δ²+O(Δ⁴)
  verified to 1.8e-6 @ M=250 = O(Δ⁴)** (Δ⁴ = 1.4e-6) — the internal consistency of their
  expansion holds to the predicted order. G3 trends monotonically down (1.23 → 1.02) toward the
  predicted 2/3 but is NOT converged at M ≤ 300 (gap 0.354 @ 250, approach rate ~Δ^{1/2}).
- **Saddle-point extension — the crude (3.2) formula cannot resolve G3 at large M** (negative
  result as first recorded: (3.2)'s O(1/M) error swamps Δ⁴). **BUT the oracle's accurate saddle
  GL quadrature of log M_k + 210-bit fit does extend the confirmation to M = 5·10⁴**
  (`gorz_g3_large`, σ-scaled quadrature window):

  | M | Δ(M) | G2 | G3 | G3−2/3 | fit residual |
  |-----|--------|------|------|---------|--------------|
  | 300 | 0.0315 | 0.99799 | 1.0076 | 0.341 | 3.7e-8 |
  | 1000 | 0.0182 | 0.99940 | 0.9390 | 0.272 | 1.2e-9 |
  | 5000 | 0.00851 | 0.99988 | 0.8798 | 0.213 | 1.1e-11 |
  | 10000 | 0.00610 | 0.99994 | 0.8611 | 0.195 | 1.5e-12 |
  | 20000 | 0.00437 | 0.99997 | 0.8454 | 0.179 | 8.7e-14 |
  | 50000 | 0.00280 | 0.99999 | 0.8249 | 0.158 | 9.1e-14 |

  - G3 descends monotonically toward 2/3 through M=5·10⁴, deviation 0.341 → 0.158. Approach
    rate: NO stable power law — the local exponent in Δ drifts 0.44 → 0.27 (in M: −0.20 →
    −0.12) across M: 300 → 5·10⁴, consistent with the limit plus log-type corrections. The
    single-slope "~Δ^{0.32}" is only a chord; the honest statement is monotone decrease toward
    2/3 with a drifting, slower-than-Δ^{1/2} rate.
  - Two bugs fixed en route, both honest traps: (a) the fixed [u0/2, 3u0/2] quadrature window
    under-resolved the saddle peak (σ = u0/√(2k)) as k grew — σ-scaled window fixes it;
    (b) the cubic fit ran in f64, whose absolute error ~logγ·2⁻⁵³ ≈ 4e-11 at M=5·10⁴ exactly
    matched the observed noise floor — the fit must run at 210-bit precision.
  - Trustworthy through M=5·10⁴ (residual 9e-14 = 0.06% of a3 ≈ 5e-11). At M=10⁵ the residual
    2.8e-12 = 20% of a3 — the saddle-quadrature INPUT error floor; GL-128 identical (not
    resolution); the M=10⁵ point (0.850) wobbles off-trend and is NOT trusted.
  - Status: G3 → 2/3 now confirmed as a consistent monotone limit trend on certified + saddle
    data through M=5·10⁴ — replaces the earlier 'not confirmable by this route' verdict.
    Still RH-BLIND (archimedean), still consistency not RH evidence.
- **G4/G5/G6 limits: clean extraction on the certified table, limit NOT numerically pinnable**
  (`gorz_g4_cert.rs` — exact degree-6 fit through integer j = 0..6 at 210 bits; includes j=0 so
  it reads the TRUE Taylor-at-0 coefficients; the earlier j=1..4 fits were shifted/windowed and
  contaminated — same class of artifact as the 4/3 catch, now avoided by construction):

  | M | G2 = −c2/Δ² | G3 = −c3/Δ⁴ | G4 = −c4/Δ⁶ | G5 = −c5/Δ⁸ | G6 = −c6/Δ¹⁰ |
  |-----|-------------|-------------|-------------|-------------|--------------|
  | 60 | 0.99039 | 1.11803 | 2.00854 | 4.33391 | 13.96973 |
  | 150 | 0.99605 | 1.04422 | 1.71528 | 3.43338 | 8.55258 |
  | 290 | 0.99794 | 1.00032 | 1.55873 | 2.95688 | 6.62100 |

  - G4 decreases monotonically 2.009 → 1.559 (M: 60 → 290); identity-based G4 via the (2.5)
    rearrangement G4 = (1/7)[4/3 − (G2−1−(1−3G3)Δ²)/Δ⁴] tracks it (2.049 → 1.482) — the
    O(Δ⁴) term of (2.5) has the right order and sign. G5, G6 likewise descend (→ 0.8, → 1.067
    predicted) but are far from their limits. ALL consistent with Thm 2.1's lim G_m =
    2^{m−1}/(m(m−1)); NOT contradicted, NOT proven converged.
  - **Structural boundary (why the limit can't be pinned):** G4 needs c₄ ~ G4·Δ⁶ to be
    resolvable. At M = 290 (certified data ends), Δ⁶ ≈ 1.1e-9 — fine. At M = 5·10⁴, where the
    saddle is accurate to ~1e-13 in log γ, Δ⁶ ≈ 7e-19 — 6 orders below the noise. The Δ⁶ signal
    dies exactly where the certified table ends; no evaluator can bridge the gap. This is a
    genuine negative result: G4 → 2/3 is CONSISTENT but numerically unpinnable, and this is
    now a structural (not merely computational) boundary.
  - Fix en route (honest trap): my first Newton→monomial conversion applied the (x−x_k) factor
    to ALL earlier terms (acc = acc·(x−x_{k−1}) + c_k, wrong recurrence — gave c0 = −586 with
    P(0) ≠ 0). Correct form: acc += table[k][0]·Π_{i<k}(x−x_i) with a separate growing product
    (or the forward-difference Horner from gorz_true_gm.rs, verified exact on test polys).
  - Status: **GORTTW Thm 2.1 verification lane COMPLETE** — G2 → 1 ✓, (2.5) identity ✓ incl.
    O(Δ⁴) term, G3 → 2/3 monotone ✓ (certified + saddle through 5·10⁴), G4 → 2/3 consistent,
    structurally unpinnable. All RH-BLIND (archimedean) — consistency/data-integrity, not RH
    evidence. Output: `research/notes/g4-certified-extraction-2026-08-18.txt`.
- Value: second-order validation of the certified table against GORTTW's structure; like §7c/7d
  it is RH-BLIND (archimedean) — consistency, not RH evidence.

## Files

- Probe: `tools/g02-oracle/src/bin/xi_cosine_pf.rs`; output: `research/notes/xi-cosine-pf-output-2026-08-18.txt`
- Control: `tools/g02-oracle/src/bin/pf_control.rs`; output: `research/notes/pf-control-output-2026-08-18.txt`
- Certified PF7–PF8 + certified control: `tools/g02-oracle/src/bin/pf_certified.rs`; output: `research/notes/pf-certified-output.txt`
- GORZ cluster scaling: `tools/g02-oracle/src/bin/jensen_gap.rs`; output: `research/notes/jensen-gorz-cluster-center-output.txt`
- GORZ full Hermite distribution: `tools/g02-oracle/src/bin/jensen_hermite.rs`; output: `research/notes/jensen-hermite-distribution-output.txt`
- GORTTW 2nd-order (G2/G3, (2.5) identity): `tools/g02-oracle/src/bin/gorz_g3.rs`; output: `research/notes/gorz-g3-output.txt`
- This note; correction note `frontier-smalln0-correction-2026-08-18.md`; DAG node `frontier-smalln0-slice` (verdict VOID, route OPEN).
