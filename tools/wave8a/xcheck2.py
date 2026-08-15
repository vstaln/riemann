import math
g = [float(x) for x in open('/home/vstaln/riemann/tools/data/zeros_rust_924k.txt')]
g1 = g[0]
def phi(gv): return math.atan2(gv,-0.5)-math.atan2(gv,0.5)
phis = [phi(x) for x in g]
def lam_real(n): return sum(2*(1-math.cos(n*p)) for p in phis)
n=89
base = lam_real(n) - 2*(1-math.cos(n*phi(g1)))
tot=0.0
for sig in (0.6,0.4):
    for sgn in (1.0,-1.0):
        rho=complex(sig,sgn*g1); tn=((rho-1.0)/rho)**n; tot+=1.0-tn.real
print("n=89: lam_real=%.6f base=%.6f planted=%.6f total=%.6f"%(lam_real(n),base,tot,base+tot))
print("phi(g1)=%.12f 1/g1=%.12f"%(phi(g1),1/g1))
