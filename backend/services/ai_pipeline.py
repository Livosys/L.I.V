import os
from openai import OpenAI

class AIPipeline:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")

        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv("AI_MODEL", "gpt-4o-mini")

    def ask(self, prompt: str, context: str):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": context}
            ]
        )

        return {
            "success": True,
            "answer": response.choices[0].message.content,
            "model": self.model
        }
