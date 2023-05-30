import string
import os

from fastapi import HTTPException, status
import sqlalchemy as sa
from sqlalchemy.sql import func
from sqlalchemy.orm import validates
from passlib.hash import bcrypt

from app.database.base import Base
from app.logs.logger import log
from app.settings import STATIC_BASE_URI


class User(Base):
    """ Модель пользователя в БД. """

    __tablename__ = 'users'

    id = sa.Column(
        sa.Integer,
        primary_key=True,
        comment='Id пользователя',
    )
    logo = sa.Column(
        sa.String,
        nullable=False,
        default=os.path.join(STATIC_BASE_URI, 'users', 'DefaultUserLogo.png'),
        comment="Uri на логотип пользователя"
    )
    username = sa.Column(
        sa.String(100),
        unique=True,
        nullable=False,
        comment='Псеводним',
    )
    email = sa.Column(
        sa.String(100),
        unique=True,
        nullable=False,
        comment='Email пользователя',
    )
    password = sa.Column(
        sa.Text,
        nullable=False,
        comment='Хэш пароля',
    )
    registred_at = sa.Column(
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        comment='Дата и время регистрации пользователя.',
    )
    is_active = sa.Column(
        sa.Boolean,
        nullable=False,
        default=True,
        comment='Флаг активен ли пользователь.',
    )

    def verify_password(self, password: str):
        """ Верификация пароля. """

        if not bcrypt.verify(password, self.password):
            log.error('Incorrect password')

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Incorrect password',
            )

    @validates('email')
    def email_validate(self, key, value: str):
        """ Валидация поля email. """

        if len(value) < 7:
            log.error('Invalid email by length')
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                'Invalid email. Have to be longer then 6 characters',
            )

        if ('@' not in value) or ('.' not in value):
            log.error('Invalid email by @.')
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                'Invalid email. Email have to contains @ and .',
            )

        for ch in value:

            if ch not in f'{string.ascii_letters}@.1234567890':
                log.error('Invalid email by symbols')
                raise HTTPException(
                    status.HTTP_400_BAD_REQUEST,
                    'Invalid email. Email contains another special characters',
                )

        return value

    @validates('username')
    def username_validate(self, key, value: str):
        """ Валидация поля username. """

        if len(value) < 5:
            log.error('Invalid username by length')
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                'Username have to be longer then 4 symbols',
            )

        for ch in value:

            if ch not in f"{string.ascii_letters}1234567890":
                log.error('Invalid username by symbols')
                raise HTTPException(
                    status.HTTP_400_BAD_REQUEST,
                    'Username have to contains eng. characters only!',
                )

        return value

    @validates('password')
    def password_validate(self, key, value: str):
        """ Хэширование пароля. """

        if len(value) < 7:
            log.error('Invalid password by length')
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                'Password have to be longer then 6 symbols',
            )

        return bcrypt.hash(value)

    def __repr__(self) -> str:
        """ Строчное представление пользователя. """

        return f'{self.__class__.__name__}<id={self.id}>'
