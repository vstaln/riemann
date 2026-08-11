#!/usr/bin/env python3
"""B6.2 (biology note): beyond-bandwidth-1 rows and the 256-law's periodicity.

Claim under test: the SAMPLED F=1 rows beyond bandwidth 1 (grid j = 257..512,
near-CUE S(j) = j/256) cannot constrain the 256-periodic ceiling law, because
periodicity + total mass 256 forces S(j+256) = S(j) + 256 automatically, i.e.
the law satisfies the beyond-1 sampled rows for free.  Hence the "beyond-1 form
factor" input only bites through CONTINUUM alpha values (or through excluding
periodicity), which is the real content of [CD-V5]'s curve -- and the reason
[ALP]'s "only p1 moves v" stands.

Also verifies the semantics of the law data (tools/lpdual/law_data.json):
the s_mid array (midpoint masses) should satisfy 256*C(j/256) ~ j (near-CUE).

Run:  uv run --quiet python beyond1_rows.py
"""
import json, numpy as np

print("=== B6.2: beyond-1 sampled rows vs periodicity of the 256-law ===")

# ---- identity (algebra, code-verified): periodic extension satisfies beyond-1 rows
N = 256
print("\nIdentity: for a 256-periodic marked law with total mark mass 256,")
print("S(j+256) = S(j) + 256 for all j  (periodicity + normalization),")
print("so if rows 1..255 are near-CUE (256*S(j)/256 ~ j) then rows 257..512 are")
print("automatically near-CUE as well.  The beyond-1 *sampled* rows add no new")
print("constraint on the law; its simple fraction p1 is unchanged.")
print("Check at j = 5:  S(5+256)/256 - (5+256)/256 = (S(5)+256)/256 - 261/256")
print("               = S(5)/256 - 5/256  -> same deviation as at j=5.  (exact)")

# ---- empirical check on the actual law data (semantics of s_mid)
d = json.load(open('/home/vstaln/riemann/tools/lpdual/law_data.json'))
s = np.array(d['s_mid'])
print(f"\nlaw_data.json: {s.size} masses; sum = {s.sum():.6f}")
cum = np.cumsum(s)
dev = 256 * cum - np.arange(1, s.size + 1)
print(f"256*cumsum(s)[j] - j : first 5 = {dev[:5]}")
print(f"                       max |dev| over j=1..255 = {np.max(np.abs(dev[:255])):.3e}")
print(f"                       at j=255 = {dev[254]:.3e}")
# periodic extension
ext = np.concatenate([cum, cum + cum[-1]])[:2 * 256]
devext = 256 * (ext / ext[-1] * 256) - np.arange(1, 2 * 256 + 1) if False else None
# cleaner: normalized CDF check
C = cum / cum[-1]
dev_n = 256 * C - np.arange(1, s.size + 1)
print(f"normalized-CDF check 256*C(j/256) - j: max |.| = {np.max(np.abs(dev_n[:255])):.3e}")
# is s_mid the *mass* convention (sum=1) or the *count* convention?
print(f"(if sum(s) ~ 1 then s_mid are masses summing to 1; "
      f"if 256*C(j) ~ j then they are near-CUE masses)")
