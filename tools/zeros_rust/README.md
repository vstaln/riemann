# rust-zeros v3 — hybrid zero-finder (pure-std Rust, f64)

Per `research/waves/wave-phone-2/task-rust-zeros-v3.md` (FIXED design; no coefficient
archaeology, rszeta.py intentionally not read).

## Design

- **Low t < 200:** Euler–Maclaurin ζ(1/2+it), N=40 terms, k=1..20 Bernoulli tail.
  Bernoulli numbers computed at startup from the recurrence B₀=1, Σ C(n+1,k)B_k=0
  (assert-checked: B₂=1/6, B₄=−1/30, B₆=1/42). Z(t)=Re(e^{iθ}ζ).
- **High t ≥ 200:** Riemann–Siegel g₀-only: n=⌊√(t/2π)⌋, a=√(t/2π)−n,
  Z = 2Σcos(θ−t ln k)/√k + (−1)^{n−1}(t/2π)^{−1/4}cos(2π(a²−a−1/16))/cos(2πa).
  Residual O(t^{−3/4}) — reported honestly vs the 10k file.
- θ(t) asymptotic: t/2·ln(t/2π) − t/2 − π/8 + 1/(48t) + 7/(5760t³) (error < 1e-9 for t≥14).
- **Scan:** step 0.2 from t=14, sign change → bisection ×80. Completeness: found vs
  N(T)= (T/2π)ln(T/2π) − T/2π + 7/8 at last zero.

## Algorithm cross-check

`check_algo.py` (numpy port of the identical f64 formulas): first 20 zeros vs mpmath
`zetazero` → max|Δ| = 1.4e-14 (VALIDATION of logic; the Rust binary's real residual
vs the 10k file is reported in results/rust-zeros.md).

## Build / run (laptop, pc-jump)

```sh
ssh pc-jump "mkdir -p /root/zeros_rs; cat > /root/zeros_rs/main.rs" < main.rs
ssh pc-jump "cd /root/zeros_rs && rustc -O main.rs -o zeros"
ssh pc-jump "cd /root/zeros_rs && nohup ./zeros 100000 > zeros_100k.txt &"
# poll: tail -2 zeros_100k.txt ; wc -l zeros_100k.txt
```

Output format: `# header`, one zero per line `idx ordinate` (flushed per zero —
crash-proof), `# done:` summary line.

## Statistics (phone)

1. Periodogram band (1.005,1.3] mean F + band-z at N=100k vs N=10k — methodology
   from `results/bump_price2.py`.
2. Realized marked m₃(1/2) vs PROVEN 5 (def in `research/notes/attack-twobandwidth.md`;
   empirical method from `tools/m3_zeros_check.py`).
3. Nearest-neighbor spacing mean + Wigner-vs-Poisson diagnostic.
