import os
from pathlib import Path


# Корневая директория
BASE_DIR = Path(__file__).resolve().parent

# TODO: Вынести все константы в .ENV
# Секретный ключ приложения
SECRET_KEY: str = os.getenv('SECRET_KEY', 'SomeSuperSecretKey')

# Подключение к БД
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_URL = (
    "postgresql+asyncpg://"
    + f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Подключение к БД (Для тестирования!)
DB_USER_TEST = os.getenv("DB_USER_TEST", "postgres_test")
DB_PASSWORD_TEST = os.getenv("DB_PASSWORD_TEST", "postgres_test")
DB_NAME_TEST = os.getenv("DB_NAME_TEST", "postgres_test")
DB_HOST_TEST = os.getenv("DB_HOST_TEST", "localhost")
DB_PORT_TEST = os.getenv("DB_PORT_TEST", 5433)
DB_URL_TEST = (
    "postgresql+asyncpg://"
    + f"{DB_USER_TEST}:{DB_PASSWORD_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}"
    + f"/{DB_NAME_TEST}"
)

# Параметры JWT
JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM', 'HS256')
JWT_EXPIRE_MIN: int = os.getenv('JWT_EXPIRE_MIN', 10_000)
