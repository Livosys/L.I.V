class EmbeddingsCompat:
    def __init__(self, embeddings):
        self.embeddings = embeddings

    def embed_query(self, text: str):
        # RAGAS expects this
        return self.embeddings.embed_documents([text])[0]

    def embed_documents(self, texts):
        return self.embeddings.embed_documents(texts)
