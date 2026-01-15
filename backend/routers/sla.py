from fastapi import APIRouter, Depends
from agents.sla_agent import sla_risk
from security.azure_ad import require_role

router = APIRouter(prefix="/api/sla", tags=["sla"])

@router.post("/risk")
def check_sla(
    payload: dict,
    user=Depends(require_role("agent"))
):
    return {
        "sla_risk": sla_risk(payload.get("ticket", {}))
    }
