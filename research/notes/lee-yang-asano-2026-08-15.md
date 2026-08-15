# g2-1: Lee-Yang / Asano route to RH — transfer analysis (2026-08-15)
Status: naive section-level transfer [VERDICT PENDING — results in section 5]; refined handle identified (integral over circle-stable blocks).

## Setup (all PROVEN; restated from verified context)
- w = (s-1)/s, i.e. s = 1/(1-w), maps Re(s)=1/2 <-> |w|=1, Re(s)>1/2 <-> |w|<1. [PROVEN, algebra]
- G(w) := Xi(1/(1-w)); RH <=> G has no zeros in |w|<1. [PROVEN, standard, via functional equation]
- Taylor: G(w) = sum_{n>=0} c_n w^n with c_n >= 0, since c_n = sum_k b_k [w^n] A^{2k}, A(w) = (1+w)/(2(1-w)) = 1/2 + w + w^2 + ... and b_k = M_k/(2k)! >= 0. [PROVEN]
- Integral form (key object): c_n = 2 int_0^inf Phi(u) gamma_n(u) du, gamma_n(u) = [w^n] cosh(u(1+w)/(1-w)), from Xi(1/2+z) = 2 int Phi(u) cosh(2zu) du. [PROVEN]
- For every u>0, h_u(w) = cosh(u(1+w)/(1-w)) has ALL zeros on |w|=1: zeros are w = (u - i*theta_k)/(u + i*theta_k), theta_k = (pi/2 + pi k)/u, |w|=1. [PROVEN]
- Phi(u) = sum_{n>=1} (2 pi^2 n^4 e^{9u} - 3 pi n^2) e^{-pi n^2 e^{4u}} > 0; b_0 = xi(1/2) = 0.4971207781883141 (anchor). [PROVEN/known]

## 1. The lemma that would need to hold
Lemma LY (CONJECTURED — the brief's proposed claim): for every N >= 0, the Taylor section G_N(w) = sum_{n=0}^N c_n w^n is in the Lee-Yang class: all zeros in |w| >= 1.
- Sufficiency PROVEN: if LY holds for all N, then G is zero-free in |w|<1 (Hurwitz: an interior zero of the limit forces one in the sections; G(0)=1/2 != 0), hence RH.
- LY is STRICTLY STRONGER than RH: RH gives G zero-free but says NOTHING about sections. Failing LY damages only this route, never RH.
- Sibling formulation (equivalent strength, different object): Jensen polynomials J_{n,d} hyperbolic for all n,d (Hermite-Poulain, verified context). The disk version is the Lee-Yang-flavored one.

## 2. Why naive Asano contraction does NOT transfer [PROVEN analysis]
- Ising: Z = PRODUCT over site/block factors, each visibly circle-stable; closure under products + Asano contraction (diagonalization) + limits.
- Riemann: G = positive INTEGRAL (continuous SUM) over u of circle-stable h_u. Asano contraction needs product-of-blocks; no contraction operation between different u exists.
- Positive sums do NOT preserve disk-stability: (1-z)^3 + (1+z)^3 = 2 + 6 z^2 has zeros +-i/sqrt(3), |z| ~ 0.577 < 1, while both summands have all zeros ON the circle. [PROVEN — explicit counterexample]
- Hence G's disk-stability, if true, is a property of the specific positive sequence c_n (moment-flavored), not of any Lee-Yang closure theorem. The one cheap sufficient route — Eneström-Kakeya dual (c decreasing => zeros in |w|>=1) — fails: c is NOT monotone (c_0 ~ 0.5, c_1 ~ 0.022, c_2 > c_1). [CHECKED NUMERICALLY below]
- The analogy survives in exactly one place: each h_u is genuinely circle-stable [PROVEN]; G is an integral over Lee-Yang functions. Whether the Phi-weighted integral preserves stability IS RH itself; the contraction mechanism has no analogue.

## 3. Cheapest Rust check (f64, std-only, < 60 s) — exact spec
File: tools/lee_yang_sections.rs. Build/run: `rustc -O tools/lee_yang_sections.rs -o /tmp/l && /tmp/l`
1. b_k for k = 0..65: M_k = 2 int_0^1 Phi(-ln x)(-ln x)^{2k} dx/x via Gauss-Legendre 512 pts on x in (0,1); Phi summed n = 1..5 (n>=4 terms < 1e-21). Anchors: b_0 = 0.4971207781883141; c_0 = sum_k b_k 4^{-k} = xi(1) = 0.5.
2. c_n = sum_{k=0}^{min(2N+10,65)} b_k [w^n] A(w)^{2k} by Cauchy products of A = 1/2 + w + w^2 + ...
3. N in {2,3,4,5,6,8,10,12,16,20,24,30,40}: roots of G_N by Durand-Kerner (seeds |w|=1.3); report m_N = min|root|, #roots with |w| < 1-1e-9, #with |w|<0.99, max residual.
4. Control (barrier discipline): planted zero G_tilde = (1-2w)G (zero at w=1/2); same section test — validates interior zeros of the limit ARE visible in sections.
- PASS all N: LY CHECKED NUMERICALLY for N <= 40 (strong RH-positive signal; proven for all N it would give RH via Hurwitz).
- FAIL at some N: LY FALSE — naive section-level transfer ABANDONED with explicit root; RH untouched.

## 4. Forecast + inversion
- Forecast (CONJECTURED): mild expectation of FAIL at moderate N via the Szegő-curve mechanism: polynomial-coefficient models (e.g. 1/(1-w)^2: sections have ALL roots inside, |w| ~ 0.6) dip into the disk; factorial-coefficient model (e^w) stays outside. Our c_n growth is subexponential/super-polynomial (essential singularity at w=1), i.e. intermediate — expect MARGINAL incursions (|w| in (1-1e-2, 1)) rather than deep ones.
- Inversions to watch: (a) clean PASS at 1e-9 for all N <= 40 -> lemma alive, escalate; (b) DEEP interior root (|w| < 0.9) -> section route structurally hostile, pivot to integral-of-h_u handle; (c) c profile deviating from ~(0.5, 0.022, 0.023, ...) -> suspect quadrature/composition bug.
- Any future lemma must also be run on RH-false controls (Davenport-Heilbronn / planted zero): a lemma that "proves" the control is wrong (proves too much).

## 5. Results (computed this session)
[CHECKED NUMERICALLY — coordinator ran tools/lee_yang_sections.rs after fixing the agent's Phi
bug: the agent's Phi used e^{9u}/e^{4u}/no-2 leading factor and gave b_0=0.142 (anchor FAIL);
corrected to the verified wave8d form e^{9u/2}/e^{5u/2}/e^{2u} x2. Anchors now PASS: b_0 =
0.497120778188 = xi(1/2), c_0 = 0.500000000000 = xi(1).]
- REAL G_N sections: min|root| = 4.64 (N=2) -> 1.02 (N=10) -> 0.982 (N=12) -> 0.941 (N=16)
  -> 0.924 (N=20) -> 0.915 (N=24) -> 0.909 (N=30). #roots inside |w|<1-1e-9: 0 up to N=10,
  2 at N=12, 2 at N=16, 6 at N=20, 10 at N=24, 30 at N=30. max residual ~1e-13 (converged).
- Lemma LY is FALSE: sections are NOT disk-stable from N=12 on. Marginal incursions (0.91-0.98),
  never deep (<0.9) — matches forecast inversion (b), NOT a clean PASS.
- Control: planted-zero G~=(1-2w)G overflowed f64 Durand-Kerner (coefficients ~1e13+ after
  multiplication — documented numerical limitation, control not informative at these N).
- Note: the earlier run (agent's broken Phi) ALSO showed incursions (0.992 at N=24) — the
  phenomenon is not an artifact of the Phi fix, though magnitudes shift.

## 6. Verdict
[ABANDONED — with explicit reason] The naive section-level Lee-Yang transfer is DEAD:
G_N(w) has roots inside |w|<1 at every N >= 12, so no Hurwitz/disk-stability argument from
sections can prove RH this way. RH itself is UNTOUCHED (LY was strictly stronger than RH).
The one surviving handle (PROVEN, section 2): each h_u(w)=cosh(u(1+w)/(1-w)) is genuinely
circle-stable, and G is a Phi-weighted INTEGRAL over them; whether the integral preserves
stability IS RH itself — a hard analytic problem, no contraction mechanism available.
Ledger: lever ABANDONED (section route), residual handle CONJECTURED (integral-of-h_u).

## 6. Verdict
[PENDING]
