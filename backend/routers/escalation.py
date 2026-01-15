from fastapi import APIRouter, Depends
from agents.sla_agent import sla_risk
from security.azure_ad import require_role

router = APIRouter(prefix="/api/escalation", tags=["escalation"])

@router.post("/check")
def check_escalation(
    payload: dict,
    user=Depends(require_role("agent"))
):
    risk = sla_risk(payload.get("ticket", {}))
    return {
        "escalate": risk.get("risk") in ("high", "critical"),
        "sla_risk": risk
    }
