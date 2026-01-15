def summarize_article(article):
    text = article.get("summary", "")
    if not text:
        return "Ingen text att sammanfatta."

    return (
        "Sammanfattning:\n"
        + text[:500]
    )
