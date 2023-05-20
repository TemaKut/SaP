from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router


app = FastAPI(
    debug=True,
    title='Backend "SaP"',
    description='Бэкенд сайта "Share a Project"',
)

# Подключение роутов
app.include_router(api_router, prefix='/api/v1')

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
