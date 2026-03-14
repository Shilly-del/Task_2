import requests
import allure

from constants import Url
from helpers.data_gen import *


class User:

    @allure.step('Создание пользователя')
    def __init__(self):
        self.email = f'{generate_random_string(7)}@gmail.com'
        self.password = generate_random_string(10)
        self.name = generate_random_string(7)

        self.payload = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }

    @allure.step('Регистрация пользователя')
    def register_user(self):
        r = requests.post(Url.REGISTER_USER, data=self.payload)
        self.token = r.json()['accessToken']
        self.headers = {'authorization': self.token}

    @allure.step('Удаление пользователя')
    def clear(self):
        headers = {'authorization': self.token}
        r = requests.delete(Url.AUTH_USER, headers=headers)

    @allure.step('Логаут')
    def logout(self):
        headers = {'authorization': self.token}
        r = requests.post(Url.LOGOUT, headers=headers)

    @allure.step('Авторизация')
    def login(self):
        payload = {
            "email": self.email,
            "password": self.password
        }
        r = requests.post(Url.LOGIN, data=payload)
        self.token = r.json()['accessToken']

    @allure.step('Получение доступных ингредиентов')
    def get_ingredients(self):
        r = requests.get(Url.INGREDIENTS)
        self.ingredients = r.json()
