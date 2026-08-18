#!/usr/bin/env python3
"""
tools/m4proper_T3000.py — M4-proper r' at T=3000 (S2-limit separation).

Goal (agy-wave22 adjudication, open item): r'(T) = (S2/S1)/L^2 with
  S1 = sum_{t<=T} |zeta'(rho)|^2, S2 = sum |zeta''(rho)|^2 over real zeros rho=1/2+it.
Measured series: 0.8168 (150), 0.8447 (300), 0.8623 (600), 0.8688 (900).
Candidates for r_inf: 0.87 (coordinator), 0.89 (own), 0.90 (CUE-flavored).
Separation needs T>=3000 where the asymptote bends visibly.

Parallel: split [14, 3000] into 8 t-ranges, one process each, merge S1/S2.
Each process: coarse sign-change bracketing of Siegel Z at step 0.5, bisect refine
to 1e-18, central-difference derivatives h=1e-5 (O(h^2), dps high enough).

Usage: nohup uv run --quiet --with mpmath python3 tools/m4proper_T3000.py > /tmp/m4_T3000.log 2>&1 &
"""
import multiprocessing as mp
import sys
import mpmath as mpm

mpm.mp.dps = 20  # cheap bracketing phase


def segment(Tlo, Thi, out_q):
    # fine phase precision
    mpm.mp.dps = 30
    z0 = mpm.siegelz(mpm.mpf(str(Tlo)))
    t = mpm.mpf(str(Tlo))
    brackets = []
    step = mpm.mpf("0.5")
    TM = mpm.mpf(str(Thi))
    while t < TM:
        tn = t + step
        zn = mpm.siegelz(tn)
        if z0 * zn < 0:
            brackets.append((t, tn))
        z0, zn = zn, tn
        t = tn
    # derivatives
    h = mpm.mpf("1e-5")
    S1 = mpm.mpf(0)
    S2 = mpm.mpf(0)
    N = 0
    last = None
    for (lo, hi) in brackets:
        try:
            r = mpm.findroot(mpm.siegelz, (lo, hi), solver="bisect",
                             tol=mpm.mpf("1e-18"), maxsteps=60)
        except Exception:
            r = (lo + hi) / 2
        if last is not None and abs(r - last) < mpm.mpf("1e-6"):
            continue
        s0 = mpm.mpc(mpm.mpf("0.5"), r)
        zp_h = mpm.zeta(s0 + h)
        zm_h = mpm.zeta(s0 - h)
        z1 = (zp_h - zm_h) / (2 * h)
        z2 = (zp_h - 2 * mpm.zeta(s0) + zm_h) / (h * h)
        S1 += abs(z1) ** 2
        S2 += abs(z2) ** 2
        N += 1
        last = r
    out_q.put((Thi, N, S1, S2))


def main():
    TMAX = 3000
    ranges = []
    lo = mpm.mpf("14.1")
    nseg = 8
    seglen = (mpm.mpf(TMAX) - lo) / nseg
    for i in range(nseg):
        a = lo + i * seglen
        b = lo + (i + 1) * seglen
        ranges.append((float(a), float(b)))
    print(f"T=3000 r' probe: {nseg} segments, step 0.5, bisect 1e-18, h=1e-5", flush=True)
    out_q = mp.Queue()
    procs = [mp.Process(target=segment, args=(a, b, out_q)) for (a, b) in ranges]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    items = sorted([out_q.get() for _ in procs])
    S1 = sum(i[2] for i in items)
    S2 = sum(i[3] for i in items)
    N = sum(i[1] for i in items)
    s = mpm.mpf(TMAX) / (2 * mpm.mpf(mpm.mp.pi))
    L = mpm.log(s)
    law1 = s * L ** 4 / 12
    rpr = (S2 / S1) / L ** 2
    print("segment results (Thi,N):", [(i[0], i[1]) for i in items], flush=True)
    print(f"RESULT Tmax={TMAX} N={N} Nest={mpm.nstr(s*(mpm.log(s)-1)+mpm.mpf('0.875'),6)} "
          f"S1/law1={mpm.nstr(S1/law1,6)} r'={mpm.nstr(rpr,7)}", flush=True)


if __name__ == "__main__":
    main()