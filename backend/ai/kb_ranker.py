def rank_articles(articles: list, query: str) -> list:
    q = query.lower()

    def rank(a):
        text = (a.get("title","") + " " + a.get("description","")).lower()
        return text.count(q)

    return sorted(articles, key=rank, reverse=True)
