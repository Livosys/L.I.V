from audit.logger import log_event

def log_rag_eval(query, context, answer, sources):
    log_event({
        "type": "rag_eval",
        "query": query,
        "context": context,
        "answer": answer,
        "sources": sources
    })
