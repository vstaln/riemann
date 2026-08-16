// S4 region-size probe: Jensen-polynomial hyperbolicity grid + regime transition.
// gamma(k) via the Phi-moment integral (MPFR), J_{d,n} roots via Aberth-Ehrlich.
// Convention (GORTTW, attack-jensen-ometer.md): gamma(j) = xi^{(2j)}(1/2) * j!/(2j)!,
//   J_{d,n}(X) = sum_{j=0}^d C(d,j) gamma(n+j) X^j.
// gamma(k) = k! * M_k / (2k)!,  M_k = 2 int_0^inf Phi(u) u^{2k} du,
//   Phi(u) = 2 sum_{n>=1} (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}.
use rug::float::Constant;
use rug::ops::Pow;
use rug::Float;
use std::cmp::Ordering;
use std::fs::File;
use std::io::Write;
use std::time::Instant;

const PG: u32 = 180; // gamma working precision (~54 digits)
const PR: u32 = 128; // root-finding precision (~38 digits)
const NSUM: usize = 8; // n-truncation in Phi
const UMAX: f64 = 4.0; // u-integral cutoff (tail < 1e-3800)
const NPAN: usize = 40; // panels on [0, UMAX]
const NGL: usize = 48; // Gauss-Legendre order
const KMAX: usize = 220; // gamma up to 220 (n<=200, d<=20)
const DMAX: usize = 20;
const NMAX: usize = 200;

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

fn main() {
    let t0 = Instant::now();
    let mut out = File::create("tools/s4-region-size/results.txt").expect("results file");

    // ---- 1. gamma(k) via moments ----
    println!("[1] computing Gauss-Legendre nodes (N={}), prec={} bits", NGL, PG);
    let gl = gl_nodes(PG);
    let mut gamma: Vec<Float> = Vec::with_capacity(KMAX + 1);
    for k in 0..=KMAX {
        let mk = moment(k, &gl, PG);
        gamma.push(gamma_k(k, &mk, PG));
    }
    // verification vs known 60-digit table (attack-jensen-ometer.md)
    let known: [(&str, &str); 9] = [
        ("gamma0", "0.4971207781883141099127737396853977198073"),
        ("gamma1", "0.0114859721575727187676249382488160851323"),
        ("gamma2", "0.000246904036140636013780691582989702276272"),
        ("gamma3", "0.000004994132888313162432028552355067724221758"),
        ("gamma4", "0.00000009581343723225929219340648631276497622301"),
        ("gamma5", "0.000000001753923091213315303489457133184146682862"),
        ("gamma6", "0.00000000003077668832786528369526151242159777679754"),
        ("gamma7", "0.0000000000005196051571847475304071348853364035054351"),
        ("gamma8", "0.000000000000008466271866458899923670642823387187309359"),
    ];
    println!("[1] gamma(k) verification (ours vs known 60-digit table):");
    let mut verif_ok = true;
    for (i, (name, s)) in known.iter().enumerate() {
        let parsed = Float::parse(s).unwrap();
        let kf = Float::with_val(PG, parsed);
        let diff = Float::with_val(PG, &gamma[i] - &kf);
        let rel = Float::with_val(PG, diff.abs() / &kf);
        let ok = rel < zf(PG, 1e-30);
        verif_ok &= ok;
        println!(
            "  {} = {:.30e}  rel-diff {:.1e}  {}",
            name,
            gamma[i],
            rel.to_f64(),
            if ok { "OK" } else { "MISMATCH" }
        );
    }
    println!(
        "  gamma verification: {}  (elapsed {:.1}s)",
        if verif_ok { "ALL OK at 1e-30" } else { "FAILED" },
        t0.elapsed().as_secs_f64()
    );
    writeln!(out, "gamma verification: {}", if verif_ok { "ALL OK at 1e-30" } else { "FAILED" }).unwrap();
    for k in 0..=KMAX {
        writeln!(out, "gamma[{}] = {:.30e}", k, gamma[k]).unwrap();
    }

    // ---- 2. hyperbolicity grid ----
    println!("\n[2] hyperbolicity grid d=1..{}, n=0..{} (Aberth-Ehrlich, {} bits)", DMAX, NMAX, PR);
    let mut hyp_table: Vec<Vec<bool>> = vec![vec![true; NMAX + 1]; DMAX + 1];
    let mut roots_table: Vec<Vec<Vec<Float>>> = vec![vec![vec![]; NMAX + 1]; DMAX + 1];
    let mut nonhyp: Vec<(usize, usize)> = vec![];
    let mut sturm_checked: usize = 0;
    let t1 = Instant::now();
    for d in 1..=DMAX {
        let td = Instant::now();
        let mut prev_roots: Option<Vec<Cx>> = None;
        for n in 0..=NMAX {
            let c = build_coefs(d, n, &gamma);
            let mut z: Vec<Cx> = match &prev_roots {
                Some(pr) if pr.len() == d => pr.clone(),
                _ => {
                    // ratio init (good for the spread regime at small n)
                    let mut zz = Vec::with_capacity(d);
                    for j in 1..=d {
                        let ratio = Float::with_val(PR, &c[j - 1].r / &c[j].r);
                        zz.push(Cx { r: -ratio, i: zf(PR, 0.0) });
                    }
                    zz
                }
            };
            let (conv, _worst) = aberth(&c, &mut z, 100);
            if std::env::var("S4DBG").is_ok() && d >= 14 && d <= 20 && n <= 20 {
                eprintln!("   POLY (d,n)=({},{}) init0={:.6}", d, n, z[0].r.to_f64());
            }
            let mut hyperbolic = true;
            for zi in z.iter() {
                let scale = Float::with_val(PR, zf(PR, 1.0) + zi.r.clone().abs());
                let thr = Float::with_val(PR, zf(PR, 1e-25) * &scale);
                if zi.i.clone().abs() > thr {
                    hyperbolic = false;
                }
            }
            if !conv || !hyperbolic {
                // independent check: Sturm count
                let cfl: Vec<Float> = c.iter().map(|x| x.r.clone()).collect();
                let sc = sturm_count_neg(&cfl);
                let sturm_hyp = sc == d;
                sturm_checked += 1;
                println!(
                    "  FLAG (d,n)=({},{}): aberth_hyp={} conv={} sturm_count={} sturm_hyp={}",
                    d, n, hyperbolic, conv, sc, sturm_hyp
                );
                writeln!(
                    out,
                    "FLAG (d,n)=({},{}): aberth_hyp={} conv={} sturm_count={} sturm_hyp={}",
                    d, n, hyperbolic, conv, sc, sturm_hyp
                )
                .unwrap();
                if !hyperbolic && !sturm_hyp {
                    nonhyp.push((d, n));
                } else if !hyperbolic && sturm_hyp {
                    hyperbolic = true; // Aberth false alarm; trust Sturm
                }
            }
            hyp_table[d][n] = hyperbolic;
            if hyperbolic {
                let mut rs: Vec<Float> = z.iter().map(|zi| zi.r.clone()).collect();
                rs.sort_by(|a, b| {
                    a.clone()
                        .abs()
                        .partial_cmp(&b.clone().abs())
                        .unwrap_or(Ordering::Equal)
                });
                roots_table[d][n] = rs;
                prev_roots = Some(z);
            } else {
                prev_roots = None;
            }
        }
        println!("  d={:2}: done in {:.2}s", d, td.elapsed().as_secs_f64());
    }
    println!(
        "[2] grid done in {:.1}s; non-hyperbolic hits: {}; sturm checks: {}",
        t1.elapsed().as_secs_f64(),
        nonhyp.len(),
        sturm_checked
    );
    for (d, n) in nonhyp.iter() {
        println!("*** NON-HYPERBOLIC J_{{ {},{} }} ***", d, n);
    }

    // ---- 3. literal onset (hyperbolic for all n' >= n) ----
    let mut onset_lit: Vec<usize> = vec![0; DMAX + 1];
    for d in 1..=DMAX {
        let mut last_bad: Option<usize> = None;
        for n in 0..=NMAX {
            if !hyp_table[d][n] {
                last_bad = Some(n);
            }
        }
        onset_lit[d] = match last_bad {
            Some(x) => x + 1,
            None => 0,
        };
    }

    // ---- 4. regime transition (shape drift) ----
    let mut drift: Vec<Vec<f64>> = vec![vec![0.0; NMAX]; DMAX + 1];
    for d in 1..=DMAX {
        for n in 0..NMAX {
            let a = &roots_table[d][n];
            let b = &roots_table[d][n + 1];
            if a.len() != d || b.len() != d {
                continue;
            }
            let mut md = 0.0f64;
            for j in 0..d {
                let s_a = a[j].to_f64() / a[0].to_f64();
                let s_b = b[j].to_f64() / b[0].to_f64();
                let dd = (s_b - s_a).abs();
                if dd > md {
                    md = dd;
                }
            }
            drift[d][n] = md;
        }
    }
    let onset_tail = |d: usize, eps: f64| -> usize {
        for n0 in 0..=NMAX {
            let mut all = true;
            for m in n0..NMAX {
                if drift[d][m] >= eps {
                    all = false;
                    break;
                }
            }
            if all {
                return n0;
            }
        }
        NMAX
    };

    println!("\n[3/4] onset table: n0*lit = literal (non-hyperbolic tail), n0(eps) = shape-drift < eps for all n beyond");
    println!("{:>3} {:>6} {:>8} {:>8}", "d", "n0*lit", "n0(1e-2)", "n0(1e-3)");
    let mut region1e2: Vec<usize> = vec![0; DMAX + 1];
    let mut region1e3: Vec<usize> = vec![0; DMAX + 1];
    for d in 1..=DMAX {
        let o1 = onset_tail(d, 1e-2);
        let o2 = onset_tail(d, 1e-3);
        region1e2[d] = o1;
        region1e3[d] = o2;
        println!("{:>3} {:>6} {:>8} {:>8}", d, onset_lit[d], o1, o2);
    }
    writeln!(out, "\nonset literal n0*(d): {:?}", onset_lit).unwrap();
    writeln!(out, "onset drift-1e-2: {:?}", region1e2).unwrap();
    writeln!(out, "onset drift-1e-3: {:?}", region1e3).unwrap();

    // region size as function of d
    println!("\nregion size R(d) = cumulative sum of n0(dprime):");
    for (eps, reg) in [(1e-2, &region1e2), (1e-3, &region1e3)] {
        let mut cum = vec![0usize; DMAX + 1];
        let mut acc = 0usize;
        for d in 1..=DMAX {
            acc += reg[d];
            cum[d] = acc;
        }
        println!("  eps={:.0e}: {:?}", eps, &cum[1..]);
        writeln!(out, "region size eps={:.0e}: cumulative {:?}", eps, &cum[1..]).unwrap();
    }

    // ---- 5. fit n0 vs d (power law) ----
    println!("\n[5] power-law fit log n0 = a + p log d, on d where n0>0:");
    for (eps, reg) in [(1e-2, &region1e2), (1e-3, &region1e3)] {
        let xs: Vec<f64> = (1..=DMAX)
            .filter(|&d| reg[d] > 0)
            .map(|d| d as f64)
            .collect();
        let ys: Vec<f64> = xs.iter().map(|&d| reg[d as usize] as f64).collect();
        if xs.len() >= 3 {
            let lx: Vec<f64> = xs.iter().map(|x| x.ln()).collect();
            let ly: Vec<f64> = ys.iter().map(|y| y.ln()).collect();
            let n = lx.len() as f64;
            let mx = lx.iter().sum::<f64>() / n;
            let my = ly.iter().sum::<f64>() / n;
            let mut sxx = 0.0;
            let mut sxy = 0.0;
            for i in 0..lx.len() {
                sxx += (lx[i] - mx) * (lx[i] - mx);
                sxy += (lx[i] - mx) * (ly[i] - my);
            }
            let p = sxy / sxx;
            let a = my - p * mx;
            let mut sse = 0.0;
            let mut sst = 0.0;
            for i in 0..lx.len() {
                let pred = a + p * lx[i];
                sse += (ly[i] - pred) * (ly[i] - pred);
                sst += (ly[i] - my) * (ly[i] - my);
            }
            let r2 = 1.0 - sse / sst;
            println!(
                "  eps={:.0e}: n0 ~ {:.3} * d**{:.3}, R2={:.4} ({} points, d {}..{})",
                eps,
                a.exp(),
                p,
                r2,
                xs.len(),
                xs[0] as usize,
                xs[xs.len() - 1] as usize
            );
            writeln!(out, "fit eps={:.0e}: n0 ~ {:.3} d**{:.3}, R2={:.4}", eps, a.exp(), p, r2).unwrap();
        } else {
            println!("  eps={:.0e}: too few positive onsets for a fit", eps);
        }
    }

    // ---- 6. min relative gap as function of n (margin structure) ----
    println!("\n[6] min relative root gap min_j(rho(j+1)/rho(j) - 1) by n (step 10), for d=9,14,20:");
    for &d in &[9usize, 14, 20] {
        let mut row = String::new();
        for n in (0..=NMAX).step_by(10) {
            let rs = &roots_table[d][n];
            if rs.len() != d {
                row.push_str(" NA");
                continue;
            }
            let mut mg = f64::INFINITY;
            for j in 0..d - 1 {
                let gap = rs[j + 1].to_f64() / rs[j].to_f64() - 1.0;
                if gap < mg {
                    mg = gap;
                }
            }
            row.push_str(&format!(" {:.2e}", mg));
        }
        println!("  d={:2}:{}", d, row);
    }
    {
        let mut row = String::new();
        for n in (0..=NMAX).step_by(10) {
            let rs = &roots_table[20][n];
            if rs.is_empty() {
                row.push_str(" NA");
            } else {
                row.push_str(&format!(" {:.3e}", rs[0].to_f64().abs()));
            }
        }
        println!("  d=20 |rho_1(n)|:{}", row);
    }

    println!("\n=== done in {:.1}s total ===", t0.elapsed().as_secs_f64());
    println!("results written to tools/s4-region-size/results.txt");
}
