#!/usr/bin/env python3
"""B5.2 + B1.3 (biology note): Hadamard-cube trace and deficit decomposition on
the real compressed Weil form W_T (cosine window).

Port of the attack-finitet construction (tools/finitet/src/main.rs):
  W_T = (1/∫ψ²) * V^T V,   V[rho][k] = Psi(s_rho - k),
  s_rho = (gamma_rho - T) * N/T,   grid k = 0..N-1,
  Psi(s) = sinc(1/(pi sqrt2) - s) + sinc(1/(pi sqrt2) + s)   [numpy sinc]
  ∫ψ²   = 1/2 + sin(sqrt2)/(2 sqrt2)
Validation target (attack-finitet table): T=100 -> trW/N = 0.992343,
HS2/N = 1.265459, bound/N = 0.719228.

New statistics:
  tr(W∘W∘W)/N      Hadamard (elementwise) cube trace  -- "epistasis kernel"
  tr(W³)/N         matrix cube (walk) trace            -- skewness-type moment
  deficit parts    diag vs offdiag split of HS2
Run:  uv run --quiet python hadamard_cube.py
"""
import numpy as np

SQRT2 = np.sqrt(2.0)
I2 = 0.5 + np.sin(SQRT2) / (2 * SQRT2)   # integral of psi^2
C = 1.0 / (SQRT2 * np.pi)               # Psi(s) = (1/2)[sinc(C - s) + sinc(C + s)]
PSI_HALF = 0.5                           # Rust: sin(a)/(sqrt2 - 2 pi s) = sin(a)/(2a)
print(f"∫ψ² = {I2:.12f}  (attack-finitet: 0.849227999318304)")

zs = np.loadtxt('/home/vstaln/riemann/tools/data/zeros_1_1000.txt')[:, 1]

def build_W(T):
    """W_T for window [T, 2T); returns W, N, s."""
    sel = (zs >= T) & (zs < 2 * T)
    g = zs[sel]
    N = g.size
    if N == 0:
        return None
    s = (g - T) * N / T
    V = np.empty((N, N))
    for k in range(N):
        t = s - k
        V[:, k] = PSI_HALF * (np.sinc(C - t) + np.sinc(C + t))
    return (V.T @ V) / I2, N, s

print("\n=== B5.2/B1.3 real W_T: trace, HS2, bound, cube traces ===")
print(f"{'T':>5} {'N':>4} {'tr/N':>8} {'HS2/N':>9} {'bound/N':>9} {'tr(W∘W∘W)/N':>13} {'tr(W³)/N':>10}")
for T in (100, 150, 200, 250, 300, 350, 400, 500, 600, 700):
    r = build_W(T)
    if r is None:
        continue
    W, N, s = r
    tr = np.trace(W)
    HS2 = np.einsum('ij,ij->', W, W)
    bound = 2 * tr - HS2
    Wc = W ** 3                     # Hadamard cube
    hcube = np.trace(Wc)
    W3 = W @ W @ W                  # matrix cube
    m3 = np.trace(W3)
    print(f"{T:>5} {N:>4} {tr/N:>8.6f} {HS2/N:>9.6f} {bound/N:>9.6f} "
          f"{hcube/N:>13.6f} {m3/N:>10.6f}")

# deficit decomposition at T=700 (N=569): diag vs offdiag of HS2
print("\n=== deficit decomposition at T=700 (N=569) ===")
W, N, s = build_W(700)
HS2 = np.einsum('ij,ij->', W, W)
diag = np.trace(W @ W) * 0          # placeholder, compute properly below
d2 = np.sum(W * W, axis=1)          # row norms
HS2_diag_part = np.sum(d2 * 0)      # will set below
# HS2 = sum_ij W_ij^2 = sum_i (W^2)_ii = trace(W^2)
HS2b = np.trace(W @ W)
# split: diagonal entries contribute sum_i W_ii^2 ; off-diagonal the rest
Wd = np.diag(W)
Hs2_diag = np.sum(Wd ** 2)
Hs2_off = HS2 - Hs2_diag
print(f"HS2/N = {HS2/N:.6f}  (trace(W^2)/N check: {HS2b/N:.6f})")
print(f"  diagonal part: {Hs2_diag/N:.6f}   off-diagonal part: {Hs2_off/N:.6f}")
print(f"  ideal-model target HS2/N = 4/3 = {4/3:.6f}; deficit from target: "
      f"{4/3 - HS2/N:+.6f}")
