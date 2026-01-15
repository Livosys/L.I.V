import requests

DOMAIN = "https://schema.freshservice.com"
KEY = "mhxrZr8PrmXdSWqQyBBs"

r = requests.get(
    f"{DOMAIN}/api/v2/tickets?per_page=50",
    auth=(KEY, "X"),
    headers={
        "Accept": "application/json",
        "User-Agent": "SHIX-RAG"
    },
    timeout=30
)

print("STATUS:", r.status_code)
print("HEADERS:", r.headers.get("content-type"))
print("BODY PREVIEW:", r.text[:200])

r.raise_for_status()
data = r.json()

tickets = data.get("tickets", [])
docs = []

for t in tickets:
    docs.append(
        f"{t.get('subject','')} {t.get('description','')}"
    )

print("TICKETS FOUND:", len(docs))

# Dummy embed markering (kopplas till din embedder sen)
if not docs:
    print("⚠️ No tickets yet – RAG empty by design")
else:
    print("✅ Ready to embed")
