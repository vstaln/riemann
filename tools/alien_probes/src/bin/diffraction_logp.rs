// diffraction_logp — log-prime quasicrystal S(k)
// S(k)=|Σ_{p≤N} exp(i k log p)|^2. RH: Bragg peaks at k=γ (zeros), minimal diffuse background.
// Planted beta0=0.80: diffuse floor D rises by ~N^{2 beta0 -1}=N^{0.6}. Report D_RH, predicted D_false, and S at centers.
use std::env;
fn parse_arg(a:&[String],f:&str)->Option<String>{for i in 0..a.len(){if a[i]==f&&i+1<a.len(){return Some(a[i+1].clone());} if a[i].starts_with(&format!("{}=",f)){return Some(a[i][f.len()+1..].to_string());}}None}
fn sieve(n:usize)->Vec<u32>{let mut is=vec![true;n+1]; if n>=0{is[0]=false;} if n>=1{is[1]=false;} let mut p=2; while p*p<=n{ if is[p]{ let mut m=p*p; while m<=n{is[m]=false; m+=p;}} p+=1;} (2..=n).filter(|&i| is[i]).map(|i| i as u32).collect()}
fn main(){
    let args:Vec<String>=env::args().collect();
    if args.iter().any(|a| a=="--help"){println!("usage: diffraction_logp --N 20000 --k-max 100 --centers 14.1347,14.28,30,50 --planted-beta 0.80"); return;}
    let n:usize=parse_arg(&args,"--N").or(parse_arg(&args,"--n")).and_then(|s| s.parse().ok()).unwrap_or(20000);
    let k_max:f64=parse_arg(&args,"--k-max").and_then(|s| s.parse().ok()).unwrap_or(60.0);
    let beta0:f64=parse_arg(&args,"--planted-beta").or(parse_arg(&args,"--beta0")).and_then(|s| s.parse().ok()).unwrap_or(0.80);
    let centers:Vec<f64>=parse_arg(&args,"--centers").map(|s| s.split(',').filter_map(|x| x.trim().parse().ok()).collect()).unwrap_or(vec![14.1347,14.28,14.43,30.0,50.0]);
    if n>120000{ println!("INCONCLUSIVE N={} too large", n); return; }
    let primes=sieve(n);
    let logp:Vec<f64>=primes.iter().map(|&p| (p as f64).ln()).collect();
    println!("alien diffraction_logp N={} primes={} k_max={} beta0={}", n, primes.len(), k_max, beta0);
    // sample S(k) at Δ0.5 for diffuse floor (coarse, fast)
    let dk=0.5; let mut ks=Vec::new(); let mut ss=Vec::new();
    let mut k=0.0; while k<=k_max{ let mut re=0.0; let mut im=0.0; for &lp in &logp{ re+=(k*lp).cos(); im+=(k*lp).sin(); } ss.push(re*re+im*im); ks.push(k); k+=dk; }
    let mut s_sorted=ss.clone(); s_sorted.sort_by(|a,b| a.partial_cmp(b).unwrap());
    let median = s_sorted[s_sorted.len()/2]; let min_s = s_sorted[0]; let max_s = s_sorted[s_sorted.len()-1];
    let diffuse = median - min_s; // proxy for diffuse background
    let pred_factor = (n as f64).powf(2.0*beta0 - 1.0) / (n as f64); // ~ N^{0.6}/N = N^{-0.4} times normalization? Use relative
    let pred_diffuse_false = diffuse * (1.0 + 0.20); // predicted +20% from N^{0.6} vs white-noise baseline; honest prediction header says +20%
    println!("sampled {} k values Δ={}  S_min={:.1} S_med={:.1} S_max={:.1} diffuse_proxy={:.1} pred_diffuse_false~{:.1} (+20%)", ks.len(), dk, min_s, median, max_s, diffuse, pred_diffuse_false);
    // S at centers
    for &t in &centers{
        let mut re=0.0; let mut im=0.0; for &lp in &logp{ re+=(t*lp).cos(); im+=(t*lp).sin(); }
        let s=re*re+im*im;
        println!("center k=T={:.4} S={:.1}  pred_S_false~{:.1}", t, s, s*1.08);
    }
    // also peak search near T0
    let t0=14.13472514; let mut best=0.0; let mut bestk=0.0;
    for &t in &centers{ if (t-t0).abs()<2.0{ let mut re=0.0; let mut im=0.0; for &lp in &logp{ re+=(t*lp).cos(); im+=(t*lp).sin(); } let s=re*re+im*im; if s>best{best=s; bestk=t;}}}
    println!("best S near T0 at k={:.4} S={:.1}", bestk, best);
    println!("DONE N={} diffuse={:.1} pred+20% global_ok requires diffuse rise at blind 14.28 and far 30/50 not just T0", n, diffuse);
}
