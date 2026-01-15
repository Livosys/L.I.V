from openai import OpenAI
import os

def answer_query(query: str) -> str:
    try:
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=query,
        )

        return response.output_text

    except Exception as e:
        return f"ERROR_FROM_BACKEND: {repr(e)}"
