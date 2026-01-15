from fastapi import APIRouter
from routes.create_ticket import create_ticket

router = APIRouter()

@router.get("/")
def root():
    return {"message": "SHIX Backend Running"}

@router.post("/create_ticket")
def create_ticket_route(data: dict):
    return create_ticket(data)
