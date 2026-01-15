import hmac
import hashlib
import os

SECRET = os.getenv("FRESHSERVICE_WEBHOOK_SECRET", "").encode()

def verify_signature(body: bytes, signature: str | None) -> bool:
    if not SECRET or not signature:
        return False

    digest = hmac.new(
        SECRET,
        body,
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(digest, signature)
