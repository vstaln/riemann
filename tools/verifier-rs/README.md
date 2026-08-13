# verifier-rs — Rust interval verifier (WIP)

Rug/MPFR port of `tools/verify_coboundary_floor.py`. Status: WIP.

**Key honest finding (see research/notes/eps-boundary-exact.md):**
- Arb (python-flint) ball enclosures and rug/MPFR enclosures are both valid
  lower bounds but have DIFFERENT widths, so node counts will NOT match
  (Python's certified 0.00620 run: 1,096,556 nodes; Rust: different count).
- The eps=0.00620 boundary is PROVEN exact: 0.00621 is a real inequality
  violation (true F_B=0.0059188 at the terminal cell, 60-digit mpmath), so
  NO tighter table can certify 0.00621. The Rust verifier's purpose is an
  independent sound cross-check, not eps breakthrough.
- Tangent bound (convexity/LDL) is ESSENTIAL for certification: Python
  without tangent fails 0.00620 (terminal-cell at 47,319 nodes); with
  tangent it certifies (1,096,556 nodes). The Rust port implements the
  interval type + kernel table + range-minimum + B&B; the tangent bound
  (exact LDL in interval arithmetic) remains to be ported.

Build (musl): RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" cargo build --release --target x86_64-unknown-linux-musl
