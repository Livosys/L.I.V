def format_kb_articles_structured(articles: list, domain: str, workspace_id: str = None):
    results = []

    base = f"https://{domain}"
    if workspace_id:
        base += f"/a/solutions/workspaces/{workspace_id}"

    for a in articles:
        article_id = a.get("id")
        title = a.get("title", "Utan titel")
        description = (a.get("description") or "").strip()

        results.append({
            "citation_id": f"KB-{article_id}",
            "article_id": article_id,
            "title": title,
            "excerpt": description[:240] + ("…" if len(description) > 240 else ""),
            "url": f"{base}/articles/{article_id}",
            "source": "freshservice"
        })

    return results
