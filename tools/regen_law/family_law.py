#!/usr/bin/env python3
"""family_law.py — extend min p1(N) to N=128/256, multi-seed, fit the exact law.

Budgets (identical to final_numbers.py):
  pointwise : |sum w f(j) - j| <= tau (j=1..N-1), F(N) bound from |D(1)|<=d1, sum w = 1.
  cumulative: |D(1)|<=d1, |E(1)|<=1/(6N^2)+tau/(2N)  (rowE = sum_j f(j)(1-j/N)/N^2, |rowE-1/6|<=Mv).
Family: common2.gen_valid_family (VALID: sum marks = N, s_c = N-2d). NOT common.gen_family_vec (BUGGY).
Reuses spectra_valid. Solver: scipy.optimize.linprog HiGHS.

Run: cd tools/regen_law && python3 family_law.py
"""
import sys, time, json, numpy as np
from scipy.optimize import linprog
sys.path.insert(0, '/root/riemann/tools/regen_law')
from common2 import gen_valid_family, spectra_valid

D1 = 0.82395317
TAU = 3e-40
NS = [8, 16, 32, 64, 128, 256]
SEEDS = [42, 1234, 2024]
NC = {8: 8000, 16: 8000, 32: 5000, 64: 4000, 128: 3000, 256: 2500}
TB = 0.6725007036794116  # Theorem-B constant

def run_both(N, nc, seed):
    """Generate one family, run pointwise + cumulative LPs. Returns dict."""
    X, M, s_c = gen_valid_family(N, nc, seed=seed)
    F = spectra_valid(X, M, N)
    m = len(F)
    out = {'N': N, 'seed': seed, 'nc': nc, 'nconfigs': m,
           'support': int((np.ones(m) > 0).sum())}
    # ---- pointwise ----
    A_ub, b_ub = [], []
    for jj in range(N-1):
        A_ub.append(F[:, jj]); b_ub.append((jj+1) + TAU)
        A_ub.append(-F[:, jj]); b_ub.append(-(jj+1) + TAU)
    Fb = N*N*(D1 + 0.5) - N*(N-1)//2
    A_ub.append(F[:, N-1]); b_ub.append(Fb)
    A_eq = np.ones((1, m)); b_eq = [1.0]
    t = time.time()
    res = linprog(s_c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0, None)]*m, method='highs')
    out['pw_dt'] = time.time() - t
    if res.success:
        out['pw_p1'] = float(res.fun)/N
        out['pw_support'] = int((res.x > 1e-9).sum())
        # E(1) from the LP solution: rowE - 1/6 (note convention E(1)=rowE-1/6 = -1/(6N^2) exact rows)
        wts = np.array([(1-(jj+1)/N) for jj in range(N)])
        rowE = float(F @ wts @ res.x / N**2)
        out['pw_E1'] = rowE - 1/6
    else:
        out['pw_p1'] = None
    # ---- cumulative ----
    wts = np.array([(1-(jj+1)/N) for jj in range(N)])
    Mv = 1/(6*N*N) + TAU/(2*N)
    row = F.sum(axis=1)/N**2
    rowE = F @ wts / N**2
    A_ub = np.array([row, -row, rowE, -rowE])
    b_ub = [D1 + 0.5, D1 - 0.5, Mv + 1/6, Mv - 1/6]
    t = time.time()
    res = linprog(s_c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0, None)]*m, method='highs')
    out['cum_dt'] = time.time() - t
    if res.success:
        out['cum_p1'] = float(res.fun)/N
        out['cum_support'] = int((res.x > 1e-9).sum())
        out['cum_E1'] = float(rowE @ res.x) - 1/6
    else:
        out['cum_p1'] = None
    return out

def E1_closed_form(N):
    """rowE_exact for exact-CUE rows f(j)=j: sum_{j=1}^N (j/N)(1-j/N)/N = (N^2-1)/(6N^2).
    Deviation from 1/6: 1/(6N^2)."""
    j = np.arange(1, N+1)
    rowE = float((j/N * (1 - j/N) / N).sum())
    dev = 1/6 - rowE
    return rowE, dev

def fits(Ns, ys):
    """Fit 4 candidate laws to cumulative p1(N). Returns list of dicts + crossing."""
    x = np.array(Ns, float); y = np.array(ys, float)
    d = 1 - y
    res = []
    # 1: p1 = 1 - c/sqrt(N)
    X1 = 1/np.sqrt(x)
    c1, *_ = np.linalg.lstsq(X1[:, None], d, rcond=None)
    yp1 = 1 - c1[0]*X1
    res.append(dict(name='1-c/sqrtN', params=dict(c=float(c1[0])), sse=float(np.sum((y-yp1)**2)),
                    yp=yp1.tolist()))
    # 2: p1 = 1 - c/N^a  (log d = log c - a log N)
    A = np.column_stack([np.ones_like(x), -np.log(x)])
    beta, *_ = np.linalg.lstsq(A, np.log(d), rcond=None)
    logc, a = float(beta[0]), float(beta[1])
    yp2 = 1 - np.exp(logc)*x**(-a)
    res.append(dict(name='1-c/N^a', params=dict(c=float(np.exp(logc)), a=a),
                    sse=float(np.sum((y-yp2)**2)), yp=yp2.tolist()))
    # 3: p1 = 1 - c*logN/N
    X3 = np.log(x)/x
    c3, *_ = np.linalg.lstsq(X3[:, None], d, rcond=None)
    yp3 = 1 - c3[0]*X3
    res.append(dict(name='1-c logN/N', params=dict(c=float(c3[0])), sse=float(np.sum((y-yp3)**2)),
                    yp=yp3.tolist()))
    # 4: p1 = c0 + c1/N^a  (grid over a)
    best = None
    for a in np.linspace(0.2, 3.0, 281):
        A4 = np.column_stack([np.ones_like(x), x**(-a)])
        (c0, c1), *_ = np.linalg.lstsq(A4, y, rcond=None)
        yp4 = c0 + c1*x**(-a)
        sse = float(np.sum((y-yp4)**2))
        if best is None or sse < best[0]:
            best = (sse, a, float(c0), float(c1), yp4.tolist())
    res.append(dict(name='c0+c1/N^a', params=dict(c0=best[2], c1=best[3], a=best[1]),
                    sse=best[0], yp=best[4]))
    # crossing N* where fitted law = TB (if it crosses on [8, 256])
    for r in res:
        nm = r['name']; p = r['params']; yp = np.array(r['yp'])
        Ns_ = np.geomspace(8, 256, 20001)
        if nm == '1-c/sqrtN':
            pred = 1 - p['c']/np.sqrt(Ns_)
        elif nm == '1-c/N^a':
            pred = 1 - p['c']*Ns_**(-p['a'])
        elif nm == '1-c logN/N':
            pred = 1 - p['c']*np.log(Ns_)/Ns_
        else:
            pred = p['c0'] + p['c1']*Ns_**(-p['a'])
        below = pred < TB
        r['below_at_8'] = bool(pred[0] < TB)
        r['above_at_256'] = bool(pred[-1] > TB)
        if below[0] and not below[-1]:
            idx = np.where(below)[0][-1]
            r['crossing_N'] = float(Ns_[idx])
        elif not below[0]:
            r['crossing_N'] = None  # never below TB on [8,256]
        else:
            r['crossing_N'] = None  # below throughout
    return res

if __name__ == '__main__':
    t0 = time.time()
    rows = []
    for N in NS:
        for seed in SEEDS:
            r = run_both(N, NC[N], seed)
            rows.append(r)
            print(f"N={N:3d} seed={seed:4d} pw={'%.8f' % r['pw_p1'] if r['pw_p1'] else 'INFEASIBLE'} "
                  f"cum={'%.8f' % r['cum_p1'] if r['cum_p1'] else 'INFEASIBLE'} "
                  f"(pw_sup={r.get('pw_support')}, cum_sup={r.get('cum_support')}, {time.time()-t0:.0f}s)", flush=True)
    # E(1) closed form check at N=128, 256 (adversarial)
    for N in (128, 256):
        rowE, dev = E1_closed_form(N)
        print(f"E(1) closed form N={N}: rowE_exact={rowE:.16f} dev from 1/6 = {dev:.3e} (expect 1/(6N^2)={1/(6*N*N):.3e})")
    # N=8 seed-sweep (cumulative): reproduce check_cum8 + extend
    sweep = []
    for nc, seed in [(4000, 1), (8000, 2), (12000, 3), (20000, 4)]:
        r = run_both(8, nc, seed)
        sweep.append(r)
        print(f"N8sweep nc={nc:6d} seed={seed}: cum={'%.8f' % r['cum_p1'] if r['cum_p1'] else 'INFEASIBLE'}", flush=True)
    for nc in (4000, 8000, 20000):
        for seed in (42, 1234, 2024):
            r = run_both(8, nc, seed)
            sweep.append(r)
            print(f"N8sweep nc={nc:6d} seed={seed}: cum={'%.8f' % r['cum_p1'] if r['cum_p1'] else 'INFEASIBLE'}", flush=True)
    # fits on cumulative per-seed curves
    fits_out = {}
    for seed in SEEDS:
        ys = [r['cum_p1'] for r in rows if r['seed'] == seed]
        fits_out[str(seed)] = fits(NS, ys)
    mean_ys = [float(np.mean([r['cum_p1'] for r in rows if r['N'] == N])) for N in NS]
    fits_out['mean'] = fits(NS, mean_ys)
    data = dict(rows=rows, sweep=sweep, fits=fits_out, mean_cum=mean_ys, Ns=NS, seeds=SEEDS,
                tb=TB, E1_closed={str(N): E1_closed_form(N)[1] for N in (128, 256)})
    with open('/root/riemann/research/waves/wave-phone-2/results/laptop-family-data.json', 'w') as f:
        json.dump(data, f, indent=1)
    print(f"DONE {time.time()-t0:.0f}s, json written")
