"""Reference LP values via scipy/HiGHS (reuses the original modules, which we do NOT
modify). Fast LP only; the slow DE global floors are taken from the task's recorded
values. Used to build the Python column of the acceptance table."""
import sys, numpy as np
sys.path.insert(0, "/home/vstaln/riemann/tools/coboundary-reopt")
from coboundary_symmetric_lp import (build_578_family, solve_symmetric_lp,
                                     L_TAWAN, C_TAWAN, floor_over, sym_lc)
from coboundary_reopt_lp import build_family, solve_maxmin, floor_over as fo2

for alpha, name in [(1.464, "a1464"), (np.sqrt(2.0), "a149"), (1.49, "a149flat")]:
    cfgs = build_578_family(alpha)
    fl_t = floor_over(alpha, L_TAWAN, C_TAWAN, cfgs)
    x = solve_symmetric_lp(alpha, cfgs)
    a1, a2, b1, b2, v = x
    l, c = sym_lc(a1, a2, b1, b2)
    fl_lp = floor_over(alpha, l, c, cfgs)
    print(f"SYM alpha={alpha}: v*={v:.9f} a1={a1:.12e} a2={a2:.12e} b1={b1:.12e} b2={b2:.12e} floor_tawan={fl_t:.9f} floor_lp={fl_lp:.9f}")

alpha = 1.49
cfgs = build_family(alpha)
print(f"REOPT family size={len(cfgs)}")
for cb in [0.06, 0.02, 0.15]:
    l, c, v = solve_maxmin(alpha, cfgs, c_bound=cb)
    fl = fo2(alpha, l, c, cfgs)
    print(f"REOPT alpha={alpha} c_bound={cb}: v*={v:.9f} l={l} c={c} floor_family={fl:.9f}")
