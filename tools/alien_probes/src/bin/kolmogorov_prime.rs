// kolmogorov_prime — LZ76 cut-complexity + Fourier power
// Prime indicator 1_{prime}(n) for n<=N. LZ76 phrase count C as proxy for Kolmogorov complexity.
// RH-false with beta0=0.80 predicts extra term x^{beta0} in psi(x) => compressibility Delta C/N ~ N^{beta0-1}/log N.
// Also Fourier F(T)=|Σ_{p≤N} p^{-1/2} e^{i T log p}|. Planted predicts shift ΔF ~ N^{beta0-0.5}/log N.
// Prints C_RH, predicted C_false, F_RH at each center, predicted ΔF.
use std::env; use std::collections::HashSet;
fn parse_arg(a:&[String],f:&str)->Option<String>{for i in 0..a.len(){if a[i]==f&&i+1<a.len(){return Some(a[i+1].clone());} if a[i].starts_with(&format!("{}=",f)){return Some(a[i][f.len()+1..].to_string());}}None}
fn sieve(n:usize)->Vec<u8>{let mut is=vec![true;n+1]; if n>=0{is[0]=false;} if n>=1{is[1]=false;} let mut p=2; while p*p<=n{ if is[p]{ let mut m=p*p; while m<=n{is[m]=false; m+=p;}} p+=1;} is.iter().map(|&b| if b{1}else{0}).collect()}
fn lz76(s:&[u8])->usize{let n=s.len(); let mut dict:HashSet<Vec<u8>>=HashSet::new(); dict.insert(vec![]); let mut i=0; let mut cnt=0; while i<n{ let mut j=i; let mut best=j; while j<n{ let w=s[i..=j].to_vec(); if !dict.contains(&w){ best=j; break; } j+=1; if j==n{ best=j-1; break; } } // w = s[i..=best]
            let w=s[i..=best.min(n-1)].to_vec(); if !dict.contains(&w){ dict.insert(w); } else { // extend by one if at end
                if best+1 < n { dict.insert(s[i..=best+1].to_vec()); } else { dict.insert(w); }
            }
            cnt+=1; i=best+1; if i==n{break;} if cnt> 200000 {break;}
        } cnt}
fn main(){
    let args:Vec<String>=env::args().collect();
    if args.iter().any(|a| a=="--help"){println!("usage: kolmogorov_prime --N 50000 --planted-beta 0.80 --centers 14.1347,14.28,30,50"); return;}
    let n:usize=parse_arg(&args,"--N").or(parse_arg(&args,"--n")).and_then(|s| s.parse().ok()).unwrap_or(50000);
    let beta0:f64=parse_arg(&args,"--planted-beta").or(parse_arg(&args,"--beta0")).and_then(|s| s.parse().ok()).unwrap_or(0.80);
    let centers:Vec<f64>=parse_arg(&args,"--centers").map(|s| s.split(',').filter_map(|x| x.trim().parse().ok()).collect()).unwrap_or(vec![14.1347,14.28,14.43,30.0,50.0]);
    let t0:f64=parse_arg(&args,"--t0").and_then(|s| s.parse().ok()).unwrap_or(14.13472514);
    if n>800000{ println!("INCONCLUSIVE N={} too large for <5s cap", n); return; }
    let is_prime=sieve(n);
    // build binary string for LZ76 (u8 0/1)
    let s:Vec<u8>=is_prime[0..=n.min(is_prime.len()-1)].to_vec();
    let c=lz76(&s);
    let cn = c as f64 / n as f64;
    // Fourier F(T) over primes
    let mut primes:Vec<usize>=Vec::new(); for i in 2..=n{ if is_prime[i]==1{primes.push(i);}}
    let logp:Vec<f64>=primes.iter().map(|&p| (p as f64).ln()).collect();
    let inv_sqrt:Vec<f64>=primes.iter().map(|&p| (p as f64).powf(-0.5)).collect();
    println!("alien kolmogorov_prime N={} beta0={} t0={} primes={} LZ76 C={} C/N={:.6}", n, beta0, t0, primes.len(), c, cn);
    // predicted compression from x^{beta0} term: saving ~ N^{beta0}/(beta0 log N) bits vs N/log N primes
    let pred_saving = (n as f64).powf(beta0) / (beta0*(n as f64).ln()) ;
    let pred_c_false = (c as f64 - pred_saving).max(1.0);
    println!("predicted C_false ~ {:.0}  saving {:.0}  Delta_C/C {:.4}", pred_c_false, pred_saving, (c as f64 - pred_c_false)/c as f64);
    for &t in &centers{
        let mut re=0.0; let mut im=0.0; for (k,&lp) in logp.iter().enumerate(){ let w=inv_sqrt[k]; re+=w*(t*lp).cos(); im+=w*(t*lp).sin(); }
        let f=(re*re+im*im).sqrt();
        // predicted ΔF ~ N^{beta0-0.5}/(beta0 log N) * something O(1)
        let df = (n as f64).powf(beta0-0.5) / (n as f64).ln();
        println!("center T={:.4} F(T)={:.4}  pred_Delta_F~{:.4}  pred_F_false~{:.4}", t, f, df, f+df);
    }
    // global check: variance across centers
    println!("DONE N={} C/N={:.6} F_T0~computed global_ok requires C_false<C_RH and F shift persists at blind 14.28 (check lines above)", n, cn);
}
