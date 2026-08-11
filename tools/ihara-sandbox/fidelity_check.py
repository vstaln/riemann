"""Fidelity check: reproduce finitet's total HS2/N, tr/N, bound/N for the real zeros (T=200, 500)
and the lattice world, using the same pipeline: W[k][k'] = (1/int_psi2) sum_rho Psi(s_rho-k) Psi(s_rho-k').
"""
import numpy as np

SQRT2 = np.sqrt(2.0)
FRAC_1_SQRT2 = 1.0 / SQRT2
PI = np.pi

def psi(s):
    s = np.asarray(s, dtype=np.float64)
    d1 = SQRT2 - 2.0 * PI * s
    d2 = SQRT2 + 2.0 * PI * s
    t1 = np.sin(FRAC_1_SQRT2 - PI * s) / d1
    t2 = np.sin(FRAC_1_SQRT2 + PI * s) / d2
    t1 = np.where(np.abs(d1) < 1e-12, 0.5, t1)
    t2 = np.where(np.abs(d2) < 1e-12, 0.5, t2)
    return t1 + t2

INT_PSI2 = 0.5 + np.sin(SQRT2) / (2.0 * SQRT2)
print(f"int psi^2 = {INT_PSI2:.15f}")

def measure(tag, s_rho):
    n = len(s_rho)
    k = np.arange(n, dtype=np.float64)
    # V[rho][k] = psi(s_rho - k); W = V^T V / int_psi2
    V = psi(s_rho[:, None] - k[None, :])          # n x n
    W = (V.T @ V) / INT_PSI2
    tr = np.trace(W)
    hs2 = (W ** 2).sum()
    bound = 2.0 * tr - hs2
    print(f"{tag}: N={n} tr/N={tr/n:.6f} HS2/N={hs2/n:.6f} bound/N={bound/n:.6f}")

# real zeros T=200, 500
gams = []
for line in open("/home/vstaln/riemann/tools/data/zeros_1_1000.txt"):
    p = line.split()
    if len(p) >= 2:
        gams.append(float(p[1]))
gams = np.array(gams)
for T in (200.0, 500.0):
    gwin = gams[(gams >= T) & (gams < 2.0 * T)]
    n = len(gwin)
    s_rho = (gwin - T) * n / T
    measure(f"real T={T:4.0f}", s_rho)

# lattice worlds: N zeros at s = k + 1/2
for N in (122, 379):
    measure(f"lattice N={N}", np.arange(N, dtype=np.float64) + 0.5)
