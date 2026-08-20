# Alien Novel Probes — Design Spec (Wave 89→100)

**Date:** 2026-08-20
**Status:** Approved (YES)
**Classification per brainstorming skill:** Architectural — new subsystem (4 Rust discriminators + frontier integration), restructures how swarm achieves global RH separation vs previous local Jensen-disc ceiling.

## 1. Context & Problem

- **Solved local result:** `jensen_probe` honest `E(c,r)=Σ log(r/|ρ-c|)` via 100k LMFDB zeros: `c=0.75 r=0.30 β0=0.80 t0=14.1347 → E_RH=0.1823 E_false=1.7917 gap=1.609 dt<0.2958`, drops to `gap 0.63 @14.28`, `0.001 @14.43`, `0 @T≥30`. Wave 88 synthesis: NO CHECKED+VERIFIED survivor, all honest gaps are geometric containment, not global discriminator. `dist(c,Re=0.5)=0.25<r=0.30` so `E_RH>0` even under RH — null premise false.
- **Lower bound ceiling:** Lean `0.68182868746` universal (two-moment), repo `0.67348/0.83674`, `sinc_m3_cert θ=0.55-0.58` proves too much, `angle_kernel` `c1 0.75329` infeasible, `finitet-cinf` heavy T≥50k INCONCLUSIVE. Firewall holds.
- **Goal for 89→100:** Replace 1-body disc containment with N-body global invariants that fire at blind `14.28 (=t0+r/2)` and far `30/50` independent of center. Must pass hostile verifier + RH-false control (planted `β0=0.80` or Davenport-Heilbronn) and never claim `E_RH=0` when `Re_dist<r`.

## 2. Approaches Considered (2-3)

1. **Recommended — Alien 4-probe crate (chosen):** One crate `tools/alien_probes` with 4 bins sharing zero/prime loaders. Each bin <150 lines, <5s, reads existing `tools/data/zeros_rust_100k.txt` or sieves to 1e5, computes one global statistic + planted delta. Keeps LangGraph topology, only touches `swarm.py` whitelist string and `--frontier-file`. YAGNI: no new validator, no Python math. Trade-off: needs 4 honest implementations now, but reuses all proven harness (auto `--manifest-path`, 60s kill, verifier blind+far rule).
2. **Single heavy probe:** One `coulomb_energy` only, deep physics, slower to falsify. Rejected: wants 12 waves of bandwidth, not one bet.
3. **Pure LLM idea-gen without bins:** Let swarm invent math, Python validates. Rejected: violates RUST-ONLY compute, proven to inflate CONJECTURED→VERIFIED (waves 78/79 lessons).

## 3. Architecture

```
tools/alien_probes/
  Cargo.toml  (4 [[bin]] → src/bin/*.rs, shared loader)
  src/bin/kolmogorov_prime.rs   A. Cut-complexity / compression
  src/bin/diffraction_logp.rs   B. Log-prime quasicrystal S(k)
  src/bin/coulomb_energy.rs     C. Log-gas ΔH/N
  src/bin/persistence_zero.rs   D. Gap barcode / H1 hole
tools/swarm_langgraph/swarm.py  (+4 names to DIRECT-RH whitelist)
research/waves/wave-89..100  (append-only, same StateGraph)
```

Data flow: `swarm.py:planner → idea_gen(4) → gate(DEATH_PATTERNS hybrid-aware) → executor(cargo run --manifest-path auto-injected) → verifier(adversarial, requires blind+far) → judge(synthesis) → critique → finalize`. Python never computes — Rust bins print `E_RH/gap/ΔH/S(k)/L` lines, exit 0 ⇒ `CHECKED NUMERICALLY`.

## 4. Components

### 4.1 kolmogorov_prime
- **Alien primitive:** `cut` complexity `K(N)` of prime indicator `1_{prime}(n) n≤N`.
- **Compute:** sieve to N (default 200k, flag `--N`), LZ76 phrase count `C` via standard incremental dictionary, plus Fourier power `F(T)=|Σ_{p≤N} p^{-1/2} e^{i T log p}|` and predicted RH-false shift `ΔF ≈ N^{β0-1/2}/log N`. Prints `C_RH, C_false_pred, F_RH, ΔF`. Label CONJECTURED if sieve fails else CHECKED.
- **Control:** planted `β0=0.80` predicts `N^{0.30}` compression; gap `ΔC/C ≈ 15%` at N=200k derivation in header. Blind test: same N, different T window.
- **Edge:** N>1e6 → early exit INCONCLUSIVE to stay <5s.

### 4.2 diffraction_logp
- **Compute:** primes to N=1e5, `S(k)=|Σ_p exp(i k log p)|^2` sampled `k∈[0,100]` Δ0.05 plus exact `T0=14.1347,14.28,30,50`. Also diffuse floor `D = median S - min S`.
- **Control:** Davenport-Heilbronn `β0=0.80` adds diffuse `~N^{2β0-1}=N^{0.6}` → predicted `D_false/D_RH ≈ 1.2`. Prints both.
- **Performance:** O(N·K) naive 1e5·2000=200M ops borderline; use single pass per k with precomputed `log p` vector, <3s.

### 4.3 coulomb_energy
- **Compute:** Load 100k zeros γ, take window `T∈[0,1000]` N≈400, `H= Σ_{i≠j} log|γ_i-γ_j| + Σ V(γ_i)` where `V` is confining ` (γ log γ)`. Compute `ΔH = H_planted - H_RH` where one zero moved `0.5→β0` at t0 (replace nearest). Print `H_RH/N, H_false/N, ΔH/N`. Global: same ΔH should appear at blind center `t0+0.145` reduced only by overlap factor.
- **Control:** Local disc gave `ΔH≈log(r/d0)=1.79` for one particle; N-body screening gives `ΔH/N≈0.004` prediction printed. Blind+far replication required by verifier.

### 4.4 persistence_zero
- **Compute:** Gaps `g_i=γ_{i+1}-γ_i` for first 5k zeros, barcode of `H0` (gap distribution variance `Var(g)`) and simple `H1` proxy: 2D nearest-neighbor hole radius `R = min_{i≠j} | (β_i-0.5,γ_i-γ_j) |`. For RH, `R≈2.5` (spacing), planted reduces to `≈0.30`. Print `Var_RH, Var_false, R_RH, R_false`.
- **Control:** Off-line zero creates short-lived H1 bar length `≈0.30` derivation in comments. Blind offset must show same hole at shifted T.

### 4.5 Swarm glue (bounded)
- **File:** `tools/swarm_langgraph/swarm.py` lines 352-361 `ALLOWED BINS` string. Add `, kolmogorov_prime, diffraction_logp, coulomb_energy, persistence_zero` to `DIRECT-RH:` list and to `idea["rust_cmd"]` validator regex.
- **Frontier file:** `/tmp/wave89_frontier.txt` ... `/tmp/wave100_frontier.txt` (reuse same 4 examples, each citing one alien bin with `--planted-beta 0.80 --centers 14.1347,14.28,30,50` including blind+far).
- **No topology change:** StateGraph nodes unchanged, `PLANNER→IDEA-GEN*→GATE→EXECUTOR*→VERIFIER*→JUDGE→SYNTHESIZER→CRITIQUE`.

## 5. Error Handling & Honesty

- Missing `tools/data/zeros_rust_100k.txt` or sieve OOM → bin prints `WARN` + exits 0 with `INCONCLUSIVE` note (does not panic). Zero distances `<1e-12` skipped (duplicate).
- `r_max` / `--c-re` flags reuse `jensen_probe` semantics; alien bins use `--N/--k-max/--T0` only, reject unknown flags with usage + exit 1 → executor labels INCONCLUSIVE.
- `ΔH, D, C` predictions are derived in crate header comments with formula; verifier will REFUTE if bin claims `VERIFIED` without blind `14.28` line.
- Strict gate: empty `rust_cmd` or bin not in whitelist ⇒ `INCONCLUSIVE`, `CONJECTURED` never promoted (2026-08-20 fix 3 invariant preserved).

## 6. Testing / Verification

- Build: `cargo build --release --manifest-path tools/alien_probes/Cargo.toml` must succeed (no `rug/arb`, only `std`).
- Smoke (<5s each): `cargo run --bin kolmogorov_prime -- --N 50000`, `diffraction_logp --N 20000`, `coulomb_energy --T0 14.1347`, `persistence_zero` → each prints `DONE` + numeric gap, exit 0.
- Swarm dry-run: `python tools/swarm_langgraph/swarm.py --dry-run` → Graph compiles.
- Wave 89 pilot: `4×2×2 --rust-timeout 60 --frontier-file /tmp/wave89_frontier.txt` → 8 ideas, ≥6 with alien `rust_cmd`, ≥4 CHECKED NUMERICALLY, verifier requires `14.28` in output else INCONCLUSIVE (catches local-only).
- Barrier: reuse `sinc_m3_cert` fake-Weil control unchanged; proportionality firewall still holds (lowers vs direct tracked separately).

## 7. Rollout Until 100

- Wave 89: launch 4-bin pilot above; record which invariant survives blind+far (expect `coulomb_energy ΔH/N` most robust, `diffraction_logp` second).
- Waves 90-92: Lit search — permute joint functional `c1,θ,χ-order` via alien weight `exp(α·S(k))` or `exp(α·ΔH)` in `finitet-cinf` hybrid (cheap `T=600` table, not heavy scan).
- Waves 93-96: Transport — Beurling `d_N` with alien weight `w=exp(α·E)` at `N=500..2000` (island defect).
- Waves 97-100: Synthesis — best survivor + Olver uniform asymptotics for Lipschitz `Δt≈0.19` cover to `H=100`; if still local-only, ledger closes as `finite-height cert to 100, not proof` (honest, no inflation).

## 8. Risks

- Sieve Fourier O(NK) may exceed 60s at N=200k → mitigation: default N=50k smoke, progressive.
- Log-gas double sum O(N²) at N=2000 is 4M, fine; larger N capped.
- LLM may ignore whitelist despite prompt → executor gate will mark INCONCLUSIVE (safe, not VERIFIED).
