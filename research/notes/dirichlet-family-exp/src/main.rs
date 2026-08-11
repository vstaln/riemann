// dirichlet-family — numerics-first probe of Remark 7.2(iii): does the family
// average over even Dirichlet characters restore bandwidth-1 (kappa = 4/3 at
// lambda = 1, certificate 2/3) for the 67.25%-method HS-norm quantity?
//
// Subcommands:
//   chars q            — enumerate primitive even characters mod q (sanity)
//   phasecheck q       — verify Z_chi is (numerically) real on [0, tmax]
//   zeros q T          — find zeros of all primitive even chars in [T-D0, 2T+D0], cache
//   hsnorm q T         — per-character + family HS-norm ratios at lambda in {0.7,0.85,1.0}
//   qaspect q          — q-aspect run: T=(ln q)^2, zeros + family HS norm at lambda=1
//   ortho q T          — prime-side orthogonality experiment
//   all t|q            — run the full suite
// Data is cached under DATA_DIR (default ./data).

mod characters;
mod em;
mod hsnorm;
mod ortho;

use std::collections::HashMap;
use std::path::PathBuf;

fn data_dir() -> PathBuf {
    PathBuf::from(std::env::var("DATA_DIR").unwrap_or_else(|_| "data".into()))
}

fn cache_path(q: u32, t1: f64, t2: f64, char_idx: usize) -> PathBuf {
    data_dir().join(format!("zeros_q{}_c{}_t{}_{}.txt", q, char_idx, t1 as i64, t2 as i64))
}

fn load_or_compute_zeros(
    q: u32,
    chi: &characters::Character,
    t0: f64,
    t1: f64,
    char_idx: usize,
) -> Vec<f64> {
    let path = cache_path(q, t0, t1, char_idx);
    if let Ok(s) = std::fs::read_to_string(&path) {
        let mut v: Vec<f64> = s
            .lines()
            .filter_map(|l| l.trim().parse::<f64>().ok())
            .collect();
        v.sort_by(|a, b| a.partial_cmp(b).unwrap());
        return v;
    }
    let zeros = em::find_zeros(t0, t1, chi);
    std::fs::create_dir_all(data_dir()).ok();
    let mut s = String::new();
    for z in &zeros {
        s.push_str(&format!("{:.12}\n", z));
    }
    std::fs::write(&path, s).ok();
    zeros
}

fn primitive_even_chars(q: u32) -> Vec<characters::Character> {
    let all = characters::all_characters(q);
    all.into_iter().filter(|c| c.conductor == q && c.even).collect()
}

fn print_chars(q: u32) {
    let all = characters::all_characters(q);
    println!("q={}  phi={}  total chars={}", q, characters::euler_phi(q), all.len());
    let mut counts: HashMap<u32, usize> = HashMap::new();
    for c in &all {
        *counts.entry(c.conductor).or_insert(0) += 1;
    }
    let mut cs: Vec<_> = counts.into_iter().collect();
    cs.sort();
    for (cond, n) in cs {
        println!("  conductor {}: {} chars", cond, n);
    }
    let pe = primitive_even_chars(q);
    println!("  primitive even: {}", pe.len());
    for c in &pe {
        let (gr, gi) = c.gauss_sum;
        println!(
            "    cond={} even tau={:+.6}{:+.6}i",
            c.conductor, gr, gi
        );
    }
}

fn phasecheck(q: u32) {
    let pe = primitive_even_chars(q);
    println!("phasecheck q={}: {} primitive even chars", q, pe.len());
    for chi in &pe {
        let worst = em::phase_selfcheck(chi, 4000.0);
        println!(
            "  chi cond={} even: max |Im Z|/|L| = {:.2e}  (should be < 1e-6)",
            chi.conductor, worst
        );
    }
}

fn zeros_cmd(q: u32, t: f64) {
    let d0 = 2.0 * t.sqrt();
    let pe = primitive_even_chars(q);
    println!(
        "zeros q={} T={} D0={}: {} primitive even chars, range [{}, {}]",
        q, t, d0, pe.len(), t - d0, 2.0 * t + d0
    );
    let counts: Vec<(u32, usize)> = std::thread::scope(|s| {
        let handles: Vec<_> = pe
            .iter()
            .enumerate()
            .map(|(ci, chi)| {
                s.spawn(move || {
                    let z = load_or_compute_zeros(q, chi, t - d0, 2.0 * t + d0, ci);
                    (chi.conductor, z.len())
                })
            })
            .collect();
        handles.into_iter().map(|h| h.join().unwrap()).collect()
    });
    let mut total = 0usize;
    let main = hsnorm::rvm_main(q, t - d0, 2.0 * t + d0);
    for (cond, n) in &counts {
        total += n;
        let err = (*n as f64 - main).abs();
        println!(
            "  chi cond={} even: {} zeros in range, RvM main {:.0}, |diff|={:.1} ({:.2}%)",
            cond, n, main, err, 100.0 * err / main.max(1.0)
        );
    }
    println!("  total zeros: {}", total);
}

/// Per-character and family-averaged HS-norm ratios over an explicit character list.
fn per_char_results_for(
    chars: &[characters::Character],
    q: u32,
    t: f64,
    d0: f64,
    win: &hsnorm::Window,
    rv: f64,
    rp: f64,
) -> Vec<(usize, f64, f64)> {
    // (n_zeros, tr bG, tr bG^2) per character, in parallel.
    std::thread::scope(|s| {
        let handles: Vec<_> = chars
            .iter()
            .enumerate()
            .map(|(ci, chi)| {
                s.spawn(move || {
                    let z = load_or_compute_zeros(q, chi, t - d0, 2.0 * t + d0, ci);
                    let (tr_g, tr2_g, _kappa, _c) = hsnorm::hs_from_zeros(&z, win, t, rv, rp);
                    let norm = win.a * win.L * win.L;
                    (z.len(), tr_g / norm, tr2_g / (norm * norm))
                })
            })
            .collect();
        handles.into_iter().map(|h| h.join().unwrap()).collect()
    })
}

/// Per-character and family-averaged HS-norm ratios over all primitive even chars mod q.
fn per_char_results(
    q: u32,
    t: f64,
    d0: f64,
    win: &hsnorm::Window,
    rv: f64,
    rp: f64,
) -> Vec<(usize, f64, f64)> {
    let pe = primitive_even_chars(q);
    per_char_results_for(&pe, q, t, d0, win, rv, rp)
}

fn hsnorm_cmd(q: u32, t: f64, lams: &[f64], d0_scale: f64, rv: f64, rp: f64) {
    let d0 = d0_scale * t.sqrt();
    let pe = primitive_even_chars(q);
    println!(
        "hsnorm q={} T={} D0={} eta=0.1: {} primitive even chars",
        q, t, d0, pe.len()
    );
    for &lam in lams {
        let win = hsnorm::window(q, t, lam, 0.1);
        println!(
            "  lambda={}: L={:.3}, d={}, X=e^L={:.0}, a={:.4}, b={:.4}",
            lam, win.L, win.d, win.x, win.a, win.b
        );
        let rows = per_char_results(q, t, d0, &win, rv, rp);
        let mut sum_tr = 0.0;
        let mut sum_tr2 = 0.0;
        let mut sum_n = 0.0;
        let mut kappas = Vec::new();
        let mut cs = Vec::new();
        for (n, tr_bg, tr2_bg) in &rows {
            if *tr_bg <= 0.0 {
                continue;
            }
            sum_tr += tr_bg;
            sum_tr2 += tr2_bg;
            sum_n += *n as f64;
            let kappa = tr2_bg / tr_bg;
            let c = tr_bg * tr_bg / tr2_bg;
            kappas.push(kappa);
            cs.push(c);
        }
        let kappa_f = sum_tr2 / sum_tr;
        let c_f = sum_tr * sum_tr / sum_tr2;
        // predictions
        let (kp, cn) = hsnorm::prediction(&win, q);
        let asym_kappa = 1.0 / lam + lam / 3.0;
        let asym_c = lam / (1.0 + lam * lam / 3.0);
        kappas.sort_by(|a, b| a.partial_cmp(b).unwrap());
        cs.sort_by(|a, b| a.partial_cmp(b).unwrap());
        let med = |v: &[f64]| v[v.len() / 2];
        println!(
            "    per-char kappa: min={:.4} med={:.4} max={:.4}",
            kappas[0],
            med(&kappas),
            kappas[kappas.len() - 1]
        );
        println!(
            "    FAMILY: kappa_F = {:.4}  (pred taper {:.4}, asymptotic {:.4});  C_F/N = {:.4}  (pred {:.4}, asym {:.4})",
            kappa_f, kp, asym_kappa, c_f / sum_n, cn, asym_c
        );
        println!(
            "    certificate H = 2 - kappa_F = {:.4}  (asymptotic 2/3 = {:.4})",
            2.0 - kappa_f,
            2.0 - asym_kappa
        );
    }
}

fn qaspect_cmd(q: u32) {    let t = ((q as f64).ln()).powi(2).ceil();
    println!(
        "\n=== q-aspect: q={} T=(ln q)^2={} ===",
        q, t
    );
    let d0 = t.sqrt();
    let pe = primitive_even_chars(q);
    println!("primitive even chars: {}", pe.len());
    let ell = (q as f64 * t / std::f64::consts::TAU).ln() + 2.0 * (2.0f64).ln() - 1.0;
    // legality numbers
    let lam_f = (q as f64).powf(0.99).ln() / ell;
    let lam_single = t.powf(0.99).ln() / ell;
    println!(
        "  ell = {:.3};  legal lambda (family, X<=q^0.99): {:.3};  legal lambda (single, X<=T^0.99): {:.3}",
        ell, lam_f, lam_single
    );
    for &lam in &[0.6, 0.7, 0.85, 1.0] {
        let win = hsnorm::window(q, t, lam, 0.1);
        if win.d == 0 {
            println!("  lambda={}: d=0 (window too small) — skip", lam);
            continue;
        }
        let rows = per_char_results(q, t, d0, &win, 8.0, 2.0);
        let mut sum_tr = 0.0;
        let mut sum_tr2 = 0.0;
        let mut sum_n = 0.0;
        let mut kappas = Vec::new();
        for (n, tr_bg, tr2_bg) in &rows {
            if *tr_bg <= 0.0 {
                continue;
            }
            sum_tr += tr_bg;
            sum_tr2 += tr2_bg;
            sum_n += *n as f64;
            kappas.push(tr2_bg / tr_bg);
        }
        let kappa_f = sum_tr2 / sum_tr;
        let c_f = sum_tr * sum_tr / sum_tr2;
        let asym = 1.0 / lam + lam / 3.0;
        kappas.sort_by(|a, b| a.partial_cmp(b).unwrap());
        let med = kappas[kappas.len() / 2];
        println!(
            "  lambda={}: N_total={} per-char-med kappa={:.3}  FAMILY kappa_F={:.3} (asym {:.3})  C_F/N={:.3} (asym {:.3})  H=2-kF={:.3}",
            lam, sum_n as usize, med, kappa_f, asym, c_f / sum_n, lam / (1.0 + lam * lam / 3.0), 2.0 - kappa_f
        );
    }
}

fn ortho_cmd(q: u32, t: f64) {
    let all = characters::all_characters(q);
    let all_even = characters::all_even(q);
    let pe = primitive_even_chars(q);
    println!(
        "\n=== orthogonality q={} T={}: all chars={}, all-even={}, primitive-even={} ===",
        q,
        t,
        all.len(),
        all_even.len(),
        pe.len()
    );
    let tau = t;
    let alphas = [0.3f64, 0.5, 0.7, 0.8, 0.9, 0.95, 0.99, 1.02, 1.1];
    println!(
        "  Q(X) = (1/|F|) sum_chi |sum_{{n<=X}} Lambda(n) chi(n) n^(-1/2-i tau)|^2, tau=T={}; D(X) = sum_{{n<=X,(n,q)=1}} Lambda(n)^2/n",
        tau
    );
    println!("    {:>7} {:>11} {:>11} {:>11} {:>11} {:>11}", "X", "D(X)", "Q_all/D", "Q_even/D", "Q_prim/D", "Q_single/D");
    for &a in &alphas {
        let x = (q as f64).powf(a);
        let d = ortho::q_diag(x, q);
        let qall = ortho::q_family(x, tau, &all) / d;
        let qeven = ortho::q_family(x, tau, &all_even) / d;
        let qprim = ortho::q_family(x, tau, &pe) / d;
        let single = pe.first().map(|c| ortho::q_single(x, tau, c) / d).unwrap_or(0.0);
        println!(
            "    {:7.2} {:11.3} {:11.4} {:11.4} {:11.4} {:11.4}",
            x, d, qall, qeven, qprim, single
        );
    }
}

/// q-aspect scaling run for prime q: T = (log q)^c, sample of even characters,
/// family HS-norm at the legal family bandwidth lambda_F and at the limit point
/// lambda = 1. D0 is chosen large enough for the pair sums (>= 1.2*rp*L at rp=2)
/// and the zero-finding window is [T-D0, 2T+D0].
fn qscale_cmd(q: u32, c: u32, nsample: usize) {
    assert!(q >= 5 && q % 2 == 1, "qscale needs an odd prime modulus");
    let lq = (q as f64).ln();
    let t = lq.powi(c as i32).ceil();
    let ell = (q as f64 * t / std::f64::consts::TAU).ln() + 2.0 * (2.0f64).ln() - 1.0;
    let lam_f = (q as f64).powf(0.99).ln() / ell;
    let lam_single = t.powf(0.99).ln() / ell;
    let l1 = hsnorm::window(q, t, 1.0, 0.1).L;
    let d0 = (2.0 * t.sqrt()).max(2.4 * l1);
    println!(
        "\n=== qscale q={} c={} T=(ln q)^{}={:.1} ===",
        q, c, c, t
    );
    println!(
        "  ell={:.3}  lambda_F (X<=q^0.99)={:.4}  lambda_single (X<=T^0.99)={:.4}  D0={:.1}  window=[{:.1},{:.1}]",
        ell, lam_f, lam_single, d0, t - d0, 2.0 * t + d0
    );
    let chars = characters::sample_even_prime(q, nsample);
    let klist: Vec<u32> = chars.iter().map(|(k, _)| *k).collect();
    let chis: Vec<characters::Character> = chars.into_iter().map(|(_, c)| c).collect();
    println!(
        "  sampled {} even (primitive) chars, k = {:?}",
        chis.len(),
        klist
    );
    // zero counts
    let counts: Vec<usize> = std::thread::scope(|s| {
        chis.iter()
            .enumerate()
            .map(|(ci, chi)| {
                s.spawn(move || load_or_compute_zeros(q, chi, t - d0, 2.0 * t + d0, ci).len())
            })
            .collect::<Vec<_>>()
            .into_iter()
            .map(|h| h.join().unwrap())
            .collect()
    });
    let main = hsnorm::rvm_main(q, t - d0, 2.0 * t + d0);
    let ntot: usize = counts.iter().sum();
    println!(
        "    total zeros over sample: {} (RvM main {:.0})",
        ntot, main
    );
    for (i, n) in counts.iter().enumerate() {
        println!(
            "    char[{}] (k={}): {} zeros, RvM main {:.0}, |diff|={:.1} ({:.2}%)",
            i,
            klist[i],
            n,
            main,
            (*n as f64 - main).abs(),
            100.0 * (*n as f64 - main).abs() / main.max(1.0)
        );
    }
    for &lam in &[lam_f, 1.0] {
        let win = hsnorm::window(q, t, lam, 0.1);
        if win.d == 0 {
            println!("  lambda={:.4}: d=0 — skip", lam);
            continue;
        }
        let rows = per_char_results_for(&chis, q, t, d0, &win, 6.0, 2.0);
        let mut sum_tr = 0.0;
        let mut sum_tr2 = 0.0;
        let mut sum_n = 0.0;
        let mut kappas = Vec::new();
        for (n, tr_bg, tr2_bg) in &rows {
            if *tr_bg <= 0.0 {
                continue;
            }
            sum_tr += tr_bg;
            sum_tr2 += tr2_bg;
            sum_n += *n as f64;
            kappas.push(tr2_bg / tr_bg);
        }
        let kappa_f = sum_tr2 / sum_tr;
        let c_f = sum_tr * sum_tr / sum_tr2;
        let (kp, cn) = hsnorm::prediction(&win, q);
        let asym_kappa = 1.0 / lam + lam / 3.0;
        let asym_c = lam / (1.0 + lam * lam / 3.0);
        kappas.sort_by(|a, b| a.partial_cmp(b).unwrap());
        let med = kappas[kappas.len() / 2];
        println!(
            "  lambda={:.4} (L={:.2}, d={}): N_total={} per-char-med kappa={:.4}  FAMILY kappa_F={:.4}  (taper-pred {:.4}, asym {:.4})",
            lam, win.L, win.d, sum_n as usize, med, kappa_f, kp, asym_kappa
        );
        println!(
            "      C_F/N={:.4} (pred {:.4}, asym {:.4});  H = 2-kappa_F = {:.4}  (asym 2-1/l-l/3 = {:.4})",
            c_f / sum_n, cn, asym_c, 2.0 - kappa_f, 2.0 - asym_kappa
        );
    }
    println!("  (family legal lambda lambda_F = {:.4}, single-char legal lambda = {:.4})", lam_f, lam_single);
}

/// Cross-check the direct prime construction against the full CRT enumeration.
fn qcross_cmd(q: u32) {
    assert!(q >= 5 && q % 2 == 1);
    let all = characters::all_characters(q);
    let g = characters::primitive_root_prime(q);
    let idx = characters::index_table_prime(q, g);
    let mut n_direct = 0;
    let mut mismatch = 0;
    for k in 0..(q - 1) {
        let dc = characters::character_prime(q, g, &idx, k);
        // find the matching character in `all` (same table)
        let same = all
            .iter()
            .find(|c| {
                (0..q).all(|a| {
                    (c.table[a as usize].0 - dc.table[a as usize].0).abs() < 1e-9
                        && (c.table[a as usize].1 - dc.table[a as usize].1).abs() < 1e-9
                })
            })
            .is_some();
        if !same {
            mismatch += 1;
        }
        if dc.even && k != 0 {
            n_direct += 1;
        }
    }
    let n_all = all.iter().filter(|c| c.even && c.conductor == q).count();
    println!(
        "qcross q={}: direct even non-principal chars = {}, CRT primitive-even = {}, table mismatches = {}",
        q, n_direct, n_all, mismatch
    );
    // spot check: gauss sums and orders for the sample
    for (k, c) in characters::sample_even_prime(q, 4) {
        let (gr, gi) = c.gauss_sum;
        println!(
            "  sample k={:>3} order={:>3} even={} |gauss|={:.6} (expect sqrt(q)={:.6})",
            k, c.order, c.even, (gr * gr + gi * gi).sqrt(), (q as f64).sqrt()
        );
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let cmd = args.get(1).map(|s| s.as_str()).unwrap_or("help");
    match cmd {
        "chars" => {
            let q: u32 = args[2].parse().unwrap();
            print_chars(q);
        }
        "phasecheck" => {
            let q: u32 = args[2].parse().unwrap();
            phasecheck(q);
        }
        "zeros" => {
            let q: u32 = args[2].parse().unwrap();
            let t: f64 = args[3].parse().unwrap();
            zeros_cmd(q, t);
        }
        "hsnorm" => {
            let q: u32 = args[2].parse().unwrap();
            let t: f64 = args[3].parse().unwrap();
            hsnorm_cmd(q, t, &[0.7, 0.85, 1.0], 2.0, 6.0, 2.0);
        }
        "qaspect" => {
            let q: u32 = args[2].parse().unwrap();
            qaspect_cmd(q);
        }
        "qscale" => {
            let q: u32 = args[2].parse().unwrap();
            let c: u32 = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(2);
            let ns: usize = args.get(4).and_then(|s| s.parse().ok()).unwrap_or(4);
            qscale_cmd(q, c, ns);
        }
        "qcross" => {
            let q: u32 = args[2].parse().unwrap();
            qcross_cmd(q);
        }
        "ortho" => {
            let q: u32 = args[2].parse().unwrap();
            let t: f64 = args[3].parse().unwrap();
            ortho_cmd(q, t);
        }
        "pool" => {
            // pooled family: union of primitive even chars over several moduli, lambda=1, T fixed
            let t: f64 = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(2000.0);
            let qs: Vec<u32> = args
                .get(3)
                .map(|s| s.split(',').filter_map(|x| x.parse().ok()).collect())
                .unwrap_or_else(|| vec![5, 7, 11, 13, 16, 20, 24, 40]);
            let d0 = 2.0 * t.sqrt();
            let win = hsnorm::window(40, t, 1.0, 0.1); // L depends on q; rebuilt per q below
            let mut sum_tr = 0.0f64;
            let mut sum_tr2 = 0.0f64;
            let mut sum_n = 0.0f64;
            let mut per_q = Vec::new();
            for &q in &qs {
                let win = hsnorm::window(q, t, 1.0, 0.1);
                let rows = per_char_results(q, t, d0, &win, 6.0, 2.0);
                let (mut s_tr, mut s_tr2, mut s_n) = (0.0, 0.0, 0.0);
                for (n, tr_bg, tr2_bg) in &rows {
                    s_tr += tr_bg;
                    s_tr2 += tr2_bg;
                    s_n += *n as f64;
                }
                sum_tr += s_tr;
                sum_tr2 += s_tr2;
                sum_n += s_n;
                per_q.push((q, s_n, s_tr2 / s_tr));
            }
            println!("pooled family (union over q={:?}, T={}, lambda=1):", qs, t);
            for (q, n, k) in &per_q {
                println!("  q={}: N={:.0} kappa_q={:.4}", q, n, k);
            }
            let kappa_pooled = sum_tr2 / sum_tr;
            println!(
                "  POOLED: N_total={:.0} kappa_pooled={:.4}  (asym 4/3 = {:.4})  H=2-kappa={:.4}  C/N={:.4}",
                sum_n, kappa_pooled, 4.0 / 3.0, 2.0 - kappa_pooled, sum_tr * sum_tr / (sum_tr2 * sum_n)
            );
        }
        "all" => {
            let mode = args.get(2).map(|s| s.as_str()).unwrap_or("t");
            if mode == "t" {
                for &q in &[5u32, 7, 11, 13, 16, 20, 24, 40] {
                    println!("\n########## q={} ##########", q);
                    print_chars(q);
                    phasecheck(q);
                    zeros_cmd(q, 2000.0);
                    hsnorm_cmd(q, 2000.0, &[0.7, 0.85, 1.0], 2.0, 6.0, 2.0);
                }
            } else if mode == "q" {
                for &q in &[40u32, 100, 200] {
                    qaspect_cmd(q);
                }
            } else if mode == "ortho" {
                for &q in &[40u32, 100, 200] {
                    let t = ((q as f64).ln()).powi(2).ceil();
                    ortho_cmd(q, t);
                }
                ortho_cmd(40, 2000.0);
            }
        }
        "debug" => {
            // convergence check: hs_from_zeros as a function of (rv, rp) on cached q=7 zeros
            let q = 7u32;
            let t: f64 = 2000.0;
            let d0 = 2.0 * t.sqrt();
            let pe = primitive_even_chars(q);
            let chi0 = &pe[0];
            let z = load_or_compute_zeros(q, chi0, t - d0, 2.0 * t + d0, 0);
            for lam in [0.7f64, 1.0] {
                let win = hsnorm::window(q, t, lam, 0.1);
                for (rv, rp) in [(3.0, 1.5), (6.0, 2.0), (10.0, 3.0), (15.0, 4.0)] {
                    let (tr_g, tr2_g, kappa, c) = hsnorm::hs_from_zeros(&z, &win, t, rv, rp);
                    let norm = win.a * win.L * win.L;
                    println!(
                        "conv lam={} rv={} rp={}: tr bG={:.3} kappa={:.5} C/N={:.5}",
                        lam,
                        rv,
                        rp,
                        tr_g / norm,
                        kappa,
                        c / (z.len() as f64)
                    );
                }
            }
            // orthogonality values for q=40
            let q40 = 40u32;
            let ae = characters::all_even(q40);
            println!("debug ortho: all-even chars={}", ae.len());
            for (n, m) in [(2u32, 3u32), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)] {
                println!("  ortho({},{})= {:.6}", n, m, ortho::orthogonality(n, m, &ae));
            }
            for chi in &ae {
                let qs = ortho::q_single(6.32, 2000.0, chi);
                println!(
                    "  chi(order={}, gs={:+.3}{:+.3}i): Q={:.6}",
                    chi.order, chi.gauss_sum.0, chi.gauss_sum.1, qs
                );
            }
            println!("  D(x) = {}", ortho::q_diag(6.32, q40));
            println!("  Q_family = {}", ortho::q_family(6.32, 2000.0, &ae));
            let win = hsnorm::window(40, 2000.0, 1.0, 0.1);
            println!(
                "debug: L={} a={} b={} b*L={} g(0)={} g(L/2)={} g(L*0.9)={}",
                win.L, win.a, win.b, win.b * win.L, hsnorm::g_of(0.0, &win), hsnorm::g_of(win.L / 2.0, &win), hsnorm::g_of(win.L * 0.9, &win)
            );
            println!("debug: J_T = {} (should be ~1/3)", hsnorm::j_t(&win, 40));
            println!("debug: pred kappa = {}  (asym {})", hsnorm::prediction(&win, 40).0, 1.0 + 1.0 / 3.0);
            let win2 = hsnorm::window(40, 2000.0, 0.85, 0.1);
            println!("debug lam=0.85: J_T = {}", hsnorm::j_t(&win2, 40));
        }
        _ => {
            println!(
                "subcommands: chars q | phasecheck q | zeros q T | hsnorm q T | qaspect q | ortho q T | pool [T] [qs] | all t|q|ortho"
            );
        }
    }
}
