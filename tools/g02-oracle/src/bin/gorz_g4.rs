// Measure G4(M) directly on the certified 210-bit table (M <= 299).
// G4 = a4/D^6 where a4 is the j^4 coefficient of log R_M(j) = log gamma(M-j)/gamma(M).
// Paper limit: G4 -> 2^{3}/(4*3) = 8/12 = 2/3.  If G4 ~ 0 instead, the (4/3 - 7 G4) D^4
// term in the exact identity would explain the measured resid/D^4 -> 4/3.
use rug::float::Constant;
use rug::ops::Pow;
use rug::Float;
use std::fs;

const PG: u32 = 210;

fn zf(prec: u32, v: f64) -> Float { Float::with_val(prec, v) }

fn fit_quartic(lg: &[Float]) -> (Float, Float, Float, Float, Float) {
    // lg[j] = log gamma(M-j), j=0..5;  L_j = lg[j]-lg[0] = c1 j + c2 j^2 + c3 j^3 + c4 j^4
    // Solve Vandermonde at j=1..4 for (c1..c4) exactly, check residual at j=5.
    let l = |j: usize| -> Float { Float::with_val(PG, &lg[j] - &lg[0]) };
    // Use the recurrence from fitting through j=1..4 (invert 4x4 Vandermonde via
    // Newton forward differences).
    // Simpler: solve the linear system with Gaussian elimination in Float.
    // A[i][k] = (i+1)^{k+1}  (i,k = 0..3), b[i] = L_{i+1}
    let mut a: Vec<Vec<Float>> = Vec::new();
    let mut b: Vec<Float> = Vec::new();
    for i in 0..4 {
        let jj = (i + 1) as f64;
        let mut row = Vec::new();
        for k in 0..4 {
            row.push(Float::with_val(PG, jj.powi(k as i32 + 1)));
        }
        a.push(row);
        b.push(l(i + 1));
    }
    // Gaussian elimination with partial pivoting
    let mut x = vec![zf(PG, 0.0); 4];
    for col in 0..4 {
        let mut piv = col;
        for r in col + 1..4 {
            if a[r][col].clone().abs() > a[piv][col].clone().abs() {
                piv = r;
            }
        }
        a.swap(col, piv);
        b.swap(col, piv);
        let pv = a[col][col].clone();
        for r in col + 1..4 {
            let f = Float::with_val(PG, &a[r][col] / &pv);
            for c in col..4 {
                let t = Float::with_val(PG, &f * &a[col][c]);
                let v = Float::with_val(PG, &a[r][c] - &t);
                a[r][c] = v;
            }
            let t = Float::with_val(PG, &f * &b[col]);
            let v = Float::with_val(PG, &b[r] - &t);
            b[r] = v;
        }
    }
    for col in (0..4).rev() {
        let mut s = b[col].clone();
        for c in col + 1..4 {
            let t = Float::with_val(PG, &a[col][c] * &x[c]);
            s = Float::with_val(PG, &s - &t);
        }
        x[col] = Float::with_val(PG, &s / &a[col][col]);
    }
    // residual at j=5
    let mut pred = zf(PG, 0.0);
    for k in 0..4 {
        let j5 = Float::with_val(PG, 5.0f64.powi(k as i32 + 1));
        pred = Float::with_val(PG, &pred + Float::with_val(PG, &x[k] * &j5));
    }
    let res = Float::with_val(PG, &pred - &l(5)).abs();
    (x[0].clone(), x[1].clone(), x[2].clone(), x[3].clone(), res)
}

fn main() {
    let txt = fs::read_to_string("/home/vstaln/riemann/research/notes/g02-moments-oracle-2026-08-18.txt")
        .expect("read table");
    let mut b: Vec<Float> = Vec::new();
    for line in txt.lines() {
        let line = line.trim();
        if line.is_empty() || line.starts_with('#') || line.starts_with("g0-2") {
            continue;
        }
        let cols: Vec<&str> = line.split('\t').collect();
        if cols.len() >= 3 {
            if let Ok(v) = Float::parse_radix(cols[2].trim(), 10) {
                b.push(Float::with_val(PG, v));
            }
        }
    }
    println!("n rows loaded: {}", b.len());
    let logfact = |n: usize| -> Float {
        let mut s = zf(PG, 0.0);
        for j in 2..=n { s += zf(PG, j as f64).ln(); }
        s
    };
    // gamma(M) = 8 * M! * b_M
    let lg = |m: usize| -> Float {
        let l8 = zf(PG, 8.0).ln();
        let lf = logfact(m);
        let lb = b[m].clone().ln();
        Float::with_val(PG, &l8 + &lf);
        Float::with_val(PG, Float::with_val(PG, &l8 + &lf) + &lb)
    };
    println!("{:>6} | {:>10} {:>12} {:>12} {:>12} {:>12} {:>10}", "M", "D", "G2=c2/D^2", "G3=c3/D^4", "G4=c4/D^6", "G4-2/3", "fit res");
    for &m in &[40usize, 100, 150, 200, 250, 290] {
        let mut lgv = vec![zf(PG, 0.0); 6];
        for j in 0..6 { lgv[j] = lg(m - j); }
        let (c1, c2, c3, c4, res) = fit_quartic(&lgv);
        // D^2 = 1/2 (1 - exp(lg[2]+lg[0]-2lg[1]))
        let t1 = Float::with_val(PG, &lgv[2] + &lgv[0]);
        let t2 = Float::with_val(PG, zf(PG, 2.0) * &lgv[1]);
        let x = Float::with_val(PG, &t1 - &t2);
        let d2 = Float::with_val(PG, 0.5 * (zf(PG, 1.0) - x.exp()));
        let d = d2.clone().sqrt();
        let d4 = Float::with_val(PG, &d2 * &d2);
        let d6 = Float::with_val(PG, &d4 * &d2);
        let g2 = Float::with_val(PG, &c2 / &d2);
        let g3 = Float::with_val(PG, &c3 / &d4);
        let g4 = Float::with_val(PG, &c4 / &d6);
        println!(
            "{:6} | {:10.5} {:12.6} {:12.6} {:12.6} {:12.4e} {:10.1e}",
            m, d.to_f64(), g2.to_f64(), g3.to_f64(), g4.to_f64(), (g4 - zf(PG, 2.0/3.0)).to_f64(), res.to_f64()
        );
    }
    println!("\nPaper limit: G4 -> 2^3/(4*3) = 2/3. If G4 ~ 2/3, resid/D^4 in (2.5) should -> 10/3, not 4/3.");
}
