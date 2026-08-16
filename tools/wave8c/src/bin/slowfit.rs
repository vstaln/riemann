// slowfit — test the gamma2-gamma3 BEAT hypothesis (P = 2pi/(g3-g2) = 1.5752) for the
// slow ~1.5-log-unit wobble of d_N*sqrt(ln N). std-only.
// Usage: slowfit <datadir> [minN]
//   M1free: sweep P, best single cosine
//   M1beat: P FIXED at 2pi/(g3-g2) = 1.5752  (also ref P=1.5112 from prior note)
//   M2beat: P1 fixed at beat, sweep P2
//   Mprod:  linear basis at the two EXPLICIT zero periods 2pi/g2, 2pi/g3
//            (the product cos(g2 x)cos(g3 x) is NOT in this linear span -> discriminator)
//   Bootstrap null: 500 permutations of residuals of the fixed-beat fit; for each,
//            refit M1free; report (a) P-distribution (how often best P lands near beat),
//            (b) how often null RMS @ beat <= observed RMS @ beat (beat-amplitude significance).
//   Dip check: prediction & residual at N=700 (and N=725, 675) for the beat model.

use std::f64::consts::PI;
use std::fs;

const G2: f64 = 21.0220;
const G3: f64 = 25.0109;
const PBEAT: f64 = 2.0 * PI / (G3 - G2); // 1.5752
const PREF: f64 = 1.5112; // prior free-fit best (N>=300 window)
const SEED: u64 = 20260818;

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

fn basis_cos(w: f64) -> impl Fn(f64, usize) -> f64 {
    move |x, j| match j {
        0 => 1.0,
        1 => (w * x).cos(),
        _ => (w * x).sin(),
    }
}

fn basis_two(w1: f64, w2: f64) -> impl Fn(f64, usize) -> f64 {
    move |x, j| match j {
        0 => 1.0,
        1 => (w1 * x).cos(),
        2 => (w1 * x).sin(),
        3 => (w2 * x).cos(),
        _ => (w2 * x).sin(),
    }
}

// product-explicit basis: 1, cos(g2 x), sin(g2 x), cos(g3 x), sin(g3 x)
fn basis_prod() -> impl Fn(f64, usize) -> f64 {
    move |x, j| match j {
        0 => 1.0,
        1 => (G2 * x).cos(),
        2 => (G2 * x).sin(),
        3 => (G3 * x).cos(),
        _ => (G3 * x).sin(),
    }
}

fn rng_next(state: &mut u64) -> u64 {
    // xorshift64
    let mut x = *state;
    x ^= x << 13;
    x ^= x >> 7;
    x ^= x << 17;
    *state = x;
    x
}

fn main() {
    let dir = std::env::args().nth(1).unwrap_or_else(|| "/tmp/osc".into());
    let minn: usize = std::env::args().nth(2).and_then(|s| s.parse().ok()).unwrap_or(0);
    let data = parse_dir(&dir, minn);
    if data.len() < 4 {
        eprintln!("only {} points parsed; need >=4", data.len());
        std::process::exit(1);
    }
    let mut xs: Vec<f64> = data.iter().map(|p| p.x).collect();
    xs.sort_by(|a, b| a.partial_cmp(b).unwrap());
    println!(
        "== slowfit: {} points, x in [{:.4},{:.4}] ({:.3} log-units), beat P = {:.4} = 2pi/(g3-g2) = 2pi/{:.4}",
        data.len(),
        xs[0],
        xs[xs.len() - 1],
        xs[xs.len() - 1] - xs[0],
        PBEAT,
        G3 - G2
    );
    let ymean: f64 = data.iter().map(|p| p.y).sum::<f64>() / data.len() as f64;
    let n = data.len() as f64;
    let rss0: f64 = data.iter().map(|p| (p.y - ymean) * (p.y - ymean)).sum();
    let rms0 = (rss0 / n).sqrt();
    println!("M0: c={:.6} RMS={:.6} RSS={:.8}", ymean, rms0, rss0);

    // ---- M1 free P (sweep + local refine) ----
    let pmin = 0.20;
    let pmax = 1.60;
    let nstep = 560;
    let dp = (pmax - pmin) / nstep as f64;
    let mut best1: (f64, f64, Vec<f64>) = (f64::MAX, 0.0, vec![]);
    for i in 0..=nstep {
        let p = pmin + i as f64 * dp;
        let w = 2.0 * PI / p;
        let (x, r) = linfit(&data, 3, &basis_cos(w));
        if r < best1.0 {
            best1 = (r, p, x);
        }
    }
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
    let phi1 = (-x1[2]).atan2(x1[1]);
    println!(
        "M1 free P: c={:.6} A={:.6} P={:.4} phi={:.4} RMS={:.6} (RMS/M0={:.3})",
        x1[0], a1, p1, phi1, r1, r1 / rms0
    );
    // how close is free P to the beat?
    println!(
        "  |P_free - P_beat| = {:.4}  (beat {:.4}, prior ref {:.4})",
        (p1 - PBEAT).abs(),
        PBEAT,
        PREF
    );

    // ---- M1 fixed at beat P and at prior ref P ----
    for (name, pfix) in [("BEAT P=1.5752", PBEAT), ("REF P=1.5112", PREF)] {
        let w = 2.0 * PI / pfix;
        let (x, r) = linfit(&data, 3, &basis_cos(w));
        let a = (x[1] * x[1] + x[2] * x[2]).sqrt();
        let ph = (-x[2]).atan2(x[1]);
        println!(
            "M1 fixed {}: c={:.6} A={:.6} phi={:.4} RMS={:.6} (RMS/M0={:.3}, vs free {:.3})",
            name,
            x[0],
            a,
            ph,
            r,
            r / rms0,
            r / r1
        );
    }

    // ---- M2: P1 = beat fixed, sweep P2 (wider range; guard near-degenerate pair) ----
    let w1 = 2.0 * PI / PBEAT;
    let pmax2 = 1.80;
    let nstep2 = 660;
    let dp2 = (pmax2 - pmin) / nstep2 as f64;
    let mut best2: (f64, f64, Vec<f64>) = (f64::MAX, 0.0, vec![]);
    for i in 0..=nstep2 {
        let p2 = pmin + i as f64 * dp2;
        if (p2 - PBEAT).abs() < 0.05 {
            continue;
        }
        let w2 = 2.0 * PI / p2;
        let (x, r) = linfit(&data, 5, &basis_two(w1, w2));
        if r < best2.0 {
            best2 = (r, p2, x);
        }
    }
    {
        let (r0, p0, _) = best2;
        for i in 1..=200 {
            let p = p0 + (i as f64 - 100.0) * 0.0001;
            if p < pmin || p > pmax2 {
                continue;
            }
            if (p - PBEAT).abs() < 0.05 {
                continue;
            }
            let w = 2.0 * PI / p;
            let (x, r) = linfit(&data, 5, &basis_two(w1, w));
            if r < best2.0 {
                best2 = (r, p, x);
            }
        }
    }
    let (r2, p2b, x2) = &best2;
    let a21 = (x2[1] * x2[1] + x2[2] * x2[2]).sqrt();
    let a22 = (x2[3] * x2[3] + x2[4] * x2[4]).sqrt();
    println!(
        "M2 beat + P2: c={:.6} A1={:.6}(beat) A2={:.6} P2={:.4} RMS={:.6} (RMS/M0={:.3}, vs M1beat {:.3})",
        x2[0],
        a21,
        a22,
        p2b,
        r2,
        r2 / rms0,
        {
            let w = 2.0 * PI / PBEAT;
            let (_, rb) = linfit(&data, 3, &basis_cos(w));
            r2 / rb
        }
    );

    // ---- Mprod: explicit zero periods (linear span) ----
    let (x4, r4) = linfit(&data, 5, &basis_prod());
    let a4g2 = (x4[1] * x4[1] + x4[2] * x4[2]).sqrt();
    let a4g3 = (x4[3] * x4[3] + x4[4] * x4[4]).sqrt();
    println!(
        "Mprod explicit {{g2,g3}} periods: c={:.6} A(g2)={:.6} A(g3)={:.6} RMS={:.6} (RMS/M0={:.3}, vs M1beat {:.3})",
        x4[0],
        a4g2,
        a4g3,
        r4,
        r4 / rms0,
        {
            let w = 2.0 * PI / PBEAT;
            let (_, rb) = linfit(&data, 3, &basis_cos(w));
            r4 / rb
        }
    );

    // ---- dip check at N=700/725/675 under the beat model ----
    {
        let w = 2.0 * PI / PBEAT;
        let (x, _) = linfit(&data, 3, &basis_cos(w));
        let a = (x[1] * x[1] + x[2] * x[2]).sqrt();
        let ph = (-x[2]).atan2(x[1]);
        for nv in [675usize, 700, 725, 750, 775, 800] {
            let xv = (nv as f64).ln();
            let pred = x[0] + a * (w * xv + ph).cos();
            let yv = data.iter().find(|p| (p.x - xv).abs() < 1e-9).map(|p| p.y);
            match yv {
                Some(y) => println!(
                    "  dip check N={}: y={:.6} beat-pred={:.6} residual={:+.6}",
                    nv, y, pred, y - pred
                ),
                None => println!("  dip check N={}: not in dataset", nv),
            }
        }
    }

    // ---- bootstrap null: permute M0 (constant-fit) residuals, 500x ----
    // Correct null: structureless noise with the observed variance. Compare:
    //  (a) RMS at FIXED beat P under null vs observed RMS@beat  -> beat-amplitude significance
    //  (b) free-P best under null: how often it lands near the beat -> beat-period emergence
    //  (c) free-P RMS under null vs observed free-P RMS
    {
        let res: Vec<f64> = data.iter().map(|p| p.y - ymean).collect();
        let mut state = SEED;
        let mut near_beat = 0usize;
        let mut as_good_beat = 0usize;
        let mut as_good_free = 0usize;
        let mut best_ps: Vec<f64> = Vec::new();
        let nb = 500usize;
        // observed statistics
        let wb = 2.0 * PI / PBEAT;
        let (_, r_obs_beat) = linfit(&data, 3, &basis_cos(wb));
        let r_obs_free = *r1;
        for _ in 0..nb {
            let mut rr = res.clone();
            for i in (1..rr.len()).rev() {
                let j = (rng_next(&mut state) % (i as u64 + 1)) as usize;
                rr.swap(i, j);
            }
            let null_data: Vec<Pt> = data
                .iter()
                .zip(rr.iter())
                .map(|(p, r)| Pt {
                    x: p.x,
                    y: ymean + *r,
                })
                .collect();
            let (_, rb) = linfit(&null_data, 3, &basis_cos(wb));
            if rb <= r_obs_beat {
                as_good_beat += 1;
            }
            let mut b: (f64, f64, Vec<f64>) = (f64::MAX, 0.0, vec![]);
            for i in 0..=nstep {
                let p = pmin + i as f64 * dp;
                let ww = 2.0 * PI / p;
                let (xx, r) = linfit(&null_data, 3, &basis_cos(ww));
                if r < b.0 {
                    b = (r, p, xx);
                }
            }
            best_ps.push(b.1);
            if (b.1 - PBEAT).abs() < 0.1575 {
                near_beat += 1; // within 10% of 1.575
            }
            if b.0 <= r_obs_free {
                as_good_free += 1;
            }
        }
        let near_frac = near_beat as f64 / nb as f64;
        let gb_frac = as_good_beat as f64 / nb as f64;
        let gf_frac = as_good_free as f64 / nb as f64;
        best_ps.sort_by(|a, b| a.partial_cmp(b).unwrap());
        println!(
            "\nbootstrap null ({} perm of M0 residuals, variance-preserving):",
            nb
        );
        println!(
            "  null RMS@beat <= observed {:.6}: {}/{} = {:.1}%  [beat-amplitude p-value: LOW % = real signal]",
            r_obs_beat, as_good_beat, nb, 100.0 * gb_frac
        );
        println!(
            "  null free-P RMS <= observed {:.6}: {}/{} = {:.1}%  [slow-structure p-value]",
            r_obs_free, as_good_free, nb, 100.0 * gf_frac
        );
        println!(
            "  null best-P lands within 10% of beat ({:.4}): {}/{} = {:.1}%  [chance emergence of the beat period from noise]",
            PBEAT, near_beat, nb, 100.0 * near_frac
        );
        println!(
            "  null best-P median={:.4}  p10={:.4} p90={:.4}",
            best_ps[nb / 2],
            best_ps[nb / 10],
            best_ps[9 * nb / 10]
        );
    }

    // ---- dense table with dev from beat model ----
    {
        let w = 2.0 * PI / PBEAT;
        let (x, _) = linfit(&data, 3, &basis_cos(w));
        let a = (x[1] * x[1] + x[2] * x[2]).sqrt();
        let ph = (-x[2]).atan2(x[1]);
        println!("\ndense table (N, y, dev-from-mean, beat-model residual):");
        for p in &data {
            let pred = x[0] + a * (w * p.x + ph).cos();
            println!(
                "  N={:.0}: y={:.6}  dev={:+.6}  beatres={:+.6}",
                p.x.exp(),
                p.y,
                p.y - ymean,
                p.y - pred
            );
        }
    }
}
