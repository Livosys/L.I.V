from fastapi import Request, HTTPException
import time

RATE = {}

def rate_limit(request: Request, limit=60):
    ip = request.client.host
    now = time.time()

    hits = RATE.get(ip, [])
    hits = [t for t in hits if now - t < 60]

    if len(hits) >= limit:
        raise HTTPException(status_code=429, detail="Too many requests")

    hits.append(now)
    RATE[ip] = hits
