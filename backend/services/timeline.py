from services.audit import log_action

def log_ai_action(user: str, ticket_id: int, action: str, content: str):
    resource = f"ticket:{ticket_id}"
    log_action(
        user=user,
        action=action,
        resource=resource,
        details=content
    )
