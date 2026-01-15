import json
from pathlib import Path
from typing import List

from services.freshservice_client import get_ticket

STATE_DIR = Path("/home/shix.livosys.se/backend/state")
STATE_DIR.mkdir(parents=True, exist_ok=True)
STATE_FILE = STATE_DIR / "last_ticket_id.json"

MAX_ID_CHECKS_PER_RUN = 10   # safety brake

STATUS_MAP = {
    "open": 2,
    "pending": 3,
    "resolved": 4,
    "closed": 5,
}

def _load_last_id() -> int:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text()).get("last_id", 0)
    return 0

def _save_last_id(last_id: int):
    STATE_FILE.write_text(json.dumps({"last_id": last_id}))

def fetch_next_tickets(max_items: int = 3, only_status: str = "closed") -> dict:
    """
    CONTROLLED ID FETCH – SAFE RAMP-UP
    """
    last_id = _load_last_id()
    checked = 0
    returned: List[dict] = []

    target_status = STATUS_MAP.get(only_status)

    current_id = last_id

    while checked < MAX_ID_CHECKS_PER_RUN and len(returned) < max_items:
        current_id += 1
        checked += 1

        try:
            ticket = get_ticket(current_id)
        except Exception:
            continue

        if not ticket:
            continue

        if target_status and ticket.get("status") != target_status:
            continue

        returned.append(ticket)

    _save_last_id(current_id)

    return {
        "safe": True,
        "strategy": "controlled_id",
        "requested_max": max_items,
        "checked_ids": checked,
        "last_cursor": current_id,
        "returned": len(returned),
        "tickets": returned,
    }
