items = [
    {
        "name": f"item{i}",
        "description": f"description{i}",
        "released": i % 2,
        "id": i
    }
    for i in range(1, 6)
]

users = [
    {
        "username": f"test_user{i}",
        "password": f"hashed_test_password{i}",
        "id": i
    }
    for i in range(1, 6)
]

