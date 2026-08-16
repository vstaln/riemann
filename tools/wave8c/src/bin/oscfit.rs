// oscfit v2 — fit oscillation structure of d_N*sqrt(ln N) vs x = ln N (std-only Rust).
// Usage: oscfit <datadir>   (reads <datadir>/prod_<N>.log RESULT lines)
// Approach: for a FIXED period P, model c + sum_j a_j*f_j(x) is LINEAR in params -> normal
// equations solved exactly. Only P is swept on a grid -> fast, no local-min traps.
// Models:
//   M0: y = c
//   M1: y = c + a1*cos(wx) + a2*sin(wx)                  (A = sqrt(a1^2+a2^2), phi = atan2(-a2,a1))
//   M2: y = c + a1*cos(w1x)+a2*sin(w1x)+a3*cos(w2x)+a4*sin(w2x)   (P1 = M1 best, sweep P2)
//   M3: y = c + (b1*cos(wx)+b2*sin(wx))/sqrt(x)           (explicit-formula 1/sqrt(x) amplitude)
// Probes: sign-agreement of (y-mean) vs cos(gamma*x+phi), phi swept.

use std::f64::consts::PI;
use std::fs;

const G1: f64 = 14.1347;
const G2: f64 = 21.0220;
const G3: f64 = 25.0109;

struct Pt {
    x: f64,
    y: f64,
}

fn parse_dir(dir: &str, minn: usize) -> Vec<Pt> {
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
            if nv >= minn {
                out.push(Pt {
                    x: (nv as f64).ln(),
                    y: ys,
                });
            }
        }
    }
    out
}

// solve A x = b (A: m x m, in row-major; partial pivoting). Returns Option<Vec<f64>>.
fn solve(m: usize, a: &mut [f64], b: &mut [f64]) -> Option<Vec<f64>> {
    for col in 0..m {
        // pivot
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

// generic linear least squares via normal equations: basis given as closures f(x).
fn linfit(data: &[Pt], m: usize, f: &dyn Fn(f64, usize) -> f64) -> (Vec<f64>, f64) {
    let n = data.len();
    let mut ata = vec![0.0; m * m];
    let mut atb = vec![0.0; m];
    for p in data {
        let mut fi = vec![0.0; m];
        for j in 0..m {
            fi[j] = f(p.x, j);
        }
        for j in 0..m {
            atb[j] += fi[j] * p.y;
            for k in 0..m {
                ata[j * m + k] += fi[j] * fi[k];
            }
        }
    }
    match solve(m, &mut ata, &mut atb) {
        Some(x) => {
            let mut s = 0.0;
            for p in data {
                let mut pred = 0.0;
                for (j, &xj) in x.iter().enumerate() {
                    pred += xj * f(p.x, j);
                }
                let d = p.y - pred;
                s += d * d;
            }
            (x, (s / n as f64).sqrt())
        }
        None => (vec![0.0; m], f64::MAX),
    }
}

// basis for model c + a1*cos(wx) + a2*sin(wx): f(x,0)=1, f(x,1)=cos(wx), f(x,2)=sin(wx)
fn basis_cos(w: f64) -> impl Fn(f64, usize) -> f64 {
    move |x, j| match j {
        0 => 1.0,
        1 => (w * x).cos(),
        _ => (w * x).sin(),
    }
}

// basis for model c + (b1*cos(wx) + b2*sin(wx))/sqrt(x)
fn basis_cos_sqrt(w: f64) -> impl Fn(f64, usize) -> f64 {
    move |x, j| match j {
        0 => 1.0,
        1 => (w * x).cos() / x.sqrt(),
        _ => (w * x).sin() / x.sqrt(),
    }
}

// basis for two-cosine model: 1, cos(w1x), sin(w1x), cos(w2x), sin(w2x)
fn basis_two(w1: f64, w2: f64) -> impl Fn(f64, usize) -> f64 {
    move |x, j| match j {
        0 => 1.0,
        1 => (w1 * x).cos(),
        2 => (w1 * x).sin(),
        3 => (w2 * x).cos(),
        _ => (w2 * x).sin(),
    }
}

fn main() {
    let dir = std::env::args().nth(1).unwrap_or_else(|| "/tmp/osc".into());
    let minn: usize = std::env::args().nth(2).and_then(|s| s.parse().ok()).unwrap_or(0);
    let data = parse_dir(&dir, minn);
    if data.len() < 4 {
        eprintln!("only {} points parsed from {}; need >=4", data.len(), dir);
        std::process::exit(1);
    }
    let mut xs: Vec<f64> = data.iter().map(|p| p.x).collect();
    xs.sort_by(|a, b| a.partial_cmp(b).unwrap());
    println!("points parsed: {}", data.len());
    println!(
        "x-range ln N: [{:.4}, {:.4}]  ({:.3} log-units)",
        xs[0],
        xs[xs.len() - 1],
        xs[xs.len() - 1] - xs[0]
    );
    let ymean: f64 = data.iter().map(|p| p.y).sum::<f64>() / data.len() as f64;
    let ysd: f64 = (data
        .iter()
        .map(|p| (p.y - ymean) * (p.y - ymean))
        .sum::<f64>()
        / data.len() as f64)
        .sqrt();
    println!(
        "y mean = {:.6}, sd = {:.6} ({}% of mean)",
        ymean,
        ysd,
        100.0 * ysd / ymean
    );
    let rss0: f64 = data.iter().map(|p| (p.y - ymean) * (p.y - ymean)).sum();
    let n = data.len() as f64;
    println!(
        "M0 baseline: c = {:.6}, RMS = {:.6}, RSS = {:.8}",
        ymean,
        (rss0 / n).sqrt(),
        rss0
    );

    // grid over period P (log-units), covering gamma1..gamma3 and beats
    let pmin = 0.20;
    let pmax = 1.60;
    let nstep = 560;
    let dp = (pmax - pmin) / nstep as f64;

    // M1: sweep P, linear fit in (1, cos, sin)
    let mut best1: (f64, f64, Vec<f64>) = (f64::MAX, 0.0, vec![]);
    for i in 0..=nstep {
        let p = pmin + i as f64 * dp;
        let w = 2.0 * PI / p;
        let (x, r) = linfit(&data, 3, &basis_cos(w));
        if r < best1.0 {
            best1 = (r, p, x);
        }
    }
    // refine P locally (finer grid around best)
    {
        let (r0, p0, _) = best1;
        for i in 1..=200 {
            let p = p0 + (i as f64 - 100.0) * 0.0001;
            if p < pmin || p > pmax {
                continue;
            }
            let w = 2.0 * PI / p;
            let (x, r) = linfit(&data, 3, &basis_cos(w));
            if r < best1.0 {
                best1 = (r, p, x);
            }
        }
    }
    let (r1, p1, x1) = &best1;
    let a1 = (x1[1] * x1[1] + x1[2] * x1[2]).sqrt();
    let phi1 = x1[2].atan2(x1[1]); // a1 cos + a2 sin = A cos(wx - atan2(a2,a1))? verify below
    // A cos(w x + phi) = A cos(wx)cos(phi) - A sin(wx)sin(phi) => a1 = A cos phi, a2 = -A sin phi
    // => phi = atan2(-a2, a1)
    let phi1c = (-x1[2]).atan2(x1[1]);
    println!(
        "\nM1 one-cosine: c={:.6} A={:.6} P={:.4} phi={:.4}  RMS={:.6}  RSS={:.8}  (RMS/M0={:.3})",
        x1[0], a1, p1, phi1c, r1, r1 * r1 * n, r1 / (rss0 / n).sqrt()
    );
    println!(
        "  gamma1 P={:.4}, gamma2 P={:.4}, gamma3 P={:.4}",
        2.0 * PI / G1,
        2.0 * PI / G2,
        2.0 * PI / G3
    );
    // RMS at the EXACT gamma periods (M1 basis), for direct comparison
    for (name, g) in [("gamma1", G1), ("gamma2", G2), ("gamma3", G3)] {
        let w = g; // period = 2pi/g <-> w = g
        let (x, r) = linfit(&data, 3, &basis_cos(w));
        let a = (x[1] * x[1] + x[2] * x[2]).sqrt();
        println!(
            "  M1 at fixed {} (P={:.4}): c={:.6} A={:.6} RMS={:.6}  (best M1 RMS={:.6})",
            name,
            2.0 * PI / g,
            x[0],
            a,
            r,
            r1
        );
    }

    // M3: c + (b1 cos + b2 sin)/sqrt(x), sweep P
    let mut best3: (f64, f64, Vec<f64>) = (f64::MAX, 0.0, vec![]);
    for i in 0..=nstep {
        let p = pmin + i as f64 * dp;
        let w = 2.0 * PI / p;
        let (x, r) = linfit(&data, 3, &basis_cos_sqrt(w));
        if r < best3.0 {
            best3 = (r, p, x);
        }
    }
    {
        let (r0, p0, _) = best3;
        for i in 1..=200 {
            let p = p0 + (i as f64 - 100.0) * 0.0001;
            if p < pmin || p > pmax {
                continue;
            }
            let w = 2.0 * PI / p;
            let (x, r) = linfit(&data, 3, &basis_cos_sqrt(w));
            if r < best3.0 {
                best3 = (r, p, x);
            }
        }
    }
    let (r3, p3, x3) = &best3;
    let b3 = (x3[1] * x3[1] + x3[2] * x3[2]).sqrt();
    let phi3 = (-x3[2]).atan2(x3[1]);
    println!(
        "\nM3 explicit-formula (B/sqrt(x) amplitude): c={:.6} B={:.6} P={:.4} phi={:.4}  RMS={:.6}  (RMS/M0={:.3})",
        x3[0], b3, p3, phi3, r3, r3 / (rss0 / n).sqrt()
    );

    // gamma-periodicity sign-agreement probe (free phase), using y-mean
    for (name, g) in [("gamma1", G1), ("gamma2", G2), ("gamma3", G3)] {
        let mut best_agree = 0.0;
        let mut best_phi = 0.0;
        for i in 0..720 {
            let ph = i as f64 * 2.0 * PI / 720.0;
            let mut agree = 0.0;
            let mut tot = 0.0;
            for p in &data {
                let s = (p.y - ymean).signum();
                let cs = (g * p.x + ph).cos().signum();
                if s != 0.0 && cs != 0.0 {
                    if s == cs {
                        agree += 1.0;
                    }
                    tot += 1.0;
                }
            }
            let frac = if tot > 0.0 { agree / tot } else { 0.0 };
            if frac > best_agree {
                best_agree = frac;
                best_phi = ph;
            }
        }
        println!(
            "probe {}: best sign-agreement {:.3} at phi={:.3}  (0.5 = chance, 1.0 = locked)",
            name, best_agree, best_phi
        );
    }

    // M2: P1 fixed at best single period, sweep P2, linear in (1, cos1, sin1, cos2, sin2)
    let w1 = 2.0 * PI / p1;
    let mut best2: (f64, f64, Vec<f64>) = (f64::MAX, 0.0, vec![]);
    for i in 0..=nstep {
        let p2 = pmin + i as f64 * dp;
        if (p2 - p1).abs() < 0.02 {
            continue; // avoid near-degenerate pair
        }
        let w2 = 2.0 * PI / p2;
        let (x, r) = linfit(&data, 5, &basis_two(w1, w2));
        if r < best2.0 {
            best2 = (r, p2, x);
        }
    }
    let (r2, p2b, x2) = &best2;
    let a21 = (x2[1] * x2[1] + x2[2] * x2[2]).sqrt();
    let a22 = (x2[3] * x2[3] + x2[4] * x2[4]).sqrt();
    let phi21 = (-x2[2]).atan2(x2[1]);
    let phi22 = (-x2[4]).atan2(x2[3]);
    println!(
        "\nM2 two-cosine: c={:.6} A1={:.6} P1={:.4} phi1={:.4} A2={:.6} P2={:.4} phi2={:.4}  RMS={:.6}  (RMS/M0={:.3}, vs M1 {:.3})",
        x2[0], a21, p1, phi21, a22, p2b, phi22, r2, r2 / (rss0 / n).sqrt(), r2 / r1
    );

    // dense table
    println!("\ndense table (N, y=d*sqrt(lnN), dev from M1 model):");
    for p in &data {
        let pred = x1[0] + a1 * ((2.0 * PI / p1) * p.x + phi1c).cos();
        println!(
            "  e^{:.4} (N={:.0}): y={:.6}  dev={:+.6}  m1res={:+.6}",
            p.x,
            p.x.exp(),
            p.y,
            p.y - ymean,
            p.y - pred
        );
    }
}
