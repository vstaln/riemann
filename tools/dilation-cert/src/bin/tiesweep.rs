// tiesweep as above
fn h_window(alpha: f64) -> f64 {
    let a = alpha / 2.0;
    let i0 = 2.0 * a.sin() / alpha;
    let i2 = 0.5 + alpha.sin() / (2.0 * alpha);
    let constant = a.sin() / alpha + 2.0 * a.cos() / (alpha * alpha);
    let j = -2.0 * i2 / (alpha * alpha) + constant * i0;
    let c = i0 * i0 / (i2 + j);
    2.0 - 1.0 / c
}
fn bound(eps: f64, m: usize, alpha: f64, psum: f64) -> f64 {
    let h = h_window(alpha);
    let a = eps * (m as f64 - 6.0);
    let thr = m as f64 / (m as f64 - 1.0);
    let b = if a <= thr { a } else { 2.0 * ((m as f64 - 1.0) * a / m as f64).sqrt() - 1.0 + a / m as f64 };
    let tau = psum * (m as f64 - 6.0) / m as f64;
    (h - tau) / (1.0 - b / m as f64)
}
fn best_bound(eps: f64, alpha: f64, psum: f64) -> (f64, usize) {
    let mut bm = 0usize; let mut bb = f64::NEG_INFINITY;
    for m in 40..=400 { let b = bound(eps, m, alpha, psum); if b > bb { bb = b; bm = m; } }
    (bb, bm)
}
fn main() {
    const REC: f64 = 0.6734808616745137;
    let alpha = 1.464;
    let eps0 = 0.0062;
    println!("lambda | model floor eps=eps0*lam^0.83 | best m | bound(model) | tie-eps* (bisect) | margin");
    let mut lam = 1.00f64;
    while lam <= 1.35 + 1e-9 {
        let psum = (1.0f64/320.0) * lam;
        let epsm = eps0 * lam.powf(0.83);
        let (bmod, mm) = best_bound(epsm, alpha, psum);
        let (mut lo, mut hi) = (0.0040f64, 0.0090f64);
        for _ in 0..60 {
            let mid = (lo+hi)/2.0;
            let (b, _) = best_bound(mid, alpha, psum);
            if b < REC { lo = mid; } else { hi = mid; }
        }
        println!("{:.2}  | {:.6} | {:>3} | {:.12} | {:.6} | {:+.6}", lam, epsm, mm, bmod, (lo+hi)/2.0, epsm - (lo+hi)/2.0);
        lam += 0.05;
    }
}
