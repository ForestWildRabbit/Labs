import jwt

from fastapi import Request, HTTPException, status
from app.core.config import SECRET_KEY
from app.core.models import User

# tested by /app/tests/test_cryptographic_failures_lab.py

'''
There is an example of unsafe jwt authentication, it accepts generated tokens.
Fix the functions 'encode_user' and 'decode_user' to pass the tests.
You should use algorithm "HS256" and verify jwt-tokens by SECRET_KEY from "app.core.config".
Authorization header format "Authorization: Bearer <token>"
Payload must contain {"username": "<username>"}.
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
