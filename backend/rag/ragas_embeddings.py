from langchain_openai import OpenAIEmbeddings

class RagasOpenAIEmbeddings:
    def __init__(self, model: str = "text-embedding-3-small"):
        self._emb = OpenAIEmbeddings(model=model)

    def embed_query(self, text: str):
        # RAGAS expects this exact method
        return self._emb.embed_documents([text])[0]
