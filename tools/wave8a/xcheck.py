import math
g = [float(x) for x in open('/home/vstaln/riemann/tools/data/zeros_rust_924k.txt')]
g1 = g[0]
def phi(gv): return math.atan2(gv,-0.5)-math.atan2(gv,0.5)
phis = [phi(x) for x in g]
def lam_real(n):
    return sum(2*(1-math.cos(n*p)) for p in phis)
def lam_control(n):
    base = lam_real(n) - 2*(1-math.cos(n*phi(g1)))
    tot = 0.0
    for sig in (0.6,0.4):
        for sgn in (1.0,-1.0):
            rho = complex(sig, sgn*g1)
            tn = ((rho-1.0)/rho)**n
            tot += 1.0 - tn.real
    return base+tot
for n in [89,178,266,355,444,1066,3552,3553]:
    print(n, "%.6f" % lam_control(n))
first=None
for n in range(1,5001,7):
    if lam_control(n) < 0: first=n; break
print("first neg (scan):", first)
first=None
m=1
while True:
    nres=int(round(2*math.pi*m*g1))
    if nres>60000: break
    if lam_control(nres) < 0 and first is None: first=nres
    m+=1
print("first neg (resonance):", first)
