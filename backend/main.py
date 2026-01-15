from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/debug")
def debug():
    return {"debug": "OK"}
