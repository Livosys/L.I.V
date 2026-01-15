def analyze_ticket(ticket: dict) -> dict:
    text = f"{ticket.get('title','')} {ticket.get('description','')}".lower()

    risk = "low"
    if ticket.get("created_at") and ticket.get("updated_at"):
        risk = "medium"

    if any(k in text for k in ["down", "offline", "vpn", "network"]):
        risk = "high"

    category_hint = "general"
    if "vpn" in text or "network" in text:
        category_hint = "network"

    summary = ticket.get("description", "")[:300]

    return {
        "summary": summary,
        "risk": risk,
        "category_hint": category_hint,
        "confidence": 0.85
    }
