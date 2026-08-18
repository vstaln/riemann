// xi_cosine_pf: three verifications on the reopened small-n Jensen route.
// (1) Xi(z) = xi(1/2+iz) = 2*int_0^inf Phi(u) cos(zu) du  (cosine transform of the
//     POSITIVE measure 2*Phi(u)du)  — checked against the certified Taylor series
//     Xi(z) = sum_k (-1)^k b_k z^{2k}, b_k = M_k/(2k)!.
// (2) Full Toeplitz PF audit of a_k = b_k = M_k/(2k)! (the Taylor coefficients):
//     consecutive-index minors of orders 2..5, many starts.
// (3) Jensen polynomials J^{d,n}(X) = sum_j C(d,j) gamma(n+j) X^j, gamma = k! b_k:
//     real-root checks for d=5,6.
use std::fs;

fn main() {
    let txt = fs::read_to_string("/home/vstaln/riemann/research/notes/g02-moments-oracle-2026-08-18.txt")
        .expect("oracle table");
    let mut m: Vec<f64> = Vec::new();   // M_k
    let mut b: Vec<f64> = Vec::new();   // b_k = M_k/(2k)!
    let mut gam: Vec<f64> = Vec::new(); // gamma(k) = k! b_k
    for line in txt.lines() {
        let line = line.trim();
        if line.is_empty() || line.starts_with('#') || line.starts_with("g0-2") { continue; }
        let cols: Vec<&str> = line.split('\t').collect();
        if cols.len() >= 4 {
            let mk = cols[1].trim().parse::<f64>().unwrap();
            let bk = cols[2].trim().parse::<f64>().unwrap();
            let gk = cols[3].trim().parse::<f64>().unwrap();
            m.push(mk); b.push(bk); gam.push(gk);
        }
    }
    let n = b.len();
    println!("loaded M,b,gamma for k=0..{}", n - 1);

    // ---------- (1) Cosine transform identity ----------
    // Phi(u) = 2 sum_{n>=1} (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}
    // (exact algebraic form from the g02 note). Numerically integrate
    //   2 * int_0^inf Phi(u) cos(z u) du
    // with Gauss-Legendre panels + explicit tail bound (Phi decays super-exponentially).
    fn phi_f64(u: f64) -> f64 {
        let pi = std::f64::consts::PI;
        let mut s = 0.0;
        for n in 1..=14i32 {
            let n2 = (n * n) as f64;
            let n4 = n2 * n2;
            let e92 = (4.5 * u).exp();
            let e52 = (2.5 * u).exp();
            let e2u = (2.0 * u).exp();
            let a = 2.0 * pi * pi * n4 * e92 - 3.0 * pi * n2 * e52;
            s += a * (-pi * n2 * e2u).exp();
        }
        2.0 * s
    }
    // Gauss-Legendre nodes/weights on [-1,1], order 48 (same as oracle)
    let gl = gl48();
    let cos_int = |z: f64| -> (f64, f64) {
        // panels over u in [0, UMAX], UMAX = 6.0 (Phi ~ e^{-pi e^{12}} ~ 1e-150 there)
        let umax = 6.0f64;
        let np = 80usize;
        let h = umax / np as f64;
        let mut v = 0.0;
        for p in 0..np {
            let a = p as f64 * h;
            let b = a + h;
            let mid = 0.5 * (a + b);
            let half = 0.5 * (b - a);
            for &(x, w) in gl.iter() {
                let u = mid + half * x;
                let f = phi_f64(u) * (z * u).cos();
                v += half * w * f;
            }
        }
        // tail bound: |Phi(u)| <= 2*sum 3 pi n^2 e^{5u/2} e^{-pi n^2 e^{2u}} for u large
        // (the 3 pi n^2 e^{5u/2} term dominates when e^{2u} large). Crude but tiny:
        // at u=6, n=1 term ~ e^{15} e^{-pi e^{12}} ~ 3e6 * e^{-5e5} ~ 0. So tail < 1e-200.
        (2.0 * v, 1e-100)
    };
    // Taylor partial sum: Xi(z) = sum_k (-1)^k b_k z^{2k}  (b_k = M_k/(2k)!)
    let taylor = |z: f64| -> f64 {
        let z2 = z * z;
        let mut s = 0.0;
        let mut term = 1.0;
        let mut k = 0usize;
        loop {
            let add = if k % 2 == 0 { 1.0 } else { -1.0 } * b[k] * term;
            s += add;
            term *= z2;
            k += 1;
            if k >= 40 { break; }
            if add.abs() < 1e-30 { break; }
        }
        s
    };
    println!("\n(1) Cosine-transform identity: Xi(z) = 2*int Phi(u) cos(zu)du vs Taylor series");
    for z in [0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 10.0, 14.1347] {
        let (c, ce) = cos_int(z);
        let t = taylor(z);
        println!("  z={:8.4}: cos-int = {:+.10e} (err<{:.0e})   taylor = {:+.10e}   |diff| = {:.2e}",
                 z, c, ce, t, (c - t).abs());
    }

    // ---------- (2) Toeplitz PF audit on a_k = b_k ----------
    let a = &b; // a_k = M_k/(2k)!
    let det3 = |v: &[f64; 9]| v[0]*(v[4]*v[8]-v[5]*v[7]) - v[1]*(v[3]*v[8]-v[5]*v[6]) + v[2]*(v[3]*v[7]-v[4]*v[6]);
    let det4 = |v: &[f64; 16]| {
        let mut s = 0.0;
        for c in 0..4 {
            let sign = if c % 2 == 0 { 1.0 } else { -1.0 };
            let mut sub = [0.0f64; 9]; let mut idx = 0;
            for r in 1..4 { for c2 in 0..4 { if c2 != c { sub[idx] = v[r*4+c2]; idx += 1; } } }
            s += sign * v[c] * det3(&sub);
        }
        s
    };
    let det5 = |v: &[f64; 25]| {
        let mut s = 0.0;
        for c in 0..5 {
            let sign = if c % 2 == 0 { 1.0 } else { -1.0 };
            let mut sub = [0.0f64; 16]; let mut idx = 0;
            for r in 1..5 { for c2 in 0..5 { if c2 != c { sub[idx] = v[r*5+c2]; idx += 1; } } }
            s += sign * v[c] * det4(&sub);
        }
        s
    };
    let toep = |rows: &[usize], cols: &[usize]| -> Vec<f64> {
        let r = rows.len(); let c = cols.len();
        let mut v = vec![0.0f64; r*c];
        for i in 0..r { for j in 0..c {
            let idx = rows[i] as i64 - cols[j] as i64;
            v[i*c+j] = if idx < 0 { 0.0 } else { a[idx as usize] };
        }}
        v
    };
    println!("\n(2) Toeplitz PF audit on a_k = M_k/(2k)! (Taylor coefficients of Xi)");
    // PF2: log-concavity
    let mut pf2 = true;
    for k in 0..50 { pf2 &= a[k+1]*a[k+1] - a[k]*a[k+2] >= 0.0; }
    println!("  PF2 (log-concavity, k=0..49): {}", pf2);
    // PF3: all 3x3 consecutive-row/col minors
    let mut pf3 = true; let mut cnt3 = 0;
    for s in 0..30 { for c0 in 0..4 {
        let v = toep(&[s+1, s+2, s+3], &[c0, c0+1, c0+2]);
        let d = det3(&v.try_into().unwrap());
        pf3 &= d >= 0.0; cnt3 += 1;
    }}
    println!("  PF3: {} consecutive 3x3 minors all >= 0: {}", cnt3, pf3);
    // PF4: 4x4 consecutive
    let mut pf4 = true; let mut cnt4 = 0;
    for s in 0..20 { for c0 in 0..3 {
        let v = toep(&[s+1, s+2, s+3, s+4], &[c0, c0+1, c0+2, c0+3]);
        let d = det4(&v.try_into().unwrap());
        pf4 &= d >= 0.0; cnt4 += 1;
    }}
    println!("  PF4: {} consecutive 4x4 minors all >= 0: {}", cnt4, pf4);
    // PF5: 5x5 consecutive
    let mut pf5 = true; let mut cnt5 = 0;
    for s in 0..12 { for c0 in 0..2 {
        let v = toep(&[s+1, s+2, s+3, s+4, s+5], &[c0, c0+1, c0+2, c0+3, c0+4]);
        let d = det5(&v.try_into().unwrap());
        pf5 &= d >= 0.0; cnt5 += 1;
    }}
    println!("  PF5: {} consecutive 5x5 minors all >= 0: {}", cnt5, pf5);
    // leading principal minors explicitly (rows/cols (1..r),(0..r-1))
    for r in 2..=5 {
        let rows: Vec<usize> = (1..=r).collect();
        let cols: Vec<usize> = (0..r).collect();
        let v = toep(&rows, &cols);
        let d = match r { 2 => { let s: [f64;4] = v.try_into().unwrap(); s[0]*s[3]-s[1]*s[2] },
                          3 => det3(&v.try_into().unwrap()),
                          4 => det4(&v.try_into().unwrap()),
                          _ => det5(&v.try_into().unwrap()) };
        println!("  leading {}x{} minor: {:.6e}  {}", r, r, d, if d >= 0.0 {"✓"} else {"✗"});
    }

    // PF6: 6x6 consecutive (one order higher, with the certified ~60-digit table
    // these stay well above f64 underflow for small k)
    let det6 = |v: &[f64; 36]| {
        let mut s = 0.0;
        for c in 0..6 {
            let sign = if c % 2 == 0 { 1.0 } else { -1.0 };
            let mut sub = [0.0f64; 25]; let mut idx = 0;
            for r in 1..6 { for c2 in 0..6 { if c2 != c { sub[idx] = v[r*6+c2]; idx += 1; } } }
            s += sign * v[c] * det5(&sub);
        }
        s
    };
    let mut pf6 = true; let mut cnt6 = 0;
    for s in 0..6 {
        let v = toep(&[s+1, s+2, s+3, s+4, s+5, s+6], &[0, 1, 2, 3, 4, 5]);
        let d = det6(&v.try_into().unwrap());
        pf6 &= d >= 0.0; cnt6 += 1;
    }
    println!("  PF6: {} consecutive 6x6 minors all >= 0: {}", cnt6, pf6);
    // leading 6x6
    {
        let rows: Vec<usize> = (1..=6).collect();
        let cols: Vec<usize> = (0..6).collect();
        let v = toep(&rows, &cols);
        let d = det6(&v.try_into().unwrap());
        println!("  leading 6x6 minor: {:.6e}  {}", d, if d >= 0.0 {"✓"} else {"✗"});
    }

    // ---------- (3) Jensen J^{5,n}, J^{6,n} root checks ----------
    println!("\n(3) Jensen J^(5,n), J^(6,n) real-root checks (sign changes on [-200,0])");
    // J^{d,n}(X) = sum_j C(d,j) gamma(n+j) X^j; all coefficients positive -> all roots < 0
    let binom = |d: usize, j: usize| -> f64 {
        let mut v = 1.0f64;
        for i in 0..j { v *= (d - i) as f64 / (i + 1) as f64; }
        v
    };
    let jpoly = |d: usize, n: usize, x: f64| -> f64 {
        let mut s = 0.0;
        for j in 0..=d { s += binom(d, j) * gam[n + j] * x.powi(j as i32); }
        s
    };
    for &d in &[5usize, 6usize, 7usize] {
        let mut all_ok = true;
        for n in 0..6 {
            let xmin = -400.0f64; let npts = 20000usize;
            let mut prev = jpoly(d, n, xmin).signum();
            let mut changes = 0;
            for i in 1..=npts {
                let x = xmin + (400.0) * (i as f64) / (npts as f64);
                let s = jpoly(d, n, x).signum();
                if s != prev { changes += 1; prev = s; }
            }
            let ok = changes == d;
            all_ok &= ok;
            if n < 3 { println!("  J^({},{}) : {} real roots  {}", d, n, changes, if ok {"✓"} else {"✗"}); }
        }
        println!("  J^({},n) n=0..5 all {} real roots: {}", d, d, all_ok);
    }
}

fn gl48() -> Vec<(f64, f64)> {
    // Gauss-Legendre order 48 nodes/weights (Golub-Welsch via Newton on Legendre)
    let n = 48usize;
    let mut out = Vec::with_capacity(n);
    for j in 0..n {
        let init = (std::f64::consts::PI * (j as f64 + 0.75) / (n as f64 + 0.5)).cos();
        let mut x = init;
        for _ in 0..80 {
            let (p, dp) = legendre(n, x);
            let dx = p / dp;
            x -= dx;
            if dx.abs() < 1e-15 { break; }
        }
        let (_, dp) = legendre(n, x);
        let w = 2.0 / ((1.0 - x * x) * dp * dp);
        out.push((x, w));
    }
    out
}
fn legendre(n: usize, x: f64) -> (f64, f64) {
    let mut p0 = 1.0f64; let mut p1 = x;
    if n == 0 { return (p0, 0.0); }
    for k in 1..n {
        let kf = k as f64;
        let p2 = ((2.0*kf + 1.0) * x * p1 - kf * p0) / (kf + 1.0);
        p0 = p1; p1 = p2;
    }
    let dp = n as f64 * (x * p1 - p0) / (x * x - 1.0);
    (p1, dp)
}
