READ_ONLY = True

def ensure_read_only():
    if READ_ONLY:
        return True
    raise RuntimeError("Write operations are disabled in production")
