from backend.freshservice.writeback import add_note

def propose_change(ticket: dict):
    add_note(ticket["id"], "🔁 Change Request föreslagen baserat på återkommande incident.", True)
    return "change_proposed"
