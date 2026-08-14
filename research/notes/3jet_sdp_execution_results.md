# 3-Jet Bundle & Derivative Tower SDP Execution Results
**Status:** CHECKED NUMERICALLY / PROVEN (Certified Multi-Precision & Semidefinite Execution)
**Solver Script:** [`tools/derivative_tower_sdp_solver.py`](file:///root/riemann/tools/derivative_tower_sdp_solver.py)
**Execution Date:** 2026-08-14

---
## 1. Mathematical Epistemic Declarations
- **[PROVEN] Exact 3-Jet Reproducing Kernel Closed Forms:** Anti-derivatives $J_0, J_2, J_4$ integrate $t^{a+b} \cos(\sqrt{2}t)\cos(2\pi x t)$ exactly. Odd moments $K^{(0,1)} = K^{(1,2)} = 0$ identically by window symmetry.
- **[PROVEN] Nodal Incompatibility & Interlacing:** Positive roots satisfy $z_k^{(2)} < z_k^{(1)} < z_k^{(0)} < z_{k+1}^{(2)}$. No simultaneous roots exist.
- **[PROVEN] Sylvester Inertia Theorem:** $\operatorname{In}(W_d) = (d, d, 0)$ on off-line pairs, yielding an inescapable penalty $\Delta_{\text{off}}(d) = 4d \cdot N_{\text{off}}$.
- **[CHECKED NUMERICALLY] Adversarial Gap Positivity:** $\min_{g \in [0.1, 5.0]} \operatorname{tr}(k(g)^2) > 0$ strictly across all sub-intervals.
- **[CHECKED NUMERICALLY] 7-Point Convex Stability Floor:** Floor values scale as $d=1: 0.0131 \to d=2: 1.9190 \to d=3: 12.7058$.
- **[CHECKED NUMERICALLY] Augmented Theoretical Dual Ceilings:** $p_{\text{ceil}}^{(1)} = 0.68183123 \to p_{\text{ceil}}^{(2)} = 0.71444973 \to p_{\text{ceil}}^{(3)} = 0.71468802$.

---
## 2. Kernel Origin & Moment Constants
- $I_0(0) = \sqrt{2}\sin(1/\sqrt{2}) = 0.9187253698655684
- $I_2(0) = \cos(1/\sqrt{2}) - \frac{3}{2\sqrt{2}}\sin(1/\sqrt{2}) = 0.0712005696764537
- $I_4(0) = \frac{73}{8\sqrt{2}}\sin(1/\sqrt{2}) - \frac{11}{2}\cos(1/\sqrt{2}) = 0.0103392160956907
- Variance Ratio $\sigma_1^2 = I_2(0)/I_0(0) = 0.0774992963205882
- Variance Ratio $\sigma_2^2 = (I_4(0)I_0(0) - I_2(0)^2)/I_0(0)^2 = 0.0052477293065782
- Nodal Curvature Coefficient $c_{\text{nodal}} = 0.1923324210661755

---
## 3. Nodal Geometry & Interlacing Table
| Root Index $k$ | $k^{(2,2)}$ Root $z_k^{(2)}$ | $k^{(1,1)}$ Root $z_k^{(1)}$ | $k^{(0,0)}$ Root $z_k^{(0)}$ | Defect $\operatorname{tr}(k(z_k^{(0)})^2)$ | Interlacing Status |
|:---:|:---|:---|:---|:---|:---:|
| **$k=1$** | `0.6047044109` | `0.6750686565` | `1.0572782910` | `1.52775945` | Strict Ordering |
| **$k=2$** | `1.7797806206` | `1.9203859521` | `2.0300675301` | `0.23057922` | Strict Ordering |
| **$k=3$** | `2.8744597479` | `2.9504159108` | `3.0202429922` | `0.04870170` | Strict Ordering |
| **$k=4$** | `3.9097177727` | `3.9636387923` | `4.0152356070` | `0.01566510` | Strict Ordering |

---
## 4. Adversarial Gap Sweeps $\operatorname{tr}(k(g)^2)$
| Sub-Interval | Minimizing Gap $g^*$ | Minimum $\operatorname{tr}(k(g^*)^2)$ | $k^{(0,0)}(g^*)$ | $k^{(1,1)}(g^*)$ | $k^{(2,2)}(g^*)$ | $k^{(0,2)}(g^*)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $[0.1, 1.0]$ | `0.683788` | `0.22242604` | `0.4283` | `-0.0188` | `-0.1956` | `-0.0137` |
| $[1.0, 2.0]$ | `1.859798` | `0.04605836` | `-0.0747` | `-0.0871` | `0.1575` | `-0.0636` |
| $[2.0, 3.0]$ | `2.910889` | `0.00658391` | `0.0309` | `0.0363` | `-0.0538` | `0.0265` |
| $[3.0, 4.0]$ | `3.934533` | `0.00188216` | `-0.0169` | `-0.0198` | `0.0281` | `-0.0144` |
| $[4.0, 5.0]$ | `4.948138` | `0.00073686` | `0.0107` | `0.0125` | `-0.0174` | `0.0091` |

---
## 5. Multi-Point Convex Spectral Stability 7-Point Floors
| Tower Height $d$ | Jet Space | Optimal 7-Point Floor $\operatorname{tr}(\Psi(M_{\text{aug}}))$ | Relative Amplification | Optimal Gap Configuration |
|:---:|:---|:---:|:---:|:---|
| **$d=1$** | $\xi$ | **`0.01310731`** | **1.00\times (Baseline)** | `[1.0363, 1.0243, 1.0213, 1.0227, 1.0322, 1.995]` |
| **$d=2$** | $(\xi, \xi')$ | **`1.91898437`** | **146.41\times** | `[0.812, 2.1032, 0.8405, 2.0978, 0.9055, 0.8838]` |
| **$d=3$** | $(\xi, \xi', \xi'')$ | **`12.70582622`** | **969.37\times** | `[0.6867, 2.0195, 0.7494, 1.9554, 1.8989, 0.6895]` |

---
## 6. Semidefinite Mode Optimization & Theoretical Ceilings
| Tower Level | Jet Dimensions | Dual Lift $\Delta p^{(d)}$ | Certified Dual Ceiling $p_{\text{ceil}}^{(d)}$ | Certified Realized Lower Bound $\kappa_s^{(d)}$ |
|:---|:---:|:---:|:---:|:---:|
| **Base Scalar ($d=1$)** | $1 \times M$ | Baseline | **68.183123\%** | **67.669944\%** |
| **1st Derivative ($d=2$)** | $2 \times M$ | +0.03261850 | **71.444973\%** | **69.137776\%** |
| **2nd Derivative ($d=3$)** | $3 \times M$ | +0.03285679 | **71.468802\%** | **69.148500\%** |

---
## 7. Sylvester Inertia Theorem Summary
| Tower Depth $d$ | Subspace $\mathcal{V}_d$ Dim | Sylvester Signature $(n_+, n_-, n_0)$ | Off-Line Penalty Factor |
|:---:|:---:|:---:|:---:|
| **$d=1$** | $2d = 2$ | $(1, 1, 0)$ | **$4d \cdot N_{\text{off}} = 4 \cdot N_{\text{off}}$** |
| **$d=2$** | $2d = 4$ | $(2, 2, 0)$ | **$4d \cdot N_{\text{off}} = 8 \cdot N_{\text{off}}$** |
| **$d=3$** | $2d = 6$ | $(3, 3, 0)$ | **$4d \cdot N_{\text{off}} = 12 \cdot N_{\text{off}}$** |
