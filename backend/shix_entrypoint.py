from fastapi import FastAPI

from routers.chat import router as chat_router
from routers.kb import router as kb_router
from routers.tickets import router as tickets_router
from routers.rag import router as rag_router

app = FastAPI()

@app.get("/")
def root():
    return {"entrypoint": "OK"}

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/debug")
def debug():
    return {"debug": "OK"}

app.include_router(chat_router, prefix="/api")
app.include_router(kb_router, prefix="/api")
app.include_router(tickets_router, prefix="/api")
app.include_router(rag_router, prefix="/api")
