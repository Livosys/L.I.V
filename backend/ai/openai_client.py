import os

def get_client():
    """
    Lazy OpenAI client factory.
    This is a safe placeholder so RAG can import without crashing.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    # Placeholder object – actual client can be injected later
    return {
        "provider": "openai",
        "api_key_present": True
    }
