import requests
import pytest
import allure

from constants import *
from helpers.data_gen import *


class TestLoginUser:
    @allure.title('Проверка успешной авторизации пользователя')
    def test_login_succesfull(self, user):
        """
        Регистрируем пользователя, выходим и отправляем запрос на авторизацию.
        """
        payload = {
            "email": user.email,
            "password": user.password
        }
        user.logout()
        log = requests.post(Url.LOGIN, data=payload)

        assert log.json()['success'] == True

    @pytest.mark.parametrize('key', ["email", "password"])
    @allure.title('Проверка авторизации с неверным логином и паролем')
    def test_incorrect_login(self, user_class_logout, key):
        """
        Регистрируем пользователя, выходим и отправляем запросы меняя одно из полей.
        """
        payload = {
            "email": user_class_logout.email,
            "password": user_class_logout.password
        }
        wrong = create_incorrect_field(payload, key)
        log = requests.post(Url.LOGIN, data=wrong)
        assert log.status_code == 401
        assert log.json()['message'] == "email or password are incorrect"
