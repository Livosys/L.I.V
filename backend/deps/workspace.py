from fastapi import Depends
from security.jwt_guard import require_role

def get_workspace_id(user=Depends(require_role("agent"))):
    return user["workspace_id"]
