from fastapi import APIRouter
from ingestion.freshservice_sync import ingest_all_freshservice_tickets

router = APIRouter()

@router.post("/sync_freshservice")
def sync_freshservice():
    try:
        result = ingest_all_freshservice_tickets()
        return {
            "message": "Freshservice ingestion completed",
            "total_ingested": result["ingested"]
        }
    except Exception as e:
        return {"error": str(e)}
