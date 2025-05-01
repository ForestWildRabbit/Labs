
from fastapi import FastAPI
from app.core.routers import items_router, users_router, jwt_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)
app.include_router(jwt_router)


