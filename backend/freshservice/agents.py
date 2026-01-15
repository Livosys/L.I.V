import os
import requests

API_KEY = os.getenv("FRESHSERVICE_API_KEY")
DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")

BASE_URL = f"https://{DOMAIN}.freshservice.com/api/v2"
_cache = {}

def get_agent_name(agent_id):
    if not agent_id:
        return "Unassigned"

    if agent_id in _cache:
        return _cache[agent_id]

    try:
        r = requests.get(
            f"{BASE_URL}/agents/{agent_id}",
            auth=(API_KEY, "X"),
            timeout=10
        )
        if not r.ok:
            return str(agent_id)

        a = r.json().get("agent", {})
        name = f"{a.get('first_name','')} {a.get('last_name','')}".strip()
        _cache[agent_id] = name or str(agent_id)
        return _cache[agent_id]
    except Exception:
        return str(agent_id)
