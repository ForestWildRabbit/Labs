from fastapi import HTTPException

from app.core.schemas import UserAuthMFA

# tested by /app/tests/test_security_logging_failures_lab.py

"""
Responses must not contain any sensitive information, that can help hackers.
In this example client will be aware exactly what sensitive data is incorrect.
This function simulates MFA authentication with username, password and totp (Time-based One-Time Password).
Let's say in this example user's password is the one of the most common passwords.
File is located at /app/static/tables/common_passwords.csv and contains 10000 passwords.
In that case totp contains 4 digits, enumeration will take 10000 times.
Totp usually exists 30 seconds, totp enumeration will take less 30 seconds, so it's possible.
The task is to make user's credentials enumeration instead of 20000 times (10000 + 10000), 
to 100_000_000 times (10000 * 10000). 
With totp changing every 30 seconds it's impossible to enumerate 100_000_000 times in 30 seconds.
"""


def simulate_mfa_authentication(user: UserAuthMFA, mfa_username, mfa_password, mfa_token):
    if user.username != mfa_username:
        raise HTTPException(status_code=400, detail="User not found")
    if user.password != mfa_password:
        raise HTTPException(status_code=400, detail="Wrong password")
    if user.totp_token != mfa_token:
        raise HTTPException(status_code=400, detail="Wrong totp")

    return {'status': 'authenticated'}
