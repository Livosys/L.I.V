from fastapi import APIRouter
from routers.tickets import list_tickets
from audit.stats import intent_stats

router = APIRouter()

@router.get("/dashboard")
def dashboard():
    tickets = list_tickets()["tickets"]
    sla = {
        "ok": sum(1 for t in tickets if t["sla_status"] == "ok"),
        "at_risk": sum(1 for t in tickets if t["sla_status"] == "at_risk"),
        "breached": sum(1 for t in tickets if t["sla_status"] == "breached"),
    }

    return {
        "tickets_total": len(tickets),
        "sla": sla,
        "intent_stats": intent_stats()
    }
