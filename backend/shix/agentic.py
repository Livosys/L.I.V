from shix.assembler import assemble_ticket
from shix.analysis import analyze_ticket
from shix.quality import quality_score
from shix.presenter import present_for_ui
from shix.rag_hook import build_rag_document
from shix.sla_agent import sla_assess

def run_shix(ticket_id: int) -> dict | None:
    ticket = assemble_ticket(ticket_id)
    if not ticket:
        return None

    analysis = analyze_ticket(ticket)
    quality = quality_score(ticket)
    sla = sla_assess(ticket)
    rag_doc = build_rag_document(ticket)

    payload = {
        "ticket": ticket,
        "analysis": analysis,
        "quality": quality,
        "sla": sla,
        "rag_document": rag_doc
    }

    return present_for_ui(payload)
