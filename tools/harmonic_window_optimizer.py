#!/usr/bin/env python3
"""
tools/harmonic_window_optimizer.py

Multi-Harmonic Window Functional Optimizer for Riemann Zeta Simple Zeros.
Optimizes the continuous window function v(t) = sum_{k=0}^K c_k cos(omega_k t)
on [-1/2, 1/2] to maximize the base Anthropic functional:
    H(v) = 2 - (I_2 + J) / I_0^2
where:
    I_0 = int_{-1/2}^{1/2} v(t) dt
    I_2 = int_{-1/2}^{1/2} v(t)^2 dt
    J   = iint_{[-1/2, 1/2]^2} |s-t| v(s) v(t) ds dt
"""

import numpy as np
import scipy.optimize as opt
import mpmath as mp

mp.dps = 50

def compute_H_window(coeffs, omegas):
    """
    Computes I_0, I_2, J, and H for v(t) = sum c_k cos(w_k t)
    using exact anti-derivatives.
    """
    # Number of harmonics
    K = len(coeffs)
    
    # 1. I_0 = sum c_k * 2 sin(w_k/2) / w_k
    I0 = mp.mpf(0)
    for c, w in zip(coeffs, omegas):
        if w == 0:
            I0 += c * 1
        else:
            I0 += c * 2 * mp.sin(w / 2) / w
            
    # 2. I_2 = int_{-1/2}^{1/2} (sum c_k cos(w_k t))^2 dt
    # cos(a t) cos(b t) = 1/2 [cos((a-b)t) + cos((a+b)t)]
    I2 = mp.mpf(0)
    for i in range(K):
        for j in range(K):
            ci, cj = coeffs[i], coeffs[j]
            wi, wj = omegas[i], omegas[j]
            
            # term 1: cos((wi - wj)t)
            w_minus = wi - wj
            if w_minus == 0:
                t1 = mp.mpf(1)
            else:
                t1 = 2 * mp.sin(w_minus / 2) / w_minus
                
            # term 2: cos((wi + wj)t)
            w_plus = wi + wj
            if w_plus == 0:
                t2 = mp.mpf(1)
            else:
                t2 = 2 * mp.sin(w_plus / 2) / w_plus
                
            I2 += ci * cj * (t1 + t2) / 4
            
    # 3. J = 2 int_{-1/2}^{1/2} v(s) [s int_{-1/2}^s v(t) dt - int_{-1/2}^s t v(t) dt] ds
    # For each pair (wi, wj):
    # F_j(s) = int_{-1/2}^s cos(wj t) dt = [sin(wj s) + sin(wj/2)] / wj
    # G_j(s) = int_{-1/2}^s t cos(wj t) dt = [t sin(wj t)/wj + cos(wj t)/wj^2]_{-1/2}^s
    # K_j(s) = s F_j(s) - G_j(s) = s sin(wj/2)/wj - cos(wj s)/wj^2 + cos(wj/2)/wj^2 - (1/2)sin(wj/2)/wj
    # J = 2 sum_i sum_j ci cj int_{-1/2}^{1/2} cos(wi s) K_j(s) ds
    J = mp.mpf(0)
    for i in range(K):
        for j in range(K):
            ci, cj = coeffs[i], coeffs[j]
            wi, wj = omegas[i], omegas[j]
            
            # We integrate numerically to 50 dps via mpmath Gauss-Legendre
            def integrand(s):
                # v_i(s)
                vi = mp.cos(wi * s)
                # K_j(s)
                if wj == 0:
                    # v_j(t) = 1 => F_j(s) = s + 1/2, G_j(s) = (s^2 - 1/4)/2
                    # K_j(s) = s(s + 1/2) - (s^2 - 1/4)/2 = s^2/2 + s/2 + 1/8
                    Kj = s*s/2 + s/2 + mp.mpf(1)/8
                else:
                    Kj = (s * mp.sin(wj/2)/wj - mp.cos(wj*s)/(wj**2) + 
                          mp.cos(wj/2)/(wj**2) - mp.sin(wj/2)/(2*wj))
                return vi * Kj
                
            pair_J = 2 * mp.quad(integrand, [-mp.mpf(1)/2, mp.mpf(1)/2])
            J += ci * cj * pair_J
            
    c_val = (I0**2) / (I2 + J)
    H_val = 2 - 1 / c_val
    return float(H_val), float(c_val), float(I0), float(I2), float(J)

def run_window_optimization():
    print("=" * 75)
    print("MULTI-HARMONIC WINDOW FUNCTIONAL CONTINUOUS OPTIMIZER")
    print("=" * 75)
    
    # 1. Baseline: Anthropic single cosine omega = sqrt(2)
    H_base, c_base, I0, I2, J = compute_H_window([1.0], [mp.sqrt(2)])
    print(f"Anthropic Baseline (omega=sqrt(2)): H = {H_base:.12f} (c = {c_base:.12f})")
    
    # 2. Single Cosine Frequency Sweep: omega in [1.3, 1.6]
    print("\n--- Single Frequency Sweep ---")
    best_w = None
    best_H = -float('inf')
    for w_val in np.linspace(1.35, 1.55, 21):
        H_w, _, _, _, _ = compute_H_window([1.0], [mp.mpf(w_val)])
        if H_w > best_H:
            best_H = H_w
            best_w = w_val
        print(f"  omega = {w_val:.4f} => H = {H_w:.10f}")
        
    print(f"Optimal Single Cosine: omega = {best_w:.4f}, H = {best_H:.10f}")
    
    # 3. Two-Harmonic Optimization: v(t) = cos(w_0 t) + c_1 cos(3 w_0 t)
    print("\n--- Two-Harmonic Window Optimization ---")
    def obj_2harmonic(params):
        w0, c1 = params
        H_val, _, _, _, _ = compute_H_window([1.0, mp.mpf(c1)], [mp.mpf(w0), mp.mpf(3*w0)])
        return -H_val
        
    res2 = opt.minimize(obj_2harmonic, [1.4142, 0.01], method='Nelder-Mead', options={'xatol': 1e-5, 'fatol': 1e-9})
    w0_opt, c1_opt = res2.x
    H_2harm = -res2.fun
    print(f"Optimal Two-Harmonic Window:")
    print(f"  w_0 = {w0_opt:.6f}, c_1 = {c1_opt:.6f} => H = {H_2harm:.12f}")
    print(f"  Gain over single cosine: {H_2harm - H_base:+.8e}")
    
    # 4. Multi-Harmonic Polynomial Envelope: v(t) = (1 - 4 t^2)^p cos(w t)
    print("\n--- Prolate Spheroidal & Slepian Window Test ---")
    # Discretized Legendre basis expansion v(t) = sum a_k P_{2k}(2t)
    # Testing higher degrees
    print("=" * 75)

if __name__ == "__main__":
    run_window_optimization()
