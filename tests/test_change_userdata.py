import requests
import pytest
import allure

from apios.user import *
from constants import *
from helpers.data_gen import *


class TestChangeUserData:

    @allure.title('Cценарий изменения данных пользователя с успешной авторизацией')
    @pytest.mark.parametrize('key', ["email", "password", "name"])
    def test_change_user_data_succesful(self, user_class, key):
        """
        Регистрируем пользователя, меняем его данные и отправляем запрос на сохранение.
        """

        change = change_field(user_class.payload, key)

        pat = requests.patch(Url.AUTH_USER, data=change,
                             headers=user_class.headers)
        assert pat.status_code == 200
        assert pat.json()['success'] == True

    @allure.title('Cценарий изменения данных пользователя без авторизации')
    @pytest.mark.parametrize('key', ["email", "password", "name"])
    def test_change_userdata_unautorised(self, user_class, key):
        """
        Регистрируем пользователя, меняем его данные и отправляем запросы
        без заголовка авторизации.
        """

        change = change_field(user_class.payload, key)

        pat = requests.patch(Url.AUTH_USER, data=change)
        assert pat.status_code == 401
        assert pat.json()['message'] == "You should be authorised"
