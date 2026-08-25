# TASK: Attack the certified record — adversarial verification + eps-max push

## Mission
The certified world record lower bound on the proportion of simple zeros on the critical line:
**0.673262865534356014645368000853343519319712248** [RETIRED 2026-08-24]
config: (α = 1.49, psum = 1/220, m = 133, eps = 0.00806). Your job:
1. Independently re-verify the headline claim.
2. Find any CERTIFIED config that beats it (the max-certified-eps question).
3. Report an honest verdict: survives / beaten / broken.

## Context — read first, do NOT re-derive
- `research/notes/discovery-6732629.md` — the record and its boundary behavior
- `research/notes/attack-pricing-sheet.md` §5–6 — the mechanism (H, τ, B, bound = (H−τ)/(1−B/m))
- `research/waves/wave-local/results/exec-two-tone.md` — **two-tone window REFUTED** (c=0 optimal; H capped at 3/2−(1/√2)cot(1/√2)=0.6725007). The lever is (eps, psum, m), NOT the window.
- `research/waves/wave-local/results/exec-eps-max-runs.log` — prior verifier runs: p=1/1320 (psum=1/220): max certified eps ≈ 0.008064; p=1/1350 (psum=1/225): max ≈ 0.007916. Failures cluster at specific terminal boxes.
- `research/notes/attack-ceiling.md` — the ceiling context (0.6818 is a proven wall for this class).

## Environment
- Phone: NO Rust. The interval verifier is Rust and lives on the LAPTOP. Run it there via:
  `proot-distro login ubuntu -- bash -lc 'ssh -o ConnectTimeout=20 pc-jump "su vstaln -c \"...\""'`
  (laptop tools under /home/vstaln/riemann/tools/, e.g. tools/bound-sweep/, plus /tmp/combine/final_leader.py, verify_H.py)
- Phone Python for anything light: `proot-distro login ubuntu -- python3` (mpmath 1.4.1, numpy 2.3.5 available).

## The work (CHECKED NUMERICALLY, script + command cited)
1. **Re-verify the headline**: find and re-run the certified machinery on the laptop (final_leader.py / verify_H.py / tools/bound-sweep). Confirm bound = 0.673262865534356… exactly, and that eps=0.00806 certifies while 0.008065 fails (re-run that boundary yourself). [RETIRED 2026-08-24]
2. **Attack the eps floor** (THE key question — bound is monotone increasing in eps): is the 0.008065 failure a genuine analytic floor or an artifact of the verifier's box-splitting? Try to certify eps = 0.00807, 0.0081 at (α=1.49, psum=1/220, m=133) with a different box strategy or interval split. Record the failing box and what it bounds.
3. **Certified bound sweep**: psum ∈ {1/220, 1/225, 1/240}, m ∈ {130,…,140}, α ∈ {1.45,…,1.53} — using CERTIFIED eps values only (conjectured eps does not count). Max certified bound? Anything > 0.6732628655? [RETIRED 2026-08-24]
4. **Adversarial formula check**: re-derive τ and B for m=133; is there ANY (eps ≤ certified max) where the bound formula fails to reproduce 0.6732628655? [RETIRED 2026-08-24]

## Deliverable
`research/waves/wave-phone-2/results/attack-record.md` — verdict, max certified eps, max certified bound, all numbers with scripts+commands. Labels: PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE.

## Ponytail (hooks/agents.md §PONYTAIL)
Smallest probe that decides. Reuse the laptop verifier via pc-jump — do NOT reimplement the interval verifier in Python unless the laptop is unreachable (then reimplement ONLY the eps=0.00806 certification in mpmath interval arithmetic, single config, `# ponytail: N boxes small`).
