from backend.rag.metrics import *

def evaluate(question, context, answer):
    return {
        "faithfulness": faithfulness(context, answer),
        "relevance": relevance(question, answer),
        "context_precision": context_precision(context),
        "context_recall": context_recall(context),
    }
