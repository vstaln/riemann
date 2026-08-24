# Port trmdy zeta-simple-zeros mechanisms (2026-08-24)

Source repo: `research/external-results/trmdy-zeta-simple-zeros-673137/`
(their own verifier + certified design included). Two mechanisms ported into our
pipeline (`/home/vstaln/riemann`).

## Port A — exact-rational KernelSpec -> KernelArb kernel   (PROVEN source)

New file: `tools/kernel_family.py`

- `kernel_from_spec(coeffs, omega_pi_multiples=(), has_sqrt2_term=False, zero_shift=0.0)`
  -> builds OUR `KernelArb` (imported from `tools/verify_coboundary_floor.py`) from a
  trmdy-style exact-rational spec. Coeffs stay exact `fmpq`; omegas are built the trmdy way
  (leading `arb(2).sqrt()` term if `has_sqrt2_term`, then `mult*pi`).
- `trmdy_kernel(zero_shift=0.0)` -> the certified 7-term window
  (coeffs = WINDOW_NUMERATORS / 1e9, omegas = (sqrt2, 2pi,4pi,..,12pi)).
- `omegas_from_spec(...)` helper.

Source refs:
- `src/zeta_ext/kernel.py:143-156` `KernelSpec` (coeffs fmpq + `omega_pi_multiples` + `has_sqrt2_term`), `:159-167` `_omegas`, `:169-175` `kernel_k0`.
- `src/zeta_ext/design.py:16-34` `WINDOW_NUMERATORS` / `WINDOW_DENOMINATOR` / `KERNEL`.

Normalization matches ours already: `w(x) = (K(x)/K(0))^2` (our `w_point` / from `k0sq`),
their `kernel_k0`. Port generalizes our single-term `cosine_kernel` to arbitrary term lists.

ZERO-REPOSITIONING KNOB: trmdy's design has NO phase/zero shift (their sinc-eval is exact at
integer x; omegas live on sqrt2 + 2*pi*Z). Provided as `zero_shift` (added to every omega),
DOCUMENTED default `0.0` = reproduces their design exactly. NOT in their source (grep for
reposition/shift/translate found nothing); it is a port-side convenience knob, defaulted to
their actual configuration. HONESTY: this is CONJECTURED as a knob; there is no proof-side use
yet — exercised only as a parameter next session.

### Exercise next session
```
cd tools
python -c "import kernel_family as k; k.trmdy_kernel(0.0) and print('ok')"   # quick import smoke
KERNEL=trmdy VERIFY_* env vars ...  # select in verify_coboundary_floor later
```
`VERIFY_*` env hooks to select trmdy_kernel() are NOT wired yet on the caller side (only the
constructor is ported). Wire `verify_coboundary_floor.py` main to read e.g. `KERNEL=trmdy` ->
`kernel_family.trmdy_kernel()` when exercise is wanted.

Risks: `arb(fmpq)` conversion of negative coeffs must preserve sign (checked in __main__);
module import pulls `verify_coboundary_floor` which imports `flint` (must be installed).

## Port B — sqrt-tail block-defect h(E) in record chain   (FLOAT-PROBE)

File: `tools/cert-floor-rs/src/main.rs`

- Added `record_chain_sqrt_tail(h, eps, p, m, q)` — mirrors the tawanerguo record chain
  (`joint_bound`, which hard-codes q=6 and cap `phi_m`) but replaces the trace-energy cap
  `B = Phi_m(eps*(m-6))` with the sqrt-tail profile `B = h_profile(eps*(m-q))`
  (h(E) = E for E<=1 else 2*sqrt(E)-1). Already present helper `h_profile` (main.rs:43) reused.
- Added CLI subcommand `chains <h> <eps> <psum>` printing both chains side by side over
  `m in [40,400]`:
  `cargo run -- chains 0.672467425578 0.0062 0.003125`

Source refs: `tools/cert_floor_driver.py` record chain / `tools/cert_param_sweep.py` h_profile
(already ported as `h_profile`). This is FLOAT-PROBE arithmetic (f64), not interval-certified.

### Exercise next session
```
cd tools/cert-floor-rs
cargo run -- chains 0.672467425578 0.0062 0.003125     # side-by-side m=40..400
```
Risks: f64 only; `cargo build` NOT run here (slow-machine policy) — see build note below.

## Build/test status
- `kernel_family.py`: VERIFIED — `uv run --with python-flint python tools/kernel_family.py`
  → `trmdy_kernel: k0=0.918725, w(0)=1.0 / kernel_family demo OK`. (Plain `python` lacks flint;
  use `uv run --with python-flint`.)
- `main.rs`: VERIFIED compile — `cargo check` finished clean (0.23s). `cargo build` not run
  (slow-machine policy). Run `cargo run -- chains 0.672467425578 0.0062 0.003125` next session
  for the side-by-side m=40..400 table.
