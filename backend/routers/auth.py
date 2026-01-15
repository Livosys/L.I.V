from fastapi import APIRouter
import jwt

router = APIRouter(prefix="/auth", tags=["auth"])
SECRET = "SHIX_SECRET_KEY"

@router.post("/login")
def login(username: str, role: str):
    token = jwt.encode(
        {"user": username, "role": role},
        SECRET,
        algorithm="HS256"
    )
    return {"access_token": token}
