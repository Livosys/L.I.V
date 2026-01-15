import json, time, os

AUDIT_FILE = "/opt/shix/data/audit_rag.log"
os.makedirs("/opt/shix/data", exist_ok=True)

def log_rag(tenant, query, results):
    record = {
        "ts": int(time.time()),
        "tenant": tenant,
        "query": query,
        "results": [r.get("id") for r in results]
    }
    with open(AUDIT_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")
