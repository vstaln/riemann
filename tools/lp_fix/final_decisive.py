import sys, math
sys.path.insert(0, '/home/vstaln/riemann/tools')
sys.path.insert(0, '/home/vstaln/riemann')
import numpy as np
from scipy.optimize import linprog
from flint import arb, fmpq
from adv_lp_loop_v3 import (build_tables, adverse_boxes, cosine_kernel,
                            squared_kernel_derivatives_arb, _up)

D=335; EPS=0.005991; ALPHA=1.464; GRID=4000
p0 = 1.0/(6.0*D); Q0 = 1.0/3.0
kernel = cosine_kernel(ALPHA)
cutoff = int(math.ceil(_up(EPS/(1.0/3000.0))*GRID))+1
ncell = cutoff + 8
ranges, second_ranges, n = build_tables(kernel, ncell)
boxes = adverse_boxes(D, n, p0, EPS)
pair_list = [(i,j) for i in range(6) for j in range(i+1,6)]

def F_mid(box, l, c):
    mid = [fmpq(lo+hi+1, 2*GRID) for lo,hi in box]
    p=[p0 + (l[i-1] if 0<=i-1<=4 else 0.0) - (l[i] if 0<=i<=4 else 0.0) for i in range(6)]
    q=[Q0 + (c[i-1] if 0<=i-1<=4 else 0.0) - (c[i] if 0<=i<=4 else 0.0) for i in range(6)]
    wval={}
    for i in range(6):
        v,_,_=squared_kernel_derivatives_arb(arb(mid[i]),kernel); wval[i]=v
    spans={}
    for i,j in pair_list:
        pt=sum(mid[i:j],fmpq(0)); v,_,_=squared_kernel_derivatives_arb(arb(pt),kernel); spans[(i,j)]=v
    val=arb(0)
    for i in range(6):
        val += arb(p[i])*arb(mid[i]) + arb(q[i])*wval[i]
    for i,j in pair_list:
        val += arb(2.0/(7-(j-i)))*spans[(i,j)]
    return float(val)

def lp(rows):
    A_rows = np.array([[-a for a in A]+[-c for c in C] for _,A,C,_ in rows])
    b_rows = np.array([const-EPS for _,_,_,const in rows])
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

# point cells, split by pressure-relevance (sum of low endpoints < cutoff)
pts = sorted(set(b for b in boxes if max(hi-lo for lo,hi in b)==0))
rel = [b for b in pts if sum(lo for lo,hi in b) < cutoff]
irr = [b for b in pts if sum(lo for lo,hi in b) >= cutoff]
print(f"point cells: {len(pts)} total; {len(rel)} pressure-relevant (<cutoff={cutoff}); {len(irr)} pressure-pruned")

# build exact F rows at base (l=c=0) for the affine form: F = const - A.l - C.c
def aff(b):
    mid=[fmpq(lo+hi+1,2*GRID) for lo,hi in b]
    wval={}
    for i in range(6):
        v,_,_=squared_kernel_derivatives_arb(arb(mid[i]),kernel); wval[i]=v
    spans={}
    for i,j in pair_list:
        pt=sum(mid[i:j],fmpq(0)); v,_,_=squared_kernel_derivatives_arb(arb(pt),kernel); spans[(i,j)]=v
    A=[float(mid[k+1]-mid[k]) for k in range(5)]       # dF/dl_k = mid[k+1]-mid[k]
    C=[float(wval[k+1]-wval[k]) for k in range(5)]     # dF/dc_k = w[k+1]-w[k]
    const = arb(p0)*sum(mid,arb(0)) + arb(Q0)*sum(wval.values(),arb(0))
    for i,j in pair_list:
        const += arb(2.0/(7-(j-i)))*spans[(i,j)]
    return A,C,float(const)

rows_rel = [(b,)+aff(b) for b in rel]
rows_all = [(b,)+aff(b) for b in pts]
r_rel = lp(rows_rel)
r_all = lp(rows_all)
print("EXACT-F LP, pressure-relevant point cells only:", r_rel.success, r_rel.message[:45])
print("EXACT-F LP, ALL point cells:", r_all.success, r_all.message[:45])

# also report min F at base over pressure-relevant cells (the deficit)
zero=[0.0]*5
vals = sorted(F_mid(b,zero,zero) for b in rel)
print("min F(base) over pressure-relevant cells:", min(vals))
print("top-5 lowest F(base):", [f"{v:.7f}" for v in vals[:5]])
print("gap to target:", EPS - min(vals))
