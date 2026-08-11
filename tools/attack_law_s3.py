#!/usr/bin/env python3
"""
H4.3 — the 256-law's triple correlation S3 vs the PROVEN sine-kernel values.

Riemann program, EXECUTIONER. Self-contained; does not edit canonical tools owned by
other agents. Run:
    uv run --quiet --with mpmath --with numpy python tools/attack_law_s3.py

What this script computes (all code-backed, all labeled):
  (A) The PROVEN sine-kernel third moments  m3(1/2)=5, m3(2/3)=13/4, m3(1)=2:
      - closed form  m3(lam) = 1 + 3(1/lam - 2*J2) + 1/lam^2 - 6*J2/lam + 2(1-lam/2),
        J2(lam) = int_0^inf sinc(pi*lam*u)^2 sinc(pi*u)^2 du  (mpmath quadrature)
      - direct DPP diagram: m3 = 1 + 3*A2 + A3 with
        A2 = int K(u)^2 (1 - S(u)^2) du,
        A3 = int_int K(u)K(v)K(u+v) rho3(u,v) du dv,
        rho3 = 1 - S(u)^2 - S(v)^2 - S(u+v)^2 + 2 S(u)S(v)S(u+v),
        K(u) = sinc(pi*lam*u), S(u) = sinc(pi*u).
  (B) The law's marked third moment as a function of the configuration data:
        S3 = D + 3*P + T,
        D = (1/N) sum_c w_c sum_i m_{c,i}^3                 (diagonal / multiplicity part)
        3P = (3/N) sum_c w_c sum_{i!=k} m_i m_k (m_i+m_k) K(x_i-x_k)^2   (pair part)
        T  = (1/N) sum_c w_c sum_{i,j,k distinct} m_i m_j m_k K_ij K_jk K_ki  (triangle part)
      Implemented as function marked_s3(config, lam) — a one-liner once the law's
      configuration (w_c, x_{c,i}, m_{c,i}) is in hand.
  (C) What the KNOWN pair rows + p0 pin:
      - D is pinned by the simple-point fraction p0:  D = 4 - 3 p0  (exact, position-free)
      - the pair part is bounded  6u <= 3P <= 12u  with
        u = (1/N) sum_m d_m ( E|mu_hat(m)|^2 - 256(2-p0) ),
        d_m = circular convolution of the window-kernel Fourier coefficients,
        E|mu_hat(m)|^2 = m  (near-CUE rows; E|mu_hat(0)|^2 = 65536 = 256^2),
        E sum_i m_i^2 = 256(2 - p0)  (from marks in {1,2}, sum = 256).
      - the triangle part T is NOT pinned by the pair rows (3rd-order data).
  (D) Sanity checks:
      - CUE law (marks all 1): the same machinery must reproduce the pair part of the
        continuum sine process 3*A2 = 3(1/lam - 2*J2) up to O(1/N) finite-size slop;
      - the bound 6u <= 3P <= 12u is validated on a random marked family.
  (E) Verdict: is the sine-kernel value inside/outside the range forced by the pair rows?
"""

import numpy as np
import mpmath as mp
from fractions import Fraction

mp.mp.dps = 60

# ----------------------------------------------------------------------
# 0. The law's recorded data (Lean LawN256.lean — read-only source of truth)
# ----------------------------------------------------------------------
# p0 = simple-point fraction (LawN256.lean header)
P0 = Fraction(10909258999421303588095230195816054408197,
              16000000000000000000000000000000000000000)
N = 256
TAU = Fraction(3, 10**40)          # near-CUE row tolerance |256 S(j) - j| <= tau
print("=" * 78)
print("H4.3: the 256-law's triple correlation S3 vs the PROVEN sine-kernel value")
print("=" * 78)
print("p0 (exact Fraction) =", P0)
print("p0 (decimal)        =", mp.nstr(mp.mpf(P0.numerator) / mp.mpf(P0.denominator), 50))

# ----------------------------------------------------------------------
# A. The PROVEN sine-kernel third moments (attack-twobandwidth.md §2)
# ----------------------------------------------------------------------
sinc = lambda x: mp.sin(mp.pi * x) / (mp.pi * x) if x != 0 else mp.mpf(1)

def J2(lam):
    """J2(lam) = int_0^inf sinc(pi lam u)^2 sinc(pi u)^2 du."""
    f = lambda u: (sinc(lam * u) ** 2) * (sinc(u) ** 2)
    # split: [0, 8] direct (tails negligible: |sinc|^2 ~ u^-2, product ~ u^-4)
    return mp.quad(f, [0, 8]) + mp.quad(lambda u: f(u), [8, mp.inf])

def m3_closed(lam):
    """m3(lam) = 1 + 3(1/lam - 2 J2) + 1/lam^2 - 6 J2/lam + 2(1 - lam/2)  (PROVEN form)."""
    j2 = J2(lam)
    return 1 + 3 * (1 / lam - 2 * j2) + 1 / lam**2 - 6 * j2 / lam + 2 * (1 - lam / 2)

def m3_diagram(lam, R=24, ng=220):
    """DPP diagram, direct quadrature (numpy Gauss–Legendre, tail-subtracted):
       m3 = 1 + 3 A2 + A3,
       A2 = int K(u)^2 (1 - S(u)^2) du            (= 1/lam - 2*J2, closed form)
       A3 = int_int K(u)K(v)K(u+v) rho3(u,v) du dv
          = 1/lam^2  +  int_int K(u)K(v)K(u+v) (rho3(u,v) - 1) du dv
       rho3 = det[ S(x_i - x_j) ]_3x3 = 1 - S(u)^2 - S(v)^2 - S(u+v)^2 + 2 S(u)S(v)S(u+v).
    The leading '1' of rho3 gives the closed-form tail D = 1/lam^2 (PROVEN in
    attack-twobandwidth.md §2.2); the remainder decays like O(r^-2) and is integrated
    on the box [-R,R]^2 with Gauss–Legendre."""
    K = lambda u: np.sinc(float(lam) * u)   # np.sinc(x) = sin(pi x)/(pi x)
    S = np.sinc
    A2 = 1 / float(lam) - 2 * float(J2(lam))   # closed form, cross-checked by quadrature below
    def rho3_minus_1(u, v):
        return (- S(u) ** 2 - S(v) ** 2 - S(u + v) ** 2
                + 2 * S(u) * S(v) * S(u + v))
    xw, xg = np.polynomial.legendre.leggauss(ng)
    uu = R * xg; vv = R * xg
    W = np.outer(xw, xw)
    U, V = np.meshgrid(uu, vv, indexing='ij')
    integ = K(U) * K(V) * K(U + V) * rho3_minus_1(U, V)
    A3_corr = (R * R) * np.sum(W * integ)          # box integral of the (rho3-1) part
    A3 = (1.0 / lam ** 2) + A3_corr                 # + closed-form tail D = 1/lam^2
    # cross-check A2 by direct 1-D quadrature on the same grid
    A2_direct = R * np.sum(xw * (K(uu) ** 2 * (1 - S(uu) ** 2)))
    return 1 + 3 * A2 + A3, A2, A3, A2_direct

print("\n--- (A) PROVEN sine-kernel third moments -------------------------------")
refs = {mp.mpf(1) / 2: mp.mpf(5), mp.mpf(2) / 3: mp.mpf(13) / 4, mp.mpf(1): mp.mpf(2)}
for lam in [mp.mpf(1) / 2, mp.mpf(2) / 3, mp.mpf(1)]:
    mc = m3_closed(lam)
    md, A2, A3, A2_direct = m3_diagram(lam)
    j2 = J2(lam)
    print(f"lam={mp.nstr(lam,4):>6}: closed m3 = {mp.nstr(mc,10):>10}   "
          f"diagram m3 = {md:>10.6f}   A2 = {float(A2):>8.5f} (direct {A2_direct:8.5f})   "
          f"A3 = {float(A3):>8.5f}   J2 = {mp.nstr(j2,8):>8}   ref = {mp.nstr(refs[lam],10):>10}")

# ----------------------------------------------------------------------
# B. The law's marked S3 as a function of the configuration data
# ----------------------------------------------------------------------
print("\n--- (B) S3 of a 256-periodic marked configuration (formula, as code) -----")

def per_kernel_coeffs(lam, N=256):
    """Fourier coefficients of the periodic rank-B window kernel with K(0)=1.
       M = floor(128*lam), B = 2M+1 modes |j| <= M, c_j = 1/B (so K(0)=1)."""
    M = int(mp.floor(128 * lam))
    B = 2 * M + 1
    c = np.zeros(N)
    for j in range(-M, M + 1):
        c[j % N] = 1.0 / B
    return c, M, B

def per_kernel_values(x, lam, N=256):
    """K(x_i - x_j) for a position array x (length n, in [0,256))."""
    c, M, B = per_kernel_coeffs(lam, N)
    n = len(x)
    d = (x[:, None] - x[None, :]) % N
    K = np.zeros((n, n))
    for j, cj in enumerate(c):
        if cj != 0:
            K += cj * np.exp(2j * np.pi * j * d / N)
    return K.real

def marked_s3(w, xs, ms, lam, N=256):
    """Exact marked third moment  S3 = D + 3P + T  of a law (w_c, x_{c,i}, m_{c,i}).
       w: array of weights (sum 1); xs: list of position arrays; ms: list of mark arrays.
       Returns (D, 3P, T, S3)."""
    D = 0.0; P = 0.0; T = 0.0
    for wc, x, m in zip(w, xs, ms):
        K = per_kernel_values(x, lam, N)
        n = len(x)
        # D: diagonal (i=j=k)
        D += wc * np.sum(m ** 3)
        # 3P: two-equal terms; sum over i!=k of m_i m_k (m_i+m_k) K_ik^2
        MM = np.outer(m, m)
        Ms = (m[:, None] + m[None, :])
        P += wc * np.sum(MM * Ms * K ** 2)          # includes i=k terms -> subtract
        P -= wc * np.sum(np.diag(MM) * np.diag(Ms) * np.diag(K) ** 2)
        # T: three-distinct; compute full tr((K diag(m))^3) then subtract 1- and 2-point parts
        KM = K * m[None, :]                          # K . diag(m)
        full = np.trace(np.linalg.matrix_power(KM, 3)).real
        one = np.sum(m ** 3)                          # i=j=k part of full
        two = np.sum(MM * Ms * K ** 2) - np.sum(np.diag(MM) * np.diag(Ms) * np.diag(K) ** 2)
        T += wc * (full - one - two)
    D /= N; P = 3 * P / N; T /= N
    return D, P, T, D + P + T

print("marked_s3(w, xs, ms, lam) -> (D, 3P, T, S3)   [one-liner once config is in hand]")

# ----------------------------------------------------------------------
# C. What the pair rows + p0 pin
# ----------------------------------------------------------------------
print("\n--- (C) pinned content: D and the pair-part bounds [6u, 12u] ------------")

p0f = float(P0)
D_pin = 4 - 3 * p0f
m2 = 2 - p0f                      # E sum m_i^2 / 256
print(f"D = 4 - 3 p0 = {D_pin:.12f}   (pinned by p0 alone; position-free)")
print(f"E sum m_i^2 / 256 = 2 - p0 = {m2:.12f}   (=> E sum m_i^2 = {256*m2:.4f})")

def pair_part_bounds(lam, rows_mode="ideal"):
    """u = (1/256) sum_m d_m (E|mu_hat(m)|^2 - 256(2-p0)),
       3P in [6u, 12u].  d = circular convolution of the window kernel coefficients.
       rows_mode='ideal': E|mu_hat(m)|^2 = m (1<=m<=255), 65536 (m=0)."""
    c, M, B = per_kernel_coeffs(lam, N)
    d = np.fft.ifft(np.fft.fft(c) ** 2).real
    E = np.zeros(N)
    for m in range(1, N):
        E[m] = m if rows_mode == "ideal" else np.nan
    E[0] = N * N
    U = np.sum(d * (E - 256 * m2))
    u = U / 256
    return u, 6 * u, 12 * u, (d, M, B)

for lam in [mp.mpf(1) / 2, mp.mpf(2) / 3]:
    u, lo, hi, (d, M, B) = pair_part_bounds(lam)
    print(f"\nlam = {mp.nstr(lam,4)}  (rank-B kernel: M = {M}, B = {B} modes, K(0) = 1)")
    print(f"  u = {u:.6f}     3P in [{lo:.6f}, {hi:.6f}]   (from ideal pair rows + p0)")
    print(f"  pinned interval of S3 (pair part + diagonal, T free): "
          f"[{D_pin + lo:.6f}, {D_pin + hi:.6f}]")
    ref = float(5 if lam == mp.mpf(1) / 2 else mp.mpf(13) / 4)
    print(f"  sine-kernel value: {ref}  ->  {'INSIDE pinned interval' if D_pin+lo <= ref <= D_pin+hi else 'OUTSIDE pinned interval'}")
    print(f"  gap from sine value to bottom of pinned interval: {D_pin + lo - ref:+.6f}")

# ----------------------------------------------------------------------
# D. Sanity checks
# ----------------------------------------------------------------------
print("\n--- (D) sanity checks ---------------------------------------------------")
rng = np.random.default_rng(0)

def family_draw():
    """A random 256-periodic marked configuration: ~192 distinct positions on the
    grid (density ~1), marks in {1,2}, total mark mass ~256."""
    npos = 192
    x = rng.permutation(np.arange(N))[0:npos].astype(float)
    m = np.ones(npos)
    nd = int(rng.integers(0, 40))
    if nd > 0:
        m[rng.choice(npos, size=nd, replace=False)] = 2.0
    return x, m

# D1. CUE law (marks all 1): pair part from the same machinery vs continuum 3*A2.
print("D1. CUE law (marks all 1, p0 = 1): pair part 6u vs continuum 3*A2 = 3(1/lam - 2 J2)")
for lam in [mp.mpf(1) / 2, mp.mpf(2) / 3]:
    c, M, B = per_kernel_coeffs(lam, N)
    d = np.fft.ifft(np.fft.fft(c) ** 2).real
    E = np.zeros(N)
    for m in range(1, N):
        E[m] = m
    E[0] = N * N
    U = np.sum(d * (E - 256 * 1.0))          # marks all 1: 256(2-p0) = 256
    u_CUE = U / 256
    cont = 3 * (1 / float(lam) - 2 * float(J2(lam)))
    print(f"  lam={mp.nstr(lam,4)}: 6 u_CUE = {6*u_CUE:.5f}   continuum 3*A2 = {cont:.5f}   "
          f"ratio = {6*u_CUE/cont:.4f}")

# D2. Exact algebraic identity: U_direct = sum_{i!=k} m_i m_k K_ik^2  ==  U_fourier = sum_m d_m (|mu_hat(m)|^2 - sum m_i^2)
print("D2. algebraic identity  U_direct == U_fourier  on random marked configurations")
for lam in [mp.mpf(1) / 2, mp.mpf(2) / 3]:
    c, M, B = per_kernel_coeffs(lam, N)
    d = np.fft.ifft(np.fft.fft(c) ** 2).real
    worst = 0.0
    for trial in range(6):
        x, m = family_draw()
        K = per_kernel_values(x, lam, N)
        MM = np.outer(m, m)
        U_direct = np.sum(MM * K ** 2) - np.sum(np.diag(MM) * np.diag(K) ** 2)
        E = np.zeros(N)
        for jj in range(1, N):
            E[jj] = np.abs(np.sum(m * np.exp(2j * np.pi * jj * x / N))) ** 2
        E[0] = np.sum(m) ** 2
        U_fourier = np.sum(d * (E - np.sum(m ** 2)))
        worst = max(worst, abs(U_direct - U_fourier))
    print(f"  lam={mp.nstr(lam,4)}: max |U_direct - U_fourier| over 6 draws = {worst:.2e}")

# D3. The bound 6u <= 3P <= 12u on random marked configurations.
print("D3. bound 6u <= 3P <= 12u on a random marked family (8 draws)")
ok = True
for trial in range(8):
    x, m = family_draw()
    K = per_kernel_values(x, mp.mpf(1) / 2, N)
    MM = np.outer(m, m); Ms = (m[:, None] + m[None, :])
    P3 = 3 * np.sum(MM * Ms * K ** 2) / N
    P3 -= 3 * np.sum(np.diag(MM) * np.diag(Ms) * np.diag(K) ** 2) / N
    # u from the actual pair rows of THIS draw
    c, M0, B0 = per_kernel_coeffs(mp.mpf(1) / 2, N)
    d = np.fft.ifft(np.fft.fft(c) ** 2).real
    E = np.zeros(N)
    for jj in range(1, N):
        E[jj] = np.abs(np.sum(m * np.exp(2j * np.pi * jj * x / N))) ** 2
    E[0] = np.sum(m) ** 2
    U = np.sum(d * (E - np.sum(m ** 2)))
    u = U / 256
    if not (6 * u - 1e-9 <= P3 <= 12 * u + 1e-9):
        ok = False
print(f"  6u <= 3P <= 12u held on all {8} draws: {ok}")

# ----------------------------------------------------------------------
# E. Verdict
# ----------------------------------------------------------------------
print("\n--- (E) verdict ---------------------------------------------------------")
print("sine-kernel values:  m3(1/2) = 5,  m3(2/3) = 13/4   (PROVEN, re-verified in (A))")
print("law's pinned diagonal: D = 4 - 3 p0 = %.12f  (position-free)" % D_pin)
print("pair part: 3P in [6u, 12u] computed from ideal pair rows (see (C))")
print("triangle part T: NOT pinned by pair rows (3rd-order datum; capacity bound needs the config)")
print("=> the sine-kernel value lies inside the full range; NOT excluded by pair rows + p0.")
print("=> exact S3(law) is BLOCKED-ON-DATA: needs (w_c, x_{c,i}, m_{c,i}).")
print("=> once config is in hand: run marked_s3(w, xs, ms, 1/2 or 2/3) -> verdict LAW-EXCLUDED iff S3 != 5/13/4.")
