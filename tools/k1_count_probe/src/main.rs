// tools/k1_count_probe — Type-1 decision arithmetic for N(1/2+b/L,T) = o(T log T) at fixed b.
// (a) Fixed-b floor: a density bound N(sig_b,T) << T^{A(1/2-b/L)} (log T)^k has
//     ratio = N-bound/(T log T) = T^{A(1/2-b/L)-1} L^{k-1}. With A >= 2 (all known theorems;
//     A<2 at sigma=1/2 would prove almost-all-on-line, open): exponent >= 1-2b/L, so
//     ratio >= e^{-2b} L^{k-1} (times T^eps if A=2+eps). Certifies ONLY IF eps=0 AND k=0.
//     Every known theorem has eps>0 and k>=1 -> ratio -> oo. Count is beyond DH strength.
// (b) DH control: certified DH off-line distances (0.3085, 0.1508) vs the moving boundary b/L.
// (c) Crossover b*(T): minimal b with ratio < 1 for the near-line Ingham-type structure.
fn main() {
    // ---------- (a) fixed-b floor, with log power k ----------
    println!("== (a) fixed-b floor: ratio = T^(expo-1) * L^(k-1) at fixed b = 0.0758 ==");
    println!("    (certifies o(T log T) only if ratio -> 0)");
    let b = 0.0758_f64;
    for &(eps, k, tag) in &[
        (0.0_f64, 0.0_f64, "DH eps=0, k=0 (log-free: NOT known)"),
        (0.0, 1.0, "DH eps=0, k=1 (log power 1)"),
        (0.0, 2.0, "DH eps=0, k=2"),
        (0.0, 13.0, "DH eps=0, k=13 (Montgomery-class)"),
        (0.01, 2.0, "DH eps=0.01, k=2"),
        (0.1, 44.0, "DH eps=0.1, k=44 (Ingham-class)"),
    ] {
        let mut row = String::new();
        let mut last = 0.0_f64;
        for t10 in 4..=10 {
            let t = 10f64.powi(t10);
            let l = t.ln();
            let expo = (2.0 + eps) * (0.5 - b / l);
            let ratio = t.powf(expo - 1.0) * l.powf(k - 1.0);
            last = ratio;
            row.push_str(&format!(" 1e{t10}:{ratio:.1e}"));
        }
        println!("  {tag}:{row}  -> last {last:.1e}");
    }

    // ---------- (c) crossover b*(T): near-line Ingham-type N << T L^k (sigma-1/2)^(-k), k=5 ----------
    println!("\n== (c) crossover b*(T) for near-line Ingham-type N << T L^k (sigma-1/2)^(-k), k=5 ==");
    let k = 5.0_f64;
    for t10 in 4..=10 {
        let t = 10f64.powi(t10);
        let l = t.ln();
        // R = L^{2k-1} b^{-k} < 1  <=>  b > L^{(2k-1)/k}
        let bstar = l.powf((2.0 * k - 1.0) / k);
        println!("    T=1e{t10}: b*(T) = {bstar:.3}  (needs b growing, never fixed)");
    }

    // ---------- (b) DH control ----------
    println!("\n== (b) DH control: certified off-line distances vs moving boundary b/L ==");
    let dh = [0.3085_f64, 0.1508];
    for &b in &[0.0758_f64, 0.2237] {
        println!("  b = {b}:");
        for t10 in 2..=8 {
            let t = 10f64.powi(t10);
            let l = t.ln();
            let boundary = b / l;
            let beyond = dh.iter().filter(|d| **d > boundary).count();
            println!("    T=1e{t10}: b/L = {boundary:.4}  DH zeros beyond boundary: {beyond} (of {})",
                dh.len());
        }
    }
}
