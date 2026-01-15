import json
from datetime import datetime

def log_rag(query: str, answer: str):
    with open("/opt/shix/backend/audit/rag.log", "a") as f:
        f.write(json.dumps({
            "ts": datetime.utcnow().isoformat(),
            "query": query,
            "answer": answer
        }) + "\n")
