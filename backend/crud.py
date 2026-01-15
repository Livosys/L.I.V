from sqlalchemy.orm import Session
from db import Ticket

def create_ticket(db: Session, subject: str, status: str):
    ticket = Ticket(subject=subject, status=status)
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

def get_all_tickets(db: Session):
    return db.query(Ticket).all()

def delete_ticket(db: Session, ticket_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        return None
    db.delete(ticket)
    db.commit()
    return ticket
