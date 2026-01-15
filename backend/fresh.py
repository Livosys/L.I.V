import os
import base64
import requests

FRESHSERVICE_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
FRESHSERVICE_API_KEY = os.getenv("FRESHSERVICE_API_KEY")

def fs_url(path: str):
    return f"https://{FRESHSERVICE_DOMAIN}/api/v2{path}"

def fs_headers():
    token = base64.b64encode(f"{FRESHSERVICE_API_KEY}:X".encode()).decode()
    return {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json"
    }

# -------------------- GET TICKET --------------------
def get_ticket(ticket_id: int):
    url = fs_url(f"/tickets/{ticket_id}")
    r = requests.get(url, headers=fs_headers())
    return r.json()

# -------------------- UPDATE TICKET --------------------
def update_ticket(ticket_id: int, data: dict):
    url = fs_url(f"/tickets/{ticket_id}")
    r = requests.put(url, headers=fs_headers(), json=data)
    return r.json()

# -------------------- LIST TICKETS --------------------
def list_tickets(filters: dict = None):
    url = fs_url("/tickets")
    r = requests.get(url, headers=fs_headers(), params=filters)
    return r.json()

# -------------------- SEARCH USER --------------------
def search_user(query: str):
    url = fs_url("/users/autocomplete")
    r = requests.post(url, headers=fs_headers(), json={"term": query})
    return r.json()

# -------------------- GET USER --------------------
def get_user(user_id: int):
    url = fs_url(f"/users/{user_id}")
    r = requests.get(url, headers=fs_headers())
    return r.json()
