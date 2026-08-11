#!/usr/bin/env python3
"""Follow-up to probe_music_moments.py: check the ~1/log T decay law for the flat-window
Gram m2 deficit (per-band LOCAL rescale) by testing c = deficit * log(h_center) for
stability across height bands.

Finding recorded: c ~ 0.28-0.30 over h in [1420, 17000] (mean 0.288, spread 0.021),
i.e. the deficit follows ~1/log T above h ~ 3000; the lowest band (h ~ 141) deviates
(boundary effects at the start of the zero sequence).
"""
import numpy as np

# (h_lo, h_hi, m2_deficit) from probe_music_moments.py output
bands = [(14, 1420, -0.0118), (1420, 5800, -0.0347),
         (5800, 10800, -0.0331), (10800, 17000, -0.0306)]
print("band         h_center   deficit   deficit*log(h_center)")
for lo, hi, d in bands:
    hc = np.sqrt(lo * hi)
    print(f"[{lo:6d},{hi:7d})  {hc:9.1f}   {d:+.4f}   {abs(d) * np.log(hc):.4f}")
cs = [abs(d) * np.log(np.sqrt(lo * hi)) for lo, hi, d in bands[1:]]
print(f"\nc = deficit*log(h) over the three high bands: {[round(float(c), 4) for c in cs]}")
print(f"mean c = {np.mean(cs):.4f}  spread = {np.max(cs) - np.min(cs):.4f}"
      "  (stable -> ~1/log T law above h ~ 3000)")
