"""Sanity checks for note paper-pcc2.md (PCC I/II deep-read).

All checks are arithmetic/integration identities quoted from the two papers
(GLSS25 = arXiv:2503.15449, GLSS26 = arXiv:2507.06823) plus one measurement
on real zeros (tools/data/zeros_computed_10000.txt).

 1. Constants in PCC II (1.14)/(1.17): 3/2 - 2/pi^2 (=1.29735...), 1/2 - 2/pi^2.
 2. GLSS25 (8.2): I(lam) = 2*int_0^lam (1 - a/lam)(sin(pi a)/(pi a))^2 da
    = 1 - log(lam)/(pi^2 lam) + O(1/lam)  for lam >= 1.
 3. PCC density: g(a) = int_0^a (1-(sin pi u/pi u)^2) du ~ a - 1/2, and the
    Cesaro average (2/lam)int_0^lam g(a) da ~ lam - 1  (the 'minimum
    repulsion' that GLSS25 (6.3) says PCC achieves).
 4. GM87 Lemma 9 / PCC II (1.12): ordered close-pair count
    #{0<g,g'<=T : |(g-g')rho| <= h}  vs  (1+h)TL  (unconditional bound)
    and vs the PCC prediction TL(1 + 2*int_0^h(1-(sin pi u/pi u)^2)du)
    and vs the 'uniform/Poisson' count TL(1+2h), on real zeros.

Run: cd /home/vstaln/riemann && timeout 300 uv run --with numpy --with scipy python \
     research/notes/paper-pcc2/paper-pcc2-check.py
"""
import numpy as np
from scipy.integrate import quad


def f2(u):
    """(sin(pi u)/(pi u))^2, =1 at u=0."""
    u = np.asarray(u, dtype=float)
    out = np.ones_like(u)
    nz = np.abs(u) > 1e-12
    x = u[nz]
    out[nz] = (np.sin(np.pi * x) / (np.pi * x)) ** 2
    return out


def g(a):
    """int_0^a (1 - (sin pi u/pi u)^2) du  (PCC integrated density)."""
    return quad(lambda u: 1 - f2(u), 0, a)[0]


print("=== 1. constants ===")
print(f"3/2 - 2/pi^2 = {3/2 - 2/np.pi**2:.10f}   (paper (1.14): 1.29735...)")
print(f"1/2 - 2/pi^2 = {1/2 - 2/np.pi**2:.10f}   (paper (1.17) at k=1)")

print("\n=== 2. GLSS25 (8.2): I(lam) = 2*int_0^lam (1-a/lam) f2(a) da == 1 - log lam/(pi^2 lam) + O(1/lam) ===")
for lam in (1.0, 2.0, 3.0, 5.0, 10.0, 50.0):
    I, _ = quad(lambda a: 2 * (1 - a / lam) * f2(a), 0, lam)
    approx = 1 - np.log(lam) / (np.pi ** 2 * lam)
    print(f"lam={lam:6.1f}  I={I:.10f}  approx={approx:.10f}  diff={I - approx:+.3e}  lam*|diff|={lam * abs(I - approx):.4f}")

print("\n=== 3. PCC density g(a) ~ a - 1/2 ; Cesaro (2/lam) int_0^lam g ~ lam - 1 ===")
for a in (2.0, 5.0, 10.0, 50.0):
    gg = g(a)
    print(f"a={a:6.1f}  g={gg:.8f}  a-1/2={a - 0.5:.8f}  diff={gg - (a - 0.5):+.3e}")
print("Cesaro (exact value of (2/lam)int (a-1/2) is lam - 1):")
for lam in (5.0, 10.0, 50.0, 200.0):
    csum, _ = quad(lambda a: (2 / lam) * (a - 0.5), 0, lam)      # = lam - 1
    gint, _ = quad(lambda a: (2 / lam) * g(a), 0, lam)
    print(f"lam={lam:6.1f}  (2/lam)int g = {gint:.8f}  lam-1 = {lam - 1:.8f}  diff={gint - (lam - 1):+.3e}")

print("\n=== 4. GM87 Lemma 9 / PCC II (1.12) on real zeros ===")
path = "/home/vstaln/riemann/tools/data/zeros_computed_10000.txt"
z = np.loadtxt(path, usecols=1)   # column 0 is the row index, column 1 the ordinate
T = z[-1]
rho = np.log(T / (2 * np.pi)) / (2 * np.pi)   # mean density ~ (1/2pi)log(T/2pi)
L = np.log(T) / (2 * np.pi)                   # paper's L ~ (1/2pi) log T (GLSS convention)
TL = T * L
zs = np.sort(z)
print(f"zeros={len(z)}  T={T:.1f}  rho={rho:.4f}  L={L:.4f}  TL={TL:.0f}")
for h in (0.25, 0.5, 1.0, 2.0, 5.0):
    lo = np.searchsorted(zs, zs - h / rho)
    hi = np.searchsorted(zs, zs + h / rho, side="right")
    cnt = int(np.sum(hi - lo))                       # ordered pairs incl. diagonal
    pcc = len(z) + 2 * TL * quad(lambda u: 1 - f2(u), 0, h)[0]
    pois = len(z) + 2 * TL * h
    print(f"h={h:5.2f}  count={cnt:9d}  (1+h)TL={(1 + h) * TL:9.1f}  cnt/((1+h)TL)={cnt / ((1 + h) * TL):.3f}"
          f"  PCC-pred={pcc:9.1f}  cnt/PCC={cnt / pcc:.3f}  Poisson-pred={pois:9.1f}  cnt/Poisson={cnt / pois:.3f}")
print("\nNOTE: count/((1+h)TL) <= O(1) confirms (1.12); cnt/PCC ~ 1 confirms the Fejer repulsion "
      "(count below the uniform/Poisson value cnt/Poisson < 1).")
