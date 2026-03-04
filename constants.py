class Url:
    BASE = 'https://stellarburgers.education-services.ru/api'
    REGISTER_USER = f'{BASE}/auth/register'
    LOGOUT = f'{BASE}/auth/logout'
    LOGIN = f'{BASE}/auth/login'
    AUTH_USER = f'{BASE}/auth/user'
    ORDERS = f'{BASE}/orders'
    INGREDIENTS = f'{BASE}/ingredients'


class TestUser:
    EMPTY_FIELD = [
        {
            "email": "",
            "password": "password",
            "name": "Vasilevs"},
        {
            "email": "Vasya03032026@mail.ru",
            "password": "",
            "name": "Vasilevs"
        },
        {
            "email": "Vasya03032026@mail.ru",
            "password": "password",
            "name": ""
        }
    ]
    INCORRECT_FIELD = [
        {
            "email": "Vasya03032026@mail.ru",
            "password": "password"}
    ]
