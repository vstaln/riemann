import sys, math
sys.path.insert(0, '/home/vstaln/riemann/tools')
sys.path.insert(0, '/home/vstaln/riemann')
import numpy as np
from scipy.optimize import linprog
from adv_lp_loop_v3 import (build_tables, adverse_boxes, tangent_affine,
                            cosine_kernel, _up)

D=335; EPS=0.005991; ALPHA=1.464; GRID=4000
p0 = 1.0/(6.0*D); Q0 = 1.0/3.0
kernel = cosine_kernel(ALPHA)
cutoff = int(math.ceil(_up(EPS/(1.0/3000.0))*GRID))+1
ncell = cutoff + 8
ranges, second_ranges, n = build_tables(kernel, ncell)
boxes = adverse_boxes(D, n, p0, EPS)

rows = []
for box in boxes:
    aff = tangent_affine(box, kernel, ranges, second_ranges, p0)
    if aff is None:
        continue
    rows.append((box,)+aff)
print("PD rows:", len(rows))

def make_lp(rs, flip_sign):
    # tangent_affine now returns TRUE gradients (fixed 2026-08-14):
    # tangent = const + A.l + C.c, want >= EPS  <=>  -A.l - C.c <= const - EPS
    A_rows = np.array([[-a for a in A]+[-c for c in C] for _,A,C,_ in rs])
    b_rows = np.array([const-EPS for _,_,_,const in rs])
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

# sign-flipped = corrected: use -A,-C rows (enforces const + A.l + C.c >= EPS)
res_correct = make_lp(rows, flip_sign=True)
print("CORRECTED LP (const + A.l + C.c >= eps):", res_correct.success, res_correct.message[:60])
if res_correct.success:
    print("  x =", res_correct.x)
    l = res_correct.x[:5]; c = res_correct.x[5:10]
    print("  l =", [f"{v:.9f}" for v in l])
    print("  c =", [f"{v:.9f}" for v in c])
    # verify against verifier tangent for a few boxes
    from adv_lp_loop_v3 import squared_kernel_derivatives_arb
    from flint import arb, fmpq
    pair_list=[(i,j) for i in range(6) for j in range(i+1,6)]
    def true_tangent(box):
        A,C,const = tangent_affine(box,kernel,ranges,second_ranges,p0)
        val = const + sum(A[k]*l[k] for k in range(5)) + sum(C[k]*c[k] for k in range(5))
        return val
    worst = min(true_tangent(b) for b in [r[0] for r in rows])
    print("  min corrected tangent over PD rows =", worst)
