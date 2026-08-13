# eps-max at the record config: the boundary is TIGHT (PROVEN)

**Date:** 2026-08-12. **Status:** CHECKED NUMERICALLY (rigorous interval verifier).
The record's eps=0.00806 at (alpha=1.49, psum=1/220, m=133) is at the certified boundary:
- max certifiable eps = 8065/1e6 (8065 verifies; 8067 fails, lower bound 0.008053)
- at psum=1/225 (p=1/1350): max eps between 7874 (verifies) and 7937 (fails)
- at psum=1/300 (p=1/1800): max eps ~0.00607 (from the two-tone verifier, same kernel family)

Data: research/waves/wave-local/results/exec-eps-max.json + exec-eps-max-runs.log
The single-cosine machinery at the record config is EXHAUSTED — no higher eps is certifiable there.
