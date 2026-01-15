import os
import requests

FRESHSERVICE_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
API_KEY = os.getenv("FRESHSERVICE_API_KEY")
WORKSPACE_ID = os.getenv("FRESHSERVICE_WORKSPACE_ID", "1")

# ⚠️ VIKTIGT: sätt en giltig category_id
DEFAULT_CATEGORY_ID = int(os.getenv("FRESHSERVICE_KB_CATEGORY_ID", "0"))

BASE_URL = f"https://{FRESHSERVICE_DOMAIN}/api/v2"

HEADERS = {
    "Content-Type": "application/json",
    "X-Workspace-Id": WORKSPACE_ID
}

def create_kb_draft(title: str, description: str):
    if not DEFAULT_CATEGORY_ID:
        raise RuntimeError("FRESHSERVICE_KB_CATEGORY_ID is not set")

    payload = {
        "article": {
            "title": title,
            "description": description,
            "category_id": DEFAULT_CATEGORY_ID,
            "status": 1  # 1 = draft
        }
    }

    r = requests.post(
        f"{BASE_URL}/solutions/articles",
        headers=HEADERS,
        auth=(API_KEY, "X"),
        json=payload,
        timeout=5
    )

    if r.status_code not in (200, 201):
        # 🔍 DEBUG-HJÄLP
        raise RuntimeError(f"Freshservice error {r.status_code}: {r.text}")

    return r.json().get("article")
