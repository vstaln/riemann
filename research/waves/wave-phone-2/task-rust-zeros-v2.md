# Task: rust-zeros v2 — Gabcke-corrected Riemann-Siegel zero-finder (v1 blocked on tail accuracy)

**Agent:** EXECUTOR (phone proot). **Charter:** ~/riemann/hooks/agents.md. **Mission:** v1 verified the infrastructure and found the blocker: the g₀-only RS tail is O(t^{−3/4}) ≈ 0.5 at t=14 — it cannot pass the <1e-4 first-100 validation. v2 MUST use the full Gabcke-corrected tail. Build, validate, generate 100k zeros, run the statistics.

**STEP 1 — EXTRACT THE EXACT CORRECTION COEFFICIENTS (the v1 handoff's core):**
- On the phone proot: `python3 -c "import mpmath, os; print(os.path.dirname(mpmath.__file__))"` → the mpmath source dir. Read `mpmath/functions/zeta.py` and `zeta_extra.py`: `grep -n "def rs_z\|def _rs\|Gabcke\|_coeff" <dir>/functions/zeta*.py`.
- mpmath's rs_z computes Z(t) = 2Σ_{k≤N} cos(θ(t)−t·ln k)/√k + (−1)^{N−1}(t/2π)^{−1/4} Σ_{j} C_j with the ψ-polynomial corrections (Gabcke). TRANSCRIBE the exact coefficient recurrence (the C₀..C₄ expressions — typically C₀ = g₀(a), C₁ = (1/(2π))·(g₁(a)), …, with a = √(t/2π) − N ∈ [0,1)) into the mission notes BEFORE writing Rust.
- θ(t): use Lanczos lnΓ(1/4+it/2) (self-contained ~20 lines) — NOT the Stirling asymptotic (unreliable below t~200). Validate θ vs mpmath at t ∈ {14, 50, 100, 1000}.

**STEP 2 — RUST (pure std, no crates):** Z(t) with the Gabcke tail, scan t step 0.2 → sign-change → bisection ×60. Completeness: N(T) = (T/2π)ln(T/2π) − T/2π + 7/8 within ±few at the top. Validate: first 100 vs mpmath zetazero (max |Δ| < 1e-4 REQUIRED) + cross-check vs tools/data/zeros_computed_10000.txt.

**STEP 3 — SHIP/BUILD/RUN (laptop, rustc 1.97.1 at /home/vstaln/.cargo/bin — rustup DONE):**
- Ship: `ssh pc-jump "mkdir -p /root/zeros_rs; cat > /root/zeros_rs/main.rs" < main.rs` (root-write worked for /tmp; if it fails use su vstaln -c + /home/vstaln/zeros_rs).
- Build: `ssh pc-jump "rustc -O /root/zeros_rs/main.rs -o /root/zeros_rs/zeros"` (export PATH=/home/vstaln/.cargo/bin:$PATH first).
- Run: `ssh pc-jump "/root/zeros_rs/zeros 100000 > /root/zeros_rs/zeros_100k.txt"` — expect seconds; nohup+poll if >60 s.
- Pull a slice for validation: `ssh pc-jump "head -100 /root/zeros_rs/zeros_100k.txt"` and compare vs mpmath on the phone.

**STEP 4 — THE STATISTICS (same as v1):**
1. Periodogram band (1.005,1.3] mean F + band-mean z at N=100k vs N=10k (mean 1.056, z=+0.43) — reuse results/bump_price2.py methodology on the new zeros.
2. Realized marked m₃(1/2) at N=100k vs PROVEN 5 (definition: research/notes/attack-twobandwidth.md; error bar ~N^{−1/2}).
3. Nearest-neighbor spacing stats (Wigner vs Poisson) or Gram's-law violation rate at N=100k.

**HARD CAPS:** notes with the extracted coefficients by your 5th tool use; .rs source + README in ~/riemann/tools/zeros_rust/ by your 10th; validate by 13th; deliverable ~/riemann/research/waves/wave-phone-2/results/rust-zeros.md by 17th; < 150K tokens; bash < 90 s; crash-proof (append after every computation); no subagents.

**Deliverable:** results/rust-zeros.md — the coefficient transcription, validation table (max residual first-100 + vs 10k file), zero-file stats (count, T_max, N(T) check), the three statistics.
**Report < 100 words:** coefficients used, validation residual, zeros generated, sharpened band-z / m₃ / spacing. End: RESULT: <status> — <one line>.