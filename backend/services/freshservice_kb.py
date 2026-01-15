import os
import requests

FRESHSERVICE_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
API_KEY = os.getenv("FRESHSERVICE_API_KEY")
WORKSPACE_ID = os.getenv("FRESHSERVICE_WORKSPACE_ID", "1")

if not FRESHSERVICE_DOMAIN:
    raise RuntimeError("FRESHSERVICE_DOMAIN is not set")

BASE_URL = f"https://{FRESHSERVICE_DOMAIN}/api/v2"

HEADERS = {
    "Content-Type": "application/json",
    "X-Workspace-Id": WORKSPACE_ID
}

def search_kb(query: str, limit: int = 3):
    try:
        params = {
            "query": query,
            "per_page": limit
        }

        r = requests.get(
            f"{BASE_URL}/solutions/articles/search",
            headers=HEADERS,
            auth=(API_KEY, "X"),
            params=params,
            timeout=2
        )

        if r.status_code != 200:
            return []

        return r.json().get("articles", [])

    except Exception:
        return []
