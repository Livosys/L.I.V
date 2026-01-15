import subprocess
import json
import logging
import os
import tempfile

log = logging.getLogger("intent")

CODEX_HOME = "/opt/shix/codexhome"
SCHEMA_PATH = "/opt/shix/codexhome/intent_schema.json"

FALLBACK = {
    "intent": "UNKNOWN",
    "filters": {},
    "value": None,
    "confidence": 0.0
}

def classify_intent(user_text: str) -> dict:
    env = os.environ.copy()
    env["CODEX_HOME"] = CODEX_HOME

    try:
        with tempfile.NamedTemporaryFile(mode="r+", delete=False) as out:
            out_path = out.name

        cmd = [
            "codex", "exec",
            "--skip-git-repo-check",
            "--sandbox", "read-only",
            "--output-schema", SCHEMA_PATH,
            "--output-last-message", out_path,
            user_text
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60, env=env)

        if result.returncode != 0:
            log.error("Codex exec error: %s", result.stderr)
            return FALLBACK

        with open(out_path, "r", encoding="utf-8") as f:
            text = f.read().strip()

        try:
            return json.loads(text)
        except Exception:
            log.error("Codex returned non-JSON: %s", text)
            return FALLBACK

    except Exception:
        log.exception("Intent classification crashed")
        return FALLBACK
