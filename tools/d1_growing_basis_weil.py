#!/usr/bin/env python3
"""D1 probe (2026-08-25): adaptive growing-basis Weil-form separation.

Question (xdom-funcfield-2026-08-24.md, D1): does ANY basis that grows
adaptively with a world's own zero positions separate the RH world (true zeta)
from the RH-false controls (DH mod-5, planted-zero Beurling, Epstein cls-2)?

Weil explicit formula (even admissible h), zeta-normalization:
    W(h) = -log(pi) h(0)
           - sum_{p,m>=1} Lambda_w(p^m)/p^{m/2} [h(m log p) + h(-m log p)]
           + (1/2pi) int hhat(t) arch(t) dt,   arch(t) = Re Psi(1/4 + i t/2)
RH for world w  <=>  W_w(h) >= 0 for all admissible h.

Adaptive dictionary (the novel part vs wave-25's fixed wavelet grid): Gabor
packets h_j(x) = W_B(x) cos(gamma_j x), gamma_j = the world's OWN zero imaginary
parts, growing d = 16..256.  W_d[i,k] = W_w(h_i h_k).  The Archimedean term is
computed honestly via the truncated t-kernel
    A(x) = (1/2pi) int_0^{Tcut} cos(t x) arch(t) dt,   Tcut = 2*gamma_max + 30,
whose pairing with our packets (hhat compactly supported in t) is exact.
Baseline (fixed wavelet grid) = tools/wave25_schur_weil_probe.py, run separately.

Verdict rule (from D1): |lam_min(RH)|/|lam_min(control)| -> oo  =>  NEW LEVER /
gap falsified;  ratio stays ~ 1 at every d  =>  CONFIRMED non-separating
(sharpens the ledger closure to "universal across adaptive finite cuts").

Worlds:
  RH      : prime weights (log p)/p^{m/2};              tuned to true zeta zeros
  DH      : wave-25 char-mod-5 |c|<=1 weights (real);   tuned to DH's own zeros
  Beurling: Lambda_Z weights of Z=zeta*(1+c*2^-s);      tuned to zeta u planted zeros
  Epstein : wave-25-style |c|<=1 weights (real);        tuned to zeta(s;Q1),zeta(s;Q2) zeros
  (fake-Weil polynomial: no Dirichlet series / explicit formula -> not applicable
   to the Weil-form probe; its RH-falseness is already PROVEN exactly in model_weil.py)

Modes:
  own  : each world tuned to ITS OWN zeros (the D1 adaptive hypothesis)
  true : DH/Beurling tuned to the TRUE zeta zeros (separates "tuning" from "form")
"""
import math, sys, time
import numpy as np
import mpmath as mp

mp.mp.dps = 30
I = mp.mpc(0, 1)

sys.path.insert(0, 'tools/barrier_zoo')
from common import newton2d, dedupe_roots, grid_find_zeros, L_dirichlet  # noqa: E402

# ------------------------------------------------------------------ helpers

def sieve_to(n):
    if n < 2:
        return []
    s = bytearray(b'\x01') * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i*i::i] = b'\x00' * (((n - i*i) // i) + 1)
    return [i for i in range(2, n + 1) if s[i]]


def arch(t):
    return float(mp.digamma(mp.mpf('0.25') + I * mp.mpf(t) / 2).real)


def window(x, B, sigma=None):
    """Smooth Gabor window: Gaussian truncated at |x| <= B, =1 at 0."""
    if sigma is None:
        sigma = B / 3.5
    return np.where(np.abs(x) <= B, np.exp(-(x ** 2) / (2 * sigma ** 2)), 0.0)


# ------------------------------------------------------------------ world weights (Weil-form prime mass)

def weights_RH(xmax):
    out = {}
    for p in sieve_to(int(math.exp(xmax)) + 2):
        lp = math.log(p)
        w = lp / math.sqrt(p)
        m = 1
        while True:
            x = m * lp
            if x > xmax + 1e-9:
                break
            out[x] = w
            w /= math.sqrt(p)
            m += 1
    return out


def weights_DH(xmax):
    """wave-25 dh=True treatment: non-multiplicative |c(n)|<=1 real weights."""
    out = {}
    for p in sieve_to(int(math.exp(xmax)) + 2):
        lp = math.log(p)
        m = 1
        while True:
            x = m * lp
            if x > xmax + 1e-9:
                break
            out[x] = 1.0 / math.sqrt(p ** m)
            m += 1
    return out


def weights_beurling(xmax, c=2.0 ** 0.6):
    """Lambda_Z of Z(s) = zeta(s)*(1 + c*2^-s):  -Z'/Z = -zeta'/zeta - c ln2 2^-s/(1+c 2^-s)
    => Lambda_Z(2^m) = (-1)^{m+1} c^m ln2, standard for odd primes."""
    out = {}
    for p in sieve_to(int(math.exp(xmax)) + 2):
        lp = math.log(p)
        m = 1
        while True:
            x = m * lp
            if x > xmax + 1e-9:
                break
            if p == 2:
                out[x] = (-1) ** (m + 1) * c ** m * lp / math.sqrt(p ** m)
            else:
                out[x] = lp / math.sqrt(p ** m)
            m += 1
    return out


# ------------------------------------------------------------------ zero sets (adaptive tuning positions)

_ZETA_CACHE = '/tmp/d1_zeta_gammas.dat'
def zeta_gammas(gmax, nmax=400):
    """True zeta zero imaginary parts gamma_j <= gmax (mpmath-certified, cached)."""
    try:
        with open(_ZETA_CACHE) as f:
            cached = [float(x) for x in f.read().split()]
        return [g for g in cached if g <= gmax][:nmax]
    except OSError:
        pass
    dv = mp.mp.dps
    mp.mp.dps = 20
    out = []
    j = 1
    try:
        while j <= nmax:
            g = float(mp.im(mp.zetazero(j)))
            if g > gmax:
                break
            out.append(g)
            j += 1
    finally:
        mp.mp.dps = dv
    with open(_ZETA_CACHE, 'w') as f:
        f.write(' '.join(repr(g) for g in out))
    return out


def dh_gammas(gmax, t_hi=330.0, dt=0.5):
    """Zeros of f_plus(s)=L(s,psi)+eps*L(s,psibar): 1-D scan |f(1/2+it)|.
    Keeps coarse minima positions (to ~dt/2); Newton-refines only the deepest 20
    (certified to ~1e-6); the rest are 'candidate critical-line positions'."""
    from model_dh import build
    b = build()
    f = b['f_plus']
    dv = mp.mp.dps
    mp.mp.dps = 12
    try:
        ts = np.arange(0.5, t_hi, dt)
        mag = np.array([abs(f(mp.mpc(0.5, float(t)))) for t in ts])
    finally:
        mp.mp.dps = dv
    idx = [i for i in range(1, len(ts) - 1)
           if mag[i] < mag[i - 1] and mag[i] < mag[i + 1] and mag[i] < 0.2]
    out = [float(ts[i]) for i in idx]
    # refine the 20 deepest minima
    ranked = sorted(idx, key=lambda i: mag[i])[:20]
    mp.mp.dps = 20
    try:
        for i in ranked:
            z, err = newton2d(f, mp.mpc(0.5, float(ts[i])))
            if err < mp.mpf('1e-6') and mp.im(z) <= gmax and mp.im(z) > 1e-6:
                out.append(float(mp.im(z)))
    finally:
        mp.mp.dps = dv
    out = sorted(set(round(g, 3) for g in out))
    return [g for g in out if g <= gmax][:256]


def beurling_gammas(gmax, zeta_gs=None):
    if zeta_gs is None:
        zeta_gs = zeta_gammas(gmax)
    gs = list(zeta_gs)
    ln2 = math.log(2.0)
    k = 0
    while True:
        g = (math.pi + 2 * math.pi * k) / ln2
        if g > gmax:
            break
        gs.append(g)
        k += 1
    return sorted(set(round(g, 6) for g in gs))


def epstein_I_c(s, Q, N=40, L=8.0, steps=500):
    """Theta-Mellin integral I(s) for zeta(s;Q), COMPLEX-valued (for Newton)."""
    from model_epstein import dual_form
    a, b, c = Q
    absD = -(b * b - 4 * a * c)
    m = np.arange(-N, N + 1)[:, None]
    n = np.arange(-N, N + 1)[None, :]
    Qmn = a * m ** 2 + b * m * n + c * n ** 2
    Qd = dual_form(Q)
    ad, bd, cd = Qd
    Qst = ad * m ** 2 - bd * m * n + cd * n ** 2
    t = np.linspace(1.0, L, steps)
    e1 = np.exp(-np.pi * t[:, None, None] * Qmn[None, :, :]).sum(axis=(1, 2))
    e2 = np.exp(-(4 * np.pi / absD) * t[:, None, None] * Qst[None, :, :]).sum(axis=(1, 2))
    g1 = (e1 - 1.0) * t ** (s - 1)
    g2 = ((2 * t / np.sqrt(absD)) * e2 - 1.0) * t ** (-s - 1)
    return np.trapezoid(g1, t) + np.trapezoid(g2, t)   # complex


def epstein_gammas(t_hi=40.0, dt=1.0):
    """Zeros of zeta(s;Q1), zeta(s;Q2) (disc -20) via a fast 1-D line scan.
    Keeps coarse minima of |I(1/2+it)| as 'candidate critical-line positions'
    (to ~dt/2); the exact off-line zeros are already PROVEN in model_epstein.py."""
    from model_epstein import Q1, Q2
    out = []
    tv = np.arange(0.5, t_hi, dt)
    for Q in (Q1, Q2):
        mag = np.array([abs(epstein_I_c(mp.mpc(0.5, float(t)), Q)) for t in tv])
        for i in range(1, len(tv) - 1):
            if mag[i] < mag[i - 1] and mag[i] < mag[i + 1]:
                out.append(float(tv[i]))
    return sorted(set(round(g, 3) for g in out))[:64]


# ------------------------------------------------------------------ matrix assembly

def W_matrix(gammas, weights, B, verbose=False):
    """W_d[i,k] = W_w(h_i h_k), h_j(x) = window_B(x) cos(gamma_j x).
    Archimedean term via truncated kernel A(x); prime mass at exact points."""
    d = len(gammas)
    gmax = max(gammas)
    xmax = 2 * B
    # x-grid: resolve gamma_max (Nyquist x ~ pi/gmax), force a point at 0, cover [-xmax, xmax]
    overs = 4
    nx = int(2 * overs * xmax * gmax / math.pi)
    nx = max(nx, 2048)
    if nx % 2 == 0:
        nx += 1
    x = np.linspace(-xmax, xmax, nx)          # nx odd -> x=0 is a grid point
    dx = 2 * xmax / (nx - 1)
    # t-grid for the Arch kernel
    Tcut = 2 * gmax + 30.0
    dt_t = 0.1
    nt = int(Tcut / dt_t) + 1
    tv = np.linspace(0.0, Tcut, nt)
    archv = np.array([arch(t) for t in tv])
    # A(x) = (1/2pi) int_0^Tcut cos(t x) arch(t) dt   (trapezoid, accumulate over t)
    A = np.zeros(nx)
    wtt = np.ones(nt)
    wtt[0] = wtt[-1] = 0.5
    for l in range(nt):
        A += np.cos(tv[l] * x) * (wtt[l] * archv[l] * dt_t)
    A *= 0.5 / math.pi
    W = (A * dx)[None, :] * window(x, B) ** 2  # per-grid-point mass; f = h_i h_k = w^2 cos cos
    # rows/cols of cos factors
    H = np.cos(np.outer(gammas, x))            # (d, nx)
    Wmat = (H * W) @ H.T              # H diag(W) H^T: sum_q mass_q h_i(x_q) h_k(x_q)  (W is (1,nx))
    # prime mass at exact points (both signs)
    xs = sorted(weights.keys())
    xp = np.array([-xx for xx in xs] + xs)
    wp = np.array([-weights[xx] for xx in xs] + [-weights[xx] for xx in xs])
    Hp = np.cos(np.outer(gammas, xp)) * window(xp, B)[None, :] ** 1
    Wmat += (Hp * wp[None, :]) @ Hp.T
    # W prime = sum over prime points of (-w) h_i(xp) h_k(xp)  ->  Hp diag(-w) Hp^T
    # -log(pi) h(0), h_j(0)=1
    Wmat -= math.log(math.pi) * np.ones((d, d))
    lam = float(np.linalg.eigvalsh(Wmat)[0])
    return lam, Wmat


# ------------------------------------------------------------------ main

def run_worlds(B, dtargets, gammasets, weightsets, labels, mode):
    print(f"\n=== mode={mode}  B={B}  d-targets={dtargets} ===")
    print(f"{'world':>9} {'d':>4} {'lam_min':>12}  (sep ratio vs RH)")
    res = {}
    for lab, gs, ws in zip(labels, gammasets, weightsets):
        dcap = min(max(dtargets), len(gs))
        ds = [d for d in dtargets if d <= len(gs)]
        if not ds:
            ds = [len(gs)]
        row = []
        for d in ds:
            t0 = time.time()
            lam, _ = W_matrix(gs[:d], ws, B)
            row.append((d, lam))
            print(f"{lab:>9} {d:>4} {lam:>+12.6f}   ({time.time()-t0:.1f}s)")
        res[lab] = row
    # ratios vs RH at matching d
    rh = dict(res.get('RH', []))
    for lab in res:
        if lab == 'RH':
            continue
        for d, lam in res[lab]:
            if d in rh:
                r = abs(rh[d]) / max(abs(lam), 1e-12)
                print(f"  [sep] {lab} d={d}: |lam_min(RH)|/|lam_min({lab})| = {r:.4f}")
    return res


_CACHE = '/tmp/d1_gammas.dat'
def _load_gammas():
    try:
        with open(_CACHE) as f:
            return [line.split() for line in f.read().splitlines()]
    except OSError:
        return None

def _save_gammas(sets):
    with open(_CACHE, 'w') as f:
        f.write('\n'.join(' '.join(repr(g) for g in s) for s in sets))


def main():
    print("D1 probe: adaptive growing-basis Weil-form separation (2026-08-25)")
    t_start = time.time()
    Bs = [1.8, 2.5, 3.5]
    dtargets = [16, 32, 64, 128, 256]
    gmax = 450.0

    cached = _load_gammas()
    print("locating zero sets ...")
    if cached:
        g_rh, g_dh, g_be, g_ep = ([float(x) for x in line] for line in cached)
        print(f"  (loaded from cache: RH {len(g_rh)}, DH {len(g_dh)}, Beurling {len(g_be)}, Epstein {len(g_ep)})")
    else:
        g_rh = zeta_gammas(gmax)
        print(f"  RH: {len(g_rh)} zeta zeros (gamma<={gmax:.0f})  [{time.time()-t_start:.0f}s]")
        g_dh = dh_gammas(gmax)
        print(f"  DH: {len(g_dh)} zeros located  [{time.time()-t_start:.0f}s]")
        g_be = beurling_gammas(gmax, g_rh)
        print(f"  Beurling: {len(g_be)} zeros (zeta + planted)  [{time.time()-t_start:.0f}s]")
        g_ep = epstein_gammas()
        print(f"  Epstein: {len(g_ep)} zeros (t<40)  [{time.time()-t_start:.0f}s]")
        _save_gammas([g_rh, g_dh, g_be, g_ep])

    for B in Bs:
        w_rh = weights_RH(2 * B)
        w_dh = weights_DH(2 * B)
        w_be = weights_beurling(2 * B)
        # adaptive mode: each world tuned to its own zeros
        run_worlds(B, dtargets,
                   [g_rh, g_dh, g_be, g_ep],
                   [w_rh, w_dh, w_be, w_dh],
                   ['RH', 'DH', 'Beurling', 'Epstein'], 'own-zeros')
        # true-zeros mode: controls tuned to the TRUE zeta zeros
        run_worlds(B, dtargets,
                   [g_rh, g_rh, g_rh],
                   [w_rh, w_dh, w_be],
                   ['RH', 'DH', 'Beurling'], 'true-zeros')
    print(f"\ntotal {time.time()-t_start:.1f}s")


if __name__ == '__main__':
    main()
