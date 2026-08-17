// direct-rh-transfer-lane falsification probe (f64, no deps, <1 min)
// Question: can NON-spECTRAL invariants of the non-self-adjoint companion (singular-value
// decay, numerical range) detect whether an entire function's zero offsets lie on the
// imaginary axis (=RH-type) vs off-axis (RH-false control type)?
// Forecast: NO signal -> the transfer/singular-value/variational frames cannot carry a
// one-way H(zeta)=>RH (dependency D1 has no bridge: SVs/range are location-blind).
// Companion matrices are deliberately NON-SYMMETRIC (non-self-adjoint) as the lane demands.

#[derive(Clone)]
struct Cplx { re: f64, im: f64 }

impl Cplx {
    fn mul(a:&Cplx,b:&Cplx)->Cplx{ Cplx{re:a.re*b.re-a.im*b.im, im:a.re*b.im+a.im*b.re} }
    fn add(a:&Cplx,b:&Cplx)->Cplx{ Cplx{re:a.re+b.re, im:a.im+b.im} }
}

// monic polynomial coefficients (real) from a complex-conjugate-symmetric root multiset,
// in ascending order: P(z)=c0+c1 z+...+c_{n-1} z^{n-1}+z^n
fn roots_to_poly(zs:&[Cplx])->Vec<f64>{
    let mut p=vec![Cplx{re:1.0,im:0.0}]; // monic, ascending, p=1
    for z in zs{
        let q=vec![Cplx{re:-z.re,im:-z.im}, Cplx{re:1.0,im:0.0}]; // (z - zi)
        let mut np=vec![Cplx{re:0.0,im:0.0};p.len()+1];
        for (i,pc) in p.iter().enumerate(){
            for (j,qc) in q.iter().enumerate(){
                let t=Cplx::mul(pc,qc);
                np[i+j]=Cplx::add(&np[i+j],&t);
            }
        }
        p=np;
    }
    // fold tiny imag parts (symmetry ensures ~0) 
    p.iter().map(|c| if c.im.abs()<1e-9 {c.re} else {panic!("non-symmetric root set")}).collect()
}

// first companion matrix (unit superdiagonal): eigenvalues == roots by algebra
fn companion(coeff:&[f64])->Vec<Vec<f64>>{
    let n=coeff.len(); // degree n, coeff ascending 0..n-1
    let mut a=vec![vec![0.0f64;n];n];
    for i in 0..n-1 { a[i][i+1]=1.0; }
    for j in 0..n { a[n-1][j]=-coeff[j]; }
    a
}

fn sym_part(a:&[Vec<f64>], cos:bool)->Vec<Vec<f64>>{
    let n=a.len(); let mut s=vec![vec![0.0f64;n];n];
    for i in 0..n { for j in 0..n {
        // Re part (A+A^T)/2  and  Im part (A-A^T)/(2i) = (A-A^T)*i/... use real skew: (A-A^T)/2 is skew-symmetric = i*Sreal
        // Hermitian part of e^{iθ}A = cosθ*(A+A^T)/2 + sinθ*((A-A^T)/(2i)) ; (A-A^T)/2 = i*S with S real symmetric => imaginary part contribution: (A-A^T)/2 as "i times real skew"...
        // Trick: real part of e^{iθ}A hermitian part = cosθ*(A+A^T)/2 + sinθ*(A-A^T)/2 * (1/i)?? compute directly:
        // H_unscaled = e^{iθ}A = (cosθ+i sinθ)(S+K), S=(A+A^T)/2, K=(A-A^T)/2 (K skew)
        // H = (M + M*)/2 with M=e^{iθ}(S+K): M* = e^{-iθ}(S+K)^T = e^{-iθ}(S-K)
        // H = 1/2[ e^{iθ}S+e^{iθ}K + e^{-iθ}S - e^{-iθ}K ] = cosθ S + i sinθ K
        // so H = cosθ*S + i*sinθ*K ; real part matrix = cosθ*S, and since K real skew = i*(-i K): imag part = sinθ*K (K real skew) -> H = cosθ S + i sinθ K with K real skew. lambda_max of complex Hermitian H.
    }}
    // The above is a comment; actual lambda_max computed in complex below.
    s
}

// power iteration: largest eigenvalue (by modulus, then refine) of Hermitian H(θ) = cosθ*S + i sinθ*K
fn lam_max_herm(cos:&[Vec<f64>], sin:&[Vec<f64>], n:usize, iters:usize)->f64{
    // real representation: H = cos*S + i sin*K ; build 2n real symmetric matrix [[cosS, -sinK],[sinK, cosS]]
    let mut m=vec![vec![0.0f64;2*n];2*n];
    for i in 0..n { for j in 0..n {
        m[i][j]=cos[i][j];
        m[n+i][n+j]=cos[i][j];
        m[i][n+j]=-sin[i][j];
        m[n+i][j]=sin[i][j];
    }}
    // power iteration on symmetric m
    let mut v=vec![1.0f64;2*n];
    let mut lam=0.0;
    for _ in 0..iters {
        let mut w=vec![0.0f64;2*n];
        for i in 0..2*n { for j in 0..2*n { w[i]+=m[i][j]*v[j]; } }
        let nrm=w.iter().map(|x| x*x).sum::<f64>().sqrt();
        for x in w.iter_mut(){ *x/=nrm; }
        v=w;
        lam = (0..2*n).map(|i| m[i].iter().zip(&v).map(|(a,b)| a*b).sum::<f64>()*v[i]).sum::<f64>();
    }
    lam
}

// numerical range radius w(A): max_θ λ_max(H(θ)); and width.
fn num_range(a:&[Vec<f64>], n:usize)->(f64,f64){
    let mut s=vec![vec![0.0f64;n];n]; // (A+A^T)/2
    let mut k=vec![vec![0.0f64;n];n]; // (A-A^T)/2 (skew)
    for i in 0..n { for j in 0..n { s[i][j]=(a[i][j]+a[j][i])/2.0; k[i][j]=(a[i][j]-a[j][i])/2.0; } }
    let mut wmax=0.0f64; let mut wmin=1e99f64;
    for step in 0..64 {
        let theta=std::f64::consts::PI*(step as f64)/64.0;
        let c=theta.cos(); let s_in=theta.sin();
        let mut cosm=vec![vec![0.0f64;n];n];
        let mut sinm=vec![vec![0.0f64;n];n];
        for i in 0..n { for j in 0..n { cosm[i][j]=c*s[i][j]; sinm[i][j]=s_in*k[i][j]; } }
        let lam=lam_max_herm(&cosm,&sinm,n,90);
        wmax=wmax.max(lam); wmin=wmin.min(lam.max(0.0));
    }
    (wmax, wmin)
}

// singular values via two-sided Jacobi (n small)
fn svd(a_in:&[Vec<f64>], n:usize)->Vec<f64>{
    let mut a:Vec<Vec<f64>>=a_in.to_vec();
    let mut q:Vec<Vec<f64>>=(0..n).map(|i|(0..n).map(|j| if i==j{1.0}else{0.0}).collect()).collect();
    for _ in 0..30 {
        for p in 0..n { for qq in (p+1)..n {
            let (app,aqq)= (a[p][p],a[qq][qq]);
            let apq=a[p][qq];
            if apq.abs()<1e-14 {continue;}
            let tau=(aqq-app)/(2.0*apq);
            let t=tau.signum()/(tau.abs()+(1.0+tau*tau).sqrt());
            let cs=1.0/(1.0+t*t).sqrt(); let sn=t*cs;
            for k in 0..n {
                let akp=a[k][p]; let akq=a[k][qq];
                a[k][p]=cs*akp-sn*akq; a[k][qq]=sn*akp+cs*akq;
            }
            for k in 0..n {
                let apk=a[p][k]; let aqk=a[qq][k];
                a[p][k]=cs*apk-sn*aqk; a[qq][k]=sn*apk+cs*aqk;
            }
            for k in 0..n {
                let qkp=q[k][p]; let qkq=q[k][qq];
                q[k][p]=cs*qkp-sn*qkq; q[k][qq]=sn*qkp+cs*qkq;
            }
        }}
    }
    let mut sv:Vec<f64>=(0..n).map(|i| a[i][i].abs()).collect();
    sv.sort_by(|x,y| y.partial_cmp(x).unwrap());
    sv
}

fn stats(name:&str, coeff:&[f64])->(f64,f64,f64){
    let n=coeff.len();
    let a=companion(coeff);
    let sv=svd(&a,n);
    let (wmax,wmin)=num_range(&a,n);
    let s1=sv[0];
    let sn=sv[n-1];
    let slope=((sn.max(1e-300)).ln()-(s1.max(1e-300)).ln())/(n as f64);
    println!("[{name}] n={n} sigma_max={s1:.4e} sigma_min={sn:.4e} logslope/unit={slope:.4e} numrange_radius={wmax:.4e} (wmin={wmin:.4e})");
    (slope, wmax, sn)
}

fn main(){
    let rng_seed=42u64;
    let mut rng=SeedRng{rng_seed};
    // ---- Model battery: single instances ----
    // model (i) all-imaginary roots (RH-like): offsets alpha_k = i*gamma_k
    let on:Vec<Cplx> = (1..=7).flat_map(|k| { let g=(k as f64)*0.7; [Cplx{re:0.0, im:g}, Cplx{re:0.0, im:-g}] }).collect();
    // model (ii) planted off-axis pair (DH-like): alpha = a +- ib plus its reflected mate
    let mut off=on.clone();
    off.extend(vec![Cplx{re:0.31, im:2.1}, Cplx{re:0.31, im:-2.1}, Cplx{re:-0.31, im:2.1}, Cplx{re:-0.31, im:-2.1}]);
    let p_on=roots_to_poly(&on);
    let p_off=roots_to_poly(&off);
    println!("== single-instance model battery (companion = non-self-adjoint Hessenberg) ==");
    let (sl_on,wr_on,sn_on)=stats("all-imag zeros (RH-like)",&p_on);
    let (sl_off,wr_off,sn_off)=stats("planted off-axis pair (DH-like)",&p_off);
    println!("-- do non-spectral invariants separate? slope diff={:.3e} radius diff={:.3e}",
        (sl_off-sl_on).abs(), (wr_off-wr_on).abs());

    // ---- Random family correlation battery: does ANY sv/range statistic track axis-deviation? ----
    // sample 120 real monic polys degree 12: roots from two regimes; measure corr(stat, max|Re alpha|)
    let mut xs:Vec<f64>=vec![]; let mut ys_slope:Vec<f64>=vec![]; let mut ys_rad:Vec<f64>=vec![]; let mut ys_smin:Vec<f64>=vec![];
    for it in 0..120 {
        let mut zs:Vec<Cplx>=vec![];
        if it%2==0 { // on-axis regime
            for _ in 0..6 { let g=next_uni(&mut rng)*2.0+0.2; zs.push(Cplx{re:0.0,im:g}); zs.push(Cplx{re:0.0,im:-g}); }
        } else { // off-axis regime: one pair pushed off
            for k in 0..5 { let g=next_uni(&mut rng)*2.0+0.3; zs.push(Cplx{re:0.0,im:g}); zs.push(Cplx{re:0.0,im:-g}); }
            let a=next_uni(&mut rng)*0.35+0.05; let b=next_uni(&mut rng)*2.0+0.3;
            zs.push(Cplx{re:a,im:b}); zs.push(Cplx{re:a,im:-b});
        }
        let p=roots_to_poly(&zs);
        let (sl,wr,smin)=stats(&format!("fam#{it}"),&p);
        let maxdev=zs.iter().map(|z| z.re.abs()).fold(0.0f64,f64::max);
        xs.push(maxdev); ys_slope.push(sl); ys_rad.push(wr); ys_smin.push(smin.ln());
    }
    let c1=corr(&xs,&ys_slope); let c2=corr(&xs,&ys_rad); let c3=corr(&xs,&ys_smin);
    println!("== correlation (statistic vs max|Re alpha|) over 120 models ==");
    println!("corr(singular-value logslope, axis-deviation) = {c1:+.3}");
    println!("corr(numerical-range radius, axis-deviation)  = {c2:+.3}");
    println!("corr(log sigma_min, axis-deviation)           = {c3:+.3}");
    println!("interpretation: |corr| ~ 0 => singular values / numerical range carry NO zero-location signal (dependency D1 absent)");
}

// tiny xorshift
struct SeedRng{ rng_seed:u64 }
fn next_uni(r:&mut SeedRng)->f64{
    let mut x=r.rng_seed;
    x^=x<<13; x^=x>>7; x^=x<<17; r.rng_seed=x;
    (x>>11) as f64 / (1u64<<53) as f64
}

fn corr(x:&[f64],y:&[f64])->f64{
    let n=x.len() as f64;
    let mx=x.iter().sum::<f64>()/n; let my=y.iter().sum::<f64>()/n;
    let mut sxy=0.0; let mut sxx=0.0; let mut syy=0.0;
    for i in 0..x.len(){ sxy+=(x[i]-mx)*(y[i]-my); sxx+=(x[i]-mx).powi(2); syy+=(y[i]-my).powi(2); }
    sxy/(sxx.sqrt()*syy.sqrt())
}