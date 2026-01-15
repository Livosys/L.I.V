from fastapi import APIRouter
from sla.rag_sla import predict_sla

router = APIRouter(prefix="/api/sla", tags=["sla"])

@router.post("/predict")
def predict(payload: dict):
    return predict_sla(payload["ticket"], payload.get("tenant","default"))
