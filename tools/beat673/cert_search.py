"""Use the verifier as ground-truth oracle: for each (alpha, psum), binary
search the max certifiable eps, then compute the resulting bound.
"""
import subprocess, sys, os

def try_certify(alpha_num, alpha_den, p_num, p_den, t_num, t_den, timeout=800):
    cmd = ["uv", "run", "--quiet", "--with", "python-flint", "python3",
           "verify_cos7.py", str(alpha_num), str(alpha_den),
           str(p_num), str(p_den), str(t_num), str(t_den), "-"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                           cwd="/tmp/combine")
        return "verified=True" in r.stdout
    except subprocess.TimeoutExpired:
        return None  # unknown

def max_certifiable_eps(alpha_num, alpha_den, p_num, p_den, lo_e, hi_e, steps=4):
    """Binary search eps (in units 1e-6) between lo_e and hi_e."""
    # first pass: coarse binary search with short timeout to bracket
    best = lo_e
    lo, hi = lo_e, hi_e
    for _ in range(steps):
        mid = (lo + hi) // 2
        ok = try_certify(alpha_num, alpha_den, p_num, p_den, mid, 10**6, timeout=500)
        if ok:
            best = max(best, mid)
            lo = mid
        else:
            hi = mid
    return best

if __name__ == "__main__":
    # candidates from deep_map: alpha, psum_inv
    cands = [(142, 200), (147, 200), (149, 200), (147, 220), (145, 240)]
    for alpha_num, psum_inv in cands:
        p_num, p_den = 1, psum_inv * 6
        # bracketing: deep_min estimates (0.0085-0.0097 for psum=1/200)
        lo, hi = 7000, 9500
        if psum_inv == 240:
            lo, hi = 6000, 8000
        eps = max_certifiable_eps(alpha_num, 100, p_num, p_den, lo, hi, steps=4)
        print(f"alpha={alpha_num/100:.2f} psum=1/{psum_inv}: max certifiable eps ~= {eps/1e6:.6f}", flush=True)
