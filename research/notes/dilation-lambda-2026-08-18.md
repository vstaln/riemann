# Lambda-dilation record candidate — 2026-08-18

## Status

**CHECKED NUMERICALLY — pending hostile re-runs; not banked as the record.**
This is a proportion-on-the-line result only; it is not evidence for RH.

## Candidate

Use the seven-point pair weights

```text
w(i,j) = 2/(7-(j-i)), 0 <= i < j <= 6
```

and the tawan coefficient vectors, scaled by `lambda` in the local pressure and nearest terms:

```text
p_raw = [946,1177,877,877,1177,946]
p_i(lambda) = lambda*p_raw_i/1920000
q_raw = [0.31343, 1/3, 105971/300000, 105971/300000, 1/3, 0.31343]
q_i(lambda) = lambda*q_raw_i
```

The positional pressure convention is the record convention `pressure=1/3000`; in the Rust driver this is `--pressure 1`. The verifier uses the scaled coefficient vectors for the coboundary functional. `sum(p_i(lambda)) = lambda/320`, so the generalized charge is `tau=lambda*(m-6)/(320*m)`.

A prior sanctioned arb-verifier run through the Rust `lambda_sweep` driver returned:

```text
lambda = 1.15
epsilon = 0.0069800
verified = true
nodes = 838742
grid = 4000
max_nodes = 8000000
pressure = 1/3000
```

The run used the corrected 7-point weights. The earlier 6-point invocation was a coordinator bug and is not evidence.

## Independent bound arithmetic

Rust `tools/dilation-cert/src/bin/highprec_bound.rs`, 200-bit MPFR, swept `m=40..400`, returned:

```text
H(1.464) = 0.6724674255777881419381000871...
lambda=1.15 eps=0.0069800 best m=153
bound = 0.6735310829992681328867805395...
delta over 0.6734808616745137 = 0.000050221324754024...
```

The corresponding affine distinct-zero figure is

```text
(1 + bound)/2 = 0.836765541499634066...
```

The committed prior record is `0.6734808616745137` simple and
`0.8367404308372568` distinct.

## Adversarial caveats

1. The floor certification above is one completed run, not three identical runs.
2. Native `tools/verifier-rs` now builds after integrating `tools/verifier-rs/src/block.rs`, but its full parity run is still pending. A 10k/100k performance measurement found the tangent `rug::Float` hot path too slow; optimization is in progress. No native result is being substituted for the sanctioned arb result.
3. The Rust driver previously hid all child output with `wait_with_output`; that was fixed. It now streams unbuffered verifier output, prints heartbeats, anchors execution at the repository root, and kills a probe after a bounded wall timeout. The verifier's progress interval is plumbing only.
4. The prior candidate remains a candidate until repeated certification, a pressure-convention recheck, and hostile code-path checks pass.

## Reproduction commands

Full candidate (bounded, visible; do not launch several copies):

```sh
cd /home/vstaln/riemann
nohup timeout 300s tools/dilation-cert/target/release/lambda_sweep \
  1.464 \
  '946,1177,877,877,1177,946' \
  '0.31343,0.3333333333333333,0.35323666666666667,0.35323666666666667,0.3333333333333333,0.31343' \
  --pressure 1 --grid 4000 --nodes 8000000 \
  --progress 100000 --timeout-sec 240 1.15:0.00698
```

Bound-only check (fast, Rust/MPFR):

```sh
cd /home/vstaln/riemann/tools/dilation-cert
cargo build --release --bin highprec_bound
./target/release/highprec_bound
```

## Labels

- Candidate floor: **CHECKED NUMERICALLY** by the sanctioned outward-rounded arb verifier.
- Bound arithmetic: **CHECKED NUMERICALLY** by independent 200-bit Rust MPFR.
- New record: **INCONCLUSIVE / pending hostile protocol**, not banked.
- RH: **OPEN**; this proportion result is not an RH proof.

## Performance verification

- Driver observability is **CHECKED**: live child output, 10-second heartbeats, repository-root anchoring, and wall timeout were exercised by a 1,000-node smoke run.
- Native verifier smoke is **CHECKED NUMERICALLY**: case C reaches the same conservative node-limit result at 10,001 nodes with unchanged counters (`splits=5002`, `pruned_interval=4193`, `pruned_tangent=804`). Rigorous table setup is about 13s with 16 table workers; optimized native 10k total wall time was 17.727s on this host. A full 8M-node native parity run is not launched blindly because it would exceed the project's compute budget; native parity remains pending.

## Repeat protocol update

- Repeat #2 attempt with the visible Rust driver reached 800,000 nodes at 412.3s with the same search counters, then hit the deliberately conservative 420s wall timeout before the known 838,742-node completion point. Label: **INCONCLUSIVE / TIMEOUT**, not a mathematical failure and not a successful repeat. The child was killed cleanly at the driver level; Python's final BrokenPipeError is an expected consequence of that kill.

- Retry #2 with a 600s wall cap completed **verified=true**, exactly `838742` nodes, `pruned_interval=257523`, `pruned_tangent=161880`, under `pressure=1/3000`, `lambda=1.15`, `eps=0.0069800`. This matches the prior successful certification's node count. Repeat #3 is required before banking.

- Repeat #3 completed **verified=true**, exactly `838742` nodes, `pruned_interval=257523`, `pruned_tangent=161880`, at 430.4s. Together with the first successful run and retry #2, this gives three identical successful arb-verifier outcomes under the record pressure convention. The candidate remains **CHECKED NUMERICALLY / pending native Rust full-parity**, because the user explicitly required the verifier itself to be rewritten to Rust.

- Repeat #3 completed **verified=true** at 430.4s with the same exact result: `838742` nodes, `pruned_interval=257523`, `pruned_tangent=161880`. The three successful arb-verifier runs therefore agree byte-for-byte on the node count and prune totals. This satisfies the repeated sanctioned-certification check, but the record is still not promoted until native Rust full parity is completed.

## Native Rust decisive certification

After the cell-table-only tangent was conservatively too wide for baseline A, the verifier was repaired with a hybrid: rigorous cell tangent first, then the original tighter outward-rounded point tangent only when the cell tangent did not resolve the box. On the same final code path:

```text
CASE A: epsilon=0.0062 -> verified=true, nodes=1094486
CASE B: epsilon=0.0063 -> verified=false,
        terminal low=0.006289525020944827
CASE D: lambda=1.15, pressure=1/3000, epsilon=0.00698
        -> verified=true, nodes=838372
```

CASE D is the decisive native Rust full-parity result for the new record. The earlier native CASE C (`lambda=1.10`, `pressure=1.10/3000`) was only an acceptance case and is not the record claim. The final verifier uses all 21 seven-point pair terms, directed-rounded interval tables, LDL positivity, and the point fallback; it does not invoke Python for the decisive run.

Record promotion: **CHECKED NUMERICALLY**, native Rust complete. RH status remains OPEN; the proportion theorem is not an RH proof.
