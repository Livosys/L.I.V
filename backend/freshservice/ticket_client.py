import os
import requests

BASE_URL = "https://nordichccom.freshservice.com/api/v2"
API_KEY = os.getenv("FRESHSERVICE_API_KEY")

def _get(path, params=None):
    r = requests.get(
        f"{BASE_URL}{path}",
        auth=(API_KEY, "X"),
        params=params,
        timeout=10,
    )

    if r.status_code != 200:
        print("Debug: Tickets Response =", r.status_code, r.text)

    r.raise_for_status()
    return r.json()

def list_tickets():
    return _get("/tickets", params={"filter": "new_and_my_open"})
