LIST_TICKETS = "LIST_TICKETS"
OPEN_TICKET = "OPEN_TICKET"
HELP = "HELP"
UNKNOWN = "UNKNOWN"

def parse_intent(message: str):
    if not message:
        return {"intent": UNKNOWN, "params": {}}

    text = message.lower().strip()

    # NORMALISERA (TA BORT UTFYLLNADSORD)
    REPLACE = [
        "alla",
        "mig",
        "mina"
    ]
    for w in REPLACE:
        text = text.replace(w, "").strip()

    # LISTA ÄRENDEN – ALLA VARIANTER
    if text in [
        "ärenden",
        "ärende",
        "visa ärenden",
        "visa ärende"
    ]:
        return {"intent": LIST_TICKETS, "params": {}}

    # ÖPPNA ÄRENDE VIA SIFFRA
    for token in text.split():
        if token.isdigit():
            return {
                "intent": OPEN_TICKET,
                "params": {"id": int(token)}
            }

    if text in ["hjälp", "help", "?"]:
        return {"intent": HELP, "params": {}}

    return {"intent": UNKNOWN, "params": {}}
