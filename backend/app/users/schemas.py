from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    """ Поля для создания пользователя. """

    username: str
    email: str
    password: str


class UserRepresentation(BaseModel):
    """ Представление пользователя. """

    id: int
    logo: str
    username: str
    email: str
    registred_at: datetime
    is_active: bool

    class Config:
        orm_mode = True


class TokenCreate(BaseModel):
    """ Необходимые данные для создания токена. """

    email: str
    password: str


class TokenRepresentation(BaseModel):
    """ Представление токена пользователя. """

    token: str
    token_type: str = 'Bearer'
