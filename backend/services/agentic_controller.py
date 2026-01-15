import os
from typing import Dict

ENABLE_AGENTIC = os.getenv("ENABLE_AGENTIC", "false") == "true"

class AgenticController:
    def __init__(self, ai_pipeline):
        self.ai = ai_pipeline
        self.enabled = ENABLE_AGENTIC

    def handle(self, query: str, context: str = "") -> Dict:
        if not self.enabled:
            # Fallback: normal AI
            return self.ai.ask(query=query, context=context)

        # 1️⃣ Classify
        classification = self._classify(query, context)

        # 2️⃣ Resolve
        resolution = self._resolve(query, context, classification)

        # 3️⃣ (Future) KB write-back
        return {
            "success": True,
            "classification": classification,
            "answer": resolution.get("answer"),
            "model": resolution.get("model"),
            "agentic": True
        }

    def _classify(self, query: str, context: str) -> Dict:
        prompt = f"""
Classify the following IT issue.

Return JSON with:
- category
- urgency
- confidence

Issue:
{query}
"""
        result = self.ai.ask(prompt, context)
        return {
            "raw": result.get("answer"),
            "category": "network",
            "urgency": "medium",
            "confidence": 0.7
        }

    def _resolve(self, query: str, context: str, classification: Dict) -> Dict:
        enriched_context = f"""
Classification:
{classification}

Original context:
{context}
"""
        return self.ai.ask(query=query, context=enriched_context)
