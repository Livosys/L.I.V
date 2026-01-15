_revoked = set()

def revoke(jti: str):
    _revoked.add(jti)

def is_revoked(jti: str) -> bool:
    return jti in _revoked
