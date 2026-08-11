#!/usr/bin/env python3
"""B4.1 (biology note): twin-moment arithmetic on the 5/6 wall.

Q: do the spectral twins of the extremal law (same tr, same HS^2) share the
third (and higher) moments?  If they share m3=2=GUE, the third-moment input
cannot act by *excluding the twins*; the fourth-moment divergence vs GUE is
then the arithmetic reason even moments help and odd moments don't
(paper 7.5(e) vs HL*(4,lam) -> 13/18).

Extremal law (N=256 crystal, ideal model): eigenvalue law 2/3 at 1, 1/6 at 2,
1/6 at 0  ->  tr/N = 1,  HS2/N = 4/3,  m_k = (2/3)*1 + (1/6)*2^k.
All-simple world with the SAME (tr,HS2): integer spectra of (N, 4N/3).

Run:  uv run --quiet python twin_m3.py
"""
import itertools, sys

def integer_spectra(N):
    """All integer multisets (non-increasing) length N, sum = N, sumsq = 4N/3.
    Returns list of tuples (padded with zeros)."""
    target_sq = 4 * N // 3
    assert target_sq * 3 == 4 * N, f"N={N} not divisible by 3"
    out = []
    def rec(rem, sq, maxv, cur):
        if rem == 0:
            if sq == target_sq:
                out.append(tuple(cur + [0] * (N - len(cur))))
            return
        if sq > target_sq:
            return
        # upper bound: can we reach target_sq from here with all remaining = 1?
        # min possible extra squares: (rem)*1^2 = rem; max: rem * maxv^2
        if sq + rem > target_sq:
            return  # all-ones still overshoots -> prune
        for v in range(min(maxv, rem), 0, -1):
            rec(rem - v, sq + v * v, v, cur + [v])
    rec(N, 0, N, [])
    return out

def moments(spec):
    n = len(spec)
    return [sum(x ** k for x in spec) / n for k in range(1, 6)]

print("=== B4.1 twin-moment arithmetic ===")
print("Extremal-law moment sequence m_k = 2/3 + 2^k/6 (k=1..5):",
      [round(2/3 + 2**k/6, 6) for k in range(1, 6)])
print("GUE/HL* sequence (k=1..4, from [AM]): [1, 4/3, 2, 13/4]  (m5 not in our notes)")

for N in (6, 12, 24, 48):
    fam = integer_spectra(N)
    # unique moment profiles
    prof = {}
    spec_of = {}
    for spec in fam:
        m = tuple(round(x, 10) for x in moments(spec))
        prof[m] = prof.get(m, 0) + 1
        spec_of.setdefault(m, spec)
    print(f"\nN={N}: {len(fam)} integer spectra of (tr,HS2)=(N,4N/3); "
          f"{len(prof)} distinct (m1..m5) profiles:")
    for m, cnt in sorted(prof.items()):
        spec = spec_of[m]
        # show the nonzero part only
        nz = tuple(x for x in spec if x > 0)
        print(f"   profile {m}  x{cnt}   e.g. nonzero spec {nz}")
    m3s = {m[2] for m in prof}
    m4s = {m[3] for m in prof}
    print(f"   m3 values: {sorted(m3s)}   m4 values: {sorted(m4s)}")
    print(f"   extremal profile present (m3=2, m4=10/3)? "
          f"{any(abs(m[2]-2) < 1e-9 and abs(m[3]-10/3) < 1e-9 for m in prof)}")
