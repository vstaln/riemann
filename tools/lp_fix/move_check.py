import sys, math
sys.path.insert(0, '/home/vstaln/riemann/tools')
sys.path.insert(0, '/home/vstaln/riemann')
import numpy as np
from flint import arb, fmpq
from adv_lp_loop_v3 import (build_tables, adverse_boxes, tangent_affine,
                            cosine_kernel, squared_kernel_derivatives_arb, _up)
from scipy.optimize import linprog

D=335; ALPHA=1.464; GRID=4000
p0 = 1.0/(6.0*D); Q0 = 1.0/3.0
kernel = cosine_kernel(ALPHA)
cutoff = int(math.ceil(_up(0.005991/(1.0/3000.0))*GRID))+1
ncell = cutoff + 8
ranges, second_ranges, n = build_tables(kernel, ncell)
boxes = adverse_boxes(D, n, p0, 0.005991)
pair_list = [(i,j) for i in range(6) for j in range(i+1,6)]

# target terminal cell family
term = tuple((v,v) for v in (4220, 8007, 8027, 8027, 7995, 4220))
A,C,const = tangent_affine(term,kernel,ranges,second_ranges,p0)
print("terminal A=", ["%.5f"%x for x in A])
print("terminal C=", ["%.6f"%x for x in C])
print("terminal const(tangent)=", const)

# at base (l=c=0) what is the tangent value and gap to target?
base_tangent = const
print("gap to target at base =", 0.005991 - base_tangent)

# build LP with the terminal cell row only + kappa/q rows, check max slack
def lp_with(extra_rows):
    rs = [((None,),A,C,const)] + extra_rows
    A_rows = np.array([[a for a in A]+[c for c in C] for _,A,C,_ in rs])
    b_rows = np.array([const_ - 0.005991 for _,_,_,const_ in rs])
    kap=[]
    for i in range(1,7):
        row=[0.0]*10
        if 1<=i-1<=5: row[i-2]=-1.0
        if 1<=i<=5: row[i-1]=1.0
        kap.append(row)
    for i in range(1,7):
        row=[0.0]*10
        if 1<=i-1<=5: row[4+(i-2)]=-1.0
        if 1<=i<=5: row[4+(i-1)]=1.0
        kap.append(row)
    A_rows=np.vstack([A_rows,np.array(kap)])
    b_rows=np.concatenate([b_rows,np.full(6,p0),np.full(6,Q0)])
    return linprog(np.zeros(10),A_ub=A_rows,b_ub=b_rows,
                   bounds=[(None,None)]*5+[(-0.06,0.06)]*5,method='highs')

# terminal row alone
res = lp_with([])
print("terminal-only LP feasible?", res.success, res.message[:40])

# add a second "adversary" box row (the other known terminal family variant) and see infeasibility
# find the most violated: for a grid of l values, compute which OTHER box binds
# simpler: find any PD box whose tangent drops below target when l0=+something
def tangent_at(box, l, c):
    aff = tangent_affine(box,kernel,ranges,second_ranges,p0)
    if aff is None: return None
    A,C,const = aff
    return const - sum(A[k]*l[k] for k in range(5)) - sum(C[k]*c[k] for k in range(5))

# scan l0 in [-0.06, 0.06], c=0, find another box that goes below 0.005991
import itertools
test_l0s = [v/1000.0 for v in range(-60, 61, 5)]
viol = {}
for l0 in test_l0s:
    l = [l0,0,0,0,0]; c=[0,0,0,0,0]
    bad = []
    for b in boxes:
        t = tangent_at(b, l, c)
        if t is not None and t < 0.005991 - 1e-9:
            bad.append(b)
    if bad:
        viol[l0] = len(bad)
print("boxes violating target for l0 in scan (c=0):")
for k,v in sorted(viol.items()):
    print(f"  l0={k:+.3f}: {v} violating boxes")
