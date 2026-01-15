import time
from collections import defaultdict

WINDOW = 60
MAX_REQ = 30
_hits = defaultdict(list)

def allow(ip: str) -> bool:
    now = time.time()
    _hits[ip] = [t for t in _hits[ip] if now - t < WINDOW]
    if len(_hits[ip]) >= MAX_REQ:
        return False
    _hits[ip].append(now)
    return True
