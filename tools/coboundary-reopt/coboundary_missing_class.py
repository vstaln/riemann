"""Pin down the true missing adverse config class for the corrected LP solution.

Correct LP (alpha=1.49, c_bound=0.06):
  l = (0.0002552, 0.0017164, 0.0002734, 0.0003247, 0.0002585)
  c = (0.06, -0.06, 0.06, -0.06, 0.06)
Checks:
  1. F_B at g=(1.0634, 25.9601, 1.0478, 1.0319, 1.0369, 1.0474) [the prior worst]
  2. single huge gap g_i = H with neighbors at kernel-zero ~1.03-1.05
  3. two huge gaps g_i, g_j = H
  4. tawan at the same configs
"""
import numpy as np

def k_alpha(x, alpha):
    x = np.asarray(x, float); a = alpha / 2.0
    z1 = np.pi * x - a; z2 = np.pi * x + a
    return 0.5 * (np.sinc(z1 / np.pi) + np.sinc(z2 / np.pi)) / np.sinc(a / np.pi)

def w_alpha(x, alpha): return k_alpha(x, alpha) ** 2

P0, Q0 = 1.0/1920, 1.0/3

def pair_coeffs():
    return {(i, j): 2.0/(7-(j-i)) for i in range(7) for j in range(i+1, 7)}

def F0(g, alpha):
    g = np.asarray(g, float)
    y = np.concatenate([[0.0], np.cumsum(g)])
    total = P0*np.sum(g) + Q0*np.sum(w_alpha(g, alpha))
    for (i,j),a in pair_coeffs().items():
        total += a*w_alpha(y[j]-y[i], alpha)
    return total

def lin_coeffs(g, alpha):
    g = np.asarray(g, float)
    g0 = np.concatenate([[0.0], g, [0.0]])
    return (np.asarray(g0[1:]-g0[:-1], float)[1:6],
            np.asarray(w_alpha(g0[1:], alpha)-w_alpha(g0[:-1], alpha), float)[1:6])

def F_B(g, alpha, l, c):
    L, C = lin_coeffs(g, alpha)
    return F0(g, alpha) + np.dot(L, l) + np.dot(C, c)

alpha = 1.49
l_lp = np.array([0.0002552, 0.0017164, 0.0002734, 0.0003247, 0.0002585])
c_lp = np.array([0.06, -0.06, 0.06, -0.06, 0.06])
l_tw = np.array([54, -123, 0, 123, -54]) / 1_920_000
c_tw = np.array([5971, 5971, 0, -5971, -5971]) / 300_000

print("== single config from the prior worst scan ==")
g = np.array([1.0634, 25.9601, 1.0478, 1.0319, 1.0369, 1.0474])
print(f"  LP  = {F_B(g, alpha, l_lp, c_lp):.6f}")
print(f"  taw = {F_B(g, alpha, l_tw, c_tw):.6f}")

print("\n== single huge gap g_i=H, others at kernel-zero ~1.04 (scan) ==")
worst_lp = (1e9, None); worst_tw = (1e9, None)
for pos in range(6):
    for H in [8, 14, 21, 26, 30]:
        g = np.array([1.04, 1.04, 1.04, 1.04, 1.04, 1.04]); g[pos] = H
        vl, vt = F_B(g, alpha, l_lp, c_lp), F_B(g, alpha, l_tw, c_tw)
        if vl < worst_lp[0]: worst_lp = (vl, g.copy())
        if vt < worst_tw[0]: worst_tw = (vt, g.copy())
print(f"  worst LP  = {worst_lp[0]:.6f} at {np.round(worst_lp[1],2)}")
print(f"  worst taw = {worst_tw[0]:.6f} at {np.round(worst_tw[1],2)}")

print("\n== two huge gaps g_i=g_j=H, others at 1.04 (scan) ==")
worst_lp = (1e9, None); worst_tw = (1e9, None)
for i in range(6):
    for j in range(i+1, 6):
        for H in [14, 21, 26]:
            g = np.array([1.04]*6); g[i] = H; g[j] = H
            vl, vt = F_B(g, alpha, l_lp, c_lp), F_B(g, alpha, l_tw, c_tw)
            if vl < worst_lp[0]: worst_lp = (vl, g.copy())
            if vt < worst_tw[0]: worst_tw = (vt, g.copy())
print(f"  worst LP  = {worst_lp[0]:.6f} at {np.round(worst_lp[1],2)}")
print(f"  worst taw = {worst_tw[0]:.6f} at {np.round(worst_tw[1],2)}")

print("\n== single huge gap, others at crystal 1.05/1.98 (the LP family's pattern) ==")
worst_lp = (1e9, None); worst_tw = (1e9, None)
for pos in range(6):
    for H in [8, 14, 21, 26, 30]:
        g = np.array([1.05, 1.98, 1.05, 1.98, 1.05, 1.98]); g[pos] = H
        vl, vt = F_B(g, alpha, l_lp, c_lp), F_B(g, alpha, l_tw, c_tw)
        if vl < worst_lp[0]: worst_lp = (vl, g.copy())
        if vt < worst_tw[0]: worst_tw = (vt, g.copy())
print(f"  worst LP  = {worst_lp[0]:.6f} at {np.round(worst_lp[1],2)}")
print(f"  worst taw = {worst_tw[0]:.6f} at {np.round(worst_tw[1],2)}")
