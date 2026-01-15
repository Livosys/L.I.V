from typing import Dict, Any

SESSIONS: Dict[str, Dict[str, Any]] = {}

def get_session(user_id: str) -> Dict[str, Any]:
    if user_id not in SESSIONS:
        SESSIONS[user_id] = {
            "last_intent": None,
            "last_ticket_id": None,
            "last_results": None,
        }
    return SESSIONS[user_id]

def update_session(user_id: str, **kwargs):
    session = get_session(user_id)
    session.update(kwargs)
