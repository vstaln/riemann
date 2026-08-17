# Direct-RH Non-Classical Domain Search: Nonlinear PDE, Optimal Transport, Information Geometry, Discrete Integrable Systems, Coding/Entropy

**Date:** 2026-08-18  
**Status:** NONE (PROVEN universal structural obstruction across all five non-classical domains)  
**Labels:** PROVEN / CHECKED NUMERICALLY / ABANDONED (reason)  
**Firewall:** Zero proportion claims; direct-RH sufficiency search only.

---

## 0. Executive Verdict: NONE

An exhaustive evaluation across five non-classical domains:
1. Nonlinear PDE & Geometric Flows (viscosity solutions, Monge-Ampere, porous medium, Hamilton-Jacobi),
2. Optimal Transport & Wasserstein Geometry (displacement convexity, Benamou-Brenier action, Wasserstein barycenters),
3. Information Geometry & Statistical Manifolds (Fisher-Rao metric, Amari-Chentsov connections, alpha-divergence),
4. Discrete Integrable Systems (Toda lattice tau-functions, Hirota bilinear equations, discrete Painleve),
5. Algorithmic Information & Entropy (zero-gap entropy, Kolmogorov complexity, Renyi/Boltzmann entropy of spectral measures),

reveals that **NO legitimate candidate object** yields a genuine, non-equivalent, one-way sufficient condition H(zeta) => RH with a non-vacuous RH-false control.

Every proposed object in these domains collapses into one of four fatal structural traps:
- **Trap A (Modulus / Line Blindness — Proves Too Much):** The object is constructed from real-line or theta-kernel positive data (e.g. Phi(u) > 0, T(s) integral, or line energy |xi(1/2+it)|^2 dt). Because the Davenport-Heilbronn class-2 control and planted-zero worlds share these exact positive symmetries, the candidate condition holds on the RH-false control, proving too much and destroying discriminatory power.
- **Trap B (Functional-Equation / S-Dual Equivalence):** The object forces zero-confinement via symmetry or potential barriers across the critical strip. Because the functional equation xi(s) = xi(1-s) forces any off-line zero to appear in symmetric quadruples 1/2 +- delta +- i gamma, any boundary or variational barrier that is zero-free on the boundary is identically satisfied by off-line quadruples, or reduces to H <=> RH (the Balazard-Saias-Yor / explicit-formula defect equivalence).
- **Trap C (Premise Refutation on True Zeta):** The object attempts to transfer total positivity or convexity from theta-density moments to Taylor coefficients. As proved by the repository's exact arithmetic, the Taylor coefficients gamma(n) = n! M_n / (2n)! fail Hankel total positivity at the second minor (det2 = -9.19e-6 < 0), refuting the integrability/convexity premise on the true zeta function.
- **Trap D (Hypothesis Smuggling / Class 4):** The candidate condition requires an a priori zero-free half-plane or uniform lower bound on the critical line (|xi(1/2+it)| >= t^-kappa) that is strictly unprovable without already assuming RH.

---

## 1. Domain-by-Domain Analysis and Collapse Map

### 1. Optimal Transport & Wasserstein Geodesics

- **Concrete Object Definition:**  
  Let phi(v) = e^{v/4} psi(e^v) > 0 be the log-domain theta density on R. Define the probability measure mu_0(v) = (1/Z) phi(v) dv. For any sigma in (1/2, 1], define the vertical spectral measure on R:
  d mu_sigma(t) = (1/Z_sigma) |xi(sigma + it)|^2 e^{-t^2 / T^2} dt.
  Consider the quadratic Wasserstein distance W_2(mu_sigma, mu_{1/2}) or the displacement convexity of the Boltzmann entropy Ent(mu) = int rho log rho along the Wasserstein geodesic between mu_sigma and mu_{1-sigma}.
- **Attempted Implication:**  
  If d^2/ds^2 Ent(mu_s) >= 0 or W_2(mu_{1/2+delta}, mu_{1/2-delta}) = 0 for all delta in (0, 1/2), then all zeros lie on Re(s) = 1/2.
- **Why the Implication Fails / Exact Fatal Flaw:**  
  1. For vertical line measures mu_sigma, by the functional equation xi(1-s) = xi(s), the line densities satisfy |xi(1/2 - delta + it)| = |xi(1/2 + delta - it)| = |xi(1/2 + delta + it)|. Hence mu_{1/2+delta} and mu_{1/2-delta} are identical measures on R for EVERY entire function satisfying the functional equation, regardless of whether zeros are on or off the line. Thus W_2(mu_{1/2+delta}, mu_{1/2-delta}) identically equals 0 (Class 1 auto-identity).
  2. For 2D optimal transport from the zero charge distribution Delta log|xi| = 2 pi sum delta_rho to the critical line x = 1/2, the Wasserstein cost is W_p^p = sum_{rho} |beta_rho - 1/2|^p. The condition W_p = 0 is literally sum |beta - 1/2|^p = 0, which is the exact BSY/RvF defect sum (Class 2 equivalence, H <=> RH).
- **Named RH-False Control:** Davenport-Heilbronn class-2 world (s = 0.808517... + i 85.6993...). Its functional equation xi_DH(s) = xi_DH(1-s) forces mu_{1/2+delta} = mu_{1/2-delta} identically.
- **Cheapest Rust-Only Falsification Test:**  
  Pure f64 quadrature in `tools/ot_probe`: evaluate W_2(mu_{0.7}, mu_{0.3}) for Davenport-Heilbronn; confirm W_2 = 0 to 1e-15 despite certified off-line zeros at t = 85.699 and t = 114.163.

---

### 2. Nonlinear PDE & Geometric Flows

- **Concrete Object Definition:**  
  Consider the fully nonlinear Monge-Ampere equation on the critical strip S = (0,1) x R for the potential u(x,y) = log |xi(x + iy)|:
  det(D^2 u) = u_xx u_yy - (u_xy)^2.
  Alternatively, consider the 2D porous medium equation or Ricci flow on the conformal metric g = |xi(x+iy)|^2 (dx^2 + dy^2).
- **Attempted Implication:**  
  Viscosity subsolution / comparison principle forcing singularity loci (zeros where u -> -infinity) to the axis of symmetry x = 1/2.
- **Why the Implication Fails / Exact Fatal Flaw:**  
  Away from zeros of xi, u(x,y) is the real part of the analytic function log xi(z), hence u is harmonic: Delta u = u_xx + u_yy = 0.
  Therefore, u_yy = -u_xx, which forces:
  det(D^2 u) = - (u_xx)^2 - (u_xy)^2 = - |(log xi)''(z)|^2 <= 0.
  The Monge-Ampere operator is non-positive everywhere off the zero set, completely independent of zero locations.
  Furthermore, any PDE boundary value problem on the strip x in [0,1] with symmetric boundary data u(0,y) = u(1,y) admits off-line symmetric singularity quadruples (x_0, y_0), (1-x_0, y_0), (x_0, -y_0), (1-x_0, -y_0) without violating any elliptic maximum or comparison principle.
  Any parabolic flow (such as Burgers via Cole-Hopf u = -2 nu (xi'/xi)) linearizes to the classical de Bruijn-Newman heat flow, which is the closed/excluded Lambda <= 0 equivalence.
- **Named RH-False Control:** Davenport-Heilbronn class-2 world. Its potential u_DH(x,y) = log|xi_DH(x+iy)| is harmonic on S \ {zeros}, satisfies u_DH(x,y) = u_DH(1-x,y), and satisfies the exact same PDE barriers while possessing certified off-line zeros.
- **Cheapest Rust-Only Falsification Test:**  
  Rust f64 finite-difference probe computing det(D^2 u) on a grid around the DH off-line zero (0.8085, 85.699); confirm det(D^2 u) <= 0 everywhere in the regular domain.

---

### 3. Information Geometry & Statistical Manifolds

- **Concrete Object Definition:**  
  Let T(s) = int_1^infty psi(u) u^{s/2 - 1} du be the entire theta-Mellin component. Define the 1-parameter exponential family on (1, infty):
  p_s(u) = (1/T(s)) psi(u) u^{s/2 - 1}.
  Define the Fisher information metric g(sigma) = Var_{p_sigma}( (1/2) log u ) = (d^2/d sigma^2) log T(sigma), and the Kullback-Leibler divergence D_KL(p_s || p_{1-s}).
- **Attempted Implication:**  
  A curvature positivity or geodesic rigidity condition on the statistical manifold (e.g. Fisher metric divergence along Re(s) != 1/2) forces all zeros of the contragredient completion xi(s) = 1/2 s(s-1)[T(s) + T(1-s)] + 1/2 to lie on Re(s) = 1/2.
- **Why the Implication Fails / Exact Fatal Flaw:**  
  T(s) is an entire function with NO zeros on the real line (since psi(u) > 0 on [1, infty)).
  The Fisher metric g(sigma) = (d^2/d sigma^2) log T(sigma) is strictly positive on R because T(sigma) is the Laplace transform of a positive measure.
  However, T(s) is NOT xi(s). The zeros of xi(s) arise from phase interference between T(s) and T(1-s).
  The statistical manifold of p_s sees only the un-interfered kernel T(s), which is completely smooth and zero-free.
  The KL divergence D_KL(p_{1/2+delta+it} || p_{1/2-delta+it}) is a smooth metric distance between probability densities; it has no singularity at zeros of xi.
- **Named RH-False Control:** Davenport-Heilbronn world. Its theta component T_DH(s) also generates a well-defined exponential family with positive Fisher metric g_DH(sigma) > 0, completely uncoupled from its off-line zeros.
- **Cheapest Rust-Only Falsification Test:**  
  Rust f64 computation of g(sigma) and D_KL(p_s || p_{1-s}) at the ordinate of the first zero t = 14.1347 vs off-zero t = 10.0; confirm that information geometric invariants are completely smooth and non-vanishing at both points.

---

### 4. Discrete Integrable Systems & Toda Lattice

- **Concrete Object Definition:**  
  Define the Toda lattice tau-function hierarchy from Hankel determinants:
  tau_n = det( [c_{j+k}]_{0 <= j,k <= n-1} ),
  where either (Option A) c_k = M_k = 2 int_0^infty Phi(u) u^{2k} du (even theta moments), or (Option B) c_k = gamma(k) = xi^{(2k)}(1/2) / (2k)! (Taylor coefficients of xi).
  Hirota bilinear equation: tau_n(t) tau_n''(t) - (tau_n'(t))^2 = tau_{n+1}(t) tau_{n-1}(t).
- **Attempted Implication:**  
  Total positivity of the Toda hierarchy tau_n > 0 for all n forces the generating function to belong to the Laguerre-Polya class, implying all real zeros.
- **Why the Implication Fails / Exact Fatal Flaw:**  
  - Under Option A (Moments M_k): Phi(u) > 0 is a strictly positive measure, so tau_n(M) > 0 for all n >= 1 unconditionally. However, as proven in `frontier-smalln0-slice` and `barrierzoo-retrotest`, the Davenport-Heilbronn world ALSO has positive theta moments M_k^{DH} with tau_n(M^{DH}) > 0 for all n. Thus tau_n(M) > 0 holds in both RH-true and RH-false worlds (Trap A, proves too much).
  - Under Option B (Taylor coefficients gamma(k)): The connection between M_k and gamma(k) is gamma(k) = k! M_k / (2k)!. As proven by exact arithmetic in the repository, the renormalization factor k! / (2k)! destroys total positivity:
    tau_2(gamma) = gamma(0) gamma(2) - (gamma(1))^2 = - 9.189076e-06 < 0.
    Thus tau_2(gamma) < 0 FAILS on the actual Riemann zeta function (Trap C, premise refuted).
- **Named RH-False Control:** Davenport-Heilbronn world for Option A; exact 210-bit g02 oracle data for Option B.
- **Cheapest Rust-Only Falsification Test:**  
  Rust rug/f64 evaluation of tau_2(gamma) from the first three Taylor coefficients c_0 = 0.497120778, c_2 = 0.02310499, c_4 = 0.00053215; verify det2 = c_0 c_4 - c_2^2 < 0 directly in 1 ms.

---

### 5. Algorithmic Information & Entropy

- **Concrete Object Definition:**  
  Let {gamma_n} be the sequence of ordinates of non-trivial zeros. Define the spectral gap entropy:
  H_N = - sum_{n=1}^N P_n log P_n, where P_n = (gamma_{n+1} - gamma_n) / (gamma_{N+1} - gamma_1).
  Alternatively, consider the Kolmogorov complexity K( xi|_B ) or the differential entropy of the normalized critical line density |xi(1/2+it)|^2.
- **Attempted Implication:**  
  An entropy maximization principle H({gamma_n}) >= H_GUE or minimal description complexity forces the horizontal offsets b_n = -(beta_n - 1/2) to vanish.
- **Why the Implication Fails / Exact Fatal Flaw:**  
  1. The zero ordinates gamma_n are functions of the imaginary parts only. Horizontal shifts beta_n -> beta_n + delta modify the local spacing of ordinates only at second order O(delta^2 / gamma_n^2).
  2. The Davenport-Heilbronn zero sequence has the exact same leading-order asymptotic density N(T) ~ (T/2pi) log(T/2pi e) and the exact same algorithmic complexity class (zeros computable via Euler-Maclaurin in polynomial time per digit).
  3. The differential entropy of |xi(1/2+it)|^2 is a 1D line integral, which is completely blind to off-line zeros (modulus-blindness).
- **Named RH-False Control:** Davenport-Heilbronn class-2 world (certified off-line zeros, identical ordinate entropy class).
- **Cheapest Rust-Only Falsification Test:**  
  Rust probe computing H_N on the first 100 zeros of zeta vs first 100 zeros of DH; confirm that the entropy difference is dominated by finite-T fluctuations and does not separate off-line zeros.

---

## 2. Strongest Universal Obstruction Theorem

**Theorem (Universal Obstruction on Classical Data):**  
Let X be any mathematical object (PDE potential, optimal transport metric, information manifold, integrable tau-function, or entropy functional) whose inputs are restricted to:
1. The theta-function density Phi(u) and its positive moments M_k,
2. The functional equation symmetry s <-> 1-s and real-axis conjugation s <-> s-bar,
3. The critical line evaluations |xi(1/2+it)| or horizontal lines Re(s) = sigma,
4. The global counting function N(T) ~ (T/2pi) log T.

Then any proposed condition H(X) => RH MUST satisfy at least one of the following:
- **(i) Vacuous on RH-False Models:** H(X_DH) is true for the Davenport-Heilbronn world (which has certified off-line zeros), so H does NOT imply RH.
- **(ii) False on Actual Zeta:** H(X_zeta) is refuted by exact arithmetic on zeta (e.g. Hankel det2 < 0, Phi not in PF_infinity, uniform phase-gap = 0).
- **(iii) Identical to RH:** H(X) is logically equivalent to RH (H <=> RH) and cannot be proved without already proving RH.
- **(iv) Unprovable Smuggled Hypothesis:** H(X) requires an unproved zero-free half-plane Re(s) > 1/2 as a hypothesis.

**Conclusion:**  
There is no legitimate, unclosed, one-way sufficient condition H(zeta) => RH in the requested non-classical domains. The search space across these five domains is **CLOSED (NONE)**.

## Coordinator epistemic correction

The domain-by-domain closures are useful research triage, but the memo's final "universal
obstruction" is **not promoted to PROVEN** as a theorem about every possible object: its input
class is a stipulated restriction, and a genuinely new prime-sensitive construction could lie
outside it. The honest campaign status is **INCONCLUSIVE / NO CANDIDATE FOUND in these five
specified domains**, with the individual elementary counterexamples and exact identities
retaining their stated labels. The search therefore continues on prime-sensitive objects.
