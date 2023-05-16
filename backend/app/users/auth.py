from datetime import datetime, timedelta

from fastapi import Request, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from jose import jwt, JWTError

from app.settings import SECRET_KEY, JWT_ALGORITHM, JWT_EXPIRE_MIN
from app.database.base import get_async_session
from app.logs.logger import log
from .models import User
from .schemas import TokenRepresentation


async def create_token(user: User) -> TokenRepresentation:
    """ Создать токен для пользователя. """
    assert isinstance(user, User), 'Not a User class'

    now = datetime.utcnow()
    token_data = {
        "iat": now,
        "exp": now + timedelta(minutes=JWT_EXPIRE_MIN),
        'user_id': user.id,
    }

    # Кодирование данных в токен
    token = jwt.encode(
        token_data,
        key=SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )

    return TokenRepresentation(token=token)


async def get_current_user(
    request: Request,
    session: AsyncSession = Depends(get_async_session),
) -> User:
    """ Получить объект пользователя из БД, выполневшего запрос. """
    error = HTTPException(status.HTTP_401_UNAUTHORIZED, 'Not authorized.')

    # Получение токена авторизации из запроса
    try:
        token = request._headers.get('authorization').split(' ')[1]

    except Exception as e:
        log.error(f'Authorization required. {e}')
        raise error

    # Расшифровка токена
    try:
        token_data = jwt.decode(token, SECRET_KEY, [JWT_ALGORITHM])

    except JWTError as e:
        log.error(f'Invalid token {e}')
        raise error

    try:
        user_id = token_data['user_id']

        query = select(User).where(User.id == user_id)
        result = await session.execute(query)
        user = result.scalars().first()

        if not user:
            raise

    except Exception as e:
        log.error(f'Cant get user from DB {e}')
        raise error

    return user
