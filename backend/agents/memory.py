from backend.utils.redis_client import r
import json

def _key(ticket_id: int):
    return f"ticket:{ticket_id}:memory"

def get_memory(ticket_id: int):
    data = r.lrange(_key(ticket_id), 0, -1)
    return [json.loads(x) for x in data]

def add_memory(ticket_id: int, role: str, content: str):
    r.rpush(
        _key(ticket_id),
        json.dumps({"role": role, "content": content})
    )
    r.expire(_key(ticket_id), 86400)
