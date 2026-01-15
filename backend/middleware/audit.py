import time
from fastapi import Request

async def audit_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start

    with open("/var/log/shix_audit.log", "a") as f:
        f.write(
            f"{request.client.host} "
            f"{request.method} "
            f"{request.url.path} "
            f"{response.status_code} "
            f"{duration:.3f}s\n"
        )
    return response
