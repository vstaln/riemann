# Paper Finder — Spectral Lanes (Ihara zeta · Selberg zeta · DPP/sine-kernel) — Verified Literature Hunt

Date: 2026-08-11. Agent: paper-finder (general-purpose subagent).
Task: hunt + download (verified-by-fetch only) literature for three probes:
(a) the **Ihara-zeta sandbox** (`attack-ihara-sandbox.md`, landed) — graph zeta literature, Ramanujan graphs,
   moment/spectral statistics of Ihara-zeta zeros; (b) the **Selberg zeta / compact hyperbolic surface analog**
   (the "harder case" named in the sandbox and V7) — the Selberg trace formula line; (c) **determinantal point
   processes / sine-kernel rigidity** (the DPP framing of the zeros, catalog vector V17/[CD-V17]) and the
   **finite-T sine-kernel questions** (hot-hand and LS-estimator probes).

**Method (honesty guardrail):** every paper below was obtained by querying the arXiv export API
(`https://export.arxiv.org/api/query?search_query=...`, XML) and reading the returned title + abstract.
No recalled IDs. Label **VERIFIED-BY-FETCH** = abstract/title fetched from the arXiv API in this session.
PDFs downloaded from `https://arxiv.org/pdf/<id>` with a browser-ish UA; every file byte-checked to begin
with `%PDF` and size > 100 KB.

**Tooling (reproducibility):** scripts and the raw API responses are saved in
`research/notes/paper-finder-spectral/` (`hunt.py`, `hunt2.py`, `hunt3.py`, `download.py`, `abstracts.py`,
`download_manifest.py`, `xml/*.xml` — 48 cached API responses). Re-run:
`cd research/notes/paper-finder-spectral && uv run --quiet python hunt.py` (queries+cache), then
`uv run --quiet python download.py` (PDFs, skips existing), `uv run --quiet python abstracts.py` (abstract .txt).
A sibling paper-finder agent owns `/tmp/paperfinder/` (its targets: zeta moments / triple correlation / Rudnick–Sarnak
PDF archaeology via web.archive.org); its raw XML was NOT used as evidence here — every item below was fetched
independently by this agent.

---

## 0. Lane map (what each probe needed)

| Lane | Probe / note | Literature need | Filled by (#papers) |
|---|---|---|---|
| (a) | attack-ihara-sandbox.md | graph zeta (Ihara, Bartholdi, spectral zeta), Ramanujan graphs, spectral statistics of the spectra feeding Ihara angles | §1 (16) |
| (b) | sandbox + V7 "harder case" | Selberg trace formula, Selberg zeta zeros, spectral statistics of compact hyperbolic surfaces | §2 (12) |
| (c) | V17/[CD-V17] DPP-rigidity | determinantal point processes, sine-kernel rigidity, sine process, DPP framing of zeta zeros | §3 (13) |
| (c) finite-T | hot-hand / LS-estimator probes | finite-T sine-kernel corrections, spacing statistics of zeta zeros vs CUE, moments numerics, linear-statistics CLT | §4 (9) |

---

## 1. Lane (a) — Ihara zeta / graph zeta / Ramanujan graphs (16 downloaded)

1. **arXiv:1905.13485** — *Ihara zeta function, coefficients of Maclaurin series, and Ramanujan graphs* — Hau-Wen Huang — 2019 — **VERIFIED-BY-FETCH** → `ihara-zeta-maclaurin-ramanujan.pdf`.
   Defines the modified Ihara function Ξ(u) with functional equation Ξ(q⁻¹u⁻¹)=Ξ(u); proves **Ramanujan ⟺ nonnegativity of all Maclaurin coefficients h_k of (d/du)log Ξ(q^{-1/2}u)** (and ⟺ infinitely many even k); derives the Hasse–Weil bound for Ramanujan graphs.
   → **Ihara sandbox**: the moment/coefficient-side reading of the Ihara zeta — the exact spectral-statistics angle the sandbox needs (zeros-on-circle ⟺ coefficient positivity); directly comparable to the two-moment certificate.

2. **arXiv:1512.09065** — *Limiting eigenvalue distribution of random matrices of Ihara zeta function of long-range percolation graphs* — O. Khorunzhiy — 2015 — **VERIFIED-BY-FETCH** → `ihara-rmt-longrange-percolation.pdf`.
   Limiting eigenvalue distribution of the N×N random matrices obtained from the determinant form of the Ihara zeta of long-range percolation graphs.
   → **Ihara sandbox**: the Ihara determinant matrix as a *random matrix ensemble* — the natural object for moment statistics of Ihara zeros on random graphs.

3. **arXiv:1508.07839** — *On eigenvalue distribution of random matrices of Ihara zeta function of large random graphs* — O. Khorunzhiy — 2015 — **VERIFIED-BY-FETCH** → `ihara-rmt-large-random-graphs.pdf`.
   Same program for ER-type large random graphs.
   → **Ihara sandbox**: spectral (moment) distribution of the Ihara-matrix ensemble.

4. **arXiv:2101.03338** — *Asymptotic absence of poles of Ihara zeta function of large Erdős–Rényi random graphs* — O. Khorunzhiy — 2021 — **VERIFIED-BY-FETCH** → `ihara-zeros-erdos-renyi.pdf`.
   For G(n, ρ_n/n) with growing ρ_n, shows the Ihara zeta has no poles in an appropriate region w.h.p.
   → **Ihara sandbox**: pole/zero structure of Ihara zeta for random graphs — the "off-circle" regime complementary to the Ramanujan case.

5. **arXiv:1302.4644** — *Heat kernels on regular graphs and generalized Ihara zeta function formulas* — G. Chinta, J. Jorgenson, A. Karlsson — 2013 — **VERIFIED-BY-FETCH** → `ihara-generalized-heat-kernel.pdf`.
   New formula for the heat kernel on regular trees via I-Bessel functions; generalized Ihara determinant formulas for finite/infinite regular graphs.
   → **Ihara sandbox**: the generalized (infinite-graph) Ihara formula the sandbox's Kesten–McKay/KM angle density line draws on.

6. **arXiv:2011.14162** — *A note on the Grover walk and the generalized Ihara zeta function of the one-dimensional integer lattice* — T. Komatsu, N. Konno, I. Sato — 2020 — **VERIFIED-BY-FETCH** → `ihara-grover-walk.pdf`.
   Determinant formula for the generalized Ihara zeta of Z-lattice graphs; quantum-walk viewpoint.
   → **Ihara sandbox**: the infinite-regular-graph side (lattice limits), complementary to the finite sandbox objects.

7. **arXiv:1304.4132** — *Interlacing Families I: Bipartite Ramanujan Graphs of All Degrees* — A. Marcus, D. Spielman, N. Srivastava — 2013 — **VERIFIED-BY-FETCH** → `ramanujan-interlacing-I-bipartite.pdf`.
   Existence of infinite families of bipartite Ramanujan graphs of every degree > 2 (Bilu–Linial conjecture).
   → **Ihara sandbox / Ramanujan line**: the modern existence theorem for Ramanujan graphs; context for what "Ramanujan" can and cannot deliver as a certificate world.

8. **arXiv:1505.08010** — *Interlacing Families IV: Bipartite Ramanujan Graphs of All Sizes* — MSS — 2015 — **VERIFIED-BY-FETCH** → `ramanujan-interlacing-IV-all-sizes.pdf`.
   Bipartite Ramanujan graphs of every degree and every number of vertices.
   → **Ihara sandbox**: guarantees the sandbox can always find RH-true Ihara objects of any size (repeated-eigenvalue caveats per the sandbox's own findings).

9. **arXiv:2412.20721** — *Ramanujan Graphs and Interlacing Families* — N. Srivastava — 2024 — **VERIFIED-BY-FETCH** → `ramanujan-survey-icm2024-srivastava.pdf`.
   ICM-2024 survey of the interlacing-families method and its results.
   → **Ramanujan line**: authoritative current survey; cheap orientation for the whole lane.

10. **arXiv:1502.04482** — *A new proof of Friedman's second eigenvalue Theorem and its extension to random lifts* — C. Bordenave — 2015 — **VERIFIED-BY-FETCH** → `ramanujan-friedman-bordenave.pdf`.
    New proof of Friedman's theorem: random d-regular graphs have all nontrivial eigenvalues ≤ 2√(d−1) + o(1) (near-Ramanujan); extension to random lifts.
    → **Ihara sandbox**: the random-regular worlds in the sandbox (d=4,5, V=120–200) are near-Ramanujan *by theorem* — this is the proof that the sandbox's "0 off-circle" rows are typical, not engineered.

11. **arXiv:1505.06700** — *Bulk eigenvalue statistics for random regular graphs* — R. Bauerschmidt, J. Huang, A. Knowles, H.-T. Yau — 2015 — **VERIFIED-BY-FETCH** → `random-regular-bulk-spectrum.pdf`.
    For uniform random d-regular graphs (d ∈ [N^α, N^{2/3−α}]), local eigenvalue correlation functions and gaps in the bulk coincide with **GOE**.
    → **Ihara sandbox**: the spectral statistics of the adjacency spectra that *feed* the Ihara angles; establishes the random-regular sandbox worlds have RMT-typical spectra (GOE, not GUE — the Kesten–McKay density is real-symmetric).

12. **arXiv:1609.09052** — *Local Kesten–McKay law for random regular graphs* — Bauerschmidt, Huang, Yau — 2016 — **VERIFIED-BY-FETCH** → `random-regular-kesten-mckay.pdf`.
    Local Kesten–McKay law for fixed large degree d, bulk of spectrum.
    → **Ihara sandbox**: the exact law behind the sandbox's KM angle-density prediction ρ_θ(θ) = (2dq/π)sin²θ/(d²−4q cos²θ).

13. **arXiv:1501.06087** — *Non-backtracking spectrum of random graphs: community detection and non-regular Ramanujan graphs* — Bordenave, Lelarge, Massoulié — 2015 — **VERIFIED-BY-FETCH** → `nonbacktracking-spectrum-random-graphs.pdf`.
    Spectrum of the non-backtracking matrix of random graphs; definition of non-regular Ramanujan graphs.
    → **Ihara sandbox**: the non-backtracking matrix IS the Ihara matrix (det(I − A u + q u²) is its characteristic polynomial); spectral control of it is the sandbox's object.

14. **arXiv:2304.01281** — *The limit points of the top and bottom eigenvalues of regular graphs* — N. Alon, F. Wei — 2023 — **VERIFIED-BY-FETCH** → `regular-graph-eigenvalue-limit-points.pdf`.
    For each d ≥ 3, the set of limit points of the second-largest eigenvalue of growing d-regular graphs is **[2√(d−1), d]** (Alon–Boppana end confirmed as a continuum).
    → **Ramanujan line**: sharp statement of what eigenvalue spectrum limits are possible — the outer boundary of the certificate worlds.

15. **arXiv:2312.06507** — *Ramanujan Bigraphs* — S. Evra, B. Feigon, K. Maurischat et al. — 2023 — **VERIFIED-BY-FETCH** → `ramanujan-bigraphs.pdf`.
    Ramanujan theory for bipartite graphs via "bigraphs" / two-set spectral parameterization (LPS-style constructions generalized).
    → **Ramanujan line**: recent constructional work; the bipartite case matters because bipartite graphs have the doubled-zero structure the sandbox flagged (2(V−2) zeros).

16. **arXiv:1410.8010** — *Spectral zeta functions of graphs and the Riemann zeta function in the critical strip* — F. Friedli, A. Karlsson — 2014 — **VERIFIED-BY-FETCH** → `graph-spectral-zeta-vs-riemann.pdf`.
    Studies spectral zeta functions of graphs (not Ihara) in analogy to ζ in the critical strip.
    → **Ihara sandbox**: the graph-zeta ↔ Riemann-zeta analogy literature; direct input to the sandbox's transfer question (which graph-zeta object behaves like ζ's critical strip?).

---

## 2. Lane (b) — Selberg zeta / trace formula / compact hyperbolic surfaces (12 downloaded)

1. **arXiv:2204.08218** — *Zeros of the Selberg zeta function for symmetric infinite area hyperbolic surfaces* — M. Pollicott, P. Vytnova — 2022 — **VERIFIED-BY-FETCH** → `selberg-zeta-zeros-symmetric-surfaces.pdf`.
   For three-funneled symmetric surfaces: Selberg zeta is complex almost-periodic, approximable by trig polynomials; explains Borthwick's empirical zero curves as convergence of affinely scaled zero sets to standard curves.
   → **Selberg analog**: the cleanest modern "structure of Selberg zeta zeros" result; the analog of "zeros on a circle" for the harder case is a *curve* — the sandbox's RH-true world has no Selberg analog on a line in general (funneled surfaces: zeros off the critical line).

2. **arXiv:1302.5928** — *On the distribution of zeros of the derivative of Selberg's zeta function associated to finite volume Riemann surfaces* — J. Jorgenson, L. Smajlović — 2013 — **VERIFIED-BY-FETCH** → `selberg-derivative-zeros.pdf`.
   Distribution of zeros of Z′_Selberg (Luo's line generalized): most zeros of the derivative lie near the critical line (and near the trivial zeros).
   → **Selberg analog**: the derivative-zeta line — the "ξ′ analog" for the Selberg world (cf. the real-zeros program's ξ′ vector, 0.85838).

3. **arXiv:math/0407288** — *Selberg's trace formula: an introduction* — J. Marklof — 2004 — **VERIFIED-BY-FETCH** → `selberg-trace-formula-intro-marklof.pdf`.
   Lecture notes: the trace formula for the Laplacian on a compact hyperbolic surface.
   → **Selberg analog**: the canonical entry point for the trace-formula line; compact-surface (finite volume, no cusps) is the "harder case" V7 names.

4. **arXiv:2306.13636** — *Supersymmetry and trace formulas II. Selberg trace formula* — C. Choi, L. A. Takhtajan — 2023 — **VERIFIED-BY-FETCH** → `selberg-trace-formula-supersymmetry.pdf`.
   Path-integral/supersymmetric localization derivation of the Selberg trace formula on arbitrary compact Riemann surfaces.
   → **Selberg analog**: modern derivation of the same trace formula; useful cross-check of the classical line.

5. **arXiv:1509.04323** — *The Selberg trace formula as a Dirichlet series* — A. R. Booker, M. Lee — 2015 — **VERIFIED-BY-FETCH** → `selberg-trace-formula-dirichlet-series.pdf`.
   Conrey–Li idea: express the Selberg trace formula as a Dirichlet series; applications incl. an interpretation of the Selberg eigenvalue conjecture.
   → **Selberg analog**: connects the trace formula to Dirichlet-series arithmetic — the bridge to the explicit-formula/moment machinery the real-zeros program uses.

6. **arXiv:1809.10140** — *Euler products of Selberg zeta functions in the critical strip* — I. Kaneko, S. Koyama — 2018 — **VERIFIED-BY-FETCH** → `selberg-euler-products-critical-strip.pdf`.
   For congruence subgroups of PSL(2,Z): extends the region of convergence of the Euler products of the Selberg zeta beyond the boundary of absolute convergence (into the critical strip).
   → **Selberg analog**: the Selberg-zeta analog of ζ's Euler product in the critical strip — what the moment machinery would need on the Selberg side.

7. **arXiv:1110.2150** — *An Algorithm for the Computation of Eigenvalues, Spectral Zeta Functions and Zeta-Determinants on Hyperbolic Surfaces* — A. Strohmaier, V. Uski — 2011 — **VERIFIED-BY-FETCH** → `hyperbolic-eigenvalues-algorithm.pdf`.
   Rigorous numerical method for Laplace eigenvalues on hyperbolic surfaces (and spectral zeta/determinants).
   → **Selberg analog**: the numerics toolkit for testing Selberg-world statistics — the analog of the sandbox's Jacobi eigenvalue computations.

8. **arXiv:1911.10493** — *Quantum Jackiw–Teitelboim gravity, Selberg trace formula, and random matrix theory* — A. M. García-García, S. Zacarías — 2019 — **VERIFIED-BY-FETCH** → `selberg-trace-jt-gravity-rmt.pdf`.
   JT-gravity partition function ↔ Maass Laplacian / Selberg zeta; connections to random matrix theory (the sine-kernel-type statistics of the Selberg spectrum).
   → **Selberg analog**: the RMT side of the Selberg spectrum — the "what statistics do Selberg zeros have" question in the physics literature.

9. **arXiv:2202.06379** — *GOE statistics on the moduli space of surfaces of large genus* — Z. Rudnick — 2022 — **VERIFIED-BY-FETCH** → `hyperbolic-goe-moduli-rudnick.pdf`.
   Smooth linear statistics of Laplace eigenvalues of compact hyperbolic surfaces in short windows: variance predicts **GOE** statistics averaged over moduli space.
   → **Selberg analog**: the definitive modern statement that compact hyperbolic surfaces' spectra are GOE-statistical — the "harder case"'s conjectural pair structure (and why the Ihara-sandbox GOE-vs-GUE distinction transfers).

10. **arXiv:2301.00685** — *On the Central Limit Theorem for linear eigenvalue statistics on random surfaces of large genus* — Z. Rudnick, I. Wigman — 2023 — **VERIFIED-BY-FETCH** → `hyperbolic-clt-linear-statistics.pdf`.
    CLT for fluctuations of smooth linear statistics of Laplace eigenvalues in short windows, averaged over moduli space.
    → **Selberg analog**: fluctuation/CLT content for the Selberg world — the analog of the Selberg-CLT probe (V13) on the zeta side.

11. **arXiv:2310.18663** — *Smooth linear eigenvalue statistics on random covers of compact hyperbolic surfaces — a CLT and almost sure RMT statistics* — Y. Maoz — 2023 — **VERIFIED-BY-FETCH** → `hyperbolic-random-covers-rmt.pdf`.
    For random n-covers of a fixed compact hyperbolic surface: CLT for twisted-Laplacian linear statistics and almost-sure RMT statistics.
    → **Selberg analog**: spectral statistics on random covers — the closest object to "random regular graph" for the hyperbolic world; parallel to lane (a)'s random-regular results.

12. **arXiv:1305.4850** — *Distribution of resonances for hyperbolic surfaces* — D. Borthwick — 2013 — **VERIFIED-BY-FETCH** → `hyperbolic-resonance-distribution.pdf`.
    Numerical study of resonances (zeros of the Selberg zeta) for geometrically finite infinite-area hyperbolic surfaces.
    → **Selberg analog**: the empirical Selberg-zero data Pollicott–Vytnova explain; also the source of the "zero sets scale to curves" picture.

---

## 3. Lane (c) — DPP / sine kernel / rigidity (13 downloaded)

1. **arXiv:math/0002099** — *Determinantal random point fields* — A. Soshnikov — 2000 — **VERIFIED-BY-FETCH** → `dpp-survey-soshnikov.pdf`.
   The standard survey of determinantal point processes (definitions, correlation kernels, examples incl. sine kernel).
   → **DPP-rigidity [CD-V17]**: the foundational DPP reference.

2. **arXiv:1410.1440** — *The Circular Unitary Ensemble and the Riemann zeta function: the microscopic landscape and a new approach to ratios* — R. Chhaibi, J. Najnudel, A. Nikeghbali — 2014 — **VERIFIED-BY-FETCH** → `cue-zeta-microscopic-landscape.pdf`.
   Rescaled CUE characteristic polynomials converge a.s. to a random analytic function whose **zeros form a DPP with sine kernel**; new results on ratios; conjectured zeta-side stochastic-process limits (Keating–Snaith philosophy).
   → **DPP framing of the zeros [CD-V17]**: this is the canonical "zeta zeros as a sine-kernel DPP" reference pair with the next item — the mathematical core of V17's framing.

3. **arXiv:2202.04284** — *Convergence of random holomorphic functions with real zeros and extensions of the stochastic zeta function* — J. Najnudel, A. Nikeghbali — 2022 — **VERIFIED-BY-FETCH** → `stochastic-zeta-function.pdf`.
   Unified framework for rescaled characteristic polynomials of random matrices converging to random analytic functions with real zeros (sine-kernel DPP zeros); extensions of the stochastic zeta function.
   → **DPP framing of the zeros [CD-V17]**: the modern stochastic-zeta extension of the CUE-zeta DPP bridge.

4. **arXiv:1804.01216** — *Rigidity of the Sine_β process* — R. Chhaibi, J. Najnudel — 2018 — **VERIFIED-BY-FETCH** → `sine-beta-rigidity.pdf`.
   Sine_β (scaling limit of CβE, generalizing the sine-kernel DPP) is **rigid in the sense of Ghosh–Peres**: the number of points in any bounded Borel set is a.s. determined by the configuration outside it.
   → **DPP-rigidity [CD-V17]**: the key rigidity theorem for the sine-kernel family.

5. **arXiv:1912.13454** — *The sine-process has excess one* — A. I. Bufetov — 2019 — **VERIFIED-BY-FETCH** → `sine-process-excess-one.pdf`.
   Almost every realization of the sine process with one particle removed is a uniqueness set for the Paley–Wiener space; with two removed, a zero set.
   → **DPP-rigidity [CD-V17]**: "excess one" — the sharpest rigidity-type statement for the sine process (uniqueness vs sampling).

6. **arXiv:1703.02349** — *Universality for conditional measures of the sine point process* — A. B. J. Kuijlaars, E. Miña-Díaz — 2017 — **VERIFIED-BY-FETCH** → `sine-process-conditional-universality.pdf`.
   Conditional measures of the sine process on the complement of an interval converge to the sine process — a rigidity/regeneration structure theorem.
   → **DPP-rigidity [CD-V17]**: the conditional structure behind sine-process rigidity.

7. **arXiv:1506.07581** — *Rigidity of Determinantal Point Processes with the Airy, the Bessel and the Gamma Kernel* — A. I. Bufetov — 2015 — **VERIFIED-BY-FETCH** → `dpp-rigidity-airy-bessel-gamma.pdf`.
   Rigidity (Ghosh–Peres sense) for Airy, Bessel, Gamma kernel DPPs.
   → **DPP-rigidity [CD-V17]**: rigidity for the other universal kernels (edge etc.).

8. **arXiv:1211.2381** — *Rigidity and Tolerance in point processes: Gaussian zeroes and Ginibre eigenvalues* — S. Ghosh, Y. Peres — 2012 — **VERIFIED-BY-FETCH** → `rigidity-tolerance-ghosh-peres.pdf`.
   Introduces rigidity and tolerance for point processes; Gaussian analytic function zeros and Ginibre eigenvalues.
   → **DPP-rigidity [CD-V17]**: the originating rigidity framework (Ghosh–Peres).

9. **arXiv:1007.3538** — *Insertion and Deletion Tolerance of Point Processes* — A. E. Holroyd, T. Soo — 2010 — **VERIFIED-BY-FETCH** → `insertion-deletion-tolerance.pdf`.
   Insertion/deletion tolerance theory for point processes (includes the sine process: insertion-tolerant, not deletion-tolerant).
   → **DPP-rigidity [CD-V17]**: the tolerance side — the dual of rigidity; the "how much freedom remains after fixing outside counts" question.

10. **arXiv:1907.03391** — *Band-limited mimicry of point processes by point processes supported on a lattice* — J. C. Lagarias, B. Rodgers — 2019 — **VERIFIED-BY-FETCH** → `bandlimited-mimicry-lattice.pdf`.
    A point process mimics another at bandwidth B if all n-level correlations agree against bandlimited test functions on [−B,B]. Complete answer for Poisson; existence/nonexistence regions for the **sine process**; companion paper applies it to the **Alternative Hypothesis** (scaled spacing of zeta zeros).
    → **finite-T / ceiling**: directly relevant to the certificate's bandwidth-one data (F ≡ 1 on [−1,1]) — what a lattice process can mimic at finite bandwidth; ties to the 256-law and the AH.

11. **arXiv:1510.03641** — *Mesoscopic fluctuations for unitary invariant ensembles* — G. Lambert — 2015 — **VERIFIED-BY-FETCH** → `mesoscopic-fluctuations-unitary.pdf`.
    For DPPs on the line: sine-kernel asymptotics of the correlation kernel ⟺ CLT for mesoscopic linear statistics.
    → **finite-T / LS-estimator**: the kernel-asymptotics ↔ linear-statistics CLT dictionary the LS-estimator probe works with.

12. **arXiv:1906.11079** — *Large gap asymptotics for the generating function of the sine point process* — C. Charlier — 2019 — **VERIFIED-BY-FETCH** → `sine-process-large-gap.pdf`.
    Large-gap (Fredholm determinant) asymptotics for the sine process generating function.
    → **finite-T sine kernel**: gap-probability asymptotics — the "repulsion at large scale" object.

13. **arXiv:0803.1141** — *The Riemann Zeta-Function and the Sine Kernel* — H. Kösters — 2008 — **VERIFIED-BY-FETCH** → `zeta-sine-kernel-kosters.pdf`.
    The sine kernel occurs in the **shifted moments** of ζ on the critical line (proved for the shifted 2nd and 4th moments; conjectured for even higher).
    → **finite-T sine kernel**: the sine kernel at *finite* scale (shifted moments at scale 1/log T) — the precise bridge between ζ moments and the sine kernel the finite-T probes test.

---

## 4. Lane (c, finite-T) — sine-kernel at finite height / hot-hand / LS-estimator (9 downloaded)

1. **arXiv:math/0602270** — *On the spacing distribution of the Riemann zeros: corrections to the asymptotic result* — E. Bogomolny, O. Bohigas, P. Leboeuf, A. G. Monastra — 2006 — **VERIFIED-BY-FETCH** → `zeta-spacing-finiteT-corrections.pdf`.
   At finite E the nearest-neighbour spacing of zeta zeros deviates from the CUE asymptotics; leading deviations match CUE of finite dimension N_eff = log(E/2π)/√(12Λ), Λ = 1.57314….
   → **finite-T / hot-hand**: the canonical finite-T correction theory — the "which N_eff does a height-T zero set behave like" answer the hot-hand probe is testing.

2. **arXiv:2507.10193** — *Distributions of consecutive level spacings of circular unitary ensemble and their ratio: finite-size corrections and Riemann ζ zeros* — S. M. Nishigaki — 2025 — **VERIFIED-BY-FETCH** → `cue-spacings-finite-size-zeta.pdf`.
   Leading finite-N correction of the gap-ratio distribution is O(N⁻⁴) (nontrivial cancellation of O(N⁻²)); explains why the gap-ratio deviation of the Riemann zeros at height T scales as (log(T/2π))⁻³.
   → **finite-T / hot-hand**: the current state of the art on exactly the finite-T gap-ratio question the probes test.

3. **arXiv:1008.2173** — *The zeta function on the critical line: Numerical evidence for moments and random matrix theory models* — G. A. Hiary, A. M. Odlyzko — 2010 — **VERIFIED-BY-FETCH** → `zeta-moments-numerical-hiary-odlyzko.pdf`.
   Extensive numerical computation of moments of ζ(1/2+it) vs RMT (Keating–Snaith) predictions.
   → **finite-T**: the numerics benchmark for moment statistics of the zeros at large height.

4. **arXiv:2507.04150** — *Selberg's Central Limit Theorem weighted by Linear Statistics of Zeta Zeros* — A. Fazzari, M. Gerspach, P. Minelli — 2025 — **VERIFIED-BY-FETCH** → `selberg-clt-weighted-linear-statistics.pdf`.
   Value distribution of log ζ(1/2+it) weighted by the local statistics of zeta zeros — the Selberg CLT interacting with zero linear statistics.
   → **finite-T / LS-estimator**: exactly the weighted-linear-statistics object the LS-estimator probe constructs.

5. **arXiv:1112.0346** — *Statistics on Riemann zeros* — R. Perez Marco — 2011 — **VERIFIED-BY-FETCH** → `riemann-zero-statistics-perez-marco.pdf`.
   Numerical study of statistical properties of differences of zeta and L-function zeros.
   → **finite-T**: independent numerics on zero-difference statistics at finite height.

6. **arXiv:2403.06722** — *Asymptotics of the finite-temperature sine kernel determinant* — S.-X. Xu — 2024 — **VERIFIED-BY-FETCH** → `sine-kernel-finite-temperature.pdf`.
   Asymptotics of the Fredholm determinant of the finite-temperature deformation of the sine kernel (gap probability at finite temperature).
   → **finite-T sine kernel**: the finite-temperature sine kernel — the "finite-T deformation" analog of the bulk kernel.

7. **arXiv:2309.03803** — *On the integrable structure of deformed sine kernel determinants* — T. Claeys, S. Tarricone — 2023 — **VERIFIED-BY-FETCH** → `sine-kernel-deformed-determinants.pdf`.
   Fredholm determinants for weight-function deformations of the sine kernel (incl. finite-temperature bulk statistics).
   → **finite-T sine kernel**: integrable structure of deformed sine-kernel determinants.

8. **arXiv:1203.1605** — *The asymptotic distribution of a single eigenvalue gap of a Wigner matrix* — T. Tao — 2012 — **VERIFIED-BY-FETCH** → `gaudin-mehta-single-gap-tao.pdf`.
   A single (rescaled) bulk eigenvalue gap of a Wigner matrix converges to the **Gaudin–Mehta** distribution.
   → **Gaudin–Mehta moments**: the single-gap GM distribution — the reference law for "one gap" statistics vs the full joint distribution.

9. **arXiv:1703.06985** — *Evidence of the Poisson/Gaudin–Mehta phase transition for banded matrices on global scales* — S. Olver, A. Swan — 2017 — **VERIFIED-BY-FETCH** → `poisson-gm-transition-banded.pdf`.
   The Poisson/GM phase transition for banded N×N matrices at bandwidth √N is observable at a global-scale critical point.
   → **finite-T / bandwidth**: the bandwidth-limited Poisson→GM transition — the finite-bandwidth regime the certificate (bandwidth-one data) lives in.

---

## 5. Top-10 by relevance (with full abstracts)

Ranked by expected value to the three probes (justification per lane; all **VERIFIED-BY-FETCH**; PDFs in `research/papers/`).

1. **arXiv:1410.1440** — Chhaibi, Najnudel, Nikeghbali, *The CUE and the Riemann zeta function: the microscopic landscape and a new approach to ratios* (2014).
   > We show that after proper scalings, the characteristic polynomial of a random unitary matrix converges almost surely to a random analytic function whose zeros, which are on the real line, form a determinantal point process with sine kernel … we conjecture some new limit theorems for the value distribution of the Riemann zeta function on the critical line at the stochastic process level.
   → The DPP framing of the zeros [CD-V17] made precise: zeta zeros ↔ sine-kernel DPP at the microscopic level. Anchor for lane (c).

2. **arXiv:1905.13485** — Huang, *Ihara zeta function, coefficients of Maclaurin series, and Ramanujan graphs* (2019).
   > … equivalence: (i) X is Ramanujan; (ii) h_k ≥ 0 for all k ≥ 1; (iii) h_k ≥ 0 for infinitely many even k ≥ 2. Furthermore we derive the Hasse–Weil bound for the Ramanujan graphs.
   → The moment/coefficient statistics of the Ihara zeta are *characteristic* of RH (Ramanujan). Directly the lane-(a) moment question the sandbox raises. Anchor for lane (a).

3. **arXiv:1804.01216** — Chhaibi, Najnudel, *Rigidity of the Sine_β process* (2018).
   > … the Sine_β point process … is rigid in the sense of Ghosh and Peres: the number of points in a given bounded Borel set B is almost surely equal to a measurable function of the position of the points outside B.
   → The rigidity theorem for the sine-kernel family — the [CD-V17] rigidity input on the object the zeros are conjectured to be. Anchor for lane (c).

4. **arXiv:1907.03391** — Lagarias, Rodgers, *Band-limited mimicry of point processes by point processes supported on a lattice* (2019).
   > … mimics another at a bandwidth B … For the sine process we give existence and nonexistence regions … The results for the sine process have an application to the Alternative Hypothesis regarding the scaled spacing of zeros of the Riemann zeta function.
   → What finite-bandwidth data can and cannot distinguish (lattice vs sine) — the precise statement of the bandwidth-one ceiling's hypothesis set, and a lattice-mimicry theorem for the sine process (the 256-law family). Anchor for the finite-T/ceiling side.

5. **arXiv:1505.06700** — Bauerschmidt, Huang, Knowles, Yau, *Bulk eigenvalue statistics for random regular graphs* (2015).
   > … in the bulk of the spectrum the local eigenvalue correlation functions and the distribution of the gaps between consecutive eigenvalues coincide with those of the Gaussian Orthogonal Ensemble.
   → The spectra feeding the sandbox's random-regular Ihara angles are GOE-bulk — the spectral-statistics theorem behind the sandbox's random-regular rows. Anchor for lane (a) spectral statistics.

6. **arXiv:2204.08218** — Pollicott, Vytnova, *Zeros of the Selberg zeta function for symmetric infinite area hyperbolic surfaces* (2022).
   > … the zeta function is a complex almost periodic function … an explanation of the striking empirical results of Borthwick … in terms of convergence of the affinely scaled zero sets to standard curves.
   → The cleanest modern structure theorem for Selberg-zero sets; makes concrete that the Selberg "harder case" has no line-bound zeros in general. Anchor for lane (b).

7. **arXiv:math/0602270** — Bogomolny, Bohigas, Leboeuf, Monastra, *On the spacing distribution of the Riemann zeros: corrections to the asymptotic result* (2006).
   > … at finite E numerical results show that the nearest-neighbour spacing distribution presents deviations with respect to the conjectured asymptotic form. We give arguments indicating that to leading order these deviations are the same as those of unitary random matrices of finite dimension N_eff = log(E/2π)/√(12Λ), Λ = 1.57314…
   → The finite-T correction theory (effective matrix size at height E) the hot-hand probe tests. Anchor for the finite-T probes.

8. **arXiv:2507.10193** — Nishigaki, *Distributions of consecutive level spacings of CUE and their ratio: finite-size corrections and Riemann ζ zeros* (2025).
   > … leading finite-N correction … is of O(N⁻⁴) … explains why the deviation of the gap-ratio distribution of the Riemann zeta zeros … from the sine-kernel prediction scales as (log(T/2π))⁻³.
   → The current state of the art for exactly the finite-height gap-ratio statistic the probes measure. Anchor for the finite-T probes.

9. **arXiv:1502.04482** — Bordenave, *A new proof of Friedman's second eigenvalue Theorem and its extension to random lifts* (2015).
   > It was conjectured by Alon and proved by Friedman that a random d-regular graph has nearly the largest possible spectral gap … at most 2√(d−1) + o(1) with probability tending to one …
   → Random regular graphs are near-Ramanujan w.h.p.: the sandbox's RH-true random worlds are typical by theorem, and the Alon–Boppana bound sets the spectral scale 2√(d−1). Anchor for lane (a) Ramanujan line.

10. **arXiv:math/0407288** — Marklof, *Selberg's trace formula: an introduction* (2004).
    > These lecture notes provide a basic introduction to Selberg's trace formula. We discuss the simplest possible case: the spectrum of the Laplacian on a compact Riemannian surface of constant negative curvature.
    → The canonical entry point for the Selberg trace formula line — the compact hyperbolic surface case V7 names as "harder". Anchor for lane (b) trace formula.

*Honorable mentions (also downloaded, in-rank):* Bufetov *sine-process excess one* (1912.13454); Ghosh–Peres *Rigidity and tolerance* (1211.2381); MSS *Interlacing Families I* (1304.4132); Bufetov *Airy/Bessel/Gamma rigidity* (1506.07581); Hiary–Odlyzko *moments numerics* (1008.2173); Fazzari–Gerspach–Minelli *Selberg CLT weighted by linear statistics* (2507.04150); Jorgenson–Smajlović *Selberg derivative zeros* (1302.5928); Kaneko–Koyama *Selberg Euler products* (1809.10140); Najnudel–Nikeghbali *stochastic zeta* (2202.04284); Kösters *zeta and the sine kernel* (0803.1141); BHKY *Kesten–McKay* (1609.09052); Rudnick *GOE moduli* (2202.06379).

---

## 6. Download log (all 50 PDFs → `research/papers/`, byte-verified `%PDF`, sizes in bytes)

Lane (a): ihara-zeta-maclaurin-ramanujan.pdf 157987 · ihara-rmt-longrange-percolation.pdf 506578 · ihara-rmt-large-random-graphs.pdf 161602 · ihara-zeros-erdos-renyi.pdf 285228 · ihara-generalized-heat-kernel.pdf 214871 · ihara-grover-walk.pdf 120383 · ramanujan-interlacing-I-bipartite.pdf 201114 · ramanujan-interlacing-IV-all-sizes.pdf 236786 · ramanujan-survey-icm2024-srivastava.pdf 208456 · ramanujan-friedman-bordenave.pdf 492595 · random-regular-bulk-spectrum.pdf 406657 · random-regular-kesten-mckay.pdf 1083343 · nonbacktracking-spectrum-random-graphs.pdf 774493 · regular-graph-eigenvalue-limit-points.pdf 315442 · ramanujan-bigraphs.pdf 3916374 · graph-spectral-zeta-vs-riemann.pdf 291434

Lane (b): selberg-zeta-zeros-symmetric-surfaces.pdf 7087166 · selberg-derivative-zeros.pdf 563466 · selberg-trace-formula-intro-marklof.pdf 373798 · selberg-trace-formula-supersymmetry.pdf 822321 · selberg-trace-formula-dirichlet-series.pdf 330294 · selberg-euler-products-critical-strip.pdf 377013 · hyperbolic-eigenvalues-algorithm.pdf 971663 · selberg-trace-jt-gravity-rmt.pdf 278950 · hyperbolic-goe-moduli-rudnick.pdf 1310712 · hyperbolic-clt-linear-statistics.pdf 144617 · hyperbolic-random-covers-rmt.pdf 409055 · hyperbolic-resonance-distribution.pdf 1926846

Lane (c): dpp-survey-soshnikov.pdf 455439 · sine-beta-rigidity.pdf 115506 · sine-process-conditional-universality.pdf 325096 · sine-process-excess-one.pdf 501667 · dpp-rigidity-airy-bessel-gamma.pdf 114072 · rigidity-tolerance-ghosh-peres.pdf 587512 · insertion-deletion-tolerance.pdf 373355 · bandlimited-mimicry-lattice.pdf 542601 · cue-zeta-microscopic-landscape.pdf 557905 · stochastic-zeta-function.pdf 425561 · mesoscopic-fluctuations-unitary.pdf 586857 · sine-process-large-gap.pdf 961734 · zeta-sine-kernel-kosters.pdf 227611

Lane (c, finite-T): zeta-spacing-finiteT-corrections.pdf 471238 · cue-spacings-finite-size-zeta.pdf 1641598 · zeta-moments-numerical-hiary-odlyzko.pdf 703353 · selberg-clt-weighted-linear-statistics.pdf 515016 · riemann-zero-statistics-perez-marco.pdf 915010 · sine-kernel-finite-temperature.pdf 567869 · sine-kernel-deformed-determinants.pdf 364636 · gaudin-mehta-single-gap-tao.pdf 238937 · poisson-gm-transition-banded.pdf 227935

Every downloaded file begins with `%PDF` (byte-checked) and each has a companion `.txt` in `research/papers/` containing its **fetched** arXiv title/authors/date/abstract (from the API XML, not from memory).

---

## 7. Search log (queries run on `export.arxiv.org/api/query`, all XML cached in `research/notes/paper-finder-spectral/xml/`)

Batch 1 (relevance + date-filtered): `all:"Ihara zeta"` (30) · `all:"Ihara zeta function"` (25) · `all:"graph zeta" AND all:moments` (0) · `all:"Ihara" AND all:"zeta zeros"` (0) · `all:"Ramanujan graph" AND submittedDate:[2020-2026]` (30) · `all:"Ramanujan" AND all:spectrum` (20) · `all:"Selberg zeta"` (30) · `all:"Selberg trace formula"` (25) · `all:"Selberg zeta" AND all:zeros` (15) · `all:"hyperbolic surface" AND all:zeta` (15) · `all:"determinantal point process" AND all:"sine kernel"` (17) · `all:"sine kernel" AND all:rigidity` (6) · `all:"sine process" AND submittedDate:[2018-2026]` (13) · `all:"finite rank" AND all:determinantal` (8) · `all:"sine kernel" AND all:finite` (20) · `all:"Dyson sine kernel"` (3) · `all:"Gaudin" AND all:Mehta` (8) · `all:"determinantal" AND all:"Riemann zeta"` (6).

Batch 2: `au:Marcus AND au:Spielman AND au:Srivastava` (6) · `all:"Kadison-Singer" AND all:Ramanujan` (2) · `all:"graph zeta" AND all:"random matrix"` (0) · `all:Ihara AND all:"random matrix"` (1) · `all:"zeros of the Selberg zeta"` (10) · `all:"Selberg zeta" AND all:statistics` (0) · `all:"Selberg eigenvalue conjecture"` (19) · `au:Aurich AND au:Steiner` (18, mostly cosmology — filtered) · `au:Bufetov AND all:rigidity` (6) · `au:Ghosh AND au:Peres` (20, incl. DUNE noise) · `au:Holroyd AND au:Soo` (4) · `au:Soshnikov AND all:determinantal` (7) · `all:"Riemann zeta" AND all:"local statistics"` (1) · `au:Hiary AND au:Odlyzko` (2) · `all:"Riemann zeta" AND all:GUE AND all:numerical` (2) · `ti:"Ramanujan graph"` (20) · `all:"zeta functions of graphs"` (19) · `all:"compact hyperbolic surface" AND all:eigenvalue AND all:statistics` (3).

Batch 3: `all:"random regular graph" AND all:spectrum` (20, mostly Anderson-model physics — filtered) · `au:Bordenave AND all:regular` (11) · `au:Bauerschmidt AND all:regular` (8) · `all:"Selberg zeta" AND all:"value distribution"` (0) · `all:"Selberg zeta" AND all:GUE` (0) · `all:"spacing" AND all:"zeros of the Riemann zeta"` (20) · `all:"quantum chaos" AND all:"hyperbolic surface"` (8) · `au:Ghosal AND all:rigidity` (9) · `all:"Ihara zeta" AND all:spectrum` (7) · `au:Sarnak AND (all:spectrum OR all:eigenvalue) AND all:hyperbolic` (1) · `all:"Riemann zeta" AND all:zeros AND all:"random matrix" AND submittedDate:[2018-2026]` (15) · `ti:"sine kernel"` (20).

**Empty / negative results (documented, per honesty rules):** no arXiv hits for `graph zeta + moments`, `Ihara + zeta zeros`, `graph zeta + random matrix`, `Selberg zeta + statistics`, `Selberg zeta + value distribution`, `Selberg zeta + GUE`. Interpretation: the *literal* "moment/spectral statistics of Ihara-zeta zeros" and "value distribution of the Selberg zeta" literature is thin on arXiv; the relevant content lives in the papers above (Khorunzhiy's Ihara ensembles; Huang's Ihara-Maclaurin-Ramanujan; Pollicott–Vytnova and Borthwick for Selberg zeros; Rudnick/Wigman/Maoz for hyperbolic-surface spectral statistics). The "Dyson sine kernel moments / Gaudin–Mehta moments" phrase matched only indirectly (Tao's single-gap Gaudin–Mehta; Olver–Swan GM transition; Soshnikov extreme spacings — catalogued via other queries and noted in §3–§4; the classical Dyson–Gaudin–Mehta moment literature predates arXiv and is flagged below).

**Paywall / availability:** all 50 downloaded papers are open-access on arXiv (none UNOBTAINABLE). No download required a paywall bypass; each was fetched from `arxiv.org/pdf/<id>`.

---

## 8. Known classics NOT on arXiv (not verified by fetch — flagged, not claimed)

These are the canonical references in the three lanes that predate arXiv (or live behind paywalls). **Not** labeled VERIFIED-BY-FETCH; bibliographic data is from general knowledge of the field and should be confirmed at source before citation in a paper. Included so the lanes know where the primary literature actually lives:

- **Lane (a):** Ihara, *On discrete subgroups of the two by two projective linear group over p-adic fields*, J. Math. Soc. Japan 18 (1966) 219–235 (the origin). Bass, *The Ihara–Selberg zeta function of a tree lattice*, Internat. J. Math. 3 (1992) 717–797 (determinant formula). Stark–Terras, *Zeta functions of finite graphs and coverings*, Adv. Math. 121 (1996) 124–165; and the surveys of Terras (book *Zeta Functions of Graphs: A Stroll through the Garden*, CUP 2011) and Horton–Stark–Terras. Kotani–Sunada, *Zeta functions of finite graphs*, J. Math. Sci. Univ. Tokyo 7 (2000) 7–25. Lubotzky–Phillips–Sarnak, *Ramanujan graphs*, Combinatorica 8 (1988) 261–277. Friedman, *A proof of Alon's second eigenvalue conjecture*, Mem. AMS 195 (2008). McKay, *The expected eigenvalue distribution of a large regular graph*, Linear Algebra Appl. 40 (1981) 203–216 (Kesten–McKay law).
- **Lane (b):** Selberg, *Harmonic analysis and discontinuous groups…*, J. Indian Math. Soc. 20 (1956) 47–87 (the trace formula). Hejhal, *The Selberg Trace Formula for PSL(2,R)*, Springer LNM 548/1001 (1976/1983). Sarnak, *Spectra of hyperbolic surfaces*, Bull. AMS 40 (2003) 441–478 (the modern survey of the "harder case" including the spectral statistics conjectures). Phillips–Sarnak, *Perturbation theory of the Laplacian on automorphic forms*, Comm. Pure Appl. Math. 38 (1985) (zeros of Selberg zeta / resonances off the line).
- **Lane (c):** Dyson (1962), Gaudin (1961), Mehta (1960, 1991 book *Random Matrices*) — the eponymous gap/moment laws. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos. Pure Math. 24 (1973) 181–193 (already held in the program). Odlyzko, *On the distribution of spacings between zeros of the zeta function*, Math. Comp. 48 (1987) 273–308 (the 10²⁰-th zero numerics — the classic finite-T GUE evidence). Valkó–Virág, *Continuum limits of random matrices and the Brownian carousel*, Invent. Math. 177 (2009) (Sine_β).

---

## 9. Honesty footer

- **Verification standard:** every paper in §1–§5 was fetched from the arXiv export API in this session and its abstract read from the API response (VERIFIED-BY-FETCH). PDFs byte-verified as `%PDF`. No paper in this note rests on a recalled arXiv ID; the 48 cached API responses are in `research/notes/paper-finder-spectral/xml/` and can be re-parsed by any future agent.
- **What was searched and failed:** the exact phrases "graph zeta moments", "Ihara zeta zeros", "Selberg zeta statistics/value distribution/GUE" return **zero** arXiv results (documented §7). The hunt therefore used adjacent phrasings; the note states clearly where the relevant content actually is. No network blocker was hit — export.arxiv.org was reachable throughout (only polite 429-backoff sleeps; a concurrent sibling agent shares the API).
- **Labels:** all entries VERIFIED-BY-FETCH; PDFs downloaded and byte-checked = additionally "(PDF held)". Classics in §8 are NOT verified (flagged, with journal locations) — treat their bibliographic data as unconfirmed. No claim here is a mathematical claim; this is a literature inventory.
- **Overlap warning (orchestrator):** a concurrent paper-finder agent owns `/tmp/paperfinder/` and is fetching moments/triple-correlation targets plus Rudnick/Sarnak PDFs via web.archive.org. If a second `paper-finder-spectral.md` appears, adjudicate by provenance: this note's entries are all backed by the cached API XML in `research/notes/paper-finder-spectral/xml/`.
- **Next-step suggestion for the probes:** (i) lane (a): read Huang 1905.13485 against the sandbox's coincident-angle collapse (its h_k positivity is per distinct spectrum — check the multiplicity caveat); (ii) lane (b): read Rudnick 2202.06379 + Maoz 2310.18663 for the GOE prediction on compact hyperbolic surfaces — the V7 "harder case" reference statistics; (iii) lane (c): read Lagarias–Rodgers 1907.03391 for the bandwidth-one mimicry bounds (ties directly to the 0.6818 ceiling's hypothesis set) and Bogomolny et al. math/0602270 + Nishigaki 2507.10193 for the finite-T correction exponents the hot-hand probe can measure.
