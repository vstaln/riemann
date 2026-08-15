"""Second-machine proxy: grid=8000 variant of the record certificate (alpha=1.464, target 620/1e5).

DIFFERENT numerical configuration vs the original grid=4000 certificate:
  * grid=8000 -> kernel table of ~149k cells (vs ~74k), a different interval
    discretization, different range-min tables, and a different B&B tree.
  * fresh ephemeral uv env (python-flint 0.9.0 / mpmath 1.4.1) on host void.
Expected if the certificate is robust: verified=True (node count will differ from
1096556 since the discretization changed). A node-limit False is INCONCLUSIVE, not
a refutation (grid=8000 is not the certified configuration).
"""
import sys
sys.path.insert(0, '/home/vstaln/riemann/tools')
from verify_coboundary_floor import verify_floor, cosine_kernel
w = {(i, j): 2.0 / (7 - (j - i)) for i in range(7) for j in range(i + 1, 7)}
p = [c / 1920000 for c in [946, 1177, 877, 877, 1177, 946]]
q = [31343 / 100000, 1 / 3, 105971 / 300000, 105971 / 300000, 1 / 3, 31343 / 100000]
r = verify_floor(cosine_kernel(1.464), w, 1.0 / 3000, 6, 620 / 100000,
                 grid=8000, cap_scheme='coboundary',
                 pressure_coeffs=p, nearest_coeffs=q, max_nodes=8000000)
print('RESULT8000', r['verified'], r['nodes'], r.get('status'), r.get('reason'), flush=True)
