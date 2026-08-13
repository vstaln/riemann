# Sharp square-root tail (m=257) — NEGATIVE for our parameters

**Date:** 2026-08-14. **Status:** PROVEN (exact arithmetic, mpmath 40-digit).

trmdy's "sharp square-root tail" h(E)=E for E≤1, h(E)=2√E−1 for E≥1 (blocks to m=257)
is ALREADY implemented in our bound formula: B = φ_m(A) = A for A≤m/(m−1), else
2√((m−1)A/m)−1+A/m. That is exactly the sharp tail.

At our record parameters (eps=0.0062, α=1.464, psum=1/320):
- m=171 (our argmax): A=1.023, B=1.0229282, bound = 0.6734808616745135
- m=257 (trmdy's block length): A=1.5562, B=1.4961514, bound = 0.6733352720073994

m=257 is STRICTLY WORSE. trmdy needed m=257 only because their (eps=0.005, H=0.672457)
made the larger block optimal; our higher eps (0.0062) shifts the argmax down to 171.

**Verdict: no gain from m=257. Record 0.673481 stands.** Script: /tmp/sharp_tail_m257.py
(`uv run --quiet --with mpmath python3 /tmp/sharp_tail_m257.py`).
