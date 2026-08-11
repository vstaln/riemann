#!/usr/bin/env python3
"""Christoffel function Lambda_2(0) for the moment sequence (1, m1, m2, m3, m4)
and the one-sided bound n+/d >= 1 - Lambda_2(0) (paper 7.5(d)-(f)).
Compare paper's moments (m3=2, m4=13/4) vs verified moments (m3=2, m4=346/105).
Orthonormal polys via Cholesky of the Hankel matrix H_{ij} = m_{i+j}, i,j in 0..m.
p_j(0): value at 0 of the j-th orthonormal polynomial.
"""
import numpy as np

def christoffel(mom, deg):
    # mom[0..2*deg]: moments m_0..m_{2deg}
    H = np.array([[mom[i+j] for j in range(deg+1)] for i in range(deg+1)])
    L = np.linalg.cholesky(H)          # H = L L^T
    Lm = np.linalg.inv(L)              # L^{-1}
    # orthonormal polynomials: p = L^{-T} * (monomial basis)  -> p_j(x) = sum_k (L^{-1})_{jk} x^k
    # value at 0: p_j(0) = (L^{-1})_{j,0} for j=0..deg (only constant term)
    p0 = Lm[:, 0]
    lam = 1.0 / np.sum(p0**2)
    return lam

m1 = 1.0; m2 = 4/3; m3 = 2.0
for name, m4 in [("paper 13/4", 13/4), ("verified 346/105", 346/105)]:
    mom = [1.0, m1, m2, m3, m4]
    L2 = christoffel(mom, 2)
    print(f"m4 = {name}: Lambda_2(0) = {L2:.6f}   1 - Lambda_2(0) = {1-L2:.6f}   (paper claims 5/36={5/36:.6f} -> 31/36 = {31/36:.6f}, and 13/18 = {13/18:.6f} via Prop 4.5 count)")

# also check the paper's claim Lambda_2(0;1)=5/36 reproduces 1-5/36=31/36 > 13/18: note paper says
# "HL*(4,lambda) for all lambda<1 would give lim inf N_s/N >= 13/18 via the count of Proposition 4.5"
# i.e. the bound is 13/18 (a different count), not 31/36; both recorded.
