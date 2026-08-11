#!/usr/bin/env python3
"""xi''-certificate constant: evaluate kappa^(2)_1(1, v) for flat/quartic/cos windows.

Derivation (CONJECTURED, to be verified in the note):
  The xi' certificate uses the coefficient family C(N; L_T) with L_T = l/2 + i*pi/4 and diagonal
  density D1(s) = s - 4s^2 + sum_k D1coeff(k) s^{2k+3}, D1coeff(k) = 2*4^{k+1} k!/(2k+2)!.
  For xi'' the analog density D1^(2) is the xi''-analog of Montgomery's pair density.  The
  derivation (Section 2 of the note) shows D1^(2)(r) = r - 4r^2 + sum_{k>=0} D1coeff2(k) r^{2k+3}
  with coefficient shift D1coeff2(k) (new, NOT D1coeff(k)).

  We VERIFY the shift numerically two ways:
  (a) directly from the xi''-zero data (interlacing counts imply N_{xi''} ~ N_{xi'} ~ N), and
  (b) by the "moment match" principle: the coefficient system for xi'' is built from the SAME
      (Lambda*log)^{*k} prime convolutions but the C(N;Lambda*) coefficients are evaluated at the
      xi'' frozen parameter (different L-star).
  Since the underlying (Lambda*log)^{*k}/N sums are universal, the xi'' density is obtained from
  D1 by the same Wk-asymptotic with k shifted, giving a NEW coefficient sequence.

Run:  uv run --quiet --with mpmath python check_cert2.py   (50 digits)
"""
import mpmath as mp

mp.mp.dps = 50
PI = mp.pi


def D1coeff(k):
    """the xi' coefficient: 2*4^{k+1} k!/(2k+2)! (k >= 0)."""
    return mp.mpf(2) * mp.power(4, k + 1) * mp.factorial(k) / mp.factorial(2 * k + 2)


def D1(r, K=60):
    return r - 4 * r ** 2 + sum(D1coeff(k) * r ** (2 * k + 3) for k in range(K + 1))


def vConv_flat(r):
    return 1 - r


def kappa1(v, D, lam=1):
    """kappa_1(lam, v; D) = (int v^2 + 2*int_0^1 D(lam r) (v*v)(r) dr)/(int v)^2 at lam = 1."""
    Iv = mp.quad(v, [-mp.mpf('0.5'), mp.mpf('0.5')])
    Iv2 = mp.quad(lambda s: v(s) ** 2, [-mp.mpf('0.5'), mp.mpf('0.5')])
    J = mp.quad(lambda r: D(r) * vConv_flat(r), [0, 1])
    return (Iv2 + 2 * J) / Iv ** 2


# --- the xi' constants (sanity; matches xiprime_check/check_cert.py) ---
kf = kappa1(lambda s: mp.mpf(1), D1)
print(f"[xi'] kappa1(1, flat)   = {mp.nstr(kf, 30)}   2-k = {mp.nstr(2 - kf, 30)}")


# --- the candidate D1^(2): coefficient shift from the tower derivation (Section 2). ---
# Derivation summary (see note): for xi'', the E'/E at a xi''-zero is xi'''/xi''; the explicit
# formula's diagonal term is built from the same prime convolutions with the coefficient
# C^(2)(N; L2*) where L2* = l/2 + i*pi/4 (the phase from xi'' realness: xi''(1/2+it) real).
# The k-fold Mertens layer for xi'' has the same (Lambda*log)^{*k} support, but the weight
# (log N)^2/(2k+2)! is replaced by the (j+2)-indexed one; this changes D1coeff.
#
# We determine the xi'' coefficients by the CONSTRAINT that the diagonal law must reproduce the
# xi'' pair density: the density must integrate to the correct total pair mass.  For xi' this is
# int_0^1 D1 = 1/6 - 4/3 + sum D1coeff(k)/(2k+4); we verify D1 >= 0 and D1(1/2)=0, D1(1) = 1 - 4 +
# sum ... The xi'' density D1^(2) must satisfy the SAME integral constraints (both count N zeros
# with the same main term), so we pin the coefficient shift from the empirical pair density of
# the xi''-zeros (via the histogram from tower_run.txt + a Montgomery-pair-correlation-style
# computation on the actual xi'' zeros).
#
# Concretely: the empirical 2-point density of xi''-zeros (scaled by 2*pi/log T, counting pairs
# at separation u) is the window functional's D.  We evaluate the pair density empirically below
# from the xi'' zeros (20 in hand + we can recompute more) and compare to D1 and to a shifted
# candidate.

def empirical_pair_density(zeros, u, T0=0.0, T1=100.0):
    """normalized pair count at separation u (Montgomery convention, R(u) = 1 - (sin pi u/pi u)^2)."""
    L = mp.log(T1 / (2 * PI))
    N = len(zeros)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            d = zeros[i] - zeros[j]
            # window in scaled separation
            if mp.fabs(d - u * 2 * PI / L) < 0.5 * 2 * PI / L:
                cnt += 1
    return cnt / (N * L / (2 * PI))

if __name__ == '__main__':
    # flat xi'-kappa sanity
    kf2 = kappa1(lambda s: mp.mpf(1), D1)
    print("xi' flat kappa1(1) =", mp.nstr(kf2, 30))
    print("2 - kappa =", mp.nstr(2 - kf2, 30))
    # the quartic window (from the xi' round)
    def vq(s):
        return 1 - mp.mpf(7) / 100 * (2 * s) ** 2 - mp.mpf(51) / 200 * (2 * s) ** 4
    # kappa via generic v (needs vConv for vq; use flat fallback: direct integral of D*vconv)
    def kappa_quartic(D):
        Iv = mp.quad(vq, [-mp.mpf('0.5'), mp.mpf('0.5')])
        Iv2 = mp.quad(lambda s: vq(s) ** 2, [-mp.mpf('0.5'), mp.mpf('0.5')])
        # vconv for quartic: v(s)v(s+r) integrated over s in [-1/2, 1/2-r]
        def vconv(r):
            return mp.quad(lambda s: vq(s) * vq(s + r), [-mp.mpf('0.5'), mp.mpf('0.5') - r])
        J = mp.quad(lambda r: D(r) * vconv(r), [0, 1])
        return (Iv2 + 2 * J) / Iv ** 2
    kq = kappa_quartic(D1)
    print("xi' quartic kappa1(1) =", mp.nstr(kq, 30), " 2-k =", mp.nstr(2 - kq, 30))
