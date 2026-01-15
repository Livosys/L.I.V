def ragas_payload(question, context, answer):
    return {
        "question": question,
        "contexts": context,
        "answer": answer,
    }
