def plan(message: str, context: dict) -> str:
    msg = message.lower()

    if "ticket" in msg or "ärende" in msg:
        return "fetch_tickets"

    if "kunskap" in msg or "kb" in msg or "artikel" in msg:
        return "fetch_kb"

    if "guida" in msg:
        return context.get("last_action", "chat")

    return "chat"

def is_vpn_guide_request(message: str) -> bool:
    return "vpn" in message.lower() and any(
        k in message.lower() for k in ["guide", "hur", "hjälp", "steg"]
    )
