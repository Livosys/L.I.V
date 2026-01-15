import os
import requests
from rag.neo4j_client import upsert_cmdb

FRESHSERVICE_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
FRESHSERVICE_API_KEY = os.getenv("FRESHSERVICE_API_KEY")
FRESHSERVICE_WORKSPACE_ID = os.getenv("FRESHSERVICE_WORKSPACE_ID", "1")

HEADERS = {
    "Content-Type": "application/json",
    "X-Workspace-Id": FRESHSERVICE_WORKSPACE_ID
}

def ingest_ticket_to_cmdb(ticket_id: int):
    url = f"https://{FRESHSERVICE_DOMAIN}.freshservice.com/api/v2/tickets/{ticket_id}"

    r = requests.get(
        url,
        auth=(FRESHSERVICE_API_KEY, "X"),
        headers=HEADERS,
        timeout=15
    )
    r.raise_for_status()

    ticket = r.json()["ticket"]

    upsert_cmdb(
        ticket_id=ticket_id,
        ci_id=str(ticket["id"]),
        ci_name=ticket.get("subject", "Unknown CI"),
        ci_type="service",
        sla_name=ticket.get("sla_policy_name", "Default"),
        customer_name=ticket.get("requester", {}).get("name", "Unknown"),
    )

    return {"ticket_id": ticket_id, "status": "ingested"}
