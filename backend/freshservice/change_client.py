import os
import requests
import logging

log = logging.getLogger("freshservice.change")

API_KEY = os.getenv("FRESHSERVICE_API_KEY")
DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
WORKSPACE_ID = os.getenv("FRESHSERVICE_WORKSPACE_ID")

BASE_URL = f"https://{DOMAIN}/api/v2"
AUTH = (API_KEY, "X")
HEADERS = {"Content-Type": "application/json"}


def list_recent_changes(limit: int = 10):
    """
    Read-only: lista senaste changes (CAB / audit)
    """
    url = f"{BASE_URL}/changes"
    params = {"per_page": limit}
    if WORKSPACE_ID:
        params["workspace_id"] = WORKSPACE_ID

    try:
        r = requests.get(
            url,
            auth=AUTH,
            headers=HEADERS,
            params=params,
            timeout=15,
        )
        r.raise_for_status()
        return r.json().get("changes", [])
    except Exception:
        log.exception("Failed to list changes from Freshservice")
        return []


def get_change_by_id(change_id: str):
    """
    Read-only: hämta en specifik change
    """
    url = f"{BASE_URL}/changes/{change_id}"
    params = {}
    if WORKSPACE_ID:
        params["workspace_id"] = WORKSPACE_ID

    try:
        r = requests.get(
            url,
            auth=AUTH,
            headers=HEADERS,
            params=params,
            timeout=15,
        )
        if r.status_code == 404:
            return None
        r.raise_for_status()
        return r.json().get("change")
    except Exception:
        log.exception("Failed to fetch change %s", change_id)
        return None
