import requests
from ingestion.ingest import ingest_text
import os

FRESH_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
API_KEY = os.getenv("FRESHSERVICE_API_KEY")

BASE_URL = f"https://{FRESH_DOMAIN}/api/v2/solutions/articles"

def fetch_articles():
    articles = []
    page = 1

    while True:
        url = f"{BASE_URL}?page={page}&per_page=30"
        print(f"Fetching page {page}...")

        r = requests.get(url, auth=(API_KEY, "X"))

        if r.status_code != 200:
            print("Error fetching:", r.text)
            break

        data = r.json()

        if "articles" not in data or len(data["articles"]) == 0:
            break

        articles.extend(data["articles"])
        page += 1

    return articles

def ingest_freshservice_kb():
    articles = fetch_articles()
    print(f"Fetched {len(articles)} articles.")

    ids = []

    for art in articles:
        title = art.get("title", "")
        desc = art.get("description", "")

        text = f"{title}\n\n{desc}"

        doc_id = ingest_text(text)
        ids.append(doc_id)

        print(f"Ingested article {art['id']} → {doc_id}")

    return ids
