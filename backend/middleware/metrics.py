from time import time
from fastapi import Request, Response

REQUEST_COUNT = 0
REQUEST_LATENCY = []

async def metrics_middleware(request: Request, call_next):
    global REQUEST_COUNT
    start = time()
    response: Response = await call_next(request)
    duration = time() - start

    REQUEST_COUNT += 1
    REQUEST_LATENCY.append(duration)

    return response


def metrics_snapshot():
    if REQUEST_LATENCY:
        avg = sum(REQUEST_LATENCY) / len(REQUEST_LATENCY)
    else:
        avg = 0.0

    return {
        "requests_total": REQUEST_COUNT,
        "avg_latency_seconds": round(avg, 6),
    }
