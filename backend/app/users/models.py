from fastapi import HTTPException, status
import sqlalchemy as sa
from sqlalchemy.sql import func
from sqlalchemy.orm import validates
from passlib.hash import bcrypt

from app.database.base import Base
from app.logs.logger import log


class User(Base):
    """ Модель пользователя в БД. """

    __tablename__ = 'users'

    id = sa.Column(
        sa.Integer,
        primary_key=True,
        comment='Id пользователя',
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
        if not (('@' in value) and (len(value) > 5)):
            log.error('Invalid email')
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Invalid email')

        return value

    @validates('username')
    def username_validate(self, key, value: str):
        """ Валидация поля email. """
        if len(value) < 3:
            log.error('Invalid username')
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Username < 3')

        return value

    @validates('password')
    def password_validate(self, key, value: str):
        """ Хэширование пароля. """

        return bcrypt.hash(value)

    def __repr__(self) -> str:
        """ Строчное представление пользователя. """

        return f'{self.__class__.__name__}<id={self.id}>'
