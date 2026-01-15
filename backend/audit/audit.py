import datetime, json

LOG = "/opt/shix/backend/audit/audit.log"

def log(actor, action, meta=None):
    with open(LOG,"a") as f:
        f.write(json.dumps({
            "ts": datetime.datetime.utcnow().isoformat(),
            "actor": actor,
            "action": action,
            "meta": meta
        }) + "\n")
