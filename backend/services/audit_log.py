import json, time

AUDIT_FILE = "/opt/shix/data/audit.log"

def audit(event: str, actor: str, meta: dict | None = None):
    entry = {
        "ts": int(time.time()),
        "event": event,
        "actor": actor,
        "meta": meta or {}
    }
    with open(AUDIT_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
