# Verify every number in the note's tables against the run transcripts.
import re, sys

def load(path):
    return open(path).read().splitlines()

sweep = load('/tmp/e4sweep-run1.txt')
nminus = load('/tmp/e4nminus-run1.txt')
probe = load('/tmp/e4probe-run1.txt')
pairdiag = load('/tmp/pairdiag-run1.txt')

errors = []

# --- §3 real column: expect exact reproduction of these (T, trn, hsn, br, bs1, eigmin) ---
real_exp = {
 100:('0.992343','1.265459','0.719228','0.703914','2.071e-6'),
 200:('0.988856','1.261182','0.716530','0.694241','3.291e-15'),
 300:('0.994489','1.275443','0.713534','0.702511','2.491e-17'),
 400:('0.995801','1.280378','0.711225','0.702828','-6.573e-17'),
 500:('0.996327','1.280708','0.711945','0.704598','1.377e-17'),
 600:('0.998163','1.287259','0.709068','0.705395','-2.259e-16'),
 700:('0.997518','1.283776','0.711259','0.706294','-4.610e-16'),
 900:('0.999009','1.290625','0.707393','0.705412',None),
 1100:('0.999128','1.291160','0.707096','0.705352',None),
 1300:('0.999522','1.294078','0.704966','0.704010',None),
}
for T,(trn,hsn,br,bs1,emin) in real_exp.items():
    # find line starting with "{T:.0}," in section A
    for ln in sweep:
        m = re.match(rf'^{T},(\d+),', ln)
        if m:
            parts = ln.split(',')
            got = (parts[2], parts[3], parts[4], parts[5])
            if got != (trn, hsn, br, bs1):
                errors.append(f"§3 real T={T}: got {got} expect {(trn,hsn,br,bs1)}")
            if emin is not None and len(parts) > 10 and parts[10] != emin:
                errors.append(f"§3 real T={T}: eigmin got {parts[10]} expect {emin}")
            break
    else:
        errors.append(f"§3 real T={T}: line not found")

# --- §4.1 T=300 top-clustered: (beta, f) -> br ---
top300 = {
 (0.05,0.0):'0.713534',(0.05,0.005):'0.711361',(0.05,0.01):'0.707426',(0.05,0.02):'0.693359',(0.05,0.04):'0.661221',(0.05,0.08):'0.610313',
 (0.10,0.0):'0.713534',(0.10,0.005):'0.711249',(0.10,0.01):'0.706969',(0.10,0.02):'0.692130',(0.10,0.04):'0.658424',(0.10,0.08):'0.604383',
 (0.20,0.0):'0.713534',(0.20,0.005):'0.710759',(0.20,0.01):'0.705011',(0.20,0.02):'0.686792',(0.20,0.04):'0.646293',(0.20,0.08):'0.578592',
 (0.30,0.0):'0.713534',(0.30,0.005):'0.709782',(0.30,0.01):'0.701250',(0.30,0.02):'0.676250',(0.30,0.04):'0.622405',(0.30,0.08):'0.527517',
 (0.50,0.0):'0.713534',(0.50,0.005):'0.704851',(0.50,0.01):'0.683966',(0.50,0.02):'0.624821',(0.50,0.04):'0.506635',(0.50,0.08):'0.276175',
 (1.00,0.0):'0.713534',(1.00,0.005):'0.564506',(1.00,0.01):'0.314024',(1.00,0.02):'-0.617796',(1.00,0.04):'-2.193532',(1.00,0.08):'-6.062494',
}
for (beta,f),exp in top300.items():
    for ln in sweep:
        if ln.startswith(f'300,{beta:.2f},{f:.4f},'):
            parts = ln.split(',')
            got = parts[6]
            if got != exp:
                errors.append(f"§4.1 T=300 beta={beta} f={f}: br got {got} expect {exp}")
            break
    else:
        errors.append(f"§4.1 T=300 beta={beta} f={f}: line not found")

# --- §4.2 T=300 scattered: (beta, f) -> br and nneg ---
# e4nminus scattered section covers f in {0.005,0.02,0.08}; e4sweep C-table covers all f.
def section_lines(lines, header):
    out = []
    on = False
    for ln in lines:
        if ln.startswith(header):
            on = True
            continue
        if on and ln.startswith("====="):
            on = False
        if on:
            out.append(ln)
    return out

scat300 = {
 (0.05,0.005):('0.683531','0'),(0.05,0.01):('0.658914','0'),(0.05,0.02):('0.635094','2'),(0.05,0.04):('0.530928','5'),(0.05,0.08):('0.373665','13'),
 (0.10,0.005):('0.683057','0'),(0.10,0.01):('0.657954','1'),(0.10,0.02):('0.633633','2'),(0.10,0.04):('0.527718','6'),(0.10,0.08):('0.367028','14'),
 (0.30,0.005):('0.677058','1'),(0.30,0.01):('0.645870','2'),(0.30,0.02):('0.614657','3'),(0.30,0.04):('0.486515','7'),(0.30,0.08):('0.282036','16'),
 (0.50,0.005):('0.658184','1'),(0.50,0.01):('0.608305','2'),(0.50,0.02):('0.551662','4'),(0.50,0.04):('0.352984','8'),(0.50,0.08):('0.007974','16'),
}
nm_scat = section_lines(nminus, "===== n_- grid: random-scattered (seed 7) =====")
sw_c = section_lines(sweep, "===== C. SWEEP (random-scattered seed=7, T=300):")
for (beta,f),(expbr,expn) in scat300.items():
    src_lines = nm_scat if f in (0.005,0.02,0.08) else sw_c
    found = False
    for ln in src_lines:
        if re.match(rf'^(300|0\.50|0\.30|0\.10|0\.05),{beta:.2f},{f:.4f},', ln) or            (f in (0.01,0.04) and re.match(rf'^{beta:.2f},{f:.4f},', ln)):
            parts = ln.split(',')
            if f in (0.01,0.04):
                # C-table format: beta,f,N2,tr,hs,br,bs1,in_band,nneg
                gotbr, gotn = parts[5], parts[8]
            else:
                # e4nminus scattered format: T,beta,f,N2,br,bs1,n9,n10,n12,eigmin -> n10 is parts[7]
                gotbr, gotn = parts[4], parts[7]
            if gotbr != expbr or gotn != expn:
                errors.append(f"§4.2 T=300 beta={beta} f={f}: got br={gotbr} n={gotn} expect {expbr},{expn}")
            found = True
            break
    if not found:
        errors.append(f"§4.2 T=300 beta={beta} f={f}: line not found")

# --- §6 pairdiag: (position, beta) -> full-W lambdamin ---
pd = {
 ('bottom',0.02):'-1.435e-4',('bottom',0.05):'-1.053e-3',('bottom',0.10):'-4.653e-3',('bottom',0.30):'-6.172e-2',('bottom',0.50):'-2.915e-1',
 ('bulk',0.02):'-7.437e-12',('bulk',0.05):'-6.492e-11',('bulk',0.10):'-1.687e-8',('bulk',0.30):'-2.232e-6',('bulk',0.50):'-1.513e-1',
 ('top',0.02):'-1.905e-15',('top',0.05):'-1.264e-14',('top',0.10):'-5.338e-14',('top',0.30):'-9.552e-13',('top',0.50):'-1.534e-7',
}
# parse the beta sweep section
in_sweep = False
for ln in pairdiag:
    if ln.startswith('beta sweep'):
        in_sweep = True
        continue
    if not in_sweep or not re.match(r'^\d', ln):
        continue
    parts = ln.split(',')  # beta,imb,bottom_min,bottom_nneg,bulk_min,bulk_nneg,top_min,top_nneg
    beta = float(parts[0])
    cols = {'bottom': parts[2], 'bulk': parts[4], 'top': parts[6]}
    for pos, exp in pd.items():
        if abs(pos[1] - beta) < 1e-9:
            got = cols[pos[0]]
            # compare scientific notation to 3 sig figs
            if abs(float(got) - float(exp)) > 1e-3 * max(abs(float(exp)), 1e-300):
                errors.append(f"§6 {pos}: beta={beta} got {got} expect {exp}")

# --- §4.3 probe: T=300 f=1.5% br values ---
probe_exp = {(0.05,0.015):'0.701516',(0.10,0.015):'0.700779',(0.20,0.015):'0.697623',(0.30,0.015):'0.691569'}
for (beta,f),exp in probe_exp.items():
    for ln in probe:
        if re.match(rf'^{beta:.2f},{f:.4f},', ln):
            parts = ln.split(',')
            if parts[5] != exp:
                errors.append(f"§4.3 probe beta={beta} f=1.5%: got {parts[5]} expect {exp}")
            break
    else:
        errors.append(f"§4.3 probe beta={beta} f=1.5%: line not found")

if errors:
    print(f"VERIFY FAIL — {len(errors)} mismatch(es):")
    for e in errors[:40]:
        print(" ", e)
    sys.exit(1)
print(f"VERIFY PASS — all {len(real_exp)} real rows, {len(top300)} top-clustered cells, {len(scat300)} scattered cells, {len(pd)} pairdiag cells, {len(probe_exp)} probe cells match the transcripts.")
