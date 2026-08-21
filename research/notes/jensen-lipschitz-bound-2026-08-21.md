# Jensen Circle-Mean Lipschitz Bound: Derivation, Verification, and Verdict

**Date:** 2026-08-21
**Task:** PROVE-OR-ABANDON Lipschitz bound L <= 0.19 for Jensen circle-mean E(c, r) along line c(t) = 0.75 + i*t, r = 0.30, t in [0, 100].

---

## 1. Executive Summary & Verdict

1. **CLAIM L <= 0.19 IS ABANDONED (REFUTED):**
   - The claimed bound L <= 0.19 was a confusion between the peak function amplitude E_max = log(r / d0) = log(0.30 / 0.25) = log(1.2) = 0.182321557... and the derivative supremum.
   - The actual Lipschitz constant on the critical-line zero corpus is:
     L = sqrt(r^2 - d0^2) / r^2 = sqrt(0.0275) / 0.09 = 5 * sqrt(11) / 9 = 1.842569328...
   - The true Lipschitz constant is 9.70x larger than the claimed 0.19.

2. **EXACT ANALYTICAL DERIVATION:**
   - For an on-line zero at rho_j = 0.5 + i*gamma_j, the horizontal distance is d0 = 0.25.
   - The zero contributes to the Jensen mean E(c(t), r) when |rho_j - c(t)| < r, which corresponds to |t - gamma_j| < Delta_t_max = sqrt(r^2 - d0^2) = sqrt(0.0275) = 0.16583124...
   - Single-zero contribution: f(t) = log(r / sqrt(d0^2 + u^2)) = 0.5 * log(r^2 / (d0^2 + u^2)), where u = t - gamma_j.
   - Derivative: f'(t) = -u / (d0^2 + u^2).
   - Derivative magnitude: g(u) = |u| / (d0^2 + u^2).
   - The unconstrained peak of g(u) occurs at u* = d0 = 0.25.
   - Since Delta_t_max = 0.165831 < d0 = 0.25 (which holds because r = 0.30 < sqrt(2)*d0 = 0.35355), the peak lies outside the disk support.
   - Thus g(u) is strictly increasing on [0, Delta_t_max], and attains its exact supremum at the boundary u -> Delta_t_max^-:
     L_single = Delta_t_max / (d0^2 + Delta_t_max^2) = sqrt(r^2 - d0^2) / r^2 = 5 * sqrt(11) / 9 = 1.842569328...

3. **ZERO SPACING & DISJOINT SUPPORT IN WINDOW [0, 100]:**
   - The 29 zeros in [0, 100] have minimum ordinate spacing:
     delta_min = gamma_28 - gamma_27 = 95.870624 - 94.651344 = 1.219280...
   - The full support width of each zero bump is 2 * Delta_t_max = 0.331662...
   - Because delta_min = 1.219280 > 0.331662, the support disks for distinct zeros NEVER overlap.
   - Consequently, for any t in [0, 100], at most one zero contributes to E(t).
   - Therefore, the global Lipschitz constant on [0, 100] is exactly L = 5 * sqrt(11) / 9 = 1.842569328...

4. **UNCONDITIONAL VS CONDITIONAL STATUS:**
   - UNCONDITIONAL: An unconditional Lipschitz bound does NOT exist without a zero-free margin around Re(s) = 0.75. If an off-line zero existed at beta0 + i*t0, as beta0 -> 0.75, d0 -> 0 and |E'(t)| -> infinity (logarithmic singularity).
   - CONDITIONAL: Conditional on the verified computational fact that all 29 zeros in [0, 100] are on the critical line Re(s) = 0.5, L <= 1.842569328 is PROVEN rigorously.

---

## 2. Exact Conditional Lemma

**Lemma (Conditional Lipschitz Bound for Jensen Circle-Mean):**
Let c(t) = 0.75 + i*t and r = 0.30.
Assume the computational certificate that in the strip 0 <= Im(s) <= 100, the Riemann zeta function zeta(s) has exactly 29 zeros rho_j = 0.5 + i*gamma_j (j = 1, ..., 29) on the critical line Re(s) = 0.5 (with gamma_1 = 14.134725... and gamma_29 = 98.831194...), and no zeros with Im(s) in [0, 100] off the critical line.

Then for all t in [0, 100]:
1. The open disk B(c(t), r) contains at most one zero of zeta(s).
2. The function E(t) = sum_{|rho - c(t)| < r} log(r / |rho - c(t)|) is continuous on [0, 100] and satisfies:
   |E(t1) - E(t2)| <= L * |t1 - t2|  for all t1, t2 in [0, 100],
   where L = sqrt(r^2 - (0.75 - 0.5)^2) / r^2 = 5 * sqrt(11) / 9 = 1.842569328...

---

## 3. Rust Grid Verification

Command:
```bash
cargo run --release --bin jensen_lipschitz
```
Location: `tools/jensen_probe/src/bin/jensen_lipschitz.rs`

Numerical output (2,000,000 grid points, dt = 5.0e-5, h = 1.0e-6):
- Exact theoretical L: 1.842569328
- Measured max |E'(t)| (analytical): 1.842568241 (relative error 5.90e-7)
- Measured max secant quotient |E(t+h) - E(t)|/h: 1.842565497
- Measured max amplitude E_max: 0.182321557 (exact match to log(1.2))
- Zero count in [0, 100]: 29
- Minimum zero spacing: 1.219290 > 2 * Delta_t_max = 0.331662 (no overlap confirmed)

---

## 4. Standing Context / Lever Rule Compliance

- Lever A (Global Covering): The Lipschitz shortcut with L <= 0.19 is dead and abandoned. The corrected constant L = 1.842569... is rigorous ONLY as a computational conditional certificate on [0, 100], and does NOT provide an unconditional escape from the logarithmic singularity barrier of off-line zeros.
- Status: Closed / Resolved honestly.
