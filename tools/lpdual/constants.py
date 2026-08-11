import mpmath as mp
mp.mp.dps = 30
# Theorem D constant: HD(1) = 3/2 - (1/sqrt(2)) cot(1/sqrt(2))  [Functional.lean: HD_one]
c = mp.mpf(3)/2 - (1/mp.sqrt(2))*mp.cot(1/mp.sqrt(2))
print("HD(1) =", mp.nstr(c, 22))
# cStar(1)
cs = mp.sqrt(2)*mp.sin(1/mp.sqrt(2))/(mp.cos(1/mp.sqrt(2)) + (1/mp.sqrt(2))*mp.sin(1/mp.sqrt(2)))
print("cStar(1) =", mp.nstr(cs, 22), " 2-1/c* =", mp.nstr(2 - 1/cs, 22))
print("p0 =", mp.nstr(mp.mpf('10909258999421303588095230195816054408197')/mp.mpf('16000000000000000000000000000000000000000'), 25))
print("p0+|E(1)| =", mp.nstr(mp.mpf('10909258999421303588095230195816054408197')/mp.mpf('16000000000000000000000000000000000000000') + mp.mpf('2.5431315104166665e-6'), 22))
print("gap 0.6818312 - 0.6725007 =", mp.nstr(mp.mpf('0.681831230595') - c, 12))
