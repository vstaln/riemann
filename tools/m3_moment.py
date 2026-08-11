#!/usr/bin/env python3
"""Compute m_k(lambda): moments of the sine-kernel Gram matrix K(u)=sinc(pi*lambda*u)
over the sine process (density 1), via the determinantal diagram expansion.

m_1 = 1
m_2 = 1 + A2,            A2 = int K(u)^2 rho2(u) du,  rho2(u) = 1 - S(u)^2
m_3 = 1 + 3*A2 + A3,
  A3 = intint K(u)K(v)K(u+v) rho3(u,v) dudv
  rho3(u,v) = 1 - S(u)^2 - S(v)^2 - S(u+v)^2 + 2 S(u)S(v)S(u+v)
  S(u) = sinc(pi u)  (sine kernel, density 1)
m_4 = 1 + 6 A2 + 3 A2^2(?) ... (we do full diagram for k=4 too)

All integrals via high-accuracy Gauss-type quadrature (scipy) or mpmath.
"""
import mpmath as mp
from mpmath import sinc, mpf, quad, inf

mp.mp.dps = 30

def S(u):
    """sine kernel density-1: sinc(pi u)"""
    return mp.sinc(mp.pi * u)

def K(u, lam):
    return mp.sinc(mp.pi * lam * u)

def m1(lam):
    return mpf(1)

def A2(lam):
    # int K(u)^2 (1 - S(u)^2) du over R
    def f(u):
        return K(u, lam)**2 * (1 - S(u)**2)
    return quad(f, [-inf, inf])

def m2(lam):
    return 1 + A2(lam)

def A3(lam):
    # intint K(u)K(v)K(u+v) [1 - S(u)^2 - S(v)^2 - S(u+v)^2 + 2 S(u)S(v)S(u+v)] du dv
    def f(u, v):
        w = u + v
        rho3 = 1 - S(u)**2 - S(v)**2 - S(w)**2 + 2*S(u)*S(v)*S(w)
        return K(u, lam)*K(v, lam)*K(w, lam)*rho3
    return quad(f, [-inf, inf], [-inf, inf])

def m3(lam):
    return 1 + 3*A2(lam) + A3(lam)

# k=4: tr G^4 = sum over partitions of {1,2,3,4}
#   (1|2|3|4): all distinct -> int K K K K rho4 (via rho4 = det[S], S(u_i-u_j))
#   exactly three equal (patterns i=j=k!=l etc, 4 choose 3 * ...): 4 * sum_{i!=j} K(0)^2 K(x_i-x_j)^2 * ... 
#   Let me do the standard counting:
#   tr G^4 = sum_{i,j,k,l} K_ij K_jk K_kl K_li
#   patterns: (i=j=k=l): K(0)^4 = 1 each -> contributes 1
#             (i=j=k != l): i=j=k, l free: K(0)^2 K(x_i-x_l)^2 -> 4 such patterns? indices (i,i,i,l): 4 ways to choose which of {i,j,k,l} is l. Each gives K(0)^3? 
#   Actually: pattern with exactly one index different: sum_{i!=l} K(0) K(x_i-x_l) K(0) K(x_l-x_i) = sum K(x_i-x_l)^2. Number of such patterns: choose the "lone" position among 4 = 4. So 4 * A2... wait K(0)=1.
#   pattern with two pairs: (i=j, k=l, i!=k): sum K(x_i-x_k)^2. Also (i=l, j=k): same. And (i=k, j=l): sum K(x_i-x_j) K(x_j-x_i) K(x_i-x_j)K(x_j-x_i) = sum K^4? hmm no: i=k, j=l: K_ij K_ji K_ij K_ji = K(x_i-x_j)^4.
#   Let me just enumerate partitions of {1,2,3,4}:
#   - {{1,2,3,4}}: 1
#   - {{1,2,3},{4}}: 4 partitions; each = sum_{i!=j} K(0)K(0)K(x_i-x_j)K(x_j-x_i) = sum K^2. Contribution 4*A2.
#   - {{1,2},{3,4}}: 3 partitions:
#       {{1,2},{3,4}}: sum_{i!=j} K_ij K_ji K_ij K_ji -> (i,j) with i in pair1... this is sum over distinct pairs: K(x_i-x_j)^4
#       {{1,3},{2,4}}: sum_{i!=j} K_ij K_jk K_kl K_li with i=k, j=l: K_ij^4 -> same sum K^4
#       {{1,4},{2,3}}: K_ij K_jk K_ki K_ij ... i=l, j=k: K_ij K_jj K_ji K_ii = K_ij^2... 
#   Hmm, let me be careful. tr G^4 = sum_{i,j,k,l} G_ij G_jk G_kl G_li.
#   partition {{1,2},{3,4}} (i=j, k=l, i!=k): term = G_ii G_ik G_kk G_ki = K(0)K(x_i-x_k)K(0)K(x_k-x_i) = K(x_i-x_k)^2. sum over i!=k: A2.
#   partition {{1,3},{2,4}} (i=k, j=l, i!=j): term = G_ij G_ji G_ij G_ji = K(x_i-x_j)^4. sum: D4 := int K(u)^4 du.
#   partition {{1,4},{2,3}} (i=l, j=k, i!=j): term = G_ij G_jj G_ji G_ii = K(x_i-x_j)^2. sum: A2.
#   So two-pair contribution: A2 (from {{1,2},{3,4}}) + D4 (from {{1,3},{2,4}}) + A2 (from {{1,4},{2,3}}) = 2A2 + D4.
#   - {{1},{2,3,4}} etc (single): same as {{1,2,3},{4}} by symmetry: 4*A2. Wait that's 4 partitions each giving A2. Hmm total so far: 1 + 4A2 + 2A2 + D4 = 1 + 6A2 + D4. But also all-distinct: {{1},{2},{3},{4}}: E[sum_{i,j,k,l all distinct} K_ijK_jkK_klK_li] = int K(x-y)K(y-z)K(z-w)K(w-x) rho4(x,y,z,w).
#   Total: m4 = 1 + 6 A2 + D4 + A4_all, where A4_all = intintint K(u)K(v)K(w)K(u+v+w)... with rho4.
#   Let me define rho4(x1..x4) = det[S(x_i-x_j)]_4x4, S(0)=1.
#   A4 = intintint K(u1)K(u2)K(u3)K(u1+u2+u3) rho4(u1,u2,u3,-u1-u2-u3) du1 du2 du3  (differences x1-x2=u1, x2-x3=u2, x3-x4=u3, x4-x1=-(u1+u2+u3))
#   det of 4x4 with 1 diag: rho4 = 1 - sum_{i<j} S_ij^2 + 2 sum_{i<j<k}(S_ij S_jk S_ki + ...)... the full determinant.
#   Let me just compute the 4x4 determinant symbolically numerically.
def det4(a,b,c,d,e,f):
    # matrix [[1,a,b,c],[a,1,d,e],[b,d,1,f],[c,e,f,1]]
    # expand: 1*(1*1 - f*f - d*(d*1 - f*e) + e*(d*f - 1*e)) ... let me just use mpmath matrix
    M = mp.matrix([[1,a,b,c],[a,1,d,e],[b,d,1,f],[c,e,f,1]])
    return mp.det(M)

def rho4_uvw(u, v, w):
    # points x1,x2,x3,x4 with x1-x2=u, x2-x3=v, x3-x4=w, x4-x1=-(u+v+w)
    # S_ij = S(x_i - x_j)
    S12 = S(u); S23 = S(v); S34 = S(w)
    S13 = S(u+v); S24 = S(v+w)
    S14 = S(u+v+w)
    return det4(S12, S13, S14, S23, S24, S34)

def A4(lam):
    def f(u, v, w):
        r4 = rho4_uvw(u, v, w)
        return K(u, lam)*K(v, lam)*K(w, lam)*K(u+v+w, lam)*r4
    return quad(f, [-inf, inf], [-inf, inf], [-inf, inf])

def D4(lam):
    def f(u):
        return K(u, lam)**4
    return quad(f, [-inf, inf])

def m4(lam):
    return 1 + 6*A2(lam) + D4(lam) + A4(lam)

if __name__ == "__main__":
    import sys
    lams = [mpf(x) for x in ("0.4","0.5","0.55","0.6","0.65","0.66","2/3","0.7","0.8","0.9","1.0")]
    print(f"{'lambda':>6} {'m2':>12} {'m3':>12} {'2m2-m3':>12} {'m4':>12}")
    for la in lams:
        try:
            m2v = m2(la); m3v = m3(la); m4v = m4(la)
            print(f"{float(la):6.3f} {float(m2v):12.6f} {float(m3v):12.6f} {float(2*m2v-m3v):12.6f} {float(m4v):12.6f}")
        except Exception as e:
            print(f"{float(la):6.3f} ERROR: {e}")
