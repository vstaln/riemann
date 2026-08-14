#!/usr/bin/env python3
"""
tools/sweep_alpha_m.py

Exhaustive search over (alpha, m, psum, eps) for the single-normalized
coboundary certificate to find the maximal certified lower bound.
"""

import mpmath as mp
import numpy as np

mp.dps = 60

def compute_bound(alpha_val, eps_val, psum_val, m_val):
    alpha = mp.mpf(alpha_val)
    eps = mp.mpf(eps_val)
    psum = mp.mpf(psum_val)
    m = int(m_val)
    
    # H(alpha)
    I0 = 2 * mp.sin(alpha / 2) / alpha
    I2 = mp.mpf(1) / 2 + mp.sin(alpha) / (2 * alpha)
    constant = mp.sin(alpha / 2) / alpha + 2 * mp.cos(alpha / 2) / alpha**2
    J = -2 * I2 / alpha**2 + constant * I0
    c = I0**2 / (I2 + J)
    H = 2 - 1 / c
    
    A = eps * (m - 6)
    thr = mp.mpf(m) / (m - 1)
    B = A if A <= thr else 2 * mp.sqrt((m - 1) * A / m) - 1 + A / m
    tau = psum * (m - 6) / m
    
    if 1 - B / m <= 0:
        return -float('inf')
        
    bound = (H - tau) / (1 - B / m)
    return float(bound)

def run_sweep():
    print("=" * 75)
    print("PARAMETER SWEEP OVER (alpha, eps, m, psum) FOR BOUND MAXIMIZATION")
    print("=" * 75)
    
    # We test alphas in [1.450, 1.480] where eps in [0.0060, 0.0066] is certifiable
    # psum = 1/320, 1/300, 1/280, 1/250
    # m in range(120, 220)
    
    best_bound = -float('inf')
    best_params = None
    
    # Grid of candidate configurations
    alphas = [1.455, 1.458, 1.460, 1.462, 1.464, 1.466, 1.468, 1.470]
    epss = [0.0058, 0.0060, 0.0062, 0.0064, 0.0066]
    psums = [1/350, 1/320, 1/300, 1/280]
    ms = list(range(130, 210, 2))
    
    for a in alphas:
        for eps in epss:
            for psum in psums:
                for m in ms:
                    b = compute_bound(a, eps, psum, m)
                    if b > best_bound:
                        best_bound = b
                        best_params = (a, eps, psum, m)
                        
    print(f"\nTop Theoretical Configuration Found:")
    print(f"  alpha = {best_params[0]}")
    print(f"  eps   = {best_params[1]}")
    print(f"  psum  = {best_params[2]:.6f} (1/{1/best_params[2]:.1f})")
    print(f"  m     = {best_params[3]}")
    print(f"  Bound = {best_bound:.12f} ({best_bound * 100:.8f}%)")
    print("=" * 75)

if __name__ == "__main__":
    run_sweep()
