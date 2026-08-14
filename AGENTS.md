# pclink ops — phone ↔ laptop remote access

The pclink system links this phone (Termux + proot Ubuntu) to the Void Linux laptop (`void`, 192.168.1.50).
Two independent layers — you can run either or both:

## Layer 1 — LAN ONLY (recommended default, no internet exposure)
`link-laptop` keeper on the laptop: LAN beacon discovery → reverse tunnel so the phone reaches the
laptop at `127.0.0.1:2223`, plus direct `pc-lan` when on the same wifi.

### Turn ON (LAN)
```sh
# on the laptop (root):
ln -sf /etc/sv/link-laptop /var/service/link-laptop && sv start link-laptop
# verify: sv status link-laptop → run: link-laptop
```
From the phone (inside proot: `proot-distro login ubuntu`):
```sh
pc        # LAN tunnel (127.0.0.1:2223)
pc-lan    # direct 192.168.1.50:22 (same wifi)
```

### Turn OFF (LAN)
```sh
# on the laptop:
sv stop link-laptop && rm -f /var/service/link-laptop
```

## Layer 2 — RELAY (from anywhere, via oracle-old container)
`pclink-relay` Docker container on oracle-old (168.110.203.180), host network, **port 25565**.
Host sshd (port 22) is admin-only. Laptop `pclink` service opens tunnel 2310 through the container.
Also makes any computer reachable via `pc-any` after running the bootstrap script.

### Turn ON (relay)
```sh
# on the relay (oracle-old, as ubuntu):
docker start pclink-relay
# on the laptop (root):
ln -sf /etc/sv/pclink /var/service/pclink && sv start pclink
```
From the phone (proot):
```sh
pc-jump      # via relay container (25565) → tunnel 2310
pc-any       # list / connect to any linked computer
```

### Turn OFF (relay)
```sh
# on the laptop:
sv stop pclink && rm -f /var/service/pclink
# on the relay:
docker stop pclink-relay        # no auto-restart (set with docker update --restart no)
```

## FULL OFF (both layers)
Combine both OFF blocks above. Nothing is ever deleted by these commands — services live in
`/etc/sv/`, the container image `pclink-relay:latest` persists, and `ln -sf` brings them back.

## Key facts / gotchas
- Phone sshd (proot) runs on port **8023**, **key-only** (no passwords). Laptop keeper uses
  `/root/.ssh/phone-keeper`. Phone host sshd port 2222 in `sshd_config.d/rescue.conf`.
- Relay container registry lives in `/opt/pclink-relay/registry` (bind-mounted volume) — survives rebuilds.
- Rebuild relay: `docker build -t pclink-relay:latest /tmp/pclink-relay-build && docker run -d --name pclink-relay --restart unless-stopped --network host -v /opt/pclink-relay/registry:/home/ubuntu/pclink pclink-relay:latest` (build context: `/root/pclink/relay-container/`).
- The public bootstrap URL (`https://vstal.in/pclink.sh`) was intentionally REMOVED (404) during shutdown — restore by copying `/root/pclink/bootstrap.sh` + `pclink.ps1` to the relay webroot `/usr/share/nginx/html/` if you ever want the curl|sh feature back.
- Oracle VCN firewall only opens 22/80/443/25565 — the relay uses 25565 because of this.
- `rescue123` root password no longer exists; don't re-add it.
- Repo: `vstaln/void-linux` (private), pclink kit in `/root/pclink/`, uncommitted work stays local.

---

# Riemann Program — Persistent Agent Hooks

## Mission
The Riemann hypothesis (RH): every nontrivial zero of ζ(s) lies on Re(s) = 1/2.
This project pursues a proof of RH — and alongside it, any rigorous, novel mathematics about ζ and its zeros. **We never give up on the search for a proof.** The search persists across sessions, attempts, and failures; a failed attack is a documented result, not a reason to stop.

## Keep trying — always (the persistence hook)
- **The search is possible. Do not stop.** A failure is a documented result, not a reason to stop. This hook binds on every model in every session, forever.
- When a computation fails, times out, or disagrees with expectations, that is the start of work, not the end: (1) record what was attempted and what actually happened; (2) find the root cause; (3) try again by a different route.
- When a proof attempt stalls, do not conclude "impossible". Re-derive from the contract, weaken the claim, transport the method from a neighboring problem, or decompose the blocker into sub-blockers.
- Only the honesty guardrails can stop a line of work: a claim may be labeled ABANDONED (with the documented reason) but the *search* is never abandoned.

## Non-negotiables (honesty guardrails)
1. Never fabricate a proof, lemma, or numerical result. No exception.
2. Every claim is labeled: PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED.
3. Nothing counts as progress until adversarial validators fail to break it.
4. Never weaken a validator to make a result pass.
5. A wrong, confident result is worse than no result — it poisons the whole search.

