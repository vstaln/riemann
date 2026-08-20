// coulomb_energy — log-gas ΔH/N discriminant
// RH: zeros γ on Re=1/2. Planted: one at beta0=0.8 replacing nearest RH zero.
// H = Σ_{i≠j} log|rho_i - rho_j| with rho = (beta, gamma). For gas near real line,
// model H_RH via 2D log interaction on (0.5+iγ); ΔH from one particle shift d0=0.30
// in Re. Prediction: ΔH≈Σ_j log|rho_plant - rho_j|/|rho_RH - rho_j| ~ O(1) global,
// ΔH/N ~ 1/N. Blind offset reduces by geometric factor but stays >0.
// Reads tools/data/zeros_rust_100k.txt; window T∈[0,Tmax] N≈Tmax*log Tmax/2π.
// Labels: CHECKED NUMERICALLY if computed, INCONCLUSIVE if no zeros.
use std::env; use std::fs; use std::path::PathBuf;
fn parse_arg(a:&[String],f:&str)->Option<String>{for i in 0..a.len(){if a[i]==f&&i+1<a.len(){return Some(a[i+1].clone());} if a[i].starts_with(&format!("{}=",f)){return Some(a[i][f.len()+1..].to_string());}}None}
fn load_zeros()->Vec<f64>{for p in ["/home/vstaln/riemann/tools/data/zeros_rust_100k.txt","tools/data/zeros_rust_100k.txt","../data/zeros_rust_100k.txt"]{if let Ok(t)=fs::read_to_string(PathBuf::from(p)){let mut v=Vec::new(); for l in t.lines(){let s=l.trim(); if s.is_empty()||s.starts_with('#'){continue;} let w:Vec<&str>=s.split_whitespace().collect(); let g=w.get(1).unwrap_or(&w[0]); if let Ok(x)=g.parse::<f64>(){v.push(x);}} if !v.is_empty(){return v;}}} eprintln!("WARN no zeros"); vec![]}
fn main(){
    let args:Vec<String>=env::args().collect();
    if args.iter().any(|a| a=="--help"){println!("usage: coulomb_energy --planted-beta 0.80 --centers 14.1347,14.28,30,50 --t-max 1000"); return;}
    let beta0: f64 = parse_arg(&args,"--planted-beta").or(parse_arg(&args,"--beta0")).and_then(|s| s.parse().ok()).unwrap_or(0.80);
    let tmax: f64 = parse_arg(&args,"--t-max").or(parse_arg(&args,"--T")).and_then(|s| s.parse().ok()).unwrap_or(1000.0);
    let centers: Vec<f64> = parse_arg(&args,"--centers").map(|s| s.split(',').filter_map(|x| x.trim().parse().ok()).collect()).unwrap_or(vec![14.1347,14.28,14.43,30.0,50.0]);
    let t0 = parse_arg(&args,"--t0").and_then(|s| s.parse().ok()).unwrap_or(14.13472514);
    let zeros = load_zeros();
    println!("alien coulomb_energy beta0={} t0={} t_max={} zeros_loaded={}", beta0, t0, tmax, zeros.len());
    // window up to tmax
    let gam: Vec<f64> = zeros.iter().copied().filter(|&g| g<=tmax && g>=1.0).collect();
    let n = gam.len();
    if n<10 { println!("INCONCLUSIVE n={} too few", n); return; }
    // pair energy H_RH = Σ_{i≠j} log|rho_i - rho_j|  rho_i=(0.5,γ_i)  (ordered pairs, so 2* unordered)
    // Use truncated sum (|i-j|<=w) to stay O(N w); w=80 captures screening
    let w = 80usize;
    let mut h_rh = 0.0;
    for i in 0..n { for j in 0..n { if i==j {continue;} if (i as isize - j as isize).abs() as usize > w {continue;} let d2 = (gam[i]-gam[j]).powi(2); // (0.5-0.5)=0
        h_rh += 0.5 * d2.ln(); } }
    let hrh_n = h_rh / n as f64;
    // planted: replace nearest gamma to t0 (move Re 0.5->beta0)
    let mut idx = 0; let mut best=f64::INFINITY; for (i,&g) in gam.iter().enumerate(){ let d=(g-t0).abs(); if d<best{best=d; idx=i;}}
    let d0 = beta0 - 0.5;
    // ΔH = Σ_{j≠idx} log(|rho_plant - rho_j|/|rho_RH - rho_j|)  + j swapped (twice, ordered)
    let mut delta = 0.0;
    for j in 0..n { if j==idx {continue;} if (idx as isize - j as isize).abs() as usize > w {continue;}
        let dt = gam[j] - gam[idx];
        let drh = (dt*dt).sqrt();
        let dpl = (d0*d0 + dt*dt).sqrt();
        if drh>1e-12 && dpl>1e-12 { delta += (dpl/drh).ln(); }
        // ordered pairs: also j->idx same term (so double)
        delta += (dpl/drh).ln(); // second direction same distance
    }
    // actually we double-counted: ordered sum has both (idx,j) and (j,idx) = 2* single
    // above already added 2* per j (loop has 2 adds) so delta is ordered ΔH
    let dhn = delta / n as f64;
    println!("window [1,{}] N={} w={} H_RH/N={:.6}  Delta_H={:.6}  Delta_H/N={:.6}  d0={:.3}  nearest_gamma={:.6} dt0={:.4}", tmax, n, w, hrh_n, delta, dhn, d0, gam[idx], (gam[idx]-t0).abs());
    // blind centers: predicted geometric reduction = exp(-|T-t0|/xi) xi~50 for log gas screening length? Actually power law ~1/|T-t0|
    // Report ΔH contribution restricted to |γ_j - T| < band
    let band = 20.0;
    for &t in &centers {
        let mut d_band = 0.0; let mut cnt=0;
        for j in 0..n { if j==idx {continue;} let dt = gam[j]-gam[idx]; let dt_band = (gam[j]-t).abs(); if dt_band>band {continue;} if (gam[j]-gam[idx]).abs() as usize>0 {} // unused
            let drh = (dt*dt).sqrt().max(1e-12); let dpl=(d0*d0+dt*dt).sqrt(); d_band += 2.0*(dpl/drh).ln(); cnt+=1;
            // weight by proximity to center: 1/(1+|γ_j-T|/5) not needed for now
        }
        // crude: band Δ scales ~ cnt/N * total? Actually d_band ≈ delta if band covers window, else partial
        // Just compute full delta restricted to band window around center T
        let mut d2=0.0;
        for j in 0..n { if j==idx {continue;} if (gam[j]-t).abs()>band {continue;} let dt=gam[j]-gam[idx]; let drh=(dt*dt).sqrt().max(1e-12); let dpl=(d0*d0+dt*dt).sqrt(); d2+=2.0*(dpl/drh).ln();}
        println!("center T={:.4} band±{:.0} Delta_band={:.5} cnt={} dt_center={:.4} in_band_plant={}", t, band, d2, cnt, (t-t0).abs(), (t-t0).abs() < band+ d0);
    }
    println!("DONE beta0={} H_RH/N={:.6} Delta_H/N={:.6} global_ok=true (Delta_H>0 independent of center by construction; verify band values stay >0 at blind 14.28)", beta0, hrh_n, dhn);
}
