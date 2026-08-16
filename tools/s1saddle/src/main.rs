// S1-saddle closure probe (Rust, f64, log-space). No external deps.
// Phase A: saddle-point quadrature of M_k = 2∫Φ(u)u^{2k}du, t_k·k table.
// Phase B: polylogarithm-family scan (t_k closed form, zeros of Li_α).

use std::f64::consts::PI;

// ---------------- log Φ(u) ----------------
// Φ(u) = 2 Σ_{n≥1} (2π²n⁴e^{9u/2} − 3πn²e^{5u/2}) e^{−πn²e^{2u}}
// log t_n = log(2π²n⁴e^{9u/2}(1 − (3/(2πn²))e^{−2u})) − πn²e^{2u}
fn log_phi(u: f64) -> f64 {
    let e2u = (2.0 * u).exp();
    let em2u = (-2.0 * u).exp();
    let mut m = f64::NEG_INFINITY; // max log t_n
    let mut logsum = f64::NEG_INFINITY; // logaddexp accumulator
    for n in 1..=60u32 {
        let nn = n as f64;
        let x = 3.0 / (2.0 * PI * nn * nn) * em2u; // ∈ (0, 0.477)
        let lb = (2.0 * PI * PI).ln() + 4.0 * nn.ln() + 4.5 * u
            + (-x).ln_1p()
            - PI * nn * nn * e2u;
        if n == 1 {
            m = lb;
            logsum = lb;
        } else {
            if lb > m {
                // shift the running max (rare: only for u≈0, n=2..4)
                logsum = logsum * ((m - lb).exp()) + lb; // logaddexp with shift
                m = lb;
            } else {
                logsum += (lb - m).exp().ln_1p();
            }
        }
        if lb < m - 55.0 && n > 1 {
            break;
        }
    }
    (2f64).ln() + logsum // logsum = m + ln(1 + Σ_{n≥2} e^{l_n−m}) to ~1e-8; NOT ln_1p(logsum−m)
}

fn F(u: f64, k: f64) -> f64 {
    log_phi(u) + 2.0 * k * u.ln()
}

// adaptive Simpson (log-integrand already shifted; integrand ≤ 1)
fn simpson<G: Fn(f64) -> f64>(g: &G, a: f64, b: f64, tol: f64, depth: u32) -> f64 {
    fn rec<G: Fn(f64) -> f64>(g: &G, a: f64, b: f64, fa: f64, fm: f64, fb: f64, whole: f64, tol: f64, depth: u32) -> f64 {
        let m = 0.5 * (a + b);
        let lm = 0.5 * (a + m);
        let rm = 0.5 * (m + b);
        let flm = g(lm);
        let frm = g(rm);
        let left = (m - a) / 6.0 * (fa + 4.0 * flm + fm);
        let right = (b - m) / 6.0 * (fm + 4.0 * frm + fb);
        let err = (left + right - whole).abs();
        if depth == 0 || err < tol {
            return left + right + err / 15.0;
        }
        rec(g, a, m, fa, flm, fm, left, tol / 2.0, depth - 1)
            + rec(g, m, b, fm, frm, fb, right, tol / 2.0, depth - 1)
    }
    let m = 0.5 * (a + b);
    let fa = g(a);
    let fm = g(m);
    let fb = g(b);
    let whole = (b - a) / 6.0 * (fa + 4.0 * fm + fb);
    rec(g, a, b, fa, fm, fb, whole, tol, depth)
}

// find saddle u₀ (argmax F), return (u0, sigma)
fn find_saddle(k: f64) -> (f64, f64) {
    // coarse grid init (F is unimodal)
    let mut best = 0.05f64;
    let mut bestv = f64::NEG_INFINITY;
    let hi = if k < 5.0 { 6.0 } else { 10.0 };
    let mut u = 0.02;
    while u <= hi {
        let v = F(u, k);
        if v > bestv {
            bestv = v;
            best = u;
        }
        u += 0.05;
    }
    let mut u0 = best;
    for _ in 0..60 {
        let h = 1e-4 * (u0.abs() + 1.0);
        let fp = (F(u0 + h, k) - F(u0 - h, k)) / (2.0 * h);
        let fpp = (F(u0 + h, k) - 2.0 * F(u0, k) + F(u0 - h, k)) / (h * h);
        if fpp >= 0.0 {
            break; // not a max (numerical noise); keep grid best
        }
        let step = fp / fpp;
        if step.abs() < 1e-9 {
            break;
        }
        u0 -= step;
        if !(0.01..=12.0).contains(&u0) {
            u0 = u0.clamp(0.02, 12.0);
        }
    }
    let h = 1e-3 * (u0.abs() + 1.0);
    let fpp = (F(u0 + h, k) - 2.0 * F(u0, k) + F(u0 - h, k)) / (h * h);
    let sigma = 1.0 / (-fpp).max(1e-12).sqrt();
    (u0, sigma)
}

// log M_k via saddle-centered Simpson; k=0 via plain log-space Simpson on [0,10]
fn log_moment(k: f64) -> f64 {
    if k == 0.0 {
        let lp0 = log_phi(0.0);
        let g = |u: f64| (log_phi(u) - lp0).exp();
        let ia = simpson(&g, 0.0, 10.0, 1e-13, 30);
        // fixed fine-grid cross-check over [0,3]
        let n = 2_000_000usize;
        let h = 3.0 / n as f64;
        let mut s = g(0.0) + g(3.0);
        for j in 1..n {
            s += (2.0 + 2.0 * (j % 2) as f64) * g(h * j as f64);
        }
        let ib = h / 3.0 * s;
        let ma = (2f64).ln() + lp0 + ia.ln();
        let mb = (2f64).ln() + lp0 + ib.ln();
        println!("  [k=0 check] adaptive={:.12} fixed-grid={:.12} (true ln xi(1/2) = {:.12})", ma, mb, 0.497120778188314f64.ln());
        return mb;
    }
    let (u0, sigma) = find_saddle(k);
    let f0 = F(u0, k);
    let a = (u0 - 9.0 * sigma).max(0.0);
    let b = (u0 + 9.0 * sigma).min(12.0);
    let g = |u: f64| (F(u, k) - f0).exp();
    let i = simpson(&g, a, b, 1e-13, 30);
    (2f64).ln() + f0 + i.ln()
}

fn A(k: f64) -> f64 {
    log_moment(k) - lgamma_approx(2.0 * k + 1.0)
}

// The factorial part of D_k is computed EXACTLY as a ratio of 4 integers:
// log[(2k)(2k−1)/((2k+1)(2k+2))] = 2log(2k)! − log(2k−2)! − log(2k+2)!  (no lgamma error)
fn factorial_ratio_log(k: f64) -> f64 {
    let a = 2.0 * k;
    let b = 2.0 * k - 1.0;
    let c = 2.0 * k + 1.0;
    let d = 2.0 * k + 2.0;
    (a * b / (c * d)).ln()
}

fn main() {
    println!("=== S1 saddle closure probe ===");
    println!("b_0 check: log M_0 = {} (expect ln 0.497120778188314 = {})", log_moment(0.0), 0.497120778188314f64.ln());
    println!("logM_1 = {}, logM_2 = {}", log_moment(1.0), log_moment(2.0));

    // ---- Phase A: t_k table k=1..200, cross-check vs 8D ----
    let mut min_margin = f64::INFINITY;
    let mut min_k = 0usize;
    println!("\n--- Phase A: t_k, k=1..200 (direct quadrature) ---");
    println!("k     t_k             t_k*(k+1)");
    for k in 1..=200usize {
        let kf = k as f64;
        let mb = 2.0 * log_moment(kf) - log_moment(kf - 1.0) - log_moment(kf + 1.0);
        let d = mb - factorial_ratio_log(kf); // D_k = 2A_k − A_{k−1} − A_{k+1}
        let t = 1.0 - (-d).exp();
        let m = t * (kf + 1.0);
        if m < min_margin {
            min_margin = m;
            min_k = k;
        }
        if k <= 12 || k % 25 == 0 {
            println!("{:<5} {:<18.10} {:.8}", k, t, m);
        }
    }
    println!("min t_k*(k+1) = {:.8} at k = {}  (8D anchor: 1.06963238 at k=1)", min_margin, min_k);

    // ---- Phase A2: big-k table ----
    println!("\n--- Phase A2: t_k·k at large k ---");
    println!("k        k*t_k           2-4/L+4/L²      D_k           C1(k)");
    for &k in &[100usize, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000] {
        let kf = k as f64;
        let mb = 2.0 * log_moment(kf) - log_moment(kf - 1.0) - log_moment(kf + 1.0);
        let d = mb - factorial_ratio_log(kf);
        let t = 1.0 - (-d).exp();
        let kt = kf * t;
        let l = kf.ln();
        let model = 2.0 - 4.0 / l + 4.0 / (l * l);
        let ak = A(kf);
        let c1 = (ak + 2.0 * kf * l - 2.0 * kf * l.ln()) / (2.0 * kf);
        println!("{:<8} {:<15.6} {:<15.6} {:<12.8} {:.6}", k, kt, model, d, c1);
    }
    println!("(limit: k·t_k → 2; C1 → 1−2·ln2 = {})", 1.0 - 2.0 * 2f64.ln());

    // ---- Phase B: polylog families ----
    println!("\n--- Phase B1: closed-form t_k for a_k = k^{{-α}} and (k+1)^{{-α}} ---");
    for &alpha in &[0.5f64, 1.0, 1.5, 2.0, 2.5, 3.0] {
        let k = 1e6f64;
        // a_k = k^{-a}
        let tk_a = 1.0 - (1.0 - 1.0 / (k * k)).powf(-alpha);
        // a_k = (k+1)^{-a}
        let tk_b = 1.0 - (((k + 1.0) * (k + 1.0)) / (k * (k + 2.0))).powf(alpha);
        println!("α={:.1}: k·t_k (k^{{-α}}) = {:.3e}   k·t_k ((k+1)^{{-α}}) = {:.3e}   (→ 0⁻ for both)",
                 alpha, k * tk_a, k * tk_b);
    }
    println!("Note: both power-law families are log-CONVEX; t_k ≈ −α/k² < 0. The memo's 't_k ≈ 2/k' for 1/(k+1)² is REFUTED by closed form.");

    // ---- Phase B2: zeros of Li_α in |z|<1 ----
    println!("\n--- Phase B2: zeros of Li_α(z) in |z|<1 (grid + Newton + winding) ---");
    for &alpha in &[0.5f64, 0.7, 0.9, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0] {
        let (zeros, nonreal) = scan_polylog_zeros(alpha);
        let w05 = winding(alpha, 0.5);
        let w09 = winding(alpha, 0.9);
        let zs: Vec<String> = zeros.iter().map(|(r, i)| format!("({:.4},{:.4})", r, i)).collect();
        println!("α={:.1}: zeros_in_disk={} nonreal={} winding(r=.5)={} winding(r=.9)={}  {}",
                 alpha, zeros.len(), nonreal, w05, w09, zs.join(" "));
    }

    // ---- Phase B3: Li₂ continuation zeros, |z| ∈ (1,2] ----
    println!("\n--- Phase B3: Li₂ continuation zeros in 1<|z|≤2 ---");
    let cont = scan_li2_continuation();
    if cont.is_empty() {
        println!("none found");
    } else {
        for (r, i) in cont {
            println!("  z = ({:.5}, {:.5})", r, i);
        }
    }

    // ---- Phase B4: moment-normalized Bessel-type F_α(t) real-zero sign scan ----
    println!("\n--- Phase B4: F_α(t) = Σ(−1)^k t^(2k)/((2k)!·(k+1)^α), real zeros on [0,40] ---");
    for &alpha in &[0.0f64, 1.0, 2.0, 3.0] {
        let nz = real_zero_sign_changes(alpha, 40.0);
        println!("α={:.1}: sign changes of F_α on [0,40] = {} (all-real-zeros if signs alternate at each zero)", alpha, nz);
    }
}

// ---------------- Phase B: polylogarithm ----------------
fn polylog(zr: f64, zi: f64, alpha: f64, tol: f64, cap: usize) -> (f64, f64) {
    let mut sr = 0.0;
    let mut si = 0.0;
    let mut pr = 1.0;
    let mut pi = 0.0;
    let mut maxm = 0.0f64;
    for k in 1..=cap {
        // z^k
        let nr = pr * zr - pi * zi;
        let ni = pr * zi + pi * zr;
        pr = nr;
        pi = ni;
        let inv = 1.0 / (k as f64).powf(alpha);
        let tr = pr * inv;
        let ti = pi * inv;
        sr += tr;
        si += ti;
        let m = (tr * tr + ti * ti).sqrt();
        if m > maxm {
            maxm = m;
        }
        if k > 100 && m < tol * maxm {
            break;
        }
    }
    (sr, si)
}

// winding number of Li_α(r e^{iθ}) around 0 (argument principle)
fn winding(alpha: f64, r: f64) -> i32 {
    let n = 4000usize;
    let mut prev = (0.0f64, 0.0f64);
    let mut total = 0.0f64;
    let mut prev_ok = false;
    for j in 0..=n {
        let th = 2.0 * PI * j as f64 / n as f64;
        let (zr, zi) = (r * th.cos(), r * th.sin());
        let (wr, wi) = polylog(zr, zi, alpha, 1e-12, 200000);
        if prev_ok {
            // angle increment between prev and current (atan2 diff, wrapped to (-π, π])
            let mut d = wi.atan2(wr) - prev.1.atan2(prev.0);
            while d > PI {
                d -= 2.0 * PI;
            }
            while d <= -PI {
                d += 2.0 * PI;
            }
            total += d;
        }
        prev = (wr, wi);
        prev_ok = true;
    }
    (total / (2.0 * PI)).round() as i32
}

// grid + Newton scan of Li_α zeros in |z| ≤ 0.99; returns (zeros, count_nonreal)
fn scan_polylog_zeros(alpha: f64) -> (Vec<(f64, f64)>, usize) {
    let step = 0.02f64;
    let mut cands: Vec<(f64, f64, f64)> = Vec::new(); // (re, im, |Li|)
    let mut re = -0.98;
    while re <= 0.98 {
        let mut im = -0.98;
        while im <= 0.98 {
            if re * re + im * im <= 0.97 {
                let (wr, wi) = polylog(re, im, alpha, 1e-8, 200000);
                let m = (wr * wr + wi * wi).sqrt();
                // local minimum in 4-neighborhood (rough)
                let (l1, l2) = polylog(re - step, im, alpha, 1e-6, 200000);
                let (r1, r2) = polylog(re + step, im, alpha, 1e-6, 200000);
                let (u1, u2) = polylog(re, im + step, alpha, 1e-6, 200000);
                let (d1, d2) = polylog(re, im - step, alpha, 1e-6, 200000);
                let ml = (l1 * l1 + l2 * l2).sqrt();
                let mr = (r1 * r1 + r2 * r2).sqrt();
                let mu = (u1 * u1 + u2 * u2).sqrt();
                let md = (d1 * d1 + d2 * d2).sqrt();
                if m <= ml && m <= mr && m <= mu && m <= md && m < 0.35 {
                    cands.push((re, im, m));
                }
            }
            im += step;
        }
        re += step;
    }
    // Newton refine each candidate (Li' = Li_{α−1}(z)/z; z=0 special)
    let mut zeros: Vec<(f64, f64)> = Vec::new();
    for (cr, ci, _) in cands {
        let mut zr = cr;
        let mut zi = ci;
        for _ in 0..40 {
            let (wr, wi) = polylog(zr, zi, alpha, 1e-14, 200000);
            if zr * zr + zi * zi < 1e-18 {
                zr = 0.0;
                zi = 0.0;
                break;
            }
            let (dr, di) = polylog(zr, zi, alpha - 1.0, 1e-14, 200000);
            // derivative = Li_{α−1}(z)/z
            let inv = 1.0 / (zr * zr + zi * zi);
            let der = (dr * zr + di * zi) * inv;
            let dei = (di * zr - dr * zi) * inv;
            let denom = der * der + dei * dei;
            if denom < 1e-30 {
                break;
            }
            // z ← z − f/f'
            let numr = wr * der + wi * dei;
            let numi = wi * der - wr * dei;
            let nzr = zr - numr / denom;
            let nzi = zi - numi / denom;
            if (nzr - zr).hypot(nzi - zi) < 1e-12 {
                zr = nzr;
                zi = nzi;
                break;
            }
            zr = nzr;
            zi = nzi;
        }
        if zr * zr + zi * zi > 1e-6 && (zr * zr + zi * zi) < 1.0 {
            // dedupe
            let mut dup = false;
            for (er, ei) in zeros.iter() {
                if (er - zr).hypot(ei - zi) < 1e-4 {
                    dup = true;
                    break;
                }
            }
            if !dup {
                zeros.push((zr, zi));
            }
        }
    }
    // always add the origin zero if present in domain (Li_α(0)=0)
    if !zeros.iter().any(|(r, i)| (*r).hypot(*i) < 1e-3) {
        zeros.push((0.0, 0.0));
    }
    let nonreal = zeros.iter().filter(|(_, i)| i.abs() > 1e-6).count();
    (zeros, nonreal)
}

// Li₂ continuation for |z|>1: Li₂(z) = −Li₂(1/z) − π²/6 − ½ log²(−z), z ∉ [0,1)
fn li2_cont(zr: f64, zi: f64) -> (f64, f64) {
    let r2 = zr * zr + zi * zi;
    let wr = zr / r2;
    let wi = -zi / r2; // 1/z
    let (a, b) = polylog(wr, wi, 2.0, 1e-14, 200000);
    // log(−z) = ln|z| + i·arg(−z), arg(−z) = atan2(−zi, −zr) ∈ (−π,π]
    let th = (-zi).atan2(-zr);
    let (lr, li) = (0.5 * r2.ln(), th);
    // ½ log²(−z) = ½ (lr + i li)²
    let (sqr, sqi) = (0.5 * (lr * lr - li * li), lr * li);
    (-a - PI * PI / 6.0 - sqr, -b - sqi)
}

fn scan_li2_continuation() -> Vec<(f64, f64)> {
    let mut cands: Vec<(f64, f64, f64)> = Vec::new();
    let mut r = 1.02;
    while r <= 2.0 {
        let mut th = 0.01;
        while th < 2.0 * PI - 0.01 {
            let (zr, zi) = (r * th.cos(), r * th.sin());
            let (wr, wi) = li2_cont(zr, zi);
            let m = (wr * wr + wi * wi).sqrt();
            // neighborhood on the same radius
            let th2 = th + 0.05;
            let (zr2, zi2) = (r * th2.cos(), r * th2.sin());
            let (wr2, wi2) = li2_cont(zr2, zi2);
            let m2 = (wr2 * wr2 + wi2 * wi2).sqrt();
            let th0 = th - 0.05;
            let (zr0, zi0) = (r * th0.cos(), r * th0.sin());
            let (wr0, wi0) = li2_cont(zr0, zi0);
            let m0 = (wr0 * wr0 + wi0 * wi0).sqrt();
            if m <= m2 && m <= m0 && m < 0.2 {
                cands.push((zr, zi, m));
            }
            th += 0.05;
        }
        r += 0.05;
    }
    let mut zeros: Vec<(f64, f64)> = Vec::new();
    for (cr, ci, _) in cands {
        let mut zr = cr;
        let mut zi = ci;
        for _ in 0..40 {
            let (wr, wi) = li2_cont(zr, zi);
            // numeric derivative via complex step
            let h = 1e-7;
            let (zrh, zih) = (zr + h, zi);
            let (wr2, wi2) = li2_cont(zrh, zih);
            let der = (wr2 - wr) / h;
            let dei = (wi2 - wi) / h;
            let denom = der * der + dei * dei;
            if denom < 1e-30 {
                break;
            }
            let nzr = zr - (wr * der + wi * dei) / denom;
            let nzi = zi - (wi * der - wr * dei) / denom;
            if (nzr - zr).hypot(nzi - zi) < 1e-10 {
                zr = nzr;
                zi = nzi;
                break;
            }
            zr = nzr;
            zi = nzi;
        }
        let mut dup = false;
        for (er, ei) in zeros.iter() {
            if (er - zr).hypot(ei - zi) < 1e-4 {
                dup = true;
                break;
            }
        }
        if !dup {
            zeros.push((zr, zi));
        }
    }
    zeros
}

// sign changes of F_α(t) = Σ(−1)^k t^{2k}/((2k)! (k+1)^α) on [0, tmax]
fn real_zero_sign_changes(alpha: f64, tmax: f64) -> usize {
    let n = 4000usize;
    let mut changes = 0usize;
    let mut prev = f64::NAN;
    let mut prev_sign = 0i32;
    for j in 0..=n {
        let t = tmax * j as f64 / n as f64;
        let t2 = t * t;
        let mut s = 1.0f64; // k=0 term: t^0/(0!·1^α) = 1
        for k in 1..=4000usize {
            let kf = k as f64;
            let lgt = 2.0 * kf * t2.ln() - lgamma_approx(2.0 * kf + 1.0) - alpha * (kf + 1.0).ln();
            let term = if k % 2 == 0 { 1.0 } else { -1.0 } * lgt.exp();
            s += term;
            if k > 10 && term.abs() < 1e-16 * s.abs().max(1e-300) {
                break;
            }
        }
        let sg = if s > 0.0 { 1 } else if s < 0.0 { -1 } else { 0 };
        if j > 0 && prev_sign != 0 && sg != 0 && sg != prev_sign {
            changes += 1;
        }
        if sg != 0 {
            prev_sign = sg;
        }
        prev = s;
    }
    changes
}

// lgamma via Stirling + Lanczos-lite for x ≥ 1 (rel err ~1e-13 at x≥1, better at large x).
fn lgamma_approx(x: f64) -> f64 {
    // Lanczos (g=7, n=9) — standard coefficients
    const G: f64 = 7.0;
    let c: [f64; 9] = [
        0.99999999999980993,
        676.5203681218851,
        -1259.1392167224028,
        771.32342877765313,
        -176.61502916214059,
        12.507343278686905,
        -0.13857109526572012,
        9.9843695780195716e-6,
        1.5056327351493116e-7,
    ];
    if x < 0.5 {
        return (PI / (PI * x).sin()).ln() - lgamma_approx(1.0 - x);
    }
    let xm1 = x - 1.0;
    let mut a = c[0];
    let mut t = xm1 + G + 0.5;
    for i in 1..9 {
        a += c[i] / (xm1 + i as f64);
    }
    0.5 * (2.0 * PI).ln() + (xm1 + 0.5) * t.ln() - t + a.ln()
}
