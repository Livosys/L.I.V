// === CMDB V1 (minimal, säker) ===

// Nodes
MERGE (ci:CI {id: $ci_id})
SET ci.name = $ci_name,
    ci.type = $ci_type

MERGE (t:Ticket {id: $ticket_id})

MERGE (s:SLA {name: $sla_name})

MERGE (c:Customer {name: $customer_name})

// Relations
MERGE (t)-[:AFFECTS]->(ci)
MERGE (ci)-[:HAS_SLA]->(s)
MERGE (ci)-[:USED_BY]->(c)
