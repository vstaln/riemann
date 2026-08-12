# Task: twobandwidth-transfer — is N_d ≥ 0.8071N (distinct, λ=2/3) a real theorem?

**Agent:** THEORIST (phone, proot Ubuntu). **Charter:** ~/riemann/hooks/agents.md (honesty + PONYTAIL — numbers first, no essays, never lazy about rigor).
**Mission:** resolve the highest-value lead in ideas-to-70.md (L1): the two-bandwidth note's computation gives a distinct-count bound **N_d ≥ 0.8071N at λ=2/3** (and 41/54 = 0.7593 at λ=1/2) with PROVEN unconditional third moments — gated on the CONJECTURED transfer of the paper's admissible-cubic Schur–Horn step to λ<1. The prior note scored this only against the conditional 5/6 wall and called it "negative" — it never asked whether 0.8071 itself is a headline theorem. That's your job.

**Read, in this order (STOP after):**
1. research/notes/attack-twobandwidth.md — the full P6.5 note (already read the key parts: m₃(λ) closed form, the table m₃(1/2)=5, m₃(2/3)=13/4, m₃(1)=2; §3.2 the admissible-cubic bound N_d ≥ (1/2 + (2m₂−m₃)/18)N + (4/9)s₁; §3.3 why cross-window mixing fails; §5.2 the transfer is OPEN).
2. research/notes/attack-multiplicity.md — the c=3 distinct functional, 5/6 sharpness, extremal world (2N/3 simple + N/6 double).
3. The paper source (research/paper/…/claude-riemann-paper.txt or wherever §7.5(f,g) lives — grep for "admissible cubic" / "Schur" / "7.5(g)" / "Λ₁").

**The three questions (method, not brute force; numerics = verification):**
1. **SEMANTICS:** exactly what does N_d count — distinct zeros ON the critical line (each multiplicity-≤2 point once)? Simple+double-on-line only? Does it include off-line pair contributions? State the precise meaning and how N_d relates to the simple fraction s₁ and the on-line total (write the bookkeeping identities: N = s₁ + 2a₂ + off-line-multiplicity, N_d = s₁ + a₂,on-line + …).
2. **THE TRANSFER:** the paper proves the admissible-cubic Schur–Horn step at λ=1 (§7.5(g)). Does it transfer to λ=2/3? The mechanism: ψ(m) = am + bm² + cm³ + d·1_{m=1} ≤ 1 with admissibility = concavity of βx²+γx³ over the eigenvalue range of H = M^{1/2}ΓM^{1/2}; the moments trÂ^k are window-dependent but PROVEN at λ=2/3 (m₂ = 31/18, m₃ = 13/4). Determine: (a) is the weight admissibility a property that survives λ<1 (it's a function on the integer marks m∈{1,2} + the eigenvalue range — check whether the eigenvalue range of the λ=2/3 Gram matrix changes the admissibility), (b) does the Schur–Horn majorization argument depend on the window, (c) VERDICT: transfer holds / fails / needs X. If the transfer is genuinely the paper's theorem at λ=1 and the λ=2/3 window only changes the MOMENTS (not the spectral structure), argue carefully whether that's enough.
3. **THE MAP:** if N_d ≥ 0.8071N (distinct, on-line) is a theorem, what does it give for (i) the on-line total, (ii) the simple-on-line fraction s₁ (the user's 70% goal)? Can the moment bookkeeping N = s₁ + 2a₂ + … + N_d ≥ 0.8071N + s₁ ≥ 2/3 force a better s₁? Be honest if the answer is "distinct ≠ simple; no direct s₁ gain".

**One cheap numeric check (< 10 min):** re-derive the bound arithmetic at λ=2/3 and λ=1/2 (mpmath, trivial: (1/2 + (2m₂−m₃)/18) + (4/9)(2/3) with m₂(2/3)=31/18, m₃(2/3)=13/4, m₂(1/2)=13/6, m₃(1/2)=5) — confirm 0.8071 and 0.7593. Then, if feasible, one LP/admissibility check on the phone (scipy.optimize.linprog — check scipy exists first; else pure algebra).

**HARD CAPS:** write research/waves/wave-phone-2/results/twobandwidth-transfer.md by your 12th tool use; finish by 18th; < 150K tokens. Crash-proof: append after every step. Do NOT launch subagents.

**Deliverable:** ~/riemann/research/waves/wave-phone-2/results/twobandwidth-transfer.md — semantics, transfer verdict, N_d → s₁ map, honest labels.
**Report (< 100 words):** the N_d semantics, the transfer verdict, what the theorem would be. End: RESULT: <status> — <one line>.
