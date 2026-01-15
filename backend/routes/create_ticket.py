import os
import requests
from fastapi import APIRouter

router = APIRouter()

FRESHSERVICE_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
FRESHSERVICE_API_KEY = os.getenv("FRESHSERVICE_API_KEY")

@router.post("/create_ticket")
def create_ticket(subject: str, description: str, email: str = "user@example.com"):
    url = f"https://{FRESHSERVICE_DOMAIN}.freshservice.com/api/v2/tickets"

    payload = {
        "subject": subject,
        "description": description,
        "email": email,
        "priority": 1,
        "status": 2
    }

    response = requests.post(
        url,
        json=payload,
        auth=(FRESHSERVICE_API_KEY, "X")
    )

    if response.status_code in [200, 201]:
        ticket = response.json()
        return {
            "success": True,
            "ticket_id": ticket["id"]
        }

    return {
        "success": False,
        "error": response.text,
        "status_code": response.status_code
    }
