import mpmath as mp, numpy as np
mp.mp.dps = 40
def prime_list(lim):
    sieve=np.ones(lim+1,dtype=bool); sieve[:2]=False
    for p in range(2,int(lim**0.5)+1):
        if sieve[p]: sieve[p*p::p]=False
    return [i for i in range(2,lim+1) if sieve[i]]
LIM=26; primes=prime_list(LIM)
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
Aconst=mp.mpf('0.5')*(mp.log(2*mp.pi)-(1-C0))
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
def primesum(t):
    et=mp.e**abs(mp.mpf(t)); ps=mp.mpf(0)
    for n,lam in Lam.items():
        if mp.mpf(n)<=et: ps+=lam/mp.sqrt(mp.mpf(n))*(abs(mp.mpf(t))-mp.log(n))
    return ps
def r(t):
    tt=mp.mpf(abs(t))
    return g(tt)-(mp.mpf('0.5')*tt*mp.log(tt)+Aconst*tt+primesum(tt))
def rpp_explicit(t):  # Suzuki: r''(t) = -(e^{|t|/2}+e^{-|t|/2}) + e^{-|t|/2}/(1-e^{-2|t|}) - 1/(2|t|)
    t=mp.mpf(abs(t))
    if t==0: return mp.mpf(0)
    return (-(mp.e**(t/2)+mp.e**(-t/2)) + mp.e**(-t/2)/(1-mp.e**(-2*t)) - 1/(2*t))
h=mp.mpf('1e-3')
print("t      r''(numeric)        r''(explicit)       diff")
for t0 in [0.2,0.4,0.6,0.8,1.0,1.2,1.5,2.0]:
    t=mp.mpf(t0)
    rpp_num=(r(t+h)-2*r(t)+r(t-h))/(h*h)
    rpp_exp=rpp_explicit(t)
    print(f"{t0:4.1f}  {float(rpp_num): .6e}   {float(rpp_exp): .6e}   {float(abs(rpp_num-rpp_exp)): .2e}")
