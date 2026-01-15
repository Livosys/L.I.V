from fastapi import APIRouter
import os
import requests

router = APIRouter(prefix="/api/fresh", tags=["Freshservice"])

@router.get("/tickets")
def get_tickets():
    domain = os.getenv("FRESHSERVICE_DOMAIN")
    key = os.getenv("FRESHSERVICE_API_KEY")

    r = requests.get(
        f"https://{domain}/api/v2/tickets",
        auth=(key, "X"),
        timeout=10,
    )

    r.raise_for_status()
    return r.json()
