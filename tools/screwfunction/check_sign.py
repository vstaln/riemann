import numpy as np
a = 1.0
def v(x):
    x=np.asarray(x,dtype=float); t=a*a-x*x
    return np.where(np.abs(x)<a, np.exp(-1.0/t),0.0)
def vp(x):
    x=np.asarray(x,dtype=float); t=a*a-x*x
    return np.where(np.abs(x)<a, np.exp(-1.0/t)*(-2.0*x)/(t*t),0.0)
xg0,wg0=np.polynomial.legendre.leggauss(12)
def quad1(lo,hi,nsub):
    xs=[];ws=[]
    for k in range(nsub):
        l=lo+(hi-lo)*k/nsub; h=lo+(hi-lo)*(k+1)/nsub
        xs.append((xg0+1)/2*(h-l)+l); ws.append(wg0*(h-l)/2)
    return np.concatenate(xs),np.concatenate(ws)
xq,wq=quad1(-a,a,400); vvp=vp(xq); vv=v(xq)
nrm2 = np.sum(wq*vv**2); ivp2 = np.sum(wq*vvp**2)
print(f"||v||^2 = {nrm2:.8e}   int v'^2 = {ivp2:.8e}   2||v||^2 = {2*nrm2:.8e}")
# (v'*v')(0) = int v'(y)v'(-y)dy = -int v'^2  (v' odd)
vpsv0 = np.sum(wq*vp(xq)*vp(-xq))
print(f"(v'*v')(0) computed = {vpsv0:.8e}   -int v'^2 = {-ivp2:.8e}")
# int|u|(v'*v')(u)du
def vpsv(u):
    lo=max(-a,u-a); hi=min(a,u+a)
    m=(xq>=lo)&(xq<=hi); y=xq[m]; wy=wq[m]
    return np.sum(wy*vp(y)*vp(u-y))
tot=0.0
for (lo,hi) in [(-2*a,0.0),(0.0,2*a)]:
    u,wu=quad1(lo,hi,400)
    for i in range(len(u)): tot += wu[i]*abs(u[i])*vpsv(u[i])
print(f"int|u|(v'*v')(u)du = {tot:.8e}   vs 2||v||^2 = {2*nrm2:.8e}")
# direct 2D: intint|x-y| v'(x)v'(y)
D = xq[:,None]-xq[None,:]
I2d = np.sum(wq[:,None]*wq[None,:]*np.abs(D)*vvp[:,None]*vvp[None,:])
print(f"intint|x-y| v'(x)v'(y) dxdy = {I2d:.8e}   vs -2||v||^2 = {-2*nrm2:.8e}")
