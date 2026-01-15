def present_for_ui(shix_payload: dict) -> dict:
    ticket = shix_payload.get("ticket", {})
    analysis = shix_payload.get("analysis", {})
    quality = shix_payload.get("quality", {})

    return {
        "id": ticket.get("ticket_id"),
        "title": ticket.get("title"),
        "description": ticket.get("description"),
        "status": ticket.get("status"),
        "priority": ticket.get("priority"),
        "tags": ticket.get("tags", []),

        "summary": analysis.get("summary"),
        "risk": analysis.get("risk"),
        "category_hint": analysis.get("category_hint"),

        "quality_score": quality.get("score"),
        "missing_fields": quality.get("missing_fields"),

        "notes": ticket.get("notes", [])
    }
