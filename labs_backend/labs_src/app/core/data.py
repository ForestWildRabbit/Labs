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

