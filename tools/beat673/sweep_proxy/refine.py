#!/usr/bin/env python3
"""Refine top candidates with heavier proxy runs (more restarts/iters) and
dump weights JSONs for the real verifier."""
import sys, json
sys.path.insert(0, "/root/riemann/tools/beat673/sweep_proxy")
from common import Ker, floor_min, default_weights, PAIRS
from sweep import build, shape_ramp_up, shape_ramp_dn, shape_peak, shape_ends, shape_flat

NAMES = ["span3_ramp_up", "span3_ends2", "ramp_up0.5", "span1_peak",
         "span2_ramp_dn", "span3_ends", "span4_ends2", "span4_ramp_dn",
         "span4_ends", "peak0.5", "default"]


def get_profile(name):
    if name == "default":
        return default_weights()
    if name == "ramp_up0.5":
        return build(shape_ramp_up(0.5))
    if name == "peak0.5":
        return build(shape_peak(0.5))
    span, shape = name.split("_")[0][4:], "_".join(name.split("_")[1:])
    r = int(span)
    flat = {rr: shape_flat for rr in range(1, 7)}
    flat[r] = {"ramp_up": shape_ramp_up(1.0), "ramp_dn": shape_ramp_dn(1.0),
               "peak": shape_peak(1.0), "ends": shape_ends(1.0),
               "ends2": shape_ends(2.0)}[shape]
    return build(None, per_span=flat)


def main():
    ker = Ker()
    out = {}
    for name in NAMES:
        w = get_profile(name)
        fl = floor_min(w, ker, restarts=30, iters=3000, seed=42)
        out[name] = fl
        print(f"{name}: refined proxy floor = {fl:.10f}  "
              f"(8066 margin {fl-8066e-6:+.3e})", flush=True)
    # dump exact weights JSONs (rational, small denominators where possible)
    import os
    os.makedirs("/tmp/riemann_sweep/weights", exist_ok=True)
    from fractions import Fraction
    for name in NAMES:
        w = get_profile(name)
        wj = {f"{i},{j}": [Fraction(w[(i, j)]).limit_denominator(1000).numerator,
                           Fraction(w[(i, j)]).limit_denominator(1000).denominator]
              for (i, j) in PAIRS}
        with open(f"/tmp/riemann_sweep/weights/{name}.json", "w") as fh:
            json.dump(wj, fh, indent=0)
    with open("/tmp/riemann_sweep/refined.json", "w") as fh:
        json.dump(out, fh, indent=1)
    print("weights JSONs -> /tmp/riemann_sweep/weights/")


if __name__ == "__main__":
    main()
