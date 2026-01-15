from fastapi import Header, HTTPException
import os

API_TOKEN = os.getenv("SHIX_API_TOKEN")

def require_token(x_api_token: str = Header(None)):
    if not API_TOKEN or x_api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
