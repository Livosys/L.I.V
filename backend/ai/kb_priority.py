def prioritize_articles(articles: list, query_stats: dict) -> list:
    def score(a):
        title = a.get("title", "").lower()
        return sum(v for k, v in query_stats.items() if k in title)

    return sorted(articles, key=score, reverse=True)
