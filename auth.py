from fastapi import Header, HTTPException, status
import secrets

import os

# in production, you add this in .env
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("PRODUCTION ERROR: API_KEY environment variable is not set!")

def verify_api_key(x_api_key: str = Header(..., description="API Key for route authentication")):
    """
    Securely validates the incoming X-API-Key header using constant-time comparison
    to prevent timing attacks.
    """
    # secrets.compare_digest mitigates timing side-channel attacks
    is_valid = secrets.compare_digest(x_api_key, API_KEY)

    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key"
        )
    return x_api_key

