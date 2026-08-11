#!/usr/bin/env python3
"""Farmer 1995 combination arithmetic (identity (6), VERIFIED-FROM-PAPER).
Run: cd /home/vstaln/riemann && uv run --quiet --with mpmath python tools/xiprime2_check/check_farmer_combo.py

Identity (6) [Farmer 1995]:  Nd >= 2^{-J}[2^{J-1} beta_0 + beta_J + sum_{n=1}^{J-1} 2^{J-n-1} beta_n] N
where beta_j >= fi_j = simple-ON-LINE proportion of xi^(j).  J=5 with Conrey's fi:
  fi_0 = 0.40219, fi_1 = 0.79874, fi_2 = 0.93469, fi_3 = 0.9673, fi_4 = 0.98006, fi_5 = 0.9863
gives the paper's Nd/N > 0.63952.
Substituting the paper C's Thm D (fi_0 = 0.6725) and the xi' certificate (fi_1 = 0.86864):
  Nd/N >= 0.79215  (beats Wu 0.6603; below the paper's own Thm E 5/6 = 0.8333).
"""
import mpmath as mp
mp.mp.dps = 30

def farmer_nd(fi, J=5):
    return (2**(J-1)*fi[0] + fi[J] + sum(2**(J-n-1)*fi[n] for n in range(1, J)))/2**J

conrey = [0.40219, 0.79874, 0.93469, 0.9673, 0.98006, 0.9863]
with_paper = [0.6725, 0.86864, 0.93469, 0.9673, 0.98006, 0.9863]

print("Farmer 1995 identity (6), J=5:")
print(f"  Conrey-only:          Nd/N >= {mp.nstr(farmer_nd(conrey), 10)}  (paper: 0.63952)")
print(f"  paper ThmD + xi'-cert: Nd/N >= {mp.nstr(farmer_nd(with_paper), 10)}  (Wu: 0.6603, paper ThmE: 5/6=0.83333)")
print(f"  > 0.6603? {farmer_nd(with_paper) > mp.mpf('0.6603')};  < 5/6? {farmer_nd(with_paper) < mp.mpf('5')/6}")
