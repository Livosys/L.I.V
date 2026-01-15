import os
from freshservice.kb_client import get_kb_articles
from rag.embeddings_engine import embed
from rag.vector_store import add
from services.audit_log import audit_log

TENANT_ID = os.getenv("TENANT_ID", "unknown")

def clean(text: str) -> str:
    return (
        text.replace("<br>", "\n")
            .replace("<br/>", "\n")
            .replace("&nbsp;", " ")
            .strip()
    )

def run():
    try:
        articles = get_kb_articles()
    except Exception as e:
        audit_log(
            "kb_ingest_failed",
            tenant=TENANT_ID,
            error=str(e)
        )
        print("❌ KB ingest failed – permissions issue")
        return  # 🔥 IMPORTANT: do not crash cron

    audit_log("kb_ingest_start", tenant=TENANT_ID, count=len(articles))

    for art in articles:
        text = clean(art.get("description", ""))
        if not text:
            continue

        source = f"kb:{art.get('id')}"
        emb = embed(text)
        add(emb, text, source)

        audit_log(
            "kb_article_ingested",
            tenant=TENANT_ID,
            source=source
        )

    audit_log("kb_ingest_complete", tenant=TENANT_ID)

if __name__ == "__main__":
    run()
