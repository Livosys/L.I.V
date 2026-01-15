from freshservice.ticket_client import get_ticket_by_id
from freshservice.requester_client import get_requester_by_id
from freshservice.sla_client import get_ticket_sla
from freshservice.conversation_client import get_ticket_conversations

def get_full_ticket_context(ticket_id: int):
    ticket = get_ticket_by_id(ticket_id)

    requester = get_requester_by_id(ticket["requester_id"])
    sla = get_ticket_sla(ticket_id)
    conversations = get_ticket_conversations(ticket_id)

    last_public = next(
        (c for c in conversations if c.get("public")), None
    )
    last_private = next(
        (c for c in conversations if not c.get("public")), None
    )

    return {
        "ticket": ticket,
        "requester": requester,
        "sla": sla,
        "last_public_reply": last_public,
        "last_internal_note": last_private
    }
