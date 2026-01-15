# Enkel, tenant-säker sessionsmemory (RAM)

SESSION_MEMORY = {}

def get_session(tenant_id: str, session_id: str):
    key = f"{tenant_id}:{session_id}"
    return SESSION_MEMORY.setdefault(key, {
        "messages": [],
        "context": {}
    })

def set_context(tenant_id: str, session_id: str, key: str, value):
    session = get_session(tenant_id, session_id)
    session["context"][key] = value

def get_context(tenant_id: str, session_id: str, key: str):
    return get_session(tenant_id, session_id)["context"].get(key)
