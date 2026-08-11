#!/usr/bin/env python3
"""Screw-function identity L == Z, vpsv fixed with proper composite GL on [lo,hi]."""
import mpmath as mp
import numpy as np
from functools import lru_cache
mp.mp.dps = 32

def prime_list(lim):
    sieve=np.ones(lim+1,dtype=bool); sieve[:2]=False
    for p in range(2,int(lim**0.5)+1):
        if sieve[p]: sieve[p*p::p]=False
    return [i for i in range(2,lim+1) if sieve[i]]
def make_g(TMAX):
    LIM=int(np.ceil(np.exp(TMAX)))+5; primes=prime_list(LIM)
    C0=mp.euler; psi14=-(mp.pi/2)-3*mp.log(2)-C0; Phi1=mp.zeta(2,mp.mpf('0.25'))
    Lam={}
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
        if t<mp.mpf('0.05'): return mp.lerchphi(z,2,mp.mpf('0.25'))
        acc=mp.mpf(0); k=0
        while True:
            term=z**k/(k+mp.mpf('0.25'))**2
            acc+=term
            if abs(term)<mp.mpf('1e-40'): break
            k+=1
        return acc
    def g(t):
        tt=mp.mpf(abs(t)); et=mp.e**tt; ps=mp.mpf(0)
        for n,lam in Lam.items():
            if mp.mpf(n)<=et: ps+=lam/mp.sqrt(mp.mpf(n))*(tt-mp.log(n))
        Phi2=lerch(tt)
        return (-4*(mp.e**(tt/2)+mp.e**(-tt/2)-2)+ps-(tt/2)*(psi14-mp.log(mp.pi))
                -mp.mpf('0.25')*(Phi1-mp.e**(-tt/2)*Phi2))
    return g,Lam
g,Lam = make_g(3.0)

def quad1(lo,hi,nsub,n=12):
    xg,wg=np.polynomial.legendre.leggauss(n); xs=[];ws=[]
    for k in range(nsub):
        l=lo+(hi-lo)*k/nsub; h=lo+(hi-lo)*(k+1)/nsub
        xs.append((xg+1)/2*(h-l)+l); ws.append(wg*(h-l)/2)
    return np.concatenate(xs),np.concatenate(ws)

def bump(a):
    af=float(a)
    def v(x):
        x=np.asarray(x,dtype=float); t=af*af-x*x
        return np.where(np.abs(x)<af, np.exp(-1.0/t),0.0)
    def vp(x):
        x=np.asarray(x,dtype=float); t=af*af-x*x
        return np.where(np.abs(x)<af, np.exp(-1.0/t)*(-2.0*x)/(t*t),0.0)
    return v,vp

for a in (0.6, 1.0, 1.5):
    af=float(a); v,vp=bump(a)
    xq,wq=quad1(-af,af,500)
    vv=v(xq)
    # Z
    vh=np.zeros(1000,dtype=complex)
    for i in range(0,1000,100):
        gb=np.array([float(l.split()[1]) for l in open('/home/vstaln/riemann/tools/data/zeros_1_1000.txt')])[i:i+100]
        vh[i:i+100]=(np.cos(np.outer(gb,xq))@(wq*vv))+1j*(np.sin(np.outer(gb,xq))@(wq*vv))
    Z=2.0*np.sum(np.abs(vh)**2)
    # L0 via (2.4)
    vvp=vp(xq)
    nrm2=np.sum(wq*vv**2)
    Ilog=np.sum(wq*np.log(af*af-xq*xq)*vv**2)
    D=xq[:,None]-xq[None,:]; Dsafe=np.where(np.abs(D)<1e-30,1e-30,D)
    Ijump=0.25*np.sum(wq[:,None]*wq[None,:]*(vv[:,None]-vv[None,:])**2/np.abs(Dsafe))
    La=Ijump-0.5*Ilog
    L0=La-nrm2
    # L1 with FIXED vpsv (proper quadrature on overlap)
    @lru_cache(maxsize=None)
    def vpsv(u):
        lo=max(-af,u-af); hi=min(af,u+af)
        if hi<=lo: return 0.0
        y,wy=quad1(lo,hi,20)
        return np.sum(wy*vp(y)*vp(u-y))
    L1=0.0
    for (lo,hi) in [(-2*af,0.0),(0.0,2*af)]:
        u,wu=quad1(lo,hi,200)
        for i in range(len(u)):
            L1 += wu[i]*float(g(u[i]))*vpsv(u[i])
    L1=-L1
    L=L0+L1
    print(f"a={a}: Z = {Z:.8e}   L = {L:.8e}  (L0={L0:.6e}, L1={L1:.6e})   |Z-L| = {abs(Z-L):.3e}  rel={abs(Z-L)/max(abs(Z),1e-99):.3e}")
