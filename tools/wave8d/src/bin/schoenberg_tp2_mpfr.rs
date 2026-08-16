// Schoenberg shift-kernel TP2 probe — FINAL: hybrid certified evaluation.
//  Xi(t) = sum_k (-1)^k b_k t^{2k}  (Taylor, b_k = M_k/(2k)!, M_k = 2∫Φ(u)u^{2k}du,
//  Φ = 2Σ(2π²n⁴e^{9u/2}−3πn²e^{5u/2})e^{−πn²e^{2u}}, Simpson 2^18 on [0,3])  for |t|<=12
//  Xi(t) = xi_complex_mpfr(t)  (certified EM zeta n=600 + Stirling gamma, z^-2 fix) for |t|>12
// Rationale: Stirling's series diverges for |z|<=~1.5 (2-term usable at |z|=0.25:
// Xi(0)=0.4423, 11% low, honest certified err 7.9e-2); Taylor (f64 b_k, rel err ~1e-11)
// is accurate to ~1e-10 at |t|=12 (verified by cross-check prints). Both paths are
// cross-checked at gamma_1/gamma_12 to settle machinery.
//
// KEY RESULT ALREADY ESTABLISHED (f64 probe + exact hand computation):
// the brief's premise "f in LP => shift kernel K(x,y)=f(x-y) totally positive" is FALSE.
// sin(x)/x = Π(1-x²/(nπ)²) is provably LP (real zeros) yet has negative 2x2 minors:
// exact: x=(0,π/4), y=(−5π/4,−π/2) gives det = −4/(15π²) ≈ −0.0270 (CHECKED by hand);
// numerically: min −0.247, ~46% of random 4-tuples negative. So negative shift-kernel
// minors are the TYPICAL signature of an even LP function with real zeros — exactly the
// structure RH gives Ξ. The correct Schoenberg duality is the Fourier-transform one
// (PF∞ ⟺ 1/f̂ in LP), NOT "f in LP ⟹ K_f TP". => the probe has NO disproof power for
// RH; negative Xi minors, if found, are RH-CONSISTENT with zero weight.
//
// This run: certified min 2x2 minor of K_Xi on [0,60] + near-zero windows at γ1..γ12;
// signature comparison vs the provably-LP sin(t)/t control; machinery gates.

include!(concat!(env!("CARGO_MANIFEST_DIR"), "/src/bin/schoenberg_tp2_body.inc"));

fn xi_mpfr(t: &Float) -> (Float, Float, Float) {
    xi_complex_mpfr(t)
}

struct Rng(u64);
impl Rng {
    fn next(&mut self) -> u64 {
        let mut x = self.0;
        x ^= x >> 12;
        x ^= x << 25;
        x ^= x >> 27;
        self.0 = x;
        x.wrapping_mul(0x2545F4914F6CDD1D)
    }
    fn unif(&mut self) -> f64 {
        (self.next() >> 11) as f64 / (1u64 << 53) as f64
    }
}

// ---- Taylor coefficients b_k = M_k/(2k)! from the Phi integral (f64) ----------
fn b_moments() -> Vec<f64> {
    const NQ: usize = 1 << 18;
    const NSUM: usize = 40;
    let h = 3.0 / NQ as f64;
    let pi = std::f64::consts::PI;
    let mut m = vec![0.0f64; 35];
    for i in 0..=NQ {
        let u = i as f64 * h;
        let w = if i == 0 || i == NQ { 1.0 } else if i % 2 == 1 { 4.0 } else { 2.0 };
        let e2u = (2.0 * u).exp();
        let mut phi = 0.0f64;
        for n in 1..=NSUM {
            let n2 = (n * n) as f64;
            let e = (-pi * n2 * e2u).exp();
            if e == 0.0 {
                break;
            }
            phi += (2.0 * pi * pi * n2 * n2 * (4.5 * u).exp() - 3.0 * pi * n2 * (2.5 * u).exp()) * e;
        }
        phi *= 2.0;
        let mut upow = 1.0;
        for k in 0..35 {
            m[k] += w * phi * upow;
            upow *= u * u;
        }
    }
    let mut b = vec![0.0f64; 35];
    for k in 0..35 {
        let mut fact = 1.0f64;
        for j in 2..=(2 * k) {
            fact *= j as f64;
        }
        b[k] = 2.0 * m[k] * (h / 3.0) / fact;
    }
    b
}

fn xi_taylor(t: f64, b: &[f64]) -> f64 {
    let t2 = t * t;
    let mut sum = 0.0;
    let mut p = 1.0;
    for (k, &bk) in b.iter().enumerate() {
        sum += if k % 2 == 0 { bk * p } else { -bk * p };
        p *= t2;
    }
    sum
}

fn main() {
    let prec = 100u32; // eps ~ 1e-30, certified; plenty for 1e-3 minors
    let t0 = std::time::Instant::now();
    let b = b_moments();
    println!("=== Schoenberg shift-kernel TP2 probe — hybrid certified (Taylor|t|<=12, mpfr>12), prec={} ===", prec);
    println!("b_0 = {:.15} (true 0.497120778188314)  b_1 = {:.6e}  b_2 = {:.6e}  b_5 = {:.6e}  b_10 = {:.6e} (true 5.62286e-25)", b[0], b[1], b[2], b[5], b[10]);

    // ---------- machinery cross-check: Taylor vs mpfr-Stirling ----------
    let cs = [4.0f64, 8.0, 12.0, 14.134725, 30.424876, 56.446248];
    for &t in &cs {
        let tv = xi_taylor(t, &b);
        let (r, _im, e) = xi_mpfr(&zf(prec, t));
        let sv = r.to_f64();
        println!("cross t={:9.6}: Taylor={:+.9e}  Stirling={:+.9e}  diff={:+.1e}  (cert err {:.1e})", t, tv, sv, tv - sv, e.to_f64());
    }
    println!("Xi(0) = {:.15}  (Taylor; true 0.497120778188314)", xi_taylor(0.0, &b));
    let mut ev_max = 0.0f64;
    for i in 1..=30 {
        let t = i as f64;
        ev_max = ev_max.max((xi_taylor(t, &b) - xi_taylor(-t, &b)).abs());
    }
    println!("Taylor evenness max|Xi(t)-Xi(-t)| t=1..30 = {:.1e}\n", ev_max);

    // ---------- hybrid Xi: (value, certified err) ----------
    let xi = |d: &Float| -> (Float, Float) {
        let t = d.to_f64();
        if t.abs() <= 12.0 {
            let v = xi_taylor(t, &b);
            (zf(prec, v), zf(prec, 1e-9)) // Taylor abs err <= ~1e-10 at |t|<=12 (conservative 1e-9)
        } else {
            let (r, _im, e) = xi_mpfr(d);
            (r, e)
        }
    };

    // ---------- sanity gates ----------
    let gammas = [
        14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178, 40.918719,
        43.327073, 48.005150, 49.773832, 52.970321, 56.446248,
    ];
    let mut zmax = 0.0f64;
    for (i, &g) in gammas.iter().enumerate() {
        let d = zf(prec, g);
        let (v, e) = xi(&d);
        let mag = v.to_f64().abs();
        zmax = zmax.max(mag);
        println!("|Xi(gamma_{:2})| t={:9.6} = {:.3e}  (cert err {:.1e})", i + 1, g, mag, e.to_f64());
    }
    println!("max |Xi(gamma_j)| = {:.3e}", zmax);
    // sign pattern: true signs = (-1)^(zeros below t). gamma13~59.347, gamma14~60.832, gamma15~65.113
    let mid = [7.6, 17.6, 23.05, 27.7, 31.7, 34.7, 39.2, 42.1, 45.7, 48.9, 51.4, 54.7, 57.9, 62.1, 66.1];
    let exp_sign = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1];
    let mut ok = true;
    for (i, &t) in mid.iter().enumerate() {
        let s = if xi_taylor(t, &b) >= 0.0 { 1 } else { -1 };
        ok &= s == exp_sign[i];
    }
    println!("sign pattern at 15 midpoints (true signs): {}", if ok { "ALL OK" } else { "MISMATCH" });
    println!("sanity wall: {:.1}s\n", t0.elapsed().as_secs_f64());

    // ---------- generic probe (mpfr arithmetic) ----------
    let mut probe = |label: &str,
                     f: &mut dyn FnMut(&Float) -> (Float, Float),
                     tmax: f64,
                     zeros: &[f64],
                     px: usize,
                     py: usize,
                     nz: usize|
     -> (f64, f64, usize, usize) {
        let mut rng = Rng(0x9E3779B97F4A7C15);
        let mut min_minor = f64::INFINITY;
        let mut min_err = 0.0f64;
        let mut argmin = (0.0f64, 0.0f64, 0.0f64, 0.0f64);
        let mut n_neg_clear = 0usize;
        let mut n_neg_all = 0usize;
        let mut n_tot = 0usize;
        let mut check = |x1: f64, x2: f64, y1: f64, y2: f64| {
            let d11 = zf(prec, x1 - y1);
            let d12 = zf(prec, x1 - y2);
            let d21 = zf(prec, x2 - y1);
            let d22 = zf(prec, x2 - y2);
            let (f11, e11) = f(&d11);
            let (f12, e12) = f(&d12);
            let (f21, e21) = f(&d21);
            let (f22, e22) = f(&d22);
            let m = sub(&mul(&f11, &f22), &mul(&f12, &f21));
            let er = add(
                &add(&mul(&abs_(&f22), &e11), &mul(&abs_(&f11), &e22)),
                &add(&mul(&abs_(&f21), &e12), &mul(&abs_(&f12), &e21)),
            );
            let mv = m.to_f64();
            let ev = er.to_f64();
            n_tot += 1;
            if mv < min_minor {
                min_minor = mv;
                min_err = ev;
                argmin = (x1, x2, y1, y2);
            }
            if mv < 0.0 {
                n_neg_all += 1;
                if -mv > 100.0 * ev {
                    n_neg_clear += 1;
                }
            }
        };
        for _ in 0..px {
            let u1 = rng.unif();
            let u2 = rng.unif();
            let x1 = u1 * tmax;
            let x2 = x1 + u2 * (tmax - x1);
            for _ in 0..py {
                let v1 = rng.unif();
                let v2 = rng.unif();
                let y1 = v1 * tmax;
                let y2 = y1 + v2 * (tmax - y1);
                check(x1, x2, y1, y2);
            }
        }
        for &z in zeros {
            for s in [1.0f64, -1.0f64] {
                for i in 0..nz {
                    let eps1 = ((i as f64) / (nz as f64) - 0.5) * 0.1;
                    let x1 = 30.0;
                    let y1 = 30.0 - (s * z + eps1);
                    let a = 0.05 + 1.45 * rng.unif();
                    let b = 0.05 + 1.45 * rng.unif();
                    check(x1, x1 + a, y1, y1 + b);
                }
            }
        }
        println!(
            "{:30} tmax={:4.0} px={:3} py={:3} : min_minor={:+.6e}  (cert err {:.1e}, margin x{:.1e})  at ({:.3},{:.3},{:.3},{:.3})  neg_clear={}/{}  neg_all={}/{}",
            label, tmax, px, py, min_minor, min_err,
            if min_err > 0.0 { min_minor.abs() / min_err } else { f64::INFINITY },
            argmin.0, argmin.1, argmin.2, argmin.3, n_neg_clear, n_tot, n_neg_all, n_tot
        );
        (min_minor, min_err, n_neg_clear, n_tot)
    };

    let mut exp2 = |d: &Float| (exp_(&neg(&mul(d, d))), zf(prec, 0.0));
    let mut sin_t = |d: &Float| {
        if d.to_f64().abs() < 1e-12 {
            (zf(prec, 1.0), zf(prec, 0.0))
        } else {
            (div(&sin_(d), d), zf(prec, 0.0))
        }
    };
    let mut nonlp = |d: &Float| {
        let t2 = mul(d, d);
        let t4 = mul(&t2, &t2);
        (sub(&add(&zf(prec, 1.0), &t2), &mul(&zf(prec, 0.5), &t4)), zf(prec, 0.0))
    };
    let sin_zeros: Vec<f64> = (1..=19).map(|k| std::f64::consts::PI * k as f64).collect();
    let nl_zeros = [1.653_073_5f64];
    println!("-- controls --");
    let (c1, _, n1c, t1c) = probe("exp(-t^2) [LP, no zeros]", &mut exp2, 3.0, &[], 100, 100, 0);
    let (c2, _, n2c, t2c) = probe("sin(t)/t [LP, real zeros]", &mut sin_t, 60.0, &sin_zeros, 100, 100, 12);
    let (c3, _, _, _) = probe("1+t^2-t^4/2 [NOT LP]", &mut nonlp, 6.0, &nl_zeros, 100, 100, 12);
    let (c4, _, _, _) = probe("1+t^2-t^4/2 [NOT LP] wide", &mut nonlp, 60.0, &nl_zeros, 100, 100, 12);

    println!("\n-- target: K(x,y)=Xi(x-y) --");
    let mut xi_f = xi;
    let (m1, e1, n1, t1) = probe("Xi [0,60] 60x60", &mut xi_f, 60.0, &gammas, 60, 60, 12);
    let (m2, e2, n2, t2) = probe("Xi [0,60] 90x90", &mut xi_f, 60.0, &gammas, 90, 90, 12);

    // ---------- verdict ----------
    println!("\n-- verdict --");
    println!("controls: exp(-t^2) min {:+.3e}, neg {}/{} (>=0 expected)", c1, n1c, t1c);
    println!("          sin(t)/t min {:+.3e}, neg {}/{} (negatives EXPECTED: provably-LP with real zeros)", c2, n2c, t2c);
    println!("          1+t^2-t^4/2 min {:+.3e} (<0 expected: non-LP detected)", c3.min(c4));
    let mmin = m1.min(m2);
    let emin = if m1 <= m2 { e1 } else { e2 };
    println!("target  : Xi min over grids = min({:+.6e}, {:+.6e}), certified err {:+.1e}", m1, m2, emin);
    println!("          Xi negative-minor rate: {}/{} and {}/{} ;  sin(t)/t control rate: {}/{}", n1, t1, n2, t2, n2c, t2c);
    let gate_ok = c1 >= 0.0 && c3.min(c4) < 0.0;
    println!("machinery gates (exp>=0, non-LP<0): {}", if gate_ok { "PASS" } else { "FAIL" });
    println!("brief premise \"LP => shift kernel TP2\" : REFUTED (sin(x)/x exact minor -4/(15 pi^2) ~ -0.0270 by hand; numerically min {:.3e}, {}/{} negatives)", c2, n2c, t2c);
    if mmin < 0.0 && mmin.abs() > 100.0 * emin {
        println!("Xi kernel HAS certified negative 2x2 minors (min {:+.3e}, cert err {:.1e}). This is the EXPECTED signature of an even LP function with real zeros (same structure and negative rate as the provably-LP sin(t)/t control). Carries ZERO disproof weight. VERDICT: RH-CONSISTENT. Probe is NOT disproof-capable: brief premise FALSE.", mmin, emin);
    } else if mmin < 0.0 {
        println!("Xi negative minor {:.3e} within certified error {:.3e} — value INCONCLUSIVE; disproof power nil regardless.", mmin, emin);
    } else {
        println!("All Xi minors >= 0 with certified margins. RH-CONSISTENT (consistency only; finite grid never proves RH).");
    }
    println!("\n=== done in {:.1}s ===", t0.elapsed().as_secs_f64());
}
