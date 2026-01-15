import time

_requests = {}

def allow(ip, limit=30, window=60):
    now = time.time()
    bucket = _requests.setdefault(ip, [])
    bucket[:] = [t for t in bucket if now - t < window]
    if len(bucket) >= limit:
        return False
    bucket.append(now)
    return True
