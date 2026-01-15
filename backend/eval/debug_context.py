from services.freshservice import get_kb_articles

articles = get_kb_articles(limit=2)

for a in articles:
    print("TITLE:", a.get("title"))
    print("TEXT:")
    print(a.get("description_text", "")[:1000])
    print("-" * 40)
