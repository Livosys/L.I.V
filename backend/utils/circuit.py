import time

FAILURES = {}
THRESHOLD = 3
RESET_AFTER = 60

def allow(name: str):
    f = FAILURES.get(name)
    if not f:
        return True
    if f["count"] < THRESHOLD:
        return True
    return (time.time() - f["time"]) > RESET_AFTER

def record_failure(name: str):
    FAILURES.setdefault(name, {"count":0,"time":time.time()})
    FAILURES[name]["count"] += 1
    FAILURES[name]["time"] = time.time()
