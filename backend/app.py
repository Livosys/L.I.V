from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"root": "OK"}

@app.get("/health")
def health():
    return {"health": "OK"}

@app.get("/debug")
def debug():
    return {"debug": "OK"}
