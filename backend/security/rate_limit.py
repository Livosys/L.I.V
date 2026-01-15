import time
from fastapi import Request, HTTPException

REQUESTS = {}

def rate_limiter(request: Request):
    ip = request.client.host
    now = time.time()

    window = 60
    limit = 60

    REQUESTS.setdefault(ip, [])
    REQUESTS[ip] = [t for t in REQUESTS[ip] if now - t < window]

    if len(REQUESTS[ip]) >= limit:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    REQUESTS[ip].append(now)
cat << 'EOF' > /opt/shix/backend/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers.rag import router as rag_router
from routers.writeback import router as writeback_router
from security.rate_limit import rate_limiter

app = FastAPI(title="SHIX API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    rate_limiter(request)
    return await call_next(request)

app.include_router(rag_router)
app.include_router(writeback_router)

@app.get("/health")
def health():
    return {"status": "ok"}
