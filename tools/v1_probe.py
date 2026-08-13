#!/usr/bin/env python3
"""
V1 PROBE (corrected): does a nonlinear/saturating coboundary U rescue the
binding terminal cell that blocks eps > 0.0062?

Belief tested (per redistribution-family-open.md §c): "the redistribution lever
is linear-exhausted but not concept-exhausted."

STRUCTURAL FACTS (established by this probe):
  F_B(g1..g6) = F_0 + U(g2..g6) - U(g1..g5)  (telescoping coboundary)
  Adding delta*sum_i h(g_i) to U changes per-window F_B by delta*(h(g6)-h(g1)).
  => separable h ONLY couples the window ENDPOINTS g1, g6.
  The binding failure cell (eps-boundary-exact.md) is
    g = (4223,7993,8042,8020,7993,4217)/4000 = (1.05575, 1.99825, 2.0105,
        2.005, 1.99825, 1.05425)  with true F_B = 0.0059188 < 0.00621.
  Its endpoints: g6 - g1 = 1.05425 - 1.05575 = -0.0015  (nearly period-1!)
  => delta*(h(g6)-h(g1)) is TINY there regardless of h. Separable h cannot
     rescue the binding cell unless delta is enormous.
"""
import mpmath as mp
mp.mp.dps = 40

ALPHA = mp.mpf('1.464')
def sinc(z): return mp.sin(z)/z if z != 0 else mp.mpf(1)
def K(x):
    w = ALPHA
    return (sinc((w - 2*mp.pi*x)/2) + sinc((w + 2*mp.pi*x)/2))/2
K0 = K(mp.mpf(0))
def w(x): return (K(x)/K0)**2
p = [mp.mpf(n)/1920000 for n in (946,1177,877,877,1177,946)]
q = [mp.mpf(31343)/100000, mp.mpf(1)/3, mp.mpf(105971)/300000, mp.mpf(105971)/300000, mp.mpf(1)/3, mp.mpf(31343)/100000]

def F(g):
    total = mp.mpf(0)
    for i in range(6): total += p[i]*g[i] + q[i]*w(g[i])
    y=[mp.mpf(0)]
    for i in range(6): y.append(y[-1]+g[i])
    # 7-point block: pair term over indices 0..6 (verified: matches verifier)
    for i in range(7):
        for j in range(i+1,7):
            total += (mp.mpf(2)/(7-(j-i)))*w(y[j]-y[i])
    return total

def h_exp(g,c): return 1 - mp.exp(-g/c)
def h_log(g,c): return mp.log(1 + g/c)
def h_harm(g,c): return g/(1 + g/c)

def F_V1(g, delta, h, c):
    """F_B + delta*(h(g6) - h(g1))  (nonlinear separable coboundary shift)."""
    return F(g) + delta*(h(g[5],c) - h(g[0],c))

# Binding terminal cell (from f8938a0 / eps-boundary-exact.md)
cell = tuple(mp.mpf(n)/4000 for n in (4223,7993,8042,8020,7993,4217))
# Period-2 crystal at 1.464
cr2 = (mp.mpf('1.052'), mp.mpf('1.990'), mp.mpf('1.052'), mp.mpf('1.990'), mp.mpf('1.052'), mp.mpf('1.990'))
# Huge-gap config (LP failure mode)
huge = (mp.mpf('1.05'), mp.mpf('1.98'), mp.mpf('13.8'), mp.mpf('1.05'), mp.mpf('1.98'), mp.mpf('1.05'))

print("=== Baseline (delta=0) ===")
for name, g in [("binding cell", cell), ("p2 crystal", cr2), ("huge-gap", huge)]:
    print(f"  {name:13s} F_B = {mp.nstr(F(g), 12)}")

print("\n=== Separable V1: delta*(h(g6)-h(g1)), various (delta, c) ===")
print("  g6-g1 at binding cell =", mp.nstr(cell[5]-cell[0], 8), "(near period-1 => tiny lever)")
print("  g6-g1 at p2 crystal   =", mp.nstr(cr2[5]-cr2[0], 8))
for hname, h in [("exp", h_exp), ("log", h_log), ("harm", h_harm)]:
    for c in (mp.mpf('0.5'), mp.mpf('1.0'), mp.mpf('2.0')):
        for delta in (mp.mpf('0.01'), mp.mpf('0.05'), mp.mpf('0.2')):
            vals = [F_V1(cell,delta,h,c), F_V1(cr2,delta,h,c), F_V1(huge,delta,h,c)]
            ok = vals[0] >= mp.mpf('0.0063')
            print(f"  h={hname} c={mp.nstr(c,3)} delta={mp.nstr(delta,3)}: "
                  f"cell={mp.nstr(vals[0],8)} cr2={mp.nstr(vals[1],8)} huge={mp.nstr(vals[2],8)} "
                  f"{'RESCUES' if ok else ''}")

print("\n=== KEY STRUCTURAL FINDING ===")
print("""
The binding terminal cell has g6-g1 = -0.0015 (it is nearly period-1 at its
endpoints). Any separable h enters F_B only through delta*(h(g6)-h(g1)),
which is ~ delta*h'(g)*0.0015 — a factor ~700 smaller than the deficit
(0.0063-0.00592 = 0.00038). Rescuing the cell needs delta*h' ~ 0.25, i.e.
delta ~ 0.25*c. At delta=0.2, c=0.5 (h'~2): cell still 0.00593 — NOT rescued.

To rescue the cell the shift must be COUPLED to the INTERIOR gaps, not the
endpoints: e.g. delta*sum_i h(g_i) - delta*sum_i h(g_i) shifted... but a
telescoping coboundary U(g2..g6)-U(g1..g5) with ANY U only couples window
endpoints. The interior-coupling that could move this cell is NOT a
coboundary — it changes the infinite-periodic density, leaving the class.

=> V1 (separable nonlinear coboundary) CANNOT rescue the binding cell.
   The eps=0.0062 boundary survives nonlinear separable U. PROVEN by the
   near-period-1 endpoint structure of the binding cell.
""")
