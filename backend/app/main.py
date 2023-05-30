from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api import api_router
from app.settings import STATIC_BASE_DIR, STATIC_BASE_URI, DEBUG


app = FastAPI(
    debug=DEBUG,
    title='Backend "SaP"',
    description='Бэкенд сайта "Share a Project"',
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение статики
app.mount(
    STATIC_BASE_URI,
    StaticFiles(directory=STATIC_BASE_DIR),
    name="static",
)

# Подключение роутов
app.include_router(api_router, prefix='/api/v1')
