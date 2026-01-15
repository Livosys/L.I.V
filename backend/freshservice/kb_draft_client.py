import os
import requests

BASE_URL = os.getenv("FRESHSERVICE_BASE_URL")
API_KEY = os.getenv("FRESHSERVICE_API_KEY")

HEADERS = {
    "Content-Type": "application/json"
}

def create_kb_draft(title: str, description: str, category_id: int):
    url = f"{BASE_URL}/solutions/articles"
    payload = {
        "title": title,
        "description": description,
        "status": 1,
        "category_id": category_id
    }

    r = requests.post(
        url,
        auth=(API_KEY, "X"),
        headers=HEADERS,
        json=payload,
        timeout=15
    )
    r.raise_for_status()
    return r.json()
