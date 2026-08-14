// Off-centre positivity probe, target (a): moving-boundary count N(1/2+b/L, T).
// Reads tools/argprinciple/data/lmfdb_zeros_*.txt (index, ordinate) pairs.
// Question: does the data show the predicted o(T log T) behaviour at b ~ 0.0758?
// Answer expected: VACUOUS -- the data stores no real parts (RH-assuming by construction),
// so the off-line count is identically 0 for every window.
use std::fs;

fn main() {
    let datadir = std::env::args().nth(1).unwrap_or_else(|| "tools/argprinciple/data".to_string());
    let b: f64 = 0.0758;

    let mut ord: Vec<f64> = Vec::new();
    let mut files: usize = 0;
    let rd = match fs::read_dir(&datadir) {
        Ok(r) => r,
        Err(e) => {
            eprintln!("cannot read {datadir}: {e}");
            std::process::exit(1);
        }
    };
    for ent in rd.flatten() {
        let name = ent.file_name().to_string_lossy().into_owned();
        if !name.starts_with("lmfdb_zeros_") || !name.ends_with(".txt") {
            continue;
        }
        files += 1;
        let txt = match fs::read_to_string(ent.path()) {
            Ok(t) => t,
            Err(_) => continue,
        };
        for line in txt.lines() {
            let mut it = line.split_whitespace();
            let _idx = it.next(); // index column: unused
            if let Some(v) = it.next() {
                if let Ok(x) = v.parse::<f64>() {
                    ord.push(x);
                }
            }
        }
    }
    ord.sort_by(|a, b| a.partial_cmp(b).unwrap());
    ord.dedup();
    let n = ord.len();
    if n == 0 {
        println!("no ordinates parsed");
        return;
    }
    let tmax = ord[n - 1];
    let l = |t: f64| (t / (2.0 * std::f64::consts::PI)).ln();
    let bnd = |t: f64| 0.5 + b / l(t);

    println!("files_parsed={}  total_ordinates={}", files, n);
    println!("t_min={:.6}  t_max={:.6}", ord[0], tmax);
    println!("moving boundary 1/2 + b/L(t), b={}:", b);
    for t in [1e3_f64, 1e4, 1e5, ord[0], tmax] {
        if t <= 0.0 || !t.is_finite() {
            continue;
        }
        println!(
            "  t={:.3e}  L=ln(t/2pi)={:.4}  boundary={:.6}",
            t,
            l(t),
            bnd(t)
        );
    }
    println!("real_part_column_stored: NONE (files hold index + ordinate only)");
    println!(
        "off_line_count(Re > 1/2 + b/L): 0  (identically, by data construction -> VACUOUS)"
    );
    let rvm = (tmax / (2.0 * std::f64::consts::PI)).ln() * tmax / (2.0 * std::f64::consts::PI);
    println!(
        "on_line N(1/2,Tmax)={}  vs (T/2pi)ln(T/2pi)={:.1}  ratio={:.6}  (Theta(T log T), NOT o)",
        n,
        rvm,
        n as f64 / rvm
    );
    println!("growing-window on-line counts (index-based; Theta(T log T) growth, never o):");
    let mut k: usize = 6;
    while (1u64 << k) as f64 <= tmax {
        let lo = (1u64 << k) as f64;
        let hi = (1u64 << (k + 1)) as f64;
        let c = ord.iter().filter(|&&g| g >= lo && g < hi).count();
        println!("  T in [{:>9.0}, {:>10.0}):  count={}", lo, hi, c);
        k += 1;
    }
    println!(
        "note: off-line count is 0 for EVERY window -> o(T log T) holds trivially but is untestable"
    );
}
