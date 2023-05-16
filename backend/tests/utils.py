from functools import wraps

from sqlalchemy import select

from app.users.models import User
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
async def create_user(session, data: dict) -> User:
    """ Создать пользователя напрямую через БД. """
    new_user = User(**data)

    session.add(new_user)

    await session.commit()
    await session.refresh(new_user)

    return new_user


@add_session_in_params
async def is_user_in_db(session, user_data: dict) -> bool:
    """ Проверить есть ли пользователь в БД. """
    query = select(User).filter_by(**user_data)
    result = await session.execute(query)

    user = result.scalars().unique().first()

    return user
