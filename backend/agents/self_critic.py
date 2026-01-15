from rag.llm_client import ask_llm


def critique(answer: str, query: str) -> bool:
    """
    Return True om svaret är tillräckligt bra.
    """
    prompt = f"""
You are a strict ITSM quality reviewer.

Question:
{query}

Answer:
{answer}

Is the answer accurate, complete, and grounded in context?
Reply ONLY with YES or NO.
"""
    result = ask_llm(prompt).strip().upper()
    return result == "YES"
