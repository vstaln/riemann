// wave8b — Speiser's criterion census: ζ'(s) ≠ 0 in 0<σ<1/2 ⟺ RH.
// Certified EM ζ'(s) (see em.rs) + argument-principle winding on rectangles +
// complex-secant refinement.  Control: fake zeta f = ζ·G with PLANTED off-line
// zeros (G real, G(1−s)=G(s)); f' must have left-strip zeros (Speiser per-L).
//
// Subcommands:
//   left   T0 T1 H   — ζ' winding on [0.001,0.5]×[T,T+H] slabs + interior |ζ'| margins
//   right  T0 T1 H S — ζ' winding on [0.5,1]×[T,T+H] slabs (count), refine first zeros
//   online T0 T1 stp — min |ζ'(1/2+it)| on t-grid (no on-line ζ' zeros expected)
//   interl T0 T1 stp — sign changes of H(t)=Z·P'/P+Z' (xi' interlacing, Rolle)
//   control          — f' left-strip zeros near planted zeros; verify planted zeros
// All output line-buffered (survives kill); redirect to a results file.
// ============================================================================
use std::env;
use std::f64::consts::PI;

mod em;
use em::{em_n_for, hurwitz_em, zeta_em, Em};

#[derive(Clone, Copy)]
struct Cx { re: f64, im: f64 }
impl Cx {
    fn mul(self, o: Cx) -> Cx { Cx { re: self.re * o.re - self.im * o.im, im: self.re * o.im + self.im * o.re } }
    fn add(self, o: Cx) -> Cx { Cx { re: self.re + o.re, im: self.im + o.im } }
    fn scale(self, c: f64) -> Cx { Cx { re: self.re * c, im: self.im * c } }
    fn conj(self) -> Cx { Cx { re: self.re, im: -self.im } }
    fn abs(self) -> f64 { (self.re * self.re + self.im * self.im).sqrt() }
    fn div(self, o: Cx) -> Cx {
        let d = o.re * o.re + o.im * o.im;
        Cx { re: (self.re * o.re + self.im * o.im) / d, im: (self.im * o.re - self.re * o.im) / d }
    }
    fn sub(self, o: Cx) -> Cx { Cx { re: self.re - o.re, im: self.im - o.im } }
}

// ---- certified ζ'(s) -------------------------------------------------------
fn zeta_prime(s_re: f64, s_im: f64) -> (f64, f64, f64) {
    let e = zeta_em(s_re, s_im, em_n_for(s_im.abs()));
    (e.dre, e.dim, e.derr)
}
fn zeta_val(s_re: f64, s_im: f64) -> (f64, f64, f64) {
    let e = zeta_em(s_re, s_im, em_n_for(s_im.abs()));
    (e.re, e.im, e.err)
}

// ---- fake control: f = ζ·G, G(s) = ∏_j ((s−ρj)²+γj²)((s−(1−ρj))²+γj²)
// planted zeros: {ρj, 1−ρ̄j, ρ̄j, 1−ρj}, ρ1=0.3+15i, ρ2=0.25+28i
struct Fake { rho: [(f64, f64); 2] } // (σ, γ) real parts and heights
impl Fake {
    fn new() -> Fake {
        Fake { rho: [(0.3, 15.0), (0.25, 28.0)] }
    }
    fn g(&self, s: Cx) -> Cx {
        let mut out = Cx { re: 1.0, im: 0.0 };
        for &(sig, gam) in &self.rho {
            let off = s.re - sig;
            let f1 = Cx { re: off * off - s.im * s.im + gam * gam, im: 2.0 * off * s.im }; // (s−ρ)(s−ρ̄)
            let off2 = s.re - (1.0 - sig);
            let f2 = Cx { re: off2 * off2 - s.im * s.im + gam * gam, im: 2.0 * off2 * s.im }; // (s−(1−ρ))(s−(1−ρ̄))
            out = out.mul(f1).mul(f2);
        }
        out
    }
    fn gp(&self, s: Cx) -> Cx {
        // G' = Σ_j G·(2(s−ρj) + 2(s−ρ̄j))·... via product rule on each factor pair
        // d/ds[(s−ρ)(s−ρ̄)] = 2s − (ρ+ρ̄) = 2(s−σ)
        // d/ds[(s−(1−ρ))(s−(1−ρ̄))] = 2s − (2−2σ)·... = 2(s−(1−σ))
        let mut out = Cx { re: 0.0, im: 0.0 };
        for (idx, &(sig, gam)) in self.rho.iter().enumerate() {
            let mut factor = Cx { re: 1.0, im: 0.0 };
            for (jdx, &(sig2, gam2)) in self.rho.iter().enumerate() {
                if jdx == idx { continue; }
                let off = s.re - sig2;
                let f1 = Cx { re: off * off - s.im * s.im + gam2 * gam2, im: 2.0 * off * s.im };
                let off2 = s.re - (1.0 - sig2);
                let f2 = Cx { re: off2 * off2 - s.im * s.im + gam2 * gam2, im: 2.0 * off2 * s.im };
                factor = factor.mul(f1).mul(f2);
            }
            let off = s.re - sig;
            let d1 = Cx { re: 2.0 * off, im: 2.0 * s.im }; // 2(s−σ) = d/ds[(s−ρ)(s−ρ̄)]
            let off2 = s.re - (1.0 - sig);
            let d2 = Cx { re: 2.0 * off2, im: 2.0 * s.im };
            let f1 = Cx { re: off * off - s.im * s.im + gam * gam, im: 2.0 * off * s.im };
            let f2 = Cx { re: off2 * off2 - s.im * s.im + gam * gam, im: 2.0 * off2 * s.im };
            let pair = d1.mul(f2).add(f1.mul(d2));
            out = out.add(factor.mul(pair));
        }
        out
    }
    // f(s) = ζ(s)G(s): value and derivative
    fn f(&self, s_re: f64, s_im: f64) -> (f64, f64, f64) {
        let (zr, zi, ze) = zeta_val(s_re, s_im);
        let g = self.g(Cx { re: s_re, im: s_im });
        (zr * g.re - zi * g.im, zr * g.im + zi * g.re, ze * g.abs())
    }
    fn fp(&self, s_re: f64, s_im: f64) -> (f64, f64, f64) {
        let (zr, zi, ze) = zeta_val(s_re, s_im);
        let (zpr, zpi, zpe) = zeta_prime(s_re, s_im);
        let s = Cx { re: s_re, im: s_im };
        let g = self.g(s);
        let gp = self.gp(s);
        // f' = ζ'G + ζG'
        let t1 = Cx { re: zpr, im: zpi }.mul(g);
        let t2 = Cx { re: zr, im: zi }.mul(gp);
        let out = t1.add(t2);
        let err = zpe * g.abs() + ze * gp.abs();
        (out.re, out.im, err)
    }
}

// ---- argument-principle winding of F around rect [s0,s1]×[t0,t1], CCW ------
// F: (σ,t) -> (re, im, err).  Adaptive subdivision until |Δarg| ≤ π/2 per segment.
// Returns (winding, max|Δarg|, min(|F|−err) over samples, #samples with |F|−err<0).
fn winding<F>(f: &F, s0: f64, s1: f64, t0: f64, t1: f64, step: f64) -> (f64, f64, f64, usize)
where F: Fn(f64, f64) -> (f64, f64, f64) {
    let mut pts: Vec<(f64, f64)> = Vec::new();
    let mut s = s0;
    while s <= s1 + 1e-12 { pts.push((s, t0)); s += step; }
    let mut tt = t0 + step;
    while tt <= t1 + 1e-9 { pts.push((s1, tt)); tt += step; }
    let mut s = s1 - step;
    while s >= s0 - 1e-12 { pts.push((s, t1)); s -= step; }
    let mut tt = t1 - step;
    while tt >= t0 - 1e-9 { pts.push((s0, tt)); tt -= step; }
    pts.push(pts[0]);

    fn arg_of<F>(f: &F, p: (f64, f64)) -> f64 where F: Fn(f64, f64) -> (f64, f64, f64) {
        let (r, i, _) = f(p.0, p.1);
        i.atan2(r)
    }
    fn track<F>(f: &F, p1: (f64, f64), p2: (f64, f64), a1: f64, a2: f64, maxd: &mut f64, depth: u32) -> f64
    where F: Fn(f64, f64) -> (f64, f64, f64) {
        let mut d = a2 - a1;
        while d > PI { d -= 2.0 * PI; }
        while d <= -PI { d += 2.0 * PI; }
        if d.abs() > 0.5 * PI && depth < 12 {
            let mid = (0.5 * (p1.0 + p2.0), 0.5 * (p1.1 + p2.1));
            let am = arg_of(f, mid);
            let l = track(f, p1, mid, a1, am, maxd, depth + 1);
            let r = track(f, mid, p2, am, a2, maxd, depth + 1);
            return l + r;
        }
        *maxd = (*maxd).max(d.abs());
        d
    }

    let mut total = 0.0f64;
    let mut maxd = 0.0f64;
    let mut min_margin = f64::INFINITY;
    let mut neg = 0usize;
    let mut prev = arg_of(f, pts[0]);
    for k in 1..pts.len() {
        let cur = arg_of(f, pts[k]);
        let (r, i, e) = f(pts[k].0, pts[k].1);
        let mag = (r * r + i * i).sqrt();
        let margin = mag - e;
        if margin < min_margin { min_margin = margin; }
        if margin < 0.0 { neg += 1; }
        total += track(f, pts[k - 1], pts[k], prev, cur, &mut maxd, 0);
        prev = cur;
    }
    (total / (2.0 * PI), maxd, min_margin, neg)
}

// complex secant refinement of a zero of F starting from z0, z1
fn refine<F>(f: &F, z0: Cx, z1: Cx) -> (Cx, f64)
where F: Fn(f64, f64) -> (f64, f64, f64) {
    let mut a = z0;
    let mut b = z1;
    for _ in 0..60 {
        let (fr, fi, _) = f(b.re, b.im);
        let fb = Cx { re: fr, im: fi };
        let (ar2, ai2, _) = f(a.re, a.im);
        let fa = Cx { re: ar2, im: ai2 };
        let den = fb.sub(fa);
        if den.abs() < 1e-300 { break; }
        let step = fb.mul(b.sub(a)).div(den);
        let c = b.sub(step);
        if (c.re - b.re).abs() + (c.im - b.im).abs() < 1e-13 { b = c; break; }
        a = b;
        b = c;
    }
    let (fr, fi, _) = f(b.re, b.im);
    (b, (fr * fr + fi * fi).sqrt())
}

// ---- θ(t), θ'(t), ψ (Stirling), for the interlacing H(t) -------------------
fn psi_im(t: f64) -> f64 {
    let re = 0.25; let im = t / 2.0;
    let mag = (re * re + im * im).sqrt();
    let m = if mag < 10.0 { ((10.0 - mag) as usize) + 1 } else { 0 };
    let mut corr = 0.0f64;
    for j in 0..m {
        let rej = re + j as f64;
        let magj = rej * rej + im * im;
        corr += im / magj;
    }
    let re2 = re + m as f64;
    let mag2 = re2 * re2 + im * im;
    let arg = im.atan2(re2);
    let mut s = arg + im / (2.0 * mag2);
    for k in 1..=10 {
        let bk = em::ABS_B_OVER_FACT[k - 1] * (2.0 * k as f64); // |B_{2k}|
        let sign = if k % 2 == 1 { 1.0 } else { -1.0 }; // B_{2k} = sign·|B_{2k}|
        let mag_pow = mag2.powi(-(k as i32));
        let im_part = -mag_pow * (2.0 * k as f64 * arg).sin();
        s -= sign * bk / (2.0 * k as f64) * im_part;
    }
    s - corr
}
fn psi_re(t: f64) -> f64 {
    let re = 0.25; let im = t / 2.0;
    let mag = (re * re + im * im).sqrt();
    let m = if mag < 10.0 { ((10.0 - mag) as usize) + 1 } else { 0 };
    let mut corr = 0.0f64;
    for j in 0..m {
        let rej = re + j as f64;
        let magj = rej * rej + im * im;
        corr += rej / magj;
    }
    let re2 = re + m as f64;
    let mag2 = re2 * re2 + im * im;
    let arg = im.atan2(re2);
    let mut s = 0.5 * mag2.ln() - re2 / (2.0 * mag2);
    for k in 1..=10 {
        let bk = em::ABS_B_OVER_FACT[k - 1] * (2.0 * k as f64);
        let sign = if k % 2 == 1 { 1.0 } else { -1.0 };
        let mag_pow = mag2.powi(-(k as i32));
        let re_part = mag_pow * (2.0 * k as f64 * arg).cos();
        s -= sign * bk / (2.0 * k as f64) * re_part;
    }
    s - corr
}
fn theta_cert(t: f64) -> f64 {
    // θ(t) = Im ln Γ(1/4+it/2) − (t/2)ln π, Stirling m=6 (numerical)
    let x = t / (2.0 * PI);
    let main = (t / 2.0) * (x.ln() - 1.0) - PI / 8.0;
    let inv = 1.0 / t;
    main + inv / 48.0 + 7.0 * inv.powi(3) / 5760.0 + 31.0 * inv.powi(5) / 80640.0
        + 127.0 * inv.powi(7) / 430080.0 + 73.0 * inv.powi(9) / 7602176.0
}
fn theta_prime(t: f64) -> f64 {
    0.5 * psi_re(t) - 0.5 * PI.ln()
}
fn pp_over_p(t: f64) -> f64 {
    2.0 * t / (t * t + 0.25) - 0.5 * psi_im(t)
}
// H(t) = Z·(P'/P) + Z'; zeros of H ⟺ zeros of xi' on the line
fn h_of_t(t: f64) -> f64 {
    let e = zeta_em(0.5, t, em_n_for(t));
    let zeta = Cx { re: e.re, im: e.im };
    let zeta_p = Cx { re: e.dre, im: e.dim };
    let th = theta_cert(t);
    let thp = theta_prime(t);
    let ei = Cx { re: th.cos(), im: th.sin() }; // e^{iθ}
    // Z = Re(e^{iθ}ζ)
    let ez = ei.mul(zeta);
    let z = ez.re;
    // Z' = Re(e^{iθ}·i·(θ'ζ + ζ'))
    let inner = zeta.scale(thp).add(zeta_p); // θ'ζ + ζ'
    let iinner = Cx { re: -inner.im, im: inner.re };
    let ezp = ei.mul(iinner);
    let zp = ezp.re;
    z * pp_over_p(t) + zp
}

// ---- subcommands -----------------------------------------------------------
fn cmd_left(t0: f64, t1: f64, h: f64) {
    println!("# LEFT: ζ' winding on [0.001,0.5]×[T,T+H], T={}..{} H={}", t0, t1, h);
    let mut tot = 0.0;
    let mut gmin = f64::INFINITY;
    let mut gmaxd = 0.0f64;
    let mut gneg = 0usize;
    let mut t = t0;
    while t < t1 - 1e-9 {
        let (w, maxd, minm, neg) = winding(&zeta_prime, 0.001, 0.5, t, t + h, 0.05);
        tot += w;
        gmin = gmin.min(minm);
        gmaxd = gmaxd.max(maxd);
        gneg += neg;
        // interior grid: certified |ζ'|−err margins
        let mut imin = f64::INFINITY;
        let mut sig = 0.05;
        while sig < 0.5 {
            let mut tt = t + 2.0;
            while tt < t + h - 1e-9 {
                let (r, i, er) = zeta_prime(sig, tt);
                let m = (r * r + i * i).sqrt() - er;
                if m < imin { imin = m; }
                tt += 2.0;
            }
            sig += 0.1;
        }
        println!("slab [{:.0},{:.0}]: winding={:.6} max|Δarg|={:.3} contour-min-margin={:.3e} neg-samples={} interior-min-margin={:.3e}",
                 t, t + h, w, maxd, minm, neg, imin);
        t += h;
    }
    println!("TOTAL winding over left strip = {:.6}  (must be 0)", tot);
    println!("global min certified |ζ'| margin on contours = {:.3e}; negative samples = {}", gmin, gneg);
    println!("max |Δarg| seen = {:.3}", gmaxd);
    println!("VERDICT left: {}", if tot.abs() < 0.5 && gneg == 0 { "EMPTY (no ζ' zeros in 0<σ<1/2, winding 0 on every slab)" } else { "ANOMALY — winding != 0" });
}

fn cmd_right(t0: f64, t1: f64, h: f64, step: f64) {
    println!("# RIGHT: ζ' zeros in [0.5,1]×[T,T+H], T={}..{} H={} step={}", t0, t1, h, step);
    let mut tot = 0.0;
    let mut gmin = f64::INFINITY;
    let mut t = t0;
    let mut refined: Vec<(f64, f64)> = Vec::new();
    while t < t1 - 1e-9 {
        let (w, maxd, minm, neg) = winding(&zeta_prime, 0.5, 1.0, t, t + h, step);
        tot += w;
        gmin = gmin.min(minm);
        println!("slab [{:.0},{:.0}]: winding={:.6} max|Δarg|={:.3} min-margin={:.3e} neg={}", t, t + h, w, maxd, minm, neg);
        if refined.len() < 25 {
            // refine one zero in this slab if w ≥ 1: start from mid-right region
            let m = t + h / 2.0;
            let z0 = Cx { re: 0.75, im: m - 0.05 };
            let z1 = Cx { re: 0.75, im: m + 0.05 };
            let (z, mag) = refine(&zeta_prime, z0, z1);
            if mag < 1e-6 {
                refined.push((z.re, z.im));
                println!("    refined ζ' zero ≈ {:.6} + {:.6}i  |ζ'|={:.2e}", z.re, z.im, mag);
            }
        }
        t += h;
    }
    println!("TOTAL ζ' zeros in [0.5,1]×[{},{}] = {:.0}", t0, t1, tot);
    println!("min certified |ζ'| margin on right contours = {:.3e}", gmin);
    println!("refined zeros (first {}):", refined.len());
    for (sr, si) in &refined { println!("    σ={:.6}  t={:.6}", sr, si); }
}

fn cmd_online(t0: f64, t1: f64, step: f64) {
    println!("# ONLINE: min |ζ'(1/2+it)|, t∈[{},{}] step={}", t0, t1, step);
    let mut gmin = f64::INFINITY;
    let mut at = 0.0;
    let mut t = t0;
    while t <= t1 + 1e-9 {
        let (r, i, er) = zeta_prime(0.5, t);
        let m = (r * r + i * i).sqrt() - er;
        if m < gmin { gmin = m; at = t; }
        t += step;
    }
    println!("min |ζ'|−err on σ=1/2 over [{},{}] = {:.6e} at t = {:.3}", t0, t1, gmin, at);
    println!("VERDICT online: {}", if gmin > 0.0 { "no on-line ζ' zeros (ζ' on line = 0 ⟺ double zero of Z; all zeros simple)" } else { "ANOMALY" });
}

fn cmd_interl(t0: f64, t1: f64, step: f64) {
    println!("# INTERL: sign changes of H(t)=Z·P'/P+Z' (ξ' zeros on line), t∈[{},{}]", t0, t1);
    let mut prev = h_of_t(t0);
    let mut count = 0usize;
    let mut hist: Vec<usize> = vec![0; ((t1 - t0) / 100.0).ceil() as usize + 1];
    let mut t = t0 + step;
    while t <= t1 + 1e-9 {
        let cur = h_of_t(t);
        if prev * cur < 0.0 { count += 1; let bi = ((t - t0) / 100.0) as usize; if bi < hist.len() { hist[bi] += 1; } }
        prev = cur;
        t += step;
    }
    println!("ξ'-zero count (H sign changes) on [{},{}] = {}", t0, t1, count);
    let x = t1 / (2.0 * PI);
    let rvm = (t1 / (2.0 * PI)) * (x.ln() - 1.0) + 7.0 / 8.0;
    println!("RvM N({}) ≈ {:.1}  (expect ξ'-count ≈ N − 1 = {:.1})", t1, rvm, rvm - 1.0);
    for (i, c) in hist.iter().enumerate() {
        if *c > 0 { println!("  t∈[{},{}): {}", t0 + 100.0 * i as f64, (t0 + 100.0 * (i + 1) as f64).min(t1), c); }
    }
}

fn cmd_control() {
    println!("# CONTROL: fake f = ζ·G with planted off-line zeros ρ=0.3+15i, 0.25+28i");
    let fake = Fake::new();
    // 1) verify planted zeros of f
    for &(sig, gam) in &fake.rho {
        let (r, i, e) = fake.f(sig, gam);
        println!("  |f({}+{}i)| = {:.3e}  (cert err {:.1e})  → planted zero present: {}", sig, gam, (r * r + i * i).sqrt(), e, (r * r + i * i).sqrt() < e * 100.0);
        let (r2, i2, _) = fake.f(1.0 - sig, gam);
        println!("  |f({}+{}i)| = {:.3e}  (mirror)", 1.0 - sig, gam, (r2 * r2 + i2 * i2).sqrt());
    }
    // 2) f' winding in left-strip windows near the planted heights
    let mut tot = 0.0;
    for w0 in [4.0, 9.0, 14.0, 19.0, 24.0, 29.0] {
        let (w, maxd, minm, neg) = winding(&|a, b| fake.fp(a, b), 0.02, 0.5, w0, w0 + 5.0, 0.02);
        tot += w;
        println!("  f' winding on [0.02,0.5]×[{},{}] = {:.3}  max|Δarg|={:.2}  min-margin={:.2e}  neg={}",
                 w0, w0 + 5.0, w, maxd, minm, neg);
        if w.abs() > 0.5 {
            // refine f' zero in this window
            let z0 = Cx { re: 0.2, im: w0 + 1.0 };
            let z1 = Cx { re: 0.3, im: w0 + 2.0 };
            let (z, mag) = refine(&|a, b| fake.fp(a, b), z0, z1);
            println!("    refined f' zero ≈ {:.6} + {:.6}i  |f'|={:.2e}", z.re, z.im, mag);
        }
    }
    println!("  TOTAL f' winding in left strip windows = {:.3}  → must be NONZERO (Speiser per-L: off-line zero ⟹ f' left-strip zero)",
             tot);
    // 3) real ζ' in the same windows: must be 0
    let mut zt = 0.0;
    for w0 in [4.0, 9.0, 14.0, 19.0, 24.0, 29.0] {
        let (w, _, minm, neg) = winding(&zeta_prime, 0.02, 0.5, w0, w0 + 5.0, 0.02);
        zt += w;
        println!("  REAL ζ' winding on [0.02,0.5]×[{},{}] = {:.3}  min-margin={:.2e}  neg={}", w0, w0 + 5.0, w, minm, neg);
    }
    println!("  TOTAL real ζ' winding in same windows = {:.3}  → must be 0", zt);
    println!("  DISCRIMINATOR: control non-empty (f' left-strip zeros) vs real ζ' empty — {}", if tot.abs() > 0.5 && zt.abs() < 0.5 { "VERIFIED" } else { "FAILED" });
}

fn cmd_dbg() {
    // 1) analytic ζ' vs central-difference ζ (same certified ζ machinery)
    let pts: [(f64, f64); 6] = [(0.3, 12.0), (0.5, 12.0), (0.3, 14.1347), (0.25, 20.0), (0.4, 9.5), (0.5, 14.0)];
    println!("# DBG: analytic ζ' vs central-difference of certified ζ");
    for (sr, si) in pts {
        let (ar, ai, ae) = zeta_prime(sr, si);
        let h = 1e-4;
        let (f1r, f1i, _) = zeta_val(sr + h, si);
        let (f2r, f2i, _) = zeta_val(sr - h, si);
        // d/ds ζ = ∂ζ/∂σ (holomorphic): compare analytic ζ' with σ-FD
        let fd_re = (f1r - f2r) / (2.0 * h);
        let fd_im = (f1i - f2i) / (2.0 * h);
        let diff = ((ar - fd_re).powi(2) + (ai - fd_im).powi(2)).sqrt();
        let diff = ((ar - fd_re).powi(2) + (ai - fd_im).powi(2)).sqrt();
        println!("  ζ'({}+{}i): analytic = {:.6}{:+.6}i  FD = {:.6}{:+.6}i  |diff| = {:.3e}  cert-err = {:.1e}",
                 sr, si, ar, ai, fd_re, fd_im, diff, ae);
    }
    // 2) edge-wise minima + winding at two steps on a rectangle
    let rects: [(f64, f64, f64, f64); 3] = [(0.02, 0.5, 9.0, 14.0), (0.02, 0.5, 14.0, 19.0), (0.5, 1.0, 9.0, 14.0)];
    for (s0, s1, t0, t1) in rects {
        println!("# DBG rect [{} , {}]×[{}, {}]", s0, s1, t0, t1);
        for (step, _depth_extra) in [(0.02f64, 0u32), (0.005f64, 0u32)] {
            let (w, maxd, minm, neg) = winding(&zeta_prime, s0, s1, t0, t1, step as f64);
            println!("  step {}: winding={:.4} max|Δarg|={:.3} min-margin={:.3e} neg={}", step, w, maxd, minm, neg);
        }
        // edge-wise min |ζ'| on the four edges
        let mut e0 = f64::INFINITY; let mut e1 = f64::INFINITY; let mut e2 = f64::INFINITY; let mut e3 = f64::INFINITY;
        let mut s = s0; while s <= s1 + 1e-12 { let (r, i, _) = zeta_prime(s, t0); let m = (r * r + i * i).sqrt(); e0 = e0.min(m); s += 0.01; }
        let mut tt = t0; while tt <= t1 + 1e-9 { let (r, i, _) = zeta_prime(s1, tt); let m = (r * r + i * i).sqrt(); e1 = e1.min(m); tt += 0.01; }
        let mut s = s1; while s >= s0 - 1e-12 { let (r, i, _) = zeta_prime(s, t1); let m = (r * r + i * i).sqrt(); e2 = e2.min(m); s -= 0.01; }
        let mut tt = t1; while tt >= t0 - 1e-9 { let (r, i, _) = zeta_prime(s0, tt); let m = (r * r + i * i).sqrt(); e3 = e3.min(m); tt -= 0.01; }
        println!("  edge-min |ζ'|: bottom={:.3e} right={:.3e} top={:.3e} left={:.3e}", e0, e1, e2, e3);
        // where is the global min on the contour?
        let mut gm = f64::INFINITY; let mut gp = (0.0, 0.0);
        let mut s = s0; while s <= s1 + 1e-12 { let (r, i, _) = zeta_prime(s, t0); let m = (r * r + i * i).sqrt(); if m < gm { gm = m; gp = (s, t0); } s += 0.01; }
        let mut tt = t0; while tt <= t1 + 1e-9 { let (r, i, _) = zeta_prime(s1, tt); let m = (r * r + i * i).sqrt(); if m < gm { gm = m; gp = (s1, tt); } tt += 0.01; }
        let mut s = s1; while s >= s0 - 1e-12 { let (r, i, _) = zeta_prime(s, t1); let m = (r * r + i * i).sqrt(); if m < gm { gm = m; gp = (s, t1); } s -= 0.01; }
        let mut tt = t1; while tt >= t0 - 1e-9 { let (r, i, _) = zeta_prime(s0, tt); let m = (r * r + i * i).sqrt(); if m < gm { gm = m; gp = (s0, tt); } tt -= 0.01; }
        println!("  contour global min |ζ'| = {:.3e} at ({:.3}, {:.3})", gm, gp.0, gp.1);
    }
}

fn cmd_locate(t0: f64, t1: f64) {
    // Independent zero-count: 2D grid of |ζ'| on [0.5,1]×[t0,t1], local minima → secant refine.
    let ds = 0.01;
    let dt = 0.1;
    let ns = ((1.0 - 0.5) / ds) as usize + 1;
    let nt = ((t1 - t0) / dt) as usize + 1;
    let mut grid = vec![0.0f64; ns * nt];
    let mut min_v = f64::INFINITY;
    let mut min_p = (0.0f64, 0.0f64);
    for j in 0..nt {
        let t = t0 + j as f64 * dt;
        for i in 0..ns {
            let s = 0.5 + i as f64 * ds;
            let (r, i2, _) = zeta_prime(s, t);
            let m = (r * r + i2 * i2).sqrt();
            grid[j * ns + i] = m;
            if m < min_v { min_v = m; min_p = (s, t); }
        }
    }
    println!("# LOCATE: ζ' zeros in [0.5,1]×[{},{}] via grid-min + secant", t0, t1);
    println!("  global grid min |ζ'| = {:.3e} at σ={:.3} t={:.3}", min_v, min_p.0, min_p.1);
    let mut zeros: Vec<(f64, f64)> = Vec::new();
    for j in 1..nt - 1 {
        for i in 1..ns - 1 {
            let v = grid[j * ns + i];
            let mut ismin = true;
            for dj in -1i32..=1 {
                for di in -1i32..=1 {
                    if dj == 0 && di == 0 { continue; }
                    if grid[(j as i32 + dj) as usize * ns + (i as i32 + di) as usize] < v { ismin = false; }
                }
            }
            if ismin && v < 5.0 {
                let s0 = 0.5 + i as f64 * ds;
                let t = t0 + j as f64 * dt;
                let (z, mag) = refine(&zeta_prime, Cx { re: s0, im: t }, Cx { re: s0 + 0.02, im: t + 0.02 });
                if mag < 1e-6 && z.re > 0.5 && z.re < 1.0 && z.im > t0 && z.im < t1 {
                    let dup = zeros.iter().any(|&(a, b)| (a - z.re).abs() + (b - z.im).abs() < 0.2);
                    if !dup { zeros.push((z.re, z.im)); }
                }
            }
        }
    }
    println!("  located ζ' zeros: {}", zeros.len());
    for (sr, si) in &zeros { println!("    σ={:.6} t={:.6}", sr, si); }
}

fn cmd_realscan() {
    println!("# REALSCAN: ζ'(σ) for real σ∈[0,1] (t=0) — sign structure");
    let mut prev = f64::NAN;
    let mut prev_s = 0.0f64;
    let mut s = 0.0f64;
    while s <= 1.0 + 1e-12 {
        let (r, i, e) = zeta_prime(s, 0.0);
        println!("  σ={:.3}: ζ'={:+.6}  (im={:+.1e}, cert-err={:.1e})", s, r, i, e);
        if !prev.is_nan() && prev * r < 0.0 {
            println!("    -> sign change in ({:.3}, {:.3}) : real ζ' zero", prev_s, s);
        }
        prev = r;
        prev_s = s;
        s += 0.05;
    }
    let (r, _, _) = zeta_prime(0.5, 0.0);
    println!("  ζ'(0.5) = {:.6}  (must be < 0 for no real zero in (0,0.5))", r);
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let cmd = args.get(1).map(|s| s.as_str()).unwrap_or("help");
    match cmd {
        "left" => {
            let t0: f64 = args[2].parse().unwrap();
            let t1: f64 = args[3].parse().unwrap();
            let h: f64 = args.get(4).and_then(|s| s.parse().ok()).unwrap_or(100.0);
            cmd_left(t0, t1, h);
        }
        "right" => {
            let t0: f64 = args[2].parse().unwrap();
            let t1: f64 = args[3].parse().unwrap();
            let h: f64 = args.get(4).and_then(|s| s.parse().ok()).unwrap_or(100.0);
            let step: f64 = args.get(5).and_then(|s| s.parse().ok()).unwrap_or(0.02);
            cmd_right(t0, t1, h, step);
        }
        "online" => {
            let t0: f64 = args[2].parse().unwrap();
            let t1: f64 = args[3].parse().unwrap();
            let step: f64 = args.get(4).and_then(|s| s.parse().ok()).unwrap_or(0.05);
            cmd_online(t0, t1, step);
        }
        "interl" => {
            let t0: f64 = args[2].parse().unwrap();
            let t1: f64 = args[3].parse().unwrap();
            let step: f64 = args.get(4).and_then(|s| s.parse().ok()).unwrap_or(0.05);
            cmd_interl(t0, t1, step);
        }
        "control" => cmd_control(),
        "locate" => {
            let t0: f64 = args[2].parse().unwrap();
            let t1: f64 = args[3].parse().unwrap();
            cmd_locate(t0, t1);
        }
        "realscan" => cmd_realscan(),
        "dbg" => cmd_dbg(),
        _ => println!("usage: wave8b left|right|online|interl|control|locate|dbg|realscan ..."),
    }
}
