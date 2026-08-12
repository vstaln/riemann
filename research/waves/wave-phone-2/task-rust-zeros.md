# Task: rust-zeros — efficient Rust algorithm for non-trivial zeros of ζ, then the statistics it unlocks

**Agent:** EXECUTOR (phone proot). **Charter:** ~/riemann/hooks/agents.md (honesty + PONYTAIL — numbers first, never lazy about rigor). **Mission:** build a FAST Rust Riemann-Siegel zero-finder (100-1000× faster than mpmath zetazero), validate it rigorously, generate 100k+ zeros, then run the statistics that have been starved by slow zeros.

**CONTEXT:** the whole program's statistics run on mpmath zetazero (10k zeros took hours). A Rust implementation (pure std, zero crates, f64) locating zeros via Riemann-Siegel + bisection changes what's possible: 100k zeros in seconds, sharper periodograms, sharper realized m₃ reads. The boxes are x86_64; the laptop just got rustup (stable toolchain at /home/vstaln/.cargo/bin, installing now — poll /tmp/rustup.log until "rustup install done" appears; rustc at /home/vstaln/.cargo/bin/rustc).

**ALGORITHM (self-contained, pure std, no external crates — build offline):**
1. **θ(t)** via Lanczos lnΓ(1/4 + it/2) (accurate ~1e-12 for all t) or the Stirling asymptotic θ(t) = (t/2)ln(t/2π) − t/2 − π/8 + 1/(48t) + 7/(5760t³) for t ≥ 200; validate whichever you use against mpmath for t ∈ {40, 100, 1000}.
2. **Z(t)** = 2Σ_{k=1}^{n} cos(θ(t) − t·ln k)/√k, n = ⌊√(t/2π)⌋, PLUS the Riemann–Siegel tail: (−1)^{n−1} (t/2π)^{−1/4} g₀(a) with a = √(t/2π) − n, g₀(a) = cos(2π(a²−a−1/16))/cos(2πa). Add the g₁ correction term if you can reproduce it from standard references; otherwise the g₀-only residual O(t^{−3/4}) is ~1e-4 at t=10⁶ — fine for locating, but REPORT the residual honestly.
3. **Bracketing:** scan t in steps of 0.2, sign-change → bisection ×60 (→ 1e-9). Verify completeness: found count must match N(T) = (T/2π)ln(T/2π) − T/2π + 7/8 within ±few (Backlund bound) at the top of the range.
4. **VALIDATION (mandatory):** first 100 ordinates vs mpmath zetazero (phone: proot-distro login ubuntu -- python3 -c "from mpmath import zetazero; ..."), max |Δ| < 1e-4 required; ALSO cross-check against the existing tools/data/zeros_computed_10000.txt (first 10k). Report the max residual in the deliverable.

**BUILD/RUN (laptop, its internet already spent on rustup):** ship the .rs via `ssh pc-jump "cat > /root/zeros_rs/main.rs"` (or /home/vstaln if no root write — use `su vstaln -c` as needed), `cargo build --release --offline` in a cargo-less project? NO — simplest: `rustc -O main.rs -o zeros` (no cargo needed at all — pure std). Run: `./zeros 100000 > /root/zeros_rs/zeros_100k.txt` (or via su vstaln). Use nohup + poll for runs > 60 s (they won't be — expect seconds).

**THEN THE PAYOFF (statistics on the new zeros):**
1. **Periodogram F̂(α) at N=100k** (the bump analysis): reuse the methodology of results/bump_price2.py (see it), extend to 100k zeros: band (1.005,1.3] mean F and band-mean z-score (n_eff scaling: σ ≈ √(n_eff)); compare vs the N=10k result (mean 1.056, z=+0.43). Does the band excess sharpen, persist, or vanish? State the new z.
2. **Realized m₃(1/2) read at N=100k**: the zeros' marked third moment (marks ≡ 1, standardized: m₃ = Σ(z_i−z̄)³/... per the m₃ machinery in research/notes/attack-twobandwidth.md — read that first for the exact definition/units). Error bar ~ N^{−1/2}; the PROVEN value is 5 (Rudnick–Sarnak). Confirm the realized read agrees within error.
3. **New territory (pick what runs fast):** zero-spacing statistics (nearest-neighbor distribution at N=100k — Wigner vs Poisson gap), Gram's law violation rate, or the N(T) Backlund check at T=10⁵.

**HARD CAPS:** write ~/riemann/tools/zeros_rust/README.md + the .rs source by your 8th tool use; run+validate by 12th; deliverable ~/riemann/research/waves/wave-phone-2/results/rust-zeros.md by 16th; < 150K tokens. bash < 90 s (nohup + poll for the big runs). No subagents.

**Deliverable:** results/rust-zeros.md — the algorithm, validation table (max residual), 100k-zero file location + checksum-ish stats (count, T_max, N(T) check), and the three statistics with the sharpened numbers.
**Report < 100 words:** validation residual, zeros generated, and the sharpened band-z / m₃ / spacing findings. End: RESULT: <status> — <one line>.
