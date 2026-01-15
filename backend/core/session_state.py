from typing import Dict

_sessions: Dict[str, Dict] = {}

def get_state(session_id: str) -> Dict:
    return _sessions.get(session_id, {})

def set_state(session_id: str, **kwargs):
    state = _sessions.get(session_id, {})
    state.update(kwargs)
    _sessions[session_id] = state
    return state

def clear_state(session_id: str):
    _sessions.pop(session_id, None)
