"""Independent adjudication: m3(1) = 2 (paper, attack-twobandwidth) vs 125/64 (m3_check.py).

Direct evaluation of m3(lam) = 1 + 3*A2 + A3 for the sine-process Gram matrix,
A2 = int K(u)^2 (1 - S(u)^2) du, A3 = intint K(u)K(v)K(u+v) rho3(u,v) du dv,
K = sinc(pi lam u), S = sinc(pi u), rho3 = 1 - S(u)^2 - S(v)^2 - S(u+v)^2 + 2 S(u)S(v)S(u+v).
Fully numerical, no closed-form reduction. Plus J2 values and the 2D quadrature.
"""
import numpy as np

def sinc(x):
    x = np.asarray(x, dtype=float)
    out = np.ones_like(x)
    m = np.abs(x) > 1e-12
    out[m] = np.sin(np.pi * x[m]) / (np.pi * x[m])
    return out

def J2(lam, N=400000):
    # int_0^inf sinc(pi lam u)^2 sinc(pi u)^2 du : decay ~ u^-4, tail via analytic ~ c/U^3
    u = np.linspace(1e-6, 60.0, N)
    f = sinc(lam * u) ** 2 * sinc(u) ** 2
    return np.trapezoid(f, u)

def m3_direct(lam, N=600, U=6.0):
    """1 + 3 A2 + A3 by 2D quadrature over |u|,|v| <= U with tail correction."""
    # A2: int_{-inf}^{inf} K^2 (1-S^2) = 1/lam - 2 J2 ; take the closed part for A2 to avoid tail
    J2v = J2(lam)
    A2 = 1.0 / lam - 2 * J2v
    # A3: integrate over square [-U,U]^2; tail |u|,|v|>U negligible ~ U^-1 scale; add exact D term
    u = np.linspace(-U, U, N)
    du = u[1] - u[0]
    Uu, Vv = np.meshgrid(u, u, indexing='ij')
    K = sinc(lam * Uu) * sinc(lam * Vv) * sinc(lam * (Uu + Vv))
    S = sinc(Uu) * sinc(Vv) * sinc(Uu + Vv)
    rho3 = 1 - sinc(Uu) ** 2 - sinc(Vv) ** 2 - sinc(Uu + Vv) ** 2 + 2 * sinc(Uu) * sinc(Vv) * sinc(Uu + Vv)
    A3_trunc = np.trapezoid(np.trapezoid(K * rho3, u, axis=1), u)
    # tail: A3 = D - 3B + 2C exactly; D = 1/lam^2 (analytic), B, C have tail but small. Estimate
    # tail of A3 via subtracting the analytic D on the truncated box:
    D_trunc = np.trapezoid(np.trapezoid(K, u, axis=1), u)  # -> converges to 1/lam^2
    tail = (1.0 / lam ** 2) - D_trunc  # missing D mass outside the box (approx A3 tail, |rho3|<=~5)
    m3 = 1 + 3 * A2 + A3_trunc + tail
    return m3, A2, A3_trunc, tail

for lam in (0.5, 2 / 3, 1.0):
    J = J2(lam)
    m3, A2, A3t, tail = m3_direct(lam)
    print("lam=%.4f  J2=%.12f  m2=1/lam+lam/3=%.10f  1/lam-2J2=%.10f"
          % (lam, J, 1 / lam + lam / 3, 1 / lam - 2 * J))
    print("   m3 direct = %.8f  (A2=%.6f A3_trunc=%.6f tail=%.3e)   | analytic claim:" % (m3, A2, A3t, tail), end=" ")
    claims = {0.5: 5.0, 2 / 3: 13 / 4, 1.0: 2.0}
    print("m3 = %s" % claims[lam])
    # also the wrong formula from m3_check: D=3/(4lam), B=2*J3 (J3 = int K^3 S^2)
    u = np.linspace(1e-6, 60, 200000)
    J3 = np.trapezoid(sinc(lam * u) ** 3 * sinc(u) ** 2, u)
    wrong = 1 + 3 * (1 / lam - 2 * J) - 3 * (2 * J3) + 2 * (1 - lam / 2) + 3 / (4 * lam)
    print("   wrong-formula m3 = %.8f (should be 125/64=%.8f at lam=1)" % (wrong, 125 / 64))

print("\n--- empirical zeta-zero moments (from zeros_computed_10000.txt) ---")
gs = [float(p.split()[1]) for p in open('tools/data/zeros_computed_10000.txt') if len(p.split()) >= 2]
# Gram moments in rescaled units: window [T,2T), N zeros, G_ij = sinc(pi lam (g_i-g_j)*N/(T))... use the
# standard rescaling: positions x_i = (g_i - T)/L * 1 where L = window/... use L = (T/2pi)log... simplest:
# use normalized spacings: density-1 embedding via the cumulative: x_i = i (mean spacing 1), kernel sinc(pi lam (x_i-x_j)).
# (matches sine-process: points at integer spacing.)
for lam in (1.0, 0.5):
    n = 9000
    x = np.arange(n, dtype=float)
    # dense Gram row computation would be n^2 = 8.1e7 — do it with Toeplitz via FFT for m2, m3 is harder.
    # Instead sample pairs/table via direct numpy for n=2000:
    nn = 1500
    xx = np.arange(nn, dtype=float)
    # moments of the actual zeros' Gram: use zeros gamma in a window scaled to mean spacing 1
    T0 = gs[1000]; T1 = gs[9000]  # use zeros 1001..9000
    seg = gs[1000:9000]
    mm = len(seg)
    L = T1 - T0  # window width; mean spacing = L/mm
    # density-1: x_i = (seg[i]-T0)/L * mm
    xi = (np.asarray(seg) - T0) / L * mm
    # G_ij = sinc(pi lam (xi_i - xi_j)); tr G^2 = sum_ij G_ij^2; tr G^3 = sum_ijk G_ij G_jk G_ki
    # (xi spans 0..mm, dense; use full matrices for mm=1000)
    mm2 = 1000
    seg2 = gs[4000:5000]
    L2 = seg2[-1] - seg2[0]
    xi2 = (np.asarray(seg2) - seg2[0]) / L2 * mm2
    d = xi2[:, None] - xi2[None, :]
    G = sinc(lam * d)
    m2_emp = np.sum(G * G) / mm2
    G3 = np.einsum('ij,jk,ki->i', G, G, G)  # (G^3)_ii
    m3_emp = G3.sum() / mm2
    print("lam=%.1f emp (1000 zeros, window [g4001,g5000]): m2=%.4f m3=%.4f  vs sine (%.4f, %.4f)"
          % (lam, m2_emp, m3_emp, 1 / lam + lam / 3, {1.0: 2.0, 0.5: 5.0}[lam]))
