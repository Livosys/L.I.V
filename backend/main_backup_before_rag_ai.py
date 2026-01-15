from fastapi import FastAPI
app=FastAPI()
@app.post("/chat")
def chat(m:dict): return {"reply":"OK"}