# SKELETT – kopplas till Neo4j senare
def upsert_ticket_node(ticket: dict):
    return {
        "node": "Ticket",
        "id": ticket.get("ticket_id"),
        "status": "queued"
    }
