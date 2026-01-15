from fastapi import APIRouter
from services.approved_write_executor import execute_approved_writes

router = APIRouter(prefix="/api/writeback", tags=["writeback"])

@router.post("/execute")
def execute():
    return execute_approved_writes()
