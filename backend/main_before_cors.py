from fastapi import FastAPI

from routers.freshservice_router import router as freshservice_router
from routers.rag_router import router as rag_router

app = FastAPI(title="SHIX Backend")

@app.get("/")
def root():
    return {"status": "SHIX Backend running"}

@app.get("/health")
def health():
    return {"status": "ok", "service": "shix"}

app.include_router(freshservice_router)
app.include_router(rag_router)
