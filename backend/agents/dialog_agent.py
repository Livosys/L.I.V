from backend.agents.tools import tool_get_ticket, tool_sla, tool_rag
from backend.agents.memory import get_memory, add_memory

def dialog_agent(ticket_id: int, user_message: str):
    add_memory(ticket_id, "user", user_message)

    ticket = tool_get_ticket(ticket_id)
    sla = tool_sla(ticket)
    rag = tool_rag(ticket)

    response_text = f"SLA-risk: {sla}. Rekommenderad åtgärd: verifiera och följ KB."

    add_memory(ticket_id, "assistant", response_text)

    return {
        "ticket_id": ticket_id,
        "memory": get_memory(ticket_id),
        "response": response_text
    }
