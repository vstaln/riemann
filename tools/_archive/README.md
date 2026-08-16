# Archived tools — recoverable, never deleted

Moved here 2026-08-18 during the wave-13 Python→Rust cleanup. These tools are
**dead code**: retracted, refuted, zero-reference, or single-use with results
already preserved in notes. Move back to `tools/` if a future lever needs them.

| Path (original) | Why archived | Result preserved in |
|---|---|---|
| `beat673/` | `verify_cos7.py` has the **kernel double-normalization bug** — the 0.6732629 record it certified was RETRACTED | `research/notes/retraction-673-invalid.md` |
| `twotone-verify/verify_twotone7.py` | Twotone lever **REFUTED** (window class closed at H=0.6725007); 0 live references | `research/notes/twotone-refuted.md` |
| `pt_symmetric_metric_solver.py` | 0 references in notes; only an old `pt_metric_lyapunov_results.json` exists | (results json in notes dir) |
| `adversarial_riemann_solver.py` | 0 references anywhere; never produced a landed result | — |
| `fourth_moment_rmt.py` | Single-use; its analysis is PROVEN and fully written up | `research/notes/fourth_moment_analysis.md` |
| `ramanujan_kernel_search.py` | Single-use probe; conjectures written up, no live consumer | `research/notes/ramanujan_conjectures.md` |

## Rule for archiving (going forward)
- **Never delete** — always move here with a manifest row (original path + reason + where the result lives).
- Only archive tools that are: (a) retracted/buggy, (b) refuted/closed levers with verdicts recorded,
  (c) zero-reference single-use probes whose results are in notes.
- Live certifiers (interval verifier, hiN.rs, wave8c/d pipelines) are NEVER archived.
