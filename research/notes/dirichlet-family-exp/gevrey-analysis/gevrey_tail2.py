# Corrected: measure |phi_hat(r - iy)| = |2 int_0^{L/2} phi(u) e^{-i(r-iy)u} du|
# = |2 int phi(u) cos(ru) cosh(yu) du + i 2 int phi(u) sin(ru) sinh(yu) du|.
import numpy as np

def rho(x):
    return x - np.sin(2*np.pi*x)/(2*np.pi)

def phi_hat_cmplx(r, y, L, w, n=40000):
    u = np.linspace(0, L/2, n)
    half = L/2
    phi = np.where(u <= half - w, 1.0, rho((half - u)/w))
    du = (L/2)/n
    # e^{-i(r-iy)u} = e^{-i r u} e^{-y u} = (cos ru - i sin ru)(cosh yu - sinh yu)
    # = cos(ru)cosh(yu) - sinh(yu)sin(ru) - i[sin(ru)cosh(yu) + cos(ru)sinh(yu)]
    # Actually e^{-i(r-iy)u} = e^{y u} e^{-i r u} = e^{yu}(cos ru - i sin ru)
    val = np.sum(phi * np.exp(y*u) * (np.cos(r*u) - 1j*np.sin(r*u))) * 2 * du
    return val

L = 9.34
w = 1.0
y = 0.5
print("L=9.34, w=1, y=0.5 (the q=1009 lambda=1 window)")
for r in [2, 5, 10, 20, 40, 80]:
    v = phi_hat_cmplx(r, y, L, w)
    print(f"  r={r:5.1f}  |phi_hat(r-iy)| = {abs(v):.3e}")

# The paper's C^3 bound is |phi_hat(r-iy)| <= e^{L/4} C1 r^-2 = X^{1/4} C1 r^-2  (from Prop 4.2 proof)
X = np.exp(L)
print(f"\nX^{{1/4}} = {X**0.25:.2f}  (paper's e^{{L/4}} factor)")
print("Paper C^3 bound e^{L/4} * 2 r^-2:")
for r in [2,5,10,20,40]:
    print(f"  r={r}: {X**0.25 * 2/r**2:.3e}")

# Gevrey prediction: |phi_hat(r-iy)| <= X^{1/4} C exp(-c |r|^{1/s}). For s=1/2 (analytic),
# the decay is exp(-c sqrt(r)). Compare measured decay slope.
print("\nMeasured decay slope d log|phi_hat|/d sqrt(r) (should be ~ -c, Gevrey constant):")
prev = None
for r in [2,5,10,20,40,80]:
    v = abs(phi_hat_cmplx(r, y, L, w))
    slope = None
    if prev is not None:
        slope = (np.log(v) - np.log(prev)) / (np.sqrt(r) - np.sqrt(prev_r))
    print(f"  r={r}: |phi_hat|={v:.3e}  slope vs sqrt(r): {slope}")
    prev, prev_r = v, r
