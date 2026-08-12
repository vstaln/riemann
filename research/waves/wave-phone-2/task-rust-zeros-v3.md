# Task: rust-zeros v3 — HYBRID zero-finder (E-M + RS-g₀), fully specified. NO coefficient archaeology.

**Agent:** EXECUTOR (phone proot). **Charter:** ~/riemann/hooks/agents.md. **Mission:** v1 found g₀-only RS fails at low t; v2 confirmed mpmath's rs_z is the FULL rigorous algorithm (rszeta.py, ~1500 lines, arbitrary-precision — transcribing it to Rust is the trap; BOTH prior agents died there). **v3's design is FIXED (below) — do not re-derive coefficients, do not read rszeta.py, just implement the spec.** The goal is 100k zeros accurate to ≤1e-3 for STATISTICS (periodogram/m₃/spacing), NOT a new zero-computation record.

**THE FIXED DESIGN (pure-std Rust, no crates, f64):**
1. **θ(t)** = (t/2)ln(t/2π) − t/2 − π/8 + 1/(48t) + 7/(5760t³) for t ≥ 200 (error < 1e-10). For t < 200 the hybrid path (below) uses ζ directly — θ not needed.
2. **Low-t path (t < 200): Euler–Maclaurin ζ(1/2+it), N=40 terms.** ζ(s) = Σ_{n=1}^{N−1} n^{−s} + N^{1−s}/(s−1) + N^{−s}/2 + Σ_{k=1}^{20} B_{2k}/(2k)! · (s)_{2k−1} · N^{−s−2k+1}, with B₂..B₄₀ hardcoded f64 (compute once via the recurrence B₀=1, Σ_{k=0}^{n−1} C(n,k)B_k = 0 — or hardcode the standard values; verify B₂=1/6, B₄=−1/30, B₆=1/42). Error at t<200, N=40 ≪ 1e-10. Z(t) = Re(e^{−iθ(t)}ζ(1/2+it)) — compute θ here via the SAME asymptotic (fine at t ≥ 14: error ~1e-9) — or better: Z = (−1)^{n}·... simplest: Z(t) = 2·Re(ζ(1/2+it))·cos(θ(t)) + 2·Im(ζ(1/2+it))·sin(θ(t))?? NO — Z(t) = ζ(1/2+it)·e^{iθ(t)} — take Re. Just compute θ(t) from the asymptotic for t in [14,200] (error ≤ 1e-9) and use Z = Re(ζ·e^{iθ}).
3. **High-t path (t ≥ 200): Riemann–Siegel g₀-only.** n = ⌊√(t/2π)⌋, a = √(t/2π) − n; Z(t) = 2Σ_{k=1}^{n} cos(θ(t) − t·ln k)/√k + (−1)^{n−1}·(t/2π)^{−1/4}·g₀(a), g₀(a) = cos(2π(a²−a−1/16))/cos(2πa). Residual O(t^{−3/4}) ≤ 7e-4 at t=10⁵ — position error ≤1.2e-4 — adequate. REPORT the residual (validate vs the zeros files).
4. **Bracketing:** scan t step 0.2 from t=14 to T_max; sign change → bisection ×80. Completeness: count vs N(T) = (T/2π)ln(T/2π) − T/2π + 7/8 within ±5 at T_max.
5. **VALIDATION (the honesty bar):** first 100 vs mpmath zetazero (proot-distro login ubuntu -- python3 -c "from mpmath import zetazero; print([float(zetazero(k)) for k in [1,2,3,10,50,100]])" etc.) + first 10000 vs tools/data/zeros_computed_10000.txt (format: check its first line). REPORT max |Δ| (expect ~1e-4 to 1e-3; if >1e-2 something is WRONG — fix). The statistics need ≤1e-3; the deliverable states the actual residual honestly.

**BUILD/RUN:** rustup DONE on the laptop — VERIFY FIRST: ssh pc-jump "ls /home/vstaln/.cargo/bin/rustc /root/.cargo/bin/rustc 2>/dev/null" (it may be at either; export PATH accordingly). Ship: ssh pc-jump "mkdir -p /root/zeros_rs; cat > /root/zeros_rs/main.rs" < main.rs; build: rustc -O ... -o zeros (if /root unwritable use su vstaln -c + /home/vstaln/zeros_rs). Run: /root/zeros_rs/zeros 100000 > zeros_100k.txt (expect ~30-120 s; nohup+poll if longer). Pull slices: ssh pc-jump "head -120 zeros_100k.txt" for validation.

**THE STATISTICS (the payoff — on the phone with the pulled zeros):**
1. Periodogram band (1.005,1.3] mean F + band-mean z at N=100k vs N=10k (mean 1.056, z=+0.43) — reuse results/bump_price2.py methodology (read it first).
2. Realized marked m₃(1/2) at N=100k vs PROVEN 5 (def in research/notes/attack-twobandwidth.md; error bar ~N^{−1/2}).
3. Nearest-neighbor spacing: mean/Wigner-vs-Poisson diagnostic at N=100k.

**HARD CAPS:** .rs source + README in ~/riemann/tools/zeros_rust/ by your 8th tool use (write it locally FIRST, then ship); validate by 12th; deliverable ~/riemann/research/waves/wave-phone-2/results/rust-zeros.md by 16th; < 150K tokens; bash < 90 s; crash-proof; no subagents; DO NOT read rszeta.py or re-derive coefficients.

**Deliverable:** results/rust-zeros.md — design, validation table (max residual first-100 + vs 10k file), zero-file stats (count, T_max, N(T) check), the three statistics.
**Report < 100 words:** validation residual, zeros generated, sharpened band-z / m₃ / spacing. End: RESULT: <status> — <one line>.