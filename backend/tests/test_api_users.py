import json

import pytest
from httpx import AsyncClient
from fastapi import status

from app.main import app
from .utils import create_user, is_user_in_db


@pytest.mark.parametrize(
    'data, status_code',
    [
        (
            {
                "username": "Test_user",
                "email": "test@yandex.ru",
                "password": "string"
            },
            status.HTTP_201_CREATED,
        ),
        (
            {
                "username": "Test_user",
                "email": "ar@r",
                "password": "string"
            },
            status.HTTP_400_BAD_REQUEST,
        ),
        (
            {
                "username": "Test_user",
                "email": "NOTEMAIL",
                "password": "string"
            },
            status.HTTP_400_BAD_REQUEST,
        ),
        (
            {
                "username": "Ar",
                "email": "test@yandex.ru",
                "password": "string"
            },
            status.HTTP_400_BAD_REQUEST,
        ),
        (
            {},
            status.HTTP_422_UNPROCESSABLE_ENTITY,
        ),
    ],
)
async def test_create_user(
    client: AsyncClient,
    data,
    status_code,
):
    """ Тест эндпоинта создания пользователя. """
    uri = app.url_path_for('register')
    response = await client.post(uri, json=data)

    assert response.status_code == status_code


async def test_get_token_after_registration(client):
    """ После регистрации пользователя - в ответе должен быть токен. """
    data = {
        "username": "Test_user",
        "email": "test@yandex.ru",
        "password": "string"
    }

    uri = app.url_path_for('register')
    response = await client.post(uri, json=data)

    assert response.status_code == status.HTTP_201_CREATED

    response_dict = json.loads(response.text)

    assert response_dict.get('token')
    assert response_dict.get('token_type')


@pytest.mark.parametrize(
    'data_token, status_code',
    [
        (
            {
                "email": "temakutuzzzov@yandex.ru",
                "password": "string"
            },
            status.HTTP_200_OK,
        ),
        (
            {
                "email": "uncorrectemail@yandex.ru",
                "password": "string"
            },
            status.HTTP_404_NOT_FOUND,
        ),
        (
            {
                "email": "temakutuzzzov@yandex.ru",
                "password": "uncorrectpassword"
            },
            status.HTTP_400_BAD_REQUEST,
        ),
    ],
)
async def test_get_token_for_registred_user(
    client,
    data_token,
    status_code,
):
    """
    Тест эндпоинта получения токена для зарегистрированного пользователя
    """
    data_register = {
        "username": "string",
        "email": "temakutuzzzov@yandex.ru",
        "password": "string"
    }
    user = await create_user(data_register)
    assert await is_user_in_db({'id': user.id})

    uri = app.url_path_for('get-token')
    response = await client.post(uri, json=data_token)

    assert response.status_code == status_code


async def test_get_all_users(client):
    """ Тест эндпоинта получения списка всех пользователей. """
    n_users = 10

    # Создать в БД n пользователей
    for i in range(n_users):
        data_register = {
            "username": f"test_user{i}",
            "email": f"temakutuzzzov{i}@yandex.ru",
            "password": "string"
        }
        user = await create_user(data_register)
        assert await is_user_in_db({'id': user.id})

    uri = app.url_path_for('get-all-users')
    response = await client.get(uri)

    assert response.status_code == status.HTTP_200_OK

    response_list = json.loads(response.text)
    assert len(response_list) == n_users


async def test_get_user_by_username(client):
    """ Тест эндпоинта получения пользователя по username """

    # Создать в БД 3 пользователя
    for i in range(3):
        data_register = {
            "username": f"test_user{i}",
            "email": f"temakutuzzzov{i}@yandex.ru",
            "password": "string"
        }
        user = await create_user(data_register)
        assert await is_user_in_db({'id': user.id})

    uri = app.url_path_for('get-all-users')
    response = await client.get(uri + 'test_user1')

    assert response.status_code == status.HTTP_200_OK


async def test_get_user_by_username_404_error(client):
    """ Тест эндпоинта получения пользователя по username """
    uri = app.url_path_for('get-all-users')
    response = await client.get(uri + 'nonexistentusername')

    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_get_info_about_me(client):
    """ Тестирование получения информации о пользователе сделавшем запрос """
    # Создать иного пользователя
    data_not_me = {
        "username": "test_user_not_me",
        "email": "test_user_not_me@yandex.ru",
        "password": "string"
    }
    user_not_me = await create_user(data_not_me)
    assert await is_user_in_db({'id': user_not_me.id})

    # Создать пользователя о котором будем получать информацию
    data_me = {
        "username": "its_my_username",
        "email": "its_my_email@yandex.ru",
        "password": "string"
    }
    user_me = await create_user(data_me)
    assert await is_user_in_db({'id': user_me.id})

    # Получить токен нужного пользователя через эндпоинт
    uri = app.url_path_for('get-token')
    response = await client.post(uri, json=data_me)
    assert response.status_code == status.HTTP_200_OK

    response_dict = json.loads(response.text)
    token = response_dict.get('token')
    token_type = response_dict.get('token_type')

    assert all([token, token_type])

    # Запрос на эндпоинт получения информации о себе без токена
    uri = app.url_path_for('get-info-about-me')
    response = await client.get(uri)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # Запрос на эндпоинт получения информации о себе с токеном
    auth_header = {'Authorization': f'{token_type} {token}'}
    response = await client.get(uri, headers=auth_header)
    assert response.status_code == status.HTTP_200_OK

    response_dict = json.loads(response.text)
    assert response_dict.get('username') == 'its_my_username'
