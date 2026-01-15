import json
import time

LOG_FILE = "/opt/shix/data/search_misses.log"

def log_search_miss(tenant: str, query: str, lang: str):
    entry = {
        "ts": int(time.time()),
        "tenant": tenant,
        "query": query,
        "lang": lang
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
