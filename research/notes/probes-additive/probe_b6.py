import numpy as np
from scipy.integrate import quad

def gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def J2(la):
    v, _ = quad(lambda u: np.sinc(la*u)**2*np.sinc(u)**2, 0, np.inf, limit=400)
    return v

def B_fast(R, la, n):
    """B = intint K(u)K(v)K(u+v) S(u)^2 dudv, direct on [-R,R]^2 (u-fast only)."""
    x, w = gl(n)
    xs = R*x; ws = R*w
    uu, vv = np.meshgrid(xs, xs, indexing='ij')
    ww = uu+vv
    f = np.sinc(la*uu)*np.sinc(la*vv)*np.sinc(la*ww)*np.sinc(uu)**2
    return float(np.sum(f * np.outer(ws, ws)))

print("A3 = 1/la^2 - 3B + 2(1-la/2)   (B numeric, D and 2C analytic); m3 = 1 + 3A2 + A3:")
for la in (1.0,):
    A2 = 1/la - 2*J2(la)
    A3_closed = 1/la**2 - (6/la)*J2(la) + 2*(1-la/2)
    dirs = []
    for (R, n) in ((120, 1200), (240, 2400)):
        A3 = 1/la**2 - 3*B_fast(R, la, n) + 2*(1-la/2)
        dirs.append(1 + 3*A2 + A3)
    tgt = {0.5: 5.0, 2.0/3: 13.0/4, 1.0: 2.0}[la]
    print(f"  lambda={la}: closed m3 = {A3_closed + 1 + 3*A2:.5f} | direct R=120 -> {dirs[0]:.4f}, R=240 -> {dirs[1]:.4f} | target {tgt}")
