from app.core.utils import scan_most_common_passwords, generate_totp
from random import choice

ITEMS_COUNT = 10
USERS_COUNT = 5

items = [
    {
        "name": f"item{i}",
        "description": f"description{i}",
        "released": i % 2,
        "id": i,
    }
    for i in range(1, ITEMS_COUNT + 1)
]

users = [
    {
        "username": f"test_user{i}",
        "password": f"hashed_test_password{i}",
        "id": i
    }
    for i in range(1, USERS_COUNT + 1)
]

ADMIN_USERNAME = "test_admin"
ADMIN_PASSWORD = "test_admin_password"

most_common_passwords = scan_most_common_passwords()

mfa_password = choice(most_common_passwords)
mfa_token = generate_totp()

