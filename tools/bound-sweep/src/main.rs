// bound-sweep — Rust search over the certified-bound parameter space.
// Formula verified to reproduce the record 0.6732628655343560 exactly.
//   bound = (H - tau) / (1 - B/m), H = window functional, A = eps*(m-6),
//   B = A if A<=m/(m-1) else 2*sqrt((m-1)*A/m)-1+A/m, tau = psum*(m-6)/m
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
fn main() {
    let record = 0.6732628655343560_f64;
    let args: Vec<String> = std::env::args().collect();
    // Optional: alpha_min alpha_max alpha_steps psum_den_max
    let a_min: f64 = args.get(1).and_then(|s| s.parse().ok()).unwrap_or(1.40);
    let a_max: f64 = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(1.55);
    let a_steps: usize = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(100);
    let psum_max_den: usize = args.get(4).and_then(|s| s.parse().ok()).unwrap_or(400);
    println!("=== bound-sweep: alpha [{},{}] {} steps, psum in [1/400..1/150] ===", a_min, a_max, a_steps);
    println!("record: {:.16}", record);
    // The achievable eps depends on (alpha, psum) — certified values we know:
    //   alpha=1.49, psum=1/220 -> eps=0.00806 (the record)
    //   alpha=1.47, psum=1/320 -> eps=0.00577 (tawanerguo)
    // eps grows with psum and with alpha near 1.49; use a model eps(alpha,psum)
    // that interpolates these known points, then scan m.
    let mut best: Vec<(f64, f64, f64, usize, f64)> = Vec::new();
    for a_i in 0..=a_steps {
        let alpha = a_min + (a_max - a_min) * a_i as f64 / a_steps as f64;
        for pden in 150..=psum_max_den {
            let psum = 1.0 / pden as f64;
            // eps model: interpolate known certified points, scaled by pressure
            // (CONJECTURED model — the true eps needs the interval verifier)
            let eps_base = if (alpha - 1.49).abs() < 0.01 { 0.00806 } else if (alpha-1.47).abs() < 0.01 { 0.00577 } else { 0.006 + 0.002*(alpha-1.45) };
            let eps = eps_base * (psum * 220.0).sqrt().min(1.5); // pressure scaling
            for m in 60..=400 {
                let b = bound(eps, m, alpha, psum);
                if b > record { best.push((b, alpha, psum, m, eps)); }
            }
        }
    }
    best.sort_by(|x, y| y.0.partial_cmp(&x.0).unwrap());
    println!("candidates > record: {}", best.len());
    for (b, alpha, psum, m, eps) in best.iter().take(10) {
        println!("{:.16} alpha={:.4} psum=1/{} m={} eps={:.6}", b, alpha, (1.0/psum).round(), m, eps);
    }
    if best.is_empty() { println!("(none — record is at/near the ceiling for this model)"); }
}
