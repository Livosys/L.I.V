import json
import redis
import os

REDIS_TTL_SECONDS = 3600  # 1 timme (GDPR-friendly)

r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    decode_responses=True
)

def _key(tenant_id: str, session_id: str):
    return f"shix:{tenant_id}:{session_id}"

def load_session(tenant_id: str, session_id: str):
    data = r.get(_key(tenant_id, session_id))
    if not data:
        return {"messages": [], "context": {}}
    return json.loads(data)

def save_session(tenant_id: str, session_id: str, session: dict):
    r.setex(
        _key(tenant_id, session_id),
        REDIS_TTL_SECONDS,
        json.dumps(session)
    )
