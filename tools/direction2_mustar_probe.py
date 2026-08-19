#!/usr/bin/env python3
"""
tools/direction2_mustar_probe.py
================================
Numeric mu* probe for the Direction-2 soundstate 2x2 covariance SDP.

The batch-2 CLOSURE (agy-batch2-adjudication-2026-08-18.md) claims the 2x2 PSD
bandlimited matrix minorant on V(t)=(Re f, Im f'/theta') CANNOT beat the scalar
Levinson extremal (psi(u)=cos(sqrt2 u), c1*=0.753296, proportion 0.6725). Mechanism:
Euler-Lagrange uncoupling -> the quotient concentrates on the dominant eigenvector
mode alone (C2 = 0), i.e. the cross-direction adds no variance.

This probe tests that mechanism NUMERICALLY against the MEASURED soundstate
covariances (covar-probe-v2-Y*.txt): if the second-mode energy fraction lambda2/lambda1
is ~0 (rank-1 dominant), the matrix minorant collapses to scalar EXACTLY as claimed,
and mu* (matrix optimum / scalar optimum) >= 1. If lambda2/lambda1 were O(1), the
matrix minorant could extract extra variance and the closure would be wrong.

mu* is defined here by the Rayleigh-quotient ratio of the 2x2 problem vs the scalar:
  Q_matrix(v) = ( v^T Sigma0 v ) / ( integral w^T v )^2 minimized over 2-vectors
The closure asserts min Q_matrix == min Q_scalar (C2=0). We proxy the decisive
object: the normalized covariance of (Re f, Im f'/theta') and its spectral split.

Only f64+numpy; reproducible:  uv run --with numpy python tools/direction2_mustar_probe.py
Label: CHECKED NUMERICALLY (probe of a PROVEN-by-mechanism closure; confirms or
refutes the closure's numeric content, does not by itself prove anything about RH).
"""

import json
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
NOTES = os.path.join(os.path.dirname(HERE), "research", "notes")

# ---- measured 4x4 + 2x2 minor covariances from covar-probe-v2-Y*.txt ----
# (Re f, Im f, Re f'/t', Im f'/t') for f = zeta*M, T=1e6 stretch, 800 samples.
MEASURED = {
    # Y=1 (no mollifier) -- from covar-probe-v2-Y1-output.txt
    1: {
        "4x4": np.array([
            [5.8048e0, 6.4845e-1, 6.8113e-1, -6.2895e0],
            [6.4845e-1, 6.4781e0, 6.9957e0, -6.7830e-1],
            [6.8113e-1, 6.9957e0, 9.5113e0, -5.9077e-1],
            [-6.2895e0, -6.7830e-1, -5.9077e-1, 8.9972e0],
        ]),
        "minor_eig": [13.8899, 0.9121],
    },
    10: {
        "4x4": np.array([
            [2.4741e0, -1.1626e-1, -1.3230e-1, -3.4004e0],
            [-1.1626e-1, 2.4474e0, 3.3828e0, 1.3053e-1],
            [-1.3230e-1, 3.3828e0, 5.5688e0, 1.3638e-1],
            [-3.4004e0, 1.3053e-1, 1.3638e-1, 5.5652e0],
        ]),
        "minor_eig": [7.7548, 0.2844],
    },
    100: {
        "4x4": np.array([
            [3.9755e0, -5.9820e-1, -1.1309e0, -6.9452e0],
            [-5.9820e-1, 2.5410e0, 4.4954e0, 1.1302e0],
            [-1.1309e0, 4.4954e0, 9.0005e0, 2.1773e0],
            [-6.9452e0, 1.1302e0, 2.1773e0, 1.3455e1],
        ]),
        "minor_eig": [17.1235, 0.3068],  # 2x2 minor (Re f, Im f'/t') eigvals
    },
    1000: {
        "4x4": np.array([
            [3.3827e0, 6.9164e-1, 1.4290e0, -7.2429e0],
            [6.9164e-1, 3.8056e0, 8.1453e0, -1.4274e0],
            [1.4290e0, 8.1453e0, 1.8619e1, -2.8031e0],
            [-7.2429e0, -1.4274e0, -2.8031e0, 1.6816e1],
        ]),
        "minor_eig": [19.9768, 0.2214],
    },
}


def eigfrac(M):
    """Return sorted eigenvalues (desc), their fractions of the trace, and
    lambda2/lambda1 (the C2-mode energy ratio)."""
    w = np.linalg.eigvalsh(M)
    w = w[::-1]
    tr = w.sum()
    frac = w / tr if tr > 0 else np.zeros_like(w)
    r21 = float(w[1] / w[0]) if w[0] > 0 else 1.0
    return w, frac, r21


def main():
    print("mu* Direction-2 soundstate 2x2 covariance SDP probe")
    print("claim under test (batch-2 CLOSURE): matrix minorant collapses to scalar")
    print("  via dominant-eigenvector (C2=0); mu* = Q_matrix/Q_scalar >= 1.\n")

    scalar_const = 0.753296  # c1* (scalar Levinson extremal), the baseline
    rows = []
    for Y in sorted(MEASURED):
        m = MEASURED[Y]
        w, frac, r21 = eigfrac(m["4x4"])
        minor = m.get("minor_eig")
        print(f"--- Y={Y} (mollifier length) ---")
        print(f"  4x4 eigvals : {['%.4e'%v for v in w]}")
        print(f"  trace fracs : {['%.4f'%f for f in frac]}")
        print(f"  2nd/1st mode energy ratio (C2): {r21:.6f}")
        if minor:
            m21 = minor[1]/minor[0]
            print(f"  2x2 minor (Re f, Im f'/t') eigvals {minor[0]:.4f},{minor[1]:.4f}"
                  f" -> lambda2/lambda1 = {m21:.6f}")
        # effective rank-1 dominance: fraction of trace in top eigenvalue
        print(f"  top-eig trace fraction (rank-1 dominance): {frac[0]:.4f}")
        rows.append((Y, r21, frac[0]))

    print("\n--- verdict summary ---")
    print("(1) FULL 4x4 covariance of (Re f, Im f, Re f'/t', Im f'/t'): genuinely rank-4,")
    print("    top eigenvalue holds only ~50-63% of trace => the 'rank-1 collapse' PRIOR is")
    print("    false (this is the covar-probe finding).")
    print()
    print("(2) DECISIVE for the Direction-2 minorant on V=(Re f, Im f'/theta'): the 2x2-minor")
    print("    second-mode energy ratio lambda2/lambda1 as a function of mollifier length Y:")
    for Y, r21, f1 in rows:
        m = MEASURED[Y].get("minor_eig")
        m21 = m[1]/m[0] if m else float('nan')
        print(f"    Y={Y:>4}: 2x2-minor lambda2/lambda1 = {m21:.6f}")
    print("    -> shrinking toward 0 with Y (0.0657,0.0367,0.0179,0.0111). The cross-mode of")
    print("    the Direction-2 target subspace becomes negligible as the mollifier grows,")
    print("    i.e. the matrix minorant's second channel adds ~0 variance at the constraint")
    print("    level -- supporting the closure's C2~0 (mu* >= 1) prediction.")
    print()
    print("Caveat (honest): the 4x4 covariance is NOT rank-1, so the original DEPLOYED")
    print("'matrix has no structure' claim is overstrong; the closure's operative claim is")
    print("about the SDP CONSTRAINT collapse, which the shrinking 2x2-minor mode supports")
    print("at large Y. A full SDP solve (not run) would be the definitive scalar-vs-matrix")
    print("comparison. Numeric probe only; no RH content either way.")
    print(f"\nBaseline scalar c1* = {scalar_const}  (proportion 0.6725).")


if __name__ == "__main__":
    main()
