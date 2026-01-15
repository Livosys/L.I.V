from fastapi import APIRouter
from freshservice.ticket_bundle import get_full_ticket_context

router = APIRouter()

@router.get("/api/tickets/{ticket_id}/full")
def get_ticket_full(ticket_id: int):
    data = get_full_ticket_context(ticket_id)

    ticket = data["ticket"]
    requester = data["requester"]
    sla = data["sla"]

    return {
        "ticket": {
            "id": ticket["id"],
            "subject": ticket.get("subject"),
            "description": ticket.get("description_text"),
            "status": ticket.get("status"),
            "priority": ticket.get("priority"),
            "category": ticket.get("category"),
            "subcategory": ticket.get("sub_category"),
            "item": ticket.get("item_category"),
            "created_at": ticket.get("created_at"),
            "updated_at": ticket.get("updated_at")
        },
        "requester": {
            "name": f'{requester.get("first_name")} {requester.get("last_name")}',
            "email": requester.get("email"),
            "job_title": requester.get("job_title"),
            "department": requester.get("department_names"),
            "location": requester.get("location_name"),
            "vip": requester.get("vip_user")
        },
        "sla": sla,
        "last_public_reply": data["last_public_reply"],
        "last_internal_note": data["last_internal_note"]
    }
