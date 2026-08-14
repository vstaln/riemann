"""Shared helpers for tools/barrier_zoo/ (rung-0 barrier checker).

Each model module is self-contained:
    uv run --quiet --with numpy python3 tools/barrier_zoo/model_dh.py
Full zoo + classifier battery:
    uv run --quiet --with numpy python3 tools/barrier_zoo/run_all.py
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 40
I = mp.mpc(0, 1)


def L_dirichlet(s, chi):
    """Dirichlet L-function via Hurwitz zeta (exact continuation for all s):
    L(s,chi) = q^-s * sum_{a=1..q-1} chi(a) * zeta(s, a/q)."""
    q = len(chi)
    tot = mp.mpc(0, 0)
    for a in range(q):
        if chi[a] != 0:
            tot += chi[a] * mp.zeta(s, mp.mpf(a) / q)
    return tot * mp.power(q, -s)


def gauss_sum(chi):
    q = len(chi)
    return sum(chi[a] * mp.e**(2 * I * mp.pi * a / q) for a in range(q))


def newton2d(f, z0, tol=mp.mpf('1e-14'), maxit=60):
    """Newton in the complex plane with central-difference derivative. Returns (root, |f(root)|)."""
    z = z0
    for _ in range(maxit):
        fz = f(z)
        h = mp.mpf('1e-8') * (1 + mp.fabs(z))
        df = (f(z + h * I) - f(z - h * I)) / (2 * h * I)
        if df == 0:
            break
        dz = fz / df
        z = z - dz
        if mp.fabs(dz) < tol * (1 + mp.fabs(z)):
            break
    return z, mp.fabs(f(z))


def grid_find_zeros(fn, sigma_lo=0.02, sigma_hi=0.98, t_lo=0.0, t_hi=40.0,
                    ds=0.05, dt=0.5, rel_thresh=0.3):
    """Coarse grid search for isolated zeros; returns candidate complex starting points."""
    sigmas = np.arange(sigma_lo, sigma_hi + 1e-9, ds)
    ts = np.arange(t_lo, t_hi + 1e-9, dt)
    mag = np.empty((len(sigmas), len(ts)))
    for i, s in enumerate(sigmas):
        for j, t in enumerate(ts):
            mag[i, j] = abs(fn(complex(s, t)))
    cands = []
    for i in range(1, len(sigmas) - 1):
        for j in range(1, len(ts) - 1):
            v = mag[i, j]
            if v < rel_thresh * min(mag[i-1, j], mag[i+1, j], mag[i, j-1], mag[i, j+1]) and v < 0.5:
                cands.append(complex(sigmas[i], ts[j]))
    return cands


def dedupe_roots(roots, gap=mp.mpf('1e-4')):
    out = []
    for r in sorted(roots, key=lambda z: (mp.im(z), mp.re(z))):
        if all(mp.fabs(r - o) > gap for o in out):
            out.append(r)
    return out


def find_offline_zeros(f, label, sigma_line=0.5, t_hi=40.0):
    """Grid-search + Newton-refine; returns zeros with |Re(s) - sigma_line| > 1e-5 (off the line).
    Search at low dps, certify at high dps."""
    mp.mp.dps = 20
    try:
        cands = grid_find_zeros(f, t_hi=t_hi)
    finally:
        mp.mp.dps = 40
    roots = []
    for z0 in cands:
        z, err = newton2d(f, mp.mpc(z0))
        if err < mp.mpf('1e-9'):
            roots.append(z)
    roots = dedupe_roots(roots)
    offline = [z for z in roots if mp.fabs(mp.re(z) - sigma_line) > mp.mpf('1e-5')]
    print(f"[{label}] zeros located: {len(roots)}, off-line: {len(offline)}")
    for z in sorted(offline, key=lambda z: mp.im(z))[:12]:
        print(f"    off-line zero: s = {mp.nstr(mp.re(z), 9)} + i*{mp.nstr(mp.im(z), 9)}"
              f"   |f(s)| = {mp.nstr(abs(f(z)), 8)}")
    return offline
