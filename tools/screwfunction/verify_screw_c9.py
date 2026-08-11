#!/usr/bin/env python3
"""Two checks on the L-side at a=1.0 (exp-bump):
1. L components: L0 (via (2.4), verified) and L1 = -int g1(u)(v'*v')(u)du, very fine grid.
2. Suzuki (2.5): for a prime power n,
   intint (|x-y|-log n) 1_{|x-y|>=log n} v'(y)v'(x) dxdy
     ==  -[ int v(x+log n)v(x)dx + int v(x-log n)v(x)dx ]
"""
import mpmath as mp
import numpy as np

mp.mp.dps = 32

def prime_list(lim):
    sieve = np.ones(lim+1, dtype=bool); sieve[:2]=False
    for p in range(2,int(lim**0.5)+1):
        if sieve[p]: sieve[p*p::p]=False
    return [i for i in range(2,lim+1) if sieve[i]]

def make_g(TMAX):
    LIM = int(np.ceil(np.exp(TMAX)))+5
    primes = prime_list(LIM)
    C0 = mp.euler; psi14 = -(mp.pi/2)-3*mp.log(2)-C0; Phi1 = mp.zeta(2, mp.mpf('0.25'))
    Lam = {}
    for n in range(2,LIM+1):
        nn=n; lam=mp.mpf(0); found=False
        for p in primes:
            if p*p>nn: break
            if nn%p==0:
                found=True; m=0
                while nn%p==0: nn//=p; m+=1
                if nn==1: lam=mp.mpf(m)*mp.log(p)
                break
        if not found and nn==n: lam=mp.log(n)
        Lam[n]=lam
    def lerch(t):
        t=mp.mpf(t)
        if t==0: return Phi1
        z=mp.e**(-2*t)
        if t < mp.mpf('0.05'): return mp.lerchphi(z,2,mp.mpf('0.25'))
        acc=mp.mpf(0); k=0
        while True:
            term=z**k/(k+mp.mpf('0.25'))**2
            acc+=term
            if abs(term)<mp.mpf('1e-40'): break
            k+=1
        return acc
    def g(t):
        tt=mp.mpf(abs(t)); et=mp.e**tt
        ps=mp.mpf(0)
        for n,lam in Lam.items():
            if mp.mpf(n)<=et: ps+=lam/mp.sqrt(mp.mpf(n))*(tt-mp.log(n))
        Phi2=lerch(tt)
        return (-4*(mp.e**(tt/2)+mp.e**(-tt/2)-2)+ps-(tt/2)*(psi14-mp.log(mp.pi))
                -mp.mpf('0.25')*(Phi1-mp.e**(-tt/2)*Phi2))
    return g,Lam

def main():
    import time
    g, Lam = make_g(3.0)
    a = 1.0
    def v(x):
        x = np.asarray(x, dtype=float)
        t = a*a - x*x
        return np.where(np.abs(x) < a, np.exp(-1.0/t), 0.0)
    def vp(x):
        x = np.asarray(x, dtype=float)
        t = a*a - x*x
        return np.where(np.abs(x) < a, np.exp(-1.0/t)*(-2.0*x)/(t*t), 0.0)
    # fine composite GL for 1D and 2D
    xg0, wg0 = np.polynomial.legendre.leggauss(12)
    def quad1(lo, hi, nsub):
        xs=[]; ws=[]
        for k in range(nsub):
            l = lo + (hi-lo)*k/nsub; h = lo + (hi-lo)*(k+1)/nsub
            xs.append((xg0+1)/2*(h-l)+l); ws.append(wg0*(h-l)/2)
        return np.concatenate(xs), np.concatenate(ws)
    # ---- L0 via (2.4) ----
    xq, wq = quad1(-a, a, 400)
    vv = v(xq); vvp = vp(xq)
    nrm2 = np.sum(wq*vv**2)
    Ilog = np.sum(wq*np.log(a*a - xq*xq)*vv**2)
    D = xq[:,None]-xq[None,:]
    Dsafe = np.where(np.abs(D)<1e-30, 1e-30, D)
    Ijump = 0.25*np.sum(wq[:,None]*wq[None,:]*(vv[:,None]-vv[None,:])**2/np.abs(Dsafe))
    La = Ijump - 0.5*Ilog
    L0 = La - nrm2
    print(f"a=1.0: L0 = {L0:.8e}  (nrm2={nrm2:.6e}, La={La:.6e})", flush=True)
    # ---- L1 via 1D with fine grid and direct g1 evals (memoized by |u|) ----
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def g1(t):
        return float(g(t)) - (0.5*abs(t)*np.log(abs(t)) if t != 0 else 0.0)
    def vpsv(u):
        lo = max(-a, u-a); hi = min(a, u+a)
        m = (xq >= lo) & (xq <= hi)
        y = xq[m]; wy = wq[m]
        return np.sum(wy*vp(y)*vp(u-y))
    L1 = 0.0
    for (lo, hi) in [(-2*a, 0.0), (0.0, 2*a)]:
        u, wu = quad1(lo, hi, 400)
        for i in range(len(u)):
            L1 += wu[i]*g1(u[i])*vpsv(u[i])
    L1 = -L1
    print(f"a=1.0: L1 = {L1:.8e}   L = L0+L1 = {L0+L1:.8e}", flush=True)
    # ---- check 2: (2.5) for n = 2 (log2 = 0.6931), n = 5 ----
    for n in (2, 5):
        ln = np.log(n)
        # LHS: intint (|x-y|-ln) 1_{|x-y|>=ln} v'(y)v'(x)
        xq2, wq2 = quad1(-a, a, 400)
        vv2 = vp(xq2)
        D2 = xq2[:,None]-xq2[None,:]
        kern = np.where(np.abs(D2) >= ln, np.abs(D2)-ln, 0.0)
        LHS = np.sum(wq2[:,None]*wq2[None,:]*kern*vv2[:,None]*vv2[None,:])
        # RHS: -[ int v(x+ln)v(x) + int v(x-ln)v(x) ]
        # RHS: -[ int v(x+ln)v(x)dx (x in [-a, a-ln]) + int v(x-ln)v(x)dx (x in [-a+ln, a]) ]
        m1 = (xq2 >= -a) & (xq2 <= a-ln)         # x+ln in [-a,a]
        R1 = np.sum(wq2[m1]*v(xq2[m1]+ln)*v(xq2[m1]))
        m2 = (xq2 >= -a+ln) & (xq2 <= a)         # x-ln in [-a,a]
        R2 = np.sum(wq2[m2]*v(xq2[m2]-ln)*v(xq2[m2]))
        RHS = -(R1 + R2)
        print(f"(2.5) n={n}: LHS = {LHS:.8e}  RHS = {RHS:.8e}  |diff| = {abs(LHS-RHS):.2e}")

if __name__ == '__main__':
    main()
