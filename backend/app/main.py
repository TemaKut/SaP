from fastapi import FastAPI

from app.api import api_router


app = FastAPI(
    debug=True,
    title='Backend "SaP"',
    description='Бэкенд сайта "Share a Project"',
)

# Подключение роутов
app.include_router(api_router, prefix='/api/v1')
