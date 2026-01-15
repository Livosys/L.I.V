def plan(message: str):
    if "ticket" in message:
        return "fetch_tickets"
    return "chat"

def act(plan: str, context: dict):
    return context

def respond(answer: str):
    return answer
