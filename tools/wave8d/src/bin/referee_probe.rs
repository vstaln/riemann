// referee_probe.rs — INDEPENDENT hostile cross-check of lk_zeta_mpfr.rs
// Different mechanisms: (1) Pochhammer (s)_{2k-1} differentiated via
//   signed Stirling numbers of the first kind (not Bell composition);
// (2) |Gamma| via log-modulus with CORRECT exponents z^{1-2k};
// (3) 256-bit throughout. q_k = Bell(u')^2 - ... same identity, checked.
// Also: direct high-precision central differences of ln|xi| for q_3(40).

#[path = "../em.rs"]
mod em;

use rug::float::Constant;
use rug::{Assign, Float, Integer};

const PREC: u32 = 256;
const N_EM: usize = 600;
const K_MAX: usize = 40;
const SHIFT: usize = 40;
const KP: usize = 28;
const M_MAX_G: usize = 79; // max 2*K_MAX-1

type C = (Float, Float);

fn zf(v: f64) -> Float { Float::with_val(PREC, v) }
fn pi() -> Float { Float::with_val(PREC, Constant::Pi) }
fn neg(a: &Float) -> Float { Float::with_val(PREC, -a) }
fn ln_(x: &Float) -> Float { Float::with_val(PREC, x.ln_ref()) }
fn exp_(x: &Float) -> Float { Float::with_val(PREC, x.exp_ref()) }
fn add(a: &Float, b: &Float) -> Float { Float::with_val(PREC, a + b) }
fn sub(a: &Float, b: &Float) -> Float { Float::with_val(PREC, a - b) }
fn mul(a: &Float, b: &Float) -> Float { Float::with_val(PREC, a * b) }
fn div(a: &Float, b: &Float) -> Float { Float::with_val(PREC, a / b) }
fn abs_(a: &Float) -> Float { Float::with_val(PREC, a.abs_ref()) }

fn cadd(a: &C, b: &C) -> C { (add(&a.0, &b.0), add(&a.1, &b.1)) }
fn csub(a: &C, b: &C) -> C { (sub(&a.0, &b.0), sub(&a.1, &b.1)) }
fn cmul(a: &C, b: &C) -> C {
    (sub(&mul(&a.0, &b.0), &mul(&a.1, &b.1)), add(&mul(&a.0, &b.1), &mul(&a.1, &b.0)))
}
fn cscale(s: &Float, a: &C) -> C { (mul(s, &a.0), mul(s, &a.1)) }
fn cinv(a: &C) -> C {
    let d2 = add(&mul(&a.0, &a.0), &mul(&a.1, &a.1));
    (div(&a.0, &d2), div(&neg(&a.1), &d2))
}
fn cmag(a: &C) -> Float { (add(&mul(&a.0, &a.0), &mul(&a.1, &a.1))).sqrt() }

static mut FACT_CACHE: Option<Vec<Float>> = None;
fn fact(m: usize) -> Float {
    unsafe {
        if FACT_CACHE.is_none() {
            let mut v = Vec::with_capacity(85);
            for n in 0..=84 {
                if n <= 1 { v.push(zf(1.0)); } else {
                    let i = Integer::from(Integer::factorial(n as u32));
                    v.push(Float::with_val(PREC, &i));
                }
            }
            FACT_CACHE = Some(v);
        }
        FACT_CACHE.as_ref().unwrap()[m].clone()
    }
}
fn binom(n: usize, j: usize) -> Float {
    if j > n { return zf(0.0); }
    let num = Integer::from(Integer::factorial(n as u32));
    let den = Integer::from(Integer::factorial(j as u32)) * Integer::from(Integer::factorial((n - j) as u32));
    Float::with_val(PREC, &num) / Float::with_val(PREC, &den)
}

fn zeta_even(k: usize) -> Float {
    let p = pi();
    if k <= 6 {
        let (num, den): (f64, f64) = match k {
            1 => (1.0, 6.0), 2 => (1.0, 90.0), 3 => (1.0, 945.0),
            4 => (1.0, 9450.0), 5 => (1.0, 93555.0), _ => (691.0, 638512875.0),
        };
        div(&mul(&exp_(&mul(&zf((2 * k) as f64), &ln_(&p))), &zf(num)), &zf(den))
    } else {
        // direct sum: zeta(2k) = 1 + sum_{m>=2} m^{-2k}, tail < 2^{-(prec+20)}
        let c = mul(&(zf(1.0) >> (PREC + 20)), &zf((2 * k - 1) as f64));
        let me = exp_(&div(&ln_(&c), &zf(-((2 * k) as f64) + 1.0)));
        let m = me.to_f64().ceil() as u64 + 2;
        let mut sum = zf(1.0);
        for mi in 2..=m {
            sum += exp_(&mul(&zf(-((2 * k) as f64)), &ln_(&zf(mi as f64))));
        }
        sum
    }
}
fn abs_b_over_fact(k: usize) -> Float {
    unsafe {
        if ABF_CACHE.is_none() {
            let mut v = Vec::with_capacity(K_MAX + 1);
            for kk in 1..=K_MAX {
                let z2k = zeta_even(kk);
                let twopi = mul(&zf(2.0), &pi());
                let inv = exp_(&mul(&zf(-(2.0 * kk as f64)), &ln_(&twopi)));
                v.push(mul(&mul(&zf(2.0), &z2k), &inv));
            }
            ABF_CACHE = Some(v);
        }
        ABF_CACHE.as_ref().unwrap()[k - 1].clone()
    }
}
static mut ABF_CACHE: Option<Vec<Float>> = None;
// signed Stirling numbers of the first kind: (x)_M = sum_j s1(M,j) x^j
fn stirling_first(M: usize) -> Vec<Integer> {
    let mut prev = vec![Integer::from(0); M + 1];
    prev[0] = Integer::from(1);
    for m in 1..=M {
        let mut cur = vec![Integer::from(0); M + 1];
        for k in 1..=m {
            let mut v = Integer::from(0);
            v += &prev[k - 1];
            let t = Integer::from((m - 1) as u64) * &prev[k];
            v -= t;
            cur[k] = v;
        }
        prev = cur;
    }
    prev
}
// falling factorial (l)_j = l!/(l-j)!
fn falling(l: usize, j: usize) -> Float {
    if j > l { return zf(0.0); }
    if j == 0 { return zf(1.0); }
    div(&fact(l), &fact(l - j))
}

// Euler-Maclaurin derivatives of zeta(s), orders 0..=m_max. N = n+1.
static mut S1_CACHE: Option<Vec<Vec<Integer>>> = None;
fn s1_row(M: usize) -> &'static Vec<Integer> {
    unsafe {
        if S1_CACHE.is_none() {
            let mut rows = Vec::with_capacity(K_MAX + 1);
            for mm in 1..=2 * K_MAX - 1 {
                rows.push(stirling_first(mm));
            }
            S1_CACHE = Some(rows);
        }
        &S1_CACHE.as_ref().unwrap()[M - 1]
    }
}
fn zeta_em_ders(s: &C, n: usize, m_max: usize) -> Vec<C> {
    let mut d = vec![(zf(0.0), zf(0.0)); m_max + 1];
    // main sum: sum_{k=1}^{n} (-ln k)^m k^{-s}
    for k in 1..=n {
        let lnx = ln_(&zf(k as f64));
        let mag = exp_(&mul(&neg(&s.0), &lnx));
        let ang = mul(&s.1, &lnx);
        let mut sc: (Float, Float) = (Float::new(PREC), Float::new(PREC));
        sc.assign(ang.sin_cos_ref());
        let tr = mul(&mag, &sc.1);
        let ti = mul(&neg(&mag), &sc.0);
        let mut p = zf(1.0);
        for m in 0..=m_max {
            d[m].0 += mul(&p, &tr);
            d[m].1 += mul(&p, &ti);
            p = mul(&neg(&p), &lnx);
        }
    }
    let lnN = ln_(&zf((n + 1) as f64));
    let lnNn = neg(&lnN);
    let mut lnNn_pow = vec![zf(1.0); m_max + 1];
    for m in 1..=m_max {
        lnNn_pow[m] = mul(&lnNn_pow[m - 1], &lnNn);
    }
    let Nneg = exp_(&mul(&neg(&s.0), &lnN)); // N^{-sigma}
    let ang = mul(&s.1, &lnN);
    let mut sc: (Float, Float) = (Float::new(PREC), Float::new(PREC));
    sc.assign(ang.sin_cos_ref());
    let Ns = (mul(&Nneg, &sc.1), mul(&neg(&Nneg), &sc.0)); // N^{-s}
    let N1s = (mul(&zf((n + 1) as f64), &Ns.0), mul(&zf((n + 1) as f64), &Ns.1)); // N^{1-s}
    let sm1 = (sub(&s.0, &zf(1.0)), s.1.clone());
    let w1 = cinv(&sm1);
    let mut w1p = vec![(zf(1.0), zf(0.0)); m_max + 2];
    for p in 1..=m_max + 1 {
        w1p[p] = cmul(&w1p[p - 1], &w1);
    }
    // tail: N^{1-s}/(s-1) + (1/2) N^{-s}
    for m in 0..=m_max {
        let mut acc = (zf(0.0), zf(0.0));
        for j in 0..=m {
            let cf = mul(&mul(&mul(&binom(m, j), &lnNn_pow[m - j]), &zf(if j % 2 == 0 { 1.0 } else { -1.0 })), &fact(j));
            acc = cadd(&acc, &cscale(&cf, &w1p[j + 1]));
        }
        acc = cmul(&acc, &N1s);
        d[m] = cadd(&d[m], &acc);
        let cf2 = mul(&zf(0.5), &lnNn_pow[m]);
        d[m] = cadd(&d[m], &cscale(&cf2, &Ns));
    }
    // powers of s
    let mut s_pow = vec![(zf(1.0), zf(0.0)); M_MAX_G + 1];
    for p in 1..=M_MAX_G {
        s_pow[p] = cmul(&s_pow[p - 1], s);
    }
    // Bernoulli corrections: sum_k B_{2k}/(2k)! (d/ds)^m [ (s)_{2k-1} N^{-s-2k+1} ]
    for k in 1..=K_MAX {
        let M = 2 * k - 1;
        let s1 = s1_row(M);
        let coef_b = if k % 2 == 1 { abs_b_over_fact(k) } else { neg(&abs_b_over_fact(k)) }; // B_{2k}/(2k)!
        // f^{(j)}(s) = sum_{l=j}^{M} s1(M,l) (l)_j s^{l-j}
        let mut fp = vec![(zf(0.0), zf(0.0)); m_max + 1];
        for j in 0..=m_max {
            let mut acc = (zf(0.0), zf(0.0));
            for l in j..=M {
                let cf = mul(&Float::with_val(PREC, s1[l].clone().abs()), &falling(l, j));
                acc = cadd(&acc, &cscale(&cf, &s_pow[l - j]));
            }
            fp[j] = acc;
        }
        let Nk = exp_(&mul(&zf(-((2 * k - 1) as f64)), &lnN)); // N^{-(2k-1)}
        let Nsk = (mul(&Nk, &Ns.0), mul(&Nk, &Ns.1));
        for m in 0..=m_max {
            let mut acc = (zf(0.0), zf(0.0));
            for j in 0..=m {
                let cf = mul(&binom(m, j), &lnNn_pow[m - j]);
                acc = cadd(&acc, &cscale(&cf, &fp[j]));
            }
            acc = cmul(&acc, &Nsk);
            d[m] = cadd(&d[m], &cscale(&coef_b, &acc));
        }
    }
    d
}

fn zeta_logderivs(s: &C, m_max: usize) -> Vec<C> {
    let d = zeta_em_ders(s, N_EM, m_max);
    let z2 = add(&mul(&d[0].0, &d[0].0), &mul(&d[0].1, &d[0].1));
    let zinv = (div(&d[0].0, &z2), div(&neg(&d[0].1), &z2));
    let mut l = vec![(zf(0.0), zf(0.0)); m_max + 1];
    l[1] = cmul(&d[1], &zinv);
    for n in 2..=m_max {
        let mut acc = d[n].clone();
        for j in 1..n {
            let c = binom(n - 1, j - 1);
            acc = csub(&acc, &cscale(&c, &cmul(&d[n - j], &l[j])));
        }
        l[n] = cmul(&acc, &zinv);
    }
    l
}

// psi^(m)(z) = (-1)^{m+1} m! sum_{l=0}^{SHIFT-1} (z+l)^{-(m+1)} + Stirling(w), w = z+SHIFT
fn polygamma(m: usize, z: &C) -> C {
    let mf = fact(m);
    let mut out = (zf(0.0), zf(0.0));
    for l in 0..SHIFT {
        let x = (add(&z.0, &zf(l as f64)), z.1.clone());
        let inv = cinv(&x);
        let mut p = (zf(1.0), zf(0.0));
        for _ in 0..(m + 1) {
            p = cmul(&p, &inv);
        }
        let sc = mul(&zf(if m % 2 == 0 { -1.0 } else { 1.0 }), &mf);
        out = cadd(&out, &cscale(&sc, &p));
    }
    let w = (add(&z.0, &zf(SHIFT as f64)), z.1.clone());
    let inv = cinv(&w);
    let maxp = m + 2 * KP + 1;
    let mut ip = vec![(zf(1.0), zf(0.0)); maxp + 1];
    for p in 1..=maxp {
        ip[p] = cmul(&ip[p - 1], &inv);
    }
    if m == 0 {
        let lnw = (mul(&zf(0.5), &ln_(&add(&mul(&w.0, &w.0), &mul(&w.1, &w.1)))), w.1.atan2(&w.0));
        out = cadd(&out, &csub(&lnw, &cscale(&zf(0.5), &inv)));
        for k in 1..=KP {
            // -B_2k/(2k) = (-1)^k |B_2k|/(2k)
            let coef = mul(&zf(if k % 2 == 0 { 1.0 } else { -1.0 }), &mul(&abs_b_over_fact(k), &fact(2 * k - 1)));
            out = cadd(&out, &cscale(&coef, &ip[2 * k]));
        }
    } else {
        let sgn = if (m - 1) % 2 == 0 { 1.0 } else { -1.0 }; // (-1)^{m-1}
        out = cadd(&out, &cscale(&mul(&zf(sgn), &fact(m - 1)), &ip[m]));
        out = cadd(&out, &cscale(&mul(&mul(&zf(sgn), &zf(0.5)), &mf), &ip[m + 1]));
        for k in 1..=KP {
            let mut rising = zf(1.0);
            for j in 1..m {
                rising = mul(&rising, &zf((2 * k + j) as f64));
            }
            // (-1)^{m-1} * B_2k * (2k+m-1)!/(2k)! ; B_2k = (-1)^{k+1}|B_2k|
            let mut coef = mul(&mul(&zf(sgn), &abs_b_over_fact(k)), &mul(&fact(2 * k), &rising));
            if k % 2 == 0 {
                coef = neg(&coef);
            }
            out = cadd(&out, &cscale(&coef, &ip[2 * k + m]));
        }
    }
    out
}

// u^(n)(t) = (d/dt)^n log Xi(t), n=1..=m_max (real part; Im should vanish)
fn logxi_derivs(t: &Float, m_max: usize) -> Vec<Float> {
    let s = (zf(0.5), t.clone());
    let l = zeta_logderivs(&s, m_max);
    let lnpi = ln_(&pi());
    let inv_s = cinv(&s);
    let sm1 = (sub(&zf(0.5), &zf(1.0)), t.clone());
    let inv_sm1 = cinv(&sm1);
    let mut sp = vec![(zf(1.0), zf(0.0)); m_max + 2];
    let mut sp1 = vec![(zf(1.0), zf(0.0)); m_max + 2];
    for p in 1..=m_max + 1 {
        sp[p] = cmul(&sp[p - 1], &inv_s);
        sp1[p] = cmul(&sp1[p - 1], &inv_sm1);
    }
    let s2 = (zf(0.25), mul(t, &zf(0.5)));
    let mut psi = vec![(zf(0.0), zf(0.0)); m_max];
    for m in 0..m_max {
        psi[m] = polygamma(m, &s2);
    }
    let one = (zf(1.0), zf(0.0));
    let mut u = vec![zf(0.0); m_max + 1];
    let mut max_im = zf(0.0);
    for n in 1..=m_max {
        let (ar, ai) = if n == 1 {
            let base = csub(&cadd(&sp[1], &sp1[1]), &cscale(&mul(&zf(0.5), &lnpi), &one));
            let base = cadd(&base, &cscale(&zf(0.5), &psi[0]));
            cadd(&base, &l[1])
        } else {
            let cf = mul(&zf(if (n - 1) % 2 == 0 { 1.0 } else { -1.0 }), &fact(n - 1));
            let halfn = div(&zf(1.0), &zf((1u64 << n) as f64));
            let base = cadd(&cscale(&cf, &cadd(&sp[n], &sp1[n])), &cscale(&halfn, &psi[n - 1]));
            cadd(&base, &l[n])
        };
        let (ur, ui) = match n % 4 {
            0 => (ar, ai),
            1 => (neg(&ai), ar),
            2 => (neg(&ar), neg(&ai)),
            _ => (ai, neg(&ar)),
        };
        if abs_(&ui) > max_im {
            max_im = ui;
        }
        u[n] = ur;
    }
    println!("  (probe) max|Im u| = {:.2e}", max_im.to_f64());
    u
}

fn bell(u: &[Float], k: usize) -> Float {
    let mut b = vec![zf(0.0); k + 1];
    b[0] = zf(1.0);
    for j in 1..=k {
        let mut s = zf(0.0);
        for m in 0..j {
            let c = binom(j - 1, m);
            s += mul(&mul(&c, &u[m + 1]), &b[j - 1 - m]);
        }
        b[j] = s;
    }
    b[k].clone()
}

// B_2k/(2k(2k-1)) = (-1)^{k+1} |B_2k|/(2k)! * (2k-2)!
fn b_over_2k_2kminus1(k: usize) -> Float {
    let sgn = if k % 2 == 1 { 1.0 } else { -1.0 };
    mul(&mul(&zf(sgn), &abs_b_over_fact(k)), &fact(2 * k - 2))
}

// ln|Gamma(x+iy)| with CORRECT Stirling exponents z^{1-2k}
fn log_abs_gamma(x: f64, y: f64) -> Float {
    let zm = (x * x + y * y).sqrt();
    let th = y.atan2(x);
    let mut acc = Float::with_val(PREC, (x - 0.5) * zm.ln() - y * th - x + 0.5 * (2.0 * std::f64::consts::PI).ln());
    let mut p = zf(1.0 / zm); // |z|^{-1}
    for k in 1..=K_MAX {
        let coef = b_over_2k_2kminus1(k);
        let angle = (1.0 - 2.0 * k as f64) * th;
        acc += mul(&coef, &mul(&p, &zf(angle.cos())));
        p = mul(&p, &zf(1.0 / (zm * zm)));
    }
    acc
}

// ln|xi(1/2+it)|  (real; xi real on critical line)
fn ln_abs_xi(t: &Float) -> Float {
    let s = (zf(0.5), t.clone());
    let z0 = zeta_em_ders(&s, N_EM, 0);
    let lnz = mul(&zf(0.5), &ln_(&add(&mul(&z0[0].0, &z0[0].0), &mul(&z0[0].1, &z0[0].1))));
    let tt = mul(t, t);
    let pre = ln_(&mul(&zf(0.5), &add(&zf(0.25), &tt)));
    let lnpi = ln_(&pi());
    let g = log_abs_gamma(0.25, (t.to_f64()) * 0.5);
    add(&add(&sub(&pre, &mul(&zf(0.25), &lnpi)), &g), &lnz)
}

fn main() {
    println!("=== referee_probe: independent cross-check, {} bits ===", PREC);

    // -1. known values
    let z2 = zeta_em_ders(&(zf(2.0), zf(0.0)), 600, 0);
    let zhalf = zeta_em_ders(&(zf(0.5), zf(0.0)), 600, 0);
    let g1 = 14.134725141734693790457251983562470270784f64;
    let zg = zeta_em_ders(&(zf(0.5), zf(g1)), 600, 0);
    println!("zeta(2)={:.17e} (true 1.64493406684822644)  |d|={:.1e}", z2[0].0.to_f64(), (z2[0].0.to_f64()-1.6449340668482264).abs());
    println!("zeta(1/2)={:.17e} (true -1.46035450880958681) |d|={:.1e}", zhalf[0].0.to_f64(), (zhalf[0].0.to_f64()+1.4603545088095868).abs());
    println!("zeta(1/2+i*g1) |z|={:.3e}  (should be ~0)", cmag(&zg[0]).to_f64());
    // real-axis polygamma
    let p0 = polygamma(0, &(zf(0.5), zf(0.0)));
    let p1 = polygamma(0, &(zf(1.0), zf(0.0)));
    let p2 = polygamma(1, &(zf(0.5), zf(0.0)));
    println!("psi(1/2)={:.17e} (true -1.96351002602142348) |d|={:.1e}", p0.0.to_f64(), (p0.0.to_f64()+1.9635100260214235).abs());
    println!("psi(1)={:.17e} (true -0.57721566490153286) |d|={:.1e}", p1.0.to_f64(), (p1.0.to_f64()+0.5772156649015329).abs());
    println!("psi'(1/2)={:.17e} (true 4.93480220054467931) |d|={:.1e}", p2.0.to_f64(), (p2.0.to_f64()-4.934802200544679).abs());

    // 0. zeta sanity vs f64 em.rs
    let e = em::zeta_em(0.5, 40.0, 600);
    let mine = zeta_em_ders(&(zf(0.5), zf(40.0)), 600, 0);
    println!("zeta(1/2+40i): probe={:+.15e}{:+.15e}i  em.rs={:+.15e}{:+.15e}i  |d|={:.2e}",
        mine[0].0.to_f64(), mine[0].1.to_f64(), e.re, e.im,
        (((mine[0].0.to_f64() - e.re).powi(2) + (mine[0].1.to_f64() - e.im).powi(2)).sqrt()));

    // 1. q_k via own composition; L_k = |xi|^2 q_k with CORRECT Gamma
    println!("\n-- q_k (probe) vs binary bracket q; L_k = |xi|^2 q --");
    let pts: [(f64, usize); 7] = [(40.0, 3), (33.6, 8), (56.5, 3), (35.5, 4), (40.0, 18), (40.0, 19), (40.0, 20)];
    for &(t, k) in &pts {
        let u = logxi_derivs(&zf(t), k + 1);
        let b_k = bell(&u, k);
        let b_km = bell(&u, k - 1);
        let b_kp = bell(&u, k + 1);
        let q = sub(&mul(&b_k, &b_k), &mul(&b_km, &b_kp));
        // |xi|^2
        let lxi = ln_abs_xi(&zf(t));
        let xi2 = exp_(&mul(&zf(2.0), &lxi));
        let lk = mul(&xi2, &q);
        println!("t={:5.1} k={:2}: q={:+.10e}  xi2={:.6e}  L_k={:+.10e}", t, k, q.to_f64(), xi2.to_f64(), lk.to_f64());
        if k >= 18 {
            let u2 = &u;
            for n in (k - 2)..=(k + 1) {
                print!("u^{}={:+.4e} ", n, u2.get(n).unwrap().to_f64());
            }
            println!();
        }
    }

    // 1b. per-order u^n and Im at t=40 (m_max=21)
    {
        let u = logxi_derivs(&zf(40.0), 21);
        let mut maxim = 0.0f64;
        for n in 1..=21 {
            let s = (zf(0.5), zf(40.0));
            let l = zeta_logderivs(&s, 21);
            // recompute Im for display: A_n via psi
            let _ = l;
            let _ = &u;
            if n >= 1 && n <= 8 {
                println!("u^{}={:+.8e}", n, u[n].to_f64());
            }
        }
        let _ = maxim;
    }

    // 2. central-difference q_3(40) from ln|xi| (fully different route)
    println!("\n-- central-difference q_3(40): ln|xi| finite diffs, h & h/2 Richardson --");
    let t0 = 40.0f64;
    let h = 0.01f64;
    let f = |dt: f64| ln_abs_xi(&zf(t0 + dt));
    let f0 = f(0.0);
    let f1 = f(h); let fm1 = f(-h);
    let f2 = f(2.0 * h); let fm2 = f(-2.0 * h);
    let f3 = f(3.0 * h); let fm3 = f(-3.0 * h);
    // h step
    let d1_h = div(&sub(&f1, &fm1), &zf(2.0 * h));
    let d2_h = div(&sub(&add(&f1, &fm1), &mul(&zf(2.0), &f0)), &zf(h * h));
    let d3_h = div(&sub(&add(&sub(&f2, &mul(&zf(2.0), &f1)), &mul(&zf(2.0), &fm1)), &fm2), &zf(2.0 * h * h * h));
    let d4_h = div(&add(&sub(&add(&sub(&f2, &mul(&zf(4.0), &f1)), &mul(&zf(6.0), &f0)), &mul(&zf(4.0), &fm1)), &fm2), &zf(h * h * h * h));
    // h/2 step
    let h2 = h / 2.0;
    let g1 = f(h2); let gm1 = f(-h2);
    let g2 = f(2.0 * h2); let gm2 = f(-2.0 * h2);
    let d1_h2 = div(&sub(&g1, &gm1), &zf(2.0 * h2));
    let d2_h2 = div(&sub(&add(&g1, &gm1), &mul(&zf(2.0), &f0)), &zf(h2 * h2));
    let d3_h2 = div(&sub(&add(&sub(&g2, &mul(&zf(2.0), &g1)), &mul(&zf(2.0), &gm1)), &gm2), &zf(2.0 * h2 * h2 * h2));
    let d4_h2 = div(&add(&sub(&add(&sub(&g2, &mul(&zf(4.0), &g1)), &mul(&zf(6.0), &f0)), &mul(&zf(4.0), &gm1)), &gm2), &zf(h2 * h2 * h2 * h2));
    // Richardson
    let d1 = div(&sub(&mul(&zf(4.0), &d1_h2), &d1_h), &zf(3.0));
    let d2 = div(&sub(&mul(&zf(4.0), &d2_h2), &d2_h), &zf(3.0));
    let d3 = div(&sub(&mul(&zf(4.0), &d3_h2), &d3_h), &zf(3.0));
    let d4 = div(&sub(&mul(&zf(4.0), &d4_h2), &d4_h), &zf(3.0));
    // Bell in raw derivatives
    let b1 = d1.clone();
    let b2 = add(&d2, &mul(&d1, &d1));
    let b3 = add(&add(&d3, &mul(&zf(3.0), &mul(&d1, &d2))), &mul(&mul(&d1, &d1), &d1));
    let b4 = add(&add(&add(&d4, &mul(&zf(4.0), &mul(&d1, &d3))), &mul(&zf(3.0), &mul(&d2, &d2))), &add(&mul(&zf(6.0), &mul(&mul(&d1, &d1), &d2)), &mul(&mul(&mul(&d1, &d1), &d1), &d1)));
    let q3_cd = sub(&mul(&b3, &b3), &mul(&b2, &b4));
    println!("u'={:.8e} u''={:.8e} u'''={:.8e} u''''={:.8e}", d1.to_f64(), d2.to_f64(), d3.to_f64(), d4.to_f64());
    println!("q_3(40) via central differences (ln|xi|, h/h2 Richardson) = {:+.10e}   [binary 3.695929, probe-composition 3.69592851]", q3_cd.to_f64());
    let _ = (f3, fm3, f1.clone(), fm1.clone(), f2.clone(), fm2.clone());

    // 3. |xi|^2 via probe (correct Gamma) vs binary implied xi2 = L/q
    println!("\n-- xi2 probe vs binary-implied (L/q) --");
    for &(t, k) in &[(40.0f64, 3usize), (33.6, 8), (56.5, 3), (35.5, 4)] {
        let lxi = ln_abs_xi(&zf(t));
        let xi2 = exp_(&mul(&zf(2.0), &lxi));
        println!("t={:5.1}: xi2(probe)={:.10e}", t, xi2.to_f64());
    }
    println!("=== probe done ===");
}
