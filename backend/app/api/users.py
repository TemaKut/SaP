from fastapi import APIRouter, Depends, Body, status

from app.users.auth import get_current_user
from app.users.crud import UsersCRUD
from app.users.models import User
from app.users.schemas import (
    UserCreate,
    UserRepresentation,
    TokenCreate,
    TokenRepresentation,
)


users_router = APIRouter(
    prefix='/users',
    tags=['Взаимодействие с пользователями']
)


@users_router.post(
    '/register',
    name='register',
    status_code=status.HTTP_201_CREATED,
    response_model=TokenRepresentation,
    responses={
        400: {'description': 'User alredy exists or validation errors'},
    }
)
async def register_user(
    data: UserCreate = Body(),
    crud: UsersCRUD = Depends(),
):
    """ Регистрация пользователя. """

    return await crud.create_user(data)


@users_router.post(
    '/get-token',
    name='get-token',
    status_code=status.HTTP_200_OK,
    response_model=TokenRepresentation,
    responses={
        400: {'description': 'Incorrect password'},
        404: {'description': 'Incorrect email or user not found'},
    }
)
async def get_token(
    data: TokenCreate = Body(),
    crud: UsersCRUD = Depends(),
):
    """ Получить токен пользователя. """

    return await crud.get_token(data)


@users_router.get(
    '/',
    name='get-all-users',
    status_code=status.HTTP_200_OK,
    response_model=list[UserRepresentation],
)
async def get_all_users(
    crud: UsersCRUD = Depends(),
):
    """ Получить список всех пользователей. """

    return await crud.get_all_users()


@users_router.get(
    '/me',
    name='get-info-about-me',
    status_code=status.HTTP_200_OK,
    response_model=UserRepresentation,
    responses={
        404: {'description': 'User not found'},
        401: {'description': 'Error with authorization'},
    }
)
async def get_info_about_me(user: User = Depends(get_current_user)):
    """ Получить информацию о пользователе сделавшем запрос. """

    return user


@users_router.get(
    '/{username}',
    name='get-user-by-username',
    status_code=status.HTTP_200_OK,
    response_model=UserRepresentation,
    responses={
        404: {'description': 'User not found'},
    }
)
async def get_user_by_username(
    username: str,
    crud: UsersCRUD = Depends(),
):
    """ Получить пользователя по username. """

    return await crud.get_user_by_username(username)
