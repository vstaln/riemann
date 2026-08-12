from mpmath import mp, mpf, sqrt, tan, nstr
mp.dps = 60

print("=== CLAIM 1: ceiling coefficient 1/(6*256^2) vs 2.55e-6 vs 2.5431316e-6 ===")
exact = mpf(1)/(6*mpf(256)**2)
print("1/(6*256^2)  =", nstr(exact, 22))
print("2.55e-6       =", nstr(mpf("2.55e-6"), 22))
print("2.5431316e-6  =", nstr(mpf("2.5431316e-6"), 22))
print("ratio 2.55e-6/exact      =", nstr(mpf("2.55e-6")/exact, 12))
print("ratio 2.5431316e-6/exact =", nstr(mpf("2.5431316e-6")/exact, 12))

print("\n=== p0 exact fraction vs our 0.6818286874638315 ===")
num = 10909258999421303588095230195816054408197
den = 16000000000000000000000000000000000000000
p0 = mpf(num)/mpf(den)
print("p0 exact =", nstr(p0, 24))
print("our p0   = 0.6818286874638315 ; diff =", nstr(p0 - mpf("0.6818286874638315"), 10))

print("\n=== ceiling display constant ===")
print("0.6818287 + 2.55e-6  =", nstr(mpf("0.6818287")+mpf("2.55e-6"), 20))
print("p0 + 1/(6*256^2)     =", nstr(p0 + exact, 20))
print("p0 + 2.5431316e-6    =", nstr(p0 + mpf("2.5431316e-6"), 20))

print("\n=== CLAIM 2: Thm D constant ===")
th = mpf(1)/sqrt(2)
c1 = sqrt(2)*tan(th)/(1 + th*tan(th))
d = mpf(2) - 1/c1
print("c1*     =", nstr(c1, 16))
print("2-1/c1* =", nstr(d, 16))
our = mpf("0.6732660791400006829")
print("OUR record          =", nstr(our, 22))
print("gap (our - (2-1/c1*)) =", nstr(our - d, 20), "  our bigger:", our > d)
print("(3-1/c1*)/2 =", nstr((mpf(3)-1/c1)/2, 16))

print("\n=== CLAIM 3: near-CUE rows from LawN256 enclosures ===")
K = 2**140
import re
txt = open("/root/riemann/research/external-results/anthropic-zeta23/bundle/LawN256.lean").read()
pairs = re.findall(r"\((\d+), (\d+)\)", txt)
pairs = [(int(a), int(b)) for a,b in pairs]
print("num enclosures parsed:", len(pairs), " K=2^140 ok:", K == 1393796574908163946345982392040522594123776)
for j in (1,2,3,128,255,256):
    lo, hi = pairs[j-1]
    Slo, Shi = mpf(lo)/mpf(K), mpf(hi)/mpf(K)
    if j < 256:
        rlo, rhi = mpf(256)*Slo - j, mpf(256)*Shi - j
        print(f"j={j:3d}: 256*S-j in [{nstr(rlo,8)},{nstr(rhi,8)}]")
    else:
        print(f"j={j:3d}: S/K in [{nstr(Slo,8)},{nstr(Shi,8)}]  (free row)")
print("worst deviations over j=1..255:")
worst_lo, worst_hi = mpf(0), mpf(0)
for j in range(1, 256):
    lo, hi = pairs[j-1]
    a = mpf(256)*mpf(lo)/mpf(K) - j
    b = j - mpf(256)*mpf(hi)/mpf(K)
    worst_lo = max(worst_lo, a); worst_hi = max(worst_hi, b)
print("max(256*lo/K - j) =", nstr(worst_lo, 8), " max(j - 256*hi/K) =", nstr(worst_hi, 8), " (enclosure width half = 128/K =", nstr(mpf(128)/mpf(K), 8), ")")

print("\n=== CLAIM 4: family law extrapolation to N=256 ===")
for c in (0.7887, 0.8315):
    for a in (0.39, 0.3925, 0.4037):
        print(f"c={c}, a={a}: 1 - c*256^-a = {nstr(mpf(1 - c*256**(-a)), 12)}")
print("actual p0(256) =", nstr(p0, 12))

print("\n=== CLAIM 6: our m3 closed forms vs sine-kernel moments mk(lambda) ===")
# our formula: m3 = 1+3(1/l - 2J2)+1/l^2-(6/l)J2+2(1-l/2), J2=integral sinc(pi l u)^2 sinc(pi u)^2 du
def J2(l):
    return mp.quad(lambda u: (mp.sinc(mp.pi*l*u))**2 * (mp.sinc(mp.pi*u))**2, [0, mp.inf])
def m3(l):
    J = J2(l)
    return 1 + 3*(1/l - 2*J) + 1/l**2 - (6/l)*J + 2*(1 - l/2)
for l in (mpf(1)/2, mpf(2)/3, mpf(1)):
    print(f"lambda={nstr(l,4)}: J2={nstr(J2(l),12)}  m3={nstr(m3(l),12)}")
print("paper mk(1) = 1, 3/4, 2, 13/4 for k<=4  -> m3(1)=2 expected")
