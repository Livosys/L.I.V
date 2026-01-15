from fastapi import Header, HTTPException
import jwt, os

PUBLIC_KEY = os.environ.get("AZURE_AD_PUBLIC_KEY","")

def require_scope(scope: str):
    def checker(authorization: str = Header(None)):
        if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing token")
        token = authorization.split(" ",1)[1]
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"], options={"verify_aud": False})
        scopes = payload.get("scp","").split()
        if scope not in scopes:
            raise HTTPException(status_code=403, detail="Missing scope")
        return payload
    return checker
