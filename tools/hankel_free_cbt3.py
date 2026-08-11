#!/usr/bin/env python3
"""C-BT3 addendum part 2 (fixed): free-mass 2-atom realization family.

The certificate does NOT know m0 = (#eigenvalues)/N, so the honest realization of
(m1,m2,m3) = (1,4/3,2) allows arbitrary total mass.  Then the 2-atom system
   m1 = w1 a + w2 b = 1,   m2 = w1 a^2 + w2 b^2 = 4/3,   m3 = w1 a^3 + w2 b^3 = 2
is 3 equations in 4 unknowns (w1, w2, a, b): a 1-parameter family of realizations.
The extremal world (a=1, b=2, w1=2/3, w2=1/6, m0=5/6) must be ON this family; the
mass-1 symmetric measure (a=1-1/sqrt3, b=1+1/sqrt3, w1=w2=1/2) must also be on it.
We sweep the first atom a, solve the reduced 3-unknown system, and check both.

Run: uv run --quiet --with numpy --with scipy python /tmp/attack_hankel/hankel_free.py
"""
import numpy as np
from scipy.optimize import least_squares

def solve_given_a(a, guess):
    def resid(p):
        w1, w2, b = p
        m = np.array([w1*a + w2*b, w1*a*a + w2*b*b, w1*a**3 + w2*b**3])
        return m - np.array([1.0, 4/3, 2.0])
    sol = least_squares(resid, guess, bounds=([0, 0, -5], [10, 10, 5]))
    return sol

print("Sweep a (first atom); solve for (w1, w2, b); count feasible 2-atom realizations")
hits = []
for a in np.linspace(0.05, 2.6, 52):
    sol = solve_given_a(a, (0.5, 0.5, 1.5))
    if sol.cost < 1e-16:
        w1, w2, b = sol.x
        hits.append((a, w1, w2, b, w1 + w2))
print(f"converged 2-atom realizations found on sweep: {len(hits)} of 52 grid points")

# exactly verify the two named members:
def check(a, w1, w2, b, name):
    m4 = w1*a**4 + w2*b**4
    err = np.abs(np.array([w1*a + w2*b, w1*a*a + w2*b*b, w1*a**3 + w2*b**3])
                 - np.array([1.0, 4/3, 2.0])).max()
    print(f"  {name:>55s}: a={a:.6f} b={b:.6f} w1={w1:.6f} w2={w2:.6f}  "
          f"m0={w1+w2:.6f}  m4={m4:.6f}  |err|={err:.2e}  {'OK' if err < 1e-9 else 'FAIL'}")

print("\nNamed members of the family (exact verification):")
check(1.0, 2/3, 1/6, 2.0, "extremal world (1, 2; w 2/3, 1/6; m0 = 5/6)")
s = np.sqrt(3)/3
check(1 - s, 0.5, 0.5, 1 + s, "mass-1 symmetric {1 +/- 1/sqrt3} (m0 = 1)")
check(0.0, 0.0, 1/3, 3.0, "one atom at 3, mass 1/3? (control, should fail m3)")
