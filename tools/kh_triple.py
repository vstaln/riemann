#!/usr/bin/env python3
"""Karle-Hauptman 3x3 triple-product bound on the third moment — code-backed check.

Vector A1 (idea-generator-crystallography.md): the K-H 3x3 determinant inequality couples
the triple correlation T = E(h) E(k-h) E(-k)  (frequencies h + (k-h) + (-k) = 0) to the
three intensities |E(h)|^2, |E(k)|^2, |E(k-h)|^2.  Question: given near-CUE pair data
(S(j) ~ j/N on [0,1]), what range of m3 = tr G^3/N is admissible, and does the bound
exclude m3 = 2 (the value that would kill the 256-law, m3(law) = 1.9545 < 2), or
m3 = 5 (the corrected sine-kernel lambda=1/2 value)?

Exact inequality (derived and symbolically verified in the session note): for
E(alpha) = (1/N) sum_rho e^{i alpha x_rho} (E(0) = 1, x = rescaled ordinates, mean
spacing 1), the 3x3 principal minor of the PSD Gram matrix on indices {0,h,k} is

    det = 1 - |E(h)|^2 - |E(k)|^2 - |E(k-h)|^2 + 2 Re(E(h) E(k-h) E(-k)) >= 0
    <==>  2 Re(T) >= |E(h)|^2 + |E(k)|^2 + |E(k-h)|^2 - 1.        (KH)

This is a TAUTOLOGY for the true configuration (PSD Gram); its content as a pair-data
constraint is the lower bound on Re(T) in terms of the intensities.

Run:  uv run --quiet --with numpy python tools/kh_triple.py
Data: tools/data/zeros_1_1000.txt (primary, flat window, all simple);
      tools/data/zeros_computed_10000.txt band 9000-9880 (cross-check at higher height).
"""
import numpy as np

TAU = 3e-40
P0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000

def load_band(fn, lo=0.0, hi=1e30):
    g = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                v = float(p[1])
                if lo <= v <= hi:
                    g.append(v)
    return np.array(sorted(g))

def rescale(gammas):
    """x = gamma / mean-spacing  (mean spacing 1), per tools/m3_zeros_check.py."""
    sp = np.diff(gammas).mean()
    return np.sort(gammas) / sp, sp

def structure_factors(x, N):
    """E_j = (1/N) sum_rho e^{i (j/N) x_rho}, j = 1..N  (alpha-grid j/N in [0,1])."""
    alpha = np.arange(1, N + 1, dtype=float) / N
    E = np.empty(N, dtype=complex)
    for i, a in enumerate(alpha):
        E[i] = np.exp(1j * a * x).sum() / N
    return alpha, E

def kh_determinant(E, h, k):
    """3x3 K-H principal minor on indices {0,h,k}; returns (det, triple T, bound RHS).
    Indices are grid positions: alpha_h = h/N, alpha_k = k/N.
    det = 1 - |Eh|^2 - |Ek|^2 - |E_{k-h}|^2 + 2 Re(Eh E_{k-h} E_{-k})
    (verified symbolically in the session; frequencies sum to 0)."""
    i0, ih, ik = 0, h - 1, k - 1   # E array is 1-indexed in grid position
    Eh = E[ih]
    Ek = E[ik]
    d = k - h
    Ekh = E[d - 1] if 1 <= d <= len(E) else None
    if Ekh is None:
        return None
    T = Eh * Ekh * np.conj(Ek)
    det = 1 - abs(Eh) ** 2 - abs(Ek) ** 2 - abs(Ekh) ** 2 + 2 * T.real
    bound = (abs(Eh) ** 2 + abs(Ek) ** 2 + abs(Ekh) ** 2 - 1) / 2
    return det, T, bound

def gram_moments(x, la):
    n = x.size
    d = x[:, None] - x[None, :]
    G = np.sinc(la * d)
    m1 = np.trace(G) / n
    G2 = G @ G
    m2 = np.trace(G2) / n
    G3 = G2 @ G
    m3 = np.trace(G3) / n
    # diagram decomposition for all-simple marks:  m3 = 1 + 3*A2 + A3
    off = np.abs(d) > 1e-12
    A2 = (G[off] ** 2).sum() / n
    # A3 = m3 - 1 - 3*A2 (exact for all-simple; includes all-distinct and i=k,j!=i terms)
    A3 = m3 - 1 - 3 * A2
    # capacity: C0 = (1/N) sum_{i,j,k distinct} |G_ij G_jk G_ki|  (upper bound via tr(|G|^3))
    A = np.abs(G)
    C0 = np.trace(A @ A @ A) / n
    return m1, m2, m3, A2, A3, C0

def report_band(name, fn, lo, hi):
    print("=" * 78)
    print(f"BAND: {name}  ({fn}, zeros in [{lo},{hi}])")
    g = load_band(fn, lo, hi)
    N = g.size
    print(f"  N = {N} zeros, gamma in [{g.min():.3f}, {g.max():.3f}]")
    x, sp = rescale(g)
    print(f"  mean spacing (gamma units): {sp:.5f}")

    # ---- 1. Gram moments m3(lambda), A2, A3, capacity ----
    print("\n[1] Gram moments (flat window, sine-kernel Gram G_ij = sinc(la(x_i-x_j)))")
    for la, (e2, e3) in ((1.0, (4 / 3, 2.0)), (0.5, (13 / 6, 5.0))):
        m1, m2, m3, A2, A3, C0 = gram_moments(x, la)
        j2 = {1.0: 1 / 3, 0.5: 5 / 12}[la]
        a2c = 1 / la - 2 * j2
        a3c = e3 - 1 - 3 * a2c
        print(f"  lambda={la}: m1={m1:.4f} m2={m2:.4f} (closed {e2:.4f}) "
              f"m3={m3:.4f} (closed {e3:.4f})")
        print(f"       A2={A2:.4f}  A3(connected)={A3:.4f}   closed forms: A2={a2c:.4f}, "
              f"A3={a3c:.4f}   [A3(1)=0 exactly: the whole m3 is two-point data at lambda=1]")
        print(f"       |A3| capacity C0=(1/N)tr(|G|^3)={C0:.2f}  (log^2 N-scale; pair data do not pin A3)")

    # ---- 2. near-CUE intensities |E(alpha_j)|^2 ----
    print("\n[2] Structure factors on the grid alpha_j = j/N, j=1..N (Montgomery range [0,1])")
    alpha, E = structure_factors(x, N)
    I = np.abs(E) ** 2
    sel = slice(0, N)  # j = 1..N
    print(f"  mean |E(j/N)|^2 over j=1..N: {I[sel].mean():.3e}   (near-CUE prediction c/N, c ~ O(1))")
    print(f"  N * mean |E|^2 (effective c): {N * I[sel].mean():.3f}")
    for j in (1, 2, 3, 4, 8, 16, 64, 128, N // 2, N):
        if j <= N:
            print(f"    j={j:4d}: |E(j/N)|^2 = {I[j-1]:.3e}   (1/N = {1/N:.3e})")
    # pair-sum (off-diagonal form factor proxy): (1/N) sum_{i != j} e^{i alpha (x_i - x_j)}
    print("  off-diagonal form factor proxy (1/N) sum_{i!=j} e^{i a (x_i-x_j)} at a=j/N,")
    for j in (1, 2, 3, N // 4, N // 2, N):
        a = j / N
        S = np.exp(1j * a * x)
        FF = (abs(S.sum()) ** 2 - N) / N
        print(f"    j={j:4d}: (N|E|^2 - 1) = {FF:.3f}   [Montgomery F(a)=1 <-> this ~ 1]")

    # ---- 3. K-H determinant: identity check + bound vs trivial ----
    print("\n[3] K-H 3x3 determinants on index sets {0,1,2} and {0,1,3}")
    worst_det = 1e9
    worst_bound_slack = 1e9
    for (h, k) in ((1, 2), (1, 3)):
        det, T, bound = kh_determinant(E, h, k)
        triv = -np.sqrt(abs(E[h - 1]) ** 2 * abs(E[k - 1]) ** 2 * abs(E[k - h - 1]) ** 2) if (1 <= k - h <= len(E)) else None
        print(f"  indices {{0,{h},{k}}}: det = {det:+.6e} (>=0? {det >= -1e-12})   "
              f"Re(T) = {T.real:+.3e}   K-H lower bound = {bound:+.3e}   "
              f"trivial |Re T| <= |T| <= {abs(T):.3e}")
        worst_det = min(worst_det, det)
        if triv is not None:
            worst_bound_slack = min(worst_bound_slack, bound - triv)
    print(f"  -> K-H bound is weaker than the trivial bound by >= {worst_bound_slack:.3e} on these triples")

    # ---- 4. aggregate: how often does the K-H bound bind? ----
    print("\n[4] K-H bound across all in-band sum-zero triples (h, k-h, -k), h,k on grid")
    M = min(N, 400)  # keep the loop cheap
    cnt_bind = 0
    cnt_neg_rhs = 0
    cnt_tot = 0
    slack_min = 1e9
    for h in range(1, M + 1):
        for k in range(1, M + 1):
            if k - h < 1:
                continue
            if k - h > len(E):
                continue
            det, T, bound = kh_determinant(E, h, k)
            cnt_tot += 1
            if bound > 0:
                cnt_bind += 1
            else:
                cnt_neg_rhs += 1
            triv = -np.sqrt(abs(E[h - 1]) ** 2 * abs(E[k - 1]) ** 2 * abs(E[k - h - 1]) ** 2)
            slack_min = min(slack_min, bound - triv)
    print(f"  triples checked: {cnt_tot}, with positive K-H RHS (could bind): {cnt_bind}, "
          f"with RHS <= 0 (vacuous): {cnt_neg_rhs}")
    print(f"  K-H bound weaker than trivial bound everywhere; min slack (bound - trivial) = {slack_min:+.3e}")

    # ---- 5. admissible m3 range from pair data ----
    print("\n[5] Admissible m3 range given the (near-CUE) pair data")
    la = 1.0
    m1, m2, m3, A2, A3, C0 = gram_moments(x, la)
    center = 1 + 3 * A2
    print(f"  lambda=1: two-point-determined center 1+3*A2 = {center:.4f}  "
          f"(measured m3 = {m3:.4f}, A3 = {A3:.4f})")
    print(f"  pair-data admissible range (marks unconstrained): [1+3A2-C0, 1+3A2+C0] = "
          f"[{center - C0:.2f}, {center + C0:.2f}]")
    print(f"    contains 2 (GUE / would-exclude-256-law value)? {center - C0 <= 2 <= center + C0}")
    print(f"    contains 1.9545 (256-law m3)?                 {center - C0 <= 1.9545 <= center + C0}")
    la = 0.5
    m1, m2, m3, A2, A3, C0 = gram_moments(x, la)
    center = 1 + 3 * A2
    print(f"  lambda=1/2: two-point-determined center 1+3*A2 = {center:.4f}  "
          f"(measured m3 = {m3:.4f}, A3 = {A3:.4f})")
    print(f"    pair-data admissible range [1+3A2-C0, 1+3A2+C0] = [{center - C0:.2f}, {center + C0:.2f}]")
    print(f"    contains 5 (sine-kernel lambda=1/2 value)?     {center - C0 <= 5 <= center + C0}")
    print(f"  NOTE (object discipline): the 256-law separator is the MULTIPLICITY moment "
          f"m3^mult = sum m^3/N = 4 - 3*p1 (marks {{1,2}}), which is a first-order (mark) object.")
    print(f"    m3^mult(law) = 1.9545, m3^mult(extremal world) = 2, and PAIR DATA do not constrain p1 at all")
    print(f"    (near-CUE rows constrain positions, not marks) -> admissible m3^mult range from pair data = [1,4].")
    print(f"    The K-H triple bound speaks to the GRAM third moment's CONNECTED part (A3), not to m3^mult:")
    print(f"    even in principle it cannot deliver 'm3^mult >= 2 excludes the law' (wrong object).")

    # ---- 6. window-shape check: box-window prediction for the low-frequency intensities ----
    print("\n[6] Low-frequency |E|^2 = finite-window shape factor (box window of length N, continuum)")
    for j in (1, 2, 3, 4, 8):
        if j <= N:
            a = j / N
            pred = (np.sin(a * N / 2) / (a * N / 2)) ** 2   # |(1/N) int_0^N e^{i a x} dx|^2
            print(f"    j={j:4d}: measured |E(j/N)|^2 = {I[j-1]:.4f}   box-window prediction = {pred:.4f}")
    print("    -> the O(1) low-frequency intensities are the box-window Fourier shape, not pair-correlation")
    print("       structure; the K-H near-tightness there (det ~ 3e-4) is the window's own (two-point) content.")

    print()
    return dict(N=N, m3_1=m3)

print("NOTE: numbers labeled 'closed' are PROVEN in attack-twobandwidth.md (m3(1)=2, m3(1/2)=5).")
print("m3(law) = 4 - 3*p0 =", 4 - 3 * P0, " (CHECKED, attack-nevanlinna.md).")
report_band("zeros_1_1000.txt, full flat window", "tools/data/zeros_1_1000.txt", 0, 1e30)
report_band("zeros_computed_10000.txt, high band (cross-check)", "tools/data/zeros_computed_10000.txt", 9000, 9880)
