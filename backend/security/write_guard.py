READ_ONLY_MODE = True

def ensure_write_allowed():
    if READ_ONLY_MODE:
        raise PermissionError("WRITE operations are disabled (READ-ONLY MODE)")
