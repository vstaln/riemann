#!/usr/bin/env python3
"""fit_law.py — refine the fit of the cumulative min-p1(N) curve (upper bounds over random family).
Reads laptop-family-data.json, fits 4 candidates + extended c0+c1/N^a with free a (curve_fit),
reports SSE, max|res|, residuals at each N, crossing vs Theorem-B line, and the limit c0.
Run: cd /root/riemann/research/waves/wave-phone-2/results && python3 fit_law.py
"""
import json, numpy as np
from scipy.optimize import curve_fit

TB = 0.6725007036794116

def fit_candidates(Ns, ys):
    x = np.array(Ns, float); y = np.array(ys, float)
    d = 1 - y
    out = []
    # 1-c/sqrtN
    c1, *_ = np.linalg.lstsq((1/np.sqrt(x))[:, None], d, rcond=None)
    yp = 1 - c1[0]/np.sqrt(x)
    out.append(dict(name='1-c/sqrtN', params=dict(c=float(c1[0])),
                    sse=float(np.sum((y-yp)**2)), maxres=float(np.max(np.abs(y-yp))),
                    res=[float(v) for v in y-yp]))
    # 1-c/N^a (linear in log-log of d)
    A = np.column_stack([np.ones_like(x), -np.log(x)])
    beta, *_ = np.linalg.lstsq(A, np.log(d), rcond=None)
    c, a = float(np.exp(beta[0])), float(beta[1])
    yp = 1 - c*x**(-a)
    out.append(dict(name='1-c/N^a', params=dict(c=c, a=a),
                    sse=float(np.sum((y-yp)**2)), maxres=float(np.max(np.abs(y-yp))),
                    res=[float(v) for v in y-yp]))
    # 1-c logN/N
    c3, *_ = np.linalg.lstsq((np.log(x)/x)[:, None], d, rcond=None)
    yp = 1 - c3[0]*np.log(x)/x
    out.append(dict(name='1-c logN/N', params=dict(c=float(c3[0])),
                    sse=float(np.sum((y-yp)**2)), maxres=float(np.max(np.abs(y-yp))),
                    res=[float(v) for v in y-yp]))
    # c0+c1/N^a, free a via curve_fit, wide start grid
    best = None
    for a0 in np.linspace(0.01, 3.0, 60):
        try:
            with np.errstate(over='ignore', invalid='ignore'):
                p, _ = curve_fit(lambda X, c0, c1, a: c0 + c1*X**(-a),
                                 x, y, p0=[1.0, -0.7, a0], maxfev=20000)
            if not np.all(np.isfinite(p)):
                continue
            yp = p[0] + p[1]*x**(-p[2])
            if not np.all(np.isfinite(yp)):
                continue
            sse = float(np.sum((y-yp)**2))
            if best is None or sse < best['sse']:
                best = dict(name='c0+c1/N^a', params=dict(c0=float(p[0]), c1=float(p[1]), a=float(p[2])),
                            sse=sse, maxres=float(np.max(np.abs(y-yp))), res=[float(v) for v in y-yp])
        except Exception:
            pass
    if best is not None:
        out.append(best)
    else:
        # fallback: best 2-param c0+c1/sqrtN
        A = np.column_stack([np.ones_like(x), 1/np.sqrt(x)])
        (c0, c1), *_ = np.linalg.lstsq(A, y, rcond=None)
        yp = c0 + c1/np.sqrt(x)
        out.append(dict(name='c0+c1/sqrtN', params=dict(c0=float(c0), c1=float(c1)),
                        sse=float(np.sum((y-yp)**2)), maxres=float(np.max(np.abs(y-yp))),
                        res=[float(v) for v in y-yp]))
    # crossings on [8, 256]
    Ns_ = np.geomspace(8, 256, 40001)
    for r in out:
        nm, p = r['name'], r['params']
        if nm == '1-c/sqrtN':
            pred = 1 - p['c']/np.sqrt(Ns_)
        elif nm == '1-c/N^a':
            pred = 1 - p['c']*Ns_**(-p['a'])
        elif nm == '1-c logN/N':
            pred = 1 - p['c']*np.log(Ns_)/Ns_
        else:
            pred = p['c0'] + p['c1']*Ns_**(-p['a'])
        below = pred < TB
        r['crossing_N'] = (float(Ns_[np.where(below)[0][-1]]) if below[0] and not below[-1]
                           else (None if not below[0] else float(Ns_[-1])))
        r['limit'] = {'1-c/sqrtN': 1.0, '1-c/N^a': 1.0, '1-c logN/N': 1.0}.get(nm, float(p.get('c0', 1.0)))
    return out

if __name__ == '__main__':
    d = json.load(open('laptop-family-data.json'))
    Ns = d['Ns']
    print(f"Theorem-B line = {TB}")
    print(f"N = {Ns}")
    for k in ['mean'] + [str(s) for s in d['seeds']]:
        ys = d['mean_cum'] if k == 'mean' else [r['cum_p1'] for r in d['rows'] if r['seed'] == int(k)]
        print(f"\n=== cumulative fit, {k} (y = {[round(v,6) for v in ys]}) ===")
        for r in fit_candidates(Ns, ys):
            print(f"  {r['name']:14s} {r['params']} sse={r['sse']:.3e} maxres={r['maxres']:.3e} "
                  f"res={[round(v,4) for v in r['res']]} cross(N)={r['crossing_N']} limit={r['limit']}")
