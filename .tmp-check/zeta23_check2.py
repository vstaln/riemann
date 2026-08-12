from mpmath import mp, mpf, sqrt, tan, cot, nstr
mp.dps = 50
th = mpf(1)/sqrt(2)
c1 = sqrt(2)*tan(th)/(1+th*tan(th))
print("c1* (README)           =", nstr(c1, 16))
print("2-1/c1*                =", nstr(2-1/c1, 16))
print("3/2 - cot(1/sqrt2)/sqrt2 =", nstr(mpf(3)/2 - cot(th)/sqrt(2), 16))
print("matches? ", abs((2-1/c1) - (mpf(3)/2 - cot(th)/sqrt(2))) < mpf("1e-40"))
# paper-appendix alternative reading 2*tan(th)/(1+th*tan(th)):
cMT_alt = 2*tan(th)/(1+th*tan(th))
print("alt cMT := 2*tan(th)/(1+th*tan(th)) =", nstr(cMT_alt, 10), " -> 2-1/cMT =", nstr(2-1/cMT_alt, 10))

print("\n=== claim 5 headroom ===")
p0 = mpf(10909258999421303588095230195816054408197)/mpf(16000000000000000000000000000000000000000)
e1 = mpf(1)/(6*mpf(256)**2)
ceiling = p0 + e1
our = mpf("0.6732660791400006829")
print("ceiling constant (r(1)=0, flat r) =", nstr(ceiling, 16))
print("our record =", nstr(our, 16))
print("gap =", nstr(ceiling - our, 16))
print("our/ceiling ratio =", nstr(our/ceiling, 10), " -> headroom =", nstr(100*(1-our/ceiling), 8), "%")
print("record vs Thm-D 0.67250:", nstr(our - (2-1/c1), 16))

print("\n=== family-law at N=256 vs p0, and vs family measurements ===")
for c,a in ((0.7887,0.3925),(0.8315,0.4037),(0.7887,0.39),(0.8315,0.39)):
    print(f"1-{c}*256^-{a} = {nstr(mpf(1-c*256**(-a)),8)}")
print("family measurements N=256: 0.90715/0.91745/0.92250 (family_law.log)")
print("LP-optimal p0(256) =", nstr(p0, 8))
