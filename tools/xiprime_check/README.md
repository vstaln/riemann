# tools/xiprime_check — ξ′ numerical verification toolkit

Independent, high-precision (mpmath, 60 digits unless noted) verification of the
ξ′-on-the-critical-line structure and of the XiPrime certificate constants
(Lean `Zeta23/XiPrime/`, paper Remark 7.3: 0.85838 / 0.86864 simple-on-line,
0.92919 / 0.93432 distinct, flat vs quartic window).

All scripts run with:
    uv run --quiet --with mpmath python <script> [args]

| script | purpose | command | runtime |
|---|---|---|---|
| `check_small_t.py [ngaps]` | H(t)=i·ξ′(1/2+it) zeros: two 60-digit formulations (direct + Z-form) cross-checked; evaluates the previous agent's claimed small-t roots; scans (0,γ₁) (expects 0 zeros); counts and locates the on-line ξ′-zeros in the first `ngaps` zeta-zero gaps + far-out sample gaps; diffs against `tools/data/xiprime_on_line_1_1000.txt` | `python check_small_t.py 20` (~7 min) / `50` (~11 min) | 60 digits |
| `check_cert.py` | reproduces κ₁(1,v) = (∫v²+2∫₀¹D₁(v⋆v))/(∫v)² for vFlat, vQuartic, vCos(√2·) from the D₁ series; checks the certified bounds 0.85838371 / 0.92919185 / 0.86864017 / 0.93432008 | `python check_cert.py` (~2 min) | 50 digits |
| `check_tower.py` | derivative tower: exactly one ξ″-zero in each interval between consecutive ξ′-zeros (interlacing), including (0, u₁) | `python check_tower.py` (~9 min) | 60 digits |
| `check_count.py` | full-range count of on-line ξ′-zeros in (0.05, γ₁₀₀₀] (999 expected) — count-only, dps=25, slow (~30 min); the same count is established faster by `check_small_t.py` + the f64 full scan | `python check_count.py` | 25 digits |
| `check_consistency.py` | H_direct vs H_zform vs complex-derivative cross-check (debug) | `python check_consistency.py` | 60 digits |

Captured runs: `small_t_run.txt`, `cert_run.txt`, `tower_run.txt`.

## Key results (details in research/notes/attack-xiprime.md)

1. True on-line ξ′-zeros (60 digits): exactly one in each zeta-zero gap (γ_n, γ_{n+1}),
   n = 1,…,999; the zero at t = 0 (ξ′(1/2) = 0 by the functional equation); **none** in (0, γ₁).
   First gap root: t = 15.5857085898293423445957292355.
2. The previous agent's ten "small-t roots" below γ₁ (tools/data/xiprime_on_line_1_1000.txt
   entries 1–10) and its gap-1 root 16.152219566157 are **numerical artifacts** of its f64
   pipeline (a sign bug in its ψ recursion for |z|<10 and Stirling divergence in θ for |z|<1,
   both confined to t < 20; its Z(t) itself is accurate). All its gap-2+ roots agree with the
   60-digit values to ≤ 4·10⁻⁶ (f64 Z′-noise level). Resolution: no hole; the small-t density
   is consistent with RvM for ξ′ and with the 0.85838 certificate.
3. Certificate constants reproduced: κ₁(1,flat) = 1.1416159452907819718 → 2−κ₁ = 0.85838405470921802815,
   3/2−κ₁/2 = 0.92919202735460901408; κ₁(1,quartic) = 1.1313594848334966975 → 0.86864051516650330245 /
   0.93432025758325165123. All four certified lower bounds (≥ 0.85838371, 0.92919185, 0.86864017,
   0.93432008) hold. Both κ₁ lie inside their certified intervals [κ₉, κ₉+ε₉].
4. Mechanism: the ξ′-functional uses the pair density D₁(r) = r − 4r² + Σ 2·4^{k+1}k!/(2k+2)! r^{2k+3}
   in place of ζ's |s−s′| kernel; the ζ-optimal cosine is NOT optimal for ξ′:
   κ₁(cos(√2·)) = 1.1321111348009480644 > κ₁(quartic) = 1.1313594848334966975 (quartic better),
   consistent with the CONJECTURED mechanism in research/notes/attack-kernel.md.
5. Derivative tower: ξ″ interlacing verified numerically (one ξ″-zero per ξ′-gap); a Farmer-style
   combination of per-derivative certificates is a plausible route to distinct-ζ bounds — CONJECTURED.
