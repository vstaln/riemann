#!/usr/bin/env python3
"""Multi-window certificate — MATRIX-LEVEL verification on real zero data (T=1000).

Verdict (scale-free, /tmp/mw_scale_free.py): the joint m-window system is equivalent to
a SINGLE window whose pair profile is V = sum_alpha u_alpha^2, hence cannot beat the
Montgomery-Taylor cosine (Theorem D / CCLM17 one-delta extremal).  This script verifies
the equivalence at the actual Gram-matrix level:

   G_joint[gamma,gamma'] = sum_{alpha,k} bu_alpha(s_g-k) bu_alpha(s_g'-k) / (m a)
        ==  b(V)(s_g - s_g') / (m a)          (sampling-kernel identity, V = sum A_alpha cos^2(w_alpha x))

and recomputes R = ||bG||_F^2/tr(bG) for the joint matrices, compared against the
single-window values and the scale-free prediction.

Everything CHECKED NUMERICALLY at f64 (numpy).
"""
import numpy as np

PI = np.pi
SQRT2 = np.sqrt(2.0)

def sinc(t):
    out = np.ones_like(t, dtype=float)
    nz = np.abs(t) > 1e-12
    out[nz] = np.sin(t[nz]) / t[nz]
    return out

def bu_cos(s, w):
    """FT of cos(w x) on [-1/2,1/2] (2 pi convention)."""
    return 0.5 * (sinc((w - 2*PI*s)/2.0) + sinc((w + 2*PI*s)/2.0))

def bv_cos2(r, w):
    """FT of cos^2(w x)."""
    return 0.5 * bu_cos(r, 0.0) + 0.5 * bu_cos(r, 2.0*w)

def load_zeros(paths):
    g = []
    for p in paths:
        with open(p) as f:
            for line in f:
                q = line.split()
                if len(q) >= 2:
                    g.append(float(q[1]))
    g.sort()
    return np.array(g)

def main():
    T = 1000.0
    D0 = np.sqrt(T)
    gams = load_zeros(["/home/vstaln/riemann/tools/data/zeros_computed_10000.txt"])
    I = (gams >= T) & (gams < 2.0*T)
    Ipr = (gams > T - D0) & (gams <= 2.0*T + D0)
    gI, gIpr = gams[I], gams[Ipr]
    N, Npr = len(gI), len(gIpr)
    print(f"T={T:.0f}: N(I)={N}, N(I')={Npr}")
    s_rho = (gIpr - T) * (N / T)
    reach = 250
    kmin = int(np.floor(s_rho.min() - reach)); kmax = int(np.ceil(s_rho.max() + reach))
    ks = np.arange(kmin, kmax + 1)
    d = len(ks)
    print(f"padded grid k in [{kmin},{kmax}], d={d}")

    # conv Q: evaluation profile u = A cos(w x), pair profile v = u^2 = A cos^2(w x), int v = a common.
    aQ = 0.5*(1.0 + np.sin(SQRT2)/SQRT2)

    def eval_mat(ws, a):
        """B[gamma, (alpha,k)] = sqrt(A_alpha) bu_cos(s_g - k),  A_alpha = a / int cos^2(w x)."""
        m = len(ws)
        B = np.empty((len(s_rho), m*d))
        for ai, w in enumerate(ws):
            A = a / (0.5*(1.0 + np.sin(w)/w))
            for i, s in enumerate(s_rho):
                B[i, ai*d:(ai+1)*d] = np.sqrt(A) * bu_cos(s - ks, w)
        return B

    def joint_stats(B, m, a):
        G = B @ B.T / (m*a)
        tr = np.trace(G)
        h = (G**2).sum()
        R = h / tr
        return tr, h, R, 2.0 - R

    # ---- single MT ----
    B1 = eval_mat([SQRT2], aQ)
    tr1, h1, R1, c1 = joint_stats(B1, 1, aQ)
    print(f"\n[1] single MT (conv Q):        tr={tr1:.4f} R={R1:.9f}  cert_int=2-R={c1:.9f}")
    print(f"      scale-free conv Q R = 1.332676 ; conv P (paper) R = 1.327499")

    # ---- joint identical x2 (control) ----
    B2i = eval_mat([SQRT2, SQRT2], aQ)
    tr2i, h2i, R2i, c2i = joint_stats(B2i, 2, aQ)
    print(f"[2] joint identical x2:         tr={tr2i:.4f} R={R2i:.9f}  cert={c2i:.9f}  (must equal single R)")

    # ---- joint detuned x2 ----
    ws2 = [SQRT2, 2.0]
    B2 = eval_mat(ws2, aQ)
    tr2, h2, R2, c2 = joint_stats(B2, 2, aQ)
    print(f"[3] joint detuned x2 {ws2}:     tr={tr2:.4f} R={R2:.9f}  cert={c2:.9f}")

    # ---- sum-profile identity: G_joint[g,g'] vs b(V)(s_g - s_g')/(m a), V = sum A cos^2 ----
    Vfun = np.zeros_like(s_rho)
    # build b(V)(s_g - s_g') for all pairs without O(n^2) Python loops:
    S = s_rho[:, None] - s_rho[None, :]          # n x n difference matrix
    GV = np.zeros_like(S)
    for w in ws2:
        A = aQ / (0.5*(1.0 + np.sin(w)/w))
        GV += A * bv_cos2(S, w)                  # b(A cos^2(w .))(r) = A b(cos^2(w .))(r)
    GV /= (2*aQ)                                  # / (m a)
    Gj = B2 @ B2.T / (2*aQ)
    err = np.abs(Gj - GV).max()
    rel = err / np.abs(GV).max()
    print(f"[4] sum-profile identity: max|G_joint - b(V)/(m a)| = {err:.3e}  (rel {rel:.3e})  -> EXACT by construction")
    # also verify the row of the sum-profile single-window Gram is the same:
    print(f"      trace(G_joint)={np.trace(Gj):.4f} trace(G_V)={np.trace(GV):.4f}")

    # ---- detuned x4, x8 ----
    for label, ws in [
        ("detuned x4 {1.0,1.4142,2.0,2.5}", [1.0, SQRT2, 2.0, 2.5]),
        ("detuned x8 {0.5,1.0,1.3,1.4142,1.8,2.2,2.6,3.0}", [0.5,1.0,1.3,SQRT2,1.8,2.2,2.6,3.0]),
    ]:
        m = len(ws)
        B = eval_mat(ws, aQ)
        tr, h, R, c = joint_stats(B, m, aQ)
        print(f"[5] {label}:  R={R:.9f}  cert={c:.9f}")

    # ---- certificate with boundary term (paper table (6) style) ----
    # cert = 4 tr bG - 2 N(I') - ||bG||_F^2, per N(I) zero  (tr bG ~ N(I') here, padded grid)
    for label, (R, trv) in [("single MT", (R1, tr1)), ("detuned x2", (R2, tr2))]:
        h_v = R * trv
        cert = (4.0*trv - 2.0*Npr - h_v) / N
        cert_int = 2.0 - R
        print(f"[6] {label}: cert(boundary-corrected)={cert:.6f}/zero(I), cert(interior)=2-R={cert_int:.6f}")

    print("\nDONE")

if __name__ == '__main__':
    main()
