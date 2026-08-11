import mpmath as mp, numpy as np
mp.mp.dps = 30
a = 0.9
def v(x):
    x=np.asarray(x,dtype=float); t=a*a-x*x
    return np.where(np.abs(x)<a, np.exp(-1.0/t),0.0)
def vp(x):
    x=np.asarray(x,dtype=float); t=a*a-x*x
    return np.where(np.abs(x)<a, np.exp(-1.0/t)*(-2.0*x)/(t*t),0.0)
def quad1(lo,hi,nsub,n=12):
    xg,wg=np.polynomial.legendre.leggauss(n); xs=[];ws=[]
    for k in range(nsub):
        l=lo+(hi-lo)*k/nsub; h=lo+(hi-lo)*(k+1)/nsub
        xs.append((xg+1)/2*(h-l)+l); ws.append(wg*(h-l)/2)
    return np.concatenate(xs),np.concatenate(ws)
xq,wq=quad1(-a,a,500)
vvp=vp(xq); vv=v(xq)
for n in (2,3,4,5,7):
    ln=np.log(n)
    if ln >= 2*a: print(f"n={n}: log n = {ln:.4f} >= 2a = {2*a}, skip"); continue
    D=xq[:,None]-xq[None,:]
    kern=np.where(np.abs(D)>=ln, np.abs(D)-ln, 0.0)
    LHS=np.sum(wq[:,None]*wq[None,:]*kern*vvp[:,None]*vvp[None,:])
    m1=(xq>=-a)&(xq<=a-ln); R1=np.sum(wq[m1]*v(xq[m1]+ln)*v(xq[m1]))
    m2=(xq>=-a+ln)&(xq<=a);   R2=np.sum(wq[m2]*v(xq[m2]-ln)*v(xq[m2]))
    RHS=-(R1+R2)
    print(f"n={n}: LHS = {LHS:.8e}  RHS = {RHS:.8e}  |diff| = {abs(LHS-RHS):.2e}")
