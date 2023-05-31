from fastapi import APIRouter

from .users import users_router
from .projects import projects_router


api_router = APIRouter()

# Подключение роутов
api_router.include_router(users_router)
api_router.include_router(projects_router)
