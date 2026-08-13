#!/usr/bin/env python3
"""Crystal read-feasibility — float exploration (numpy, f64). S(j) of crystal
families vs GUE-flat datum S(j)~j, and per-atom tau. Labels: CHECKED NUMERICALLY
(f64 float exploration; the verdict does not rest on tight digits)."""
import numpy as np

SQRT2 = np.sqrt(2.0)
H0 = 1.5 - (1/SQRT2)*1/np.tan(1/SQRT2)
L = 1/H0

def k(x):
    x = np.asarray(x, float)
    def sinc(y):
        y = np.asarray(y, float)
        return np.where(np.abs(y) < 1e-9, 1.0, np.sin(y)/y)
    a = (SQRT2 - 2*np.pi*x)/2
    b = (SQRT2 + 2*np.pi*x)/2
    K0 = 2*sinc(SQRT2/2)
    return (sinc(a)+sinc(b))/K0

def S_of(gaps):
    """gaps: full cell gaps INCLUDING wrap gap, in mean-gap units L.
    n atoms/cell: positions 0..P-L, cell size P = sum(gaps)*L."""
    gabs = np.asarray(gaps, float)*L
    P = gabs.sum()
    pos = np.concatenate([[0.0], np.cumsum(gabs[:-1])])  # n distinct atoms
    n = len(pos)
    out = []
    for j in range(1, n):
        v = np.exp(-2j*np.pi*j*pos/P).sum()
        out.append(abs(v)**2/n)
    return np.array(out), P

def tau_of(gaps, nper=200):
    g = np.tile(np.asarray(gaps, float), nper)
    gam = np.cumsum(g)
    d = gam[:, None]-gam[None, :]
    M = k(d)
    lam = np.linalg.eigvalsh(M)
    psi = np.where(lam <= 2.0, (lam-1.0)**2, 2.0*lam-3.0)
    return float(np.mean(psi))

print(f"H0={H0:.15f} L={L:.15f}")
z = []
xs = np.linspace(0.5, 4.0, 80001)
kv = k(xs)
idx = np.where(np.diff(np.sign(kv)) != 0)[0]
for i in idx:
    a, b = xs[i], xs[i+1]
    for _ in range(80):
        m = (a+b)/2
        if k(m)*k(a) <= 0: b = m
        else: a = m
    z.append((a+b)/2)
print("kernel zeros:", [f"{v:.6f}" for v in z])

eps_per_atom = 0.007759/7
print(f"certified floor per atom (eps=0.007759/7): {eps_per_atom:.6e}")

rows = []
# L-UNIT gaps (mean-gap units); physical abs gaps = gaps*L.
# kernel/tau need ABS gaps; S(j) is scale-covariant (pos/P), same either way.
cases = [
    ("7-crystal (1,2,.01,3,1,1)+wrap1", [1.0, 2.0, 0.01, 3.0, 1.0, 1.0, 1.0], True),
    ("2-per(delta=z1)", [z[0]/L, 2.0 - z[0]/L], True),
    ("alt(1,2.03) (abs gaps 1,2.03)", [1.0 / L, 2.03 / L], True),
    ("flat lattice (7 equal)", [1.0] * 7, True),
]
for name, gaps, inL in cases:
    S, P = S_of(gaps)
    absg = np.asarray(gaps, float) * L if inL else np.asarray(gaps, float)
    t = tau_of(absg)
    j = np.arange(1, len(gaps))
    dev = np.abs(S - j).max()
    rows.append((name, float(P), S, dev, t))
    print(f"\n{name}  period={float(P):.4f} abs ({float(P / L):.3f} L)")
    print(f"  S(j) j=1..{len(gaps) - 1}: {np.round(S, 4)}")
    print(f"  NearCUE datum j:        {j}")
    print(f"  max|S(j)-j| = {dev:.4f}   (NearCUE 256-law: ~3e-40)")
    print(f"  tau per atom = {t:.5e}   ratio vs certified eps/atom = {t / eps_per_atom:.1f}x")
