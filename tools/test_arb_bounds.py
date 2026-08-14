#!/usr/bin/env python3
"""
tools/test_arb_bounds.py

Rapid interval verifier probe across candidate alphas and eps targets.
"""

import sys
sys.path.insert(0, '/root/riemann/tools')
from verify_coboundary_floor import verify_floor, cosine_kernel

def test_config(alpha_val, target_val, p_val=1.0/3000):
    w = {(i, j): 2.0 / (7 - (j - i)) for i in range(7) for j in range(i + 1, 7)}
    p = [c / 1920000 for c in [946, 1177, 877, 877, 1177, 946]]
    q = [31343 / 100000, 1/3, 105971 / 300000, 105971 / 300000, 1/3, 31343 / 100000]
    
    print(f"Testing alpha={alpha_val}, target={target_val}...")
    try:
        r = verify_floor(
            cosine_kernel(alpha_val),
            w,
            p_val,
            6,
            target_val,
            grid=4000,
            cap_scheme='coboundary',
            pressure_coeffs=p,
            nearest_coeffs=q,
            max_nodes=100000
        )
        print(f"  Result: verified={r['verified']}, nodes={r.get('nodes', 0)}")
        return r['verified']
    except Exception as e:
        print(f"  Error: {e}")
        return False

if __name__ == "__main__":
    for alpha in [1.464, 1.460, 1.455]:
        for target in [0.0062, 0.0063, 0.0064]:
            test_config(alpha, target)
