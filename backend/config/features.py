import os

FEATURE_FRESHSERVICE = os.getenv("FEATURE_FRESHSERVICE", "false").lower() == "true"
FEATURE_RAG = os.getenv("FEATURE_RAG", "false").lower() == "true"
