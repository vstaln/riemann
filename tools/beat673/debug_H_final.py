"""Careful direct computation of J = int int |s-t| v(s) v(t) with mpmath,
using splitting at the kink, and compare to analytic."""
import mpmath as mp
mp.mp.dps = 80
alpha = mp.mpf(149)/100
def v(x): return mp.cos(alpha*x)

# J = int_s int_t |s-t| v(s) v(t).  Split: 2 * int_{s>t} (s-t) v(s)v(t)
# = 2 * int_{t=-0.5}^{0.5} int_{s=t}^{0.5} (s-t) v(s) v(t) ds dt
def J_direct():
    return mp.quad(lambda s, t: abs(s-t)*v(s)*v(t), [-0.5,0.5], [-0.5,0.5], method='gauss-legendre', maxdegree=20)
def J_split():
    # int_{-0.5}^{0.5} dt v(t) * [ int_t^{0.5} (s-t) v(s) ds ]  *2  (symmetry)
    inner = lambda t: mp.quad(lambda s: (s-t)*v(s), [mp.mpf(t), 0.5])
    return 2*mp.quad(lambda t: v(t)*inner(t), [-0.5, 0.5])

I0 = 2*mp.sin(alpha/2)/alpha
I2 = mp.mpf(1)/2 + mp.sin(alpha)/(2*alpha)
C1 = I0/2 + 2*mp.cos(alpha/2)/alpha**2
J_an = -2*I2/alpha**2 + C1*I0
print(f"I0 = {mp.nstr(I0, 30)}")
print(f"I2 = {mp.nstr(I2, 30)}")
print(f"C1 = {mp.nstr(C1, 30)}")
print(f"J_analytic = {mp.nstr(J_an, 30)}")
print(f"J_split    = {mp.nstr(J_split(), 30)}")
print(f"J_gauss    = {mp.nstr(J_direct(), 30)}")
