from fastapi import Header, HTTPException, status
import os

API_TOKEN = os.getenv("SHIX_API_TOKEN", "ADMIN_TOKEN_123")

def require_token(x_api_token: str = Header(...)):
    if x_api_token != API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API token"
        )
