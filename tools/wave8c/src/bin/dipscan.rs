// dipscan — pin the mechanism of the certified N=700 dip in the d_N flat law.
// Part B1: scan the 15 zero-pair beat cosines (gamma_i - gamma_j, i<j<=6), fixed-period single-cosine
//   fits of y = d_N*sqrt(ln N) - flat, on several windows; report per-pair amplitude, RMS, and the
//   RESIDUAL AT N=700 (the dip). A pair that LOCALIZES the dip leaves ~0 residual at N=700.
// Part B2: divisor-structure test at N=700 = 2^2*5^2*7 vs neighbors: d(n), sigma(n), summatory Sd(n).
// std-only. Usage: dipscan <datadir>

use std::f64::consts::PI;
use std::fs;

// first six non-trivial zeros of zeta (high precision)
const GAM: [f64; 6] = [
    14.13472514173469379045725198356247027078425711569924,
    21.02203963877155499262847959389690277733434052490278,
    25.010857580145688763213790992562821818659549672557996,
    30.4248761258595132103118975305840913201815600237154,
    32.9350615877391846905314471454761305854546261505234,
    37.5861781588256712571717634808284937090197838271928,
];

#[derive(Clone, Copy)]
struct Pt {
    x: f64,
    y: f64,
}

fn parse_dir(dir: &str) -> Vec<Pt> {
    let mut out: Vec<Pt> = Vec::new();
    let mut names: Vec<String> = Vec::new();
    if let Ok(rd) = fs::read_dir(dir) {
        for e in rd.flatten() {
            let n = e.file_name().to_string_lossy().to_string();
            if n.starts_with("prod_") && n.ends_with(".log") {
                names.push(n);
            }
        }
    }
    names.sort();
    for n in &names {
        let txt = fs::read_to_string(format!("{}/{}", dir, n)).unwrap_or_default();
        let mut ys = f64::NAN;
        for line in txt.lines() {
            if let Some(i) = line.find("d*sqrt(ln N)=") {
                let tail = &line[i + 13..];
                let val: f64 = tail
                    .split_whitespace()
                    .next()
                    .unwrap_or("")
                    .parse()
                    .ok()
                    .unwrap_or(f64::NAN);
                if val.is_finite() {
                    ys = val;
                }
            }
        }
        if ys.is_finite() {
            let nv: usize = n
                .trim_start_matches("prod_")
                .trim_end_matches(".log")
                .parse()
                .unwrap_or(0);
            out.push(Pt {
                x: (nv as f64).ln(),
                y: ys,
            });
        }
    }
    out
}

fn solve(m: usize, a: &mut [f64], b: &mut [f64]) -> Option<Vec<f64>> {
    for col in 0..m {
        let mut piv = col;
        let mut best = a[col * m + col].abs();
        for r in (col + 1)..m {
            if a[r * m + col].abs() > best {
                best = a[r * m + col].abs();
                piv = r;
            }
        }
        if best < 1e-14 {
            return None;
        }
        if piv != col {
            for c in 0..m {
                a.swap(col * m + c, piv * m + c);
            }
            b.swap(col, piv);
        }
        for r in (col + 1)..m {
            let f = a[r * m + col] / a[col * m + col];
            if f == 0.0 {
                continue;
            }
            for c in col..m {
                a[r * m + c] -= f * a[col * m + c];
            }
            b[r] -= f * b[col];
        }
    }
    let mut x = vec![0.0; m];
    for r in (0..m).rev() {
        let mut s = b[r];
        for c in (r + 1)..m {
            s -= a[r * m + c] * x[c];
        }
        x[r] = s / a[r * m + r];
    }
    Some(x)
}

fn linfit(data: &[Pt], w: f64) -> Option<(Vec<f64>, f64)> {
    let m = 3;
    let n = data.len();
    let mut ata = vec![0.0; m * m];
    let mut atb = vec![0.0; m];
    for p in data {
        let fi = [1.0, (w * p.x).cos(), (w * p.x).sin()];
        for j in 0..m {
            atb[j] += fi[j] * p.y;
            for k in 0..m {
                ata[j * m + k] += fi[j] * fi[k];
            }
        }
    }
    let x = solve(m, &mut ata, &mut atb)?;
    let mut s = 0.0;
    for p in data {
        let pred = x[0] + x[1] * (w * p.x).cos() + x[2] * (w * p.x).sin();
        let d = p.y - pred;
        s += d * d;
    }
    Some((x, (s / n as f64).sqrt()))
}

fn divisor_count(n: usize) -> usize {
    let mut c = 0;
    let mut i = 1;
    while i * i <= n {
        if n % i == 0 {
            c += 1;
            if i != n / i {
                c += 1;
            }
        }
        i += 1;
    }
    c
}

fn divisor_sum(n: usize) -> u64 {
    let mut s = 0u64;
    let mut i = 1usize;
    while i * i <= n {
        if n % i == 0 {
            s += i as u64;
            if i != n / i {
                s += (n / i) as u64;
            }
        }
        i += 1;
    }
    s
}

fn main() {
    let dir = std::env::args().nth(1).unwrap_or_else(|| "/tmp/osc".into());
    let data_all = parse_dir(&dir);
    if data_all.len() < 4 {
        eprintln!("only {} points parsed", data_all.len());
        std::process::exit(1);
    }
    println!("parsed {} points from {}", data_all.len(), dir);

    // windows: dip-local (N>=500), slow (N>=300), full
    for (wname, minn) in [("N>=500", 500usize), ("N>=300", 300), ("full", 0)] {
        let data: Vec<Pt> = data_all
            .iter()
            .filter(|p| p.x.exp() >= minn as f64 - 0.5)
            .cloned()
            .collect();
        let ymean: f64 = data.iter().map(|p| p.y).sum::<f64>() / data.len() as f64;
        let n = data.len() as f64;
        let rms0 = (data.iter().map(|p| (p.y - ymean) * (p.y - ymean)).sum::<f64>() / n).sqrt();
        println!(
            "\n==== window {} ({} pts), ymean={:.6}, RMS0(const)={:.6} ====",
            wname, data.len(), ymean, rms0
        );
        // the slow-fit baseline (beat) residual at 700 for reference:
        // 15 pairs
        let x700 = (700.0f64).ln();
        println!(
            "{:>3} {:>9} {:>8} {:>8} {:>9} {:>9} {:>9}",
            "pair", "P=2pi/dg", "Amp", "RMS", "RMS/M0", "resid@700", "RMS@700rel"
        );
        let mut best: (f64, usize, usize) = (f64::MAX, 0, 0);
        for i in 0..6 {
            for j in (i + 1)..6 {
                let dg = GAM[j] - GAM[i];
                let p = 2.0 * PI / dg;
                let w = dg; // frequency = gamma_j - gamma_i in log-units
                match linfit(&data, w) {
                    Some((x, r)) => {
                        let a = (x[1] * x[1] + x[2] * x[2]).sqrt();
                        let ph = (-x[2]).atan2(x[1]); // y = c + A cos(wx + phi)
                        let pred700 = x[0] + a * (w * x700 + ph).cos();
                        let y700 = data
                            .iter()
                            .find(|p| (p.x - x700).abs() < 1e-9)
                            .map(|p| p.y);
                        let resid = y700.map(|y| y - pred700).unwrap_or(f64::NAN);
                        let rrel = (r / rms0).max(1e-12);
                        println!(
                            "g{}-g{} {:>9.4} {:>8.6} {:>8.6} {:>9.3} {:>9.6} {:>9.2}",
                            i + 1,
                            j + 1,
                            p,
                            a,
                            r,
                            rrel,
                            resid,
                            resid.abs() / r
                        );
                        if r < best.0 {
                            best = (r, i, j);
                        }
                    }
                    None => println!("g{}-g{} singular", i + 1, j + 1),
                }
            }
        }
        let (br, bi, bj) = best;
        println!(
            "best-RMS pair: g{}-g{} P={:.4} RMS={:.6} (RMS/M0={:.3})",
            bi + 1,
            bj + 1,
            2.0 * PI / (GAM[bj] - GAM[bi]),
            br,
            br / rms0
        );
    }

    // ---- B2: divisor structure around 700 ----
    println!("\n==== B2 divisor structure near N=700 = 2^2*5^2*7 ====");
    println!("{:>5} {:>6} {:>10} {:>10}", "n", "d(n)", "sigma(n)", "sumd<=n");
    let mut running = 0u64;
    let start = 680usize;
    let end = 720usize;
    for n in 1..=end {
        running += divisor_count(n) as u64;
        if n >= start {
            println!(
                "{:>5} {:>6} {:>10} {:>10}",
                n,
                divisor_count(n),
                divisor_sum(n),
                running
            );
        }
    }
    // context: how anomalous is d(700)=18 in [680,720]? also factor 700, and a wider summatory slope
    let mut maxd = 0usize;
    let mut maxn = 0usize;
    for n in 680..=720 {
        let d = divisor_count(n);
        if d > maxd {
            maxd = d;
            maxn = n;
        }
    }
    println!("max d(n) in [680,720]: d({})={}", maxn, maxd);
    let mut dd: Vec<(usize, usize)> = (680..=720).map(|n| (n, divisor_count(n))).collect();
    dd.sort_by(|a, b| b.1.cmp(&a.1));
    println!("top-5 divisor counts in [680,720]: {:?}", dd[..5.min(dd.len())].to_vec());
    println!("700 factors: 2^2 * 5^2 * 7 ; d(700)=(2+1)(2+1)(1+1)=18; sigma(700)=(1+2+4)(1+5+25)(1+7)=1736");
}
