#!/usr/bin/env python3
"""Probe M2.2 (music-ling catalog): masking width of a (1,1)-plane.

Question: at what separation d do two off-line pairs stop being "independently counted"
by the positive-index statistic? Model: each off-line pair at complex height s+i*beta
contributes 2*(Re(v)Re(v)^T - Im(v)Im(v)^T) to the compressed Weil form W_T, with
v[k] = Psi(s - k) (Psi = Fourier transform of the cosine window, closed form from
attack-finitet.md; [AF] gives Psi(s) = sin(1/sqrt2 - pi s)/(sqrt2 - 2 pi s)
+ sin(1/sqrt2 + pi s)/(sqrt2 + 2 pi s), removable poles at 2 pi s = +/- sqrt2).
n_+(M(d)) = positive index of the sum over two pairs separated by d. If n_+ < 2 for
small d, the positive parts overlap (subadditivity / "masking"): the certificate's
p-bookkeeping overcharges clustered off-line pairs.

Model computation on synthetic off-line pairs - labels everything, claims nothing
about real zeros. Expected: n_+ = 2 for all d above exact coincidence (worst-case
bound is tight, [AM] lemmaR_tight), i.e. masking radius ~ 0.
"""
import numpy as np

SQRT2 = np.sqrt(2.0)

def Psi(s):
    """Fourier transform of psi(u)=cos(sqrt2 u) on [-1/2,1/2]; pole-safe."""
    s = np.asarray(s, dtype=float)
    a = SQRT2 - 2 * np.pi * s
    b = SQRT2 + 2 * np.pi * s
    t1 = np.sin(1 / SQRT2 - np.pi * s)
    t2 = np.sin(1 / SQRT2 + np.pi * s)
    out = np.zeros_like(s)
    for i, si in enumerate(np.atleast_1d(s)):
        ai = SQRT2 - 2 * np.pi * si
        bi = SQRT2 + 2 * np.pi * si
        if abs(ai) < 1e-9:
            # limit: derivative of numerator w.r.t. s / derivative of denominator
            val = (-np.pi * np.cos(1 / SQRT2 - np.pi * si)) / (-2 * np.pi)
        elif abs(bi) < 1e-9:
            val = (np.pi * np.cos(1 / SQRT2 + np.pi * si)) / (2 * np.pi)
        else:
            val = np.sin(1 / SQRT2 - np.pi * si) / ai + np.sin(1 / SQRT2 + np.pi * si) / bi
        out[i] = val
    return out

def plane_vectors(s, beta, K):
    """Return (r, q) = (Re v, Im v) on the k-grid [-K, K], v[k] = Psi(s - k + 1j*beta)."""
    ks = np.arange(-K, K + 1, dtype=float)
    z = (s - ks) + 1j * beta
    # Psi at complex argument: use the analytic continuation - same formula with complex s.
    v = Psi_complex(z)
    return v.real, v.imag

def Psi_complex(z):
    """Psi at complex z; pole-safe."""
    z = np.asarray(z, dtype=complex)
    out = np.zeros(z.shape, dtype=complex)
    for i, zi in enumerate(z.flat):
        ai = SQRT2 - 2 * np.pi * zi
        bi = SQRT2 + 2 * np.pi * zi
        if abs(ai) < 1e-9:
            val = -np.pi * np.cos(1 / SQRT2 - np.pi * zi) / (-2 * np.pi)
        elif abs(bi) < 1e-9:
            val = np.pi * np.cos(1 / SQRT2 + np.pi * zi) / (2 * np.pi)
        else:
            val = np.sin(1 / SQRT2 - np.pi * zi) / ai + np.sin(1 / SQRT2 + np.pi * zi) / bi
        out.flat[i] = val
    return out

def pos_index(M, tol=1e-9):
    w = np.linalg.eigvalsh(M)
    scale = max(abs(w).max(), 1e-300)
    return int(np.sum(w > tol * scale)), w

def main():
    K = 32
    beta = 0.5   # "shallow off-line" depth (normalized s-units)
    s1 = 32.0
    print(f"model: Psi closed form, k-grid [-{K},{K}], beta={beta}, s1={s1}")

    # single pair sanity: n_+ should be 1
    r, q = plane_vectors(s1, beta, K)
    M1 = 2.0 * (np.outer(r, r) - np.outer(q, q))
    p1, _ = pos_index(M1)
    print(f"single off-line pair: n_+(M) = {p1}  (expect 1)")

    print("\n== masking width: n_+(M(d)) for two pairs separated by d ==")
    print("d        n_+     min_eig/max_eig")
    for d in [0.0, 1e-5, 1e-4, 1e-3, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 4.0, 8.0]:
        r1, q1 = plane_vectors(s1, beta, K)
        r2, q2 = plane_vectors(s1 + d, beta, K)
        M = 2.0 * (np.outer(r1, r1) - np.outer(q1, q1)
                   + np.outer(r2, r2) - np.outer(q2, q2))
        p, w = pos_index(M)
        ratio = w.min() / max(abs(w).max(), 1e-300)
        print(f"{d:5.2f}   {p}      {ratio:+.2e}")

    # K-dependence check at d = 0.2
    print("\n== K-dependence at d=0.2 ==")
    for KK in [16, 32, 64]:
        r1, q1 = plane_vectors(s1, beta, KK)
        r2, q2 = plane_vectors(s1 + 0.2, beta, KK)
        M = 2.0 * (np.outer(r1, r1) - np.outer(q1, q1)
                   + np.outer(r2, r2) - np.outer(q2, q2))
        p, _ = pos_index(M)
        print(f"K={KK:3d}: n_+ = {p}")

if __name__ == "__main__":
    main()
