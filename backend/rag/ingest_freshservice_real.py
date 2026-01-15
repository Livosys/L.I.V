import os
import pickle
import requests
from typing import List
from rag.embedding import embed_texts

VECTOR_DIR = "/opt/shix/data/vectors"
META_FILE = f"{VECTOR_DIR}/meta.pkl"

FRESHSERVICE_DOMAIN = os.environ["FRESHSERVICE_DOMAIN"]
FRESHSERVICE_API_KEY = os.environ["FRESHSERVICE_API_KEY"]

BASE_URL = f"https://{FRESHSERVICE_DOMAIN}.freshservice.com/api/v2"


def get_kb_articles() -> List[dict]:
    url = f"{BASE_URL}/solutions/articles"
    r = requests.get(url, auth=(FRESHSERVICE_API_KEY, "X"))
    r.raise_for_status()
    return r.json().get("articles", [])


def ingest():
    os.makedirs(VECTOR_DIR, exist_ok=True)

    meta = []
    texts = []

    articles = get_kb_articles()

    for article in articles:
        text = article.get("description_text") or ""
        if not text.strip():
            continue

        url = f"https://{FRESHSERVICE_DOMAIN}.freshservice.com/a/solutions/articles/{article['id']}"

        texts.append(text)
        meta.append({
            "text": text,
            "source": url
        })

        print("Ingesting:", article.get("title"))

    if not texts:
        print("No articles ingested")
        return

    embeddings = embed_texts(texts)

    with open(META_FILE, "wb") as f:
        pickle.dump(meta, f)

    print(f"✅ Ingested {len(meta)} Freshservice KB articles")


if __name__ == "__main__":
    ingest()
