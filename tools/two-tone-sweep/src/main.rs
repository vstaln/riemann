// two-tone — explore two-tone window functions v(s) = cos(a*s) + c*cos(b*s)
// on [-1/2, 1/2].  Computes the window functional H via numerically-integrated
// I0 = int v ds, I2 = int v^2 ds, J = int int |s-t| v(s) v(t) ds dt (kink-split),
// then bound = (H - tau)/(1 - B/m) with A = eps*(m-6),
// B = A if A<=m/(m-1) else 2*sqrt((m-1)*A/m) - 1 + A/m, tau = psum*(m-6)/m.
//
// CONVENTION (matches the certified record scripts final_leader.py / verify_H.py):
//   I0 = int v ds ,  I2 = int v^2 ds ,  c = I0^2/(I2+J) ,  H = 2 - 1/c
// The task prose labels these I0/I2 differently, but its own check formula
// 1/2 + sin(alpha)/(2 alpha) == int cos^2(alpha s) ds proves I2 = int v^2.
// The validation mode also computes the literal-prose reading and reports which
// reproduces the reference H(1.49) = 0.6724218860964.
//
// Two-tone structure: v = cos(a s) + c cos(b s), so
//   I0 = A0 + c B0
//   I2 = A2 + 2c X2 + c^2 B2
//   J  = Jaa + 2c Jab + c^2 Jbb        (bilinear in the cosine pair kernel)
// where the pair kernels Juv = int int |s-t| cos(u s) cos(v t) are computed ONCE
// per (a,b) by kink-split Gauss-Legendre; the c-loop is then O(1) per c.
//
// Build:  export PATH=$HOME/.cargo/bin:$PATH
//         export RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes"
//         cargo build --release --target x86_64-unknown-linux-musl
// Run:    ./target/x86_64-unknown-linux-musl/release/two-tone            (sweep)
//         ./target/x86_64-unknown-linux-musl/release/two-tone validate
//         ./target/x86_64-unknown-linux-musl/release/two-tone single <a> <b> <c> <psum> <m> <eps>

const L: f64 = 0.5;                // domain [-L, L]
const EPS_DEFAULT: f64 = 0.00806;  // CONJECTURED achievable eps (record-level ~0.008)

// ---------- Gauss-Legendre nodes/weights on [-1,1], order n ----------
fn gauss_legendre(n: usize) -> (Vec<f64>, Vec<f64>) {
    let mut x = vec![0.0; n];
    let mut w = vec![0.0; n];
    let m = (n + 1) / 2;
    for i in 0..m {
        let mut t = (std::f64::consts::PI * (i as f64 + 0.75) / (n as f64 + 0.5)).cos();
        loop {
            let mut p0: f64 = 1.0;
            let mut p1: f64 = t;
            for k in 2..=n {
                let kf = k as f64;
                let p2 = ((2.0 * kf - 1.0) * t * p1 - (kf - 1.0) * p0) / kf;
                p0 = p1;
                p1 = p2;
            }
            let dp = n as f64 * (t * p1 - p0) / (t * t - 1.0);
            let dt = p1 / dp;
            t -= dt;
            if dt.abs() < 1e-15 { break; }
        }
        let mut p0: f64 = 1.0;
        let mut p1f: f64 = t;
        for k in 2..=n {
            let kf = k as f64;
            let p2 = ((2.0 * kf - 1.0) * t * p1f - (kf - 1.0) * p0) / kf;
            p0 = p1f;
            p1f = p2;
        }
        let dp = n as f64 * (t * p1f - p0) / (t * t - 1.0);
        x[i] = t;
        x[n - 1 - i] = -t;
        w[i] = 2.0 / ((1.0 - t * t) * dp * dp);
        w[n - 1 - i] = w[i];
    }
    (x, w)
}

fn v(s: f64, a: f64, b: f64, c: f64) -> f64 {
    (a * s).cos() + c * (b * s).cos()
}

// Pair kernel Juv = int_{-L}^{L} int_{-L}^{L} |s-t| cos(u s) cos(v t) ds dt
// kink-split: Juv = 2 * int_{-L}^{L} cos(v t) g(t) dt ,  g(t) = int_{t}^{L} (s-t) cos(u s) ds
// (g computed with Gauss-Legendre mapped to [t, L]; outer with GL on [-L,L]).
fn j_cos(u: f64, v: f64, xg: &[f64], wg: &[f64]) -> f64 {
    let inner = |t: f64| -> f64 {
        let half = (L - t) * 0.5;
        let mut s = 0.0;
        for (i, &xi) in xg.iter().enumerate() {
            let sp = t + half * (xi + 1.0);
            s += wg[i] * (sp - t) * (u * sp).cos();
        }
        s * half
    };
    let mut s = 0.0;
    for (i, &xi) in xg.iter().enumerate() {
        let t = L * xi;
        s += wg[i] * (v * t).cos() * inner(t);
    }
    2.0 * s * L
}

// closed-form single-cosine pieces (cross-checks); k=0 = constant function 1
fn cosine_i0(a: f64) -> f64 {
    if a.abs() < 1e-12 { 1.0 } else { 2.0 * (a * 0.5).sin() / a }
}
fn cosine_i2(a: f64) -> f64 {
    if a.abs() < 1e-12 { 1.0 } else { 0.5 + a.sin() / (2.0 * a) }
}
fn cosine_j(a: f64) -> f64 {
    let alpha = a;
    let i2 = cosine_i2(alpha);
    let i0 = cosine_i0(alpha);
    let constant = (alpha * 0.5).sin() / alpha + 2.0 * (alpha * 0.5).cos() / (alpha * alpha);
    -2.0 * i2 / (alpha * alpha) + constant * i0
}

fn h_from(i0: f64, i2: f64, j: f64) -> f64 {
    let c = i0 * i0 / (i2 + j);
    2.0 - 1.0 / c
}

fn bound(eps: f64, m: usize, h: f64, psum: f64) -> f64 {
    let a = eps * (m as f64 - 6.0);
    let thr = m as f64 / (m as f64 - 1.0);
    let b = if a <= thr { a } else { 2.0 * ((m as f64 - 1.0) * a / m as f64).sqrt() - 1.0 + a / m as f64 };
    let tau = psum * (m as f64 - 6.0) / m as f64;
    (h - tau) / (1.0 - b / m as f64)
}

fn main() {
    let record = 0.6732628655343560_f64;
    let args: Vec<String> = std::env::args().collect();
    let mode = args.get(1).map(|s| s.as_str()).unwrap_or("sweep");

    let (xg, wg) = gauss_legendre(96);
    let (xg32, wg32) = gauss_legendre(48);

    match mode {
        "validate" => {
            println!("== validation ==");
            // 1) cosine cross-check: numeric kink-split vs closed form, c=0 case
            for &alpha in &[1.47, 1.49, 1.5] {
                let (i0n, i2n, jn) = (cosine_i0(alpha), cosine_i2(alpha), j_cos(alpha, alpha, &xg, &wg));
                let j_an = cosine_j(alpha);
                let h_num = h_from(i0n, i2n, jn);
                let h_an = h_from(i0n, i2n, j_an);
                println!("cos alpha={}: I0={:.12} I2={:.12} J_num={:.12} J_an={:.12} dJ={:.3e} | H_num={:.12} H_an={:.12} dH={:.3e}",
                    alpha, i0n, i2n, jn, j_an, (jn - j_an).abs(), h_num, h_an, (h_num - h_an).abs());
            }
            // 2) reference: H(1.49) must equal 0.6724218860964
            let h149 = h_from(cosine_i0(1.49), cosine_i2(1.49), j_cos(1.49, 1.49, &xg, &wg));
            println!("H(1.49) numeric = {:.13}  reference = 0.6724218860964  diff={:.3e}",
                h149, (h149 - 0.6724218860964).abs());
            // 3) the literal-prose reading (I0=int v^2, I2=int v^2 s^2) — documented, not used
            let i0p = integrate_l(&|s| v(s, 1.49, 0.0, 0.0).powi(2), &xg, &wg);
            let i2p = integrate_l(&|s| v(s, 1.49, 0.0, 0.0).powi(2) * s * s, &xg, &wg);
            let jp = j_cos(1.49, 1.49, &xg, &wg);
            let h_prose = h_from(i0p, i2p, jp);
            println!("[prose reading] I0=∫v^2={:.12} I2=∫v^2 s^2={:.12} -> H={:.12} (does NOT match reference; prose labels shifted)",
                i0p, i2p, h_prose);
            // 4) bound reproduction with certified inputs
            let b = bound(0.00806, 133, h149, 1.0 / 220.0);
            println!("bound(eps=0.00806, m=133, alpha=1.49, psum=1/220) = {:.16}  record = {:.16}  diff={:.3e}",
                b, record, (b - record).abs());
            // 5) resolution check: 96-pt vs 48-pt kink-split agree
            let h48 = h_from(cosine_i0(1.49), cosine_i2(1.49), j_cos(1.49, 1.49, &xg32, &wg32));
            println!("resolution: H(1.49) n=48 = {:.13}  diff(96 vs 48) = {:.3e}", h48, (h149 - h48).abs());
        }
        "cosmax" => {
            // dense scan of single-cosine H(alpha) over [0.5, 3.0]
            let mut best_h = f64::NEG_INFINITY;
            let mut best_a = 0.0;
            for ia in 0..5001 {
                let a = 0.5 + 2.5 * ia as f64 / 5000.0;
                let h = h_from(cosine_i0(a), cosine_i2(a), j_cos(a, a, &xg, &wg));
                if h > best_h { best_h = h; best_a = a; }
            }
            // refine around best_a
            for ia in 0..10001 {
                let a = (best_a - 0.01) + 0.02 * ia as f64 / 10000.0;
                let h = h_from(cosine_i0(a), cosine_i2(a), j_cos(a, a, &xg, &wg));
                if h > best_h { best_h = h; best_a = a; }
            }
            let classic = 1.5 - (1.0 / 2.0f64.sqrt()) * (1.0 / 2.0f64.sqrt()).tan().recip();
            println!("max H_cos over alpha = {:.15} at alpha = {:.9}", best_h, best_a);
            println!("classic 3/2 - (1/sqrt2)cot(1/sqrt2) = {:.15}", classic);
            println!("excess over classic = {:.3e}", best_h - classic);
        }
        "fine" => {
            // fine two-tone scan around the optimum: a in [1.40,1.42], b in [2.50,2.56],
            // c in [-0.02,0.02] — does c != 0 push H above the pure-cosine max?
            let (am, ax) = (1.4000f64, 1.4200f64);
            let (bm, bx) = (2.5000f64, 2.5600f64);
            let (cm, cx) = (-0.0200f64, 0.0200f64);
            let (na, nb, nc) = (201usize, 201usize, 401usize);
            let mut best: Vec<(f64, f64, f64, f64)> = Vec::new();
            for ia in 0..na {
                let a = am + (ax - am) * ia as f64 / (na - 1) as f64;
                for ib in 0..nb {
                    let b = bm + (bx - bm) * ib as f64 / (nb - 1) as f64;
                    let jaa = j_cos(a, a, &xg, &wg);
                    let jab = j_cos(a, b, &xg, &wg);
                    let jbb = j_cos(b, b, &xg, &wg);
                    for ic in 0..nc {
                        let c = cm + (cx - cm) * ic as f64 / (nc - 1) as f64;
                        let i0 = cosine_i0(a) + c * cosine_i0(b);
                        let i2 = cosine_i2(a) + 2.0 * c * cross2(a, b) + c * c * cosine_i2(b);
                        let j = jaa + 2.0 * c * jab + c * c * jbb;
                        let h = h_from(i0, i2, j);
                        if best.len() < 10 {
                            best.push((h, a, b, c));
                        } else if h > best[9].0 {
                            best[9] = (h, a, b, c);
                        }
                        if best.len() == 10 { best.sort_by(|x, y| y.0.partial_cmp(&x.0).unwrap()); }
                    }
                }
            }
            best.sort_by(|x, y| y.0.partial_cmp(&x.0).unwrap());
            println!("fine scan around optimum — top 10 by H:");
            for &(h, a, b, c) in best.iter() {
                println!("  H={:.15} a={:.5} b={:.5} c={:+.5}", h, a, b, c);
            }
        }
        "wide" => {
            // coarse wide scan: a in [0.5,3.0], b in [0,6.0], c in [-1,1]
            // (b=0 = constant offset mode cos(a s)+c; large b = fast oscillation)
            let (am, ax) = (0.5f64, 3.0f64);
            let (bm, bx) = (0.0f64, 6.0f64);
            let (cm, cx) = (-1.0f64, 1.0f64);
            let (na, nb, nc) = (101usize, 121usize, 81usize);
            let mut best: Vec<(f64, f64, f64, f64)> = Vec::new();
            let mut n = 0usize;
            for ia in 0..na {
                let a = am + (ax - am) * ia as f64 / (na - 1) as f64;
                for ib in 0..nb {
                    let b = bm + (bx - bm) * ib as f64 / (nb - 1) as f64;
                    let jaa = j_cos(a, a, &xg, &wg);
                    let jab = j_cos(a, b, &xg, &wg);
                    let jbb = j_cos(b, b, &xg, &wg);
                    for ic in 0..nc {
                        let c = cm + (cx - cm) * ic as f64 / (nc - 1) as f64;
                        let i0 = cosine_i0(a) + c * cosine_i0(b);
                        let i2 = cosine_i2(a) + 2.0 * c * cross2(a, b) + c * c * cosine_i2(b);
                        let j = jaa + 2.0 * c * jab + c * c * jbb;
                        let h = h_from(i0, i2, j);
                        n += 1;
                        if best.len() < 5 {
                            best.push((h, a, b, c));
                        } else if h > best[4].0 {
                            best[4] = (h, a, b, c);
                        }
                        if best.len() == 5 { best.sort_by(|x, y| y.0.partial_cmp(&x.0).unwrap()); }
                    }
                }
            }
            best.sort_by(|x, y| y.0.partial_cmp(&x.0).unwrap());
            println!("wide coarse scan ({n} configs) — top 5 by H:");
            for &(h, a, b, c) in best.iter() {
                println!("  H={:.15} a={:.4} b={:.4} c={:+.4}", h, a, b, c);
            }
        }
        "single" => {
            let a: f64 = args[2].parse().unwrap();
            let b: f64 = args[3].parse().unwrap();
            let c: f64 = args[4].parse().unwrap();
            let psum: f64 = args[5].parse().unwrap();
            let m: usize = args[6].parse().unwrap();
            let eps: f64 = args.get(7).and_then(|s| s.parse().ok()).unwrap_or(EPS_DEFAULT);
            let i0 = integrate_l(&|s| v(s, a, b, c), &xg, &wg);
            let i2 = integrate_l(&|s| v(s, a, b, c).powi(2), &xg, &wg);
            let j = j_cos(a, a, &xg, &wg) + 2.0 * c * j_cos(a, b, &xg, &wg) + c * c * j_cos(b, b, &xg, &wg);
            let h = h_from(i0, i2, j);
            let bd = bound(eps, m, h, psum);
            println!("a={} b={} c={} psum={} m={} eps={}", a, b, c, psum, m, eps);
            println!("I0={:.12} I2={:.12} J={:.12}", i0, i2, j);
            println!("H={:.12}  bound={:.16}  record={:.16}", h, bd, record);
        }
        _ => {
            // ---- the sweep ----
            println!("=== two-tone sweep ===");
            println!("grid: a in [1.4,1.6] (201), b in [2.5,3.5] (201), c in [-0.3,0.3] (121), psum in {{1/220,1/250,1/300}}, m in [100,200]");
            println!("eps assumed achievable = {:.6} (CONJECTURED; record-level ~0.008 — needs interval verifier)", EPS_DEFAULT);
            println!("record = {:.16}", record);
            let psums = [1.0 / 220.0, 1.0 / 250.0, 1.0 / 300.0];
            let n_a = 201usize;
            let n_b = 201usize;
            let n_c = 121usize;
            let n_m = 101usize;
            // top-10 fixed-size heap (sorted descending at end)
            let mut top: Vec<(f64, f64, f64, f64, f64, usize, f64)> = Vec::with_capacity(10);
            let mut max_h = f64::NEG_INFINITY;
            let mut max_h_cfg = (0.0, 0.0, 0.0);
            let mut n_cfg = 0usize;
            for ia in 0..n_a {
                let a = 1.4 + 0.2 * ia as f64 / (n_a - 1) as f64;
                for ib in 0..n_b {
                    let b = 2.5 + 1.0 * ib as f64 / (n_b - 1) as f64;
                    // pair kernels — O(1) per (a,b), then reuse across all c
                    let jaa = j_cos(a, a, &xg, &wg);
                    let jab = j_cos(a, b, &xg, &wg);
                    let jbb = j_cos(b, b, &xg, &wg);
                    for ic in 0..n_c {
                        let c = -0.3 + 0.6 * ic as f64 / (n_c - 1) as f64;
                        let i0 = cosine_i0(a) + c * cosine_i0(b);
                        let i2 = cosine_i2(a) + 2.0 * c * cross2(a, b) + c * c * cosine_i2(b);
                        let j = jaa + 2.0 * c * jab + c * c * jbb;
                        let h = h_from(i0, i2, j);
                        if h > max_h {
                            max_h = h;
                            max_h_cfg = (a, b, c);
                        }
                        for &psum in &psums {
                            for im in 0..n_m {
                                let m = 100 + im;
                                let bd = bound(EPS_DEFAULT, m, h, psum);
                                n_cfg += 1;
                                if top.len() < 10 {
                                    top.push((bd, a, b, c, psum, m, h));
                                } else if bd > top[9].0 {
                                    top[9] = (bd, a, b, c, psum, m, h);
                                }
                                // keep heap-ish: resort small array each push (n<=10)
                                if top.len() == 10 { top.sort_by(|x, y| y.0.partial_cmp(&x.0).unwrap()); }
                            }
                        }
                    }
                }
            }
            top.sort_by(|x, y| y.0.partial_cmp(&x.0).unwrap());
            println!("configs evaluated: {}", n_cfg);
            println!("MAX H over grid: H={:.12} at (a,b,c)=({:.4},{:.4},{:.4})", max_h, max_h_cfg.0, max_h_cfg.1, max_h_cfg.2);
            println!();
            println!("{:<4} {:<9} {:<9} {:<9} {:<9} {:<6} {:<15} {:<19}", "rank", "a", "b", "c", "psum", "m", "H", "bound");
            for (i, &(bd, a, b, c, psum, m, h)) in top.iter().enumerate() {
                println!("{:<4} {:<9.4} {:<9.4} {:<9.4} {:<9} {:<6} {:<15.12} {:<19.16} {}", i + 1, a, b, c, format!("1/{}", (1.0 / psum).round()), m, h, bd,
                    if bd > record { "> record" } else { "" });
            }
            if top.iter().all(|x| x.0 <= record) {
                println!("(none beats the record under the CONJECTURED eps model)");
            }
        }
    }
}

// int_{-L}^{L} f(s) ds via GL
fn integrate_l(f: &dyn Fn(f64) -> f64, xg: &[f64], wg: &[f64]) -> f64 {
    let mut s = 0.0;
    for (i, &t) in xg.iter().enumerate() {
        s += wg[i] * f(L * t);
    }
    s * L
}

// int_{-L}^{L} cos(a s) cos(b s) ds — closed form: cos(a s)cos(b s) = [cos((a-b)s)+cos((a+b)s)]/2,
// and int_{-L}^{L} cos(k s) ds = 2 sin(k/2)/k = sinc(k) with sinc(0) := 1 (a=b handled).
fn cross2(a: f64, b: f64) -> f64 {
    let sinc = |k: f64| -> f64 {
        if k.abs() < 1e-12 { 1.0 } else { (k * 0.5).sin() / (k * 0.5) }
    };
    0.5 * (sinc(a - b) + sinc(a + b))
}
