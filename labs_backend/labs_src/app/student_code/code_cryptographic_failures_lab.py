import jwt

from fastapi import Request, HTTPException, status
from app.core.config import SECRET_KEY
from app.core.models import User

# tested by /app/tests/test_cryptographic_failures_lab.py

'''
Fix the functions 'encode_user' and 'decode_user'.
You should use algorithm "HS256" and verify jwt-tokens by SECRET_KEY from app.core.config.
Payload should contain {"username": "<username>"}.
'''

def encode_user(user: User) -> str:
    return jwt.encode({"username": user.username}, key=None, algorithm="none")


def decode_user(request: Request) -> dict:
    auth_header = request.headers.get('Authorization')

    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(token, options={"verify_signature": False})
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    return payload
