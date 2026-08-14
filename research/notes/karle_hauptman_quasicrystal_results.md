# Karle-Hauptman Quasicrystal & Phase Retrieval Gram Positivity Audit

**Vector:** S4H Vector 4 (Crystallography, Phase Retrieval & Quasicrystal Gram Positivity)  
**Date:** August 2026  
**Script:** [`tools/test_karle_hauptman_gram.py`](file:///root/riemann/tools/test_karle_hauptman_gram.py)  
**Data Artifact:** [`tools/data/karle_hauptman_audit_results.json`](file:///root/riemann/tools/data/karle_hauptman_audit_results.json)  
**Zero Dataset:** [`tools/data/zeros_1_1000.txt`](file:///root/riemann/tools/data/zeros_1_1000.txt) (First $N=1000$ non-trivial zeros of $\zeta(s)$)

---

## Executive Summary & Epistemic Verdicts

1. **PROVEN (Gram Positive Semi-Definiteness on Critical Line):**  
   For any set of real ordinates $\{x_j\}_{j=1}^N \subset \mathbb{R}$ (corresponding to critical line zeros $\beta_j = 1/2$), the $3 \times 3$ Karle-Hauptman matrix:
   $$K_3(\alpha_1, \alpha_2) = \begin{pmatrix} 1 & F(\alpha_1) & F(\alpha_2) \\ F^*(\alpha_1) & 1 & F(\alpha_2 - \alpha_1) \\ F^*(\alpha_2) & F^*(\alpha_2 - \alpha_1) & 1 \end{pmatrix}$$
   is the exact Gram matrix $V^\dagger V$ of three vectors $v_0 = \frac{1}{\sqrt{N}}\mathbf{1}, v_1 = \frac{1}{\sqrt{N}}(e^{i \alpha_1 x_j})_j, v_2 = \frac{1}{\sqrt{N}}(e^{i \alpha_2 x_j})_j \in \mathbb{C}^N$. Consequently, $K_3 \succeq 0$ and $\det(K_3(\alpha_1, \alpha_2)) \ge 0$ unconditionally for all frequencies $\alpha_1, \alpha_2 \in \mathbb{R}$.

2. **PROVEN & CHECKED NUMERICALLY (Off-Line Gram Breakdown):**  
   When a zero $\rho_j = \beta_j + i \gamma_j$ is displaced off the critical line by $\delta_j = \beta_j - 1/2 \neq 0$, the structure factor entries acquire non-unitary modulus weights $e^{\alpha \delta_j}$ (or $\cosh(\alpha \delta_j)$ for functional-equation symmetric pairs). The cross-term in $K_3$ is $F(\alpha_2 - \alpha_1)$ with weight factor $e^{(\alpha_2 - \alpha_1)\delta_j}$, whereas the genuine Hilbert inner product $\langle v_1, v_2 \rangle$ requires $e^{(\alpha_1 + \alpha_2)\delta_j}$. Because $(\alpha_1 + \alpha_2) \neq (\alpha_2 - \alpha_1)$ for $\alpha_1 \neq 0$, $K_3$ **ceases to be a Gram matrix**.

3. **CHECKED NUMERICALLY (Physical Positivity Violation):**  
   - In local clusters ($N_c = 3$ zero triplets), an off-line displacement of $\delta = 0.01$ immediately drives $\det(K_3) = -9.4 \times 10^{-5} < 0$, $\lambda_{\min} = -2.62 \times 10^{-4} < 0$.
   - At $\delta = 0.05$, $14/300$ frequency pairs in the Rudnick-Sarnak window $[0.1, 1.5]$ exhibit $\det(K_3) < 0$ (reaching $\min \det = -0.011856$).
   - At $\delta = 0.25$, $158/300$ frequency pairs ($52.7\%$) violate positivity, reaching $\min \det(K_3) = -0.618971$ and $\lambda_{\min} = -0.273818$.
   - Under standard crystallographic normalized structure factors $E(\alpha) = \sqrt{N} F(\alpha)$, off-line perturbations severely violate positivity ($\min \det = -19.3418$ at $\delta = 0.25$).

4. **CONJECTURED / STRUCTURAL BOUNDARY:**  
   The Karle-Hauptman positivity condition $\det(K_3) \ge 0$ serves as an exact physical admissibility barrier: a point process with complex ordinates cannot represent a positive scattering density / Meyer quasicrystal. However, in large-window empirical averages ($N=1000$) with unnormalized structure factors $F(\alpha) = \frac{1}{N}\sum e^{i\alpha x_j}$, the off-diagonal entries are suppressed as $O(1/\sqrt{N})$, meaning that macroscopic unnormalized determinants are dominated by the diagonal identity matrix. Positivity violations are sharpest at local cluster scales ($N_c \le 10$) and in normalized phase retrieval.

---

## 1. Mathematical Formulation

### 1.1 The Karle-Hauptman 3x3 Determinant
In crystallographic phase retrieval (Karle & Hauptman, 1950), any non-negative point measure $\mu = \sum_j m_j \delta_{x_j}$ with $m_j \ge 0$ generates structure factors:
$$F(\alpha) = \frac{1}{N} \sum_{j=1}^N m_j e^{i \alpha x_j}, \quad F(0) = 1, \quad F(-\alpha) = F^*(\alpha)$$
For three frequency arguments $\{0, \alpha_1, \alpha_2\}$, the $3 \times 3$ Toeplitz-Gram matrix is:
$$K_3(\alpha_1, \alpha_2) = \begin{pmatrix} 1 & F(\alpha_1) & F(\alpha_2) \\ F^*(\alpha_1) & 1 & F(\alpha_2 - \alpha_1) \\ F^*(\alpha_2) & F^*(\alpha_2 - \alpha_1) & 1 \end{pmatrix}$$
Expanding the determinant algebraically:
$$\det(K_3(\alpha_1, \alpha_2)) = 1 - |F(\alpha_1)|^2 - |F(\alpha_2)|^2 - |F(\alpha_2 - \alpha_1)|^2 + 2 \text{Re}\left( F(\alpha_1) F^*(\alpha_2) F(\alpha_2 - \alpha_1) \right)$$
The term $T(\alpha_1, \alpha_2) = F(\alpha_1) F(-\alpha_2) F(\alpha_2 - \alpha_1)$ is the zero-sum triplet phase product ($\alpha_1 - \alpha_2 + (\alpha_2 - \alpha_1) = 0$).

### 1.2 Off-Line Perturbation Physics
Let $\rho_j = 1/2 + \delta_j + i \gamma_j$ be non-trivial zeros. Under the unfolded coordinate $x_j = \gamma_j / \langle \Delta \rangle$:
- **Unilateral / One-Sided Shift:**  
  $$F_{\text{off}}(\alpha) = \frac{1}{N} \sum_{j=1}^N e^{\alpha \delta_j} e^{i \alpha x_j}$$
- **Functional-Equation Symmetric Pairs ($1/2 \pm \delta_j + i\gamma_j$):**  
  $$F_{\text{symm}}(\alpha) = \frac{1}{N} \sum_{j=1}^N \cosh(\alpha \delta_j) e^{i \alpha x_j}$$

Because $\cosh(\alpha \delta) > 1$ for $\delta \neq 0$, off-line zeros exponentially amplify high-frequency structure factors while desynchronizing the triplet phase relation $\text{Re}(T)$, causing the Gram minor $\det(K_3)$ to collapse below zero.

---

## 2. Numerical Results & Verification Tables

### Table 1: Critical Line Baseline vs Off-Line Perturbations ($N=1000$, Full Sample)
Across 300 frequency pairs $(\alpha_1, \alpha_2)$ in the Rudnick-Sarnak window $[0.1, 1.5]$:

| Shift $\delta = \beta - 1/2$ | Perturbation Mode | $\min \det(K_3)$ | $\min \lambda_{\min}(K_3)$ | $\Delta \det$ Deficit vs On-Line | Neg. Pairs |
|:---|:---|:---|:---|:---|:---:|
| **$\delta = 0.00$ (On-Line)** | **Exact Zeros** | **$+0.98725942$** | **$+0.88752669$** | **$0.000000$ (Baseline)** | **$0 / 300$** |
| $\delta = 0.01$ | One-Sided $\exp$ | $+0.98701596$ | $+0.88645324$ | $+2.4345 \times 10^{-4}$ | $0 / 300$ |
| $\delta = 0.01$ | Symmetric $\cosh$ | $+0.98725824$ | $+0.88752150$ | $+1.1733 \times 10^{-6}$ | $0 / 300$ |
| $\delta = 0.05$ | One-Sided $\exp$ | $+0.98599334$ | $+0.88205047$ | $+1.2661 \times 10^{-3}$ | $0 / 300$ |
| $\delta = 0.05$ | Symmetric $\cosh$ | $+0.98723006$ | $+0.88739668$ | $+2.9356 \times 10^{-5}$ | $0 / 300$ |
| $\delta = 0.10$ | One-Sided $\exp$ | $+0.98459784$ | $+0.87629386$ | $+2.6616 \times 10^{-3}$ | $0 / 300$ |
| $\delta = 0.10$ | Symmetric $\cosh$ | $+0.98714171$ | $+0.88700629$ | $+1.1770 \times 10^{-4}$ | $0 / 300$ |
| $\delta = 0.20$ | One-Sided $\exp$ | $+0.98136414$ | $+0.86388387$ | $+5.8953 \times 10^{-3}$ | $0 / 300$ |
| $\delta = 0.20$ | Symmetric $\cosh$ | $+0.98678412$ | $+0.88543969$ | $+4.7530 \times 10^{-4}$ | $0 / 300$ |
| $\delta = 0.25$ | One-Sided $\exp$ | $+0.97949524$ | $+0.85720088$ | $+7.7642 \times 10^{-3}$ | $0 / 300$ |
| $\delta = 0.25$ | Symmetric $\cosh$ | $+0.98651147$ | $+0.88425941$ | $+7.4795 \times 10^{-4}$ | $0 / 300$ |

---

### Table 2: Local Cluster Positivity Breakdown ($N_c = 3, 5, 10, 20$)
Local zero clusters isolate the phase-coupling mechanism before large-$N$ central limit suppression intervenes:

| Cluster Size $N_c$ | Shift $\delta$ | $\min \det(K_3)$ | $\min \lambda_{\min}(K_3)$ | Violated Pairs (det < 0) | Physical Positivity Status |
|:---|:---|:---|:---|:---:|:---|
| **$N_c = 3$** | **$\delta = 0.00$** | **$+0.000087$** | **$+0.000238$** | **$0 / 300$** | **VALID (Gram PSD)** |
| $N_c = 3$ | $\delta = 0.01$ | $-0.000094$ | $-0.000262$ | $1 / 300$ | **VIOLATED ($\det < 0$)** |
| $N_c = 3$ | $\delta = 0.05$ | $-0.011856$ | $-0.005938$ | $14 / 300$ | **VIOLATED ($\det < 0$)** |
| $N_c = 3$ | $\delta = 0.10$ | $-0.135658$ | $-0.065986$ | $42 / 300$ | **VIOLATED ($\det < 0$)** |
| $N_c = 3$ | $\delta = 0.20$ | $-0.436526$ | $-0.199563$ | $140 / 300$ | **VIOLATED ($\det < 0$)** |
| $N_c = 3$ | $\delta = 0.25$ | $-0.618971$ | $-0.273818$ | $158 / 300$ | **VIOLATED ($\det < 0$)** |
| **$N_c = 5$** | **$\delta = 0.00$** | **$+0.001538$** | **$+0.002098$** | **$0 / 300$** | **VALID (Gram PSD)** |
| $N_c = 5$ | $\delta = 0.05$ | $-0.000371$ | $-0.000516$ | $1 / 300$ | **VIOLATED ($\det < 0$)** |
| $N_c = 5$ | $\delta = 0.10$ | $-0.002209$ | $-0.003136$ | $2 / 300$ | **VIOLATED ($\det < 0$)** |
| $N_c = 5$ | $\delta = 0.25$ | $-0.013532$ | $-0.012264$ | $10 / 300$ | **VIOLATED ($\det < 0$)** |
| **$N_c = 10$** | **$\delta = 0.00$** | **$+0.030208$** | **$+0.020573$** | **$0 / 300$** | **VALID (Gram PSD)** |
| $N_c = 10$ | $\delta = 0.25$ | $+0.008645$ | $+0.005966$ | $0 / 300$ | Marginal ($71.4\%$ drop) |
| **$N_c = 20$** | **$\delta = 0.00$** | **$+0.283229$** | **$+0.151060$** | **$0 / 300$** | **VALID (Gram PSD)** |
| $N_c = 20$ | $\delta = 0.25$ | $+0.256898$ | $+0.135791$ | $0 / 300$ | Marginal ($9.3\%$ drop) |

---

## 3. Structural Analysis & Epistemic Synthesis

### 3.1 Why Positivity Holds On-Line (The Gram Tautology)
On $\text{Re}(s) = 1/2$, the ordinates $\gamma_j$ are purely real. The vectors $v_a = \frac{1}{\sqrt{N}}(e^{i \alpha_a x_j})_{j=1}^N$ are unit vectors in $\mathbb{C}^N$. Every principal submatrix of the infinite Toeplitz matrix $K_\infty = (F(\alpha_j - \alpha_k))_{j,k}$ is a Gram matrix of unit vectors.  
Therefore:
$$\forall \alpha_1, \dots, \alpha_M \in \mathbb{R}, \quad K_M \succeq 0, \quad \det(K_M) \ge 0 \quad \text{(PROVEN)}$$

### 3.2 Why Off-Line Zeros Break Positivity
When $\delta_j = \beta_j - 1/2 \neq 0$:
1. **Norm Inflation:** The vector components acquire real exponential factors $e^{\alpha \delta_j}$. For $\alpha > 0$ and $\delta > 0$, the $L_2$ norm $\|v(\alpha)\|^2$ is no longer 1.
2. **Gram Incoherence:** The matrix entry $K_{1,2} = F(\alpha_2 - \alpha_1)$ scales as $e^{(\alpha_2 - \alpha_1)\delta}$, while the genuine inner product $\langle v(\alpha_1), v(\alpha_2) \rangle$ scales as $e^{(\alpha_1 + \alpha_2)\delta}$.
3. **Phase Inversion:** The triple correlation $T = F(\alpha_1)F(-\alpha_2)F(\alpha_2 - \alpha_1)$ is insufficient to compensate for the sum of squared magnitudes $|F(\alpha_1)|^2 + |F(\alpha_2)|^2 + |F(\alpha_2 - \alpha_1)|^2$, forcing $\det(K_3) < 0$.

### 3.3 Limitations and Connection to the Riemann Program
- **Local vs Global:** The Karle-Hauptman determinant is an intensely local phase-retrieval constraint. On macroscopic sets ($N=1000$), unnormalized empirical structure factors $F(\alpha)$ decay as $O(1/\sqrt{N})$, rendering the global Gram matrix diagonally dominant.
- **Connection to Weil Positivity:** The Karle-Hauptman Gram positivity $K_3 \succeq 0$ is the 3-point Fourier analogue of the Weil quadratic functional $W(f * \tilde{f}) \ge 0$. While Weil positivity acts on test functions in real space, Karle-Hauptman positivity acts directly on the discrete Fourier diffraction amplitudes of the zero process.

---

## 4. Reproducibility & Code Execution

To re-run the complete test suite and generate the exact metrics:
```bash
python3 /root/riemann/tools/test_karle_hauptman_gram.py
```
Output results are archived at [`tools/data/karle_hauptman_audit_results.json`](file:///root/riemann/tools/data/karle_hauptman_audit_results.json).
