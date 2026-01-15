import json
from pathlib import Path
from uuid import uuid4

STORE = Path("/opt/shix/data/approvals")
STORE.mkdir(parents=True, exist_ok=True)

def create_approval(ticket_id: int, proposal: str):
    approval_id = str(uuid4())
    record = {
        "id": approval_id,
        "ticket_id": ticket_id,
        "proposal": proposal,
        "status": "pending"
    }

    with open(STORE / f"{approval_id}.json", "w") as f:
        json.dump(record, f)

    return record
