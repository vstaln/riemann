import numpy as np
from scipy.integrate import quad

def gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def J2(la):
    v, _ = quad(lambda u: np.sinc(la*u)**2*np.sinc(u)**2, 0, np.inf, limit=400)
    return v

def A3_fast(R, la, n):
    x, w = gl(n)
    xs = R*x; ws = R*w
    uu, vv = np.meshgrid(xs, xs, indexing='ij')
    ww = uu+vv
    fast = -3.0*np.sinc(la*uu)*np.sinc(la*vv)*np.sinc(la*ww)*np.sinc(uu)**2 \
           + 2.0*np.sinc(la*uu)*np.sinc(la*vv)*np.sinc(la*ww)*np.sinc(uu)*np.sinc(vv)*np.sinc(ww)
    return float(np.sum(fast * np.outer(ws, ws)))

print("m3 via corrected closed form A3 = 1/la^2 - (6/la)*J2 + 2(1-la/2)  vs  direct 2D (D and 2C analytic):")
for la in (0.5, 2.0/3, 1.0):
    A2 = 1/la - 2*J2(la)
    A3_closed = 1/la**2 - (6/la)*J2(la) + 2*(1 - la/2)
    m3_closed = 1 + 3*A2 + A3_closed
    dirs = []
    for (R, n) in ((60, 800), (120, 1600)):
        A3 = 1/la**2 + 2*(1-la/2) + A3_fast(R, la, n)
        dirs.append(1 + 3*A2 + A3)
    tgt = {0.5: 5.0, 2.0/3: 13.0/4, 1.0: 2.0}[la]
    print(f"  lambda={la}: closed m3 = {m3_closed:.5f} | direct R=60 -> {dirs[0]:.4f}, R=120 -> {dirs[1]:.4f} | target {tgt}")
