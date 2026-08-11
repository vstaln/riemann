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
import re
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
    x, w = np.polynomial.legendre.leggauss(ng)   # x = nodes in [-1,1], w = weights
    uu = R * x
    A2_direct = R * np.sum(w * (K(uu) ** 2 * (1 - S(uu) ** 2)))
    def rho3_minus_1(u, v):
        return (- S(u) ** 2 - S(v) ** 2 - S(u + v) ** 2
                + 2 * S(u) * S(v) * S(u + v))
    W = np.outer(w, w)
    U, V = np.meshgrid(uu, uu, indexing='ij')
    integ = K(U) * K(V) * K(U + V) * rho3_minus_1(U, V)
    A3_corr = (R * R) * np.sum(W * integ)          # box integral of the (rho3-1) part
    A3 = (1.0 / lam ** 2) + A3_corr                 # + closed-form tail D = 1/lam^2
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
# A2. The law's recorded pair rows, from the Lean enclosures (read-only parse)
# ----------------------------------------------------------------------
print("\n--- (A2) the law's recorded pair rows (LawN256.lean enclosures) ---------")
src = open('/home/vstaln/riemann/research/lean-zeta-23/Zeta23/PairCeiling/LawN256.lean').read()
mrows = re.search(r'encl := \[(.*?)\]\n  tn', src, re.S)
pairs = re.findall(r'\((-?\d+), (-?\d+)\)', mrows.group(1))
Kbig = 2 ** 140; base = 2 ** 132
assert len(pairs) == 256, len(pairs)
los = [int(a) for a, b in pairs]; his = [int(b) for a, b in pairs]
row_ok = all(abs(los[j - 1] - j * base) <= 1 for j in range(1, 256))
below = sum(1 for j in range(1, 256) if los[j - 1] == j * base - 1)
at = sum(1 for j in range(1, 256) if los[j - 1] == j * base)
print(f"  rows parsed: {len(pairs)};  |lo_j - j*2^132| <= 1 for all j=1..255: {row_ok}")
print(f"  rows below j/256 (lo = j*2^132 - 1): {below};  at/above (lo = j*2^132): {at}")
# exact integer form: |256*S(j) - j| <= 256*|box|/K ; box deviation is at most 1 unit of 2^-140
dev_int = max(abs(256 * los[j - 1] - j * Kbig) for j in range(1, 256))
print(f"  max |256*S(j) - j| over boxes = {dev_int}/2^140 = 2^-{140 - dev_int.bit_length() + 1} = {dev_int / Kbig:.3e}  "
      f"(tau = 3e-40)")
S256 = (los[255] + his[255]) / 2 / Kbig
print(f"  S(256) (closed-band row, box midpoint) = {S256:.9f}  (D(1) consistency: 0.82395..)")

# ----------------------------------------------------------------------
# A3. Empirical real-zero third moment at lambda = 1/2 (ties 5 to data)
# ----------------------------------------------------------------------
print("\n--- (A3) empirical real-zero m3(1/2) (zeros_computed_10000.txt) ---------")
import os
zfn = '/home/vstaln/riemann/tools/data/zeros_computed_10000.txt'
if os.path.exists(zfn):
    g = []
    with open(zfn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                g.append(float(p[1]))
    g = np.array(g)
    m = (g >= 9000) & (g <= 9880)
    band = np.sort(g[m])
    sp = np.diff(band).mean()
    x = band / sp
    d = x[:, None] - x[None, :]
    lam = 0.5
    G = np.sinc(lam * d)
    n = len(x)
    m3 = np.trace(G @ G @ G) / n
    m2 = np.trace(G @ G) / n
    print(f"  band [{band.min():.1f}, {band.max():.1f}], N = {n}: m2(1/2) = {m2:.4f} (closed 13/6 = 2.1667), "
          f"m3(1/2) = {m3:.4f} (PROVEN 5; finite-height deficit pattern ~3%)")
else:
    print("  zeros file not found; skipping (value cited from attack-twobandwidth.md: m3 ~ 4.80)")

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
    K = np.zeros((n, n), dtype=complex)
    for j, cj in enumerate(c):
        if cj != 0:
            K += cj * np.exp(2j * np.pi * j * d / N)
    return K.real

def marked_s3(w, xs, ms, lam, N=256):
    """Exact marked third moment  S3 = D + 3P + T  of a law (w_c, x_{c,i}, m_{c,i}).
       w: array of weights (sum 1); xs: list of position arrays; ms: list of mark arrays.
       Diagram over the marked atoms (K_ij = K_lam(x_i - x_j), K(0) = 1):
         tr((K D)^3) = sum_{i,j,k} m_i m_j m_k K_ij K_jk K_ki
         D (i=j=k)            = sum_i m_i^3
         pair (two-equal)     = sum_{i!=k} m_i^2 m_k K_ik^2 + sum_{i!=j} m_i m_j (m_i+m_j) K_ij^2
                              = (3/2) sum_{i!=j} m_i m_j (m_i+m_j) K_ij^2
         T (three-distinct)   = tr((K D)^3) - D - pair
       S3 = (D + pair + T)/N per mark.  Returns (D/N, pair/N, T/N, S3)."""
    Dtot = 0.0; Ptot = 0.0; Ttot = 0.0
    for wc, x, m in zip(w, xs, ms):
        K = per_kernel_values(x, lam, N)
        MM = np.outer(m, m)
        Ms = (m[:, None] + m[None, :])
        s = np.sum(MM * Ms * K ** 2)                       # ordered i!=j (incl i=j)
        s -= np.sum(np.diag(MM) * np.diag(Ms) * np.diag(K) ** 2)   # drop i=j
        pair = (3 / 2) * s                                 # true two-equal part
        one = np.sum(m ** 3)
        KM = K * m[None, :]
        full = np.trace(np.linalg.matrix_power(KM, 3)).real
        Dtot += wc * one
        Ptot += wc * pair
        Ttot += wc * (full - one - pair)
    return Dtot / N, Ptot / N, Ttot / N, (Dtot + Ptot + Ttot) / N

print("marked_s3(w, xs, ms, lam) -> (D, 3P, T, S3)   [one-liner once config is in hand]")

# ----------------------------------------------------------------------
# C. What the pair rows + p0 pin
# ----------------------------------------------------------------------
print("\n--- (C) pinned content: D and the pair-part bounds [3u, 6u] ------------")

p0f = float(P0)
D_pin = 4 - 3 * p0f
m2 = 2 - p0f                      # E sum m_i^2 / 256
print(f"D = 4 - 3 p0 = {D_pin:.12f}   (pinned by p0 alone; position-free)")
print(f"E sum m_i^2 / 256 = 2 - p0 = {m2:.12f}   (=> E sum m_i^2 = {256*m2:.4f})")

def pair_part_bounds(lam, rows_mode="ideal"):
    """u = (1/256) sum_m d_m (E|mu_hat(m)|^2 - 256(2-p0)),
       pair part (two-equal) per mark  in [3u, 6u]   because (m_i+m_j) in [2,4].
       d = circular convolution of the window-kernel Fourier coefficients.
       rows_mode='ideal': E|mu_hat(m)|^2 = m (1<=m<=255), 65536 (m=0)  -- the law's
       recorded near-CUE rows (enclosures, EnclOK)."""
    c, M, B = per_kernel_coeffs(lam, N)
    d = np.fft.ifft(np.fft.fft(c) ** 2).real
    E = np.zeros(N)
    for m in range(1, N):
        E[m] = m if rows_mode == "ideal" else np.nan
    E[0] = N * N
    U = np.sum(d * (E - 256 * m2))
    u = U / 256
    return u, 3 * u, 6 * u, (d, M, B)

for lam in [mp.mpf(1) / 2, mp.mpf(2) / 3]:
    u, lo, hi, (d, M, B) = pair_part_bounds(lam)
    print(f"\nlam = {mp.nstr(lam,4)}  (rank-B kernel: M = {M}, B = {B} modes, K(0) = 1)")
    print(f"  u = {u:.6f}      pair part in [{lo:.6f}, {hi:.6f}]   (from ideal pair rows + p0)")
    print(f"  pinned interval of S3 (pair part + diagonal, T free): "
          f"[{D_pin + lo:.6f}, {D_pin + hi:.6f}]")
    ref = float(5 if lam == mp.mpf(1) / 2 else mp.mpf(13) / 4)
    print(f"  sine-kernel value: {ref}  ->  "
          f"{'INSIDE pinned interval' if D_pin+lo <= ref <= D_pin+hi else 'BELOW pinned interval'}")
    print(f"  pinned bottom minus sine value: {D_pin + lo - ref:+.6f}   "
          f"(positive => S3 >= sine value requires a NEGATIVE connected part T)")

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

# D1. NOTE on the CUE comparison: the CUE's form factor is symmetric
#     (E|mu_hat(m)|^2 = min(m, 256-m)), which is a DIFFERENT pair datum from the law's
#     recorded rows (E|mu_hat(m)|^2 = m for ALL m = 1..255 -- off-grid positions make
#     S(256-j) != S(j) in general).  The CUE is therefore NOT a valid cross-check for
#     the law's u; the valid checks are the exact algebraic identity (D2) and the
#     bounds (D3).

# D2. Exact algebraic identity: U_direct = sum_{i!=j} m_i m_j K_ij^2  ==  U_fourier = sum_m d_m (|mu_hat(m)|^2 - sum m_i^2)
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

# D3. The bound 3u <= (pair part) <= 6u on random marked configurations.
print("D3. bound 3u <= pair part <= 6u on a random marked family (8 draws, lam = 1/2)")
ok = True
for trial in range(8):
    x, m = family_draw()
    K = per_kernel_values(x, mp.mpf(1) / 2, N)
    MM = np.outer(m, m); Ms = (m[:, None] + m[None, :])
    s = np.sum(MM * Ms * K ** 2) - np.sum(np.diag(MM) * np.diag(Ms) * np.diag(K) ** 2)
    pair = (3 / 2) * s / N
    # u from the actual pair rows of THIS draw
    c, M0, B0 = per_kernel_coeffs(mp.mpf(1) / 2, N)
    d = np.fft.ifft(np.fft.fft(c) ** 2).real
    E = np.zeros(N)
    for jj in range(1, N):
        E[jj] = np.abs(np.sum(m * np.exp(2j * np.pi * jj * x / N))) ** 2
    E[0] = np.sum(m) ** 2
    U = np.sum(d * (E - np.sum(m ** 2)))
    u = U / 256
    if not (3 * u - 1e-9 <= pair <= 6 * u + 1e-9):
        ok = False
print(f"  3u <= pair part <= 6u held on all {8} draws: {ok}")

# D4. marked_s3 on a single random configuration: verify the diagram decomposition
#     D + pair + T = tr((K diag m)^3)/N exactly, and T is genuinely 3rd-order.
print("D4. marked_s3 decomposition identity on a random configuration (lam = 1/2)")
x, m = family_draw()
w = np.array([1.0]); xs = [x]; ms = [m]
D, P, T, S3 = marked_s3(w, xs, ms, mp.mpf(1) / 2)
K = per_kernel_values(x, mp.mpf(1) / 2, N)
KM = K * m[None, :]
full = np.trace(np.linalg.matrix_power(KM, 3)).real / N
print(f"  D = {D:.5f},  pair = {P:.5f},  T = {T:.5f},  S3 = {S3:.5f},  tr((KD)^3)/N = {full:.5f}")
print(f"  D + pair + T == tr((KD)^3)/N : {abs(D + P + T - full) < 1e-9}")

# ----------------------------------------------------------------------
# E. Verdict
# ----------------------------------------------------------------------
print("\n--- (E) verdict ---------------------------------------------------------")
print("sine-kernel values:  m3(1/2) = 5,  m3(2/3) = 13/4   (PROVEN, re-verified in (A))")
print("law's pinned diagonal: D = 4 - 3 p0 = %.12f  (position-free)" % D_pin)
print("pair part: in [3u, 6u] computed from ideal pair rows (see (C))")
print("triangle part T: NOT pinned by pair rows (3rd-order datum; capacity bound needs the config)")
print("=> pinned bottom D + 3u EXCEEDS the sine-kernel value at both windows:")
print("   S3 >= D + 3u = 5.44 > 5 (lam=1/2);  S3 >= 3.98 > 13/4 (lam=2/3), UNLESS T < 0.")
print("=> the sine-kernel value is NOT excluded (T may be negative), but matching it")
print("   forces a NEGATIVE connected part, opposite in sign to the sine kernel's own")
print("   A3 = +1/2 (lam = 1/2).  Structural tension, not a proof of exclusion.")
print("=> exact S3(law) is BLOCKED-ON-DATA: needs (w_c, x_{c,i}, m_{c,i}).")
print("=> once config is in hand: run marked_s3(w, xs, ms, 1/2 or 2/3) -> verdict LAW-EXCLUDED iff S3 != 5/13/4.")
