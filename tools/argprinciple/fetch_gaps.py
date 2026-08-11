import os, time, urllib.request
OUT = "data"
URL = "https://www.lmfdb.org/zeros/zeta/list?N={}&limit={}"
have = set()
for f in os.listdir(OUT):
    if f.startswith("lmfdb_zeros_") and f.endswith(".txt"):
        a, b = f.replace("lmfdb_zeros_","").replace(".txt","").split("-")
        for s in range(int(a), int(b)+1, 1000):
            have.add((int(a)//1000)*1000)
missing = [s for s in range(1000, 64800, 1000) if s not in have]
print("missing chunk starts:", len(missing), missing[:20], "...")
for s in missing:
    fname = os.path.join(OUT, f"lmfdb_zeros_{s}-{s+999}.txt")
    ok = False
    for attempt in range(6):
        try:
            req = urllib.request.Request(URL.format(s, 1000), headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) research fetch"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read().decode()
            lines = [ln for ln in data.splitlines() if ln.strip()]
            if not lines or "reCAPTCHA" in data or lines[0].startswith("<!DOCTYPE"):
                raise RuntimeError("blocked")
            idx = [int(ln.split()[0]) for ln in lines]
            assert idx == list(range(s, s+len(idx))), (s, idx[0], idx[-1])
            with open(fname, "w") as f:
                f.write("\n".join(lines) + "\n")
            print("OK", s, flush=True)
            ok = True
            break
        except Exception as e:
            print("retry", s, attempt, str(e)[:60], flush=True)
            time.sleep(10 + 15*attempt)
    time.sleep(6)
    if not ok:
        print("FAILED", s, flush=True)
print("done")
