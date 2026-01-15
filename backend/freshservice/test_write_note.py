import os
import requests

FRESHSERVICE_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
FRESHSERVICE_API_KEY = os.getenv("FRESHSERVICE_API_KEY")
FRESHSERVICE_WORKSPACE_ID = os.getenv("FRESHSERVICE_WORKSPACE_ID", "2")

TICKET_ID = 4

url = f"https://{FRESHSERVICE_DOMAIN}.freshservice.com/api/v2/tickets/{TICKET_ID}/notes"

payload = {
    "body": "🤖 SHIX test note: CMDB ingest verified successfully.",
    "private": True
}

headers = {
    "Content-Type": "application/json",
    "X-Workspace-Id": FRESHSERVICE_WORKSPACE_ID
}

r = requests.post(
    url,
    auth=(FRESHSERVICE_API_KEY, "X"),
    headers=headers,
    json=payload,
    timeout=15
)

print("Status:", r.status_code)
print(r.text)
