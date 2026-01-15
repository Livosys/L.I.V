import os
import jwt
import requests
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

TENANT_ID = os.getenv("AZURE_TENANT_ID")
CLIENT_ID = os.getenv("AZURE_CLIENT_ID")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
JWKS_URL = f"{AUTHORITY}/discovery/v2.0/keys"

security = HTTPBearer()
_jwks = None

def get_jwks():
    global _jwks
    if _jwks is None:
        _jwks = requests.get(JWKS_URL).json()
    return _jwks

def verify_jwt(token: str):
    try:
        unverified_header = jwt.get_unverified_header(token)
        jwks = get_jwks()

        key = next(
            k for k in jwks["keys"]
            if k["kid"] == unverified_header["kid"]
        )

        public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)

        payload = jwt.decode(
            token,
            public_key,
            algorithms=["RS256"],
            audience=CLIENT_ID,
            issuer=f"{AUTHORITY}/v2.0"
        )

        return payload

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token: {str(e)}"
        )

def require_role(required_role: str):
    def _role_guard(
        creds: HTTPAuthorizationCredentials = Depends(security)
    ):
        payload = verify_jwt(creds.credentials)
        roles = payload.get("roles", [])

        if required_role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient role"
            )

        return payload

    return _role_guard
