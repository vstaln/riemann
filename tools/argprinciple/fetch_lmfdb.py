#!/usr/bin/env python3
"""Fetch LMFDB Riemann zeta zero ordinates (plain text) for the C-NY1 strips.

Endpoint: https://www.lmfdb.org/zeros/zeta/list?N=<zero index>&limit=<count>
(N-based, 1-indexed zero number). Chunks of 1000, >= 0.4s delay between requests
(per the Riemann-program network etiquette). Output: one file per chunk,
"lmfdb_zeros_<start>-<start+999>.txt", lines "<index> <ordinate 34dp>".

Ranges (by zero index) chosen to cover the strips [T, T+H] with margin, and to
give exact N(T), N(T+H) (count of ordinates <= height) inside the fetched data:
  strip [1e4, 1.05e4]  -> indices 9000..10999
  strip [2e4, 2.05e4]  -> indices 21500..23499
  strip [5e4, 5.05e4]  -> indices 62000..64799
"""
import os, sys, time, urllib.request, urllib.error

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(OUT, exist_ok=True)

RANGES = [(9000, 10999), (21500, 23499), (62000, 64799)]
CHUNK = 1000
DELAY = 0.4
URL = "https://www.lmfdb.org/zeros/zeta/list?N={}&limit={}"


def fetch(start, count, retries=4):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(URL.format(start, count), headers={
                "User-Agent": "Mozilla/5.0 (research zero-count fetch)",
            })
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read().decode("utf-8", "replace")
            if data.strip().startswith("<!DOCTYPE") or "reCAPTCHA" in data:
                raise RuntimeError("challenge page returned")
            lines = [ln for ln in data.splitlines() if ln.strip()]
            if not lines:
                raise RuntimeError("empty body")
            # sanity: first line must parse as "<int> <float>"
            first = lines[0].split()
            float(first[1])
            return lines
        except Exception as e:
            print(f"  attempt {attempt+1}/{retries} failed for start={start}: {e}", flush=True)
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"give up on start={start}")


def main():
    total = 0
    for lo, hi in RANGES:
        for s in range(lo, hi + 1, CHUNK):
            cnt = min(CHUNK, hi - s + 1)
            fname = os.path.join(OUT, f"lmfdb_zeros_{s}-{s + cnt - 1}.txt")
            if os.path.exists(fname):
                n = sum(1 for _ in open(fname))
                print(f"skip (exists) {fname} ({n} lines)", flush=True)
                total += n
                time.sleep(DELAY)
                continue
            lines = fetch(s, cnt)
            with open(fname, "w") as f:
                f.write("\n".join(lines) + "\n")
            # verify chunk count / continuity
            idx = [int(ln.split()[0]) for ln in lines]
            assert idx == list(range(s, s + len(idx))), f"index gap in {fname}"
            total += len(lines)
            print(f"wrote {fname}: {len(lines)} zeros (idx {idx[0]}..{idx[-1]})", flush=True)
            time.sleep(DELAY)
    print(f"DONE. total zeros fetched: {total}", flush=True)


if __name__ == "__main__":
    main()
