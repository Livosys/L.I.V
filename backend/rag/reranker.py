def cosine(a,b):
    s = sum(x*y for x,y in zip(a,b))
    na = sum(x*x for x in a) ** 0.5
    nb = sum(x*x for x in b) ** 0.5
    return s / (na*nb + 1e-9)

def rerank(query_emb, rows, k=3):
    rows.sort(key=lambda r: cosine(query_emb, r["emb"]), reverse=True)
    return rows[:k]
