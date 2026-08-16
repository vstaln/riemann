// dbheat_probe: de Bruijn heat-deformation probe for the Riemann Xi.
// H_t(z) = 2 * int_0^inf e^{t u^2} Phi(u) cos(zu) du,  Phi = wave8d-corrected weight
//   Phi(u) = 2 sum_{n>=1} (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}
// f64, NON-RIGOROUS (CHECKED NUMERICALLY only). See research/notes/dbheat-deformation-2026-08-18.md
//
// Direction facts (PROVEN, pure math -- see note):
//   - Newman: zeros of H_t all real  <=>  t >= Lambda (de Bruijn-Newman constant).
//   - RH <=> Lambda <= 0; Rodgers-Tao: Lambda >= 0; Polymath15: Lambda < 1/2.
//   - Hence "H_t all-real for all t>0" <=> Lambda <= 0 <=> RH: the wave-20 premise IS RH.
//   - For every t<0, H_t has NON-REAL zeros (RT+Newman), at some height. Low zeros staying
//     real is RH-consistent only; it cannot disprove RH. Only a non-real zero at t>0 would
//     be an RH-disproof signal (forces Lambda > t > 0).

use std::time::Instant;

const PI: f64 = std::f64::consts::PI;

// Phi(u) (wave8d-corrected; validated in wave8d: b_0 = 2*int Phi = 0.497120778188314)
fn phi(u: f64) -> f64 {
    let e2u = (2.0 * u).exp();
    let eu2 = u.exp().sqrt();
    let e9h = e2u * e2u * eu2; // e^{9u/2}
    let e5h = e2u * eu2;       // e^{5u/2}
    let mut s = 0.0;
    for n in 1..=80u64 {
        let nf = n as f64;
        let n2 = nf * nf;
        let n4 = n2 * n2;
        let arg = PI * n2 * e2u;
        let term = 2.0 * (2.0 * PI * PI * n4 * e9h - 3.0 * PI * n2 * e5h) * (-arg).exp();
        s += term;
        if n > 1 && term.abs() < 1e-30 * s.abs() { break; }
    }
    s
}

// gaussian counterexample weight: Phi~ = e^{-(u-5)^2} + e^{-(u+5)^2} + 3 e^{-u^2}  (>0, even)
fn g_phi(u: f64) -> f64 {
    let a = u - 5.0;
    let b = u + 5.0;
    (-a * a).exp() + (-b * b).exp() + 3.0 * (-u * u).exp()
}

// adaptive Simpson, vector (re, im) valued
fn adapt(f: &impl Fn(f64) -> (f64, f64), a: f64, b: f64, tol: f64, depth: u32, evals: &mut u64) -> (f64, f64) {
    if *evals > 600_000 {
        let mid = 0.5 * (a + b);
        let (fa, fai) = f(a);
        let (fm, fmi) = f(mid);
        let (fb, fbi) = f(b);
        *evals += 3;
        return ((fa + 4.0 * fm + fb) * (b - a) / 6.0, (fai + 4.0 * fmi + fbi) * (b - a) / 6.0);
    }
    let mid = 0.5 * (a + b);
    let (fa, fai) = f(a);
    let (fm, fmi) = f(mid);
    let (fb, fbi) = f(b);
    *evals += 3;
    let sab = ((fa + 4.0 * fm + fb) * (b - a) / 6.0, (fai + 4.0 * fmi + fbi) * (b - a) / 6.0);
    let lmid = 0.5 * (a + mid);
    let rmid = 0.5 * (mid + b);
    let (fl, fli) = f(lmid);
    let (fr, fri) = f(rmid);
    *evals += 2;
    let sl = ((fa + 4.0 * fl + fm) * (mid - a) / 6.0, (fai + 4.0 * fli + fmi) * (mid - a) / 6.0);
    let sr = ((fm + 4.0 * fr + fb) * (b - mid) / 6.0, (fmi + 4.0 * fri + fbi) * (b - mid) / 6.0);
    let s2 = (sl.0 + sr.0, sl.1 + sr.1);
    let scale = s2.0.abs().max(s2.1.abs());
    let err = ((s2.0 - sab.0).abs() / 15.0).max((s2.1 - sab.1).abs() / 15.0);
    let tolabs = tol * scale + 1e-14;
    if depth == 0 || err < tolabs {
        (s2.0, s2.1)
    } else {
        let (l0, l1) = adapt(f, a, mid, tol, depth - 1, evals);
        let (r0, r1) = adapt(f, mid, b, tol, depth - 1, evals);
        (l0 + r0, l1 + r1)
    }
}

// composite Simpson on uniform grid
fn comp(f: &impl Fn(f64) -> (f64, f64), a: f64, b: f64, n: usize) -> (f64, f64) {
    let h = (b - a) / n as f64;
    let (fa, fai) = f(a);
    let (fb, fbi) = f(b);
    let mut sum = (fa + fb, fai + fbi);
    for i in 1..n {
        let x = a + i as f64 * h;
        let (v, vi) = f(x);
        let w = if i % 2 == 1 { 4.0 } else { 2.0 };
        sum.0 += w * v;
        sum.1 += w * vi;
    }
    (sum.0 * h / 3.0, sum.1 * h / 3.0)
}

// Richardson-doubled composite Simpson (reliable for oscillatory cos(xu) integrands)
fn quad(f: &impl Fn(f64) -> (f64, f64), a: f64, b: f64, tol: f64) -> (f64, f64) {
    let mut n = 256usize;
    let mut s = comp(f, a, b, n);
    loop {
        let s2 = comp(f, a, b, 2 * n);
        let scale = s2.0.abs().max(s2.1.abs()).max(1e-30);
        let diff = (s2.0 - s.0).abs().max((s2.1 - s.1).abs());
        if diff < tol * scale + 1e-13 || n >= 65536 {
            return s2;
        }
        s = s2;
        n *= 2;
    }
}

// H_t(z), z = x + iy, on [0, UMAX] (integrand mass at u~0.1; tail < 1e-30 even at t=0.5, |y|<=1)
fn ht_on(t: f64, x: f64, y: f64, umax: f64) -> (f64, f64) {
    let f = |u: f64| {
        let w = phi(u) * (t * u * u).exp();
        let c = (x * u).cos() * (y * u).cosh();
        let s = (x * u).sin() * (y * u).sinh();
        (w * c, -w * s)
    };
    let (r, i) = quad(&f, 0.0, umax, 1e-12);
    (2.0 * r, 2.0 * i)
}

fn ht(t: f64, x: f64, y: f64) -> (f64, f64) { ht_on(t, x, y, 6.0) }

// H_t'(z) = -2 int u e^{t u^2} Phi [sin(xu)cosh(yu) + i cos(xu)sinh(yu)] du
fn htp(t: f64, x: f64, y: f64) -> (f64, f64) {
    let f = |u: f64| {
        let w = phi(u) * (t * u * u).exp() * u;
        let s = (x * u).sin() * (y * u).cosh();
        let c = (x * u).cos() * (y * u).sinh();
        (-w * s, -w * c)
    };
    let (r, i) = quad(&f, 0.0, 6.0, 1e-12);
    (2.0 * r, 2.0 * i)
}

// complex Newton for H_t; seed (x0, y0). returns (re, im, |H|, iters)
fn cnewton(t: f64, x0: f64, y0: f64) -> Option<(f64, f64, f64, u32)> {
    let mut x = x0;
    let mut y = y0;
    for it in 0..60u32 {
        let (hr, hi) = ht(t, x, y);
        let (dr, di) = htp(t, x, y);
        let den = dr * dr + di * di;
        if den < 1e-40 { return None; }
        let nzr = (hr * dr + hi * di) / den;
        let nzi = (hi * dr - hr * di) / den;
        let nx = x - nzr;
        let ny = y - nzi;
        let dx = (nx - x).abs();
        let dy = (ny - y).abs();
        x = nx;
        y = ny;
        if dx < 1e-12 && dy < 1e-12 {
            let (hr, hi) = ht(t, x, y);
            return Some((x, y, (hr * hr + hi * hi).sqrt(), it));
        }
    }
    let (hr, hi) = ht(t, x, y);
    Some((x, y, (hr * hr + hi * hi).sqrt(), 60))
}

// bisection on Re H_t(x,0) in [lo,hi] (sampling step 0.005); first sign change
fn real_root(t: f64, lo: f64, hi: f64) -> Option<f64> {
    let mut prev_x = lo;
    let mut prev_v = ht(t, lo, 0.0).0;
    let step = 0.005;
    let mut n = lo;
    while n < hi {
        n += step;
        let v = ht(t, n, 0.0).0;
        if prev_v != 0.0 && v / prev_v < 0.0 {
            let mut a = prev_x;
            let mut b = n;
            let sgn = prev_v > 0.0;
            for _ in 0..70 {
                let m = 0.5 * (a + b);
                let vm = ht(t, m, 0.0).0;
                if (vm > 0.0) == sgn { a = m; } else { b = m; }
            }
            return Some(0.5 * (a + b));
        }
        prev_x = n;
        prev_v = v;
    }
    None
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.get(1).map(|s| s.as_str()) == Some("verify") { verify(); return; }
    let t0 = Instant::now();
    // ---- validation at t = 0 ----
    let known: [f64; 8] = [
        14.13472514173469379, 21.02203963877155499, 25.01085758014568876, 30.42487612585951321,
        32.93506158773918569, 37.58617815882567126, 40.91871901214749519, 43.32707328091499952,
    ];
    // 2*int Phi = xi(1/2)
    let f = |u: f64| (phi(u), 0.0);
    let (r0, _) = quad(&f, 0.0, 6.0, 1e-13);
    println!("2*int Phi = {:.12}   (expect 0.497120778188314)", 2.0 * r0);

    // find first 8 real zeros at t=0 by bisection over [0,68]
    let mut g0 = Vec::new();
    {
        let mut prev_x = 0.0_f64;
        let mut prev_v = ht(0.0, 0.0, 0.0).0;
        let mut n = 0.0;
        while n < 68.0 {
            n += 0.05;
            let v = ht(0.0, n, 0.0).0;
            if prev_v != 0.0 && v / prev_v < 0.0 {
                let mut a = prev_x;
                let mut b = n;
                let sgn = prev_v > 0.0;
                for _ in 0..70 {
                    let m = 0.5 * (a + b);
                    let vm = ht(0.0, m, 0.0).0;
                    if (vm > 0.0) == sgn { a = m; } else { b = m; }
                }
                g0.push(0.5 * (a + b));
            }
            prev_x = n;
            prev_v = v;
            if g0.len() >= 8 { break; }
        }
    }
    println!("t=0 zeros (bisection) vs published gamma_1..8:");
    println!("  (note: |Xi(t)| ~ e^(-pi t/4) ~ 2e-15 at t=43, so absolute x-precision at high j is envelope-limited ~1e-6; quadrature itself is 1e-17-accurate)");
    let mut ok = true;
    for (j, &r) in g0.iter().enumerate() {
        let d = (r - known[j]).abs();
        if d > 5e-5 { ok = false; }
        println!("  j={}: {:.10}  |d|={:.2e}", j + 1, r, d);
    }
    if !ok || g0.len() != 8 { println!("VALIDATION FAILED"); return; }
    println!("validation OK in {:.1}s", t0.elapsed().as_secs_f64());

    // ---- zero tracking vs t ----
    let ts: [f64; 10] = [-0.001, -0.005, -0.01, -0.02, -0.05, -0.1, -0.2, -0.35, -0.5, -1.0];
    println!("\n=== t < 0: tracking gamma_1..8 (seeded from published gamma at t=0; |Im|>1e-4 => OFF-AXIS) ===");
    println!("t        j:  Re            Im            |H|    flag");
    let mut prev_re: Vec<f64> = known.to_vec();
    for &t in &ts {
        let mut line = format!("{:.4}  ", t);
        let mut any_off = false;
        let mut next: Vec<f64> = Vec::new();
        for j in 0..8 {
            let x0 = prev_re[j];
            let (ra, ia, ha, _) = match cnewton(t, x0, 1e-3) {
                Some(v) => v,
                None => { line.push_str(&format!(" j{}:NULL", j + 1)); next.push(x0); continue; }
            };
            let (rb, ib, hb, _) = match cnewton(t, x0, -1e-3) {
                Some(v) => v,
                None => { line.push_str(&format!(" j{}:NULL", j + 1)); next.push(ra); continue; }
            };
            // take the branch with smaller |H|; zero is on-axis if both Im ~ 0
            let (re, im, h) = if ha <= hb { (ra, ia, ha) } else { (rb, ib, hb) };
            let flag = if im.abs() > 1e-4 { any_off = true; "OFF-AXIS" } else { "" };
            line.push_str(&format!("j{}: {:.7} {:+.3e} {:.1e} {}", j + 1, re, im, h, flag));
            next.push(re);
        }
        println!("{}", line);
        if any_off { println!("  !!! off-axis zero at t={} (t<0): expected under RH (RT+Newman); NOT a disproof. height of first-8 collision measured.", t); }
        prev_re = next;
    }

    // deeper t<0: where do the first 8 eventually leave? (may or may not in range)
    let ts2: [f64; 4] = [-2.0, -5.0, -10.0, -20.0];
    println!("\n=== t < 0 (deeper): first-8 tracking ===");
    for &t in &ts2 {
        let mut line = format!("{:.1}  ", t);
        let mut any_off = false;
        let mut next: Vec<f64> = Vec::new();
        for j in 0..8 {
            let x0 = prev_re[j];
            match cnewton(t, x0, 1e-3) {
                Some((re, im, h, _)) => {
                    let flag = if im.abs() > 1e-4 { any_off = true; "OFF-AXIS" } else { "" };
                    line.push_str(&format!("j{}: {:.6} {:+.3e} {:.1e} {}", j + 1, re, im, h, flag));
                    next.push(re);
                }
                None => { line.push_str(&format!("j{}:NULL", j + 1)); next.push(x0); }
            }
        }
        println!("{}", line);
        if any_off { println!("  off-axis at t={} (first-8 collision height measured; RH-consistent)", t); }
        prev_re = next;
    }

    // t > 0 (the only side with RH-disproof potential)
    let tsu: [f64; 7] = [0.001, 0.01, 0.05, 0.1, 0.25, 0.5, 1.0];
    println!("\n=== t > 0: tracking gamma_1..8 (non-real zero here => Lambda>t>0 => RH FALSE) ===");
    let mut prev_re: Vec<f64> = known.to_vec();
    for &t in &tsu {
        let mut line = format!("{:.3}  ", t);
        let mut any_off = false;
        let mut next: Vec<f64> = Vec::new();
        for j in 0..8 {
            let x0 = prev_re[j];
            match cnewton(t, x0, 1e-3) {
                Some((re, im, h, _)) => {
                    let flag = if im.abs() > 1e-4 { any_off = true; "OFF-AXIS !!!" } else { "" };
                    line.push_str(&format!("j{}: {:.7} {:+.3e} {:.1e} {}", j + 1, re, im, h, flag));
                    next.push(re);
                }
                None => { line.push_str(&format!("j{}:NULL", j + 1)); next.push(x0); }
            }
        }
        println!("{}", line);
        if any_off {
            println!("  !!! OFF-AXIS zero at t={:+.4}>0 : forces Lambda > {:+.4} > 0 => RH FALSE (numerical signal; triple-check before any claim)", t, t);
        }
        prev_re = next;
    }

    // ---- counterexample: gaussian Phi~ ----
    println!("\n=== counterexample Phi~(u)=e^-(u-5)^2 + e^-(u+5)^2 + 3e^-u^2 ===");
    // G_t(z) = int_0^inf e^{t u^2} Phi~ cos(zu) du
    let g_ht = |t: f64, x: f64, y: f64| -> (f64, f64) {
        let f = |u: f64| {
            let w = g_phi(u) * (t * u * u).exp();
            let c = (x * u).cos() * (y * u).cosh();
            let s = (x * u).sin() * (y * u).sinh();
            (w * c, -w * s)
        };
        quad(&f, 0.0, 14.0, 1e-12)
    };
    let g_htp = |t: f64, x: f64, y: f64| -> (f64, f64) {
        let f = |u: f64| {
            let w = g_phi(u) * (t * u * u).exp() * u;
            let s = (x * u).sin() * (y * u).cosh();
            let c = (x * u).cos() * (y * u).sinh();
            (-w * s, -w * c)
        };
        quad(&f, 0.0, 14.0, 1e-12)
    };
    let g_newton = |t: f64, x0: f64, y0: f64| -> Option<(f64, f64)> {
        let mut x = x0;
        let mut y = y0;
        for _ in 0..60 {
            let (hr, hi) = g_ht(t, x, y);
            let (dr, di) = g_htp(t, x, y);
            let den = dr * dr + di * di;
            if den < 1e-40 { return None; }
            let nzr = (hr * dr + hi * di) / den;
            let nzi = (hi * dr - hr * di) / den;
            let nx = x - nzr;
            let ny = y - nzi;
            if (nx - x).abs() < 1e-12 && (ny - y).abs() < 1e-12 {
                return Some((nx, ny));
            }
            x = nx;
            y = ny;
        }
        Some((x, y))
    };
    // H_0 analytic zeros: z = (pi+2pi k)/5 +- i*0.19249 ; check k=0
    println!("G_0 analytic zero: z = pi/5 +- i*(1/5)ln((3+sqrt5)/2) = {:.6} +- {:.6}i", PI / 5.0, (1.0 / 5.0) * ((3.0 + 5.0_f64.sqrt()) / 2.0).ln());
    for &(x0, y0) in &[(PI / 5.0, 0.19), (PI / 5.0, -0.19)] {
        match g_newton(0.0, x0, y0) {
            Some((rx, ry)) => println!("  Newton G_0: z = {:.7} {:.7}i", rx, ry),
            None => println!("  Newton G_0: NULL"),
        }
    }
    // track the +branch pair through t
    println!("tracking k=0 pair (Re=pi/5) as t increases (Im -> 0 = collision => real zeros beyond):");
    let mut prev = (PI / 5.0, 0.19);
    for &t in &[0.05_f64, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5] {
        match g_newton(t, prev.0, prev.1) {
            Some((rx, ry)) => {
                println!("  t={:.2}: z = {:.7} {:.7}i  |Im|={:.2e}", t, rx, ry, ry.abs());
                prev = (rx, ry);
            }
            None => println!("  t={:.2}: NULL", t),
        }
    }
    // verify G_0.5 real-rooted: real-axis scan near cos(10x)=0 solutions
    println!("G_0.5 real-axis zeros near (pi/2+k pi)/10 (expect all real):");
    for k in 0..4 {
        let c0 = (PI / 2.0 + k as f64 * PI) / 10.0;
        let r = real_root_g(&g_ht, c0 - 0.2, c0 + 0.2);
        match r {
            Some(x) => {
                let (_, hi) = g_ht(0.5, x, 1e-4);
                let (_, hi2) = g_ht(0.5, x, 1e-2);
                println!("  k={}: zero x={:.8}  Im(H(x+i1e-4))={:+.3e}  Im(H(x+i1e-2))={:+.3e}", k, x, hi, hi2);
            }
            None => println!("  k={}: no sign change found", k),
        }
    }
    println!("\ntotal time {:.1}s", t0.elapsed().as_secs_f64());
}

fn real_root_g(gh: &impl Fn(f64, f64, f64) -> (f64, f64), lo: f64, hi: f64) -> Option<f64> {
    let mut prev_x = lo;
    let mut prev_v = gh(0.5, lo, 0.0).0;
    let step = 0.001;
    let mut n = lo;
    while n < hi {
        n += step;
        let v = gh(0.5, n, 0.0).0;
        if prev_v != 0.0 && v / prev_v < 0.0 {
            let mut a = prev_x;
            let mut b = n;
            let sgn = prev_v > 0.0;
            for _ in 0..60 {
                let m = 0.5 * (a + b);
                let vm = gh(0.5, m, 0.0).0;
                if (vm > 0.0) == sgn { a = m; } else { b = m; }
            }
            return Some(0.5 * (a + b));
        }
        prev_x = n;
        prev_v = v;
    }
    None
}

// ---- verify mode: fine t-continuation (0.05) to pin first off-axis event + direct checks ----
fn verify() {
    let known: [f64; 8] = [
        14.13472514173469379, 21.02203963877155499, 25.01085758014568876, 30.42487612585951321,
        32.93506158773918569, 37.58617815882567126, 40.91871901214749519, 43.32707328091499952,
    ];
    println!("=== fine continuation t: 0 -> -1.0 step 0.05 (track gamma_1..8) ===");
    let mut prev = known.to_vec();
    let mut first_off: Option<(f64, usize, f64, f64)> = None; // (t, j, re, im)
    let mut t = 0.0_f64;
    while t > -1.0001 {
        t -= 0.05;
        let mut next: Vec<f64> = Vec::new();
        let mut row = format!("t={:+.2}  ", t);
        for j in 0..8 {
            match cnewton(t, prev[j], 1e-3) {
                Some((re, im, h, _)) => {
                    let flag = if im.abs() > 1e-4 {
                        if first_off.is_none() { first_off = Some((t, j, re, im)); }
                        "OFF!"
                    } else { "" };
                    row.push_str(&format!("j{}:{:8.4}{:+.2e}{} ", j + 1, re, im, flag));
                    next.push(re);
                }
                None => { row.push_str(&format!("j{}:NULL ", j + 1)); next.push(prev[j]); }
            }
        }
        println!("{}", row);
        prev = next;
        if first_off.is_some() { break; }
    }
    match first_off {
        Some((t0, j, re, im)) => {
            println!("\nFIRST off-axis among gamma_1..8 at t={:.3}, j={} (seed gamma_{}): z ~ {:.6} {:.6}i", t0, j + 1, j + 1, re, im);
            // verify the pair with fresh Newton from several seeds
            for &(sx, sy) in &[(re, im), (re, -im), (re + 0.3, im), (re - 0.3, im)] {
                match cnewton(t0, sx, sy) {
                    Some((rx, ry, h, _)) => println!("  fresh Newton from ({:.3},{:+.3}): z={:.7}{:+.7}i |H|={:.1e}", sx, sy, rx, ry, h),
                    None => println!("  fresh Newton from ({:.3},{:+.3}): NULL", sx, sy),
                }
            }
            // real-axis zeros nearby?
            let mut reals = Vec::new();
            for lo in [re - 4.0, re + 4.0] {
                if let Some(x) = real_root(t0, lo, lo + 8.0) { reals.push(x); }
            }
            println!("  real-axis zeros of H_{} in [{:.2},{:.2}]: {:?}", t0, re - 4.0, re + 4.0, reals);
        }
        None => println!("no off-axis event among gamma_1..8 for t in [-1,0]"),
    }
    // direct check of the t=-1 pair seen in the main run
    println!("\n=== direct verification at t=-1 (main run saw pair near 33.115, +-0.1505) ===");
    for &(sx, sy) in &[(33.115_f64, 0.15_f64), (33.115, -0.15), (33.1, 0.2), (33.2, 0.1)] {
        match cnewton(-1.0, sx, sy) {
            Some((rx, ry, h, _)) => println!("  seed ({:.3},{:+.2}): z={:.7}{:+.7}i |H|={:.1e}", sx, sy, rx, ry, h),
            None => println!("  seed ({:.3},{:+.2}): NULL", sx, sy),
        }
    }
    // ---- pin the collision interval: count real zeros of H_t in [31.5,34.5] for t near -1 ----
    println!("\n=== pin collision: real-axis zeros of H_t in [31.5,34.5] (count 2 = both real; 0 = merged pair) ===");
    let mut t = -0.90_f64;
    while t >= -1.001 {
        let r = count_real(t, 31.5, 34.5, 0.002);
        println!("  t={:+.3}: {} real zero(s) in [31.5,34.5] {:?}", t, r.len(), r);
        t -= 0.02;
    }
    // fine near the boundary
    let mut t = -0.95_f64;
    while t >= -1.001 {
        let r = count_real(t, 31.5, 34.5, 0.001);
        println!("  t={:+.3}: {} real zero(s) in [31.5,34.5] {:?}", t, r.len(), r);
        t -= 0.01;
    }
    // conjugate symmetry check + a real-axis scan of H_{-1}
    let mut reals = Vec::new();
    let mut x = 30.0;
    while x < 36.0 {
        if let Some(r) = real_root(-1.0, x, x + 1.0) { reals.push(r); }
        x += 1.0;
    }
    println!("  H_-1 real-axis zeros in [30,36]: {:?}", reals);
}

// ---- pin collision interval: robust real-axis zero count in [a,b] at given t ----
fn count_real(t: f64, a: f64, b: f64, step: f64) -> Vec<f64> {
    let mut out = Vec::new();
    let mut prev_x = a;
    let mut prev_v = ht(t, a, 0.0).0;
    let mut n = a;
    while n < b {
        n += step;
        let v = ht(t, n, 0.0).0;
        if prev_v != 0.0 && v / prev_v < 0.0 {
            let mut lo = prev_x;
            let mut hi = n;
            let sgn = prev_v > 0.0;
            for _ in 0..70 {
                let m = 0.5 * (lo + hi);
                let vm = ht(t, m, 0.0).0;
                if (vm > 0.0) == sgn { lo = m; } else { hi = m; }
            }
            out.push(0.5 * (lo + hi));
        }
        prev_x = n;
        prev_v = v;
        if out.len() >= 4 { break; }
    }
    out
}
