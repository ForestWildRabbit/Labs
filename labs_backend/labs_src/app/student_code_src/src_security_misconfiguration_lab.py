import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from app.core.data import ADMIN_USERNAME, ADMIN_PASSWORD

# tested by /app/tests/test_security_misconfiguration_lab.py

'''
Securing automatically generated docs (/docs, and /openapi.json) is important, 
especially in production, where exposing your API schema can aid attackers.
Write function taking HTTPBasicCredentials and compare with <ADMIN_USERNAME> and <ADMIN_PASSWORD>.
So only admin can access API Docs.
'''


def verify_admin_credentials() -> bool:
    pass
