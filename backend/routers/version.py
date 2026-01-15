from fastapi import APIRouter

router = APIRouter()

@router.get("/version")
def version():
    return {"version": "1.0.0"}
