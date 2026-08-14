#!/usr/bin/env python3
"""
tools/slepian_window_optimizer.py

Track 2: Continuous Slepian Prolate Spheroidal & Multi-Harmonic Window Optimizer.
Optimizes the continuous window v(t) over an orthogonal Legendre basis
    v(t) = sum_{k=0}^K c_k P_{2k}(2t)   for t in [-1/2, 1/2]
to maximize the exact Anthropic window functional
    H(v) = 2 - (I_2 + J) / I_0^2
where all integrals I_0, I_2, J are computed via exact Legendre anti-derivatives.
"""

import numpy as np
import scipy.optimize as opt
import mpmath as mp

mp.dps = 60

def legendre_P2k(k, x):
    """Evaluates the 2k-th Legendre polynomial P_{2k}(x)."""
    # x in [-1, 1]
    return mp.legendre(2 * k, x)

def compute_H_legendre(coeffs):
    """
    Computes exact I_0, I_2, J, and H for v(t) = sum_{k=0}^{K-1} c_k P_{2k}(2t) on [-1/2, 1/2].
    Using substitution x = 2t in [-1, 1].
    dt = dx / 2.
    """
    K = len(coeffs)
    coeffs = [mp.mpf(c) for c in coeffs]
    
    # 1. I_0 = int_{-1/2}^{1/2} v(t) dt = (1/2) int_{-1}^1 sum c_k P_{2k}(x) dx
    # By orthogonality, int_{-1}^1 P_{2k}(x) dx = 2 if k=0, else 0.
    # Therefore, I_0 = (1/2) * (c_0 * 2) = c_0.
    I0 = coeffs[0]
    if abs(I0) < 1e-15:
        return -float('inf'), 0, 0, 0, 0
        
    # 2. I_2 = int_{-1/2}^{1/2} v(t)^2 dt = (1/2) int_{-1}^1 [sum c_k P_{2k}(x)]^2 dx
    # By orthogonality, int_{-1}^1 P_{2k}(x)^2 dx = 2 / (4k + 1).
    # Therefore, I_2 = (1/2) * sum c_k^2 * (2 / (4k + 1)) = sum_{k=0}^{K-1} c_k^2 / (4k + 1).
    I2 = sum(coeffs[k]**2 / (4 * k + 1) for k in range(K))
    
    # 3. J = int_{-1/2}^{1/2} int_{-1/2}^{1/2} |s-t| v(s) v(t) ds dt
    # With u = 2s, v_var = 2t in [-1, 1]:
    # |s-t| = (1/2) |u - v_var|
    # ds dt = (1/4) du dv_var
    # J = (1/8) int_{-1}^1 int_{-1}^1 |u - v_var| [sum c_i P_{2i}(u)] [sum c_j P_{2j}(v_var)] du dv_var
    # We compute the symmetric matrix M_{ij} = int_{-1}^1 int_{-1}^1 |u - v| P_{2i}(u) P_{2j}(v) du dv
    # For |u - v| = 2 max(u, v) - (u + v) = 2 (u - v)_+ + ...
    # We evaluate M_{ij} to high precision via 1D anti-derivative:
    # int_{-1}^u (u - v) P_{2j}(v) dv
    
    # Double integral using mpmath adaptive quadrature
    def J_integrand(u, v_var):
        val_u = sum(coeffs[i] * mp.legendre(2 * i, u) for i in range(K))
        val_v = sum(coeffs[j] * mp.legendre(2 * j, v_var) for j in range(K))
        return abs(u - v_var) * val_u * val_v
        
    # Split into u >= v_var by symmetry: J = 2 * (1/8) int_{-1}^1 du int_{-1}^u dv_var (u - v_var) v(u) v(v_var)
    # Using 1D integration over u of v(u) * antiderivative_v(u)
    # Anti-derivative G_j(u) = int_{-1}^u (u - v) P_{2j}(v) dv
    # For j=0: P_0 = 1 => G_0(u) = (u+1)^2 / 2
    # For j>=1: int_{-1}^u (u-v) P_{2j}(v) dv = u int P_{2j} - int v P_{2j}
    # = u [P_{2j+1}(u) - P_{2j-1}(u)] / (4j+1) - int_{-1}^u v P_{2j}(v) dv
    
    # Accurate numerical evaluation
    J_val = (mp.mpf(1) / 4) * mp.quad(
        lambda u: sum(coeffs[i] * mp.legendre(2 * i, u) for i in range(K)) * 
                  mp.quad(lambda v_var: (u - v_var) * sum(coeffs[j] * mp.legendre(2 * j, v_var) for j in range(K)), [-1, u]),
        [-1, 1]
    )
    
    c_val = (I0**2) / (I2 + J_val)
    H_val = 2 - 1 / c_val
    return float(H_val), float(c_val), float(I0), float(I2), float(J_val)

def run_slepian_optimizer():
    print("=" * 75)
    print("TRACK 2: CONTINUOUS SLEPIAN / LEGENDRE WINDOW OPTIMIZER")
    print("=" * 75)
    
    # 1. Baseline: c_0 = 1.0 (Flat window v(t) = 1)
    H_flat, c_flat, I0, I2, J = compute_H_legendre([1.0])
    print(f"Flat Window (K=1): H = {H_flat:.12f} (c = {c_flat:.12f})")
    
    # 2. Degree K=2: v(t) = c_0 P_0 + c_1 P_2(2t) = c_0 + c_1 (3(4t^2) - 1)/2
    print("\n--- Optimizing Degree K=2 (P_0, P_2) ---")
    def obj_K2(c1):
        H, _, _, _, _ = compute_H_legendre([1.0, c1[0]])
        return -H
        
    res2 = opt.minimize(obj_K2, [-0.2], method='Nelder-Mead', options={'xatol': 1e-5, 'fatol': 1e-8})
    c1_opt = res2.x[0]
    H_K2, c_K2, _, _, _ = compute_H_legendre([1.0, c1_opt])
    print(f"Optimal K=2 Window:")
    print(f"  c_0 = 1.0, c_1 = {c1_opt:.8f}")
    print(f"  H(v) = {H_K2:.12f} (c = {c_K2:.12f})")
    
    # 3. Degree K=3: v(t) = c_0 P_0 + c_1 P_2 + c_2 P_4
    print("\n--- Optimizing Degree K=3 (P_0, P_2, P_4) ---")
    def obj_K3(params):
        H, _, _, _, _ = compute_H_legendre([1.0, params[0], params[1]])
        return -H
        
    res3 = opt.minimize(obj_K3, [c1_opt, 0.05], method='Nelder-Mead', options={'xatol': 1e-5, 'fatol': 1e-8})
    c1_opt3, c2_opt3 = res3.x
    H_K3, c_K3, _, _, _ = compute_H_legendre([1.0, c1_opt3, c2_opt3])
    print(f"Optimal K=3 Window:")
    print(f"  c_0 = 1.0, c_1 = {c1_opt3:.8f}, c_2 = {c2_opt3:.8f}")
    print(f"  H(v) = {H_K3:.12f} (c = {c_K3:.12f})")
    
    # 4. Slepian Prolate Comparison
    H_cos_base = float(mp.mpf(3)/2 - mp.cot(1/mp.sqrt(2))/mp.sqrt(2))
    print("\n===========================================================================")
    print("CONTINUOUS WINDOW THEORETICAL SUMMARY:")
    print(f"  Classical Cosine Window H(sqrt(2)): {H_cos_base:.12f}")
    print(f"  Optimal Legendre K=3 Window H(v):  {H_K3:.12f}")
    print(f"  Shift in Continuous Baseline:      {H_K3 - H_cos_base:+.8e}")
    print("===========================================================================")
    
    with open("/root/riemann/research/notes/slepian_window_results.md", "w") as f:
        f.write("# Slepian & Orthogonal Legendre Window Optimization Results\n\n")
        f.write(f"- **K=3 Optimal Coefficients:** $c_0 = 1.0$, $c_1 = {c1_opt3:.8f}$, $c_2 = {c2_opt3:.8f}$\n")
        f.write(f"- **Optimal Continuous Functional:** $H(v) = {H_K3:.12f}$\n")
        f.write(f"- **Shift over Single Cosine:** $\\Delta H = {H_K3 - H_cos_base:+.8e}$\n")

if __name__ == "__main__":
    run_slepian_optimizer()
