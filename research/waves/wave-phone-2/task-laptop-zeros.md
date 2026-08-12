# TASK: Laptop worker — verify nontrivial zeros of ζ(s) and build a zero corpus

## Mission (brain directive: the laptop finds zeros, the phone proves)
Numerically verify the first N nontrivial zeros of the Riemann zeta function lie on the
critical line Re(s) = 1/2, search for any OFF-LINE zero below height T, and produce a
high-precision zero corpus file for the phone's correlation proofs (S₃, pair correlation).
Goal N = 10⁵ zeros; guaranteed floor N = 10⁴ (do the floor first, scale if the tool is fast).

## Environment (laptop worker, user vstaln)
- Repo: /home/vstaln/riemann. Tools in /home/vstaln/riemann/tools/.
- Rust available (musl+rust-lld per hooks/agents.md). The eps-interval-verifier used Arb —
  LOCATE its source first (grep the repo and /tmp for the verifier that certified eps=0.00806;
  it may be in tools/ or /tmp/) and reuse its Arb/Cargo setup if practical.
- Python: `uv run --with python-flint` (fast Arb-backed), or `uv run --with mpmath`.
- No internet guarantee on the box — prefer installed/uv-cached deps.

## The work (all numbers CHECKED NUMERICALLY, tool + command cited)
1. **Method (pick the smallest that verifies):** standard practice —
   (a) locate zeros via sign changes of the real Hardy function Z(t) on the critical line
       (Riemann–Siegel via acb_zeta/flint, or the count N(T) = (T/2π)log(T/2π) − T/2π + 7/8
       with a rigorous error bound to bound the search), or
   (b) Turing's Gram-block method for a rigorous "all zeros up to height T are on the line"
       statement (report Gram points and any Gram-law violations — expected ~1 in 4 blocks),
   (c) refine each found zero to ≥12 significant digits (Newton on Z(t) or acb root).
   Verify the count: #zeros found in [0,T] must equal round(N(T)) with the error term handled.
2. **Off-line zero search:** within the searched range, any zero with |Re(s) − 1/2| > 0 would
   be a counterexample to RH — state explicitly: none found below T (or report one!).
3. **Corpus output:** write `research/notes/zeros-corpus/zeros_N.txt` — one γ per line,
   N ≤ γ_N values, ≥12 digits. Write INCREMENTALLY (append every 10⁴ zeros) so a crash keeps
   the partial corpus.
4. **Report:** `research/waves/wave-phone-2/results/laptop-zeros.md` —
   N, height T_N, method + error bounds, Gram stats, off-line-zero verdict, tool+commands,
   runtime. Labels: every claim PROVEN/CHECKED NUMERICALLY with the script+command.

## Deliverables
1. `research/notes/zeros-corpus/zeros_N.txt` (the corpus — the phone's S₃ empirics read this)
2. `research/waves/wave-phone-2/results/laptop-zeros.md` (verification statement)

## Ponytail (hooks/agents.md §PONYTAIL)
Smallest verifier that decides. Reuse the eps-verifier's Arb setup; reuse existing count/check
tools in tools/xiprime_check/ if they fit. Do NOT build a framework — a single-file verifier.
Crash-proof: nohup long runs, append corpus incrementally, keep each tool call < 90 s or poll.
