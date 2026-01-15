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

def fetch_all_tickets():
    tickets = []
    page = 1
    while True:
        print(f"Fetching page {page}...")
        r = requests.get(
            f"{BASE_URL}/tickets",
            auth=(API_KEY, "X"),
            params={"filter": "new_and_my_open", "page": page, "per_page": 100}  # Changed to a valid filter
        )
        print(f"Status code: {r.status_code}")
        if r.status_code != 200:
            print(f"Error: {r.text}")
            break
        batch = r.json().get("tickets", [])
        if not batch:
            print(f"No more tickets found. Total fetched: {len(tickets)}")
            break
        tickets.extend(batch)
        page += 1
    return tickets

if __name__ == "__main__":
    tickets = fetch_all_tickets()
    if tickets:
        ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        out = f"{OUT_DIR}/tickets_{ts}.json"
        with open(out, "w") as f:
            json.dump(tickets, f, indent=2)
        print(f"INGEST OK: {len(tickets)} tickets → {out}")
    else:
        print("No tickets found with status: 'new_and_my_open'")
