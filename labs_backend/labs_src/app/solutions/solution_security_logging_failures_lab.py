from fastapi import HTTPException

from app.core.schemas import UserAuthMFA


def simulate_mfa_authentication(user: UserAuthMFA, mfa_username, mfa_password, mfa_token):
    if user.username != mfa_username or user.password != mfa_password or user.totp_token != mfa_token:
        raise HTTPException(status_code=400, detail="Wrong credentials")

    return {'status': 'authenticated'}