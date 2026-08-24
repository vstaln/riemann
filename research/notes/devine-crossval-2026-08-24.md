# Cross-validation hunt: Circumjovial/Devine clean-room tooling

Date: 2026-08-24
Agent: adventurer (recon, read-only)
Status: **NOT_FOUND** — script is not on this machine.

## What was searched

1. `find /home /tmp -name "*vstalin*"` (full, incl. dotfiles) — all hits are CVs,
   the `/home/vstaln/vstalin` portfolio, images, and unrelated job-search artifacts.
   **No** `experiments/vstalin_claim_arb_witness.py` or anything like it.
2. `find /home /tmp -iname "*arb_witness*" -o -iname "*claim_arb*"` — zero hits.
3. `grep -rl "vstalin_claim|claim_arb|arb_witness"` across `/home/vstaln/riemann`,
   `/home/vstaln/agents`, `/tmp` — zero hits (excl. `.git`).
4. Clone dirs: `/home/vstaln/riemann/experiments` does **not exist**. The actual
   external clones live at `research/external-results/`:
   `ainta-zeta-simple-zeros`, `anthropic-zeta23`, `openai-ten-proofs`,
   `tawanerguo-zeta-simple-zeros`, `trmdy-zeta-simple-zeros-673137`.
   **No JoshuaHKU clone present.** Tawan clone contains `tools/*.py`
   (compute_joint_bound, evaluate_coboundary_bound, generate_joint_kernel_table,
   generate_coboundary_derivative_table, etc.) — the "Tawan verifier" pinned source
   presumably refers to one of these, but that is the *claimed* verifier, not the
   auditor's clean-room witness.
5. `grep -ri "circumjovial|devine|pinned|clean-room"` in `research/` — hits are prose
   in the README/verifier docs of the GitHub clones (word "devine"), **not** the auditor.
6. Existing notes: `dispute-vstalin-code-2026-08-24.md` and
   `dispute-vstalin-tawan-2026-08-24.md` document the *code-side* dispute
   (IMPLEMENTED = F_V, audit is right about the code) but contain no copy of the
   auditor's clean-room script or pinned commit hashes.

## Implication

Without the auditor's script we cannot run an *independent adversarial* validation of
the corrected pipeline (F_T, span1_mode=replaced, alpha=1.4263026187858052,
lam=1.351623997475116, raw_p/raw_q arrays). Any validation we run self-hosted is
only **internal** cross-checking (INCONCLUSIVE as independence); the entire point of
the clean-room witness is that a third party re-derives the bound from the posted
claim without touching our code. That independence gap is only closed by obtaining
the script or its pinned commit hashes.

## Public ask draft (2 sentences, neutral)

> @CircumjovialLLC — we've corrected the pipeline per your audit (F_T, span-one pairs
> replaced by q terms; candidate α=1.4263026187858052, λ=1.351623997475116). Could
> you share the clean-room script `experiments/vstalin_claim_arb_witness.py` and the
> pinned commit hashes of the claim and the two verifiers you cite, so we can run your
> witness against our corrected inputs and cross-certify?

## What would make this an independent validation (if we get the script)

- Verify: which functional (F_T/F_V/F_B), which params (alpha/lam/raw_p/raw_q via
  env or args), which arithmetic backend (float64 / mpmath / interval / rational).
- Run it with our corrected inputs; agreement with our own corrected bound on the
  same point = INDEPENDENT corroboration (different implementation path).
- Compare pinned claim-commit hash vs our corrected commit; mismatch means we must
  re-run on the pinned claim commit. CONJECTURED until script in hand.