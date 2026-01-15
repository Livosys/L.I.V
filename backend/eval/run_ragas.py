from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from datasets import Dataset

from langchain_openai import OpenAIEmbeddings
from eval.embeddings_compat import EmbeddingsCompat
from eval.ragas_adapter import shix_answer


questions = [
    "How do I reset my VPN password?",
    "VPN is not connecting on Windows",
    "How to access a shared mailbox?",
    "Why is my laptop slow?"
]

answers = [shix_answer(q) for q in questions]

dataset = Dataset.from_dict({
    "question": [a["question"] for a in answers],
    "answer": [a["answer"] for a in answers],
    "contexts": [a["contexts"] for a in answers],
})

# 🔑 EXPLICIT embeddings (patched for RAGAS compatibility)
base_embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
embeddings = EmbeddingsCompat(base_embeddings)

result = evaluate(
    dataset,
    metrics=[
        faithfulness,
        answer_relevancy
    ],
    embeddings=embeddings
)

print(result)
