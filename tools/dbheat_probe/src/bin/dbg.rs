// quick debug of quadrature accuracy at x ~ 43
use std::f64::consts::PI;
fn phi(u: f64) -> f64 {
    let e2u = (2.0*u).exp();
    let eu2 = u.exp().sqrt();
    let e9h = e2u*e2u*eu2;
    let e5h = e2u*eu2;
    let mut s = 0.0;
    for n in 1..=80u64 {
        let nf = n as f64; let n2 = nf*nf; let n4 = n2*n2;
        let arg = PI*n2*e2u;
        let term = 2.0*(2.0*PI*PI*n4*e9h - 3.0*PI*n2*e5h)*(-arg).exp();
        s += term;
        if n>1 && term.abs() < 1e-30*s.abs() { break; }
    }
    s
}
fn comp(f: &impl Fn(f64)->(f64,f64), a: f64, b: f64, n: usize) -> (f64,f64) {
    let h = (b-a)/n as f64;
    let (fa,fai)=f(a); let (fb,fbi)=f(b);
    let mut sum = (fa+fb, fai+fbi);
    for i in 1..n {
        let x = a + i as f64*h;
        let (v,vi)=f(x);
        let w = if i%2==1 {4.0} else {2.0};
        sum.0 += w*v; sum.1 += w*vi;
    }
    (sum.0*h/3.0, sum.1*h/3.0)
}
fn main() {
    for &x in &[14.1347251417, 43.3270733, 43.3270752] {
        let f = |u: f64| { let w = phi(u); let c=(x*u).cos(); (w*c, 0.0) };
        let mut n = 256usize;
        let mut s = comp(&f, 0.0, 6.0, n);
        println!("x={}: ", x);
        for _ in 0..8 {
            let s2 = comp(&f, 0.0, 6.0, 2*n);
            let v2 = 2.0*s2.0;
            println!("  n={:6} H~{:.12e}  diff={:.2e}", 2*n, v2, (s2.0-s.0).abs());
            s = s2; n *= 2;
        }
    }
    // H' at gamma8
    let x = 43.327073280915;
    let fp = |u: f64| { let w = phi(u)*u; let s=(x*u).sin(); (-w*s, 0.0) };
    let n = 65536;
    let s = comp(&fp, 0.0, 6.0, n);
    println!("H'({}) ~ {:.6e}", x, 2.0*s.0);
}
