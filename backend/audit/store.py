import json
import hashlib
import datetime
from pathlib import Path

BASE = Path("/opt/shix/backend/audit/logs")
BASE.mkdir(parents=True, exist_ok=True)

def log_event(tenant: str, actor: str, action: str, details: dict):
    timestamp = datetime.datetime.utcnow().isoformat()
    entry = {
        "tenant": tenant,
        "actor": actor,
        "action": action,
        "details": details,
        "timestamp": timestamp
    }

    raw = json.dumps(entry, sort_keys=True)
    entry["hash"] = hashlib.sha256(raw.encode()).hexdigest()

    logfile = BASE / f"{tenant}.log"
    with open(logfile, "a") as f:
        f.write(json.dumps(entry) + "\n")
