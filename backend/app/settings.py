import os
from pathlib import Path


# Корневая директория
BASE_DIR = Path(__file__).resolve().parent

# Настройка статики
STATIC_BASE_DIR = os.path.join(BASE_DIR, 'static')
STATIC_BASE_URI = '/static'

# TODO: Вынести все константы в .ENV
# Секретный ключ приложения
SECRET_KEY: str = os.getenv('SECRET_KEY')

# Подключение к БД
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_URL = (
    "postgresql+asyncpg://"
    + f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Подключение к БД (Для тестирования!)
DB_USER_TEST = os.getenv("DB_USER_TEST")
DB_PASSWORD_TEST = os.getenv("DB_PASSWORD_TEST")
DB_NAME_TEST = os.getenv("DB_NAME_TEST")
DB_HOST_TEST = os.getenv("DB_HOST_TEST")
DB_PORT_TEST = os.getenv("DB_PORT_TEST")
DB_URL_TEST = (
    "postgresql+asyncpg://"
    + f"{DB_USER_TEST}:{DB_PASSWORD_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}"
    + f"/{DB_NAME_TEST}"
)

# Параметры JWT
JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM')
JWT_EXPIRE_MIN: int = int(os.getenv('JWT_EXPIRE_MIN'))
