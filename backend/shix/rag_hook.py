def build_rag_document(ticket: dict) -> dict:
    text = f"""
    Title: {ticket.get('title')}
    Description: {ticket.get('description')}
    Status: {ticket.get('status')}
    Priority: {ticket.get('priority')}
    """

    for n in ticket.get("notes", []):
        text += f"\nNOTE: {n.get('body')}"

    return {
        "id": ticket.get("ticket_id"),
        "text": text.strip(),
        "metadata": {
            "priority": ticket.get("priority"),
            "status": ticket.get("status"),
            "tags": ticket.get("tags", [])
        }
    }
