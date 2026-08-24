# Dispute check: which functional does the interval verifier certify? (code-side)

Date: 2026-08-24
Agent: adventurer (code-side extraction, read-only)
Sources read: `tools/verify_coboundary_floor.py` (full), `tmplogs/cert_790.log` (header). No other files read. Nothing modified.

## Verdict (one line)

**IMPLEMENTED = F_V — the audit is RIGHT about the code.** The verified lower bound
includes the span-one pair terms (j−i=1, coefficient 2/(7−1)=1/3) of the full 21-pair
sum IN ADDITION to the separate q_i·w(g_i) terms; the q_i do NOT replace the span-one
pairs. Label: PROVEN (by direct reading of the implementation).

---

## (a) The exact objective as implemented

In the parameterized mode (`main()`, env-var driven — this is the mode the certified
run uses), the pair weights are built over ALL 21 pairs, spans r=1..6:

- `verify_coboundary_floor.py:498`
  ```python
  w_uniform = {(i, j): 2.0 / (7 - (j - i)) for i in range(7) for j in range(i + 1, 7)}
  ```
  (`range(7)` × `range(i+1, 7)` = all (i,j), 0≤i<j≤6 — no span filter.)

The lower bound computed per box, coboundary branch, `box_lower()`:

- `verify_coboundary_floor.py:261-281` (verbatim)
  ```python
        if cap_scheme == "coboundary":
            # F_B = sum_i p_i g_i + sum_i q_i w(g_i)
            #       + sum_{i<j} a_ij w(y_j - y_i)   (uniform a_ij)
            result = 0.0
            for i in range(q):
                p_i = pressure_coeffs[i]
                result = _down(result + _down(p_i * (low_prefix[i + 1] - low_prefix[i]) / grid))
            for i in range(q):
                q_i = nearest_coeffs[i]
                low_i, high_i = box[i]
                if high_i < ranges.length:
                    result = _down(result + _down(q_i * ranges.query(low_i, high_i)))
            for i, j in pair_list:
                span = j - i
                left = low_prefix[j] - low_prefix[i]
                right = high_prefix[j] - high_prefix[i] + span - 1
                if right >= ranges.length:
                    continue
                result = _down(result + _down(weights[(i, j)] * ranges.query(left, right)))
            return result
  ```

So as implemented:

```
F = Σ_i p_i·g_i + Σ_i q_i·w(g_i) + Σ_{0≤i<j≤6} (2/(7−(j−i)))·w(y_j − y_i)
```

with `low_prefix[j] − low_prefix[i]` = sum of gaps i..j−1 = y_j − y_i (y_0=0,
y_k = g_1+…+g_k, coordinates are the 6 gaps g_0..g_5). The comment at line 262-263
states the intent explicitly: `sum_{i<j} a_ij w(y_j - y_i)` with NO span restriction.

## (b) Span-one handling: ADDED, not replaced

The audit's claim — span-one pairs appear in addition to the q_i terms — is confirmed
by two facts:

1. `pair_list = sorted(weights)` (`:251`) is built from `w_uniform` which contains
   ALL 21 pairs including the six span-one pairs (i,i+1) with weight 2/(7−1)=1/3.
   The `box_lower` loop over `pair_list` (`:273-279`) iterates every pair with no
   `span == 1` exclusion, adding `weights[(i,j)]·w(y_j−y_i)` for each.
2. The `q_i·w(g_i)` terms are a SEPARATE loop (`:268-271`), added on top.

Hence for each i the functional contains BOTH `q_i·w(g_i)` AND `(2/(7−1))·w(g_i)`
(the span-one pair (i,i+1) is exactly w(y_{i+1}−y_i) = w(g_i)). Tawan's F_T, which
restricts the pair sum to r=2..6, is NOT what the code computes.

(Note: the same is true in the "h" scheme, where there is no separate q_i but the
span-one pairs with coefficient 1/3 are part of the full pair sum. The audit's F_V
characterization holds for both schemes.)

## (c) Kernel w definition (verbatim)

`w = (K/K0)^2`, K a sinc kernel, K0 = K(0):

- `:35-36`
  ```python
        k0 = arb(0)
        for c, w in zip(self.coeffs, self.omegas):
            k0 += c * 2 * (w / 2).sin() / w
        self.k0 = k0
        self.k0sq = k0 * k0
  ```
- `:39-48` (`K(x)`)
  ```python
        pi = arb.pi()
        total = arb(0)
        for c, w in zip(self.coeffs, self.omegas):
            a = (w - 2 * pi * x) / 2
            b = (w + 2 * pi * x) / 2
            total += c * (_sinc(a) + _sinc(b)) / 2
        return total
  ```
- `:102-104` (`w_point`, and the cell lower bound at `:60-65` uses
  `ratio = k / self.k0`, `low = ratio.abs_lower()`, returning
  `math.nextafter(low*low, -math.inf)`)
  ```python
    def w_point(self, x):
        k = self.K(arb(x))
        return (k / self.k0) ** 2
  ```

Normalization: w = (K/K0)² with K0 = K(0) = Σ_j c_j·(2 sin(w_j/2)/w_j). For the
cosine kernel (the certified run's family) `cosine_kernel(alpha)` (`:108`) is
`KernelArb([1.0], [float(alpha)])`.

## (d) Domain constraints on g and the candidate point

The verified statement is F(g_1..g_6) ≥ target **for all g_i ≥ 0** (docstring `:18`),
discretized on cells of size 1/grid (grid=4000), with the domain truncated by the
pressure cutoff:

- `:199-201`
  ```python
     cutoff_cells = int(math.ceil(_up(cutoff_units) * grid)) + 1
     cell_count = cutoff_cells + 8
  ```
  with `cutoff_units = target / pressure` (`:198`).
- pressure prune (per-box lower bound on Σg_i):
  ```python
        # pressure prune: sum of gap lower bounds beyond cutoff
        if sum(part[0] for part in box) >= cutoff_cells:
            pruned_pressure += 1
            continue
  ```
- one-body pruning uses only `p_i·g + q_i·w(g) < target` (cells outside any
  surviving component are excluded; `:217-245`).

So: **no sign constraints beyond g_i ≥ 0; no upper box bounds except the cutoff**
Σg_i < cutoff_cells/grid ≈ 23.7 (for the certified run) and per-coordinate one-body
extent; no explicit normalization (y_0=0, y_j = g_1+…+g_j is by construction, total
sum unconstrained within the cutoff).

Candidate g = (7993,4182,7967,8003,7971,4197)/4000: cell indices (7993,4182,7967,
8003,7971,4197); all lie inside the surviving components of cert_790.log
(e.g. coord 0: (3718,4971)∪(6965,49247) contains 7993; coord 1: (3717,4968)∪(6979,
37531) contains 4182; etc.); Σ = 40313 < cutoff_cells = 94802. **The candidate lies
inside the verified domain.** (CHECKED NUMERICALLY against log components.)

## (e) Verdict (again)

**IMPLEMENTED = F_V** — the audit is right about the code: the verifier certifies
Σp_i·g_i + Σq_i·w(g_i) + Σ_{0≤i<j≤6}(2/(7−(j−i)))·w(y_j−y_i), span-one pair terms
included in addition to the q_i terms, NOT Tawan's F_T (r=2..6 only). PROVEN by
direct reading.

## (f) Parameters of the certified eps=0.0079 run (as printed in cert_790.log)

Verbatim from `tmplogs/cert_790.log`:

```
  grid=4000 cutoff_cells=94802 cell_count=94810
  kernel table built in 0.6s sha=c3859c7b4d8bcc6d
  coord 0: 2 components: [(3718, 4971), (6965, 49247)]...
  coord 1: 2 components: [(3717, 4968), (6979, 37531)]...
  coord 2: 2 components: [(3727, 4950), (6995, 45735)]...
  coord 3: 2 components: [(3727, 4950), (6995, 45735)]...
  coord 4: 2 components: [(3717, 4968), (6979, 37531)]...
  coord 5: 2 components: [(3718, 4971), (6965, 49247)]...
  initial boxes: 64
VERIFY_RESULT {"verified": true, "nodes": 27679928, "status": null, "reason": null, "pruned_interval": 13839793, "pruned_pressure": 0, "pruned_tangent": 203}
```

- grid=4000; pressure = 1/3000, target = 0.0079 inferred from
  `cutoff_cells = ceil(up((target/pressure))*grid)+1 = 94802`
  (CHECKED NUMERICALLY: 0.0079·3000 = 23.7; nextafter(23.7)·4000 = 94800.00…;
  ceil = 94801; +1 = 94802 ✓).
- alpha and the p_i/q_i coefficient vectors are NOT printed in the log (INCONCLUSIVE
  from the log alone). The mirror-symmetric component structure (coord 0 = coord 5,
  coord 1 = coord 4, coord 2 = coord 3) and relative extents (p=1177 coords shortest
  extent 37531, p=877 coords 45735, p=946 coords 49247) are CONSISTENT with the
  TAWAN-baseline-style symmetric coefficients in the code
  (`:527-530`: p=[946,1177,877,877,1177,946]/1920000, q=[0.31343, 1/3, 0.35324, …]
  under the coboundary scheme), but this is CONJECTURED, not printed.

## Bottom line for the dispute

The certified eps=0.0079 bound is a lower bound for F_V, NOT for Tawan's F_T. Any
claim that the run "certifies F_T" is false as a statement about this code; the
audit's F_V reading of the implementation is accurate.
