// Wave RH-5E: bounded scan of the Uniform Hadamard Deficit Conjecture.
use std::{f64::consts::PI, fs, process::Command};
type C = (f64, f64);
const SIGMAS: [f64; 9] = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45];
const M: usize = 24;
fn add(a:C,b:C)->C{(a.0+b.0,a.1+b.1)}
fn sub(a:C,b:C)->C{(a.0-b.0,a.1-b.1)}
fn mul(a:C,b:C)->C{(a.0*b.0-a.1*b.1,a.0*b.1+a.1*b.0)}
fn div(a:C,b:C)->C{let d=b.0*b.0+b.1*b.1;((a.0*b.0+a.1*b.1)/d,(a.1*b.0-a.0*b.1)/d)}
fn abs(a:C)->f64{a.0.hypot(a.1)}
fn scale(a:C,x:f64)->C{(a.0*x,a.1*x)}
fn inv(a:C)->C{div((1.0,0.0),a)}
fn pow_x(s:C,x:f64)->C{let l=x.ln();let(sn,co)=(s.1*l).sin_cos();let r=(-s.0*l).exp();(r*co,-r*sn)}
fn coeffs() -> [f64; M] {
    let mut c = [0.0; M];
    c[..10].copy_from_slice(&[8.333333333333333e-2,-1.388888888888889e-3,
        3.306878306878307e-5,-8.267195767195768e-7,2.087675698786810e-8,
        -5.284190138687493e-10,1.338253653068468e-11,-3.389680318224120e-13,
        8.586069205618e-15,-2.175643985292551e-16]);
    for m in 11..=M {
        let p = (2 * m) as i32;
        let z2: f64 = (1..=16).map(|k| (k as f64).powi(-p)).sum();
        c[m - 1] = if m % 2 == 1 { 1.0 } else { -1.0 } * 2.0 * z2 / (2.0 * PI).powi(p);
    }
    c
}
// EM continuation; remainder uses |B_2M({x})| <= 2(2M)!zeta(2M)/(2pi)^(2M).
fn finish(s:C,n:usize,mut z:C,mut zp:C,mut az:f64,mut ap:f64,bc:&[f64;M])->(C,C,f64,f64){
    let x = n as f64 + 1.0;
    let l = x.ln();
    let w = pow_x(s, x);
    let sm1 = sub(s, (1.0, 0.0));
    let tail = div(scale(w, x), sm1);
    let dtail = mul(
        scale(w, x),
        sub(div((-l, 0.0), sm1), div((1.0, 0.0), mul(sm1, sm1))),
    );
    z = add(add(z, tail), scale(w, 0.5));
    zp = add(add(zp, dtail), scale(w, -0.5 * l));
    az += abs(tail) + 0.5 * abs(w);
    ap += abs(dtail) + 0.5 * l * abs(w);
    let (mut p, mut hs, mut deg) = ((1.0, 0.0), (0.0, 0.0), 0usize);
    for m in 1..=M {
        let k = 2 * m - 1;
        while deg < k {
            let q = add(s, (deg as f64, 0.0));
            p = mul(p, q);
            hs = add(hs, inv(q));
            deg += 1;
        }
        let wk = scale(w, x.powi(-(k as i32)));
        let term = scale(mul(p, wk), bc[m - 1]);
        let dterm = mul(term, sub(hs, (l, 0.0)));
        z = add(z, term);
        zp = add(zp, dterm);
        az += abs(term);
        ap += abs(dterm);
    }
    let q = add(s, (deg as f64, 0.0));
    p = mul(p, q);
    hs = add(hs, inv(q));
    let a = s.0 + 2.0 * M as f64 - 1.0;
    let base = bc[M - 1].abs() * abs(p) * x.powf(-a);
    let rz = base / a;
    let rzp = base * (abs(hs) / a + l / a + 1.0 / (a * a));
    let round = 128.0 * f64::EPSILON * (n + 2 * M + 8) as f64;
    (z, zp, rz + round * az + 1e-14, rzp + round * ap + 1e-14)
}
fn point(s: C, n: usize, bc: &[f64; M]) -> (C, C, f64, f64) {
    let (mut z, mut zp, mut az, mut ap) = ((0.0, 0.0), (0.0, 0.0), 0.0, 0.0);
    for k in 1..=n {
        let l = (k as f64).ln();
        let w = pow_x(s, k as f64);
        z = add(z, w);
        zp = add(zp, scale(w, -l));
        az += abs(w);
        ap += l * abs(w);
    }
    finish(s, n, z, zp, az, ap, bc)
}

fn nearest(zeros: &[f64], sigma: f64, t: f64) -> (f64, f64) {
    let i = zeros.partition_point(|&g| g < t);
    let mut g = zeros[i.min(zeros.len() - 1)];
    if i > 0 && (zeros[i - 1] - t).abs() < (g - t).abs() {
        g = zeros[i - 1];
    }
    (((0.5 - sigma).powi(2) + (g - t).powi(2)).sqrt(), g)
}

fn main() {
    let bc = coeffs();
    let (z2, _, e2, _) = point((2.0, 0.0), 64, &bc);
    let self_err=(z2.0-PI*PI/6.0).abs();
    let (z1,p1,e1,f1)=point((0.05,16.0),64,&bc);
    let (z2x,p2,e2x,f2)=point((0.05,16.0),128,&bc);
    let cross=abs(sub(div(p1,z1),div(p2,z2x)));
    let cross_bound=f1/(abs(z1)-e1)+abs(p1)*e1/(abs(z1)*(abs(z1)-e1))+f2/(abs(z2x)-e2x)+abs(p2)*e2x/(abs(z2x)*(abs(z2x)-e2x));
    println!("uhdc_scan EM_M={} selfcheck_zeta2_abs={:.3e} bound={:.3e} cross_N64_N128={:.3e} combined_bound={:.3e}",M,self_err,e2,cross,cross_bound);
    assert!(self_err<=e2 && z2.1.abs()<=e2 && cross<=cross_bound);
    let path = format!("{}/../data/zeros_rust_100k.txt", env!("CARGO_MANIFEST_DIR"));
    let text = fs::read_to_string(path).expect("zero data");
    let zeros: Vec<f64> = text
        .lines()
        .filter(|l| l.as_bytes().first().is_some_and(u8::is_ascii_digit))
        .filter_map(|l| l.split_whitespace().nth(1)?.parse().ok())
        .collect();
    let tmax = 17200.0f64.min(*zeros.last().expect("zeros")); // QUARANTINE: old file untrusted above gamma~17255 (commit fd74184)
    let (mut included, mut excluded, mut violations, mut uncertain) =
        (0usize, 0usize, 0usize, 0usize);
    let (mut minq, mut mine, mut mins, mut mint, mut mind, mut ming) =
        (f64::INFINITY, 0.0, 0.0, 0.0, 0.0, 0.0);
    let (mut vals, mut first_bad) = (Vec::new(), None::<(f64, f64, f64, f64, f64)>);
    let mut t = 14.0;
    while t <= tmax {
        let n = (0.30 * t).ceil().max(64.0) as usize;
        let (mut zs, mut zps, mut azs, mut aps) =
            ([(0.0, 0.0); 9], [(0.0, 0.0); 9], [0.0; 9], [0.0; 9]);
        for k in 1..=n {
            let l = (k as f64).ln();
            let (sn, co) = (t * l).sin_cos();
            let r = (-0.05 * l).exp();
            let mut amp = r;
            for j in 0..9 {
                let w = (amp * co, -amp * sn);
                zs[j] = add(zs[j], w);
                zps[j] = add(zps[j], scale(w, -l));
                azs[j] += amp;
                aps[j] += l * amp;
                amp *= r;
            }
        }
        for j in 0..9 {
            let sg = SIGMAS[j];
            let (d, g) = nearest(&zeros, sg, t);
            if d < 3.0 / t.ln() {
                excluded += 1;
                continue;
            }
            let (z, zp, ez, ep) = finish((sg, t), n, zs[j], zps[j], azs[j], aps[j], &bc);
            let zm = abs(z);
            included += 1;
            if zm <= ez {
                uncertain += 1;
                continue;
            }
            let q = div(zp, z);
            let qe = ep / (zm - ez) + abs(zp) * ez / (zm * (zm - ez));
            let centered = q.0 - 0.5 * (t / (2.0 * PI)).ln();
            vals.push(centered);
            if q.0 < minq {
                (minq, mine, mins, mint, mind, ming) = (q.0, qe, sg, t, d, g);
            }
            if q.0 + qe < 0.0 {
                violations += 1;
                if first_bad.is_none() {
                    first_bad = Some((sg, t, q.0, qe, d));
                }
            } else if q.0 - qe <= 0.0 {
                uncertain += 1;
            }
        }
        t += 2.0;
    }
    let mean = vals.iter().sum::<f64>() / vals.len() as f64;
    let lo = vals.iter().copied().fold(f64::INFINITY, f64::min);
    let hi = vals.iter().copied().fold(f64::NEG_INFINITY, f64::max);
    let third = vals.len() / 3;
    let m1 = vals[..third].iter().sum::<f64>() / third as f64;
    let m3 = vals[2 * third..].iter().sum::<f64>() / (vals.len() - 2 * third) as f64;
    let mut hist = [0usize; 10];
    for &v in &vals {
        let b = if hi == lo {
            0
        } else {
            (((v - lo) / (hi - lo) * 10.0) as usize).min(9)
        };
        hist[b] += 1;
    }
    println!(
        "grid sigma=0.05..0.45 step=.05 t=14..{:.0} step=2 included={} excluded={}",
        tmax, included, excluded
    );
    println!("minimum Re(zeta'/zeta)={:.12e} +/- {:.3e} at s={:.2}+{:.1}i nearest_zero={:.12} distance={:.6}",minq,mine,mins,mint,ming,mind);
    println!("centered=Re(zeta'/zeta)-0.5log(t/2pi): min={:.6} max={:.6} mean={:.6} first_third_mean={:.6} last_third_mean={:.6}",lo,hi,mean,m1,m3);
    for b in 0..10 {
        println!(
            "hist[{:2}] [{:+.6},{:+.6}) = {}",
            b,
            lo + (hi - lo) * b as f64 / 10.0,
            lo + (hi - lo) * (b + 1) as f64 / 10.0,
            hist[b]
        );
    }
    println!("violations={} uncertain={}", violations, uncertain);
    if let Some((sg, tt, q, e, d)) = first_bad {
        let code = format!(
            "import mpmath as m;m.mp.dps=40;s=m.mpc({},{});print(m.re(m.diff(m.zeta,s)/m.zeta(s)))",
            sg, tt
        );
        let check = Command::new("python3")
            .args(["-c", &code])
            .output()
            .ok().filter(|o|o.status.success()&&!o.stdout.is_empty())
            .map(|o|String::from_utf8_lossy(&o.stdout).trim().to_string())
            .unwrap_or_else(||"MANUAL RECHECK REQUIRED".into());
        println!(
            "first_violation s={:.2}+{:.1}i value={:.12e} bound={:.3e} distance={:.6} mpmath40={}",
            sg, tt, q, e, d, check
        );
        println!("VERDICT: FAIL — UHDC refuted on scanned grid [CHECKED NUMERICALLY]");
    } else if uncertain == 0 {
        println!("VERDICT: PASS — UHDC holds on scanned grid [CHECKED NUMERICALLY]");
    } else {
        println!(
            "VERDICT: INCONCLUSIVE — no certified violation but {} unresolved points",
            uncertain
        );
    }
}
