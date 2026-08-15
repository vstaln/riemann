// WAVE 8C — Nyman–Beurling / Báez-Duarte distance d_N in L^2(0,1), rho_k(x)={1/(kx)}.
// Closed forms: b_k = (ln k + 1 - gamma)/k ; G_jk = int_1^inf {t/j}{t/k} t^-2 dt
//   evaluated exactly: period L=lcm(j,k), piecewise-quadratic f, m=0 exact, m=1..3 via
//   stable v-substitution, tail m>=4 via p-expansion with Z_p = sum_{m>=4} m^{-(p+2)}.
// f64 sweep + 256-bit MPFR (rug) cross-check (ill-conditioned Gram, kappa ~ N).
use rug::Float;
use std::fs;
use std::thread;

const GAMMA: f64 = 0.57721566490153286060651209008240243104215933593992;

fn gcd(a: u64, b: u64) -> u64 {
    let (mut x, mut y) = (a, b);
    while y != 0 {
        let t = x % y;
        x = y;
        y = t;
    }
    x
}
fn lcm(a: u64, b: u64) -> u64 {
    a / gcd(a, b) * b
}

// intervals (alpha,beta,floor(alpha/j),floor(alpha/k)) covering [1,1+L]
fn intervals(j: u64, k: u64, l: u64) -> Vec<(u64, u64, u64, u64)> {
    let end = 1 + l;
    let mut pts: Vec<u64> = Vec::with_capacity(((l / j) + (l / k) + 2) as usize);
    let mut m = 1u64;
    loop {
        let p = m * j;
        if p > end {
            break;
        }
        if p > 1 {
            pts.push(p);
        }
        m += 1;
    }
    let mut m = 1u64;
    loop {
        let p = m * k;
        if p > end {
            break;
        }
        if p > 1 {
            pts.push(p);
        }
        m += 1;
    }
    pts.sort_unstable();
    pts.dedup();
    let mut ivs = Vec::with_capacity(pts.len() + 1);
    let mut cur = 1u64;
    for &p in &pts {
        if p > cur {
            ivs.push((cur, p, cur / j, cur / k));
            cur = p;
        }
    }
    if cur < end {
        ivs.push((cur, end, cur / j, cur / k));
    }
    ivs
}

// Z_p = sum_{m=m0}^inf m^{-(p+2)} (m0=4: combined tail), direct sum + Euler-Maclaurin
fn z_table_f64(p_max: usize, m0: u64) -> Vec<f64> {
    let n1 = 10_000u64;
    let mut z = vec![0.0f64; p_max];
    for p in 0..p_max {
        let s = p as f64 + 2.0;
        let mut acc = 0.0;
        for m in m0..=n1 {
            acc += (m as f64).powf(-s);
        }
        let x = n1 as f64;
        acc += x.powf(1.0 - s) / (s - 1.0)
            + 0.5 * x.powf(-s)
            + (s / 12.0) * x.powf(-s - 1.0)
            - (s * (s + 1.0) * (s + 2.0) / 720.0) * x.powf(-s - 3.0);
        z[p] = acc;
    }
    z
}

fn gram_f64(j: u64, k: u64, z: &[f64]) -> f64 {
    let l = lcm(j, k);
    let ivs = intervals(j, k, l);
    let lf = l as f64;
    let jf = j as f64;
    let kf = k as f64;
    let mut total = 0.0f64;
    for &(x1, x2, ai, bi) in &ivs {
        let a = x1 as f64;
        let b = x2 as f64;
        let aif = ai as f64;
        let bif = bi as f64;
        let c2 = 1.0 / (jf * kf);
        let c1 = -(aif / kf + bif / jf);
        let c0 = aif * bif;
        // m = 0 exact
        total += c2 * (b - a) + c1 * (b.ln() - a.ln()) + c0 * (1.0 / a - 1.0 / b);
        // m = 1..3 via stable v-substitution
        for m in 1..4u64 {
            let ml = m as f64 * lf;
            let v1 = a / ml;
            let v2 = b / ml;
            let c2p = ml * ml / (jf * kf);
            let c1p = -ml * (aif / kf + bif / jf);
            let c0p = aif * bif;
            let e2 = |v: f64| v - 2.0 * (v + 1.0).ln() - 1.0 / (v + 1.0);
            let e1 = |v: f64| (v + 1.0).ln() + 1.0 / (v + 1.0);
            let e0 = |v: f64| -1.0 / (v + 1.0);
            total += (c2p * (e2(v2) - e2(v1)) + c1p * (e1(v2) - e1(v1)) + c0p * (e0(v2) - e0(v1))) / ml;
        }
        // tail m >= 4 via p-expansion
        let bl = b / lf;
        let al = a / lf;
        let mut pb1 = bl;
        let mut pa1 = al;
        for p in 0..z.len() {
            let pb2 = pb1 * bl;
            let pa2 = pa1 * al;
            let pb3 = pb2 * bl;
            let pa3 = pa2 * al;
            let d1 = pb1 - pa1;
            let d2 = pb2 - pa2;
            let d3 = pb3 - pa3;
            let pf = p as f64;
            let sign = if p & 1 == 0 { 1.0 } else { -1.0 };
            let t1 = c2 * lf * d3 / (pf + 3.0);
            let t2 = c1 * d2 / (pf + 2.0);
            let t3 = c0 * d1 / lf / (pf + 1.0);
            total += sign * (pf + 1.0) * z[p] * (t1 + t2 + t3);
            pb1 = pb2;
            pa1 = pa2;
        }
    }
    total
}

fn z_table_mpfr(p_max: usize, m0: u64) -> Vec<Float> {
    z_table_f64(p_max, m0)
        .iter()
        .map(|v| Float::with_val(256, *v))
        .collect()
}

fn gram_mpfr(j: u64, k: u64, z: &[Float]) -> Float {
    let l = lcm(j, k);
    let ivs = intervals(j, k, l);
    let mut total = Float::with_val(256, 0);
    let lf = Float::with_val(256, l);
    let jf = Float::with_val(256, j);
    let kf = Float::with_val(256, k);
    let two = Float::with_val(256, 2);
    for &(x1, x2, ai, bi) in &ivs {
        let a = Float::with_val(256, x1);
        let b = Float::with_val(256, x2);
        let aif = Float::with_val(256, ai);
        let bif = Float::with_val(256, bi);
        let jk = Float::with_val(256, &jf * &kf);
        let c2 = Float::with_val(256, 1.0 / &jk);
        let ak = Float::with_val(256, &aif / &kf);
        let bj = Float::with_val(256, &bif / &jf);
        let akbj = Float::with_val(256, &ak + &bj);
        let c1 = Float::with_val(256, -&akbj);
        let c0 = Float::with_val(256, &aif * &bif);
        // m = 0
        let db = Float::with_val(256, &b - &a);
        let t1 = Float::with_val(256, &c2 * &db);
        let la = Float::with_val(256, &a).ln();
        let lb = Float::with_val(256, &b).ln();
        let dl = Float::with_val(256, &lb - &la);
        let t2 = Float::with_val(256, &c1 * &dl);
        let ra = Float::with_val(256, 1.0 / &a);
        let rb = Float::with_val(256, 1.0 / &b);
        let dr = Float::with_val(256, &ra - &rb);
        let t3 = Float::with_val(256, &c0 * &dr);
        let m0 = Float::with_val(256, &t1 + &t2);
        total += Float::with_val(256, &m0 + &t3);
        // m = 1..3 via v-substitution
        for m in 1..4u64 {
            let ml = Float::with_val(256, m * l);
            let v1 = Float::with_val(256, &a / &ml);
            let v2 = Float::with_val(256, &b / &ml);
            let ml2 = Float::with_val(256, &ml * &ml);
            let c2p = Float::with_val(256, &ml2 / &jk);
            let mla = Float::with_val(256, &ml * &akbj);
            let c1p = Float::with_val(256, -mla);
            let c0p = Float::with_val(256, &aif * &bif);
            let w1 = Float::with_val(256, &v1 + 1.0);
            let w2 = Float::with_val(256, &v2 + 1.0);
            let lw1 = Float::with_val(256, &w1).ln();
            let lw2 = Float::with_val(256, &w2).ln();
            let rw1 = Float::with_val(256, 1.0 / &w1);
            let rw2 = Float::with_val(256, 1.0 / &w2);
            let twl1 = Float::with_val(256, &two * &lw1);
            let twl2 = Float::with_val(256, &two * &lw2);
            let u1 = Float::with_val(256, &v1 - &twl1);
            let e2v1 = Float::with_val(256, &u1 - &rw1);
            let u2 = Float::with_val(256, &v2 - &twl2);
            let e2v2 = Float::with_val(256, &u2 - &rw2);
            let e1v1 = Float::with_val(256, &lw1 + &rw1);
            let e1v2 = Float::with_val(256, &lw2 + &rw2);
            let e0v1 = Float::with_val(256, -&rw1);
            let e0v2 = Float::with_val(256, -&rw2);
            let d2e = Float::with_val(256, &e2v2 - &e2v1);
            let d1e = Float::with_val(256, &e1v2 - &e1v1);
            let d0e = Float::with_val(256, &e0v2 - &e0v1);
            let p1 = Float::with_val(256, &c2p * &d2e);
            let p2 = Float::with_val(256, &c1p * &d1e);
            let p3 = Float::with_val(256, &c0p * &d0e);
            let p12 = Float::with_val(256, &p1 + &p2);
            let p123 = Float::with_val(256, &p12 + &p3);
            total += Float::with_val(256, &p123 / &ml);
        }
        // tail m >= 4 via p-expansion (mirror of gram_f64: t1 carries *lf, t3 carries /lf)
        let bl = Float::with_val(256, &b / &lf);
        let al = Float::with_val(256, &a / &lf);
        let mut pb1 = bl.clone();
        let mut pa1 = al.clone();
        for p in 0..z.len() {
            let pb2 = Float::with_val(256, &pb1 * &bl);
            let pa2 = Float::with_val(256, &pa1 * &al);
            let pb3 = Float::with_val(256, &pb2 * &bl);
            let pa3 = Float::with_val(256, &pa2 * &al);
            let d1 = Float::with_val(256, &pb1 - &pa1);
            let d2 = Float::with_val(256, &pb2 - &pa2);
            let d3 = Float::with_val(256, &pb3 - &pa3);
            let pf = p as f64;
            let c2d3 = Float::with_val(256, &c2 * &d3);
            let c1d2 = Float::with_val(256, &c1 * &d2);
            let c0d1 = Float::with_val(256, &c0 * &d1);
            // f64: t1 = c2*lf*d3/(p+3); t2 = c1*d2/(p+2); t3 = c0*d1/lf/(p+1)
            let c2d3lf = Float::with_val(256, &c2d3 * &lf);
            let t1 = Float::with_val(256, &c2d3lf / (pf + 3.0));
            let t2 = Float::with_val(256, &c1d2 / (pf + 2.0));
            let c0d1lf = Float::with_val(256, &c0d1 / &lf);
            let t3 = Float::with_val(256, &c0d1lf / (pf + 1.0));
            let t12 = Float::with_val(256, &t1 + &t2);
            let inner = Float::with_val(256, &t12 + &t3);
            let sgn = if p & 1 == 0 { 1.0f64 } else { -1.0f64 };
            let zl = Float::with_val(256, sgn * (pf + 1.0) * &z[p]);
            total += Float::with_val(256, &zl * inner);
            pb1 = pb2;
            pa1 = pa2;
        }
    }
    total
}

fn b_f64(k: u64) -> f64 {
    ((k as f64).ln() + 1.0 - GAMMA) / k as f64
}
fn b_mpfr(k: u64) -> Float {
    let g = Float::with_val(256, GAMMA);
    let one = Float::with_val(256, 1);
    let lk = Float::with_val(256, k).ln();
    let l1 = Float::with_val(256, &lk + &one);
    let num = Float::with_val(256, &l1 - &g);
    Float::with_val(256, &num / Float::with_val(256, k))
}

// ---- independent verification: x-quadrature with exact rational antiderivatives ----
fn gram_quad(j: u64, k: u64, m0: u64) -> (f64, f64) {
    let mut pts: Vec<f64> = Vec::with_capacity(2 * m0 as usize);
    for m in 1..=m0 {
        pts.push(1.0 / (m as f64 * j as f64));
        pts.push(1.0 / (m as f64 * k as f64));
    }
    pts.sort_by(|a, b| b.partial_cmp(a).unwrap());
    pts.dedup();
    let mut total = 0.0;
    let mut prev = 1.0f64;
    for &p in &pts {
        if p >= prev {
            continue;
        }
        let xm = 0.5 * (p + prev);
        let aj = (1.0 / (j as f64 * xm)).floor();
        let bk = (1.0 / (k as f64 * xm)).floor();
        let f = |x: f64| {
            -1.0 / (j as f64 * k as f64 * x) - (aj / k as f64) * x.ln() - (bk / j as f64) * x.ln() + aj * bk * x
        };
        total += f(prev) - f(p);
        prev = p;
    }
    (total, prev)
}

fn b_quad(k: u64, m0: u64) -> (f64, f64) {
    let mut pts: Vec<f64> = Vec::with_capacity(m0 as usize);
    for m in 1..=m0 {
        pts.push(1.0 / (m as f64 * k as f64));
    }
    pts.sort_by(|a, b| b.partial_cmp(a).unwrap());
    pts.dedup();
    let mut total = 0.0;
    let mut prev = 1.0f64;
    for &p in &pts {
        if p >= prev {
            continue;
        }
        let xm = 0.5 * (p + prev);
        let a = (1.0 / (k as f64 * xm)).floor();
        let f = |x: f64| (1.0 / k as f64) * x.ln() - a * x;
        total += f(prev) - f(p);
        prev = p;
    }
    (total, prev)
}

// ---- Cholesky solves ----
fn cholesky_solve_f64(g: &[f64], b: &[f64], n: usize) -> (Vec<f64>, f64, bool, f64) {
    let mut l = vec![0.0f64; n * n];
    let mut ok = true;
    let mut min_diag = f64::INFINITY;
    let mut max_diag = 0.0f64;
    for i in 0..n {
        for j in 0..=i {
            let mut s = g[i * n + j];
            for k in 0..j {
                s -= l[i * n + k] * l[j * n + k];
            }
            if i == j {
                if s <= 0.0 {
                    ok = false;
                    s = 1e-300;
                }
                l[i * n + i] = s.sqrt();
                min_diag = min_diag.min(s);
                max_diag = max_diag.max(s);
            } else {
                l[i * n + j] = s / l[j * n + j];
            }
        }
    }
    let mut y = vec![0.0f64; n];
    for i in 0..n {
        let mut s = b[i];
        for j in 0..i {
            s -= l[i * n + j] * y[j];
        }
        y[i] = s / l[i * n + i];
    }
    let mut c = vec![0.0f64; n];
    for i in (0..n).rev() {
        let mut s = y[i];
        for j in (i + 1)..n {
            s -= l[j * n + i] * c[j];
        }
        c[i] = s / l[i * n + i];
    }
    let bt: f64 = b.iter().zip(&c).map(|(x, y)| x * y).sum();
    (
        c,
        1.0 - bt,
        ok,
        if min_diag > 0.0 { max_diag / min_diag } else { f64::INFINITY },
    )
}

fn cholesky_solve_mpfr(g: &[Float], b: &[Float], n: usize) -> (Float, Float) {
    let mut l = vec![Float::with_val(256, 0); n * n];
    for i in 0..n {
        for j in 0..=i {
            let mut s = g[i * n + j].clone();
            for k in 0..j {
                let t = Float::with_val(256, &l[i * n + k] * &l[j * n + k]);
                s -= t;
            }
            if i == j {
                l[i * n + i] = s.sqrt();
            } else {
                l[i * n + j] = Float::with_val(256, &s / &l[j * n + j]);
            }
        }
    }
    let mut y = vec![Float::with_val(256, 0); n];
    for i in 0..n {
        let mut s = b[i].clone();
        for j in 0..i {
            let t = Float::with_val(256, &l[i * n + j] * &y[j]);
            s -= t;
        }
        y[i] = Float::with_val(256, &s / &l[i * n + i]);
    }
    let mut c = vec![Float::with_val(256, 0); n];
    for i in (0..n).rev() {
        let mut s = y[i].clone();
        for j in (i + 1)..n {
            let t = Float::with_val(256, &l[j * n + i] * &c[j]);
            s -= t;
        }
        c[i] = Float::with_val(256, &s / &l[i * n + i]);
    }
    let mut bt = Float::with_val(256, 0);
    for i in 0..n {
        let t = Float::with_val(256, &b[i] * &c[i]);
        bt += t;
    }
    (c[0].clone(), Float::with_val(256, 1) - bt)
}

// ---- threaded Gram fill ----
fn gram_matrix(n: usize, idx: &(dyn Fn(usize) -> u64 + Sync), z: &[f64]) -> Vec<f64> {
    let mut g = vec![0.0f64; n * n];
    let nthreads = 8.min(n);
    thread::scope(|s| {
        let base = g.as_mut_ptr() as usize;
        for t in 0..nthreads {
            let start = t * n / nthreads;
            let end = (t + 1) * n / nthreads;
            let z = z;
            s.spawn(move || {
                for i in start..end {
                    let ji = idx(i);
                    for k in 0..n {
                        unsafe {
                            *((base + (i * n + k) * 8) as *mut f64) = gram_f64(ji, idx(k), z);
                        }
                    }
                }
            });
        }
    });
    g
}

fn mobius_sieve(limit: usize) -> Vec<i64> {
    let mut mu = vec![1i64; limit + 1];
    let mut is_prime = vec![true; limit + 1];
    let mut primes: Vec<usize> = Vec::new();
    for i in 2..=limit {
        if is_prime[i] {
            primes.push(i);
            mu[i] = -1;
        }
        for &p in &primes {
            if i * p > limit {
                break;
            }
            is_prime[i * p] = false;
            if i % p == 0 {
                mu[i * p] = 0;
                break;
            } else {
                mu[i * p] = -mu[i];
            }
        }
    }
    mu
}

fn main() {
    let out = "tools/wave8c/results";
    fs::create_dir_all(out).unwrap();
    let mut log = String::new();

    let z = z_table_f64(32, 4);
    let zm = z_table_mpfr(32, 4);

    // ============ 1. VERIFICATION: closed forms vs independent quadrature ============
    log.push_str("=== VERIFICATION (closed form vs independent x-quadrature, m0=1e5) ===\n");
    let mut vok = true;
    for k in 1..=6u64 {
        let (bq, left) = b_quad(k, 100_000);
        let bc = b_f64(k);
        let rel = (bc - bq).abs() / bq.abs().max(1e-300);
        let ok = rel < 1e-4;
        vok &= ok;
        log.push_str(&format!(
            "b_{} = {:.12e} (closed) vs {:.12e} (quad, leftover {:.1e}) rel={:.1e} {}\n",
            k, bc, bq, left, rel, if ok { "OK" } else { "FAIL" }
        ));
    }
    for &(j, k) in &[(1u64, 1u64), (1, 2), (2, 3), (3, 5), (4, 7), (5, 8), (6, 7)] {
        let (gq, _left) = gram_quad(j, k, 100_000);
        let gc = gram_f64(j, k, &z);
        let gm = gram_mpfr(j, k, &zm).to_f64();
        let rel_q = (gc - gq).abs() / gq.abs().max(1e-300);
        let rel_m = (gc - gm).abs() / gm.abs().max(1e-300);
        let ok = rel_q < 1e-4 && rel_m < 1e-10;
        vok &= ok;
        log.push_str(&format!(
            "G_{},{} = {:.12e} (f64) quad {:.12e} rel_q={:.1e} mpfr rel_m={:.1e} {}\n",
            j, k, gc, gq, rel_q, rel_m, if ok { "OK" } else { "FAIL" }
        ));
    }
    let (g11, g12, g22) = (gram_f64(1, 1, &z), gram_f64(1, 2, &z), gram_f64(2, 2, &z));
    let pd = g11 * g22 - g12 * g12;
    log.push_str(&format!(
        "G11={:.10e} G12={:.10e} G22={:.10e} det2={:.3e} (must be >0) {}; d1={:.6e}\n",
        g11, g12, g22, pd, if pd > 0.0 { "OK" } else { "FAIL" },
        (1.0 - b_f64(1) * b_f64(1) / g11).max(0.0).sqrt()
    ));
    vok &= pd > 0.0;
    log.push_str(&format!("verification overall: {}\n\n", if vok { "PASS" } else { "FAIL" }));

    // ============ 2. d_N sweep (f64) ============
    let ns: Vec<usize> = vec![10, 20, 30, 50, 75, 100, 150, 200, 300, 400, 600, 800, 1000];
    log.push_str("=== d_N sweep (f64, Cholesky) ===\nN\td_N\td_N^2\td_N*sqrt(N)\tkappa_piv\n");
    let mut rows: Vec<(usize, f64, f64, f64, f64)> = Vec::new();
    for &n in &ns {
        let g = gram_matrix(n, &|i| (i as u64) + 1, &z);
        let b: Vec<f64> = (1..=n as u64).map(b_f64).collect();
        let t0 = std::time::Instant::now();
        let (_c, d2, ok, kp) = cholesky_solve_f64(&g, &b, n);
        let dt = t0.elapsed().as_secs_f64();
        let d = d2.max(0.0).sqrt();
        let dn = d * (n as f64).sqrt();
        log.push_str(&format!(
            "{}\t{:.10e}\t{:.4e}\t{:.6e}\t{:.1e} (solve {:.1}s, cholesky {})\n",
            n, d, d2, dn, kp, dt, if ok { "ok" } else { "FAILED" }
        ));
        eprintln!("N={} d_N={:.6e} sqrtN*d={:.6e} kappa~{:.1e} t={:.1}s", n, d, dn, kp, dt);
        rows.push((n, d, d2, dn, kp));
    }
    let last = &rows[rows.len() - 4..];
    let mut sx = 0.0;
    let mut sy = 0.0;
    let mut sxx = 0.0;
    let mut sxy = 0.0;
    for &(n, d, _, _, _) in last {
        let x = (n as f64).ln();
        let y = d.ln();
        sx += x;
        sy += y;
        sxx += x * x;
        sxy += x * y;
    }
    let m = last.len() as f64;
    let slope = (m * sxy - sx * sy) / (m * sxx - sx * sx);
    log.push_str(&format!(
        "\nlog-log slope of d_N (last 4 pts N={}..{}): {:.4}  (d_N ~ N^{:.4})\n",
        last[0].0, last[last.len() - 1].0, slope, slope
    ));
    eprintln!("slope = {:.4}", slope);

    // ============ 3. MPFR cross-check ============
    log.push_str("\n=== MPFR (256-bit) cross-check ===\n");
    for &n in &[50usize, 100, 251, 500] {
        let mut g = vec![Float::with_val(256, 0); n * n];
        for i in 0..n {
            for k in 0..n {
                g[i * n + k] = gram_mpfr((i as u64) + 1, (k as u64) + 1, &zm);
            }
        }
        let b: Vec<Float> = (1..=n as u64).map(b_mpfr).collect();
        let (_c0, d2m) = cholesky_solve_mpfr(&g, &b, n);
        let dm = d2m.to_f64().max(0.0).sqrt();
        let gf = gram_matrix(n, &|i| (i as u64) + 1, &z);
        let bf: Vec<f64> = (1..=n as u64).map(b_f64).collect();
        let (_, d2f, _, _) = cholesky_solve_f64(&gf, &bf, n);
        let df = d2f.max(0.0).sqrt();
        let rel = (dm - df).abs() / dm.max(1e-300);
        log.push_str(&format!("N={}: d_mpfr={:.10e} d_f64={:.10e} rel={:.1e}\n", n, dm, df, rel));
        eprintln!("MPFR N={} d={:.6e} vs f64 {:.6e} rel {:.1e}", n, dm, df, rel);
    }

    // ============ 4. optimal coefficients (N=1000) ============
    let n = 1000usize;
    let g = gram_matrix(n, &|i| (i as u64) + 1, &z);
    let b: Vec<f64> = (1..=n as u64).map(b_f64).collect();
    let (c, d2, _ok, _kp) = cholesky_solve_f64(&g, &b, n);
    let mu = mobius_sieve(200);
    let mut agree = 0i64;
    let mut sq = 0i64;
    for k in 1..=200usize {
        if mu[k] != 0 {
            sq += 1;
            if (c[k - 1].is_sign_positive()) == (mu[k] > 0) {
                agree += 1;
            }
        }
    }
    let neg = c.iter().filter(|x| x.is_sign_negative()).count();
    let sumc: f64 = c.iter().sum();
    let mass_low: f64 = c.iter().take(n / 2).map(|x| x.abs()).sum();
    let mass_all: f64 = c.iter().map(|x| x.abs()).sum();
    let mut cl = String::new();
    for k in 0..30 {
        cl.push_str(&format!("{:.4e} ", c[k]));
    }
    log.push_str(&format!(
        "\n=== optimal coefficients N=1000 ===\nc_1={:.6e} c_10={:.6e} c_100={:.6e} c_500={:.6e} c_N={:.6e}\n",
        c[0], c[9], c[99], c[499], c[999]
    ));
    log.push_str(&format!(
        "sign-correlation with mu(k) for squarefree k<=200: {}/{} = {:.3}\n",
        agree, sq, agree as f64 / sq as f64
    ));
    log.push_str(&format!(
        "negatives: {} of {}; sum(c)={:.4e}; mass(k<=N/2)/mass(all)={:.4}; d_N={:.6e}\n",
        neg, n, sumc, mass_low / mass_all, d2.max(0.0).sqrt()
    ));
    log.push_str(&format!("first 30 c_k: {}\n", cl));
    log.push_str(&format!(
        "sample c_k at k=1..10: {}\n",
        (0..10).map(|k| format!("{:.4e}", c[k])).collect::<Vec<_>>().join(" ")
    ));

    // ============ 5. CONTROLS ============
    log.push_str("\n=== CONTROL: powers of 2 (expect SATURATION: d' not -> 0) ===\n");
    for m in 2..=14usize {
        let idx = |i: usize| 1u64 << i;
        let g = gram_matrix(m + 1, &idx, &z);
        let b: Vec<f64> = (0..=m as u64).map(|i| b_f64(1u64 << i)).collect();
        let (_c, d2, ok, kp) = cholesky_solve_f64(&g, &b, m + 1);
        let d = d2.max(0.0).sqrt();
        log.push_str(&format!(
            "pow2 up to 2^{}: N={} d'={:.6e} kappa~{:.1e} cholesky {}\n",
            m, m + 1, d, kp, if ok { "ok" } else { "FAIL" }
        ));
        eprintln!("CONTROL pow2 m={} d'={:.6e}", m, d);
    }
    log.push_str("\n=== CONTROL: squares {1/(k^2 x)} (same machinery, idx=k^2) ===\n");
    for &n in &[10usize, 20, 30, 40] {
        let idx = |i: usize| ((i as u64) + 1) * ((i as u64) + 1);
        let g = gram_matrix(n, &idx, &z);
        let b: Vec<f64> = (1..=n as u64).map(|k| b_f64(k * k)).collect();
        let (_c, d2, ok, kp) = cholesky_solve_f64(&g, &b, n);
        let d = d2.max(0.0).sqrt();
        log.push_str(&format!(
            "squares N={}: d''={:.6e} kappa~{:.1e} cholesky {}\n",
            n, d, kp, if ok { "ok" } else { "FAIL" }
        ));
        eprintln!("CONTROL squares N={} d''={:.6e}", n, d);
    }

    fs::write(format!("{}/wave8c_results.txt", out), &log).unwrap();
    println!("{}", log);
    println!("results written to {}/wave8c_results.txt", out);
}

