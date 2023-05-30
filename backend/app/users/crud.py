from fastapi import Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update, and_, inspect

from app.logs.logger import log
from app.database.base import get_async_session
from .models import User
from .auth import create_token
from .schemas import (
    UserCreate,
    UserPatch,
    UserRepresentation,
    TokenCreate,
    TokenRepresentation,
)


class UsersCRUD():
    """ CRUD операции с пользователями. """

    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        """ Инициализация объекта класса. """
        self.session = session

    async def create_user(self, data: UserCreate) -> TokenRepresentation:
        """ Создать пользователя в БД """
        new_user = User(**data.dict())
        self.session.add(new_user)

        try:
            await self.session.commit()
            await self.session.refresh(new_user)

        except IntegrityError as e:
            log.error(f'User not created. {e}')
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                'User alredy exists.',
            )

        return await create_token(new_user)

    async def get_token(self, data: TokenCreate) -> TokenRepresentation:
        """ Получить токен пользователя. """
        # Превратить данные в словарь и вырезать пароль
        data = data.dict()
        query_password = data.pop('password')

        # Получить пользователя. В случае отсутствия - ошибка
        user = await self._get_user_by_params(data)

        # Верификация пароля с хэшем в БД. В случае несовпадения - ошибка
        user.verify_password(query_password)

        return await create_token(user)

    async def get_all_users(self) -> list[User]:
        """ Получить список всех пользователей из БД """
        query = select(User)
        result = await self.session.execute(query)

        return result.scalars().unique().all()

    async def get_user_by_username(self, username: str) -> User:
        """ Получить пользователя из БД по его username """
        user = await self._get_user_by_params({'username': username})

        return user

    async def change_user_data(
        self, user: User, data: UserPatch
    ) -> UserRepresentation:
        """ Изменить одно или несколько полей у пользователя в БД """

        for key, value in data.dict().items():

            if value:
                setattr(user, key, value)

        await self.session.commit()
        await self.session.refresh(user)

        return user

    async def _get_user_by_params(self, params: dict) -> User:
        """ Получить пользователя из БД по параметрам. """
        query = select(User).filter_by(**params)
        result = await self.session.execute(query)

        user = result.scalars().unique().first()

        if not user:

            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                'User not found.'
            )

        return user
