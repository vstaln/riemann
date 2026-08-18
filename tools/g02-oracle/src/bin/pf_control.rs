// pf_control: adversarial firewall check for the reopened Jensen/PF lane.
// Question: do the finite Toeplitz-PF tests (PF2..PF6) that the zeta Taylor coefficients
// b_k = M_k/(2k)! pass also pass for an RH-false (non-LP) positive-measure world?
//
// Control world: rho(u) = (1/4) sech^2(u/2), the logistic density. Its Fourier transform is
// pi*z/sinh(pi*z), whose zeros are z = i*n — purely imaginary, NOT real. So the cosine/Fourier
// transform of rho is NOT in the Laguerre-Polya class (equivalently: the corresponding
// "Xi-like" function has non-real zeros; this is the operator-lane-polya-density control,
// PROVEN non-LP). We compute M_k = int rho(u) u^{2k} du, b_k = M_k/(2k)!, and run the same
// PF2..PF6 audit. If the control FAILS a finite test that zeta PASSES, the finite tests are
// already discriminating (consistency signal only — never a proof). If it PASSES all, the
// finite tests are weak (expected), confirming the firewall: finite PF is not RH.
use std::f64::consts::PI;

fn main() {
    // moments M_k = int_0^inf (1/4) sech^2(u/2) u^{2k} du by GL quadrature
    let gl = gl48();
    let mut m = vec![0.0f64; 40];
    let umax = 60.0f64;
    let np = 200usize;
    let h = umax / np as f64;
    for k in 0..40usize {
        let mut v = 0.0;
        for p in 0..np {
            let a = p as f64 * h; let b = a + h;
            let mid = 0.5 * (a + b); let half = 0.5 * (b - a);
            for &(x, w) in gl.iter() {
                let u = mid + half * x;
                let rho = 0.25 / (u * 0.5).cosh().powi(2);
                v += half * w * rho * u.powi(2 * k as i32);
            }
        }
        m[k] = v;
    }
    // b_k = M_k/(2k)!
    let mut b = vec![0.0f64; 40];
    for k in 0..40usize {
        let mut fact = 1.0f64;
        for j in 1..=(2 * k) { fact *= j as f64; }
        b[k] = m[k] / fact;
    }
    println!("Control: logistic density rho(u)=(1/4)sech^2(u/2), FT = pi*z/sinh(pi*z), zeros z=in (NON-LP, RH-false-in-sense)");
    for k in 0..8 { println!("  M[{}]={:.6e}  b[{}]={:.6e}", k, m[k], k, b[k]); }

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
            v[i*c+j] = if idx < 0 { 0.0 } else { b[idx as usize] };
        }}
        v
    };
    println!("\nPF audit on control b_k (same tests as zeta):");
    let mut pf2 = true;
    for k in 0..30 { pf2 &= b[k+1]*b[k+1] - b[k]*b[k+2] >= 0.0; }
    println!("  PF2 (log-concavity k=0..29): {}", if pf2 {"PASS (not discriminating at PF2)"} else {"FAIL — discriminates!"});
    let mut pf3 = true;
    for s in 0..20 { for c0 in 0..3 {
        let v = toep(&[s+1,s+2,s+3], &[c0,c0+1,c0+2]);
        let d = det3(&v.try_into().unwrap());
        pf3 &= d >= 0.0;
    }}
    println!("  PF3 (60 3x3 minors): {}", if pf3 {"PASS"} else {"FAIL — discriminates!"});
    let mut pf4 = true;
    for s in 0..12 { for c0 in 0..2 {
        let v = toep(&[s+1,s+2,s+3,s+4], &[c0,c0+1,c0+2,c0+3]);
        let d = det4(&v.try_into().unwrap());
        pf4 &= d >= 0.0;
    }}
    println!("  PF4 (24 4x4 minors): {}", if pf4 {"PASS"} else {"FAIL — discriminates!"});
    let mut pf5 = true;
    for s in 0..6 {
        let v = toep(&[s+1,s+2,s+3,s+4,s+5], &[0,1,2,3,4]);
        let d = det5(&v.try_into().unwrap());
        pf5 &= d >= 0.0;
    }
    println!("  PF5 (6 5x5 minors): {}", if pf5 {"PASS"} else {"FAIL — discriminates!"});
    // first sign where PF5 fails, for detail
    println!("\n  detail: PF3 minors, rows(1,2,3) x cols(c,c+1,c+2), c=0..6:");
    for c0 in 0..7 {
        let v = toep(&[1,2,3], &[c0,c0+1,c0+2]);
        println!("    c={}: {:.4e}", c0, det3(&v.try_into().unwrap()));
    }
    println!("  detail: PF3 minors, rows(s+1,s+2,s+3) x cols(0,1,2), s=0..14:");
    for s in 0..15 {
        let v = toep(&[s+1,s+2,s+3], &[0,1,2]);
        println!("    s={}: {:.4e}", s, det3(&v.try_into().unwrap()));
    }
    println!("  detail: PF5 minors, rows(s+1..s+5) x cols(0..4), s=0..5:");
    for s in 0..6 {
        let v = toep(&[s+1,s+2,s+3,s+4,s+5], &[0,1,2,3,4]);
        println!("    s={}: {:.4e}", s, det5(&v.try_into().unwrap()));
    }
}

fn gl48() -> Vec<(f64, f64)> {
    let n = 48usize;
    let mut out = Vec::with_capacity(n);
    for j in 0..n {
        let init = (PI * (j as f64 + 0.75) / (n as f64 + 0.5)).cos();
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
