from config.features import FEATURE_RAG

def _fallback():
    return [
        {
            "title": "VPN – Installation Guide",
            "category": "VPN",
            "summary": "Step-by-step guide for installing VPN on Windows and macOS.",
            "url": "https://livosys.freshservice.com/a/solutions/articles/58000003580",
            "score": 1.0,
            "actions": {"open_kb": "https://livosys.freshservice.com/a/solutions/articles/58000003580"}
        }
    ]

def search_kb(query: str, category: str | None = None):
    if not FEATURE_RAG:
        results = _fallback()
    else:
        try:
            from rag.vector_store import search
            vec = [0.1] * 384  # måste matcha index-dim
            results = search(vec)
        except Exception:
            results = []

    # kategori-filter
    if category:
        results = [r for r in results if r.get("category") == category]

    # säkerställ actions
    for r in results:
        r.setdefault("actions", {})["open_kb"] = r.get("url")

    return results
