from agents.sla_agent import evaluate_sla
from freshservice.client import get_ticket
import requests
import os

FRESHSERVICE_URL = "https://livosys.freshservice.com/api/v2"
API_KEY = os.getenv("FRESHSERVICE_API_KEY")

def auto_escalate(ticket_id: int):
    ticket = get_ticket(ticket_id)

    priority = ticket["ticket"]["priority"]
    hours_open = ticket["ticket"]["created_at"]

    sla = evaluate_sla(priority="high", hours_open=4)

    if sla["risk"] == "breach":
        requests.post(
            f"{FRESHSERVICE_URL}/tickets/{ticket_id}/notes",
            auth=(API_KEY, "X"),
            json={
                "body": f"🚨 AUTO-ESCALATION: {sla['action']}",
                "private": True
            }
        )

        return {"escalated": True, "reason": sla["action"]}

    return {"escalated": False}
