// Independent hostile-referee check for claim 456a3a85. std only, no deps.
// (a) exact small-k closed-form t_k for k^{-a} and (k+1)^{-a} (direct evaluation, no formula shortcut)
// (b) winding of Li_a at r = 0.5,0.9,0.99,0.999 (independent polylog + angle sum; probe grid stops at 0.97)
// (c) moment-based t_k*k for the real Xi at k=1000,1e4,1e5 (plain fine-grid Simpson + brute-force saddle, no Newton/adaptive)
use std::f64::consts::PI;

fn log_phi(u: f64) -> f64 {
    // independent-ish: plain logaddexp, no max-shift trick, 80 terms, hard cutoff
    let e2u = (2.0*u).exp();
    let em2u = (-2.0*u).exp();
    let mut logsum = f64::NEG_INFINITY;
    for n in 1..=80u32 {
        let nn = n as f64;
        let x = 3.0/(2.0*PI*nn*nn)*em2u;
        let lb = (2.0*PI*PI).ln() + 4.0*nn.ln() + 4.5*u + (-x).ln_1p() - PI*nn*nn*e2u;
        if n==1 { logsum = lb; }
        else {
            let mx = logsum.max(lb);
            logsum = mx + ((logsum-mx).exp() + (lb-mx).exp()).ln();
        }
        if lb < logsum - 60.0 && n > 5 { break; }
    }
    2.0f64.ln() + logsum
}

fn F(u: f64, k: f64) -> f64 { log_phi(u) + 2.0*k*u.ln() }

fn log_moment_indep(k: f64) -> f64 {
    // brute-force saddle on fine grid + parabolic refine; composite Simpson, N=1e6
    let mut best = 0.05f64; let mut bestv = f64::NEG_INFINITY;
    let mut u = 0.02;
    while u <= 12.0 { let v = F(u,k); if v>bestv {bestv=v; best=u;} u += 0.001; }
    // parabolic refine on 3 pts around best
    let h = 0.001;
    let (a,b,c) = (best-h, best, best+h);
    let (fa,fb,fc) = (F(a,k),F(b,k),F(c,k));
    let denom = (fa - 2.0*fb + fc);
    let u0 = if denom.abs() > 1e-18 { b - 0.5*h*(fc-fa)/denom } else { b };
    // sigma from second difference
    let s2 = (F(u0+h,k) - 2.0*F(u0,k) + F(u0-h,k))/(h*h);
    let sigma = 1.0/(-s2).max(1e-12).sqrt();
    let f0 = F(u0,k);
    let win = 8.0*sigma;
    let lo = (u0-win).max(0.0);
    let hi = (u0+win).min(12.0);
    let n = 1_000_000usize;
    let w = (hi-lo)/n as f64;
    let g = |u: f64| (F(u,k)-f0).exp();
    let mut s = g(lo)+g(hi);
    for j in 1..n { s += (2.0 + 2.0*(j%2) as f64)*g(lo + w*j as f64); }
    let i = w/3.0*s;
    (2f64).ln() + f0 + i.ln()
}

fn factorial_ratio_log(k: f64) -> f64 {
    let a=2.0*k; let b=2.0*k-1.0; let c=2.0*k+1.0; let d=2.0*k+2.0;
    (a*b/(c*d)).ln()
}

fn polylog(zr: f64, zi: f64, alpha: f64) -> (f64,f64) {
    let mut sr=0.0; let mut si=0.0; let mut pr=1.0; let mut pi=0.0;
    let mut maxm=0.0f64;
    for k in 1..=2_000_000usize {
        let nr = pr*zr - pi*zi; let ni = pr*zi + pi*zr;
        pr=nr; pi=ni;
        let inv = 1.0/(k as f64).powf(alpha);
        let tr = pr*inv; let ti = pi*inv;
        sr+=tr; si+=ti;
        let m = (tr*tr+ti*ti).sqrt();
        if m>maxm {maxm=m;}
        if k>200 && m < 1e-14*maxm { break; }
    }
    (sr,si)
}

fn winding(alpha: f64, r: f64) -> i32 {
    let n = 20000usize;
    let mut total = 0.0f64;
    let (mut pr, mut pi) = polylog(r, 0.0, alpha);
    let mut pa = pi.atan2(pr);
    for j in 1..=n {
        let th = 2.0*PI*j as f64/n as f64;
        let (wr,wi) = polylog(r*th.cos(), r*th.sin(), alpha);
        let wa = wi.atan2(wr);
        let mut d = wa - pa;
        while d > PI { d -= 2.0*PI; }
        while d <= -PI { d += 2.0*PI; }
        total += d;
        pr=wr; pi=wi; pa=wa;
    }
    (total/(2.0*PI)).round() as i32
}

fn main() {
    println!("=== (a) exact closed-form t_k, small k, direct evaluation ===");
    for alpha in [0.5f64, 1.0, 2.0, 3.0] {
        for k in 2..=5usize {
            let kf = k as f64;
            let (a_km, a_k, a_kp) = ((kf-1.0).powf(-alpha), kf.powf(-alpha), (kf+1.0).powf(-alpha));
            let tk = 1.0 - (a_km*a_kp)/(a_k*a_k);
            let asym = -alpha/(kf*kf);
            // (k+1)^{-a}
            let (b_km, b_k, b_kp) = (kf.powf(-alpha), (kf+1.0).powf(-alpha), (kf+2.0).powf(-alpha));
            let tk2 = 1.0 - (b_km*b_kp)/(b_k*b_k);
            println!("a={:.1} k={}: t_k(k^-a)={:.6} (asym {:.4})  t_k((k+1)^-a)={:.6}", alpha,k,tk,asym,tk2);
        }
    }
    // exact rational spot check k=2 a=2: 1-(1*1/9)/(1/16)=1-16/9=-7/9
    println!("exact k=2,a=2: k^-a -> {:.12} (expect -7/9 = {:.12}); (k+1)^-a -> {:.12} (expect -17/64 = {:.12})",
        1.0-(1.0*(1.0/9.0))/(0.25*0.25), -7.0/9.0,
        1.0-((0.25)*(1.0/16.0))/((1.0/9.0)*(1.0/9.0)), -17.0/64.0);

    println!("\n=== (b) independent winding Li_a, r=0.5..0.999 ===");
    for alpha in [0.5f64, 0.6, 1.0, 1.5, 2.0, 2.7, 3.0] {
        let w05 = winding(alpha, 0.5);
        let w09 = winding(alpha, 0.9);
        let w099 = winding(alpha, 0.99);
        let w0999 = winding(alpha, 0.999);
        println!("a={:.1}: w(0.5)={} w(0.9)={} w(0.99)={} w(0.999)={}", alpha,w05,w09,w099,w0999);
    }
    // Li2 explicit: Li2(-1)=-pi^2/12, Li2(1)=pi^2/6
    let (r1,i1)=polylog(-1.0,0.0,2.0);
    let (r2,i2)=polylog(1.0,0.0,2.0);
    println!("Li2(-1)=({:.9},{:.9}) expect (-{:.9},0); Li2(1)=({:.9},{:.9}) expect ({:.9},0)", r1,i1, PI*PI/12.0, r2,i2, PI*PI/6.0);

    println!("\n=== (c) independent moment t_k*k, real Xi ===");
    let m0 = log_moment_indep(0.0);
    println!("log M_0 = {:.12} (expect ln xi(1/2) = {:.12})", m0, 0.497120778188314f64.ln());
    for &k in &[1000usize, 10000, 100000] {
        let kf = k as f64;
        let (mkm, mk, mkp) = (log_moment_indep(kf-1.0), log_moment_indep(kf), log_moment_indep(kf+1.0));
        let mb = 2.0*mk - mkm - mkp;
        let d = mb - factorial_ratio_log(kf);
        let t = 1.0 - (-d).exp();
        let l = kf.ln();
        println!("k={}: k*t_k = {:.6}   (2-k*t_k)*ln k = {:.4}   D_k = {:.3e}", k, kf*t, (2.0-kf*t)*l, d);
    }
}
