from freshservice.ticket_client import list_tickets

def dispatch(intent, message):
    if intent == "LIST_TICKETS":
        data = list_tickets()
        return {
            "answer": "Här är dina ärenden",
            "data": data.get("tickets", [])
        }

    return {"answer": "Okänt kommando"}
