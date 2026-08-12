"""Compute the projected bound for each (alpha, psum) using achievable eps.
This tells us the certifiable ceiling of the 7-point uniform mechanism."""
import mpmath as mp
mp.mp.dps = 50
def H_cosine(alpha):
    I0 = 2*mp.sin(alpha/2)/alpha
    I2 = mp.mpf(1)/2 + mp.sin(alpha)/(2*alpha)
    constant = mp.sin(alpha/2)/alpha + 2*mp.cos(alpha/2)/alpha**2
    J = -2*I2/alpha**2 + constant*I0
    c = I0**2/(I2+J)
    return 2 - 1/c
def Phi(E, m):
    E, m = mp.mpf(E), mp.mpf(m)
    thr = m/(m-1)
    return E if E <= thr else 2*mp.sqrt((m-1)*E/m) - 1 + E/m
def bound_from_eps(H, eps, m, psum):
    A = eps*(m-6); B = Phi(A, m); tau = psum*(m-6)/m
    return (H-tau)/(1-B/m)

# achievable eps from eps_map (interpolated from runs)
eps_data = {
    (1.40,320):0.0058990,(1.40,280):0.0064303,(1.40,260):0.0067497,(1.40,240):0.0077556,(1.40,220):0.0084243,(1.40,200):0.0087146,
    (1.41,320):0.0058120,(1.41,280):0.0068454,(1.41,260):0.0070708,(1.41,240):0.0072557,(1.41,220):0.0075646,(1.41,200):0.0080999,
    (1.414,320):0.0059448,(1.414,280):0.0066136,(1.414,260):0.0069160,(1.414,240):0.0073183,(1.414,220):0.0079088,(1.414,200):0.0088271,
    (1.42,320):0.0058615,(1.42,280):0.0064547,(1.42,260):0.0069050,(1.42,240):0.0072714,(1.42,220):0.0084350,(1.42,200):0.0092003,
    (1.45,320):0.0059360,(1.45,280):0.0066124,(1.45,260):0.0068071,(1.45,240):0.0078839,(1.45,220):0.0083178,(1.45,200):0.0086294,
    (1.47,320):0.0058453,(1.47,280):0.0067963,(1.47,260):0.0070945,(1.47,240):0.0073470,(1.47,220):0.0085198,(1.47,200):0.0091198,
    (1.49,320):0.0061206,(1.49,280):0.0067460,(1.49,260):0.0072607,(1.49,240):0.0076485,(1.49,220):0.0079772,(1.49,200):0.0092630,
    (1.50,320):0.0060868,(1.50,280):0.0064886,(1.50,260):0.0068309,(1.50,240):0.0077071,(1.50,220):0.0084080,(1.50,200):0.0088676,
    (1.52,320):0.0062330,(1.52,280):0.0069064,(1.52,260):0.0069474,(1.52,240):0.0073705,(1.52,220):0.0083544,(1.52,200):0.0091770,
    (1.55,320):0.0061089,(1.55,280):0.0069634,(1.55,260):0.0076314,(1.55,240):0.0076791,(1.55,220):0.0084420,(1.55,200):0.0090776,
}

record = mp.mpf("0.6731929114731422535")
results = []
for (alpha, psum_inv), eps in eps_data.items():
    H = H_cosine(alpha)
    psum = mp.mpf(1)/psum_inv
    best = (mp.mpf(-1), None)
    for m in range(60, 800):
        b = bound_from_eps(H, eps, m, psum)
        if b > best[0]: best = (b, m)
    results.append((float(best[0]), alpha, psum_inv, eps, best[1]))
results.sort(reverse=True)
print("=== TOP 15 projected certifiable bounds (7-pt uniform mechanism) ===")
for r in results[:15]:
    print(f"bound={r[0]:.10f} alpha={r[1]:.3f} psum=1/{r[2]} eps={r[3]:.7f} m={r[4]}")
