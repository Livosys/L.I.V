from fastapi import APIRouter

router = APIRouter(tags=["Ops"])

@router.get("/ready")
def ready():
    return {"ready": True}
