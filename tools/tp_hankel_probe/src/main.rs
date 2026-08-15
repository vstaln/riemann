// tp_hankel_probe — Hankel-minor sign test for the moment sequence b_k = M_k/(2k)!,
// M_k = 2 int_0^inf Phi(u) u^{2k} du,  Phi(u) = 2 sum_n (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}.
// Question (brief g0-0/g3-0): is the Hankel matrix (b_{i+j}) totally positive?
// Expected answer (PROVEN in note): NO — under RH the Hankel minors ALTERNATE in sign
// with (-1)^{r(r-1)/2}; the overlapping 2x2 minors equal -T_k (Turan), negative under RH.
// Detector: real case must alternate; planted control (one complex zero pair) must break it.
// f64, std only, < 1 min.

fn phi(u: f64) -> f64 {
    // Phi(u) = 2 sum_{n>=1} (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}
    let pi = std::f64::consts::PI;
    let mut s = 0.0;
    let e2u = (2.0 * u).exp();
    let e92 = (4.5 * u).exp();
    let e52 = (2.5 * u).exp();
    for n in 1..40u32 {
        let nn = (n * n) as f64;
        let term = (2.0 * pi * pi * nn * nn * e92 - 3.0 * pi * nn * e52) * (-pi * nn * e2u).exp();
        s += term;
        if term.abs() < 1e-320 {
            break;
        }
    }
    2.0 * s
}

// composite Simpson on [0,3], 2^18 subintervals; f array precomputed at nodes
fn simpson(f: &[f64], n: usize, h: f64) -> f64 {
    // f has n+1 points on [0, n*h]
    let mut s = f[0] + f[n];
    for i in 1..n {
        s += if i % 2 == 0 { 2.0 } else { 4.0 } * f[i];
    }
    s * h / 3.0
}

// determinant via LU with partial pivoting; returns (sign, log10|det|, det)
fn det_lu(a: &[f64], n: usize) -> (i32, f64, f64) {
    let mut m = a.to_vec();
    let mut sign = 1i32;
    for k in 0..n {
        let mut piv = k;
        let mut mx = m[k * n + k].abs();
        for i in (k + 1)..n {
            let v = m[i * n + k].abs();
            if v > mx {
                mx = v;
                piv = i;
            }
        }
        if mx == 0.0 {
            return (0, -f64::INFINITY, 0.0);
        }
        if piv != k {
            for j in 0..n {
                m.swap(k * n + j, piv * n + j);
            }
            sign = -sign;
        }
        let pv = m[k * n + k];
        for i in (k + 1)..n {
            let f = m[i * n + k] / pv;
            m[i * n + k] = 0.0;
            for j in (k + 1)..n {
                m[i * n + j] -= f * m[k * n + j];
            }
        }
    }
    let mut d = 1.0f64;
    let mut ld = 0.0f64;
    for i in 0..n {
        d *= m[i * n + i];
        ld += m[i * n + i].abs().log10();
    }
    // true sign = permutation sign * sign of pivot product
    let true_sign = sign * if d < 0.0 { -1 } else { 1 };
    (true_sign, ld, d)
}

fn hankel_scan(b: &[f64], name: &str) {
    println!("== {} ==", name);
    // overlapping 2x2 minors = -T_k
    let mut first_fail: Option<usize> = None;
    let mut min_tk = f64::INFINITY;
    let mut min_k = 0usize;
    let mut min_ratio = f64::INFINITY;
    for k in 1..b.len() - 1 {
        let tk = b[k] * b[k] - b[k - 1] * b[k + 1];
        let tkn = tk / (b[k] * b[k]);
        if tkn < min_tk {
            min_tk = tkn;
            min_k = k;
        }
        let ratio = tkn * (k as f64 + 1.0);
        if ratio < min_ratio {
            min_ratio = ratio;
        }
        if tk < 0.0 && first_fail.is_none() {
            first_fail = Some(k);
            println!("  FIRST T_k < 0 at k={}: T_k={:.6e} t_k={:.6e}", k, tk, tkn);
        }
    }
    match first_fail {
        Some(k) => println!("  Turan FAILS at k={}", k),
        None => println!("  T_k > 0 for k=1..{} (no Turan fail)", b.len() - 2),
    }
    println!("  min t_k = {:.6e} at k={};  min t_k*(k+1) = {:.6e} (RH-necessary: >= 1)", min_tk, min_k, min_ratio);
    // leading principal Hankel minors D_n = det(b_{i+j})_{0<=i,j<=n}, n=1..8
    for n in 1..=8usize {
        let mut h = vec![0.0f64; (n + 1) * (n + 1)];
        for i in 0..=n {
            for j in 0..=n {
                h[i * (n + 1) + j] = b[i + j];
            }
        }
        let (sg, ld, _) = det_lu(&h, n + 1);
        let expect = if (n * (n + 1) / 2) % 2 == 0 { 1 } else { -1 };
        let ok = sg == expect && sg != 0;
        println!(
            "  D_{} = det(b_{{i+j}})_{{0..{}}} : sign={}{}  log10|D|={:+.1}  expected {} {}",
            n, n, if sg >= 0 { "+" } else { "-" },
            if sg == 0 { "(zero)" } else { "" }, ld, if expect > 0 { "+" } else { "-" },
            if ok { "OK" } else { "<-- WRONG SIGN" }
        );
    }
}

fn moments_bk(kmax: usize) -> Vec<f64> {
    // composite Simpson on [0,3], 2^18 intervals; Phi nodes computed once
    let n = 1 << 18;
    let a = 0.0f64;
    let b = 3.0f64;
    let h = (b - a) / n as f64;
    let mut phis = vec![0.0f64; n + 1];
    for i in 0..=n {
        let u = a + i as f64 * h;
        phis[i] = phi(u);
    }
    let mut bk = vec![0.0f64; kmax + 1];
    let mut f = vec![0.0f64; n + 1];
    let mut fac = 1.0f64; // (2k)!
    for k in 0..=kmax {
        for i in 0..=n {
            let u = a + i as f64 * h;
            f[i] = phis[i] * u.powi(2 * k as i32);
        }
        let mk = 2.0 * simpson(&f, n, h);
        if k > 0 {
            fac *= (2 * k) as f64 * (2 * k - 1) as f64;
        }
        bk[k] = mk / fac;
    }
    bk
}

fn control_bk(plant: bool, kmax: usize) -> Vec<f64> {
    // b_k = e_k(1/rho^2) over first 15 zeta-zero heights, one pair optionally planted (replaces gamma_2)
    let gammas: [f64; 15] = [
        14.13472514173469379, 21.02203963877155499, 25.01085758014568876, 30.42487612585951321,
        32.93506158773918569, 37.58617815882567126, 40.91871901214749519, 43.32707328091499952,
        48.00515088116715973, 49.77383247767230218, 52.97032147771446064, 56.44624769706339480,
        59.34704400260235308, 60.83177852460980984, 65.11254404808160666,
    ];
    let mut p = vec![0.0f64; kmax + 1];
    p[0] = 1.0;
    for i in 0..gammas.len() {
        if plant && i == 1 {
            // replace gamma_2 by complex pair 0.35 +/- 21.1 i
            let beta = 0.35f64;
            let gh = 21.1f64;
            let re = beta * beta - gh * gh;
            let im = 2.0 * beta * gh;
            let denom = re * re + im * im;
            // (1 + x/rho^2)(1 + x/conj(rho)^2) = 1 + (2 re/denom) x + (1/denom) x^2
            let a = 2.0 * re / denom;
            let bq = 1.0 / denom;
            let mut np = vec![0.0f64; kmax + 1];
            for k in 0..=kmax {
                if p[k] != 0.0 {
                    np[k] += p[k];
                    if k + 1 <= kmax {
                        np[k + 1] += a * p[k];
                    }
                    if k + 2 <= kmax {
                        np[k + 2] += bq * p[k];
                    }
                }
            }
            p = np;
        } else {
            let a = 1.0 / (gammas[i] * gammas[i]);
            for k in (0..=kmax).rev() {
                p[k] = if k > 0 { p[k] + a * p[k - 1] } else { p[k] };
            }
        }
    }
    p
}

fn main() {
    let kmax = 16usize;
    println!("=== REAL b_k from Phi quadrature (k=0..{}) ===", kmax);
    let bk = moments_bk(kmax);
    for (k, &v) in bk.iter().enumerate() {
        println!("  b_{} = {:.10e}", k, v);
    }
    println!("  sanity: b_0 should be xi(1/2) = 0.49712077818831391;  b_10 ~ 5.62e-25 (wave8d-run5)");
    hankel_scan(&bk, "REAL case (b_k = M_k/(2k)!, Phi > 0)");

    println!();
    let allreal = control_bk(false, kmax);
    hankel_scan(&allreal, "CONTROL all-real (15 zeta-zero heights)");

    println!();
    let planted = control_bk(true, kmax);
    hankel_scan(&planted, "CONTROL planted (gamma_2 -> 0.35 +/- 21.1 i)");

    println!();
    println!("Verdict key: real case must satisfy T_k>0 (k=1..15) AND D_n sign = (-1)^{{n(n+1)/2}} for n=1..8;");
    println!("planted control must break at least one of these, else the discriminator is dead.");
}
