from functools import wraps
import json

from fastapi import status
from sqlalchemy import select
from httpx import AsyncClient

from app.users.models import User
from app.main import app
from .conftest import Session


def add_session_in_params(function):
    """ Декоратор. Добавляет объект сессии БД в аргументы """

    @wraps(function)
    async def wrapper(*args, **kwargs):
        """ Обёртка функции. """
        db_sesion = Session()
        result = await function(db_sesion, *args, **kwargs)
        await db_sesion.close()

        return result

    return wrapper


@add_session_in_params
async def is_user_in_db(session, user_data: dict) -> bool:
    """ Проверить есть ли пользователь в БД. """
    query = select(User).filter_by(**user_data)
    result = await session.execute(query)

    user = result.scalars().unique().first()

    return user


@add_session_in_params
async def create_user(session, data: dict) -> User:
    """ Создать пользователя напрямую через БД. """
    new_user = User(**data)

    session.add(new_user)

    await session.commit()
    await session.refresh(new_user)

    return new_user


@add_session_in_params
async def get_token(session, client: AsyncClient, data: dict) -> dict:
    """ Получить токен для пользователя. """
    uri = app.url_path_for('get-token')
    response = await client.post(uri, json=data)

    assert response.status_code == status.HTTP_200_OK

    response_dict = json.loads(response.text)

    token = response_dict.get('token')
    token_type = response_dict.get('token_type')

    assert all([token, token_type])

    return (token, token_type)
