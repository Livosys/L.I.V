REQUIRED_FIELDS = [
    "ticket_id",
    "title",
    "description",
    "status",
    "priority"
]

def quality_score(ticket: dict) -> dict:
    present = 0
    missing = []

    for f in REQUIRED_FIELDS:
        if ticket.get(f):
            present += 1
        else:
            missing.append(f)

    score = round(present / len(REQUIRED_FIELDS), 2)

    return {
        "score": score,
        "missing_fields": missing
    }
