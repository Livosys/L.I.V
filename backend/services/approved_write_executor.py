from services.approval_service import list_approved
from freshservice.writeback import add_note

ALLOWED_DECISIONS = {
    "RECOMMEND_INTERNAL_NOTE",
    "RECOMMEND_ESCALATION"
}

def execute_approved_writes():
    executed = []

    for a in list_approved():
        if a["decision"] not in ALLOWED_DECISIONS:
            continue

        add_note(
            a["ticket_id"],
            f"🤖 SHIX approved action: {a['decision']} – {a['reason']}",
            private=True
        )

        executed.append(a)

    return executed
