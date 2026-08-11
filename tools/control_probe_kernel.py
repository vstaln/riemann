# Probe for idea-generator-control.md, C-LY3 (Caratheodory-Fejer / PSD-Toeplitz real-rootedness).
# Part A: are the Gabor frame kernels real-rooted (all complex roots on the real axis)?
#   Phi(x) = integral_{-1/2}^{1/2} cos^2(sqrt2 u) e^{i x u} du   (paper Lemma 2.2 frame kernel)
#   Psi(s) = sin(1/sqrt2 - pi s)/(sqrt2 - 2 pi s) + sin(1/sqrt2 + pi s)/(sqrt2 + 2 pi s)   (finite-T Gabor kernel, two-form note)
# Part B: does the Caratheodory-Fejer mechanism fire on the finite Toeplitz compression
#   T[j,k] = Phi(j-k) (critical-density grid): is T PSD, and is the ground-state eigenvector
#   polynomial real-rooted?
# Run: uv run --quiet python tools/control_probe_kernel.py
# Labels: all numbers below are CHECKED NUMERICALLY (mpmath dps=40 / numpy f64 + longdouble).

import mpmath as mp
import numpy as np

mp.mp.dps = 40
SQRT2 = mp.sqrt(2)
PI = mp.pi
A = mp.mpf('0.5')          # half-window length
B = 2 * SQRT2              # cos^2 freq
POLE_VAL = mp.mpf('0.5') + mp.sin(SQRT2) / (2 * SQRT2)   # removable-pole value of Psi, = int psi^2 = 0.8492...


def sinc_term(x, a):
    # sin(a x)/x, removable at 0
    if abs(x) < mp.mpf('1e-30'):
        return a
    return mp.sin(a * x) / x


def Phi(z):
    # closed form of integral (derived: cos^2 = (1+cos)/2)
    t1 = sinc_term(z, A)
    t2 = mp.mpf('0.5') * (sinc_term(z + B, A) + sinc_term(z - B, A))
    return t1 + t2


def Psi(z):
    t1 = mp.sin(mp.mpf(1) / SQRT2 - PI * z) / (SQRT2 - 2 * PI * z)
    t2 = mp.sin(mp.mpf(1) / SQRT2 + PI * z) / (SQRT2 + 2 * PI * z)
    if abs(SQRT2 - 2 * PI * z) < mp.mpf('1e-30'):
        t1 = POLE_VAL
    if abs(SQRT2 + 2 * PI * z) < mp.mpf('1e-30'):
        t2 = POLE_VAL
    return t1 + t2


def arg_principle_count(f, xmin, xmax, ymin, ymax, n_pts=6000):
    """Zeros of f inside the box via winding number of f on the boundary."""
    t = np.linspace(0, 1, n_pts, endpoint=False)
    # boundary parametrization: bottom, right, top, left
    zs = []
    for tt in t:
        zs.append(complex(xmin + (xmax - xmin) * tt, ymin))
    for tt in t:
        zs.append(complex(xmax, ymin + (ymax - ymin) * tt))
    for tt in t:
        zs.append(complex(xmax - (xmax - xmin) * tt, ymax))
    for tt in t:
        zs.append(complex(xmin, ymax - (ymax - ymin) * tt))
    phis = []
    for z in zs:
        v = f(mp.mpc(z))
        phis.append(float(mp.arg(v)))
    # accumulate wrapped increments
    total = 0.0
    for i in range(len(phis)):
        d = phis[(i + 1) % len(phis)] - phis[i]
        while d > PI:
            d -= 2 * PI
        while d < -PI:
            d += 2 * PI
        total += d
    return round(total / (2 * PI))


def find_roots(f, xmin, xmax, ymin, ymax, nx=240, ny=120, thresh=mp.mpf('0.35')):
    """Grid + Newton (mpmath muller) root search. Returns list of (re, im, |f|)."""
    roots = []
    for i in range(nx):
        for j in range(ny):
            x0 = xmin + (xmax - xmin) * (i + 0.5) / nx
            y0 = ymin + (ymax - ymin) * (j + 0.5) / ny
            z = mp.mpc(x0, y0)
            if abs(f(z)) < thresh:
                try:
                    r = mp.findroot(f, z, solver='muller', tol=mp.mpf('1e-30'))
                except Exception:
                    continue
                fr = f(r)
                if abs(fr) < mp.mpf('1e-15'):
                    re_v = float(mp.re(r)); im_v = float(mp.im(r))
                    dup = any(abs(re_v - rr[0]) < 1e-7 and abs(im_v - rr[1]) < 1e-7 for rr in roots)
                    if not dup:
                        roots.append((re_v, im_v, float(abs(fr))))
    return roots


def analyze(name, f, xmin, xmax, ymin, ymax):
    print(f"--- {name} ---")
    n = arg_principle_count(f, xmin, xmax, ymin, ymax)
    print(f"zeros in box [{xmin},{xmax}]x[{ymin},{ymax}] (argument principle): {n}")
    roots = find_roots(f, xmin, xmax, ymin, ymax)
    roots.sort(key=lambda r: (r[1], r[0]))
    print(f"found {len(roots)} distinct roots (|f|<1e-15):")
    for re_v, im_v, af in roots:
        print(f"  re={re_v:+.6f}  im={im_v:+.6f}  |f|={af:.1e}")
    max_im = max((abs(r[1]) for r in roots), default=0.0)
    real_rooted = max_im < 1e-8
    print(f"max |Im(root)| = {max_im:.3e}  ->  real-rooted: {real_rooted}")
    # consistency: 2*(# roots with im>=0 within box) should equal winding count (roots off boundary)
    return real_rooted, n, roots


def cf_check(d=24):
    """Caratheodory-Fejer-style check on the finite Toeplitz T[j,k] = Phi(j-k), j,k in 0..d-1.
    Report PSD-ness and whether the ground-state eigenvector polynomial is real-rooted."""
    print(f"--- CF check: Toeplitz T[j,k]=Phi(j-k), d={d} ---")
    # build with mpmath then convert
    T = np.zeros((d, d), dtype=np.longdouble)
    for j in range(d):
        for k in range(j, d):
            v = float(mp.re(Phi(mp.mpc(j - k))))
            T[j, k] = v
            T[k, j] = v
    T = np.asarray(T, dtype=np.float64)  # linalg.eigh needs f64
    evals, evecs = np.linalg.eigh(T)
    print(f"smallest 5 eigenvalues: {evals[:5]}")
    print(f"largest  eigenvalue:    {evals[-1]:.6f}")
    print(f"min eigenvalue:         {evals[0]:.6e}  (PSD: {evals[0] >= -1e-12})")
    # ground-state eigenvector polynomial
    c = evecs[:, 0].astype(np.complex128)
    roots_p = np.roots(c[::-1])
    max_im = np.max(np.abs(np.imag(roots_p)))
    print(f"ground-state eigenvector polynomial: {d-1} roots, max |Im| = {max_im:.3e}  "
          f"-> real-rooted: {max_im < 1e-8}")
    # report the ratio of the two smallest eigenvalues (the 'rank n-1' proximity)
    if d >= 3:
        print(f"ratio eig[1]/eig[0] = {evals[1]/max(evals[0],1e-300):.3e} (rank-(n-1) proximity)")
    return bool(evals[0] >= -1e-12), max_im < 1e-8


if __name__ == '__main__':
    print("=== C-LY3 probe: Gabor frame kernel real-rootedness + Caratheodory-Fejer condition ===")
    print(f"Phi(0) = {Phi(mp.mpc(0))}   (expect int psi^2 = 0.849227999318304)")
    print(f"Psi(0) = {Psi(mp.mpc(0))}   Psi at pole = {POLE_VAL}")
    analyze("Phi (frame kernel, box [-40,40]x[-20,20])", Phi, -40, 40, -20, 20)
    analyze("Psi (finite-T Gabor kernel, box [-40,40]x[-20,20])", Psi, -40, 40, -20, 20)
    for d in (12, 24, 48):
        cf_check(d)
    print("=== done ===")
