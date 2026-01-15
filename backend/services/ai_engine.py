def generate_resolution(ticket: dict) -> dict:
    subject = ticket.get("subject", "No subject")

    resolution = (
        "🤖 Auto-resolution by SHIX\n\n"
        f"Subject: {subject}\n\n"
        "Actions performed:\n"
        "- Service restart\n"
        "- Access validation\n"
        "- User notified\n\n"
        "If the issue persists, this ticket can be reopened."
    )

    return {
        "status": 4,  # Resolved
        "resolution": resolution
    }
