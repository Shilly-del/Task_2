import requests
import pytest
import allure

from apios.user import *
from constants import *


class TestRegisterUser:
    @allure.title('Проверка успешной регистрации пользователя')
    def test_register_succesfull(self):
        """
        Регистрируем пользователя, проверяем тело ответа.
        """
        user = User()

        reg = requests.post(Url.REGISTER_USER, data=user.payload)
        user.token = f'{reg.json()['accessToken']}'
        user.headers = {'authorization': user.token}
        assert reg.json()['success'] == True

        # удаление созданной записи после теста
        user.clear()

    @allure.title('Проверка повторной регистрации пользователя')
    def test_repeat_register(self):
        """
        Регистрируем пользователя, отправляем новый запрос с теми же данными.
        """
        user = User()
        payload = user.payload
        reg = requests.post(Url.REGISTER_USER, data=payload)
        user.token = f'{reg.json()['accessToken']}'
        reg = requests.post(Url.REGISTER_USER, data=payload)

        assert reg.status_code == 403
        assert reg.json()['success'] == False

        # удаление созданной записи после теста
        user.clear()

    @allure.title('Проверка регистрации пользователя без заполнения обязательных полей')
    @pytest.mark.parametrize('payload', TestUser.EMPTY_FIELD)
    def test_register_without_data(self, payload):
        """
        Проводим попытку регистрации пользователя без заполнения логина или пароля, проверяем код и сообщение ответа
        """

        reg = requests.post(Url.REGISTER_USER, data=payload)

        assert reg.status_code == 403
        assert reg.json()[
            "message"] == "Email, password and name are required fields"
