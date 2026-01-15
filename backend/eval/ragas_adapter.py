from agents.enterprise_agent import enterprise_answer

def shix_answer(question: str):
    result = enterprise_answer(question)

    sources = result.get("sources", [])

    contexts = []
    for src in sources:
        if isinstance(src, dict):
            if "content" in src:
                contexts.append(src["content"])
            elif "title" in src:
                contexts.append(src["title"])

    return {
        "question": question,
        "answer": result.get("answer", ""),
        "contexts": contexts
    }
