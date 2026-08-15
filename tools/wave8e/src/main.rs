// wave8e — Beurling-operator finite shadows of the Nyman–Baez-Duarte criterion.
// Objects: Lambda_k(x) = {1/(kx)} in L^2(0,1).
//   G_N(j,k) = <Lambda_j, Lambda_k> ; c_k = <1, Lambda_k> ; d_N^2 = 1 - c^T G^{-1} c.
//   d_N^2 is EXACTLY the smallest eigenvalue of the augmented Gram matrix of {1,Lambda_1..N}
//   (eigenvector (1,-u), u = G^{-1}c). RH <-> d_N -> 0 (Baez-Duarte; literature, not corpus).
// Control: planted-zero fake Lambda'_k = {1/(kx)} + c0*{2/(kx)}, c0 = 2^(1/2+delta),
//   Mellin-lift of Z(s) = zeta(s)(1 + c0*2^-s) with exact zeros at 1/2+delta + i*pi/ln2 (mod 2pi i/ln2).
//
// Entry computation (exact breakpoint walk, f64):
//   <{a/(jx)},{b/(kx)}> = (1/(jk)) [ min(J,K) - a*b + R ],  J=aj, K=bk, g=gcd(J,K), P=lcm=JK/g,
//   R = int_{1/max(J,K)}^P {Jv}{Kv} v^-2 dv + tail,
//   tail = sum_{q=1..Q} int_0^P {Jv}{Kv} (qP+v)^-2 dv + m/((Q+1)P), m = period mean.
// Derived closed forms (verified symbolically in-note): c_a(k) = (a/k)(1-gamma + ln(k/a)), k>=a.

use rug::Float;

const GAMMA: f64 = 0.57721566490153286060651209008240243104215933593992;

pub fn gcd(mut a: usize, mut b: usize) -> usize {
    while b != 0 { let t = b; b = a % b; a = t; }
    a
}

/// Integrate int_a^b (Jv - M)(Kv - N) v^-2 dv  (for R-head and tail is separate).
/// Returns JK(b-a) - (JN+KM) ln(b/a) + MN (1/a - 1/b).
#[inline]
fn int_v2(J: f64, K: f64, M: f64, N: f64, a: f64, b: f64) -> f64 {
    J * K * (b - a) - (J * N + K * M) * (b / a).ln() + M * N * (1.0 / a - 1.0 / b)
}

/// Integrate int_a^b (Jv-M)(Kv-N) dv (for the period mean).
#[inline]
fn int_plain(J: f64, K: f64, M: f64, N: f64, a: f64, b: f64) -> f64 {
    J * K * (b * b * b - a * a * a) / 3.0 - (J * N + K * M) * (b * b - a * a) / 2.0
        + M * N * (b - a)
}

/// Integrate int_a^b (Jv-M)(Kv-N) (W+v)^-2 dv, W = qP.
#[inline]
fn int_block(J: f64, K: f64, M: f64, N: f64, a: f64, b: f64, W: f64) -> f64 {
    let f = |v: f64| {
        let wv = W + v;
        let l = wv.ln();
        J * K * (v - 2.0 * W * l - W * W / wv)
            - (J * N + K * M) * (l + W / wv)
            - M * N / wv
    };
    f(b) - f(a)
}

/// <{a1/(j x)},{a2/(k x)}> in L^2(0,1). a1,a2 in {1,2}.
pub fn gram_entry(a1: usize, j: usize, a2: usize, k: usize) -> f64 {
    let (J, K) = (a1 * j, a2 * k);
    let (Jf, Kf) = (J as f64, K as f64);
    let g = gcd(J, K);
    let P = J * K / g;                 // lcm
    let Pf = P as f64;
    let v0 = 1.0 / Jf.max(Kf);
    let _nJ = K / g;                    // J-multiples m=1..nJ in (0,P)
    let _nK = J / g;                    // K-multiples n=1..nK in (0,P)
    // plain region v in (1/(jk), 1/max(J,K)) exists iff jk >= max(J,K); there {Jv}{Kv}=JKv^2
    let jk = (j * k) as f64;
    let plain = if jk >= Jf.max(Kf) { Jf * Kf * (v0 - 1.0 / jk) } else { 0.0 };
    let vstart = v0.max(1.0 / jk);

    // one pass over merged breakpoints from vstart to P: R-head + mean-head
    let m0 = (Jf * vstart).floor() as usize + 1;
    let n0 = (Kf * vstart).floor() as usize + 1;
    let mut m = m0;
    let mut n = n0;
    let mut M0 = (m0 - 1) as f64; // floor(Jv) on (vstart, next bp)
    let mut N0 = (n0 - 1) as f64;
    let mut a = vstart;
    let mut rhead = 0.0f64;
    let mut mhead = 0.0f64;
    loop {
        let bj = (m as f64) / Jf;
        let bk = (n as f64) / Kf;
        let b = if bj <= bk { bj } else { bk };
        if b > Pf { break; }
        rhead += int_v2(Jf, Kf, M0, N0, a, b);
        mhead += int_plain(Jf, Kf, M0, N0, a, b);
        if bj <= bk { M0 += 1.0; m += 1; } // bj == bk: both fire
        if bk <= bj { N0 += 1.0; n += 1; }
        a = b;
    }
    // period mean m0 = (1/P)[ int_0^v0 JK v^2 dv + mhead ]
    let mean = (Jf * Kf * v0 * v0 * v0 / 3.0 + mhead) / Pf;

    // tail: Q blocks + remainder
    let qneed = (2.0e4 / Pf).ceil() as usize;
    let Q = qneed.max(1);
    let mut tail = 0.0f64;
    // full-period walk (0,P) for each block
    for q in 1..=Q {
        let W = (q as f64) * Pf;
        let mut m = 1usize;
        let mut n = 1usize;
        let (mut M0, mut N0) = (0.0f64, 0.0f64);
        let mut a = 0.0f64;
        loop {
            let bj = (m as f64) / Jf;
            let bk = (n as f64) / Kf;
            let b = if bj <= bk { bj } else { bk };
            if b >= Pf { break; }
            tail += int_block(Jf, Kf, M0, N0, a, b, W);
            if bj <= bk { M0 += 1.0; m += 1; } else { N0 += 1.0; n += 1; }
            a = b;
        }
        // last cell (a, P)
        tail += int_block(Jf, Kf, M0, N0, a, Pf, W);
    }
    tail += mean / ((Q as f64 + 1.0) * Pf);

    let R = rhead + tail;
    (plain + R) / jk
}

/// c_a(k) = <1, {a/(k x)}> = (a/k)(1 - gamma + ln(k/a)), k >= a.
/// For k < a (only a=2,k=1 occurs): c_2(1) = 2*int_2^inf {v} v^-2 dv = 3 - 2 ln2 - 2 gamma.
fn c_a(a: usize, k: usize) -> f64 {
    if k < a {
        // a=2,k=1
        return 3.0 - 2.0 * 2f64.ln() - 2.0 * GAMMA;
    }
    (a as f64 / k as f64) * (1.0 - GAMMA + (k as f64 / a as f64).ln())
}

// ---------- dense linear algebra (f64) ----------
fn cholesky_solve(g: &[f64], n: usize, c: &[f64]) -> Vec<f64> {
    // L L^T = G (lower). returns u = G^-1 c.
    let mut l = vec![0.0f64; n * n];
    for i in 0..n {
        for j in 0..=i {
            let mut s = g[i * n + j];
            for k in 0..j {
                s -= l[i * n + k] * l[j * n + k];
            }
            if i == j {
                l[i * n + j] = s.sqrt();
            } else {
                l[i * n + j] = s / l[j * n + j];
            }
        }
    }
    // solve L y = c, L^T u = y
    let mut y = vec![0.0f64; n];
    for i in 0..n {
        let mut s = c[i];
        for k in 0..i { s -= l[i * n + k] * y[k]; }
        y[i] = s / l[i * n + i];
    }
    let mut u = vec![0.0f64; n];
    for i in (0..n).rev() {
        let mut s = y[i];
        for k in (i + 1)..n { s -= l[k * n + i] * u[k]; }
        u[i] = s / l[i * n + i];
    }
    u
}

/// smallest eigenvalue of symmetric PD matrix via Cholesky + inverse iteration
fn min_eig(g: &[f64], n: usize, iters: usize) -> (f64, Vec<f64>) {
    let mut v = vec![1.0f64 / (n as f64).sqrt(); n];
    let mut lam = 0.0f64;
    for _ in 0..iters {
        let w = cholesky_solve(g, n, &v);
        let dot: f64 = w.iter().zip(v.iter()).map(|(a, b)| a * b).sum();
        let nrm: f64 = w.iter().map(|a| a * a).sum::<f64>().sqrt();
        lam = dot / nrm.max(1e-300); // Rayleigh: v^T G v / |v|^2 with w = G^-1 v
        // v^T G v = v^T w? (w = G^-1 v -> G w = v -> v^T G w = v^T v) — use (v·w)/(w·w) style:
        lam = dot / nrm.max(1e-300);
        for (vi, wi) in v.iter_mut().zip(w.iter()) { *vi = wi / nrm; }
    }
    // Rayleigh quotient of converged v: v^T G v = v^T (G v); G v = ? we have w = G^-1 v.
    // Compute Gv explicitly:
    let mut gv = vec![0.0f64; n];
    for i in 0..n {
        let mut s = 0.0;
        for j in 0..n { s += g[i * n + j] * v[j]; }
        gv[i] = s;
    }
    let lam = v.iter().zip(gv.iter()).map(|(a, b)| a * b).sum();
    (lam, v)
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let mode = args.get(1).map(|s| s.as_str()).unwrap_or("real");
    let n: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(600);

    // ---- cross-check vs rug (independent x-space breakpoint integration) ----
    if mode == "xcheck" {
        crosscheck_rug();
        return;
    }
    if mode == "proft" {
        use std::time::Instant;
        let pairs: [(usize, usize, usize, usize); 7] =
            [(1,1,1,1),(1,100,1,100),(1,100,1,101),(1,97,1,89),(1,50,1,50),(1,2,1,3),(1,70,1,71)];
        for &(a1, j, a2, k) in &pairs {
            let t = Instant::now();
            let v = gram_entry(a1, j, a2, k);
            println!("gram<{}/{}x,{}/{}x> = {:.8e} in {:?}", a1, j, a2, k, v, t.elapsed());
        }
        return;
    }
    if mode == "dbg" {
        let (a1, j, a2, k) = (args.get(2).and_then(|s| s.parse().ok()).unwrap_or(1),
                              args.get(3).and_then(|s| s.parse().ok()).unwrap_or(1),
                              args.get(4).and_then(|s| s.parse().ok()).unwrap_or(1),
                              args.get(5).and_then(|s| s.parse().ok()).unwrap_or(1));
        println!("gram<{}/{}x,{}/{}x> = {:.12e}", a1, j, a2, k, gram_entry(a1, j, a2, k));
        // components
        let (J, K) = (a1 * j, a2 * k);
        let (Jf, Kf) = (J as f64, K as f64);
        let g = gcd(J, K);
        let P = J * K / g;
        let Pf = P as f64;
        let v0 = 1.0 / Jf.max(Kf);
        let jk = (j * k) as f64;
        let plain = if jk >= Jf.max(Kf) { Jf * Kf * (v0 - 1.0 / jk) } else { 0.0 };
        let vstart = v0.max(1.0 / jk);
        // head walk
        let m0 = (Jf * vstart).floor() as usize + 1;
        let n0 = (Kf * vstart).floor() as usize + 1;
        let mut m = m0;
        let mut n = n0;
        let mut M0 = (m0 - 1) as f64;
        let mut N0 = (n0 - 1) as f64;
        let mut a = vstart;
        let mut rhead = 0.0f64;
        let mut mhead = 0.0f64;
        let mut cells = 0usize;
        loop {
            let bj = (m as f64) / Jf;
            let bk = (n as f64) / Kf;
            let b = if bj <= bk { bj } else { bk };
            if b > Pf { break; }
            rhead += int_v2(Jf, Kf, M0, N0, a, b);
            mhead += int_plain(Jf, Kf, M0, N0, a, b);
            cells += 1;
            if bj <= bk { M0 += 1.0; m += 1; }
            if bk <= bj { N0 += 1.0; n += 1; }
            a = b;
        }
        println!("  plain={:.6e} vstart={:.6e} rhead={:.6e} mhead={:.6e} cells={} mean={:.6e}",
                 plain, vstart, rhead, mhead, cells, (Jf*Kf*v0*v0*v0/3.0 + mhead)/Pf);
        // tail first 3 blocks
        let mut tsum = 0.0f64;
        for q in 1..=3 {
            let W = (q as f64) * Pf;
            let mut m = 1usize;
            let mut n = 1usize;
            let (mut M0, mut N0) = (0.0f64, 0.0f64);
            let mut a = 0.0f64;
            let mut bl = 0.0f64;
            loop {
                let bj = m as f64 / Jf;
                let bk = n as f64 / Kf;
                let b = bj.min(bk);
                if b >= Pf { break; }
                bl += int_block(Jf, Kf, M0, N0, a, b, W);
                if bj <= bk { M0 += 1.0; m += 1; } else { N0 += 1.0; n += 1; }
                a = b;
            }
            bl += int_block(Jf, Kf, M0, N0, a, Pf, W);
            println!("  block q={}: {:.6e}", q, bl);
            tsum += bl;
        }
        println!("  tail(first3)={:.6e}", tsum);
        return;
    }

    // build Gram + c
    let mut g = vec![0.0f64; n * n];
    let t0 = std::time::Instant::now();
    for j in 0..n {
        for k in 0..n {
            g[j * n + k] = gram_entry(1, j + 1, 1, k + 1);
        }
    }
    eprintln!("[build G N={} in {:?}]", n, t0.elapsed());
    let mut c = vec![0.0f64; n];
    for k in 0..n { c[k] = c_a(1, k + 1); }

    let control = mode == "control";
    let c0 = 2.0f64.powf(0.6); // 2^(1/2+delta), delta=0.1
    if control {
        for j in 0..n {
            for k in 0..n {
                let base = g[j * n + k];
                let g12 = gram_entry(1, j + 1, 2, k + 1);
                let g21 = gram_entry(2, j + 1, 1, k + 1);
                let g22 = gram_entry(2, j + 1, 2, k + 1);
                g[j * n + k] = base + c0 * (g12 + g21) + c0 * c0 * g22;
            }
        }
        for k in 0..n {
            let base = c[k];
            let c2 = c_a(2, k + 1);
            c[k] = base + c0 * c2;
        }
    }

    // solve G u = c ; d_N^2 = 1 - c.u  (== lambda_min of augmented Gram matrix, eigenvector (1,-u))
    let u = cholesky_solve(&g, n, &c);
    let cu: f64 = c.iter().zip(u.iter()).map(|(a, b)| a * b).sum();
    let d2 = 1.0 - cu;

    // raw lambda_min of G (degenerate: diagonal ~ const/k -> trivially -> 0)
    let (lmin, _v) = min_eig(&g, n.min(400), 30);
    // normalized correlation matrix, small n
    let nn = n.min(300);
    let mut cn = vec![0.0f64; nn * nn];
    for j in 0..nn {
        for k in 0..nn {
            let dj = g[j * n + j].sqrt();
            let dk = g[k * n + k].sqrt();
            cn[j * nn + k] = g[j * n + k] / (dj * dk);
        }
    }
    let (lcorr, _vc) = min_eig(&cn, nn, 40);

    // optimal coefficient profile u(k); Mellin-ish content at low t
    let mut prof = vec![0.0f64; n];
    let mut osc = 0.0f64;
    for k in 0..n {
        let kk = (k + 1) as f64;
        prof[k] = u[k] * kk * kk.ln(); // "smooth kernel" probe
        if k > 0 { osc = osc.max((prof[k] - prof[k - 1]).abs()); }
    }
    let pmin = prof.iter().cloned().fold(f64::INFINITY, f64::min);
    let pmax = prof.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
    // Mellin power |sum_k u_k k^{-1/2-it}|^2 at sample t (relative to t=0)
    let ts = [0.0f64, 4.532, 14.1347, 21.0220, 25.0109];
    let mut mpower = Vec::new();
    for &t in &ts {
        let (mut re, mut im) = (0.0f64, 0.0f64);
        for k in 0..n {
            let kk = (k + 1) as f64;
            let ang = -t * kk.ln();
            re += u[k] * ang.cos();
            im += u[k] * ang.sin();
        }
        mpower.push(re * re + im * im);
    }

    println!("== wave8e {} case, N={} ==", if control { "CONTROL" } else { "real" }, n);
    println!("d_N^2 (== lambda_min of augmented Gram) = {:.12e}", d2);
    println!("sqrt(N)*d_N = {:.6e}", (n as f64).sqrt() * d2.sqrt());
    println!("lambda_min(G_N) raw (n={}) = {:.6e}   (trivially->0: diag ~ const/k)", n.min(400), lmin);
    println!("lambda_min(correlation C_N) (n={}) = {:.6e}", nn, lcorr);
    println!("u-profile k*ln(k)*u_k: min={:.4e} max={:.4e} max|adjacent diff|={:.4e}", pmin, pmax, osc);
    println!("Mellin power |sum u_k k^(-1/2-it)|^2 at t = {:?}:", ts.iter().map(|x| format!("{:.4}", x)).collect::<Vec<_>>().join(","));
    for (i, p) in mpower.iter().enumerate() {
        println!("   t={:.4}: {:.6e}", ts[i], p);
    }
    // few u_k values for the record
    print!("u_k (k=1..12): ");
    for k in 0..12.min(n) { print!("{:.4e} ", u[k]); }
    println!();
}

// ---------- independent rug cross-check: x-space breakpoints, exact ----------
fn crosscheck_rug() {
    let prec = 256u32;
    let pairs: [(usize, usize, usize, usize); 6] = [(1,1,1,1),(1,1,1,2),(1,2,1,3),(1,7,1,11),(1,1,1,50),(2,1,2,3)];
    for &(a1, j, a2, k) in &pairs {
        // integrate_0^1 {a1/(jx)}{a2/(kx)} dx exactly via breakpoints x = a1/(j m), a2/(k n)
        // head on [x0, 1] with x0 = 1/M, tail [0,x0] via period-mean in v-space (rug)
        let mcut: usize = 200;
        let mut acc = Float::with_val(prec, 0);
        // breakpoints in x from x0=1/mcut up to 1: at a1/(j m) (m=1..) and a2/(k n)
        let mut xs: Vec<f64> = Vec::new();
        for m in 1..=(a1 * j * mcut) { let x = a1 as f64 / (j as f64 * m as f64); if x <= 1.0 && x >= 1.0 / mcut as f64 { xs.push(x); } }
        for n in 1..=(a2 * k * mcut) { let x = a2 as f64 / (k as f64 * n as f64); if x <= 1.0 && x >= 1.0 / mcut as f64 { xs.push(x); } }
        xs.sort_by(|p, q| p.partial_cmp(q).unwrap());
        xs.dedup();
        let mut lo = 1.0 / mcut as f64;
        for &hi in &xs {
            // ascending: intervals (lo, hi), hi = next breakpoint up; on it floor values constant:
            // a1/(jx) in [m1, m1+1) with m1 = floor(a1/(j*hi)) etc.
            if hi <= lo { continue; }
            let m1 = (a1 as f64 / (j as f64 * hi)).floor();
            let n1 = (a2 as f64 / (k as f64 * hi)).floor();
            // integrand (a1/(jx)-m1)(a2/(kx)-n1); antiderivative in x:
            // = a1a2/(jk) x^-2 - (a1 n1 / j + a2 m1 / k) x^-1 + m1 n1
            let A = a1 as f64 * a2 as f64 / (j as f64 * k as f64);
            let B = a1 as f64 * n1 / j as f64 + a2 as f64 * m1 / k as f64;
            let f = |x: f64| -A / x - B * x.ln() + m1 * n1 * x;
            acc += Float::with_val(prec, f(hi) - f(lo));
            lo = hi;
        }
        // final cell (lo, 1)
        if lo < 1.0 {
            let m1 = (a1 as f64 / (j as f64 * 1.0)).floor();
            let n1 = (a2 as f64 / (k as f64 * 1.0)).floor();
            let A = a1 as f64 * a2 as f64 / (j as f64 * k as f64);
            let B = a1 as f64 * n1 / j as f64 + a2 as f64 * m1 / k as f64;
            let f = |x: f64| -A / x - B * x.ln() + m1 * n1 * x;
            acc += Float::with_val(prec, f(1.0) - f(lo));
        }
        // tail x in (0, x0): v=1/x in (mcut, inf): mean of {a1 v/j}{a2 v/k} over period P=lcm(a1 j, a2 k)
        // approximate: average value m0 * x0 (correction o(x0)); use v-space head (1/max..) trick instead:
        // tail = int_{mcut}^inf {a1 v/j}{a2 v/k} v^-2 dv ~ mean/P-style; compute exactly via blocks
        let (J, K) = (a1 * j, a2 * k);
        let g = gcd(J, K);
        let P = J * K / g;
        // mean of {J t}{K t} over (0,P)
        let mut m0 = 0.0f64;
        let v0 = 1.0 / (J.max(K) as f64);
        m0 += J as f64 * K as f64 * v0 * v0 * v0 / 3.0;
        // walk (v0,P)
        let (mut m, mut n) = (1usize, 1usize);
        let (mut M0, mut N0) = if J == K { (1.0f64, 1.0f64) } else { (0.0, 0.0) };
        let (mut a, mut s) = (v0, 0.0f64);
        loop {
            let bj = m as f64 / J as f64;
            let bk = n as f64 / K as f64;
            let b = bj.min(bk);
            if b > P as f64 { break; }
            s += (J as f64 * K as f64) * (b * b - a * a) / 2.0 - (J as f64 * N0 + K as f64 * M0) * (b - a) + M0 * N0 * (b / a).ln();
            if bj <= bk { M0 += 1.0; m += 1; } else { N0 += 1.0; n += 1; }
            a = b;
        }
        m0 += s;
        m0 /= P as f64;
        // tail = int_{mcut}^inf ... v^-2 dv with v from mcut: f v^-2 ~ mean m0 -> m0/mcut + corr O(1/mcut^2)
        let tail = m0 / mcut as f64;
        acc += Float::with_val(prec, tail);
        let mine = gram_entry(a1, j, a2, k);
        let diff = (Float::with_val(prec, mine) - &acc).abs();
        let denom = acc.clone().abs();
        let rel = diff.to_f64() / denom.to_f64();
        println!("<{}/{}x , {}/{}x>: f64={:.10e} rug={:.10e} rel={:.2e}",
                 a1, j, a2, k, mine, acc.to_f64(), rel);
    }
}
