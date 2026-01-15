from backend.freshservice.writeback import add_note

def auto_resolve(ticket: dict):
    add_note(
        ticket["id"],
        "✅ Ärendet markerat som löst enligt standardlösning.",
        private=False
    )
    return "resolved"
