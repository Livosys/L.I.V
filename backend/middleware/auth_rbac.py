from fastapi import Header, HTTPException

def require_role(required_role: str):
    """
    Dependency – körs endast när endpoint anropas
    Aldrig vid import
    """
    def checker(x_role: str | None = Header(default=None)):
        if x_role != required_role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return True

    return checker
