from fastapi import APIRouter
from change.kpi import summary

router = APIRouter()

@router.get("/api/kpi/change")
def change_kpi():
    return summary()
