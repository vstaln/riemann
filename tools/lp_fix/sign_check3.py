import sys, math
sys.path.insert(0, '/home/vstaln/riemann/tools')
sys.path.insert(0, '/home/vstaln/riemann')
from flint import arb, fmpq
from adv_lp_loop_v3 import (build_tables, tangent_affine,
                            cosine_kernel, squared_kernel_derivatives_arb, _up)

D=335; ALPHA=1.464; GRID=4000
p0 = 1.0/(6.0*D); Q0 = 1.0/3.0
kernel = cosine_kernel(ALPHA)
cutoff = int(math.ceil(_up(0.005991/(1.0/3000.0))*GRID))+1
ncell = cutoff + 8
ranges, second_ranges, n = build_tables(kernel, ncell)
pair_list = [(i,j) for i in range(6) for j in range(i+1,6)]

box = tuple((v,v) for v in (4220, 8007, 8027, 8027, 7995, 4220))

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

aff = tangent_affine(box,kernel,ranges,second_ranges,p0)
print("aff None:", aff is None)
A,C,const = aff
print("A_script=", ["%.6f"%x for x in A])
print("C_script=", ["%.6f"%x for x in C])
print("const=", const)
zero=[0.0]*5; base=F_mid(box,zero,zero)
print("F(mid) base =", base)
delta=1e-6
for k in range(5):
    l=[0.0]*5; l[k]=delta
    d=(F_mid(box,l,zero)-base)/delta
    print(f"l_{k}: dF/dl={d:+.6f}   -A_k={-A[k]:+.6f}")
for k in range(5):
    c=[0.0]*5; c[k]=delta
    d=(F_mid(box,zero,c)-base)/delta
    print(f"c_{k}: dF/dc={d:+.6f}   -C_k={-C[k]:+.6f}")
