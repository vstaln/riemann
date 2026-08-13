#!/usr/bin/env python3
"""Generate the figures for the Vstalin Grady preprint from REAL data.
Data sources:
  - /tmp/lambda_n.txt  (Li coefficients, dps=60)
  - certified bound values (attack_bound_check.py, committed)
  - 10M-zero stats (laptop run, verbatim in results)
  - 21M-zero stats (laptop full run, pending)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

plt.rcParams.update({
    'font.size': 11,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'figure.dpi': 130,
    'savefig.dpi': 200,
    'axes.grid': True,
    'grid.alpha': 0.3,
})

OUT = "/root/riemann/research/waves/wave-phone-2/results/figures/"
import os
os.makedirs(OUT, exist_ok=True)

# ---------- Figure 1: certified bound vs eps (the record ladder) ----------
# bound = (H - tau)/(1 - B/m), H=0.67242188609644747, tau=(1/220)(127/133),
# A = eps*127, B = Phi_133(A). Values from attack_bound_check.py (committed).
eps_vals = [8060e-6, 8063e-6, 8064e-6, 8065e-6, 8066e-6, 8070e-6, 8080e-6]
bounds = [0.6732599, 0.6732640, 0.6732654, 0.6732661, 0.6732676, 0.6732723, 0.6732826]

fig, ax = plt.subplots(figsize=(7, 4.4))
ax.plot([e*1e6 for e in eps_vals], bounds, 'o-', color='#0b5394', lw=2, ms=6,
        label='certified bound $(H-\\tau)/(1-B/m)$, $m{=}133$')
# mark the record
ax.scatter([8065], [0.6732660791], s=220, facecolors='none', edgecolors='#cc0000',
           linewidths=2.5, zorder=5, label='record: $0.6732660791$ (eps$=8065\\times10^{-6}$)')
# published floor
ax.axhline(0.4167, color='#666666', ls='--', lw=1.5, label='published unconditional: 5/12 $\\approx 0.4167$')
ax.axhline(0.6818312306, color='#e69138', ls=':', lw=1.8, label='in-class ceiling: $0.6818312306$ (proven)')
ax.set_xlabel('certified eps $\\varepsilon$  ($\\times 10^{-6}$)')
ax.set_ylabel('simple-on-line lower bound')
ax.set_title('Certified proportion of zeros on the critical line')
ax.legend(fontsize=8.5, loc='lower right')
ax.set_xlim(7950, 8200)
ax.set_ylim(0.672, 0.684)
fig.tight_layout()
fig.savefig(OUT + 'fig1_certified_bound.png', bbox_inches='tight')
plt.close(fig)

# ---------- Figure 2: Li coefficients lambda_n (positivity probe) ----------
data = [(int(l.split()[0]), mp.mpf(l.split()[1])) for l in open('/tmp/lambda_n.txt')]
ns = [d[0] for d in data]
vals = [float(d[1]) for d in data]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))
# left: first 40 (the numerically trustworthy regime)
n40 = [n for n, v in zip(ns, vals) if n <= 40]
v40 = [v for n, v in zip(ns, vals) if n <= 40]
ax1.plot(n40, v40, 'o-', color='#38761d', lw=1.6, ms=4)
# RH asymptotic lambda_n ~ (n/2)(log n + gamma - 1 - log 2pi)
euler = float(mp.euler)
n_arr = np.array(n40, dtype=float)
asymp = (n_arr/2) * (np.log(n_arr) + euler - 1 - np.log(2*np.pi))
ax1.plot(n_arr, asymp, '--', color='#cc0000', lw=1.5, label='RH asymptote')
ax1.set_xlabel('$n$'); ax1.set_ylabel('$\\lambda_n$')
ax1.set_title('Keiper–Li coefficients (trusted range)')
ax1.legend(fontsize=9)

# right: log-scale showing the precision wall
ax2.semilogy(ns, [abs(v) for v in vals], color='#0b5394', lw=1.4)
ax2.axvline(92, color='#cc0000', ls='--', lw=1.3)
ax2.text(95, 1e6, 'precision wall', color='#cc0000', fontsize=9, rotation=90)
ax2.set_xlabel('$n$'); ax2.set_ylabel('$|\\lambda_n|$ (log)')
ax2.set_title('Ill-conditioning beyond $n \\approx 90$ (dps$=60$)')
fig.tight_layout()
fig.savefig(OUT + 'fig2_li_coefficients.png', bbox_inches='tight')
plt.close(fig)

# ---------- Figure 3: 10M-zero spacing / m3-N scaling ----------
# Values from the laptop 10M run (verbatim):
# N=64: m3=4.72457+-0.00031, pair=3.31412, T mean=+0.41045 min=+0.1797 max=+0.7270 rho1=-0.2924 rho5=-0.0104
# N=256: m3=4.83841+-0.00020, pair=3.40719, T mean=+0.43122 min=+0.3333 max=+0.5408 rho1=-0.3043 rho5=+0.1203
# N=512: m3=4.86075+-0.00016, pair=3.42542, T mean=+0.43533 min=+0.3526 max=+0.4790 rho1=-0.1697 rho5=+0.2237
Nblocks = [64, 256, 512]
m3 = [4.72457, 4.83841, 4.86075]
m3err = [0.00031, 0.00020, 0.00016]
Tmean = [0.41045, 0.43122, 0.43533]
Tmin = [0.1797, 0.3333, 0.3526]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))
ax1.errorbar(Nblocks, m3, yerr=m3err, fmt='o-', color='#0b5394', lw=2, ms=7, capsize=4)
ax1.axhline(3.0, color='#cc0000', ls='--', lw=1.4, label='GUE prediction $m_3=3$ (deficit)')
ax1.set_xscale('log')
ax1.set_xlabel('block size $N$'); ax1.set_ylabel('$m_3 = \\mathrm{tr}\\,G^3/N$')
ax1.set_title('Third moment vs block size (10M zeros)')
ax1.legend(fontsize=9)

ax2.plot(Nblocks, Tmean, 'o-', color='#38761d', lw=2, ms=7, label='mean $T$-block')
ax2.plot(Nblocks, Tmin, 's-', color='#e69138', lw=2, ms=7, label='min $T$-block')
ax2.axhline(1/3, color='#666666', ls=':', lw=1.5, label='$T = 1/3$ floor')
ax2.set_xscale('log')
ax2.set_xlabel('block size $N$'); ax2.set_ylabel('marked $T$')
ax2.set_title('Marked-$T$ floor $= 1/3$ (10M zeros)')
ax2.legend(fontsize=9)
fig.tight_layout()
fig.savefig(OUT + 'fig3_spacing_stats.png', bbox_inches='tight')
plt.close(fig)

print("figures written to", OUT)
for f in sorted(os.listdir(OUT)):
    print("  ", f, os.path.getsize(OUT+f), "bytes")
