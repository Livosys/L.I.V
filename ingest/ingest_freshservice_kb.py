#!/usr/bin/env python3
import os
import json
import requests
from datetime import datetime

API_KEY = os.getenv("FRESHSERVICE_API_KEY")
DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")

assert API_KEY, "FRESHSERVICE_API_KEY missing"
assert DOMAIN, "FRESHSERVICE_DOMAIN missing"

BASE_URL = f"https://{DOMAIN}.freshservice.com/api/v2"
OUT_DIR = "/opt/shix/data/ingest"
os.makedirs(OUT_DIR, exist_ok=True)

CATEGORY_ID = 58000008974
FOLDER_ID = 58000010015

def fetch_all_articles():
    articles = []
    page = 1
    while True:
        r = requests.get(
            f"{BASE_URL}/solutions/articles",
            auth=(API_KEY, "X"),
            params={"category_id": CATEGORY_ID, "folder_id": FOLDER_ID, "page": page, "per_page": 100}
        )
        r.raise_for_status()
        batch = r.json().get("articles", [])
        if not batch:
            break
        articles.extend(batch)
        page += 1
    return articles

if __name__ == "__main__":
    articles = fetch_all_articles()
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    out = f"{OUT_DIR}/kb_{ts}.json"
    with open(out, "w") as f:
        json.dump(articles, f, indent=2)
    print(f"INGEST OK: {len(articles)} articles → {out}")
