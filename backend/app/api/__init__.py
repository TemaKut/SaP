from fastapi import APIRouter

from .users import users_router


api_router = APIRouter()

# Подключение роутов
api_router.include_router(users_router)
