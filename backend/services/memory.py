SESSION = {}

def get(session_id: str):
    return SESSION.setdefault(session_id, {})

def set(session_id: str, key: str, value):
    SESSION.setdefault(session_id, {})[key] = value
