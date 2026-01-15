from neo4j import GraphDatabase
import os

URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
USER = os.getenv("NEO4J_USER", "neo4j")
PASSWORD = os.getenv("NEO4J_PASSWORD", "neo4j")

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def upsert_cmdb(ticket_id, ci_id, ci_name, ci_type, sla_name, customer_name):
    cypher = """
    MERGE (ci:CI {id: $ci_id})
    SET ci.name = $ci_name,
        ci.type = $ci_type
    MERGE (t:Ticket {id: $ticket_id})
    MERGE (s:SLA {name: $sla_name})
    MERGE (c:Customer {name: $customer_name})
    MERGE (t)-[:AFFECTS]->(ci)
    MERGE (ci)-[:HAS_SLA]->(s)
    MERGE (ci)-[:USED_BY]->(c)
    """
    with driver.session() as session:
        session.run(
            cypher,
            ticket_id=ticket_id,
            ci_id=ci_id,
            ci_name=ci_name,
            ci_type=ci_type,
            sla_name=sla_name,
            customer_name=customer_name,
        )

def get_ticket_context(ticket_id):
    cypher = """
    MATCH (t:Ticket {id: $id})-[:AFFECTS]->(ci:CI)
    OPTIONAL MATCH (ci)-[:HAS_SLA]->(s:SLA)
    OPTIONAL MATCH (ci)-[:USED_BY]->(c:Customer)
    RETURN ci.id AS ci_id,
           ci.name AS ci_name,
           ci.type AS ci_type,
           s.name AS sla,
           c.name AS customer
    """
    with driver.session() as session:
        result = session.run(cypher, id=ticket_id)
        return [r.data() for r in result]

def get_ci_impact(ticket_id):
    """
    Blast radius:
    Ticket -> CI <- other Tickets
    CI -> Customer
    CI -> SLA
    """
    cypher = """
    MATCH (t:Ticket {id: $id})-[:AFFECTS]->(ci:CI)
    OPTIONAL MATCH (ci)<-[:AFFECTS]-(other:Ticket)
    OPTIONAL MATCH (ci)-[:USED_BY]->(c:Customer)
    OPTIONAL MATCH (ci)-[:HAS_SLA]->(s:SLA)
    RETURN
        ci.id AS ci_id,
        ci.name AS ci_name,
        collect(DISTINCT other.id) AS impacted_tickets,
        collect(DISTINCT c.name) AS customers,
        collect(DISTINCT s.name) AS slas
    """
    with driver.session() as session:
        result = session.run(cypher, id=ticket_id)
        record = result.single()
        return record.data() if record else {}
