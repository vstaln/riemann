// Verification checks: constant, bracket, explicit formula, pair correlation,
// rank-trace brute force, Montgomery-Vaughan sanity.

use std::fs;
use std::path::PathBuf;

use crate::zeta;

const TWO_PI: f64 = 6.283185307179586;

fn psi(t: f64) -> f64 {
    (std::f64::consts::SQRT_2 * t).cos() * if t.abs() <= 0.5 { 1.0 } else { 0.0 }
}

/// 1) constant check + the variational identity (closed forms + quadrature).
pub fn constant() {
    println!("== constant ==");
    // 3/2 - (1/sqrt2) cot(1/sqrt2)
    let c = 1.5 - (1.0 / std::f64::consts::SQRT_2) * (1.0 / std::f64::consts::SQRT_2).tan().recip();
    println!("3/2 - (1/sqrt2)cot(1/sqrt2) = {:.17}  (expected 0.67250070367941165)", c);
    // 2 - 1/c1*, c1* = sqrt2 tan(th)/(1+th tan th), th = 1/sqrt2
    let th = 1.0 / std::f64::consts::SQRT_2;
    let c1 = std::f64::consts::SQRT_2 * th.tan() / (1.0 + th * th.tan());
    println!("2 - 1/c1*                    = {:.17}", 2.0 - 1.0 / c1);
    // variational identity: ∫ψ² + ∬|u-v|ψ(u)ψ(v) = (1/2 + (1/√2)cot(1/√2))·(∫ψ)²
    // closed forms: ∫ψ = √2 sin(1/√2); ∫ψ² = 1/2 + (√2/4)sin(√2)... derive numerically:
    // ∫_{-1/2}^{1/2} cos²(√2 u) du = 1/2 + sin(√2)/(2√2)
    let int_psi = std::f64::consts::SQRT_2 * (1.0 / std::f64::consts::SQRT_2).sin();
    let int_psi2 = 0.5 + (std::f64::consts::SQRT_2).sin() / (2.0 * std::f64::consts::SQRT_2);
    // double integral: ∬|u-v|ψ(u)ψ(v) du dv = 2∫_0^1 w (ψ∗ψ)(w) dw; compute by quadrature
    let n = 4001;
    let h = 1.0 / (n as f64);
    let mut dbl = 0.0;
    for i in 0..n {
        let u = (i as f64 + 0.5) * h - 0.5;
        for j in 0..n {
            let v = (j as f64 + 0.5) * h - 0.5;
            dbl += (u - v).abs() * psi(u) * psi(v) * h * h;
        }
    }
    let lhs = int_psi2 + dbl;
    let rhs = (0.5 + (1.0 / std::f64::consts::SQRT_2) * (1.0 / std::f64::consts::SQRT_2).tan().recip()) * int_psi * int_psi;
    println!("variational identity: lhs={:.12} rhs={:.12}  diff={:.3e} (CHECKED NUMERICALLY)",
             lhs, rhs, (lhs - rhs).abs());
    // Rayleigh quotient of ψ itself
    println!("quotient (∫ψ²+∬|u-v|ψψ)/(∫ψ)² = {:.12}  expected 1/2+(1/√2)cot(1/√2)={:.12}",
             lhs / (int_psi * int_psi), 0.5 + (1.0 / std::f64::consts::SQRT_2) * (1.0 / std::f64::consts::SQRT_2).tan().recip());
}

/// 2) verify cached LMFDB zeros are bracketed sign changes of Z(t).
pub fn bracket(data_dir: &PathBuf, n: usize) {
    println!("== bracket: first {} LMFDB zeros ==", n);
    let path = data_dir.join("zeros_1_1000.txt");
    let txt = fs::read_to_string(&path).expect("zeros_1_1000.txt");
    let gs: Vec<f64> = txt
        .lines()
        .filter_map(|l| {
            let mut it = l.split_whitespace();
            it.next()?;
            it.next()?.parse().ok()
        })
        .collect();
    let nn = gs.len().min(n);
    let mut fails = 0;
    for i in 0..nn.saturating_sub(2) {
        // Z should have the same sign throughout (γ_i, γ_{i+1}) and alternate across i.
        // Check: Z at midpoint of gap i and midpoint of gap i+1 have opposite signs.
        let m = 0.5 * (gs[i] + gs[i + 1]);
        let zm = zeta::zeta_z(m);
        let m2 = 0.5 * (gs[i + 1] + gs[i + 2]);
        let zm2 = zeta::zeta_z(m2);
        if zm * zm2 > 0.0 || zm.abs() < 1e-6 || zm2.abs() < 1e-6 {
            fails += 1;
            if fails <= 3 {
                println!("  ? sign anomaly around zero {} (Z(m)={:.3e} Z(m2)={:.3e})", i + 1, zm, zm2);
            }
        }
    }
    // also: |Z(γ_i)| should be tiny compared to typical |Z|
    let mut max_atzero = 0.0f64;
    for i in 0..nn.min(500) {
        let z = zeta::zeta_z(gs[i]);
        max_atzero = max_atzero.max(z.abs());
    }
    println!("zeros checked: {} | sign-alternation anomalies: {} | max |Z(gamma_i)| (i<=500): {:.2e}",
             nn - 1, fails, max_atzero);
    if fails == 0 && max_atzero < 1e-4 {
        println!("VERDICT: PASS — LMFDB ordinates are bracketed sign changes of Z(t) (CHECKED NUMERICALLY, f64)");
    } else {
        println!("VERDICT: REVIEW NEEDED");
    }
}

/// 3) Guinand-Weil explicit formula — the paper's spectral form (Lean H-EF):
/// W(f,f) = Σ_ρ m_ρ |h_f(γ_ρ)|² = ∫_R |h_f(τ)|² · ν_X(τ) dτ,   ν_X = μ + Π_X + P_X,
/// with paperFT h_f(τ) = ∫ f(u) e^{iτu} du (no 2π), supp f ⊆ [−L/2, L/2], X = e^L,
/// μ(τ) = (1/2π)Re ψ(1/4+iτ/2) − lnπ/2π,
/// Π_X(τ) = 1/(2π(1/4+τ²)) + (1/π)Re((X^s − 1)/s), s = 1/2+iτ,
/// P_X(τ) = −(1/π) Σ_{n≤X} Λ(n)/√n cos(τ ln n).
/// L = 12 (X = e^12 ≈ 162755, sieveable); f = C∞ even bump on [−6,6].
pub fn explicit_formula() {
    println!("== Guinand-Weil (paper spectral form; family of bump widths) ==");
    let gs = read_zeros_1000();
    // --- RHS terms (closures shared across widths) ---
    // μ via digamma (recurrence lift + asymptotic)
    let psi = |zr: f64, zi: f64| -> f64 {
        // ψ(z) for Re z = 0.25: lift by M, asymptotic at z+M
        let m = 40.0;
        let (wr, wi) = (zr + m, zi);
        let mag2 = wr * wr + wi * wi;
        // ψ(w) ≈ ln w − 1/(2w) − Σ_{k=1..6} B_{2k}/(2k w^{2k})
        let lnw = 0.5 * mag2.ln();
        let mut v = lnw - 0.5 * wr / mag2;
        for k in 1..=6 {
            let b = crate::zeta::bernoulli(2 * k);
            // Re(B_{2k}/(2k) w^{-2k}): w^{-2k} = conj(w)^{2k}/|w|^{4k}
            let (a, b2) = (wr, wi); // conj(w) = (wr, -wi) -> (a,-b2); (a - i b2)^{2k}
            let mag4 = mag2.powi(2 * k as i32);
            // compute Re((a - i b2)^{2k}) via binomial/trig: (r e^{-iφ})^{2k} = r^{2k} e^{-i2kφ}
            let r = mag2.sqrt();
            let phi = wi.atan2(wr);
            let re = r.powi(2 * k as i32) * (2.0 * k as f64 * phi).cos();
            v -= b / (2.0 * k as f64) * re / mag4;
        }
        // subtract Σ_{j=0}^{M-1} 1/(z+j)
        for j in 0..40 {
            let (jr, ji) = (zr + j as f64, zi);
            let d = jr * jr + ji * ji;
            v -= jr / d;
        }
        v
    };
    let mu = |tau: f64| (psi(0.25, tau / 2.0)) / TWO_PI - std::f64::consts::PI.ln() / TWO_PI;
    // --- loop over test-function widths: wide -> prime side, narrow -> zero side ---
    println!(" width a |  LHS (zeros) |     RHS     |  μ-part  |  Π-part  |  P-part  |  |Δ|/scale");
    use std::io::Write;
    let mut all_ok = true;
    for &a in &[6.0, 1.0, 0.3, 0.15] {
        print!("[a={}] computing h_f / LHS ... ", a);
        std::io::stdout().flush().unwrap();
        let l: f64 = 2.0 * a + 0.1;
        let x: f64 = l.exp();
        let half = a;
        let f = |u: f64| {
            if u.abs() < half {
                let t = u / half;
                (1.0 - 1.0 / (1.0 - t * t)).exp()
            } else {
                0.0
            }
        };
        let hf = |tau: f64| {
            let cycles = (tau.abs() * half / std::f64::consts::PI).ceil() as usize;
            let n = (24 * cycles).max(64);
            let h = (2.0 * half) / (n as f64);
            let mut s = 0.0;
            for i in 0..=n {
                let u = -half + i as f64 * h;
                let w = if i == 0 || i == n { 1.0 } else if i % 2 == 0 { 2.0 } else { 4.0 };
                s += w * f(u) * (tau * u).cos();
            }
            s * h / 3.0
        };
        // integration range/step: wide bumps decay super-exponentially (H=30..60 plenty);
        // narrow bumps have a slow 1/τ² tail (need H=200). step 0.002 suffices everywhere.
        let h = if a < 0.5 { 200.0 } else if a < 1.5 { 60.0 } else { 30.0 };
        let step = if a < 0.5 { 0.001 } else { 0.002 };
        let n = (2.0 * h / step) as usize;
        // LHS: 2 Σ_{γ>0} h_f(γ)² (h_f even -> negative-ordinate zeros double the sum)
        let mut lhs = 0.0;
        let (mut l100, mut l300, mut l600) = (0.0, 0.0, 0.0);
        for (i, &g) in gs.iter().enumerate() {
            let v = hf(g);
            lhs += v * v;
            if i < 100 {
                l100 += v * v;
            }
            if i < 300 {
                l300 += v * v;
            }
            if i < 600 {
                l600 += v * v;
            }
        }
        lhs *= 2.0;
        l100 *= 2.0;
        l300 *= 2.0;
        l600 *= 2.0;
        if a < 0.5 {
            println!("LHS partial: 100 {:.6}  300 {:.6}  600 {:.6}  1000 {:.6}", l100, l300, l600, lhs);
        } else {
            println!("done (LHS {:.6})", lhs);
        }
        print!("[a={}] integrating RHS over ±{} ... ", a, h);
        std::io::stdout().flush().unwrap();
        // RHS pieces at this L
        let lnx = l;
        let pi_x = |tau: f64| {
            let s_re = 0.5;
            let s_im = tau;
            let xsr = x.sqrt() * (tau * lnx).cos();
            let xsi = x.sqrt() * (tau * lnx).sin();
            let num_re = xsr - 1.0;
            let num_im = xsi;
            let d2 = s_re * s_re + s_im * s_im;
            let re_div = (num_re * s_re + num_im * s_im) / d2;
            1.0 / (TWO_PI * (0.25 + tau * tau)) + re_div / std::f64::consts::PI
        };
        let nmax = x as usize;
        let lam = sieve_lambda(nmax);
        let p_x = |tau: f64| {
            let mut s = 0.0;
            for (n_, &l) in lam.iter().enumerate().skip(2) {
                if l > 0.0 {
                    s += l * (tau * (n_ as f64).ln()).cos() / (n_ as f64).sqrt();
                }
            }
            -s / std::f64::consts::PI
        };

        let step = 2.0 * h / (n as f64);
        let (mut rhs, mut rm, mut rp, mut rpp, mut tail) = (0.0, 0.0, 0.0, 0.0, 0.0);
        for i in 0..=n {
            let tau = -h + i as f64 * step;
            let w = if i == 0 || i == n { 1.0 } else if i % 2 == 0 { 2.0 } else { 4.0 };
            let hf2 = hf(tau) * hf(tau);
            let (m, p2, pp) = (mu(tau), pi_x(tau), p_x(tau));
            rhs += w * hf2 * (m + p2 + pp);
            rm += w * hf2 * m;
            rp += w * hf2 * p2;
            rpp += w * hf2 * pp;
            if tau.abs() > 100.0 {
                tail += w * hf2 * (m + p2 + pp).abs();
            }
        }
        rhs *= step / 3.0;
        rm *= step / 3.0;
        rp *= step / 3.0;
        rpp *= step / 3.0;
        tail *= step / 3.0;
        println!("done");
        let scale = rm.abs().max(rp.abs()).max(rpp.abs()).max(lhs.abs()).max(rhs.abs()).max(1.0);
        let rel = (lhs - rhs).abs() / scale;
        let ok = rel < 1e-5;
        all_ok &= ok;
        println!(" {:6.2} | {:11.6} | {:11.6} | {:8.4} | {:8.4} | {:8.4} | {:.2e} {}   (tail|τ|>100: {:.1e})",
                 a, lhs, rhs, rm, rp, rpp, rel, if ok { "PASS" } else { "REVIEW" }, tail);
    }
    println!("VERDICT: {}", if all_ok { "PASS — Guinand-Weil spectral identity holds (CHECKED NUMERICALLY)" } else { "REVIEW" });
}

/// 4) empirical Montgomery form factor F(α) ≈ |α| for 0<|α|<1.
/// Uses zeros γ_1..γ_N:  F(α) ≈ (2π/(N·L²)) Σ_{n≠m} e^{iα(γ_n−γ_m)L}·w(...) — we use the
/// standard "spacing density" histogram + its Fourier transform instead (simpler, robust).
pub fn paircorr(n: usize) {
    println!("== pair correlation: normalized spacing histogram vs 1-(sin πu/πu)² (N={}) ==", n);
    let gs = zeta::find_zeros(n);
    // normalized spacings δ_i = (γ_{i+1} − γ_i)·L/(2π), L = ln(γ_N/2π)
    let L = (gs[n - 1] / TWO_PI).ln();
    let mut deltas: Vec<f64> = Vec::with_capacity(n - 1);
    for i in 0..n - 1 {
        deltas.push((gs[i + 1] - gs[i]) * L / TWO_PI);
    }
    let mean = deltas.iter().sum::<f64>() / deltas.len() as f64;
    println!("mean normalized spacing: {:.6} (should be ~1)", mean);
    // histogram in bins [k*0.1, (k+1)*0.1), k=0..20
    let mut hist = [0usize; 20];
    for &d in &deltas {
        let k = (d / 0.1) as usize;
        if k < 20 {
            hist[k] += 1;
        }
    }
    let total = deltas.len() as f64;
    println!(" u     emp density  1-(sinπu/πu)²");
    for k in 0..16 {
        let u = (k as f64 + 0.5) * 0.1;
        let emp = hist[k] as f64 / (0.1 * total);
        let mont = 1.0 - (std::f64::consts::PI * u).sin().powi(2) / (std::f64::consts::PI * u).powi(2);
        println!(" {:4.1}   {:10.4}   {:10.4}", u, emp, mont);
    }
    // form factor F(α) = (1/N) Σ_{n≠m} sin²(πα(γ_n-γ_m)L/2π·...)... use the standard:
    // F(α) = (2π/(L·T)) Σ e^{iα...}: skip — histogram is the honest check here.
    println!("VERDICT: qualitative check (sample noise is large at N={}); label CHECKED NUMERICALLY (trend only)", n);
}

/// 5) Lemma 3.4 brute force: for random Hermitian A>=0, symmetric B:
///    rank A >= 2 tr A + 4 tr B - 4 n+(B) - ||A+B||_HS^2
pub fn ranktrace(trials: usize) {
    println!("== Lemma 3.4 brute force: {} trials ==", trials);
    let mut rng = XorShift::new(0x9E3779B97F4A7C15u64);
    let mut violations = 0;
    let mut worst = -1e300f64;
    let mut max_nplus = 0usize;
    for _ in 0..trials {
        let n = 2 + (rng.next() % 9) as usize; // 2..=10
        let r = 1 + (rng.next() % n as u64) as usize; // rank of A: 1..=n
        // A = L L^T, L: n x r
        let mut a = vec![vec![0.0; n]; n];
        for i in 0..n {
            for j in 0..n {
                let mut s = 0.0;
                for k in 0..r {
                    let li = rng.gauss();
                    let lj = rng.gauss();
                    // reuse same L column: to keep it simple sample L entries once
                    s += li * lj;
                }
                a[i][j] = s;
            }
        }
        // that's wrong (resampled); rebuild properly:
        let mut l = vec![vec![0.0; r]; n];
        for i in 0..n {
            for k in 0..r {
                l[i][k] = rng.gauss();
            }
        }
        for i in 0..n {
            for j in 0..n {
                let mut s = 0.0;
                for k in 0..r {
                    s += l[i][k] * l[j][k];
                }
                a[i][j] = s;
            }
        }
        // B symmetric
        let mut b = vec![vec![0.0; n]; n];
        for i in 0..n {
            for j in i..n {
                let v = rng.gauss();
                b[i][j] = v;
                b[j][i] = v;
            }
        }
        // eigenvalues of A and B via symmetric Jacobi
        let (ev_a, _) = jacobi(&a);
        let (ev_b, _) = jacobi(&b);
        let eps = 1e-9 * (ev_a.iter().map(|x| x.abs()).fold(0.0, f64::max).max(1.0));
        let rank = ev_a.iter().filter(|&&x| x > eps).count();
        let tr_a: f64 = ev_a.iter().sum();
        let tr_b: f64 = ev_b.iter().sum();
        let nplus = ev_b.iter().filter(|&&x| x > eps).count();
        max_nplus = max_nplus.max(nplus);
        let mut hs = 0.0;
        for i in 0..n {
            for j in 0..n {
                let x = a[i][j] + b[i][j];
                hs += x * x;
            }
        }
        let rhs = 2.0 * tr_a + 4.0 * tr_b - 4.0 * nplus as f64 - hs;
        let slack = rank as f64 - rhs;
        worst = worst.max(-slack);
        if slack < -1e-6 * (1.0 + rhs.abs()) {
            violations += 1;
            if violations <= 3 {
                println!("  VIOLATION: n={} r={} rank={} trA={:.3} trB={:.3} n+={} hs={:.3} rhs={:.3}",
                         n, r, rank, tr_a, tr_b, nplus, hs, rhs);
            }
        }
    }
    println!("trials={} violations={} worst deficit (rank-rhs)= {:.3e} (negative = violation)", trials, violations, worst);
    if violations == 0 {
        println!("VERDICT: PASS — Lemma 3.4 holds on all random instances (CHECKED NUMERICALLY)");
    } else {
        println!("VERDICT: FAIL — REAL BUG FOUND");
    }
}

/// 6) Montgomery-Vaughan sanity: |Σ_{m≠n} x_m conj(x_n)/(y_m - y_n)| <= π Σ|x_n|²/δ.
pub fn montgomery_vaughan() {
    println!("== Montgomery-Vaughan / Hilbert inequality sanity ==");
    let mut rng = XorShift::new(0x123456789ABCDEFu64);
    let mut worst_ratio = 0.0f64;
    for trial in 0..200 {
        let n = 50 + (rng.next() % 50) as usize;
        let mut x = Vec::with_capacity(n);
        for _ in 0..n {
            let re = rng.gauss();
            let im = rng.gauss();
            x.push((re, im));
        }
        let y: Vec<f64> = (0..n).map(|i| i as f64 + 0.25).collect(); // gaps = 1
        let mut s_re = 0.0;
        let mut s_im = 0.0;
        for m in 0..n {
            for l in 0..n {
                if m == l {
                    continue;
                }
                let dy = y[m] - y[l];
                let (xr, xi) = x[m];
                let (xr2, xi2) = x[l];
                // x_m · conj(x_l) / (y_m - y_l)
                let num_re = xr * xr2 + xi * xi2;
                let num_im = xi * xr2 - xr * xi2;
                s_re += num_re / dy;
                s_im += num_im / dy;
            }
        }
        let mag = (s_re * s_re + s_im * s_im).sqrt();
        let norm2: f64 = x.iter().map(|(r, i)| r * r + i * i).sum();
        let ratio = mag / (std::f64::consts::PI * norm2);
        worst_ratio = worst_ratio.max(ratio);
        if trial % 50 == 0 {
            println!("  trial {}: |S|/(πΣ|x|²) = {:.4}", trial, ratio);
        }
    }
    println!("worst |S|/(π Σ|x|²) over 200 trials = {:.4}  (should be <= 1 for unit gaps)",
             worst_ratio);
    println!("VERDICT: {}", if worst_ratio <= 1.001 { "PASS (CHECKED NUMERICALLY)" } else { "REVIEW — ratio exceeds 1" });
}

// ---------- helpers ----------

fn read_zeros_1000() -> Vec<f64> {
    let path = PathBuf::from(env_data_dir()).join("zeros_1_1000.txt");
    let txt = fs::read_to_string(&path).expect("read zeros_1_1000.txt (run the LMFDB fetch or check tools/data)");
    txt.lines()
        .filter_map(|l| {
            let mut it = l.split_whitespace();
            it.next()?;
            it.next()?.parse().ok()
        })
        .collect()
}

fn env_data_dir() -> String {
    std::env::var("ZETA_DATA").unwrap_or_else(|_| "../data".into())
}

fn sieve_lambda(nmax: usize) -> Vec<f64> {
    // Λ(n) for n <= nmax
    let mut lam = vec![0.0f64; nmax + 1];
    let mut is_prime = vec![true; nmax + 1];
    is_prime[0] = false;
    is_prime[1] = false;
    for p in 2..=nmax {
        if is_prime[p] {
            let mut pk = p as f64;
            let mut k = 1usize;
            while pk <= nmax as f64 {
                let idx = pk as usize;
                lam[idx] = (p as f64).ln();
                // mark multiples of p^k composite already handled; standard: for the exponent
                // we just set Λ(p^k) = log p — set all multiples of p except p^1 handled by marking
                let mut m = idx;
                while m <= nmax {
                    is_prime[m] = false;
                    m += idx;
                }
                pk *= p as f64;
                k += 1;
            }
        }
    }
    lam
}

/// symmetric Jacobi eigenvalue solver (returns eigenvalues, eigenvectors discarded)
fn jacobi(a: &[Vec<f64>]) -> (Vec<f64>, Vec<Vec<f64>>) {
    let n = a.len();
    let mut a = a.to_vec();
    let mut v = vec![vec![0.0; n]; n];
    for i in 0..n {
        v[i][i] = 1.0;
    }
    let mut n_sweeps = 0;
    loop {
        // find largest off-diagonal
        let mut p = 0;
        let mut q = 1;
        let mut maxv = 0.0;
        for i in 0..n {
            for j in (i + 1)..n {
                let av = a[i][j].abs();
                if av > maxv {
                    maxv = av;
                    p = i;
                    q = j;
                }
            }
        }
        if maxv < 1e-13 {
            break;
        }
        let app = a[p][p];
        let aqq = a[q][q];
        let apq = a[p][q];
        let theta = 0.5 * (aqq - app) / apq;
        let t = theta.signum() / (theta.abs() + (theta * theta + 1.0).sqrt());
        let c = 1.0 / (1.0 + t * t).sqrt();
        let s = t * c;
        for k in 0..n {
            if k != p && k != q {
                let akp = a[k][p];
                let akq = a[k][q];
                a[k][p] = c * akp - s * akq;
                a[p][k] = a[k][p];
                a[k][q] = s * akp + c * akq;
                a[q][k] = a[k][q];
            }
        }
        a[p][q] = 0.0;
        a[q][p] = 0.0;
        let appn = c * c * app - 2.0 * s * c * apq + s * s * aqq;
        let aqqn = s * s * app + 2.0 * s * c * apq + c * c * aqq;
        a[p][p] = appn;
        a[q][q] = aqqn;
        n_sweeps += 1;
        if n_sweeps > 100 * n * n {
            break;
        }
    }
    let ev: Vec<f64> = (0..n).map(|i| a[i][i]).collect();
    (ev, v)
}

/// simple xorshift64 + Box-Muller gaussian
struct XorShift(u64);
impl XorShift {
    fn new(seed: u64) -> Self {
        XorShift(seed.max(1))
    }
    fn next(&mut self) -> u64 {
        let mut x = self.0;
        x ^= x << 13;
        x ^= x >> 7;
        x ^= x << 17;
        self.0 = x;
        x
    }
    fn unit(&mut self) -> f64 {
        (self.next() >> 11) as f64 / (1u64 << 53) as f64
    }
    fn gauss(&mut self) -> f64 {
        let u1 = self.unit().max(1e-12);
        let u2 = self.unit();
        (-2.0 * u1.ln()).sqrt() * (TWO_PI * u2).cos()
    }
}
