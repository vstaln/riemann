fn zf(prec: u32, v: f64) -> Float {
    Float::with_val(prec, v)
}

// ---------- Gauss-Legendre ----------
fn legendre(prec: u32, n: usize, x: &Float) -> (Float, Float) {
    let mut p0 = zf(prec, 1.0); // P_0
    if n == 0 {
        return (p0, zf(prec, 0.0));
    }
    let mut p1 = x.clone(); // P_1
    for k in 1..n {
        let kf = zf(prec, k as f64);
        let kp1 = zf(prec, (k + 1) as f64);
        let c = zf(prec, (2 * k + 1) as f64);
        // P_{k+1} = ((2k+1) x P_k - k P_{k-1}) / (k+1)
        let t1 = Float::with_val(prec, &c * x);
        let t2 = Float::with_val(prec, &t1 * &p1);
        let u1 = Float::with_val(prec, &kf * &p0);
        let v1 = Float::with_val(prec, t2 - u1);
        let p2 = Float::with_val(prec, v1 / &kp1);
        p0 = p1;
        p1 = p2;
    }
    let x2 = Float::with_val(prec, x * x);
    let t = Float::with_val(prec, x * &p1 - &p0);
    let num = Float::with_val(prec, zf(prec, n as f64) * t);
    let den = Float::with_val(prec, x2 - zf(prec, 1.0));
    (p1, Float::with_val(prec, num / den))
}

fn gl_nodes(prec: u32) -> Vec<(Float, Float)> {
    let mut out = Vec::with_capacity(NGL);
    for j in 0..NGL {
        let init = (std::f64::consts::PI * (j as f64 + 0.75) / (NGL as f64 + 0.5)).cos();
        let mut x = zf(prec, init);
        for _ in 0..80 {
            let (p, dp) = legendre(prec, NGL, &x);
            let dx = Float::with_val(prec, &p / &dp);
            x -= &dx;
            if dx.clone().abs() < zf(prec, 1e-75) {
                break;
            }
        }
        let (_, dp) = legendre(prec, NGL, &x);
        let x2 = Float::with_val(prec, &x * &x);
        let one_m = Float::with_val(prec, zf(prec, 1.0) - x2);
        let dp2 = Float::with_val(prec, &dp * &dp);
        let den = Float::with_val(prec, one_m * dp2);
        let w = Float::with_val(prec, zf(prec, 2.0) / den);
        out.push((x, w));
    }
    out
}

// ---------- Phi and moments ----------
fn phi(u: &Float, prec: u32) -> Float {
    let pi = Float::with_val(prec, Constant::Pi);
    let e2u = Float::with_val(prec, zf(prec, 2.0) * u).exp();
    let e9 = Float::with_val(prec, zf(prec, 4.5) * u).exp();
    let e5 = Float::with_val(prec, zf(prec, 2.5) * u).exp();
    let mut s = zf(prec, 0.0);
    for n in 1..=NSUM {
        let n2 = zf(prec, (n * n) as f64);
        let n4 = Float::with_val(prec, &n2 * &n2);
        let neg_pi = Float::with_val(prec, -&pi);
        let a1 = Float::with_val(prec, &neg_pi * &n2);
        let arg = Float::with_val(prec, &a1 * &e2u);
        let e = arg.exp();
        let c2 = zf(prec, 2.0);
        let c2pi = Float::with_val(prec, &c2 * &pi);
        let t0 = Float::with_val(prec, &c2pi * &pi);
        let t1 = Float::with_val(prec, &t0 * &n4);
        let t1 = Float::with_val(prec, &t1 * &e9);
        let c3 = zf(prec, 3.0);
        let t2 = Float::with_val(prec, &c3 * &pi);
        let t2 = Float::with_val(prec, &t2 * &n2);
        let t2 = Float::with_val(prec, &t2 * &e5);
        let diff = Float::with_val(prec, t1 - t2);
        s += Float::with_val(prec, diff * e);
    }
    Float::with_val(prec, s * zf(prec, 2.0))
}

fn moment(k: usize, gl: &[(Float, Float)], prec: u32) -> Float {
    let h = UMAX / NPAN as f64;
    let mut s = zf(prec, 0.0);
    for p in 0..NPAN {
        // exact panel boundaries p/10 (no f64 contamination): 4.0*p exact in f64 for p<=40
        let a = Float::with_val(prec, 4.0 * p as f64) / Float::with_val(prec, 40.0);
        let b = Float::with_val(prec, 4.0 * (p + 1) as f64) / Float::with_val(prec, 40.0);
        let ab = Float::with_val(prec, &a + &b);
        let mid = Float::with_val(prec, ab / 2.0);
        let ba = Float::with_val(prec, &b - &a);
        let half = Float::with_val(prec, ba / 2.0);
        for (x, w) in gl {
            let hx = Float::with_val(prec, &half * x);
            let u = Float::with_val(prec, &mid + hx);
            let f = phi(&u, prec);
            let uk = Float::with_val(prec, u.pow(2 * k as u32));
            let wf = Float::with_val(prec, w * f);
            s += Float::with_val(prec, wf * uk);
        }
    }
    Float::with_val(prec, Float::with_val(prec, s * zf(prec, 4.0)) / zf(prec, 40.0)) // M_k = (4/40)*s = h*s, exact
}

fn gamma_k(k: usize, mk: &Float, prec: u32) -> Float {
    // gamma(k) = k! M_k / (2k)! = M_k / prod_{j=k+1}^{2k} j
    let mut d = zf(prec, 1.0);
    for j in (k + 1)..=(2 * k) {
        d *= zf(prec, j as f64);
    }
    Float::with_val(prec, mk / d)
}

// ---------- complex MPFR ----------
#[derive(Clone)]
struct Cx {
    r: Float,
    i: Float,
}

fn cadd(a: &Cx, b: &Cx) -> Cx {
    Cx {
        r: Float::with_val(PR, &a.r + &b.r),
        i: Float::with_val(PR, &a.i + &b.i),
    }
}
fn csub(a: &Cx, b: &Cx) -> Cx {
    Cx {
        r: Float::with_val(PR, &a.r - &b.r),
        i: Float::with_val(PR, &a.i - &b.i),
    }
}
fn cmul(a: &Cx, b: &Cx) -> Cx {
    let ar_br = Float::with_val(PR, &a.r * &b.r);
    let ai_bi = Float::with_val(PR, &a.i * &b.i);
    let ar_bi = Float::with_val(PR, &a.r * &b.i);
    let ai_br = Float::with_val(PR, &a.i * &b.r);
    Cx {
        r: Float::with_val(PR, ar_br - ai_bi),
        i: Float::with_val(PR, ar_bi + ai_br),
    }
}
fn cdiv(a: &Cx, b: &Cx) -> Cx {
    let br2 = Float::with_val(PR, &b.r * &b.r);
    let bi2 = Float::with_val(PR, &b.i * &b.i);
    let den = Float::with_val(PR, br2 + bi2);
    let ar_br = Float::with_val(PR, &a.r * &b.r);
    let ai_bi = Float::with_val(PR, &a.i * &b.i);
    let ai_br = Float::with_val(PR, &a.i * &b.r);
    let ar_bi = Float::with_val(PR, &a.r * &b.i);
    Cx {
        r: Float::with_val(PR, Float::with_val(PR, ar_br + ai_bi) / &den),
        i: Float::with_val(PR, Float::with_val(PR, ai_br - ar_bi) / &den),
    }
}
fn czabs(a: &Cx) -> Float {
    let r2 = Float::with_val(PR, &a.r * &a.r);
    let i2 = Float::with_val(PR, &a.i * &a.i);
    Float::with_val(PR, r2 + i2).sqrt()
}

fn horner(c: &[Cx], z: &Cx) -> (Cx, Cx) {
    let d = c.len() - 1;
    let mut p = c[d].clone();
    let mut pp = Cx { r: zf(PR, 0.0), i: zf(PR, 0.0) };
    for j in (0..d).rev() {
        pp = cadd(&cmul(&pp, z), &p);
        p = cadd(&cmul(&p, z), &c[j]);
    }
    (p, pp)
}

fn binom_f(m: usize, j: usize) -> f64 {
    let mut r = 1.0f64;
    for k in 0..j {
        r *= (m - k) as f64 / (j - k) as f64;
    }
    r
}

fn build_coefs(d: usize, n: usize, g: &[Float]) -> Vec<Cx> {
    let mut c = Vec::with_capacity(d + 1);
    for j in 0..=d {
        let b = Float::with_val(PR, binom_f(d, j));
        let gj = Float::with_val(PR, &g[n + j]);
        c.push(Cx {
            r: Float::with_val(PR, gj * b),
            i: zf(PR, 0.0),
        });
    }
    c
}

// ---------- Aberth-Ehrlich ----------
fn aberth(c: &[Cx], z: &mut [Cx], maxit: usize) -> (bool, Float) {
    let d = z.len();
    let tol = zf(PR, 1e-27);
    let one = Cx { r: zf(PR, 1.0), i: zf(PR, 0.0) };
    for _it in 0..maxit {
        let mut max_rel = zf(PR, 0.0);
        let mut pv = Vec::with_capacity(d);
        let mut pdp = Vec::with_capacity(d);
        for zi in z.iter() {
            let (p, dp) = horner(c, zi);
            pv.push(p);
            pdp.push(dp);
        }
        let mut sums: Vec<Cx> = (0..d)
            .map(|_| Cx { r: zf(PR, 0.0), i: zf(PR, 0.0) })
            .collect();
        for i in 0..d {
            for j in 0..d {
                if i == j {
                    continue;
                }
                let dj = csub(&z[i], &z[j]);
                sums[i] = cadd(&sums[i], &cdiv(&one, &dj));
            }
        }
        for i in 0..d {
            let num = cdiv(&pv[i], &pdp[i]);
            let den = csub(&one.clone(), &cmul(&num, &sums[i]));
            let dz = cdiv(&num, &den);
            let m = czabs(&dz);
            let zi_abs = czabs(&z[i]);
            let scale = Float::with_val(PR, zf(PR, 1.0) + zi_abs);
            let rel = Float::with_val(PR, &m / &scale);
            if rel > max_rel {
                max_rel = rel;
            }
            if m > Float::with_val(PR, zf(PR, 1e6) * &scale) {
                continue; // clamp blowup
            }
            z[i] = csub(&z[i], &dz);
        }
        if std::env::var("S4DBG").is_ok() && _it < 40 {
            eprintln!("   it {}: max_rel {:.2e}", _it, max_rel.to_f64());
        }
        if max_rel < tol {
            break;
        }
    }
    // residual check (relative to Horner bound)
    let mut worst = zf(PR, 0.0);
    for zi in z.iter() {
        let (p, _) = horner(c, zi);
        let pm = czabs(&p);
        let mut bnd = zf(PR, 0.0);
        let mut xp = zf(PR, 1.0);
        for cj in c.iter() {
            bnd += Float::with_val(PR, czabs(cj) * &xp);
            xp *= czabs(zi);
        }
        let rel = Float::with_val(PR, &pm / &bnd);
        if rel > worst {
            worst = rel;
        }
    }
    (worst < zf(PR, 1e-20), worst)
}

// ---------- Sturm count (backup check) ----------
fn poly_divrem(a: &[Float], b: &[Float]) -> (Vec<Float>, Vec<Float>) {
    let da = a.len() - 1;
    let db = b.len() - 1;
    if da < db {
        // defensive: dividend of lower degree -> remainder is a itself
        return (vec![], a.to_vec());
    }
    let mut r = a.to_vec();
    let mut q = vec![zf(PR, 0.0); da - db + 1];
    for k in (0..=da - db).rev() {
        let coeff = Float::with_val(PR, &r[db + k] / &b[db]);
        q[k] = coeff.clone();
        if coeff.cmp0() != Some(Ordering::Equal) {
            for j in 0..=db {
                let prod = Float::with_val(PR, &coeff * &b[j]);
                r[j + k] -= prod;
            }
        }
    }
    while r.len() > 1 && r[r.len() - 1].cmp0() == Some(Ordering::Equal) {
        r.pop();
    }
    (q, r)
}

fn sturm_count_neg(coef: &[Float]) -> usize {
    // # distinct real roots of P in (-inf, 0], P = sum coef[j] x^j (ascending)
    let d = coef.len() - 1;
    if d == 0 {
        return 0;
    }
    let mut p1: Vec<Float> = Vec::with_capacity(d);
    for j in 1..=d {
        p1.push(Float::with_val(PR, zf(PR, j as f64) * &coef[j]));
    }
    let mut seq: Vec<Vec<Float>> = vec![coef.to_vec(), p1];
    loop {
        let n = seq.len();
        let (_, rem) = poly_divrem(&seq[n - 2], &seq[n - 1]);
        if rem.len() == 1 && rem[0].cmp0() == Some(Ordering::Equal) {
            break;
        }
        let neg: Vec<Float> = rem.iter().map(|v| -v.clone()).collect();
        seq.push(neg);
        if seq.len() > 2 * d + 2 {
            break;
        }
    }
    let sc_at0 = {
        let mut prev_sign = 0i32;
        let mut changes = 0usize;
        for p in seq.iter() {
            let s = match p[0].clone().cmp0().unwrap() {
                Ordering::Greater => 1i32,
                Ordering::Less => -1i32,
                Ordering::Equal => 0i32,
            };
            if s != 0 && prev_sign != 0 && s != prev_sign {
                changes += 1;
            }
            if s != 0 {
                prev_sign = s;
            }
        }
        changes
    };
    let sc_at_minf = {
        let mut prev_sign = 0i32;
        let mut changes = 0usize;
        for p in seq.iter() {
            let deg = p.len() - 1;
            let s0 = match p[deg].clone().cmp0().unwrap() {
                Ordering::Greater => 1i32,
                Ordering::Less => -1i32,
                Ordering::Equal => 0i32,
            };
            let s = if deg % 2 == 1 { -s0 } else { s0 };
            if s != 0 && prev_sign != 0 && s != prev_sign {
                changes += 1;
            }
            if s != 0 {
                prev_sign = s;
            }
        }
        changes
    };
    sc_at_minf.saturating_sub(sc_at0)
}

