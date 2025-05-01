import jwt

from fastapi import Request, HTTPException, status
from app.core.config import SECRET_KEY
from app.core.models import User


def encode_user(user: User) -> str:
    return jwt.encode({"username": user.username}, key=SECRET_KEY, algorithm="HS256")


def decode_user(request: Request) -> dict:
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing"
        )

    if not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token format"
        )

    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(
            token,
            key=SECRET_KEY,
            algorithms=["HS256"],
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    return payload
