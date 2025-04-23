from fastapi import Request, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.models import User

# tested by /app/tests/test_broken_access_control_lab.py

'''
Write the function 'is_owner' that fetch token from 'Authentication' header and
check if the user has the same id as the argument 'user_id'.
Check test file /app/tests/test_broken_access_control_lab.py for required token format and error messages.
'''


def is_owner(user_id: int):
    pass
