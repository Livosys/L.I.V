from rag.neo4j_client import get_ci_impact

def analyze_impact(ticket_id: int):
    """
    Root cause + blast radius analysis
    """
    impact = get_ci_impact(ticket_id)

    if not impact:
        return {
            "ticket_id": ticket_id,
            "status": "no_ci_found"
        }

    return {
        "ticket_id": ticket_id,
        "root_ci": {
            "id": impact.get("ci_id"),
            "name": impact.get("ci_name"),
        },
        "blast_radius": {
            "impacted_tickets": impact.get("impacted_tickets", []),
            "customers": impact.get("customers", []),
            "slas": impact.get("slas", []),
        }
    }
