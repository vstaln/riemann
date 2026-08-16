#!/usr/bin/env python3
"""Ground-truth oracle: run the real verifier (grid 1000) on each candidate
profile at a given target eps. Prints verified True/False, and on failure the
terminal-box floor (the true floor estimate). Usage:
  python3 oracle.py TARGET_NUM [TARGET_DEN=1e6] [GRID=1000] [profile names...]
"""
import subprocess, sys, json, os

VERIFY = "/root/riemann/tools/beat673/verify_cos7.py"
WDIR = "/tmp/riemann_sweep/weights"

PROFILES = ["span3_ramp_up", "span3_ends2", "ramp_up0.5", "span1_peak",
            "span2_ramp_dn", "span3_ends", "span4_ends2", "span4_ramp_dn",
            "span4_ends", "peak0.5", "default"]


def run(name, t_num, t_den=10 ** 6, grid=1000, timeout=1200):
    wj = os.path.join(WDIR, f"{name}.json")
    cmd = ["python3", VERIFY, "149", "100", "1", "1320",
           str(t_num), str(t_den), wj, str(grid)]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, None, None
    out = r.stdout
    ok = "verified=True" in out
    lower = None
    for line in out.splitlines():
        if "FAILED at terminal" in line:
            lower = line.split("lower=")[-1]
    nodes = None
    for line in out.splitlines():
        if line.startswith("nodes="):
            nodes = line.split("=")[1]
    return ok, lower, nodes


def main():
    t_num = int(sys.argv[1]) if len(sys.argv) > 1 else 8066
    t_den = int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 6
    grid = int(sys.argv[3]) if len(sys.argv) > 3 else 1000
    names = sys.argv[4:] if len(sys.argv) > 4 else PROFILES
    print(f"target = {t_num}/{t_den} grid={grid}")
    for name in names:
        ok, lower, nodes = run(name, t_num, t_den, grid)
        status = "VERIFIED" if ok else ("TIMEOUT" if lower is None and nodes is None else "FAIL")
        print(f"{name}: {status}  lower={lower}  nodes={nodes}", flush=True)


if __name__ == "__main__":
    main()
