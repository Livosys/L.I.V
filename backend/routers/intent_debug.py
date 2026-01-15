from fastapi import APIRouter
import subprocess
import json
import os
import tempfile

router = APIRouter()

CODEX_HOME = "/opt/shix/codexhome"
SCHEMA_PATH = "/opt/shix/codexhome/intent_schema.json"

@router.post("/api/intent_debug")
def intent_debug(payload: dict):
    message = payload.get("message", "")

    with tempfile.NamedTemporaryFile(mode="r+", delete=False) as out:
        out_path = out.name

    env = os.environ.copy()
    env["CODEX_HOME"] = CODEX_HOME

    cmd = [
        "codex", "exec",
        "--skip-git-repo-check",
        "--sandbox", "read-only",
        "--output-schema", SCHEMA_PATH,
        "--output-last-message", out_path,
        message
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60, env=env)

    if result.returncode != 0:
        return {"ok": False, "stderr": result.stderr, "stdout": result.stdout}

    try:
        with open(out_path, "r", encoding="utf-8") as f:
            text = f.read().strip()
        data = json.loads(text)
    except Exception:
        return {"ok": False, "stderr": "Codex returned non-JSON output", "stdout": text}

    return {"ok": True, "intent": data}
