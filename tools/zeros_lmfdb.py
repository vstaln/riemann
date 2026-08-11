"""LMFDB Riemann zeta zero client.

Fetch imaginary parts of zeros of zeta(s) on the critical line from LMFDB
(https://www.lmfdb.org/zeros/zeta/list), the canonical verified dataset
(first 103,800,788,359 zeros, Re(rho)=1/2 checked, |Im| precision ~2.5e-31).

Usage (as library):
    from zeros_lmfdb import cached_zeros, zeros_in_height_range
    gs = cached_zeros(1, 5000)                 # gamma_1..gamma_5000
    gs = zeros_in_height_range(1000.0, 2000.0) # all zeros with Im in [1000,2000)

CLI:
    uv run --with mpmath python zeros_lmfdb.py 1 100000   # cache zeros 1..100000
    uv run --with mpmath python zeros_lmfdb.py --height 1000 2000

Notes
-----
- LMFDB rate-limits: single requests > ~1000 zeros hit a reCAPTCHA. We chunk at
  `CHUNK` (default 1000) with a delay between requests and retry on HTML replies.
- Data is cached as plain text lines "N gamma_N" (LMFDB's own format) under
  tools/data/. Cached files are reused on subsequent calls.
- mpmath is used only for mpf conversion (and an optional cross-check).
"""
from __future__ import annotations

import os
import re
import sys
import time
import urllib.request
import urllib.error

from mpmath import mp, mpf

BASE = "https://www.lmfdb.org/zeros/zeta/list"
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
CHUNK = 1000            # safe per-request limit (larger requests get captcha'd)
DELAY = 0.35            # seconds between requests
RETRIES = 4
UA = "riemann-verification-toolkit/0.1 (research; contact: riemann@localhost)"

MPF_RE = re.compile(rb"^\s*(\d+)\s+(\d+\.\d+)\s*$")


def _request(start: int, count: int) -> list[tuple[int, str]]:
    """One HTTP request; returns [(n, gamma_str), ...] or [] on captcha/HTML."""
    url = f"{BASE}?N={start}&limit={count}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
    except urllib.error.HTTPError as e:
        print(f"  [http {e.code} at N={start}]", file=sys.stderr)
        return []
    # A captcha / error page is HTML; the data is pure text lines "N gamma".
    if raw.lstrip().startswith(b"<!doctype") or b"<html" in raw[:500]:
        print(f"  [captcha/html reply at N={start}, retrying later]", file=sys.stderr)
        return []
    out = []
    for line in raw.splitlines():
        m = MPF_RE.match(line)
        if m:
            out.append((int(m.group(1)), m.group(2).decode()))
    if not out:
        print(f"  [unparseable reply at N={start}]", file=sys.stderr)
    return out


def fetch_chunked(start: int, end: int, chunk: int = CHUNK, delay: float = DELAY,
                  verbose: bool = True) -> list[tuple[int, str]]:
    """Fetch zeros with indices in [start, end] inclusive, chunked + retried."""
    out: dict[int, str] = {}
    n = start
    while n <= end:
        got = False
        for attempt in range(RETRIES):
            rows = _request(n, min(chunk, end - n + 1))
            if rows:
                out.update(dict(rows))
                got = True
                break
            time.sleep(delay * (attempt + 3))  # back off on captcha
        if not got:
            print(f"  [FAILED after {RETRIES} tries at N={n}; skipping]", file=sys.stderr)
        if verbose and n % (10 * chunk) == 0 or n == start:
            print(f"  ... fetched up to N={n} (last gamma={out.get(n)})", file=sys.stderr)
        n += chunk
        time.sleep(delay)
    return sorted(out.items())


def cache_path(start: int, end: int) -> str:
    return os.path.join(DATA_DIR, f"zeros_{start}_{end}.txt")


def cached_zeros(start: int, end: int, force: bool = False,
                 verbose: bool = True) -> list[mpf]:
    """Zeros gamma_start..gamma_end as mpmath mpf, using/creating disk cache."""
    os.makedirs(DATA_DIR, exist_ok=True)
    path = cache_path(start, end)
    if not force and os.path.exists(path):
        rows = _read_cache(path)
        if rows and rows[-1][0] >= end:
            if verbose:
                print(f"[cache hit] {path} ({len(rows)} zeros)")
            return [mpf(g) for _, g in rows]
    if verbose:
        print(f"[fetch] LMFDB zeros {start}..{end} (chunked, may take a while)")
    rows = fetch_chunked(start, end, verbose=verbose)
    with open(path, "w") as f:
        for n, g in rows:
            f.write(f"{n} {g}\n")
    if verbose:
        print(f"[saved] {path} ({len(rows)} zeros)")
    return [mpf(g) for _, g in rows]


def _read_cache(path: str) -> list[tuple[int, str]]:
    rows = []
    with open(path) as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                rows.append((int(parts[0]), parts[1]))
    return rows


def zeros_in_height_range(a: float, b: float, pad: int = 50) -> list[tuple[int, mpf]]:
    """All zeros with Im(gamma) in [a, b), by first guessing the index range.

    Uses Riemann-von Mangoldt: N(T) ~ (T/2pi)(log(T/2pi) - 1) + 7/8 + ...
    Returns [(n, gamma_n), ...].
    """
    from math import log

    def N_est(T: float) -> int:
        T = max(T, 10.0)
        return int((T / (2 * 3.141592653589793)) * (log(T / (2 * 3.141592653589793)) - 1) + 7 / 8)

    n0 = max(1, N_est(a) - pad)
    n1 = N_est(b) + pad
    gs = cached_zeros(n0, n1)
    return [(n0 + i, g) for i, g in enumerate(gs) if a <= g < b]


def crosscheck_mpmath(n: int = 1000, tol: float = 1e-28) -> None:
    """Compare LMFDB zeros against mpmath's independent Riemann-Siegel computation."""
    from mpmath import zetazero
    gs = cached_zeros(1, n, verbose=False)
    worst = mpf(0)
    for i, g in enumerate(gs, start=1):
        ref = zetazero(i)
        d = abs(g - ref)
        if d > worst:
            worst = d
    status = "OK" if worst < tol else "MISMATCH"
    print(f"crosscheck vs mpmath zetazero (n=1..{n}): worst |d| = {mp.nstr(worst, 3)} "
          f"({status}, tol={tol})")


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Fetch/cache LMFDB zeta zeros")
    ap.add_argument("start", type=int, nargs="?", help="first zero index")
    ap.add_argument("end", type=int, nargs="?", help="last zero index")
    ap.add_argument("--height", nargs=2, type=float, metavar=("A", "B"),
                    help="fetch all zeros with Im in [A, B)")
    ap.add_argument("--crosscheck", action="store_true", help="compare vs mpmath")
    args = ap.parse_args()
    mp.dps = 40
    if args.crosscheck:
        crosscheck_mpmath()
    elif args.height:
        rows = zeros_in_height_range(*args.height)
        print(f"{len(rows)} zeros in [{args.height[0]}, {args.height[1]})")
        for n, g in rows[:5]:
            print(n, mp.nstr(g, 34))
        print("...")
        for n, g in rows[-3:]:
            print(n, mp.nstr(g, 34))
    else:
        gs = cached_zeros(args.start, args.end)
        print(f"{len(gs)} zeros; first: {mp.nstr(gs[0], 34)}; last: {mp.nstr(gs[-1], 34)}")
