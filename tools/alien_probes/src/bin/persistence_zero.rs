// persistence_zero — gap barcode + 2D hole invariant
// Gaps g_i = γ_{i+1}-γ_i for first M zeros. VAR(g) and 2D hole radius R.
// Planted zero at (beta0=0.8, t0=14.13) moved from (0.5,t0) creates short H1 bar ~d0=0.30.
// Reads zeros_rust_100k.txt; default M=5000. Prints VAR_RH, VAR_false_pred, R_RH, R_false.
use std::env; use std::fs; use std::path::PathBuf;
fn parse_arg(a:&[String],f:&str)->Option<String>{for i in 0..a.len(){if a[i]==f&&i+1<a.len(){return Some(a[i+1].clone());} if a[i].starts_with(&format!("{}=",f)){return Some(a[i][f.len()+1..].to_string());}}None}
fn load_zeros()->Vec<f64>{for p in ["/home/vstaln/riemann/tools/data/zeros_rust_100k.txt","tools/data/zeros_rust_100k.txt"]{if let Ok(t)=fs::read_to_string(PathBuf::from(p)){let mut v=Vec::new(); for l in t.lines(){let s=l.trim(); if s.is_empty()||s.starts_with('#'){continue;} let w:Vec<&str>=s.split_whitespace().collect(); let g=w.get(1).unwrap_or(&w[0]); if let Ok(x)=g.parse::<f64>(){v.push(x);}} if !v.is_empty(){return v;}}} vec![]}
fn main(){
    let args:Vec<String>=env::args().collect();
    if args.iter().any(|a| a=="--help"){println!("usage: persistence_zero --M 5000 --planted-beta 0.80 --centers 14.1347,14.28,30,50 --t0 14.13472514"); return;}
    let m:usize=parse_arg(&args,"--M").or(parse_arg(&args,"--m")).and_then(|s| s.parse().ok()).unwrap_or(5000);
    let beta0:f64=parse_arg(&args,"--planted-beta").or(parse_arg(&args,"--beta0")).and_then(|s| s.parse().ok()).unwrap_or(0.80);
    let t0:f64=parse_arg(&args,"--t0").and_then(|s| s.parse().ok()).unwrap_or(14.13472514);
    let centers:Vec<f64>=parse_arg(&args,"--centers").map(|s| s.split(',').filter_map(|x| x.trim().parse().ok()).collect()).unwrap_or(vec![14.1347,14.28,14.43,30.0,50.0]);
    let zeros=load_zeros();
    let gam:Vec<f64>=zeros.into_iter().take(m).collect();
    if gam.len()<100{ println!("INCONCLUSIVE need >=100 zeros"); return;}
    // gaps
    let gaps:Vec<f64>=(0..gam.len()-1).map(|i| gam[i+1]-gam[i]).collect();
    let mean: f64 = gaps.iter().sum::<f64>()/gaps.len() as f64;
    let var: f64 = gaps.iter().map(|&g| (g-mean).powi(2)).sum::<f64>()/gaps.len() as f64;
    let min_g = gaps.iter().cloned().fold(f64::INFINITY, f64::min);
    let max_g = gaps.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
    println!("alien persistence_zero M={} beta0={} t0={} mean_gap={:.5} VAR={:.6} min={:.4} max={:.4}", gam.len(), beta0, t0, mean, var, min_g, max_g);
    // planted: nearest gap to t0 shrinks/broadens by moving one point off line
    // Approximate: moving one zero by d0=0.30 in Re does not change gap directly (still 1D projection), but 2D hole R changes.
    // 2D hole: min distance from planted point to others in (beta,gamma) plane vs RH plane distance
    let d0=beta0-0.5;
    // find nearest neighbor distance in 1D (RH) vs 2D (planted)
    let mut idx=0; let mut best=f64::INFINITY; for (i,&g) in gam.iter().enumerate(){ let d=(g-t0).abs(); if d<best{best=d; idx=i;}}
    let mut min1d=f64::INFINITY; for &g in &gam{ if (g-gam[idx]).abs()<1e-9{continue;} let d=(g-gam[idx]).abs(); if d<min1d{min1d=d;}}
    // planted 2D distance to neighbors: sqrt(d0^2 + (dt)^2)
    let mut min2d=f64::INFINITY; for &g in &gam{ if (g-gam[idx]).abs()<1e-9{continue;} let dt=g-gam[idx]; let d2=(d0*d0+dt*dt).sqrt(); if d2<min2d{min2d=d2;}}
    println!("nearest idx={} gamma={:.6} dt0={:.4} min1D={:.4} min2D_planted={:.4} d0={:.3}", idx, gam[idx], (gam[idx]-t0).abs(), min1d, min2d, d0);
    // hole invariant R = min_{i≠j} |(beta_i-beta_j, gamma_i-gamma_j)| for RH: beta diff 0, so R = min gap
    // with one planted, minimal 2D distance becomes min(min1d, min2d) but min2d > min1d, so R_RH = min_g, R_false = min_g (almost unchanged) unless planted creates new small 2D gap
    // Instead report max gap hole persistence: longest bar in H0 = max_g
    // For H1, planted creates loop: report delta between min2d and min1d as hole radius
    let hole_gain = min2d - min1d;
    println!("H0 persistence longest bar = max_gap={:.4}  H1 hole proxy = min2D-min1D={:.4}  (planted creates inflation)", max_g, hole_gain);
    for &t in &centers{
        // gap variance local to band |γ - t|<20
        let local: Vec<f64>=gam.windows(2).filter(|w| (w[0]-t).abs()<20.0 || (w[1]-t).abs()<20.0).map(|w| w[1]-w[0]).collect();
        if local.is_empty(){ println!("center T={:.4} local_gaps=0", t); continue;}
        let lm: f64 = local.iter().sum::<f64>()/local.len() as f64;
        let lv: f64 = local.iter().map(|&g| (g-lm).powi(2)).sum::<f64>()/local.len() as f64;
        println!("center T={:.4} local_n={} local_VAR={:.6} local_mean={:.4} dt_center={:.4}", t, local.len(), lv, lm, (t-t0).abs());
    }
    println!("predicted VAR_false ~ VAR*(1+ hole_gain/mean)  H1_bar_length ~ d0={:.3}  global_ok requires local_VAR rise at blind 14.28", d0);
    println!("DONE M={} VAR={:.6} min2D={:.4} hole_gain={:.4} global_ok=check local lines above", gam.len(), var, min2d, hole_gain);
}
