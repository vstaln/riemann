// Wave 8D: Turan/Laguerre inequalities on Xi's Taylor coefficients.
// Xi(t) = xi(1/2+it) = 2 * int_0^inf Phi(u) cos(tu) du,
//   Phi(u) = 2 * sum_{n>=1} (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}
//   (corrected classical form; derived from scratch: Phi = H'' - H/4, H = sum e^{u/2} e^{-pi n^2 e^{2u}},
//    constant 1/2 + 2H'(0) = 0 exactly via theta identity 4 pi sum n^2 e^{-pi n^2} = 1/2 + sum e^{-pi n^2})
// b_k = M_k/(2k)!,  M_k = 2 int_0^inf Phi(u) u^{2k} du,  Xi(t) = sum_k (-1)^k b_k t^{2k}
// Turan: T_k = b_k^2 - b_{k-1} b_{k+1};  normalized margin t_k = T_k/b_k^2.
//   b_k^2 >= b_{k-1}b_{k+1}  <=>  R_k := M_k^2/(M_{k-1}M_{k+1}) >= c_k, c_k = (2k)(2k-1)/((2k+1)(2k+2)) ~ 1 - 2/k.
//   Raw C-S gives R_k <= 1 (log-convexity), wrong direction => T_k >= 0 is NON-trivial.
//   Newton's inequality (all zeros real => b_k = Xi(0) e_k(1/gamma^2), e_k^2 >= e_{k-1}e_{k+1}(k+1)/k):
//   NECESSARY for RH:  t_k >= 1/(k+1) for all k.
// Laguerre: L_k(t) = (Xi^(k)(t))^2 - Xi^(k-1)(t) Xi^(k+1)(t) >= 0  (k>=1, all t)  <=> Xi in LP <=> RH.
use rug::{Float, ops::Pow};
use std::time::Instant;

const PREC: u32 = 128; // ~38 digits (margins ~1e-3; rel accuracy 1e-10 suffices)

fn pi(prec: u32) -> Float { Float::with_val(prec, rug::float::Constant::Pi) }
fn mul(a: &Float, b: &Float, prec: u32) -> Float { Float::with_val(prec, a * b) }
fn sub(a: &Float, b: &Float, prec: u32) -> Float { Float::with_val(prec, a - b) }

// Phi(u) = 2 sum_{n>=1} (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}
fn phi(u: &Float, prec: u32) -> Float {
    let p = pi(prec);
    let eu = u.clone().exp();
    let e2u = mul(&eu, &eu, prec);
    let sq = eu.sqrt();                                  // e^{u/2}
    let e4u = mul(&e2u, &e2u, prec);
    let e9h = mul(&e4u, &sq, prec);                      // e^{9u/2}
    let e5h = mul(&e2u, &sq, prec);                      // e^{5u/2}
    let mut two_pp = Float::with_val(prec, 2.0);
    two_pp *= &p;
    two_pp *= &p;                                        // 2 pi^2
    let mut three_p = Float::with_val(prec, 3.0);
    three_p *= &p;                                       // 3 pi
    let two = Float::with_val(prec, 2.0);
    let eps = Float::with_val(prec, 1e-50);
    let mut s = Float::with_val(prec, 0);
    let mut n = 1u64;
    loop {
        let nf = Float::with_val(prec, n);
        let n2 = mul(&nf, &nf, prec);
        let n4 = mul(&n2, &n2, prec);
        let pn2 = mul(&p, &n2, prec);
        let arg = mul(&pn2, &e2u, prec);                 // pi n^2 e^{2u}
        let t1 = mul(&two_pp, &n4, prec);
        let t1 = mul(&t1, &e9h, prec);
        let t2 = mul(&three_p, &n2, prec);
        let t2 = mul(&t2, &e5h, prec);
        let inner = sub(&t1, &t2, prec);
        let mut term = Float::with_val(prec, &inner * &(-arg).exp());
        term *= &two;
        let mag = term.clone().abs();
        s += &term;
        if mag < &eps * s.clone().abs() && n > 1 { break; }
        n += 1;
        if n > 3000 { break; }
    }
    s
}

// Rigorous tail bound for int_U^inf Phi(u) u^{2k} du (see derivation in note)
fn phi_tail_bound(u: &Float, prec: u32) -> Float {
    let p = pi(prec);
    let e2u = (2.0_f64 * u.to_f64()).exp();
    if e2u < 2.0 { return Float::with_val(prec, f64::INFINITY); }
    let fac = 1.0_f64 + 16.0_f64 * (-6.0_f64 * std::f64::consts::PI).exp()
             + 81.0_f64 * (-16.0_f64 * std::f64::consts::PI).exp()
             + 256.0_f64 * (-30.0_f64 * std::f64::consts::PI).exp();
    let z = mul(&p, &Float::with_val(prec, e2u), prec);
    let z = Float::with_val(prec, &z / 2.0_f64);
    let pp = mul(&p, &p, prec);
    let c = Float::with_val(prec, Float::with_val(prec, 4.0) * &pp);
    let c = Float::with_val(prec, &c * fac);
    let num = Float::with_val(prec, &c * &(-z.clone()).exp());
    let den = Float::with_val(prec, Float::with_val(prec, 2.0) * &z);
    Float::with_val(prec, &num / &den)
}

// adaptive Simpson on [a,b] of f; returns (value, est_error)
fn adapt_simpson<F: Fn(&Float) -> Float>(f: &F, a: &Float, b: &Float, tol: &Float, depth: u32) -> (Float, Float) {
    let mid = Float::with_val(PREC, (a.clone() + b.clone()) / 2.0_f64);
    let fa = f(a); let fm = f(&mid); let fb = f(b);
    let fm4 = Float::with_val(PREC, Float::with_val(PREC, 4.0) * &fm);
    let s_ab = Float::with_val(PREC, (fa.clone() + &fm4 + fb.clone()) * (b.clone() - a) / 6.0_f64);
    let lmid = Float::with_val(PREC, (a.clone() + &mid) / 2.0_f64);
    let rmid = Float::with_val(PREC, (mid.clone() + b) / 2.0_f64);
    let fl = f(&lmid); let fr = f(&rmid);
    let fl4 = Float::with_val(PREC, Float::with_val(PREC, 4.0) * &fl);
    let fr4 = Float::with_val(PREC, Float::with_val(PREC, 4.0) * &fr);
    let s_l = Float::with_val(PREC, (fa + &fl4 + fm.clone()) * (mid.clone() - a) / 6.0_f64);
    let s_r = Float::with_val(PREC, (fm + &fr4 + fb) * (b.clone() - &mid) / 6.0_f64);
    let s2 = s_l + s_r;
    let err = Float::with_val(PREC, (s2.clone() - s_ab).abs() / 15.0_f64);
    // relative tol with tiny absolute floor (floor must be << M_k for small k, else the
    // sharp peak can be missed entirely and the estimator terminates prematurely)
    let rhs = Float::with_val(PREC, tol * &s2.clone().abs());
    let rhs = Float::with_val(PREC, &rhs + Float::with_val(PREC, 1e-28));
    if depth == 0 || err < rhs {
        (s2, err)
    } else {
        let (l, el) = adapt_simpson(f, a, &mid, tol, depth - 1);
        let (r, er) = adapt_simpson(f, &mid, b, tol, depth - 1);
        (l + r, el + er)
    }
}

// M_k = 2 int_0^Umax Phi(u) u^{2k} du  (tail bound returned separately)
fn moment(k: u64, prec: u32) -> (Float, Float) {
    let mut ustar = 1.0_f64;
    for _ in 0..10 {
        let e2u = (k as f64) / (std::f64::consts::PI * ustar.max(0.3));
        ustar = 0.5 * e2u.ln();
        if !(ustar.is_finite() && ustar > 0.0) { ustar = 1.0; break; }
    }
    let umax = ustar + 4.5;
    let f = |u: &Float| -> Float { mul(&phi(u, prec), &u.clone().pow(2 * k as u32), prec) };
    let tol = Float::with_val(prec, 1e-13);
    let a = Float::with_val(prec, 0);
    let b = Float::with_val(prec, umax);
    let (val, err) = adapt_simpson(&f, &a, &b, &tol, 34);
    let tail = mul(&phi_tail_bound(&b, prec), &Float::with_val(prec, umax).pow(2 * k as u32), prec);
    let two = Float::with_val(prec, 2.0);
    let v = Float::with_val(prec, &two * &val);
    let e1 = Float::with_val(prec, &two * &err);
    let e2 = Float::with_val(prec, &two * &tail);
    let e = Float::with_val(prec, &e1 + &e2);
    (v, e)
}

fn factorial2k(k: u64, prec: u32) -> Float {
    let mut r = Float::with_val(prec, 1);
    for i in 1..=2 * k { r *= i; }
    r
}

// Xi^(m)(t) = sum_j (-1)^j b_j (2j)!/(2j-m)! t^{2j-m}
fn xi_deriv(b: &[Float], m: u64, t: &Float, prec: u32) -> Float {
    let mut s = Float::with_val(prec, 0);
    let mut j = (m + 1) / 2;
    let t2 = t.clone().square();
    loop {
        let jf = Float::with_val(prec, j);
        let mut falling = Float::with_val(prec, 1);
        for q in 0..m {
            let mut fac = Float::with_val(prec, Float::with_val(prec, 2.0) * &jf);
            fac -= q as f64;
            falling *= fac;
        }
        let pw = 2 * j - m;
        let tp = if pw == 0 {
            Float::with_val(prec, 1)
        } else if pw % 2 == 0 {
            t2.clone().pow((pw / 2) as u32)
        } else {
            mul(&t2.clone().pow(((pw - 1) / 2) as u32), t, prec)
        };
        let mut term = mul(&b[j as usize].clone(), &falling, prec);
        term *= &tp;
        if j % 2 == 0 { s += &term; } else { s -= &term; }
        if term.clone().abs() < Float::with_val(prec, 1e-40) * s.clone().abs() && j > 80 { break; }
        j += 1;
        if j >= b.len() as u64 { break; }
    }
    s
}

fn xi_eval(b: &[Float], t: &Float, prec: u32) -> Float {
    let mut s = Float::with_val(prec, 0);
    let t2 = t.clone().square();
    for (j, bj) in b.iter().enumerate() {
        let term = mul(bj, &t2.clone().pow(j as u32), prec);
        if j % 2 == 0 { s += &term; } else { s -= &term; }
        if term.clone().abs() < Float::with_val(prec, 1e-40) * s.clone().abs() && j > 80 { break; }
    }
    s
}

// ---------------- control ----------------
// poly: P(t) = sum_k c_k t^{2k}, c_k = (-1)^k e_k (p = c coefficients)
// P^(m)(t) = sum_k c_k (2k)!/(2k-m)! t^{2k-m}
fn poly_deriv(p: &[f64], m: u64, t: &Float, prec: u32) -> Float {
    let mut s = Float::with_val(prec, 0);
    let t2 = t.clone().square();
    for (k, &pk) in p.iter().enumerate() {
        let kk = k as u64;
        if 2 * kk < m { continue; }
        let mut falling = Float::with_val(prec, 1);
        for q in 0..m {
            let mut fac = Float::with_val(prec, Float::with_val(prec, 2.0) * kk as f64);
            fac -= q as f64;
            falling *= fac;
        }
        let pw = 2 * kk - m;
        let tp = if pw == 0 {
            Float::with_val(prec, 1)
        } else if pw % 2 == 0 {
            t2.clone().pow((pw / 2) as u32)
        } else {
            mul(&t2.clone().pow(((pw - 1) / 2) as u32), t, prec)
        };
        let mut term = mul(&Float::with_val(prec, pk), &falling, prec);
        term *= &tp;
        s += term;
    }
    s
}

// scan L_k(t) for k=1..k_hi; return first (k,t,L) with L<0, and global min
fn laguerre_scan(p: &[f64], name: &str, k_hi: u64, tmax: f64, step: f64) {
    let prec = PREC;
    let mut any_neg: Option<(u64, f64, f64)> = None;
    let mut gmin = f64::INFINITY;
    let mut gk = 0u64;
    let mut gt = 0.0_f64;
    for k in 1..=k_hi {
        let mut t = 0.0_f64;
        while t <= tmax + 1e-9 {
            let tf = Float::with_val(prec, t);
            let dk = poly_deriv(p, k, &tf, prec);
            let dkm1 = poly_deriv(p, k - 1, &tf, prec);
            let dkp1 = poly_deriv(p, k + 1, &tf, prec);
            let lk = Float::with_val(prec, dk.clone().square() - dkm1 * dkp1);
            let lkf = lk.to_f64();
            if lkf < gmin { gmin = lkf; gk = k; gt = t; }
            if lkf < 0.0 && any_neg.is_none() {
                any_neg = Some((k, t, lkf));
                println!("  {}: FIRST L_k(t) < 0 at k={}, t={:.3}: L_k = {:.4e}", name, k, t, lkf);
            }
            t += step;
        }
    }
    match any_neg {
        Some((k, t, _)) => println!("  {}: FAILS Laguerre at k={}, t={:.3}  -> NOT LP (non-real zeros)", name, k, t),
        None => println!("  {}: all L_k(t) >= 0 for k=1..{} on [0,{}] (global min {:.4e} at k={}, t={:.2})", name, k_hi, tmax, gmin, gk, gt),
    }
}

fn control(plant: bool) {
    let gammas: [f64; 15] = [
        14.13472514173469379, 21.02203963877155499, 25.01085758014568876, 30.42487612585951321,
        32.93506158773918569, 37.58617815882567126, 40.91871901214749519, 43.32707328091499952,
        48.00515088116715973, 49.77383247767230218, 52.97032147771446064, 56.44624769706339480,
        59.34704400260235308, 60.83177852460980984, 65.11254404808160666,
    ];
    let n = gammas.len();
    let mut p: Vec<f64> = vec![1.0];
    for i in 0..n {
        let (a, bq) = if plant && i == 1 {
            let beta = 0.35; let gh = 21.1;
            let re = beta * beta - gh * gh;
            let im = 2.0 * beta * gh;
            let denom = re * re + im * im;
            (2.0 * re / denom, 1.0 / denom)
        } else {
            (1.0 / (gammas[i] * gammas[i]), 0.0)
        };
        let mut np = vec![0.0; p.len() + 2];
        for (k, &pk) in p.iter().enumerate() {
            np[k] += pk;
            np[k + 1] -= a * pk;
            np[k + 2] += bq * pk;
        }
        p = np;
    }
    println!("=== CONTROL ({}) ===", if plant { "planted off-line pair beta=0.35+-21.1i (replaces gamma_2)" } else { "all-real zeros" });
    let mut first_fail: Option<usize> = None;
    let mut min_tk = f64::INFINITY;
    let mut min_k = 0usize;
    let mut min_ratio = f64::INFINITY;
    for k in 1..p.len() - 1 {
        let tk = p[k] * p[k] - p[k - 1] * p[k + 1];
        let tkn = tk / (p[k] * p[k]);
        if tkn < min_tk { min_tk = tkn; min_k = k; }
        let ratio = tkn / (1.0 / (k as f64 + 1.0));
        if ratio < min_ratio { min_ratio = ratio; }
        if tk < 0.0 && first_fail.is_none() {
            first_fail = Some(k);
            println!("  FIRST T_k < 0 at k = {}: T_k = {:.6e}, t_k = {:.6e}", k, tk, tkn);
        }
    }
    match first_fail {
        Some(k) => println!("  FAILS Turan at k = {}", k),
        None => println!("  no negative T_k for k=1..{}", p.len() - 2),
    }
    println!("  min t_k = {:.6e} at k = {}", min_tk, min_k);
    println!("  min t_k/(1/(k+1)) = {:.6e}  (RH-necessary would be >= 1)", min_ratio);
    // L_k scan, k=1..8, fine grid
    laguerre_scan(&p, if plant { "planted(beta=0.35)" } else { "all-real" }, 8, 60.0, 0.05);
}

// control with a strongly off-line pair (beta=5.0)
fn control_far() {
    let gammas: [f64; 15] = [
        14.13472514173469379, 21.02203963877155499, 25.01085758014568876, 30.42487612585951321,
        32.93506158773918569, 37.58617815882567126, 40.91871901214749519, 43.32707328091499952,
        48.00515088116715973, 49.77383247767230218, 52.97032147771446064, 56.44624769706339480,
        59.34704400260235308, 60.83177852460980984, 65.11254404808160666,
    ];
    let mut p: Vec<f64> = vec![1.0];
    for i in 0..gammas.len() {
        let (a, bq) = if i == 1 {
            let beta = 5.0; let gh = 21.1;
            let re = beta * beta - gh * gh;
            let im = 2.0 * beta * gh;
            let denom = re * re + im * im;
            (2.0 * re / denom, 1.0 / denom)
        } else {
            (1.0 / (gammas[i] * gammas[i]), 0.0)
        };
        let mut np = vec![0.0; p.len() + 2];
        for (k, &pk) in p.iter().enumerate() {
            np[k] += pk;
            np[k + 1] -= a * pk;
            np[k + 2] += bq * pk;
        }
        p = np;
    }
    let mut first_fail: Option<usize> = None;
    let mut min_tk = f64::INFINITY;
    for k in 1..p.len() - 1 {
        let tk = p[k] * p[k] - p[k - 1] * p[k + 1];
        let tkn = tk / (p[k] * p[k]);
        if tkn < min_tk { min_tk = tkn; }
        if tk < 0.0 && first_fail.is_none() {
            first_fail = Some(k);
            println!("  planted(beta=5.0): FIRST T_k < 0 at k = {}: T_k = {:.6e}, t_k = {:.6e}", k, tk, tkn);
        }
    }
    match first_fail {
        Some(k) => println!("  planted(beta=5.0): FAILS Turan at k = {}", k),
        None => println!("  planted(beta=5.0): no negative T_k (min t_k = {:.4e})", min_tk),
    }
    laguerre_scan(&p, "planted(beta=5.0)", 8, 60.0, 0.05);
}

// ---------------- real Xi ----------------
fn real_case() {
    let t0 = Instant::now();
    let k_max = 200u64;
    let mut b: Vec<Float> = Vec::with_capacity(k_max as usize + 1);
    let mut max_rel_err = Float::with_val(PREC, 0);
    for k in 0..=k_max {
        let (mk, err) = moment(k, PREC);
        let rel = Float::with_val(PREC, &err / &mk.clone().abs());
        if rel > max_rel_err { max_rel_err = rel.clone(); }
        let bk = Float::with_val(PREC, &mk / &factorial2k(k, PREC));
        if k % 10 == 0 {
            println!("  k={}: M_k~{:.6e} b_k~{:.6e} est.rel.err={:.1e}", k, mk.to_f64(), bk.to_f64(), rel.to_f64());
        }
        b.push(bk);
    }
    println!("moments done in {:.1}s, max est rel err = {:.1e}", t0.elapsed().as_secs_f64(), max_rel_err.to_f64());
    println!("VALIDATION: b_0 = {:.15}  (xi(1/2) = 0.497120778188314)", b[0].to_f64());

    // roots of Xi(t)
    let mut root_t: Vec<f64> = Vec::new();
    let mut tprev = 0.0_f64;
    let mut vprev = xi_eval(&b, &Float::with_val(PREC, 0.0), PREC).to_f64();
    for i in 1..=1400 {
        let t = i as f64 * 0.05;
        let v = xi_eval(&b, &Float::with_val(PREC, t), PREC).to_f64();
        if vprev != 0.0 && v / vprev < 0.0 {
            let mut lo = tprev; let mut hi = t;
            let sgn = vprev > 0.0;
            for _ in 0..80 {
                let mid = 0.5 * (lo + hi);
                let vm = xi_eval(&b, &Float::with_val(PREC, mid), PREC).to_f64();
                if (vm > 0.0) == sgn { lo = mid; } else { hi = mid; }
            }
            root_t.push(0.5 * (lo + hi));
        }
        tprev = t; vprev = v;
        if root_t.len() >= 4 { break; }
    }
    let known = [14.134725, 21.022040, 25.010858, 30.424876];
    for (i, r) in root_t.iter().enumerate() {
        println!("  VALIDATION root {} = {:.6}  vs gamma_{} = {:.6}", i + 1, r, i + 1, known[i]);
    }

    // Turan
    println!("=== TURAN ===");
    let mut min_tk = Float::with_val(PREC, f64::INFINITY);
    let mut min_k = 0u64;
    let mut min_ratio = Float::with_val(PREC, f64::INFINITY);
    let mut min_ratio_k = 0u64;
    let mut any_neg = false;
    for k in 1..=k_max {
        let bk = b[k as usize].clone();
        let tkn = Float::with_val(PREC, &bk.clone().square() - &(mul(&b[(k - 1) as usize], &b[(k + 1) as usize], PREC)));
        let tkn = Float::with_val(PREC, &tkn / &bk.clone().square());
        if tkn < min_tk { min_tk = tkn.clone(); min_k = k; }
        let ratio = Float::with_val(PREC, &tkn * (k as f64 + 1.0));
        if ratio < min_ratio { min_ratio = ratio.clone(); min_ratio_k = k; }
        if tkn.to_f64() < 0.0 { any_neg = true; println!("  !!! T_k < 0 at k = {}: T_k = {:.4e}", k, tkn.to_f64()); }
        if k % 20 == 0 {
            println!("  k={}: t_k={:.8e}  t_k*(k+1)={:.8e}", k, tkn.to_f64(), ratio.to_f64());
        }
    }
    println!("  min t_k = {:.8e} at k = {}", min_tk.to_f64(), min_k);
    println!("  min t_k*(k+1) = {:.8e} at k = {}  (RH-necessary: >= 1)", min_ratio.to_f64(), min_ratio_k);
    if any_neg { println!("  !!! NEGATIVE T_k FOUND -> RH DISPROOF. ESCALATE."); }
    let mut ys = Vec::new();
    for k in (k_max - 60)..=k_max {
        let bk = b[k as usize].clone();
        let tk = Float::with_val(PREC, &bk.clone().square() - &(mul(&b[(k - 1) as usize], &b[(k + 1) as usize], PREC)));
        let tkn = Float::with_val(PREC, &tk / &bk.clone().square());
        ys.push(((k as f64).ln(), tkn.to_f64().ln()));
    }
    let n = ys.len() as f64;
    let sx: f64 = ys.iter().map(|x| x.0).sum();
    let sy: f64 = ys.iter().map(|x| x.1).sum();
    let sxx: f64 = ys.iter().map(|x| x.0 * x.0).sum();
    let sxy: f64 = ys.iter().map(|x| x.0 * x.1).sum();
    let pp = (n * sxy - sx * sy) / (n * sxx - sx * sx);
    let logc = (sy - pp * sx) / n;
    println!("  tail fit (k={}..{}): t_k ~ {:.4e} * k^({:.3})", k_max - 60, k_max, logc.exp(), pp);

    // Laguerre grid
    println!("=== LAGUERRE L_k(t), t in [0,40], step 0.25 ===");
    let mut global_min = Float::with_val(PREC, f64::INFINITY);
    let mut gmin_k = 0u64;
    let mut gmin_t = 0.0_f64;
    let mut any_lneg = false;
    for k in 1..=20u64 {
        let mut kmin = Float::with_val(PREC, f64::INFINITY);
        let mut kmin_t = 0.0_f64;
        let mut t = 0.0_f64;
        while t <= 40.0 + 1e-9 {
            let tf = Float::with_val(PREC, t);
            let dk = xi_deriv(&b, k, &tf, PREC);
            let dkm1 = xi_deriv(&b, k - 1, &tf, PREC);
            let dkp1 = xi_deriv(&b, k + 1, &tf, PREC);
            let lk = Float::with_val(PREC, dk.clone().square() - dkm1 * dkp1);
            let lkf = lk.to_f64();
            if lkf < kmin.to_f64() { kmin = lk.clone(); kmin_t = t; }
            if lkf < global_min.to_f64() { global_min = lk.clone(); gmin_k = k; gmin_t = t; }
            if lkf < 0.0 && !any_lneg {
                any_lneg = true;
                println!("  !!! L_k(t) < 0 at k={}, t={:.2}: L_k = {:.4e} -> RH DISPROOF. ESCALATE.", k, t, lkf);
            }
            t += 0.25;
        }
        println!("  k={}: min L_k = {:.6e} (rel to b_0^2: {:.2e}) at t = {:.2}", k, kmin.to_f64(), (kmin.clone() / b[0].clone().square()).to_f64(), kmin_t);
    }
    println!("  GLOBAL min L_k = {:.6e} at k={}, t={:.2}", global_min.to_f64(), gmin_k, gmin_t);
    if !any_lneg {
        println!("  all L_k(t) >= 0 on the grid");
    }
    println!("total time {:.1}s", t0.elapsed().as_secs_f64());
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() > 1 && args[1] == "control" {
        control(false);
        control(true);
        control_far();
        return;
    }
    control(false);
    control(true);
    real_case();
}
