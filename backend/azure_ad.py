import requests, jwt
from fastapi import HTTPException, Header

TENANT_ID = "YOUR_TENANT_ID"
CLIENT_ID = "YOUR_CLIENT_ID"
JWKS_URL = f"https://login.microsoftonline.com/{TENANT_ID}/discovery/v2.0/keys"

jwks = requests.get(JWKS_URL).json()

def verify_azure_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")

    token = authorization.replace("Bearer ", "")
    header = jwt.get_unverified_header(token)
    key = next(k for k in jwks["keys"] if k["kid"] == header["kid"])
    payload = jwt.decode(
        token,
        jwt.algorithms.RSAAlgorithm.from_jwk(key),
        audience=CLIENT_ID,
        algorithms=["RS256"]
    )
    return payload
