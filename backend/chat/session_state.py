SESSION_STATE = {}

def get_state(session_id: str):
    return SESSION_STATE.get(session_id, {})

def set_state(session_id: str, state: dict):
    SESSION_STATE[session_id] = state

def clear_state(session_id: str):
    SESSION_STATE.pop(session_id, None)
