# Refined legality: use the ACTUAL family window X = q^lambda (not the lambda=1 upper bound),
# and sweep the Gevrey constant c to find the threshold where the tail becomes o(1).
# tail_gevrey / N  where N ~ T*ell/(2pi) is the family zero count, T=(log q)^c.
import math

def ell(q, T):
    return math.log(q*T/(2*math.pi)) + 2*math.log(2) - 1

def lambda_f(q, T, eps=0.01):
    return (1-eps)*math.log(q)/ell(q, T)

def tail_rel(q, T, c_g, s=0.5, eps=0.01):
    D0 = math.sqrt(T)
    lam = lambda_f(q, T, eps)
    X = q**lam   # actual family window X = q^lambda (the legal window)
    N = T*ell(q,T)/(2*math.pi)
    # |eE|/N ~ X^{1/2} log(4T) D0^{-2} exp(-2 c_g D0^{1/s}) / N
    return math.sqrt(X)*math.log(4*T)/(D0*D0) * math.exp(-2*c_g*D0**(1/s)) / N

print("Tail/N under Gevrey taper, sweep of Gevrey constant c (s=1/2):")
print("(theorem holds when tail/N = o(1), i.e. <~ 0.01)")
print(f"{'q':>7} {'c_pow':>5} {'lam_F':>7} {'c=0.1':>9} {'c=0.5':>9} {'c=1.0':>9} {'c=1.5':>9} {'c=2.0':>9}")
for q in [101, 1009, 10007, 100003]:
    for cp in [1, 2, 3]:
        T = math.log(q)**cp
        lf = lambda_f(q, T)
        row = [f"{tail_rel(q,T,c):.1e}" for c in [0.1, 0.5, 1.0, 1.5, 2.0]]
        print(f"{q:>7} {cp:>5} {lf:>7.3f} {row[0]:>9} {row[1]:>9} {row[2]:>9} {row[3]:>9} {row[4]:>9}")
print()
print("Interpretation: the measured Gevrey constant for the C^3 ramp is c~1.5-2 (gevrey_tail2.py).")
print("Even c=0.5 suffices at (101,1) and (1009,2); c=1.0 suffices everywhere shown.")
