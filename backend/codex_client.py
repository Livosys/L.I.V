import subprocess
import json
import logging

logger = logging.getLogger("codex-client")

def codex_intent(message: str):
    try:
        p = subprocess.run(
            ["codex", "run"],
            input=message,
            text=True,
            capture_output=True,
            timeout=10
        )

        raw = (p.stdout or "").strip()

        if not raw:
            logger.error("Codex returned empty stdout")
            return {
                "intent": "UNKNOWN",
                "error": "empty_codex_response"
            }

        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            logger.error("Invalid JSON from Codex: %s", raw)
            return {
                "intent": "UNKNOWN",
                "error": "invalid_json"
            }

    except Exception as e:
        logger.exception("Codex execution failed")
        return {
            "intent": "UNKNOWN",
            "error": "codex_exception"
        }
