# Referee verdict — L_k(t) ≥ 0 at k=18,19,20, t=40 (and 4 control points), MPFR port

Date: 2026-08-18. Referee: hostile blind (read only the binary + first principles; did NOT read the agent's note).
Binary reviewed: `tools/wave8d/src/bin/lk_zeta_mpfr.rs`. Independent cross-checks: custom 256-bit rug probe
(`tools/wave8d/src/bin/referee_probe.rs`) with a **different derivative mechanism** (unsigned-Stirling-of-first-kind
Pochhammer differentiation vs the binary's Bell composition), its own polygamma, a **correct** |Γ| modulus, and a
finite-difference route over ln|ξ| with no derivative machinery at all.

## VERDICT: CLAIM HOLDS — CHECKED NUMERICALLY (with one real bug found that does not flip the verdict)

All 7 values are positive in the binary AND in two independent implementations. The sign-determining quantity is
`q_k = B_k² − B_{k−1}B_{k+1}` (since `L_k = Xi(t)²·q_k` and `Xi(t)² > 0` for real t off zeros; the code squares the
real part of Xi, whose Im is ~1e-40, correctly negligible). q is computed from u-derivatives built from polygamma +
zeta-log-derivatives only — **not** from the Gamma function — so q is unaffected by the Gamma bug below.

| (t,k) | binary L_k | probe L_k (correct Γ) | probe q_k | binary q (printed) | sign |
|---|---|---|---|---|---|
| (40,3)   | +1.657396e-21 | +1.657373e-21 | +3.6959285e0  | +3.695929e0  | + |
| (33.6,8) | +2.166795e-17 | +2.166753e-17 | +6.1522234e0  | +6.152223e0  | + |
| (56.5,3) | +8.869039e-32 | +8.868977e-32 | +1.1435295e3  | +1.143530e3  | + |
| (35.5,4) | +1.021881e-18 | +1.021864e-18 | +5.8646572e-1 | +5.864657e-1 | + |
| (40,18)  | +1.984181e-20 | +1.984153e-20 | +4.4246449e1  | +4.424645e1  | + |
| (40,19)  | +2.028007e-20 | +2.027979e-20 | +4.5223759e1  | +4.522376e1  | + |
| (40,20)  | +2.048938e-20 | +2.048909e-20 | +4.5690506e1  | +4.569051e1  | + |

q agrees to the binary's 7-digit print precision at all 7 points; L agrees to ~1.4e-5 relative — the residual being
exactly the |Xi|² factor (Gamma bug), see below. Third route (central differences of ln|ξ|, h & h/2 Richardson):
q_3(40) = +3.69582 (finite-difference truncation ~4e-5), u′..u⁗ match the composition route to ≤1e-5.

## What I verified in the code (line by line)

1. **The identity & the B_k convention.** L_k = (Xi^(k))² − Xi^(k−1)Xi^(k+1) = Xi²(B_k² − B_{k−1}B_{k+1}) holds with
   B_j = **complete Bell polynomial in the RAW derivatives u^(j)** (Faà di Bruno: Xi^(j)/Xi = Bell_j(u′,u″,…,u^(j))).
   The binary's `bell_series`-style recurrence (`b[j] = Σ C(j−1,m)·u[m+1]·b[j−1−m]`, raw u) is CORRECT. Note: the
   referee brief's instruction to check "B_k = u^(k)/k!, not u^(k)" is INVERTED — substituting normalized coefficients
   u^(k)/k! into the Bell polynomial would compute the WRONG quantity (that gives Taylor-coefficient Bell, whose
   square-difference is not Xi²·q). The code is right; do not "fix" it.
2. **A_n composition.** A_1 = 1/s + 1/(s−1) − ½lnπ + ½ψ(s/2) + ζ′/ζ; for n≥2: A_n = (−1)^{n−1}(n−1)![s^{−n}+(s−1)^{−n}]
   + ψ^{(n−1)}(s/2)/2^n + (d/ds)^n log ζ — signs, (−1)^{n−1} coefficient, and 1/2^n factor all match the code.
   u^(n) = i^n·A_n(½+it) rotation (n mod 4) is correct; reality check max|Im u| ≈ 1e-40 (binary) / 1e-55 (my probe).
   zeta log-derivatives use the standard recurrence L_n = (ζ^{(n)} − Σ_j C(n−1,j−1)ζ^{(n−j)}L_j)/ζ — correct.
3. **Polygamma.** Shift sum sign (−1)^{m+1}m!(z+l)^{−(m+1)} ✓; Stirling m≥1: (−1)^{m−1}(m−1)!w^{−m} + (−1)^{m−1}m!w^{−(m+1)}/2
   + Σ_k (−1)^{m−1}B_{2k}(2k+m−1)!/(2k)!·w^{−(2k+m)} ✓ (the (2k+m−1)!/(2k)! factor is present — the "missing factorial"
   bug from the f64 route is fixed); m=0: ln w − 1/(2w) − Σ B_{2k}/(2k)w^{−2k} with (−1)^k|B_{2k}|(2k−1)! coefficient ✓
   (Bernoulli sign fixed). Real-axis sanity: ψ(1/2), ψ(1), ψ′(1/2), ψ(1/4) match constants to 1e-51..1e-60.
   (I initially reproduced BOTH claimed bug classes in my own probe — signed-Stirling Pochhammer and a ψ m=0
   coefficient error — and confirmed the binary's versions are the correct ones; the "two bugs fixed" claim is true.)
4. **Certified EM remainder** is a genuine bound structure (Cauchy/EM remainder with σ→σ−δ inflation, |s+j|→|s+j|+δ,
   K=40, n=600; cross-checked n=600 vs 900 → 1e-62, 200 vs 256 bit → 1e-63).

## REAL BUG FOUND (does not flip the verdict)

`gamma_complex_stirling_mpfr` implements ln Γ(z) = (z−½)ln z − z + ½ln(2π) + Σ B_{2k}/(2k(2k−1))·z^{1−2k}, but the
loop updates p as `p *= 1/z` each step, so term k uses **z^{−k} instead of z^{−(2k−1)}** (off for all k ≥ 2).
Consequences: |Xi|² (and hence L_k = |Xi|²·q) is wrong by ~1.4e-5 relative (~3e-25 absolute for the k=18..20 values;
my correct-Γ probe L_20 = 2.0489093e-20 vs binary 2.048938e-20, ratio 1.000014). The claimed "certified error ~1e-33"
is therefore NOT a valid certified bound (the systematic series error is ~1e-25, ~9 orders above the printed err).
It does **not** touch q, does **not** touch the sign, and positivity survives by ≥5 orders of magnitude even against
the honest error. Fixing the exponent (step p by z^{−2}) is trivial.

## Secondary finding (test-expectation bug, not a computation error)

The binary prints "sign pattern: FAILED" at t=62.1 and t=66.1. This is a bug in the *expectation list*, not in the
computed Xi: two zeros (γ_13 = 59.347, γ_14 = 60.832) lie between the listed midpoints 57.9 and 62.1, so 62.1 ∈ I15
(sign +, computed + ✓) and 66.1 ∈ I16 (sign −, computed − ✓). The computed signs are correct; the alternating list
assumed consecutive intervals. Xi(0), |Xi(γ_1..4)| ~ 1e-43..1e-47, and the other 13 midpoint signs all check out.

## Independent cross-check detail (referee_probe.rs, 256-bit)

- ζ(2), ζ(1/2): match to print precision; ζ(½+40i) matches f64 em.rs to 1.6e-14.
- ψ(1/2), ψ(1), ψ′(1/2): match constants to print precision.
- u^(16..21) at t=40: −5.0766e12, −8.8412e13, −1.6360e15, −3.2053e16, −6.6289e17, −1.4431e19 — match the binary
  to ≥4 significant digits.
- max|Im u| ~ 1e-55 (reality of log-Xi derivatives holds).
- Central differences (independent of all derivative machinery): q_3(40) = +3.69582 > 0.

## Bottom line

The claim **holds**: L_k > 0 at all 7 stated points; no RH disproof. Caveats for the ledger: (1) the Γ-Stirling
exponent bug makes the stated "certified error ~1e-33" invalid as a certified bound (honest error ~1e-25 for the
k=18..20 values; still ≪ signal), and (2) "sign pattern: FAILED" is an expectation-list bug, not a computation error.
Neither affects the positivity verdict. Label: CHECKED NUMERICALLY (two independent 256-bit implementations + a
finite-difference route agree on q and on positivity).
