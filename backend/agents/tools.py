from backend.freshservice.client import get_ticket
from backend.agents.sla_agent import sla_risk
from backend.agents.rag_agent import rag_answer

def tool_get_ticket(ticket_id: int):
    return get_ticket(ticket_id).get("ticket", {})

def tool_sla(ticket: dict):
    return sla_risk(ticket)

def tool_rag(ticket: dict):
    return rag_answer(ticket)
